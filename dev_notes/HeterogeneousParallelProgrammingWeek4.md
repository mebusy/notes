## Week4 

### Lecture 4.1: Parallel Computation Patterns - Reduction 

#### Partition and Summarize

 - A commonly used strategy for processing large input data sets
    - There is no required order of processing elements in a data set (associative 结合 and commutative 可 交换)
        - associative: `(A*B)*C = A*(B*C)`  
        - commutative: `a+b = b+a`
    - Partition the data set into smaller chunks
    - Have each thread to process a chunk
    - Use a reduction tree to summarize the results from each chunk into the final answer
 - Google and Hadoop MapReduce frameworks support this strategy
 - We will focus on the reduction tree step for now.

#### Reduction enables other techniques

 - Reduction is also needed to clean up after some commonly used parallelizing transformations
 - Privatization
    - Multiple threads write into an output location 
    - Replicate the output location into many locations so that each thread has a private output location
    - Use a reduction tree to combine the values of private locations into the original output location

#### What is a reduction computation?

 - Mathmatically a reduction is a computation that summarize a set of input values into one value using a “reduction operation”
    - Max
    - Min
    - Sum
    - Product
    - all those operators are both associative and commutative , so that's we can use reduction. 
 - Often with user defined reduction operation function as long as the operation
    - Is associative and commutative
    - Has a well-defined identity value (e.g., 0 for sum)

#### An Efficient Sequential Reduction O(N)

We can write a fairly efficient sequential reduction program by following this procedure: 

 - Initialize the result as an identity value for the reduction operation
    - Smallest possible value for max reduction
    - Largest possible value for min reduction
    - 0 for sum reduction
    - 1 for product reduction
 - Iterate through the input and perform the reduction operation between the result value and the current input value
    - N reduction operations performed for N input values

#### A prarallel reduction tree algorithm log(N)

perferms N-1 Operations in log(N)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallel_reduction_tree.png)

#### A tournament is a reduction tree with "max" operation

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/tournament_reduction.png)

#### A Quick Analysis

 - For N input values, the reduction tree performs
    - (1/2)N + (1/4)N + (1/8)N + … (1)N = (1- (1/N))N = N-1 operations 
    - In Log (N) steps – 1,000,000 input values take 20 steps
        - Assuming that we have enough execution resources 
    - Average Parallelism (N-1)/Log(N)
        - For N = 1,000,000, average parallelism is 50,000 
        - However, peak resource requirement is 500,000!
        - This is not resource efficient.
    - This is a work-efficient parallel algorithm
        - The amount of work done is comparable to sequential 
        - Many parallel algorithms are not work efficient

---

### Lecture 4.2: Parallel Computation Patterns - A Basic Reduction Kernel 

#### Parallel Sum Reduction

 - Parallel implementation:
    - Recursively half # of threads, add two values per thread in each step 
    - Takes log(n) steps for n elements, requires n/2 threads
 - Assume an in-place reduction using shared memory
    - The original vector is in device global memory
    - The shared memory is used to hold a partial sum vector
    - Each step brings the partial sum vector closer to the sum
    - The final sum will be in element 0
    - Reduces global memory traffic due to partial sum values
    - Thread block size limits n to be less than or equal to 2,048

#### A Parallel Sum Reduction Example

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/example_parallel_sum.png)

#### A Naive Thread Index to Data Mapping

 - Each thread is responsible of an even-index location of the partial sum vector
 - After each step, half of the threads are no longer needed
 - One of the inputs is always from the location of responsibility
 - In each step, one of the inputs comes from an increasing distance away

#### A Simple Thread Block Design

 - Each thread block takes 2* BlockDim.x input elements
 - Each thread loads 2 elements into shared memory

```
#shared memory,deal data 2 times #threads in a block
__shared__ float partialSum[2*BLOCK_SIZE]; 

unsigned int t = threadIdx.x;

# skip the *input* date elements that are covered 
# by the previsous thread blocks
unsigned int start = 2*blockIdx.x*blockDim.x;
partialSum[t] = input[start + t];
partialSum[blockDim+t] = input[start + blockDim.x+t]; // .x ?
```

#### The Reduction Steps

```
for (unsigned int stride = 1; stride <= blockDim.x; stride *= 2) {
    __syncthreads();
    if (t % stride == 0)
        partialSum[2*t]+= partialSum[2*t+stride];
}
```

