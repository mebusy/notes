## Week #6

### Lecture 6.1: Efficient Host-Device Data Transfer - Pinned Host Memory 
 - important concepts involved in copying (transferring) data between host and device
    - System Interconnect
    - Direct Memory Access
    - Pinned memory

#### CPU-GPU Data Transfer using DMA

 - DMA (Direct Memory Access) hardware is used for cudaMemcpy() for better efficiency
    - Frees CPU for other tasks
    - Transfers a number of bytes requested by OS
    - Uses system interconnect, typically PCIe in today’s systems
    - not only for GPUs , but also for other I/O devices such as network interface cards
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DMA.png)

 - CPU sends commands to DMA and get it started. then the CPU can go to do other task

#### Virtual Memory Management

To understand how DMA works, we'd better know something about Virtual Memory.

 - Modern computers use virtual memory management
    - Many virtual memory spaces mapped into a single physical memory 
    - Virtual addresses (pointer values) are translated into physical addresses
        - the compute has a single DRAM base memory system
        - each process, or application, will have its own address space

 - Not all variables and data structures are always in the physical memory
    - Each virtual address space is divided into pages when mapped into physical memory 
    - Memory pages can be paged out to make room
    - Whether a variable is in the physical memory is checked at address translation time

#### Data Transfer and Virtual Memory 

 - DMA uses physical addresses
    - When cudaMemcpy() copies an array, it is implemented as one or more DMA transfers 
    - Address is translated and page presence checked at the beginning of each DMA transfer
    - No address translation for the rest of the same DMA transfer so that high efficiency can be achieved

 - The OS could accidentally page-out the data that is being read or written by a DMA and page-in another virtual page into the same physical location
    - because the CPU is now freed up to be able to do these other tasks

#### Pinned Memory and DMA Data Transfer 

固定内存

 - Pinned memory are virtual memory pages that are specially marked so that they cannot be paged out
 - Allocated with a special system API function call
 - a.k.a. Page Locked Memory, Locked Pages, etc.
 - CPU memory that serve as the source , or destination , of a DMA transfer must be allocated as pinned memory

#### CUDA data transfer uses pinned memory

 - If a source or destination of a cudaMemcpy() in the host memory is not allocated in pinned memory, it needs to be first copied to a pinned memory – extra overhead
 - cudaMemcpy() is faster if the host memory source or destination is allocated in pinned memory since no extra copy is needed

#### Allocate/Free Pinned Memory

 - cudaHostAlloc(), 3 parameters
    - Address of pointer to the allocated memory 
    - Size of the allocated memory in bytes
    - Option – use cudaHostAllocDefault for now
 - cudaFreeHost(), one parameter
    - Pointer to the memory to be freed

#### Using Pinned Memory in CUDA

 - Use the allocated pinned memory and its pointer the same way as those returned by malloc();
 - The only difference is that the allocated memory cannot be paged by the OS
 - The cudaMemcpy() function should be about 2X faster with pinned memory
 - ***Pinned memory is a limited resource***
    - over-subscription can have serious consequences  
    - if we take away too much of memory from the paging pool, the virtual memory system will start to function very poorly.

#### Vector Addition Host Code Example

```
int main()
{
    float *h_A, *h_B, *h_C;
    …
    cudaHostAlloc((void **)&h_A, N* sizeof(float),cudaHostAllocDefault);
    cudaHostAlloc((void **)&h_B, N* sizeof(float),cudaHostAllocDefault);
    cudaHostAlloc((void **)&h_C, N* sizeof(float),cudaHostAllocDefault);
    …
    vecAdd(h_A, h_B, h_C, N);
}
```
    
     

      
    
### Lecture 6.2: Efficient Host-Device Data Transfer - Task Parallelism in CUDA

 - task parallelism in CUDA 
    - CUDA Streams

#### Serialized Data Transfer and Computation

 - So far, the way we use cudaMemcpy serializes data transfer and GPU computation for VecAddKernel()
    - PCIe can actually do simulataneously transfer in both directions 
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cuda_serializedDataTransfer.png)

#### Device Overlap

 - Some CUDA devices support device overlap
    - Simultaneously execute a kernel while copying data between device and host memory

```
int dev_count;
cudaDeviceProp prop;
cudaGetDeviceCount( &dev_count);
for (int i = 0; i < dev_count; i++) {
    cudaGetDeviceProperties(&prop, i);
    if (prop.deviceOverlap) 
        … 
```
    
#### Ideal, Pipelined Timing

 - Divide large vectors into segments
 - Overlap transfer and compute of adjacent segments

![][1] 

 - Trans C0
 - Comp C2
 - Trans A2,B2
 - Do Simultaneously

#### CUDA Streams

 - CUDA supports parallel execution of kernels and Memcpy with “Streams”
    - Stream is a simple hardware mechanism , that supports the exploration of task parallelism. 
 - Each stream is a queue of operations (kernel launches and Memcpy’s)
 - Operations (tasks) in different streams can go in parallel
    - “Task parallelism”

