# 并行计算key concept

## why thread block?

 - Divide thread array into mulitple blocks. 
    - 执行同一份代码的threads 称为 thread block.
 - Threads within a block cooperate via **shared memory**(exchange data), **atomic operations** (update same variable) , and **barrier synchronization**(屏障同步 to force others to wait)
    - 线程对global memory的修改，其他线程可能无法看到 
 - Every thread has a thread index , and a thread block index. Index can be 1-3D.
 - Thread 以block的粒度被分配给 SM，每个SM能分配的thread block是有限制的。
 - 硬件设计上，每个block中的 每32-thread 作为一个**warp**, executed in SIMD.


## Control Divergence

 - Divergence can arise only when branch condition is a function(or condition) of **thread indices**
 - 要避免warp 中的 Divergence


## Tiled Parallel Algorithms：

 - 把需要处理的数据 分割成 tile, 每个事件处理一个或多个 tile的计算。
 - tiled algorithm 也是为了充分利用 shared memory


## Convolution

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/1DConvolutionExample.jpg)


## Reduction

 - process large input data sets
    - associative: `(A*B)*C = A*(B*C)`
    - commutative: `a+b = b+a`
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/better_reduction_kernel.png)

 - prevent divergence in warp

## Scan

`[x₀,x₁,...,xn₋₁] => [x₀,(x₀⊕x₁),...,(x₀⊕x₁⊕...⊕xn₋₁)]`

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/parallel_scan_put_together.png)


## Histogramming

 - A method for extracting notable features and patterns from large data sets
 - threads will interference when they write into their outputs
 

### Atomic Operations

### Privatization technique

 - Privatization is a powerful and frequently used techniques for parallelizing applications
 - The operation needs to be associative and commutative


### DMA transfers

 - cudaMemcpy() is implemented as one or more DMA transfers
 - The OS could accidentally page-out the data that is being read or written by a DMA and page-in another virtual page into the same physical location
 - CPU memory that serve as the source , or destination , of a DMA transfer must be allocated as pinned memory
 
### Task Parallelism

 - CUDA Streams
 
