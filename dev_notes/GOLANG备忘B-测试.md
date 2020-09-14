...menustart

- [调试](#b7c0bfff1b6f1cc255716a1cb8b68011)
    - [1.GDB](#6d2dd9e13619a9a30d228258e738bf79)
    - [2. Data Race](#083909d82e2fa7cbd29182329ca0af32)
- [测试](#db06c78d1e24cf708a14ce81c9b617ec)
    - [自带代码测试,性能测试,覆盖率测试框架](#cdc2fd32f8686b30a27eec945d4c89c2)
    - [1. Test](#3e6d52aaaab83cf1b430ee1b852f8e80)
        - [使用 testing.T 的相关方法 决定测试流程和状态](#7c48b716c9cbed3ac77ee9481f9719ef)
        - [默认go test执行所有单元测试函数,支持go build参数](#3dc0daaccf38c2fd1bccb719ea603476)
        - [可重写TestMain 函数,处理一下setup/teardown操作](#87e041bd083f49e8f03c0ce9d75a0fbc)
    - [2. Benchmark](#0dfe3eaa7457f42ed65afa33b3ecd757)
        - [性能测试要运行足够多的次数](#9f368a8263892b3eb1f42391a23c7599)
        - [go test不会执行性能测试函数,需使用-bench 参数](#286254b85491398b07fecc79b0948033)
    - [3. Example](#e9c87d7875b48b0611d47da7800c61ae)
    - [4. Cover](#1ac8a0cb44c8a5041acb4e1695082370)
        - [用浏览器输出结果](#86823af6f0061332b23b9d012396126c)
    - [5.PProf](#8bf6fd1319c5c9eba78d6baae4e82d9f)

...menuend


<h2 id="b7c0bfff1b6f1cc255716a1cb8b68011"></h2>


# 调试

<h2 id="6d2dd9e13619a9a30d228258e738bf79"></h2>


## 1.GDB

默认情况下,编译的二进制文件已经包含 DWARFv3调试信息.

只要GDB 7.1以上版本都可以调试

相关选项

- 调试: 禁用内联和优化 -gcflags "-N -l"
- 发布: 删除调试信息和符号表 -ldflags "-w -s"


除了使用 GDB 断点命令外，还可以使用runtime.Breakpoint函数触发中断. 

另外，runtime/debug.PrintStack 可以用来输出调用堆栈信息.


<h2 id="083909d82e2fa7cbd29182329ca0af32"></h2>


## 2. Data Race

```bash
-race
```

<h2 id="db06c78d1e24cf708a14ce81c9b617ec"></h2>


# 测试

<h2 id="cdc2fd32f8686b30a27eec945d4c89c2"></h2>


##### 自带代码测试,性能测试,覆盖率测试框架

- 测试代码必须保存在 *_test.go 文件
- 测试函数命名符合 TestName格式

`不要将代码放在名为 main的目录下, 会导致go test错误`

<h2 id="3e6d52aaaab83cf1b430ee1b852f8e80"></h2>


## 1. Test

<h2 id="7c48b716c9cbed3ac77ee9481f9719ef"></h2>


##### 使用 testing.T 的相关方法 决定测试流程和状态

testing.T

方法 |  说明 |  其他
--- |  ---  |   ---
Fail    | 标记失败，继续执行
FailNow |   失败,立即停止当前测试函数
Log |   输出信息,仅在失败或 -v参数时输出   | Logf
SkipNow |   跳过当前测试函数    | Skipf=SkipNow + Logf
Error   |   Fail + Log  |   Errorf
Fetal   |   FailNow + Log   |   Fatalf


```go
func TestSum(t *testing.T) {
    time.Sleep(time.Second * 2)
    if sum(1, 2, 3) != 6 {
        t.Fatal("sum error!")
    } 
}
func TestTimeout(t *testing.T) {
    time.Sleep(time.Second * 5)
}    
```

<h2 id="3dc0daaccf38c2fd1bccb719ea603476"></h2>


##### 默认go test执行所有单元测试函数,支持go build参数

参数 |  说明 |  示例
--- |  ---  |   ---
-c  |   仅编译
-v  |   显示所有测试函数执行细节
-run regex  |   执行指定的测试函数
-parallel n |   并发执行测试函数(默认:GOMAXPROCS)
-timeout t  | 单个测试超时时间 |    -timeout 2m30s

```bash
$ go test -v -timeout 3s

=== RUN TestSum
--- PASS: TestSum (2.00 seconds) 
=== RUN TestTimeout
panic: test timed out after 3s 
FAIL  test  3.044s

$ go test -v -run "(?i)sum"

=== RUN TestSum
--- PASS: TestSum (2.00 seconds) 
PASS
ok   test  2.044s
```

<h2 id="87e041bd083f49e8f03c0ce9d75a0fbc"></h2>


##### 可重写TestMain 函数,处理一下setup/teardown操作

```go
func TestMain(m *testing.M) {
    println("setup")
    code := m.Run()
    println("teardown")
    os.Exit(code)
}
func TestA(t *testing.T) {}
func TestB(t *testing.T) {}

func BenchmarkC(b *testing.B) {}
```

```bash
$ go test -v -test.bench .

setup
=== RUN TestA
--- PASS: TestA (0.00s) 
=== RUN TestB
--- PASS: TestB (0.00s) 
PASS
BenchmarkC  2000000000  
teardown
ok   test  0.028s
```

<h2 id="0dfe3eaa7457f42ed65afa33b3ecd757"></h2>


## 2. Benchmark

<h2 id="9f368a8263892b3eb1f42391a23c7599"></h2>


##### 性能测试要运行足够多的次数

```go
func BenchmarkSum(b *testing.B) {
    for i := 0; i < b.N; i++ {
        if sum(1, 2, 3) != 6 {
            b.Fatal("sum")
        }
    } 
}
```

<h2 id="286254b85491398b07fecc79b0948033"></h2>


##### go test不会执行性能测试函数,需使用-bench 参数

参数 |  说明 
--- |  ---  
-bench regex    | 指定性能测试函数集
-benchmem   | 输出内存统计信息
-benchtime t    | 设置每个性能测试运行时间
-cpu    |   设置并发测试,默认 GOMAXPROCS


```bash
$ go test -v -bench .
=== RUN TestSum
--- PASS: TestSum (2.00 seconds)
=== RUN TestTimeout
--- PASS: TestTimeout (5.00 seconds)
PASS

BenchmarkSum 100000000 11.0 ns/op 
ok   test  8.358s

$ go test -bench . -benchmem -cpu 1,2,4 -benchtime 30s
```

<h2 id="e9c87d7875b48b0611d47da7800c61ae"></h2>


## 3. Example

与 testing.T 类似, 区别在于通过捕获 stdout输出来判断测试结果。

```go
func ExampleSum() {
    fmt.Println(sum(1, 2, 3))
    fmt.Println(sum(10, 20, 30))
    // Output:
    // 6
    // 60
}
```

<h2 id="1ac8a0cb44c8a5041acb4e1695082370"></h2>


## 4. Cover

除显示代码覆盖率百分比外，还可输出详细分析记录文件。

参数 |  说明 
--- |  ---  
-cover  |   允许覆盖分析
-covermode |   分析模式 set:是否执行 count:执行次数 atomic: 次数，并发支持
-coverprofile   | 输出结果文件

```bash
$ go test -cover -coverprofile=cover.out -covermode=count

PASS
coverage: 80.0% of statements 
ok   test  0.043s

$ go tool cover -func=cover.out
test.go: Sum 100.0% 
test.go: Add 0.0% 
total:  (statements) 80.0%
```

<h2 id="86823af6f0061332b23b9d012396126c"></h2>


##### 用浏览器输出结果

```bash
$ go tool cover -html=cover.out
```

<h2 id="8bf6fd1319c5c9eba78d6baae4e82d9f"></h2>


## 5.PProf

监控程序执行，找出性能瓶颈

```go
import ( "os"
    "runtime/pprof"
)
func main() {
    // CPU
    cpu, _ := os.Create("cpu.out")
    defer cpu.Close()
    pprof.StartCPUProfile(cpu)
    defer pprof.StopCPUProfile()
    
    // Memory
    mem, _ := os.Create("mem.out")
    defer mem.Close()
    defer pprof.WriteHeapProfile(mem)
}
```

除调用 runtime/pprof 相关函数外, 还可直接用测试命名输出所需记录文件

参数 |  说明 
--- |  ---  
-blockprofile block.out | goroutine 阻塞
-blockprofilerate n |   超出时间n的阻塞才会记录,单位:纳秒
-cpuprofile cpu.out | CPU
-memprofile mem.out | 内存分配
-memprofilerate n   |   超过n的内存分配n被记录,默认512k

以 net/http 包为演示,先生成记录文件

```bash
$ go test -v -test.bench "." -cpuprofile cpu.out -memprofile mem.out net/http
```

进入交互式查看模式

```bash
$ go tool pprof http.test mem.out
```

输出图形文件

```bash
$ go tool pprof -web http.test mem.out
```

还可用 net/http/pprof 实时查看 runtime profiling信息

```go
package main
import (
    _ "net/http/pprof"
    "net/http"
    "time" 
)
func main() {
    go http.ListenAndServe("localhost:6060", nil)
    for {
        time.Sleep(time.Second)
    } 
}
```

在浏览器中查看

```
http://localhost:6060/debug/pprof/
```

