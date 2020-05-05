...menustart

 - [同步/异步 阻塞/非阻塞](#e985ed72fda13866ca02463097549a48)
     - [进程间通信的同步/异步， 阻塞/非阻塞](#33a2cac7be4f98ad450a1903f8111ef4)
     - [I/O System Call 的阻塞/非阻塞， 同步/异步](#759c4a462849255bba99567256a3ffdd)
     - [总结](#25f9c7fa3b50aebe5125112ac1187777)

...menuend


<h2 id="e985ed72fda13866ca02463097549a48"></h2>


# 同步/异步 阻塞/非阻塞

- 同步（Synchronous）
- 异步( Asynchronous)
- 阻塞( Blocking )
- 非阻塞( Nonblocking)


<h2 id="33a2cac7be4f98ad450a1903f8111ef4"></h2>


## 进程间通信的同步/异步， 阻塞/非阻塞

- 3.4.2.2 Synchronization
    - Communication between processes takes place through calls to `send()` and `receive()` primitives.
        - There are many different design options for implementing each primitive. 
        - Message passing may be either **blocking** or **nonblocking** , also known as **synchronous** and **asynchronous**.
        - (Throughout this text, you will encounter the concepts of synchronous and asynchronous behavior in relation to various operating-system algorithms. )
    - **Blocking send**
        - The sending process is blocked until the message is received by the receiving process or by the mailbox.
    - **Nonblocking send**
        - The sending process sends the message and resumes operation
    - **Blocking receive**
        - The receiver blocks until a message is available
    - **Nonblocking receive**
        - The receiver retrieves either a valid message or a null.
    - Different combinations of `send()` and `receive()` are possible. 
        - when both `send()` and `receive()` are blocking, we have a **rendezvous** between the sender and receiver.
        - The solution to the producer-consumer problem becomes trivial when we use blocking `send()` and `receive()` statements.

    - 也就是说， 从进程级通信的维度讨论时， 阻塞和同步（非阻塞和异步）就是一对同义词， 且需要针对发送方和接收方作区分对待。
- 进程切换
    - 重要步骤
        1. 当一个程序正在执行的过程中， 中断（interrupt） 或 系统调用（system call） 发生可以使得 CPU 的控制权会从当前进程转移到操作系统内核。
        2. 操作系统内核负责保存进程 i 在 CPU 中的上下文（程序计数器， 寄存器）到 PCBi （操作系统分配给进程的一个内存块）中。
        3. 从 PCBj 取出进程 j 的CPU 上下文， 将 CPU 控制权转移给进程 j ， 开始执行进程 j 的指令。
    - 底层概念
        - 中断（interrupt）
            - CPU 层级的 while 轮询
            - 在每个CPU时钟周期的末尾, CPU会去检测那个中断信号位是否有中断信号到达
            - 如果有， 则会根据中断优先级决定是否要暂停当前执行的指令， 转而去执行处理中断的指令。 
        - 时钟中断( Clock Interrupt )
            - 一个硬件时钟会每隔一段（很短）的时间就产生一个中断信号发送给 CPU
            - CPU 在响应这个中断时， 就会去执行操作系统内核的指令，继而将 CPU 的控制权转移给了操作系统内核， 可以由操作系统内核决定下一个要被执行的指令。
        - 系统调用（system call）
            - system call 是操作系统提供给应用程序的接口。 用户通过调用 systemcall 来完成那些需要操作系统内核进行的操作， 例如硬盘， 网络接口设备的读写等。

- 进程阻塞
    - 在任意时刻， 一个 CPU 核心上（processor）只可能运行一个进程 。
    - “阻塞”是指进程在发起了一个系统调用（System Call） 后， 由于该系统调用的操作不能立即完成，需要等待一段时间，于是内核将进程挂起为等待 （waiting）状态， 以确保它不会被调度执行， 占用 CPU 资源。


<h2 id="759c4a462849255bba99567256a3ffdd"></h2>


## I/O System Call 的阻塞/非阻塞， 同步/异步

- 阻塞和非阻塞 描述的是进程的一个操作是否会使得进程转变为“等待”的状态, 为什么我们总是把它和 IO 连在一起讨论
- **阻塞** 这个词是与系统调用 System Call 紧紧联系在一起的, 因为 要让一个进程进入 等待（waiting） 的状态, 
    - 要么是它主动调用 wait() 或 sleep() 等挂起自己的操作
    - 另一种就是它调用 System Call, 而 System Call 因为涉及到了 I/O 操作， 不能立即完成
        - 于是内核就会先将该进程置为等待状态， 调度其他进程的运行， 等到 它所请求的 I/O 操作完成了以后， 再将其状态更改回 ready 。
- 大部分操作系统默认为用户级应用程序提供的都是阻塞式的系统调用 （blocking systemcall）接口， 因为阻塞式的调用，使得应用级代码的编写更容易（代码的执行顺序和编写顺序是一致的）。
- 但同样， 现在的大部分操作系统也会提供非阻塞I/O 系统调用接口（Nonblocking I/O system call）。 
    - 一个非阻塞调用不会挂起调用程序， 而是会立即返回一个值， 表示有多少bytes 的数据被成功读取（或写入）。
- 非阻塞I/O 系统调用( nonblocking system call )的另一个替代品是 异步I/O系统调用 （asychronous system call）
    - 与非阻塞 I/O 系统调用类似，asychronous system call 也是会立即返回， 不会等待 I/O 操作的完成， 应用程序可以继续执行其他的操作， 等到 I/O 操作完成了以后，操作系统会通知调用进程（设置一个用户空间特殊的变量值 或者 触发一个 signal 或者 产生一个软中断 或者 调用应用程序的回调函数）。
- 非阻塞I/O 系统调用( nonblocking system call ) 和 异步I/O系统调用 （asychronous system call）的区别 仅仅是 返回结果的方式和内容有所不同
    - **非阻塞I/O** 系统调用 read() 操作立即返回的是任何可以立即拿到的数据， 可以是完整的结果， 也可以是不完整的结果， 还可以是一个空值。
    - **异步I/O系统调** 用 read（）结果必须是完整的， 但是这个操作完成的通知可以延迟到将来的一个时间点。

- 同步I/O 与 异步 I/O 的区别
    - ![](https://pic3.zhimg.com/80/v2-e0180a5ffebd91c480d0ccdc02c6d2a7_720w.jpg)

- 附: Linux 基本上使用的都是 1对1内核级线程模型, 线程调用阻塞i/o 不会导致整个进程被挂起


<h2 id="25f9c7fa3b50aebe5125112ac1187777"></h2>


## 总结

1. 阻塞/非阻塞， 同步/异步的概念要注意讨论的上下文：
    - 在进程通信层面， 阻塞/非阻塞， 同步/异步基本是同义词, 区分讨论的对象是发送方还是接收方。
    - 发送方阻塞/非阻塞（同步/异步）和接收方的阻塞/非阻塞（同步/异步） 是互不影响的
    - 在 IO 系统调用层面（ IO system call ）层面， 非阻塞 IO 系统调用 和 异步 IO 系统调用存在着一定的差别
        - 都属于非阻塞系统调用（ non-blocing system call ),  它们都不会阻塞进程
        - 但是返回结果的方式和内容有所差别
2. 非阻塞系统调用（non-blocking I/O system call 与 asynchronous I/O system call） 的存在可以用来实现线程级别的 I/O 并发