Why do we need `__syncthreads()`?

 - `__syncthreads()` are needed to ensure that all elements of each version of partial sums have been generated before we proceed to the next step
    - 1st call is to ensure all datas loaded
    - next call is to ensure all sum in this step done


#### Back to the Global Picture

 - At the end of the kernel, Thread 0 in each thread block writes the sum of the thread block in partialSum[0] into a vector indexed by the blockIdx.x
 - There can be a large number of such sums if the original vector is very large
    - The host code may iterate and launch another kernel 
 - If there are only a small number of sums, the host can simply transfer the data back and add them together.

### Lecture 4.3: Parallel Computation Patterns - A Better Reduction Kernel 

#### Some Observations on the naïve reduction kernel

 - In each iteration, two control flow paths will be sequentially traversed for each warp
    - Threads that perform addition and threads that do not  
    - Threads that do not perform addition still consume execution resources
 - Half or fewer of threads will be executing after the first step
    - All odd-index threads are disabled after first step
    - After the 5th step, entire warps in each block will fail the if test, poor resource utilization but no divergence
        - This can go on for a while, up to 6 more steps (stride = 32, 64, 128, 256, 512, 1024), where each active warp only has one productive thread until all warps in a block retire.

#### Thread Index Usage Matters

 - In some algorithms, one can shift the index usage to improve the divergence behavior
    - Commutative and associative operators
 - Always compact the partial sums into the front locations in the partialSum[] array
 - Keep the active threads consecutive
        
#### An Example of 4 threads

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/better_reduction_kernel.png)

#### A Better Reduction Kernel

```
for (unsigned int stride = blockDim.x; stride > 0; stride /= 2)
{
    __syncthreads();
    if (t < stride)
        partialSum[t] += partialSum[t+stride];
}
```

#### A Quick Analysis

 - For a 1024 thread block
    - No divergence in the first 5 steps
        - 1024, 512, 256, 128, 64, 32 consecutive threads are active in each step 
        - All threads in each warp either all active or all inactive
    - The final 5 steps will still have divergence  


### Lecture 4.4: Parallel Computation Patterns - Scan (Prefix Sum)     

Scan is a key primitive in many parallel algorithms to convert serial computation into parallel computation.

#### (Inclusive) Prefix-Sum (Scan) Definition

Inclusive scan is a mathmatical operation on a sequence of numbers.

**Definition**: The all-prefix-sums operation takes a binary associative operator ⊕, and an array of n elements:

`[x₀,x₁,...,xn₋₁]`,

and returns the array:

`[x₀,(x₀⊕x₁),...,(x₀⊕x₁⊕...⊕xn₋₁)]`,

Inclusive: all elements in the cumulative

#### An Inclusive Scan Application Example

 - Assume that we have a 100-inch sausage to feed 10 person
 - We know how much each person wants in inches 
    - [3 5 2 7 28 4 3 0 8 1]
 - How do we cut the sausage quickly? 
 - How much will be left
 - Method 1: cut the sections sequentially: 3 inches first, 5 inches second, 2 inches third, etc. 
 - Method 2: calculate prefix sum:
    - [3, 8, 10, 17, 45, 49, 52, 52, 60, 61] (39 inches left)
    - 现在我们知道每次切割下刀的位置，这样就可以用10把刀同时切割

#### Typical Applications of Scan

 - Scan is a simple and useful parallel building block
    - Convert recurrences from sequential :
```
for(j=1;j<n;j++)
    out[j] = out[j-1] + f(j);
```
 - into parallel:
```
forall(j) { temp[j] = f(j) };
scan(out, temp);
```
 - Useful for many parallel algorithms:
    - Radix sort,Quicksort,String comparison,Lexical analysis,Stream compaction,Polynomial evaluation,Solving recurrences,Tree operations,Histograms, ....

#### Other Applications

 - Assigning camp slots
 - Assigning farmer market space
 - Allocating memory to parallel threads
 - Allocating memory buffer for communication channels
 - ...

#### An Inclusive Sequential Addition Scan

 - Given a sequence [x₀, x₁, x₂, ... ]
 - Calculate output [y₀, y₁, y₂, ... ]
 - Such that: y₀=x₀, y₁=x₀+x₁, y₂=x₀+x₁+x₂, ...
 - Using a recursive definition: `yᵢ= yᵢ₋₁ + xᵢ`

#### A Work Efficient C Implementation

Sequential implementation:

