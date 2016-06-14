## Week5

### Lecture 5.1: Parallel Computation Patterns - Histogramming 

To learn the parallel histogram computation pattern:

 - threads will interference when they write into their outputs

#### Histogramming

 - A method for extracting notable features and patterns from large data sets
    - Feature extraction for object recognition in images 
    - Fraud detection in credit card transactions
    - ...
 - Basic histograms - for each element in the data set, use the value to identify a “bin” to increment.

#### A Histogram Example

 - In sentence “Programming Massively Parallel Processors” build a histogram of frequencies of each letter
 - A(4), C(1), E(1), G(1), …

 - How can we do this in parallel?
    - Have each thread to take a section of the input
    - For each input letter, use atomic operations to build the histogram

#### Iteration #1 – 1st letter in each section

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/histo_step1.png)
     
      
### Lecture 5.2: Parallel Computation Patterns - Atomic Operations 

 - To understand atomic operations
    - Read-modify-write in parallel computation
    - Race conditions when performing read-modifywrite

#### A Common Parallel Coordination Pattern

 - Multiple bank tellers出纳员 count the total amount of cash in the safe
 - Each grab a pile and count
 - Have a central display of the running total
 - Whenever someone finishes counting a pile, add the subtotal of the pile to the running total
    - read the original total,  add the subtotal, write to the original total 
 - A bad outcome
    - Some of the piles were not accounted for 

#### Atomic Operations

If Mem[x] was initially 0, what would the value of Mem[x] be after threads 1 and 2 have completed?

 - What does each thread get in their Old variable?

The answer may vary due to data races. To avoid data races, you should use atomic operations.



### Lecture 5.3: Parallel Computation Patterns - Atomic Operations in CUDA 

#### Atomic Operations in General

 - Performed by a **single instruction** on a memory location address
    - Read the old value, calculate a new value, and write the new value to the location 
 - The hardware ensures that no other threads can access the location until the atomic operation is complete
    - Any other threads that access the location will typically be held in a queue until its turn
    - All threads perform the atomic operation serially if they modify the same location

#### Atomic Operations in CUDA

 - Function calls that are translated into single instructions (a.k.a. intrinsic functions or intrinsics)
    - Atomic add, sub, inc, dec, min, max, exch (exchange), CAS (compare and swap)
    - Read CUDA C programming Guide 4.0 or later for details

 - Atomic Add
    - int atomicAdd(int* address, int val)
    - reads the 32-bit word old pointed to by address in **global** or **shared** memory, 
    - computes (old + val), and stores the result back to memory at the same address. 
    - The function returns old.
    
#### More Atomic Adds in CUDA

 - Unsigned 32-bit integer atomic add
    - unsigned int atomicAdd(unsigned int* address, unsigned int val); 
 - Unsigned 64-bit integer atomic add
    - unsigned long long int atomicAdd( ... );  
 - Single-precision floating-point atomic add (capability > 2.0)
    - float atomicAdd(float* address, float val);  

#### Uncoalesced memory accesses in Sectoned Histogram Algorithm 

分区域直方图算法中的 非联合内存访问

 - Reads from the input array are not coalesced
    - Adjacent threads process non-adjacent input letters

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/histo_uncoalesced.png)

#### A Better Thread to Data Mapping

 - Reads from the input array are coalesced
    - Assign inputs to each thread in a strided pattern
    - Adjacent threads process adjacent input letters

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/histo_better_mem_access.png)

#### A Basic Histogram Kernel

 - The kernel receives a pointer to the input buffer of byte values
 - Each thread process the input in a strided pattern

```
// buffer: input
// size: number of chars in input buffer
// histo : 
__global__ void histo_kernel(unsigned char *buffer, long size, 
                                unsigned int *histo)
{
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    // stride is total number of threads of all blocks
    int stride = blockDim.x * gridDim.x;
    // All threads handle blockDim.x * gridDim.x consecutive elements
    while (i < size) {
        atomicAdd( &(histo[buffer[i]]), 1);
        i += stride;
    }
}
```

### Lecture 5.4: Parallel Computation Patters - Atomic Operations Performance 

 - main performance considerations of atomic operations
    - Latency and throughput of atomic operations 
    - Atomic operations on global memory
    - Atomic operations on shared L2 cache
    - Atomic operation on shared memory


#### Atomic Operations on DRAM

 - An atomic operation starts with a read, with a latency of a few hundred cycles
 - The atomic operation ends with a write, with a latency of a few hundred cycles
 - During this whole time, no one else can access the location
 - Each Load-Modify-Store has two full memory access delays
    - All atomic operations on the same variable (DRAM location) are serialized 

#### Latency determines throughput

 - Throughput of an atomic operation is the rate at which the application can execute an atomic operation.  
 - The rate for atomic operation on a particular location is limited by the total latency of the read-modifywrite sequence, typically more than 1000 cycles for global memory (DRAM) locations.
 - This means that if many threads attempt to do atomic operation on the same location (contention), the memory bandwidth is reduced to <
    - using atomic operation **extremely dangerous** if we're not careful, we can accidentally serialize all the threads. 
 
#### Hardware Improvements 

 - Atomic operations on Fermi L2 cache
    - Later Fermi
    - Medium latency, but still serialized
    - Shared among all blocks (all the streaming multiprocessors?)
    - “Free improvement” on Global Memory atomics
        - the programmer still think that they are use atomic operation on the global memory 
 - Atomic operations on Shared Memory
    - Very short latency, but still serialized
    - Private to each thread block
    - Need algorithm work by programmers(more later)

### Lecture 5.5: Parallel Computation Patterns - A Privatized Histogram Kernel

 - write a high performance histogram kernel
    - ***Privatization technique*** for reducing latency, increasing throughput, and reducing serialization
    - Practical use of shared memory and L2 cache atomic operations

#### Histogram Privatization

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/histogram_privatization.png)

 - right pic
    - private copies of the histogram in the shared memory of each thread block
    - all the threads in the thread block just accumulate their findings into the private histogram
    - at the end of the kernel , all the threads in the thread block will collaborate , and update a final copy of the histogram based on the contents of it's local or private histogram.

#### Atomics in Shared Memory Requires Privatization

```
__global__ void histo_kernel(unsigned char *buffer, 
                            long size, unsigned int *histo) {
    // Create private copies of the histo[] array
    // for each thread block
    __shared__ unsigned int histo_private[256];     
    if (threadIdx.x < 256) 
        histo_private[threadidx.x]= 0;
    __syncthreads();    

```
    
#### Build Private Histogram

```
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    // stride is total number of threads
    int stride = blockDim.x * gridDim.x;
    while (i < size) {
        atomicAdd(
            &(histo_private[buffer[i]), 1
        );
        i += stride;
    }
```

#### Build Final Histogram

```
    // wait for all other threads in the block to finish
    __syncthreads();
    if (threadIdx.x < 256) {
        atomicAdd( &(histo[threadIdx.x]), histo_private[threadIdx.x] );
    }
}
```

#### More on Privatization

 - Privatization is a powerful and frequently used techniques for parallelizing applications
 - The operation needs to be ***associative and commutative***
    - istogram add operation is associative and commutative 
 - The private histogram size needs to be small
    - Fits into shared memory 
 - What if the histogram is too large to privatize?
