# 并发

    7.1 Goroutine
        修改 runtime.GOMAXPROCS, 改变用语服务goroutine的线程数量
        runtime.Goexit 将⽴即终止当前 goroutine 执行，defer语句会确保被调用
        Gosched 让出底层线程, 等待下次被调度执行, 和协程 y ield 作⽤用类似
    7.2 Channel
        channel 是类似 pipe 的单/双向数据管道。
        Channel 是一个类型的通道, 通过 <- 操作符 传输数据
        必须使用 make 创建 , ch := make(chan int)
        默认同步模式 , 需要发送和接收配对
        异步模式, 通道缓冲 , ch := make(chan int, 100)
        缓冲区是内部属性,并非类型 构成要素
        发送方 可以关闭通道， 接收方可以 测试 通道 是否被关闭
        可以在channel上 使用 range
        向 closed channel 发送数据引发 panic 错误, 接收则返回零值
        nil channel, 无论收发都会被阻塞
        内置函数 len 返回未被读取的缓冲元素数量, cap 返回缓冲区大小
    7.2.1 单向
        可以将 channel 隐式转换为单向队列, 只收或只发, 反之出错
    7.2.2 选择 select
        select 随机选择一个可用的channel 做收发操作, 或执行default case
        select 会阻塞， 直到有一个 case 可以run
        在循环中使用 select default case 需要小心,避免形成洪水
    7.2.3 模式
        简单⼯工⼚厂模式打包并发任务和 channel
        用 channel 实现信号量 (semaphore)
        用 closed channel 发出退出通知 ( closed channel接受不会阻塞 )
        用 select 实现超时 (timeout)
        channel 可传参(内部实现为指针), 或 作为 结构成员


## 7.1 Goroutine

```go
go func() {
    println("Hello, World!")
}()
```

##### 修改 runtime.GOMAXPROCS, 改变用语服务goroutine的线程数量

```go
//1.5 已经默认使用 runtime.NumCPU()
runtime.GOMAXPROCS(runtime.NumCPU())
```

##### runtime.Goexit 将⽴即终止当前 goroutine 执行，defer语句会确保被调用

```go
runtime.Goexit()
```

##### Gosched 让出底层线程, 等待下次被调度执行, 和协程 y ield 作⽤用类似

```go
runtime.Gosched()
```


## 7.2 Channel

##### channel 是类似 pipe 的单/双向数据管道。

    从设计上确保,在同⼀时刻,只有⼀个 goroutine能从中接收数据。
    发送和接收都是原⼦子操作,不会中断,只会失败。

##### Channel 是一个类型的通道, 通过 <- 操作符 传输数据

```go
ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and assign value to v.
<-c // 接收数据，丢弃
```

##### 必须使用 make 创建 , ch := make(chan int)

```go
ch := make(chan int)
```

##### 默认同步模式 , 需要发送和接收配对

    发送接收操作会造成阻塞， 支持另一方准备好
    1) 在一个channel上的发送操作会阻塞，直到该channel上有一个接收者就绪。
    2) 在一个channel上到的接收操作会阻塞，直到该channel上有一个发送者就绪。

##### 异步模式,  通道缓冲 , ch := make(chan int, 100)
    
```go
ch := make(chan int, 100)
```

    发送数据只有当通道缓冲满 的时候才会阻塞
    同样的， 当通道缓冲空的时候，接收操作会阻塞
    

    异步 channel 可减少排队阻塞,具备更高的效率。
    但应该考虑使用指针规避 大对象拷⻉,
    将多个元素打包,减小缓冲区大小等.

##### 缓冲区是内部属性,并非类型 构成要素

```go
var a, b chan int = make(chan int), make(chan int, 3)
```

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

##### 可以在channel上 使用 range 
```go
for value := range <-ch {
    use(value)
}
```

##### 向 closed channel 发送数据引发 panic 错误, 接收则返回零值
---
##### nil channel, 无论收发都会被阻塞
---
##### 内置函数 len 返回未被读取的缓冲元素数量, cap 返回缓冲区大小

---
### 7.2.1 单向

##### 可以将 channel 隐式转换为单向队列, 只收或只发, 反之出错

```go
c := make(chan int, 3)

var send chan<- int = c  // send-only 
var recv <-chan int = c  // receive-only

send <- 1
<-recv
```


### 7.2.2 选择 select

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
##### select 会阻塞， 直到有一个 case 可以run 
---
##### 在循环中使用 select default case 需要小心,避免形成洪水


---
### 7.2.3 模式

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

##### channel 可传参(内部实现为指针), 或 作为 结构成员