```
y[0] = x[0];
for (i = 1; i < Max_i; i++)
    y[i] = y [i-1] + x[i];
```

Computationally efficient:

 - N additions needed for N elements - O(N)
 - Only slightly more expensive than sequential reduction.

#### A Naive Inclusive Parallel Scan

 - Assign one thread to calculate each y element
 - Have every thread to add up all x elements needed for the y element:
    - thread 0 do y₀=x₀, thread 1 do y₁=x₀+x₁, ...

this is really naive and ridiculous.

***Parallel programming is easy as long as you do not care about performance.***

---

### Lecture 4.5: Parallel Computation Patterns - A Work-Inefficient Scan Kernel 

#### A Better Parallel Scan Algorithm

 1. Read input from device global memory to shared memory
 2. Iterate log(n) times; stride from 1 to n-1: 
    - double stride each iteration
 3. Write output from shared memory to device memory

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallelScanAlgorithm.png)

 - Active threads stride to n-1 (n-stride threads)
 - Thread j adds elements j and `j-stride` from shared memory and writes result into element j in shared memory
    - 1次迭代，结果是2个数的和
    - 2次迭代，结果是4个数的和(2+2)
    - 3次迭代，结果是8个数的和(4+4)
 - Requires barrier synchronization, once before read and once before write
    - 因为 add的结果会破坏输入数据，所以在write之前需要一次同步。 

#### Handling Dependencies

 - During every iteration, each thread can overwrite the input of another thread.
    - Barrier synchronization to ensure all inputs have been properly generated
    - All threads secure input operand 操作数 that can be overwritten by another thread
    - Barrier synchronization to ensure that all threads have secured their inputs
    - All threads perform Addition and write output

#### A Work-Inefficient Scan Kernel

伪代码，可能有错误.

```
# X: input
# Y: output
# InputSize: # of elements in the original vector
# SECTION_SIZE: section of input, taken by each thread block?
__global__ void scan_kernel(float *X, float *Y, int InputSize) {
    __shared__ float XY[SECTION_SIZE];
    int i = blockIdx.x*blockDim.x + threadIdx.x;
    if (i < InputSize) {
        XY[threadIdx.x] = X[i];
    }
    // the code below performs iterative scan on XY
    for (unsigned int stride = 1; stride <= threadIdx.x; stride *= 2) {
        __syncthreads(); # store in register
        float in1 = XY[threadIdx.x-stride];
        __syncthreads();
        XY[threadIdx.x] += in1;
    }
    __syncthreads();
    if (i<InputSize) {
        Y[i]=XY[threadIdx.x];
    }
}
```

#### Work Efficiency Considerations

 - This Scan executes log(n) parallel iterations
    - The steps do (n-1), (n-2), (n- 4),..(n- n/2) adds each 
    - Total adds: n * log(n) - (n-1)  O(n*log(n)) work
 - This scan algorithm is not work efficient
    - Sequential scan algorithm does n adds
    - A factor of log(n) can hurt: 10x for 1024 elements!
 - ***A parallel algorithm can be slower than a sequential one when execution resources are saturated from low work efficiency***.

 
### Lecture 4.6: Parallel Computation Patterns - A Work-Efficient Parallel Scan Kernel 

 - Two-phased balanced tree traversal
 - Aggressive reuse of computation results
 - Reducing control divergence with more complex thread index to data index mapping

#### Improving Efficiency

 - Balanced Trees
    - Form a balanced binary tree on the input data and sweep it to and from the root
    - Tree is not an actual data structure, but a concept to determine what each thread does at each step
        - at each iteration or each step which thread should be taking action and how the action should be done?
 - For scan:
    - Traverse down from leaves to root building partial sums at internal nodes in the tree 
        - building a partial sum at the intermediate internal nodes in the tree
        - at each step whenever we compute a partial sum, we will be updating one of the data elements in the shared memory
        - Root holds sum of all leaves    
    - Traverse back up the tree, building the output from the partial sums

#### Parallel Scan - Reduction Phase

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallel_scan_reduction.png)

 - start by having all the elements in the shared memory array

#### Reduction Phase Kernel Code

```
// XY[2*BLOCK_SIZE] is in shared memory
// assume that BLOCK_SIZE is half the number of elements in each section
// 1 thread handle 2 elments
for (int stride = 1;stride <= BLOCK_SIZE; stride *= 2) {
    int index = (threadIdx.x+1)*stride*2 - 1;
    // stride:   1,2,4
    // thread 0: 1,3,7
    // thread 1: 3,7,15
    // thread 2: 5,11,...
    // thread 3: 7,15,...
    if(index < 2*BLOCK_SIZE)
        XY[index] += XY[index-stride];
    __syncthreads();
}
```

