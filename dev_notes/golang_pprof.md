[](...menustart)

- [使用 pprof 测试 golang 应用性能](#8ec32b199f9a9a6ce8a763ba4073c7d0)
    - [Profiling](#1a226c2f1347809a185b8567ba1fc5a7)
    - [收集方式](#2de72cd86d6ee0cf5da415280e9faeb6)
        - [工具型应用](#d2d36738c9707ef71ede62277101dad5)
        - [服务型应用](#743a11634b020d87ee3e35723fd383d0)
    - [分析 Profiling](#2dc9540acc752760e72345ad9529d612)
        - [go 1.10 提供了一个 web UI， 同时支持 火焰图](#628f3bfbcd42ebb9c0e60322c9cdfce8)
    - [和go test files 的集成](#f6876b634c1b05222f8af0f08779c5bb)

[](...menuend)


<h2 id="8ec32b199f9a9a6ce8a763ba4073c7d0"></h2>

# 使用 pprof 测试 golang 应用性能

<h2 id="1a226c2f1347809a185b8567ba1fc5a7"></h2>

## Profiling

 1. CPU profile
 2. Memory Profile（Heap Profile）
 3. Block Profiling：报告 goroutines 不在运行状态的情况，可以用来分析和查找死锁等性能瓶颈
 4. Goroutine Profiling：报告 goroutines 的使用情况，有哪些 goroutine，它们的调用关系是怎样的

<h2 id="2de72cd86d6ee0cf5da415280e9faeb6"></h2>

## 收集方式

 1. `runtime/pprof`
 2. `net/http/pprof`
 3. `go test`

<h2 id="d2d36738c9707ef71ede62277101dad5"></h2>

### 工具型应用

- 如果你的应用是一次性的，运行一段时间就结束。那么最好的办法，就是在应用退出的时候把 profiling 的报告保存到文件中，进行分析。
- 对于这种情况，可以使用 runtime/pprof 库。
- pprof 封装了很好的接口供我们使用.

- 比如要想进行 CPU Profiling，可以调用 pprof.StartCPUProfile() 方法
    - 它会对当前应用程序进行 CPU profiling，并写入到提供的参数中（w io.Writer），要停止调用 StopCPUProfile() 即可.

```go
// 一般写在写在 main.go 文件中
f, err := os.Create(*cpuprofile)
if err != nil {
    log.Fatal("could not create CPU profile: ", err)
}
if err := pprof.StartCPUProfile(f); err != nil {
    log.Fatal("could not start CPU profile: ", err)
}
defer pprof.StopCPUProfile()
```

- 要获得内存的数据，直接使用 WriteHeapProfile 就行, 不用 start 和 stop 这两个步骤了：

```go
f, err := os.Create(*memprofile)
pprof.WriteHeapProfile(f)
f.Close()
```

<h2 id="743a11634b020d87ee3e35723fd383d0"></h2>

### 服务型应用

- 如果你的应用是一直运行的，比如 web 应用，那么可以使用 net/http/pprof 库, 它提供 HTTP 服务进行分析
- 1. [推荐] 如果使用了默认的 http.DefaultServeMux（通常是代码直接使用 `http.ListenAndServe("0.0.0.0:8000", nil)` ) ，只需要添加一行：
    - `import _ "net/http/pprof"`
- 2. 如果你使用自定义的 Mux，则需要手动注册一些路由规则： 比如
    - 不推荐
    - 
    ```go
    // r.HandleFunc("/debug/pprof/", pprof.Index) // must end with '/' 
    // r.HandleFunc("/debug/pprof/cmdline", pprof.Cmdline)
    // r.HandleFunc("/debug/pprof/profile", pprof.Profile)
    // r.HandleFunc("/debug/pprof/symbol", pprof.Symbol)
    // r.HandleFunc("/debug/pprof/trace", pprof.Trace)
    ```

- 即便你是 第2中情况， 你依然可以 额外启动一个 http 服务 来提供 pprof

```go
import _ "net/http/pprof 

...

go func() {
    log.Println(http.ListenAndServe("localhost:6060", nil))
}()
```


- 不管哪种方式，你的 HTTP 服务都会多出 `/debug/pprof/` endpoint，访问它会得到类似下面的内容：

```html
/debug/pprof/

profiles:
0    block
62    goroutine
444    heap
30    threadcreate

full goroutine stack dump
```

- 这个路径下还有几个子页面：
    - /debug/pprof/profile：访问这个链接会自动进行 CPU profiling，持续 30s，并生成一个文件供下载
    - /debug/pprof/heap： Memory Profiling 的路径，访问这个链接会得到一个内存 Profiling 结果的文件
    - /debug/pprof/goroutines：运行的 goroutines 列表，以及调用关系
    - ... 


<h2 id="2dc9540acc752760e72345ad9529d612"></h2>

## 分析 Profiling 

- `go tool pprof` 命令行工具
    - 如果要生成调用关系 和 火焰图， 需要安装 graphviz .
- 使用方式为 `go tool pprof [binary] <source>`
    - binary 是 应用程序的二进制文件， 用来解析各种符号 
    - source 表示 profile 数据的来源，  可以是本地的文件，也可以是 http 地址， 比如
    - `go tool pprof ./hyperkube http://172.16.3.232:10251/debug/pprof/profile`
    - 这个命令会进行 CPU profiling 分析，等待一段时间（默认是 30s，如果在 url 最后加上 ?seconds=60 参数可以调整采集数据的时间为 60s）. 之后，我们就进入了一个交互式命令行，可以对解析的结果进行查看和导出。
        - 可以通过 help 来查看支持的自命令有哪些。
        - 一个有用的命令是 topN，它列出最耗时间的地方： 比如 top10
        - web 命令 ： 在交互模式下输入 web，就能自动生成一个 svg 文件，并跳转到浏览器打开，生成了一个函数调用图.
    - 要想更细致分析，就要精确到代码级别了，看看每行代码的耗时，直接定位到出现性能问题的那行代码。
        - list 命令后面跟着一个正则表达式，就能查看匹配函数的代码以及每行代码的耗时： `list yourCodeRegularExpression`
        - `weblist <regex>`  打开一个页面，同时显示源码 和 汇编代码
- NOTE：
    - 更详细的 pprof 使用方法可以参考 pprof --help 或者 [pprof 文档](https://github.com/google/pprof/tree/master/doc)
- tips
    - 如果应用比较复杂，生成的调用图特别大，看起来很乱，有两个办法可以优化：
        - 使用 web funcName 的方式，只打印和某个函数相关的内容
        - 运行 go tool pprof 命令时加上 `--nodefration=0.05` 参数，表示如果调用的子函数使用的 CPU、memory 不超过 5%，就忽略它，不要显示在图片中

<h2 id="628f3bfbcd42ebb9c0e60322c9cdfce8"></h2>

### go 1.10 提供了一个 web UI， 同时支持 火焰图

- 启动 pprof web ui:

```bash
$ go tool pprof -http=:8080 [binary] profile.out
```



<h2 id="f6876b634c1b05222f8af0f08779c5bb"></h2>

## 和go test files 的集成

- go test 命令有两个参数和 pprof 相关，它们分别指定生成的 CPU 和 Memory profiling 保存的文件：
    - -cpuprofile：cpu profiling 数据要保存的文件地址
    - -memprofile：memory profiling 数据要报文的文件地址
- 比如下面执行go test的同时，也会执行 CPU profiling，并把结果保存在 cpu.prof 文件中：
    - `$ go test -bench . -cpuprofile=cpu.prof`
- 执行结束之后，就会生成 main.test 和 cpu.prof 文件。要想使用 go tool pprof，需要指定的二进制文件就是 main.test。
- 等效于上面的CPU profile等 



# How to read pprof ?

https://blog.pickme.lk/how-to-get-profiling-right-with-go-813ff89d4757


## 1. top command 

```bash
(pprof) top
Showing nodes accounting for 3816, 100% of 3816 total
Showing top 10 nodes out of 27
      flat  flat%   sum%        cum   cum%
      2521 66.06% 66.06%       2521 66.06%  runtime.malg
       910 23.85% 89.91%        910 23.85%  runtime.allocm
       257  6.73% 96.65%        257  6.73%  bufio.NewWriterSize (inline)
       128  3.35%   100%        128  3.35%  syscall.copyenv
         0     0%   100%        257  6.73%  net/http.(*conn).serve
         0     0%   100%        257  6.73%  net/http.newBufioWriterSize
```

#### Flat and Cumulative?

- Flat means the amount of resources used in the function itself. 
- Cumulative is the total amount of resources used in the function **and the calling functions down the call stack**.

- `sum%` is basically the total of `flat%`
    - e.g. , `66.06% + 23.85% = 89.91%`
    - e.g. , `66.06% + 23.85% + 6.73% = 96.65%`


## 2. list command

```bash
(pprof) list runtime.malg
Total: 3816
ROUTINE ======================== runtime.malg in /usr/local/Cellar/go/1.19.1/libexec/src/runtime/proc.go
      2521       2521 (flat, cum) 66.06% of Total
         .          .   4063:	execLock.unlock()
         .          .   4064:}
         .          .   4065:
         .          .   4066:// Allocate a new g, with a stack big enough for stacksize bytes.
         .          .   4067:func malg(stacksize int32) *g {
      2521       2521   4068:	newg := new(g)
         .          .   4069:	if stacksize >= 0 {
         .          .   4070:		stacksize = round2(_StackSystem + stacksize)
         .          .   4071:		systemstack(func() {
         .          .   4072:			newg.stack = stackalloc(uint32(stacksize))
         .          .   4073:		})
```


## 3. web command

The above command will open the call-graph in a web-view( it wil open your browser ).


## 4. The `weblist` command

something like `list` to `web` browser ...

```bash
(pprof) help weblist
Display annotated source in a web browser
  Usage:
    weblist<func_regex|address> [-focus_regex]* [-ignore_regex]*
    Include functions matching func_regex, or including the address specified.
    Include samples matching focus_regex, and exclude ignore_regex.
```



