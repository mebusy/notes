...menustart

 - [Common](#d13bc5b68b2bd9e18f29777db17cc563)
     - [multiple characters replacement](#092987d14c5ea50ca1043604d333f7f7)
     - [Ternary expression](#50ac00ef46e6ca65b6eda7d8fbc3d3eb)
     - [How to find out which types implement ByteReader interface in golang pkg ?](#2929210b0e8a534b0f6389e8de130779)
     - [don't use alias for enums 'cause this breaks type safety](#c81f40d0d79a6378c73da8285af6a87f)
     - [the short form for slice initialization is `a := \[\]T{}`](#1a2da25898c4fd8e23e5530a6d1676c4)
         - [the zero value of a slice is nil](#3b74cf78eee2b1bdb3ac72e39aa0b9ec)
     - [use `%+v` to print data with sufficient details](#3fb8e7e955dd2ef147753428825decc1)
     - [using range loop to iterate over array or slice](#226081b0fa35e5ae1ca0233b34285901)
     - [comparing timestamps by using `time.Before` or `time.After`.](#a5e5af3efeb419f96f350782021e2e41)
     - [be careful with empty struct `struct{}`](#9b63cdf4a17f6bc00c607ce0b8c34e62)
     - [be careful with range in Go](#96d33eb12c7b98e7c443951fcd4bd31b)
     - [reading nonexistent key from map will not panic](#cc01793243c2fa1852f2972d1adf0972)
     - [simple random element from a slice](#efcd04c1f0dae7d0002c6671eed2d378)
 - [Concurrency](#3e48afddb0c5521684b8d2687b0869d6)
     - [T12 inherits the mutex lock , YES anonymous structs are cool](#b27f2b80be1e9c908fcec253c881177c)
     - [T14 Closing channels](#949c5b9f71365fae2a311ff363602d87)
         - [use chan struct{} to pass signal, chan bool makes it less clear](#38d57280e166d4e78ace55c47bd88624)
     - [T15 Locking with buffered channels (size of 1, to replace Lock)](#34f46f2a72a5a37dbfa0c051251e6d91)
     - [best candidate to make something once in a thread-safe way is sync.Once](#61585cd8a4eb857f05a268dded0d9196)
     - [concurrency-safe](#fe89095a25ed4db8aa993b7f4e45d1cb)
 - [Error](#902b0d55fddef6f8d651fe1035b7d4bd)
     - [T17 Use custom error types to return additional information](#d1de0b2cb3348dca42f909c843dcf5bc)
         - [Or use to wrap an error](#65263ac49cb63677beb20a5cefd0791d)
     - [T18 Error variables , create errors as package-scoped variables and reference those variables](#87b731d7e572733aa294fbdd8513c9e0)
     - [Panics and goroutines](#d3679e82565b6cc42c359a29ad5c8ffd)
     - [use panic only in very specific situations, you have to handle error](#88d00ec4fe58aa422b9c3e2fd7eac2a0)
 - [Debug & Test](#4582db50ce6fbe4c2d279f27c53a8741)
     - [Accessing stack traces](#ede22a82337ad92405e2e3f2875d248f)
     - [dump goroutines](#0615f6469476f5c64c9c20eae6348a7b)
     - [to get call stack we've runtime.Caller](#826c20b622dd27722a65b20623a45754)
     - [Generative testing , random test edge cases](#3338f48367f6f6923613b593a7e0749b)
     - [30 Parallel benchmarks  and race detection](#c5a9149a4c668ac9542a3eabd9078d5d)
     - [easy way to split test into different builds](#a9928fbcd297bb4fb75ea5528df8edad)
 - [Web Cloud and Micro Service](#909dbd9520809eab1b9f3c2544d7e831)
     - [T9 URL Faster routing](#172a5c78b32d6fc444e4d1c3b61744d2)
     - [T49 Detecting timeouts](#9b750e13615f6e945e21136f2486944e)
     - [T50 resuming download with HTTP](#5864385d2a98ac5198627d336c9e3215)
     - [T58 detect IP addr on the host](#70d85a28319eb9789bccde5293aeef77)
     - [T59 Detecting where depend command exists on host](#93f6310cc55bf4890ceb40446c51d45d)
     - [T60 Batch Cross-compiling](#60ee39b263dfd49c2df587ebd0603552)
     - [T61 Monitoring the Go runtime](#d229185d44acbaf8549510f633db7bbf)
     - [T62 Reusing connections](#127f2f792279fa876b89569831a2170a)
     - [T63 Faster JSON marshal and unmarshal](#5671e185bb514a943cc0340216a81cbf)
     - [httputil.DumpRequest is very useful thing, don't create your own](#6807f9517e74e39fcdde04bee03bd940)
 - [Reflection](#aea1e492943ccbad7ee270ec1e064758)
     - [T70 Generating code with go generate](#490e9ac4eae32799c8876c485d61477f)
 - [Performance](#9446a98ad14416153cc4d45ab8b531bf)
     - [Do NOT overuse fmt.Sprintf in your hot path.](#f2e1d768493590d77cb642c9efb98268)
     - [always discard body e.g. `io.Copy(ioutil.Discard, resp.Body)`  if you don't use it](#a7701ee1968dee6ec433541b590f0d44)
     - [don't use defer in a loop or you'll get a small memory leak](#8081b8d04a6f4d4ee17eeca49c63613a)
     - [don't forget to stop ticker, unless you need a leaked channel](#3b9ec32447f983783ee40bcb4e2448fe)
     - [`sync.Map` isn't a silver bullet, do not use it without a strong reasons](#543e9d26325c59e0d80371ab11f03a3e)
     - [to hide a pointer from escape analysis you might carefully(!!!) use this func:](#457a0f3166a881858238dadb30c3b00d)
     - [for fastest atomic swap you might use this `m := (*map\[int\]int)(atomic.LoadPointer(&ptr))`](#81d856f273cef05d6d36437fb6770bc8)
     - [use buffered I/O if you do many sequential reads or writes](#ad7dad3c5b207cff2caf801d111437d3)
     - [there are 2 ways to clear a map:](#869e770545ab96a38832ba21ea6e9199)
 - [Build](#c74c1f42f141c011ca6bd8b1114fc3d0)
     - [strip your binaries with this command go build -ldflags="-s -w" ...](#822c1164685d599334ea5584d4638941)
     - [tiniest Go docker image](#e34c20517da18245d8e7fe706febc368)
     - [check if there are mistakes in code formatting `diff -u <(echo -n) <(gofmt -d .)`](#1695cd016ed1ed01d8ff7cecde62d867)
     - [check interface implementation during compilation](#fbc04a03c1a5ee00e1b416744fb3154b)
 - [sql](#ac5c74b64b4b8352ef2f181affb5ac2a)
     - [where in](#cca85d15132b75981103827efd17081b)
     - [Scan rows to struct](#b589b58d1c70513bf77a35c489473590)
     - [Parameter Placeholder Syntax](#f546c79ad1cdb480d0e3df44316a5a29)
     - [数据库操作](#1475e8cb4633b25db26bd0b484bfc45f)
         - [多行查询](#c8c95af3e4422ec0c4e188c720d67079)
         - [单行查询](#520a0fe1e028d3bfd9e80f3d51311100)
         - [插入数据](#131d2cc4055f927cc5f593ebb1042224)
         - [其他](#0d98c74797e49d00bcc4c17c9d557a2b)
         - [事务](#9f82401d0ae9254f9429eaa46e1fe666)
 - [Misc](#74248c725e00bf9fe04df4e35b249a19)
     - [regexp , reference captured group](#ae4367a7f966679339c605ac0b009418)
     - [CGO_ENALBE=1 情况下, 实现纯静态连接](#12f3c642086ddb0279f69574a34db7ef)
     - [BASH: auto add current path to GOPATH when opening a new terminal window](#b052a32a028f65a554fd6d75ca2cb331)
     - [go time format](#d631c51d63e223eda44e441f1ce4c0ac)

...menuend


**Go Tips**

<h2 id="d13bc5b68b2bd9e18f29777db17cc563"></h2>


# Common

<h2 id="092987d14c5ea50ca1043604d333f7f7"></h2>


## multiple characters replacement

```go
r := strings.NewReplacer("(", "", ")", "")
fmt.Println( r.Replace( "a(b)c)d" )  )
```

<h2 id="50ac00ef46e6ca65b6eda7d8fbc3d3eb"></h2>


## Ternary expression

```go
func If(condition bool, trueVal, falseVal interface{}) interface{} {  
    if condition {
        return trueVal
    }
    return falseVal
}

// If(i==0,"A","B").(string)
```

<h2 id="2929210b0e8a534b0f6389e8de130779"></h2>


## How to find out which types implement ByteReader interface in golang pkg ?

```
https://golang.org/search?q=ReadByte
```


<h2 id="c81f40d0d79a6378c73da8285af6a87f"></h2>


## don't use alias for enums 'cause this breaks type safety

```go
package main
type Status = int
type Format = int // remove `=` to have type safety

const A Status = 1
const B Format = 1

func main() {
    println(A == B)   // true
}
```

<h2 id="1a2da25898c4fd8e23e5530a6d1676c4"></h2>


## the short form for slice initialization is `a := []T{}`

<h2 id="3b74cf78eee2b1bdb3ac72e39aa0b9ec"></h2>


### the zero value of a slice is nil

```
var s []int
fmt.Println(s, len(s), cap(s))
if s == nil {
    fmt.Println(s, "is nil!")
}
// Output:
// [] 0 0
// [] is nil!

var a []string
b := []string{}
fmt.Println( a==nil, b==nil )
fmt.Println(reflect.DeepEqual(a, []string{}))
fmt.Println(reflect.DeepEqual(b, []string{}))
// Output:
// true false
// false
// true
```


<h2 id="3fb8e7e955dd2ef147753428825decc1"></h2>


## use `%+v` to print data with sufficient details


<h2 id="226081b0fa35e5ae1ca0233b34285901"></h2>


## using range loop to iterate over array or slice 

```go
for _, c := range a[3:7] {...}
```

<h2 id="a5e5af3efeb419f96f350782021e2e41"></h2>


## comparing timestamps by using `time.Before` or `time.After`.

<h2 id="9b63cdf4a17f6bc00c607ce0b8c34e62"></h2>


## be careful with empty struct `struct{}`

```go
func f1() {
    var a, b struct{}
    print(&a, "\n", &b, "\n") // Prints same address
    fmt.Println(&a == &b)     // Comparison returns false
}

func f2() {
    var a, b struct{}
    fmt.Printf("%p\n%p\n", &a, &b) // Again, same address
    fmt.Println(&a == &b)          // ...but the comparison returns true
}
```

<h2 id="96d33eb12c7b98e7c443951fcd4bd31b"></h2>


## be careful with range in Go

 - `for i := range a` and `for i, v := range &a` doesn't make a copy of a
 - but `for i, v := range` a does

<h2 id="cc01793243c2fa1852f2972d1adf0972"></h2>


## reading nonexistent key from map will not panic 

 - `value := map["no_key"]` will be zero value
 - `value, ok := map["no_key"]` is much better

<h2 id="efcd04c1f0dae7d0002c6671eed2d378"></h2>


## simple random element from a slice

```go
[]string{"one", "two", "three"}[rand.Intn(3)]
```




<h2 id="3e48afddb0c5521684b8d2687b0869d6"></h2>


# Concurrency

<h2 id="b27f2b80be1e9c908fcec253c881177c"></h2>


## T12 inherits the mutex lock , YES anonymous structs are cool

```go
type words struct {
    sync.Mutex
    found map[string]int
}

func (w *words) add(word string, n int) {
    w.Lock()
    defer w.Unlock()
    ...
}
```

<h2 id="949c5b9f71365fae2a311ff363602d87"></h2>


## T14 Closing channels

 - write(send) to a closed channel will cause **panic**
    - the close function should be **called only by a sender**
 - when receiver has done, it should notify the sender that sender can safely close the channel now
 - implementation:
    - sender should take 2 channel, for example:
        - `msg` channel: for messages
        - `done` channel: the other is for notification 
    - when receiver is done, nofity the sender,  and now sender can close the channle safely

<h2 id="38d57280e166d4e78ace55c47bd88624"></h2>


### use chan struct{} to pass signal, chan bool makes it less clear



<h2 id="34f46f2a72a5a37dbfa0c051251e6d91"></h2>


## T15 Locking with buffered channels (size of 1, to replace Lock)


<h2 id="61585cd8a4eb857f05a268dded0d9196"></h2>


## best candidate to make something once in a thread-safe way is sync.Once

 - don't use flags, mutexes, channels or atomics

<h2 id="fe89095a25ed4db8aa993b7f4e45d1cb"></h2>


## concurrency-safe

 - In general the rule is this: 
    - top-level functions like strings.Split or fmt.Printf or rand.Int63 may be called from any goroutine at any time
        - (otherwise programming with them would be too restrictive)
    - but objects you create (like a new bytes.Buffer or rand.Rand) must only be used by one goroutine at a time unless otherwise noted 
        - (like net.Conn's documentation does).


<h2 id="902b0d55fddef6f8d651fe1035b7d4bd"></h2>


# Error

<h2 id="d1de0b2cb3348dca42f909c843dcf5bc"></h2>


## T17 Use custom error types to return additional information

<h2 id="65263ac49cb63677beb20a5cefd0791d"></h2>


### Or use to wrap an error 

```
$ go get github.com/pkg/errors
```

```go
errors.Wrap(err, "additional message to a given error")
```

<h2 id="87b731d7e572733aa294fbdd8513c9e0"></h2>


## T18 Error variables , create errors as package-scoped variables and reference those variables

```go
var ErrTimeout = errors.New("The request timed out") 

return "", ErrTimeout
```

<h2 id="d3679e82565b6cc42c359a29ad5c8ffd"></h2>


## Panics and goroutines

 - If a panic on a goroutine goes unhandled on that goroutine’s call stack, it crashes the entire program
 - `github.com/Masterminds/cookoo/safely`
    - `safely.Go( xxxx )`

<h2 id="88d00ec4fe58aa422b9c3e2fd7eac2a0"></h2>


## use panic only in very specific situations, you have to handle error



<h2 id="4582db50ce6fbe4c2d279f27c53a8741"></h2>


# Debug & Test 

<h2 id="ede22a82337ad92405e2e3f2875d248f"></h2>


## Accessing stack traces

```go
import (
    "runtime/debug"
)

func bar() {
    debug.PrintStack()
}
```

```go
import (
    "runtime"
)
func bar() {
    // Makes a buffer
    buf := make([]byte, 1024)
    // Writes the stack into the buffer
    runtime.Stack(buf, false)
    // Prints the results
    fmt.Printf(“Trace:\n %s\n", buf)
}
```

<h2 id="0615f6469476f5c64c9c20eae6348a7b"></h2>


## dump goroutines 

 - To mimic the Java behaviour of stack-dump on SIGQUIT but still leaving the program running:

```go
go func() {
sigs := make(chan os.Signal, 1)
      signal.Notify(sigs, syscall.SIGQUIT)
      buf := make([]byte, 1<<20)
      for {
          <-sigs
          stacklen := runtime.Stack(buf, true)
          log.Printf("=== received SIGQUIT ===\n*** goroutine dump...\n%s\n*** end\n", buf[:stacklen])
      }
}()
```

 - On `*NIX` systems (including OSX) send a signal abort SIGQUIT:
    - `pkill -SIGQUIT program_name`
 - [stackoverflow discussion](https://stackoverflow.com/questions/19094099/how-to-dump-goroutine-stacktraces/27398062#27398062)


<h2 id="826c20b622dd27722a65b20623a45754"></h2>


## to get call stack we've runtime.Caller


 - https://golang.org/pkg/runtime/#Caller

```go
func Caller(skip int) (pc uintptr, file string, line int, ok bool)
```
        
<h2 id="3338f48367f6f6923613b593a7e0749b"></h2>


## Generative testing , random test edge cases

 - `testing/quick`

```go
// assume your Pad function always return 
// a string with given length
func Pad(s string, max uint) string {
    ...
}

func TestPadGenerative(t *testing.T) {
    // fn takes a string and a uint8,
    // runs Pad(), and checks that
    // the returned length is right.
    fn := func(s string, max uint8) bool {
        p := Pad(s, uint(max))
        return len(p) == int(max)
    }
    // Using testing/quick, you tell it to
    // run no more than 200
    // randomly generated tests of fn
    if err := quick.Check(fn, &quick.Config{MaxCount: 200}); err != nil {
        // You report any errors throug
        // the normal testing package
        t.Error(err)
    }
}
```


<h2 id="c5a9149a4c668ac9542a3eabd9078d5d"></h2>


## 30 Parallel benchmarks  and race detection

```
$ go test -bench . -cpu=1,2,4
```

```
$ go test -bench . -race -cpu=1,2,4
```


<h2 id="a9928fbcd297bb4fb75ea5528df8edad"></h2>


## easy way to split test into different builds 

 - use `// +build integration` and run them with `go test -v --tags integration` .


<h2 id="909dbd9520809eab1b9f3c2544d7e831"></h2>


# Web Cloud and Micro Service

<h2 id="172a5c78b32d6fc444e4d1c3b61744d2"></h2>


## T9 URL Faster routing

```
github.com/gorilla/mux
```

<h2 id="9b750e13615f6e945e21136f2486944e"></h2>


## T49 Detecting timeouts

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_8.md#ed8f378a99622e6fa9e881ad40b1ee0a

<h2 id="5864385d2a98ac5198627d336c9e3215"></h2>


## T50 resuming download with HTTP

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_8.md#9828258f9f00dd06f2a1b4105c62f4d6


<h2 id="70d85a28319eb9789bccde5293aeef77"></h2>


## T58 detect IP addr on the host

```go
func main() {
    name, err := os.Hostname()
    if err != nil {
        fmt.Println(err)
        return
    }
    // Looks up the IP addresses
    // associated with the hostname
    addrs, err := net.LookupHost(name)
    if err != nil {
        fmt.Println(err)
        return
    }
    // Prints each of the IP addresses,
    // as there can be more than one
    for _, a := range addrs {
        fmt.Println(a)
    }
}
```

<h2 id="93f6310cc55bf4890ceb40446c51d45d"></h2>


## T59 Detecting where depend command exists on host

```go
func checkDep(name string) error {
    // Checks whether the passed-in dependency 
    // is in one of the PATHs. 
    if _, err := exec.LookPath(name); err != nil {
        es := "Could not find '%s' in PATH: %s"
        return fmt.Errorf(es, name, err)
    }
    return nil
}
```

<h2 id="60ee39b263dfd49c2df587ebd0603552"></h2>


## T60 Batch Cross-compiling

```
$ go get -u github.com/mitchellh/gox
$ gox \
  -os="linux darwin windows " \
  -arch="amd64 386" \
  -output="dist/{{.OS}}-{{.Arch}}/{{.Dir}}" .
```

<h2 id="d229185d44acbaf8549510f633db7bbf"></h2>


## T61 Monitoring the Go runtime

```go
// Listing 9.9 Monitor an application’s runtime
func monitorRuntime() {
    log.Println("Number of CPUs:", runtime.NumCPU())
    m := &runtime.MemStats{}
    for {
        r := runtime.NumGoroutine()
        log.Println("Number of goroutines", r)
        runtime.ReadMemStats(m)
        log.Println("Allocated memory", m.Alloc)
        time.Sleep(10 * time.Second)
    }
}
```

<h2 id="127f2f792279fa876b89569831a2170a"></h2>


## T62 Reusing connections

 - Go tries to reuse connections out of the box.
 - **It’s the patterns in an application’s code that can cause this to not happen.**, for example:
    - one response body not being closed before another HTTP request is made.
        - **ALWAYS close http body**
    - custom `http.Transport` without `Dial` property in which the `KeepAlive` is set.

```
tr := &http.Transport{
     TLSClientConfig:    &tls.Config{RootCAs: pool},
     DisableCompression: true,
     Dial: (&net.Dialer{
            Timeout:   30 * time.Second,
            KeepAlive: 30 * time.Second,
     }).Dial,
}
```

<h2 id="5671e185bb514a943cc0340216a81cbf"></h2>


## T63 Faster JSON marshal and unmarshal

```
$ go get -u github.com/ugorji/go/codec/codecgen
```

<h2 id="6807f9517e74e39fcdde04bee03bd940"></h2>


## httputil.DumpRequest is very useful thing, don't create your own

 - https://godoc.org/net/http/httputil#DumpRequest

```go
func DumpRequest(req *http.Request, body bool) ([]byte, error)
```


<h2 id="aea1e492943ccbad7ee270ec1e064758"></h2>


# Reflection

<h2 id="490e9ac4eae32799c8876c485d61477f"></h2>


## T70 Generating code with go generate

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_11.md#eb80f5b52be56947902eca88e1c67eb4


<h2 id="9446a98ad14416153cc4d45ab8b531bf"></h2>


# Performance

<h2 id="f2e1d768493590d77cb642c9efb98268"></h2>


## Do NOT overuse fmt.Sprintf in your hot path. 
 - It is costly due to maintaining the buffer pool and dynamic dispatches for interfaces.
 - if you are doing fmt.Sprintf("%s%s", var1, var2), consider simple string concatenation.
 - if you are doing fmt.Sprintf("%x", var), consider using hex.EncodeToString or strconv.FormatInt(var, 16)


<h2 id="a7701ee1968dee6ec433541b590f0d44"></h2>


## always discard body e.g. `io.Copy(ioutil.Discard, resp.Body)`  if you don't use it

 - HTTP client's Transport will not reuse connections unless the body is read to completion and closed

<h2 id="8081b8d04a6f4d4ee17eeca49c63613a"></h2>


## don't use defer in a loop or you'll get a small memory leak

 - cause defers will grow your stack without the reason

<h2 id="3b9ec32447f983783ee40bcb4e2448fe"></h2>


## don't forget to stop ticker, unless you need a leaked channel

```go
ticker := time.NewTicker(1 * time.Second)
defer ticker.Stop()
```

<h2 id="543e9d26325c59e0d80371ab11f03a3e"></h2>


## `sync.Map` isn't a silver bullet, do not use it without a strong reasons

<h2 id="457a0f3166a881858238dadb30c3b00d"></h2>


## to hide a pointer from escape analysis you might carefully(!!!) use this func:

```go
// noescape hides a pointer from escape analysis.  noescape is
// the identity function but escape analysis doesn't think the
// output depends on the input. noescape is inlined and currently
// compiles down to zero instructions.
func noescape(p unsafe.Pointer) unsafe.Pointer {
x := uintptr(p)
       return unsafe.Pointer(x ^ 0)
}
```

<h2 id="81d856f273cef05d6d36437fb6770bc8"></h2>


## for fastest atomic swap you might use this `m := (*map[int]int)(atomic.LoadPointer(&ptr))`

<h2 id="ad7dad3c5b207cff2caf801d111437d3"></h2>


## use buffered I/O if you do many sequential reads or writes

 - to reduce number of syscalls

<h2 id="869e770545ab96a38832ba21ea6e9199"></h2>


## there are 2 ways to clear a map:

reuse map memory

```go
for k := range m {
    delete(m, k)
}
```

allocate new

```go
m = make(map[int]int)
```


<h2 id="c74c1f42f141c011ca6bd8b1114fc3d0"></h2>


# Build

<h2 id="822c1164685d599334ea5584d4638941"></h2>


## strip your binaries with this command go build -ldflags="-s -w" ...

<h2 id="e34c20517da18245d8e7fe706febc368"></h2>


## tiniest Go docker image

```
CGO_ENABLED=0 go build -ldflags="-s -w" app.go && tar C app | docker import - myimage:latest
```

<h2 id="1695cd016ed1ed01d8ff7cecde62d867"></h2>


## check if there are mistakes in code formatting `diff -u <(echo -n) <(gofmt -d .)`

<h2 id="fbc04a03c1a5ee00e1b416744fb3154b"></h2>


## check interface implementation during compilation

```go
var _ io.Reader = (*MyFastReader)(nil)
```

---

<h2 id="ac5c74b64b4b8352ef2f181affb5ac2a"></h2>


# sql 

<h2 id="cca85d15132b75981103827efd17081b"></h2>


## where in

```go
var openids []interface{}
... // init openids

// expand multiple `?` in `where in ()`
table:= "tbl_user"
query := fmt.Sprintf(" select DISTINCT id from %s where id in (?" , table ) + strings.Repeat(",?", len(openid_list)-1) + ")" 

rows, err := db.Query( query ,   openid_list...  )
if err != nil {
    log.Fatalln( err )    
} 
defer rows.Close() 

for rows.Next() {
    var (
        openid string
    )
    if err := rows.Scan(&openid); err != nil {
        ... 
    }
    // DO something
}
```

<h2 id="b589b58d1c70513bf77a35c489473590"></h2>


## Scan rows to struct 

```
    for rows.Next() {
        var match Match
        // match == Person{0, ""}
        pointers := make([]interface{}, len(columnNames))
        // pointers == `[]interface{}{nil, nil}`
        structVal := reflect.ValueOf(&match).Elem()
        for i, colName := range columnNames {
            fieldVal := structVal.FieldByName(strings.Title(colName))
            // log.Println( i, colName, fieldVal )
            if !fieldVal.IsValid() {
                log.Println("field not valid")
                return nil, errors.New( "field not valid " +  colName )
            }
            pointers[i] = fieldVal.Addr().Interface()
        }
        // pointers == `[]interface{}{&int, &string}`
        err := rows.Scan(pointers...)
        if err != nil {
            // handle err
            log.Println(err)
            return nil , err
        }

        // log.Print( "%+v" , match )
    }

```

<h2 id="f546c79ad1cdb480d0e3df44316a5a29"></h2>


## Parameter Placeholder Syntax

mysql | postgreSQL  | Oracle
--- | --- | ---
WHERE col = ?     |  WHERE col = $1     |   WHERE col = :col
VALUES(?, ?, ?)   |  VALUES($1, $2, $3) |   VALUES(:val1, :val2, :val3)

<h2 id="1475e8cb4633b25db26bd0b484bfc45f"></h2>


## 数据库操作

<h2 id="c8c95af3e4422ec0c4e188c720d67079"></h2>


### 多行查询

 - db.Query , 返回 Rows, error
 - rows.Next() 迭代
 - rows.Scan() 读取行
 - 每次db.Query操作后, 都建议调用rows.Close(). 

```go
	dbw.QueryDataPre()
	rows, err := dbw.Db.Query(`SELECT * From user where age >= 20 AND age < 30`)
	defer rows.Close()
	if err != nil {
		fmt.Printf("insert data error: %v\n", err)
		return
	}
	for rows.Next() {
		rows.Scan(&dbw.UserInfo.Id, &dbw.UserInfo.Name, &dbw.UserInfo.Age)
		if err != nil {
			fmt.Printf(err.Error())
			continue
		}
		if !dbw.UserInfo.Name.Valid {
			dbw.UserInfo.Name.String = ""
		}
		if !dbw.UserInfo.Age.Valid {
			dbw.UserInfo.Age.Int64 = 0
		}
		fmt.Println("get data, id: ", dbw.UserInfo.Id, " name: ", dbw.UserInfo.Name.String, " age: ", int(dbw.UserInfo.Age.Int64))
	}

	err = rows.Err()
	if err != nil {
		fmt.Printf(err.Error())
	}
```

<h2 id="520a0fe1e028d3bfd9e80f3d51311100"></h2>


### 单行查询

 - db.QueryRow , 返回 Row
 - rows.Scan() 读取行
 - err在Scan后才产生

```go
var name string
err = db.QueryRow("select name from user where id = ?", 1).Scan(&name)
```


<h2 id="131d2cc4055f927cc5f593ebb1042224"></h2>


### 插入数据

```go
	ret, err := dbw.Db.Exec(`INSERT INTO user (name, age) VALUES ("xys", 23)`)
	if err != nil {
		fmt.Printf("insert data error: %v\n", err)
		return
	}
	if LastInsertId, err := ret.LastInsertId(); nil == err {
		fmt.Println("LastInsertId:", LastInsertId)
	}
	if RowsAffected, err := ret.RowsAffected(); nil == err {
		fmt.Println("RowsAffected:", RowsAffected)
	}
```

<h2 id="0d98c74797e49d00bcc4c17c9d557a2b"></h2>


### 其他

 - db.Prepare()返回的statement使用完之后需要手动关闭，即defer stmt.Close()

<h2 id="9f82401d0ae9254f9429eaa46e1fe666"></h2>


### 事务

```
CREATE PROCEDURE PRO2()
BEGIN
    DECLARE t_error INTEGER;
    DECLARE    CONTINUE HANDLER FOR SQLEXCEPTION SET t_error = 1;

    START TRANSACTION;
        INSERT INTO test_tab VALUES    (1, '2');
        INSERT INTO test_tab VALUES    (1, '3');

        IF t_error = 1 THEN
            ROLLBACK;
        ELSE
            COMMIT;
        END IF;
END
```


 - Go uses sql.DB for autocommit, and sql.Tx for manual commit. 
 - 事务场景

```go
func clearTransaction(tx *sql.Tx){
    err := tx.Rollback()
    if err != sql.ErrTxDone && err != nil{
        log.Println(err)
    }
}
```

```go
func DoSomething() error {
    tx , err := db.Begin()
    if err != nil {
        log.Println( err )    
        return err
    }
    defer clearTransaction( tx )


    if _, err = tx.Exec(...); err != nil {
        return err
    }
    if _, err = tx.Exec(...); err != nil {
        return err
    }
    // ...

    if err := tx.Commit(); err != nil {
        log.Println( err )    
        return err
    }
    return nil
}
```

 - 事务中，如果有 Query 命令， 执行后续命令之间，必需调用 rows.Close() 关闭连接


<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


# Misc


<h2 id="ae4367a7f966679339c605ac0b009418"></h2>


## regexp , reference captured group 

 - use `$1` instead of `\1` 

<h2 id="12f3c642086ddb0279f69574a34db7ef"></h2>


## CGO_ENALBE=1 情况下, 实现纯静态连接

cmd/link的两种工作模式：internal linking和external linking。

1、internal linking

internal linking的大致意思是若用户代码中仅仅使用了net、os/user等几个标准库中的依赖cgo的包时，cmd/link默认使用internal linking，而无需启动外部external linker(如:gcc、clang等)

因此如果标准库是在CGO_ENABLED=1情况下编译的，那么编译出来的最终二进制文件依旧是动态链接的，即便在go build时传入 -ldflags '-extldflags "-static"'亦无用，因为根本没有使用external linker

2、external linking

而external linking机制则是cmd/link将所有生成的.o都打到一个.o文件中，再将其交给外部的链接器，比如gcc或clang去做最终链接处理。

如果此时，我们在cmd/link的参数中传入 -ldflags '-linkmode "external" -extldflags "-static"'，那么gcc/clang将会去做静态链接，将.o中undefined的符号都替换为真正的代码。

因为 MacOSX 上只有 libc的dylib, 没有 .a , 所以一般会失败。


<h2 id="b052a32a028f65a554fd6d75ca2cb331"></h2>


## BASH: auto add current path to GOPATH when opening a new terminal window 

```
if [ -d "./src" ] && [[ ! $GOPATH =~ $curDir ]]
then
    export GOPATH=$curDir:$GOPATH
fi
```

<h2 id="d631c51d63e223eda44e441f1ce4c0ac"></h2>


## go time format 

[time format example](https://programming.guide/go/format-parse-string-time-date-example.html)