#### Parallel Scan - Post Reduction Reverse Phase

 - after we have all these partial results in these element positions
 - we will start to sweep back from the root back to the leaves
 - the point of the computation is to as quickly as possible assemble the final result from the partial sums.
 - allows us to do just one more step and bring everyone to the final value.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallel_scan_post_reduction.png)

#### Putting it together
 
 - 16 elements case

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallel_scan_put_together.png)


#### Post Reduction Reverse Phase Kernel Code

```
// BLOCK_SIZE = 8 , in 16 elements case
for (int stride = BLOCK_SIZE/2; stride > 0;stride /= 2) {
    // ensure previous reduction step , or previous iteration finish
    __syncthreads();
    // stride         :  4   ,  2  ,  1
    // thread+stride 0:  7+4 , 3+2 , 1+1
    // thread+stride 1: 15+4 , 7+2 , 3+1
    // thread+stride 6: 55+4 , 27+2 ,13+1
    // thread+stride 7: 63+4 , 31+2 ,15+1
    int index = (threadIdx.x+1)*stride*2 - 1;
    if(index+stride < 2*BLOCK_SIZE) {
        XY[index + stride] += XY[index];
    }
}
__syncthreads();
// write back to global memory
if (i < InputSize) Y[i] = XY[threadIdx.x];
```

### Lecture 4.7: Parallel Computation Patterns - More on Parallel Scan

 - Exclusive scan
 - Handling large input vectors
 
#### Work Analysis of the Work Efficient Kernel

 - kernel executes log(n) parallel iterations in the reduction step
    - The iterations do n/2, n/4,..1 adds 
    - Total adds: (n-1) → O(n) work
 - It executes log(n)-1 parallel iterations in the post reduction reverse step
    - The iterations do 2-1, 4-1, …. n/2-1 adds
    - Total adds: (n-2) – (log(n)-1) → O(n) work
 - The total number of adds is no more than twice of that done in the efficient sequential algorithm
    - The benefit of parallelism can easily overcome the 2X work when there is sufficient hardware 
    

#### Some Tradeoffs

 - The work efficient scan kernel is normally more desirable
    - Better Energy efficiency
    - Less execution resource requirement
 - However, the work inefficient kernel could be better for absolute performance due to its single-step nature if
    - There is sufficient execution resource 
    

#### Exclusive Scan Definition

**Definition**: The exclusive scan operation takes a binary associative operator ⊕, and an array of n elements:

```
[x₀,x₁,...,xn₋₁],
```

and returns the array:

```
[0, x₀,(x₀⊕x₁),...,(x₀⊕x₁⊕...⊕xn₋₂)],
```

Example:

 - if ⊕ is addition
 - array:  [3 1 7  0  4  1  6  3]
 - return: [0 3 4 11 11 15 16 22]
 
#### Why Exclusive Scan

 - To find the beginning address of allocated buffers
 - Inclusive and exclusive scans can be easily derived from each other; it is a matter of convenience
    -            [3 1 7 0 4 1 6 3]
    - exclusive: [0 3  4 11 11 15 16 22]
    - inclusive: [3 4 11 11 15 16 22 25]


#### A simple exclusive scan kernel

 - Adapt an inclusive, work in-efficient scan kernel
 - Block 0:
    - Thread 0 loads 0 into XY[0]
    - Other threads load X[threadIdx.x-1] into XY[threadIdx.x]
 - All other blocks:
    - All thread load X[blockIdx.x*blockDim.x+threadIdx.x-1] into XY[threadIdex.x] 
 - Similar adaption for work efficient scan kernel but pay attention that each thread loads two elements
    - Only one zero should be loaded
    - All elements should be shifted by only one position

#### Handling large Input Vectors

 - Build on the work efficient scan kernel 
 - Have each section of 2*blockDim.x elements assigned to a block
 - Have each block write the sum of its section into a ***Sum[]*** array indexed by blockIdx.x
 - Run the scan kernel on the ***Sum[]*** array
 - Add the scanned ***Sum[]*** array values to the elements of corresponding sections
 - Adaptation of work inefficient kernel is similar.



![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/scan_flow.png)


