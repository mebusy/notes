
# Go Tips

# Common

## multiple characters replacement

```go
r := strings.NewReplacer("(", "", ")", "")
fmt.Println( r.Replace( "a(b)c)d" )  )
```

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

## How to find out which types implement ByteReader interface in golang pkg ?

```
https://golang.org/search?q=ReadByte
```


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

## the short form for slice initialization is `a := []T{}`

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


## use `%+v` to print data with sufficient details


## using range loop to iterate over array or slice 

```go
for _, c := range a[3:7] {...}
```

## comparing timestamps by using `time.Before` or `time.After`.

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

## be careful with range in Go

 - `for i := range a` and `for i, v := range &a` doesn't make a copy of a
 - but `for i, v := range` a does

## reading nonexistent key from map will not panic 

 - `value := map["no_key"]` will be zero value
 - `value, ok := map["no_key"]` is much better

## simple random element from a slice

```go
[]string{"one", "two", "three"}[rand.Intn(3)]
```




# Concurrency

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

## T14 Closing channels

 - write(send) to a closed channel will cause **panic**
    - the close function should be **called only by a sender**
 - when receiver has done, it should notify the sender that sender can safely close the channel now
 - implementation:
    - sender should take 2 channel, for example:
        - `msg` channel: for messages
        - `done` channel: the other is for notification 
    - when receiver is done, nofity the sender,  and now sender can close the channle safely

### use chan struct{} to pass signal, chan bool makes it less clear



## T15 Locking with buffered channels (size of 1, to replace Lock)


## best candidate to make something once in a thread-safe way is sync.Once

 - don't use flags, mutexes, channels or atomics

## concurrency-safe

 - In general the rule is this: 
    - top-level functions like strings.Split or fmt.Printf or rand.Int63 may be called from any goroutine at any time
        - (otherwise programming with them would be too restrictive)
    - but objects you create (like a new bytes.Buffer or rand.Rand) must only be used by one goroutine at a time unless otherwise noted 
        - (like net.Conn's documentation does).


# Error

## T17 Use custom error types to return additional information

### Or use to wrap an error 

```
$ go get github.com/pkg/errors
```

```go
errors.Wrap(err, "additional message to a given error")
```

## T18 Error variables , create errors as package-scoped variables and reference those variables

```go
var ErrTimeout = errors.New("The request timed out") 

return "", ErrTimeout
```

## Panics and goroutines

 - If a panic on a goroutine goes unhandled on that goroutine’s call stack, it crashes the entire program
 - `github.com/Masterminds/cookoo/safely`
    - `safely.Go( xxxx )`

## use panic only in very specific situations, you have to handle error



# Debug & Test 

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


## to get call stack we've runtime.Caller


 - https://golang.org/pkg/runtime/#Caller

```go
func Caller(skip int) (pc uintptr, file string, line int, ok bool)
```
        
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


## 30 Parallel benchmarks  and race detection

```
$ go test -bench . -cpu=1,2,4
```

```
$ go test -bench . -race -cpu=1,2,4
```


## easy way to split test into different builds 

 - use `// +build integration` and run them with `go test -v --tags integration` .


# Web Cloud and Micro Service

## T9 URL Faster routing

```
github.com/gorilla/mux
```

## T49 Detecting timeouts

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_8.md#ed8f378a99622e6fa9e881ad40b1ee0a

## T50 resuming download with HTTP

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_8.md#9828258f9f00dd06f2a1b4105c62f4d6


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

## T60 Batch Cross-compiling

```
$ go get -u github.com/mitchellh/gox
$ gox \
  -os="linux darwin windows " \
  -arch="amd64 386" \
  -output="dist/{{.OS}}-{{.Arch}}/{{.Dir}}" .
```

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

## T63 Faster JSON marshal and unmarshal

```
$ go get -u github.com/ugorji/go/codec/codecgen
```

## httputil.DumpRequest is very useful thing, don't create your own

 - https://godoc.org/net/http/httputil#DumpRequest

```go
func DumpRequest(req *http.Request, body bool) ([]byte, error)
```


# Reflection

## T70 Generating code with go generate

 - https://github.com/mebusy/notes/blob/master/dev_notes/GoIn70_11.md#eb80f5b52be56947902eca88e1c67eb4


# Performance

## Do NOT overuse fmt.Sprintf in your hot path. 
 - It is costly due to maintaining the buffer pool and dynamic dispatches for interfaces.
 - if you are doing fmt.Sprintf("%s%s", var1, var2), consider simple string concatenation.
 - if you are doing fmt.Sprintf("%x", var), consider using hex.EncodeToString or strconv.FormatInt(var, 16)


## always discard body e.g. `io.Copy(ioutil.Discard, resp.Body)`  if you don't use it

 - HTTP client's Transport will not reuse connections unless the body is read to completion and closed

## don't use defer in a loop or you'll get a small memory leak

 - cause defers will grow your stack without the reason

## don't forget to stop ticker, unless you need a leaked channel

```go
ticker := time.NewTicker(1 * time.Second)
defer ticker.Stop()
```

## `sync.Map` isn't a silver bullet, do not use it without a strong reasons

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

## for fastest atomic swap you might use this `m := (*map[int]int)(atomic.LoadPointer(&ptr))`

## use buffered I/O if you do many sequential reads or writes

 - to reduce number of syscalls

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


# Build

## strip your binaries with this command go build -ldflags="-s -w" ...

## tiniest Go docker image

```
CGO_ENABLED=0 go build -ldflags="-s -w" app.go && tar C app | docker import - myimage:latest
```

## check if there are mistakes in code formatting `diff -u <(echo -n) <(gofmt -d .)`

## check interface implementation during compilation

```go
var _ io.Reader = (*MyFastReader)(nil)
```


