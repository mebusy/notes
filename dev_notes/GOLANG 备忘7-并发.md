[](...menustart)

- [并发](#065a9b80a66476c57e1a80b9c262b0ab)
    - [7.1 Goroutine](#667f2ff8b591eb1e86e81dea9d65f407)
        - [修改 runtime.GOMAXPROCS, 改变用语服务goroutine的线程数量](#0fa47a8ea15a8f7e6e581d158200c031)
        - [runtime.Goexit 将⽴即终止当前 goroutine 执行，defer语句会确保被调用](#6cb3840015f36ea21d9a38b22fd782a1)
        - [Gosched 让出底层线程, 等待下次被调度执行, 和协程 y ield 作⽤用类似](#866a01d74a59323f87dd66a4be6887e4)
    - [7.2 Channel](#3eb6b9328888e5f64461426e25a98d9c)
        - [channel 是类似 pipe 的单/双向数据管道。](#adaf1ac202146d52ffeba2e71cc3c413)
        - [Channel 是一个类型的通道, 通过 <- 操作符 传输数据](#b402f129f1970639d5660becd02ee50e)
        - [必须使用 make 创建 , ch := make(chan int)](#c7a1b62f291a44bc49f940820cdc8903)
        - [默认同步模式 , 需要发送和接收配对](#429c41904e5b3734807651e0cf46b384)
        - [异步模式,  通道缓冲 , ch := make(chan int, 100)](#e4623663be0ab1d250238752f3f96c38)
        - [缓冲区是内部属性,并非类型 构成要素](#2d08e715004e5800ba9b1afcfc39862c)
        - [发送方 可以关闭通道， 接收方可以 测试 通道 是否被关闭](#1855ce8120d25f7ff9046215e353f986)
        - [可以在channel上 使用 range](#42154c90d129cea43ad3f5b31c13d714)
        - [向 closed channel 发送数据引发 panic 错误, 接收则返回零值](#27a72f1612def7a6535116343a2d1b83)
        - [nil channel, 无论收发都会被阻塞](#15ad3da382d6686eddc4fa77ef7bfe1f)
        - [内置函数 len 返回未被读取的缓冲元素数量, cap 返回缓冲区大小](#e22c3257bc5511d58ca1817914b82412)
        - [7.2.1 单向](#e07be157f6c7c916e9a170040e205340)
            - [可以将 channel 隐式转换为单向队列, 只收或只发, 反之出错](#143129b11cc6cb85e3c06bfeb5e404e1)
        - [7.2.2 选择 select](#602c159c42ecd59d48c0727e6a118856)
            - [select 随机选择一个可用的channel 做收发操作, 或执行default case](#c1ea955e4351de33d2dd18a9ba504e47)
            - [select 会阻塞， 直到有一个 case 可以run](#7031a0e3553771f54c99acc61403b6e5)
            - [在循环中使用 select default case 需要小心,避免形成洪水](#56fa9599addb4d2b62acec690101e196)
        - [7.2.3 模式](#7cb8b1870f81941ef4a0b1b9f60bf94d)
            - [简单⼯工⼚厂模式打包并发任务和 channel](#e801cf1b79e2738cc7502a26f278d269)
            - [用 channel 实现信号量 (semaphore)](#ccfc33b9fc3d9ab4d1b58bb5cbc4fba9)
            - [用 closed channel 发出退出通知 ( closed channel接受不会阻塞 )](#76b59db978a8ec6a372c39ea89ac02cc)
            - [用 select 实现超时 (timeout)](#cde8fe32f9b8886236870f0e615fba81)
            - [channel 可传参(内部实现为指针), 或 作为 结构成员](#7012283f647776697633c244ec95b9de)

[](...menuend)


<h2 id="065a9b80a66476c57e1a80b9c262b0ab"></h2>

# 并发




<h2 id="667f2ff8b591eb1e86e81dea9d65f407"></h2>

## 7.1 Goroutine

```go
go func() {
    println("Hello, World!")
}()
```

<h2 id="0fa47a8ea15a8f7e6e581d158200c031"></h2>

##### 修改 runtime.GOMAXPROCS, 改变用语服务goroutine的线程数量

```go
//1.5 已经默认使用 runtime.NumCPU()
runtime.GOMAXPROCS(runtime.NumCPU())
```

<h2 id="6cb3840015f36ea21d9a38b22fd782a1"></h2>

##### runtime.Goexit 将⽴即终止当前 goroutine 执行，defer语句会确保被调用

```go
runtime.Goexit()
```

<h2 id="866a01d74a59323f87dd66a4be6887e4"></h2>

##### Gosched 让出底层线程, 等待下次被调度执行, 和协程 y ield 作⽤用类似

```go
runtime.Gosched()
```


<h2 id="3eb6b9328888e5f64461426e25a98d9c"></h2>

## 7.2 Channel

<h2 id="adaf1ac202146d52ffeba2e71cc3c413"></h2>

##### channel 是类似 pipe 的单/双向数据管道。

    从设计上确保,在同⼀时刻,只有⼀个 goroutine能从中接收数据。
    发送和接收都是原⼦子操作,不会中断,只会失败。

<h2 id="b402f129f1970639d5660becd02ee50e"></h2>

##### Channel 是一个类型的通道, 通过 <- 操作符 传输数据

```go
ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and assign value to v.
<-c // 接收数据，丢弃
```

<h2 id="c7a1b62f291a44bc49f940820cdc8903"></h2>

##### 必须使用 make 创建 , ch := make(chan int)

```go
ch := make(chan int)
```

<h2 id="429c41904e5b3734807651e0cf46b384"></h2>

##### 默认同步模式 , 需要发送和接收配对

    发送接收操作会造成阻塞， 支持另一方准备好
    1) 在一个channel上的发送操作会阻塞，直到该channel上有一个接收者就绪。
    2) 在一个channel上到的接收操作会阻塞，直到该channel上有一个发送者就绪。

<h2 id="e4623663be0ab1d250238752f3f96c38"></h2>

##### 异步模式,  通道缓冲 , ch := make(chan int, 100)
    
```go
ch := make(chan int, 100)
```

    发送数据只有当通道缓冲满 的时候才会阻塞
    同样的， 当通道缓冲空的时候，接收操作会阻塞
    

    异步 channel 可减少排队阻塞,具备更高的效率。
    但应该考虑使用指针规避 大对象拷⻉,
    将多个元素打包,减小缓冲区大小等.

<h2 id="2d08e715004e5800ba9b1afcfc39862c"></h2>

##### 缓冲区是内部属性,并非类型 构成要素

```go
var a, b chan int = make(chan int), make(chan int, 3)
```

<h2 id="1855ce8120d25f7ff9046215e353f986"></h2>

##### 发送方 可以关闭通道， 接收方可以 测试 通道 是否被关闭

```go
//当没有剩余数据可以被接收， 并且通道被关闭， 返回false
for {
    if v , ok := <-ch; ok {
        fmt.Println(v)
    } else {
        break 
    }
}
```

<h2 id="42154c90d129cea43ad3f5b31c13d714"></h2>

##### 可以在channel上 使用 range 
```go
for value := range <-ch {
    use(value)
}
```

<h2 id="27a72f1612def7a6535116343a2d1b83"></h2>

##### 向 closed channel 发送数据引发 panic 错误, 接收则返回零值
---
<h2 id="15ad3da382d6686eddc4fa77ef7bfe1f"></h2>

##### nil channel, 无论收发都会被阻塞
---
<h2 id="e22c3257bc5511d58ca1817914b82412"></h2>

##### 内置函数 len 返回未被读取的缓冲元素数量, cap 返回缓冲区大小

---
<h2 id="e07be157f6c7c916e9a170040e205340"></h2>

### 7.2.1 单向

<h2 id="143129b11cc6cb85e3c06bfeb5e404e1"></h2>

##### 可以将 channel 隐式转换为单向队列, 只收或只发, 反之出错

```go
c := make(chan int, 3)

var send chan<- int = c  // send-only 
var recv <-chan int = c  // receive-only

send <- 1
<-recv
```


<h2 id="602c159c42ecd59d48c0727e6a118856"></h2>

### 7.2.2 选择 select

<h2 id="c1ea955e4351de33d2dd18a9ba504e47"></h2>

##### select 随机选择一个可用的channel 做收发操作, 或执行default case

    select是Go中的一个控制结构，类似于用于通信的switch语句。
    每个case必须是一个通信操作，要么是send要么是receive。


```go
go func() {
    v, ok, s := 0, false, ""
    for {
        select {   // 随机选择可用 channel,接收数据
        case v, ok = <-a: s = "a"
        case v, ok = <-b: s = "b"
        }
        if ok {
            fmt.Println(s, v)
        } else {
            os.Exit(0)
        } 
    }
}()
```
---
<h2 id="7031a0e3553771f54c99acc61403b6e5"></h2>

##### select 会阻塞， 直到有一个 case 可以run 
---
<h2 id="56fa9599addb4d2b62acec690101e196"></h2>

##### 在循环中使用 select default case 需要小心,避免形成洪水


---
<h2 id="7cb8b1870f81941ef4a0b1b9f60bf94d"></h2>

### 7.2.3 模式

<h2 id="e801cf1b79e2738cc7502a26f278d269"></h2>

##### 简单⼯工⼚厂模式打包并发任务和 channel

    "返回channel的函数"是Go中的一个重要的惯用法

```go
func NewTest() chan int {
    c := make(chan int)
    rand.Seed(time.Now().UnixNano())
    go func() {
        time.Sleep(time.Second)
        c <- rand.Int()
    }()
    return c 
}

func main() {
    t := NewTest()
    println(<-t) // 等待 goroutine 结束返回
}
```

<h2 id="ccfc33b9fc3d9ab4d1b58bb5cbc4fba9"></h2>

##### 用 channel 实现信号量 (semaphore)

```go
func main() {
    wg := sync.WaitGroup{}
    wg.Add(3)
    sem := make(chan int, 1)
    
    for i := 0; i < 3; i++ {
        go func(id int) {
            defer wg.Done()
            
            sem <- 1   // 向 sem 发送数据,阻塞或者成功
            
            for x := 0; x < 3; x++ {
                fmt.Println(id, x)
            } 
            
            <-sem  // 接收数据,使得其他阻塞 goroutine 可以发送数据
        }(i)
    }
    wg.Wait() 
}
输出:
2 0
2 1
2 2
0 0
0 1
0 2
1 0
1 1
1 2
```

<h2 id="76b59db978a8ec6a372c39ea89ac02cc"></h2>

##### 用 closed channel 发出退出通知 ( closed channel接受不会阻塞 )

```go
func main() {
    var wg sync.WaitGroup
    quit := make(chan bool)
    
    for i := 0; i < 2; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            task := func() {
                println(id, time.Now().Nanosecond())
                time.Sleep(time.Second)
            }
            for {
                select {
                case <-quit: //closed channel接受不会阻塞, 可用作退出通知
                    return
                default:
                    task()
                } 
            } // end for
        }(i)
    }
    time.Sleep(time.Second * 5)
    close(quit)             // 发出退出通知
    wg.Wait()
}
```

<h2 id="cde8fe32f9b8886236870f0e615fba81"></h2>

##### 用 select 实现超时 (timeout)

```go
func main() {
    w := make(chan bool)
    c := make(chan int, 2)
    go func() {
        select {
        case v := <-c: fmt.Println(v)
            //func After(ns int64) <-chan int64
            //在指定时间段之后，它向返回的channel中传递一个值(当前时间)。
        case <-time.After(time.Second * 3): fmt.Println("timeout.")
        }
        
        w <- true 
    }()
    
    // c <- 1       // 注释掉，从而引发 timeout
    <-w 
}
```

<h2 id="7012283f647776697633c244ec95b9de"></h2>

##### channel 可传参(内部实现为指针), 或 作为 结构成员