#### Streams

 - Requests made from the host code are put into First-In-First-Out queues
    - Queues are read and processed asynchronously by the driver and device
        - device driver will be a taking operations out of the queue sequentially
    - Driver ensures that commands in a queue are processed in sequence. E.g., Memory copies end before kernel launch, etc.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_stream.png)

#### Streams cont.

 - To allow concurrent copying and kernel execution, use multiple queues, called “streams”
    - CUDA “events” allow the host thread to query and synchronize with individual queues (i.e. streams).
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_streams.png)


### Lecture 6.3: Efficient Host-Device Data Transfer - Overlapping Data Transfer with Computation 

 - overlap data transfer with computation
    - Asynchronous Data Transfer in CUDA
    - Practical Limitation of CUDA Streams

#### A Simple Multi-Stream Host Code

```
cudaStream_t stream0, stream1;
cudaStreamCreate(&stream0);
cudaStreamCreate(&stream1);

float *d_A0, *d_B0, *d_C0;// device memory for stream 0
float *d_A1, *d_B1, *d_C1;// device memory for stream 1

// cudaMalloc for d_A0, d_B0, d_C0, d_A1, d_B1, d_C1 go here
for (int i=0; i<n; i+=SegSize*2) {
    // stream 0
    cudaMemcpyAsync(d_A0, h_A+i, SegSize*sizeof(float),…, stream0);
    cudaMemcpyAsync(d_B0, h_B+i, SegSize*sizeof(float),…, stream0);
    vecAdd<<<SegSize/256, 256, 0, stream0>>>(d_A0, d_B0,…);
    cudaMemcpyAsync(h_C+i, d_C0, SegSize*sizeof(float),…, stream0);
    
    // stream 1
    cudaMemcpyAsync(d_A1, h_A+i+SegSize, 
                    SegSize*sizeof(float),…, stream1);
    cudaMemcpyAsync(d_B1, h_B+i+SegSize, 
                    SegSize*sizeof(float) ,…,stream1);
    vecAdd<<<SegSize/256, 256, 0, stream1>>>(d_A1, d_B1, …);
    cudaMemcpyAsync(d_C1, h_C+i+SegSize, 
                    SegSize*sizeof(float),…,stream1);
}
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_steam_reality.png)

 - the arcs show the dependency
 - bad case because of the implementation choice

#### Not quite the overlap we want in some GPUs

 - C.0 blocks A.1 and B.1 in the copy engine queue

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_streaming_block.png)

#### A Better Multi-Stream Host Code 

```
for (int i=0; i<n; i+=SegSize*2) {
    // steam 0
    cudaMemcpyAsync(d_A0, h_A+i, SegSize*sizeof(float),…, stream0);
    cudaMemcpyAsync(d_B0, h_B+i, SegSize*sizeof(float),…, stream0);
    // steam 1
    cudaMemcpyAsync(d_A1, h_A+i+SegSize, 
                    SegSize*sizeof(float),…,stream1);
    cudaMemcpyAsync(d_B1, h_B+i+SegSize, 
                    SegSize*sizeof(float),…,stream1);
    // steam 0
    vecAdd<<<SegSize/256, 256, 0, stream0>>>(d_A0, d_B0, …);
    // steam 1
    vecAdd<<<SegSize/256, 256, 0, stream1>>>(d_A1, d_B1, …);
    // steam 0
    cudaMemcpyAsync(h_C+i, d_C0, SegSize*sizeof(float),…, stream0);
    // steam 1
    cudaMemcpyAsync(h_C+i+SegSize, d_C1, 
                    SegSize*sizeof(float),…, stream1);
}
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_streaming_noblock.png)

#### Better, not quite the best overlap

 - C.1 blocks next iteration A.0 and B.0 in the copy engine queue
 - 一般情况下， kernel占用的时间比例相对 data transfer是很小的，因此即便不是最优的，这种算法也会有较大的性能提升

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDA_streaming_noblock2.png)

#### Ideal, Pipelined Timing

 - Will need at least three buffers for each original A, B,and C, code is more complicated (MP description)

![][1] 

#### Hyper Queues

 - Provide multiple real queues for each engine
 - Allow much more concurrency by allowing some streams to make progress for an engine while others are blocked 

#### Wait until all tasks have completed

 - cudaStreamSynchronize(stream_id)
    - Used in host code
    - Takes one parameter – stream identifier
    - Wait until all tasks in a stream have completed
 - This is different from cudaDeviceSynchronize()
    - Also used in host code
    - No parameter
    - cudaDeviceSynchronize() waits until all tasks in all streams have completed for the current device

```
cudaStreamSynchronize(stream0);
// In host code ensures that all tasks in
//the queues of stream0 have completed
cudaDeviceSynchronize();
```  

---

[1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/CUDADeviceOverlap.png

