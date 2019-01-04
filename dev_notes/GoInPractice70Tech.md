...menustart

 - [Go In Practice , 70 Teches](#71c585005b73e8b143984da7dee9b0d3)
 - [2 A solid foundation](#0d64118c7f6ff8aeadfb2c9db268f32b)
     - [2.1 Working wiht CLI applications, the Go way](#f4fc9ba35db46faa075c17a7587260c1)
         - [2.1.1 Command-line flags](#56dfd6c36821c5a64983eff289699453)
     - [2.2 Handling configuration](#3863b9486b6e97a49ff1790df08b38dc)
     - [2.3 Working with real-world web servers](#1e5b504a7ecb0799f2b760c225242b19)
         - [2.3.1 Starting up and shutting down a server](#d1dfba069bae305472df676269e71aa9)
         - [2.3.2 Routing web requests](#daef946a510d0ed9c04cffe18d824726)
 - [3 Concurrency in Go](#16f99609cccf72d44e6fb4b00b7aa9b5)
 - [4 Handling errors and panics](#5c14286df98cd800d088a14ee136b866)
     - [4.1 Error handling](#1a2bb328b5fa8ef5dcc6324dfc56d06d)
     - [4.2 The panic system](#e72b11fe4a7d7755c9bb9da078ed7c7a)
         - [4.2.2 Working with panics](#948d52c1d352272f319d60422e92f251)
         - [4.2.3 Recovering from panics](#58be2510484c3a3b9626aaa5bcbc69c9)
         - [4.2.4 Panics and goroutines](#23ae8dbb31cc7891d0c3de597f0bc523)
 - [5 Debugging and testing](#b8ad4f9f531cf42a4bbe3bc9ecf746ab)
     - [5.2 Logging](#2c0ce02cb81521bcb1e13a7d2537d1dd)
         - [5.2.1 Using Go’s logge](#0a06ab7d7bc94825761e4f71180d1739)
         - [5.2.2 Working with system loggers](#b11462d84b0c705a445bf62b0d7af407)
     - [5.3 Accessing stack traces](#9c010432392bbfc8119a5ee9de0994a3)
     - [5.4 Testing](#8cdb7f7ceb9bff6df74283972fe543d7)
         - [5.4.1 Unit testing](#d6c479cf7ba6e15bc5b1d5044c047f6c)
             - [TECHNIQUE 28: Verifying interfaces with canary tests  TODO , page 132](#628a115ba69d21b430e18b21a0aa97a5)
 - [11 Reflection and code generation](#f226d92098f959d56447d8f0dceb5f79)
     - [11.1 Three features of reflection](#207d97ac8eab80209297f51985f3082d)
         - [TECHNIQUE 66 Switching based on type and kind](#cc58f61e729a92813f5391cab7b2425c)
         - [TECHNIQUE 67: Discovering whether a value implements an interface](#a9ca11ee99ed6c97a08a7c7c459b6507)
         - [TECHNIQUE 68 Accessing fields on a struct](#78a78128f589cf18b987ed6a4b0cf18c)

...menuend


<h2 id="71c585005b73e8b143984da7dee9b0d3"></h2>

# Go In Practice , 70 Teches

<h2 id="0d64118c7f6ff8aeadfb2c9db268f32b"></h2>

# 2 A solid foundation

<h2 id="f4fc9ba35db46faa075c17a7587260c1"></h2>

## 2.1 Working wiht CLI applications, the Go way

<h2 id="56dfd6c36821c5a64983eff289699453"></h2>

### 2.1.1 Command-line flags

 - Go flag system won't let you combine multiple flags ( eg. `ls -la` , instead see `la` as one flag ) 
 - standard `flag` package
 
```go
import "flag"

// 1. Creates a new variable from a flag
// flag.String takes a flag name, default value, and description as arguments
// the value of name is an address , you should access it as a pointer
var name = flag.String( "name", "World", "A name to say hello to." )

// 2. New variable to store flag value
var spanish bool

// iniialize local variable
func init() {
    // 3. Set variable to the flag value
    // step 2 and 3 are another method for handling a flag which
    // let you have a long and short flag
    flag.BoolVar( &spanish,"spanish", false, "Use Spanish language" )
    flag.BoolVar( &spanish,"s", false, "Use Spanish language" )
}

func main() {
    // 4. Parses the flags, placing values in variables
    flag.Parse()
    
    // 5. Accesses name as a pointer
    if spanish == true {
        fmt.Printf( "Hola %s!\n" , *name )
    } else {
        fmt.Printf( "Hello %s!\n" , *name )    
    }
}
```  

```
$ flag_cli –-spanish –name Buttercup
Hola Buttercup!
```

 - The `PrintDefaults` function generates help text for flags. 

<h2 id="3863b9486b6e97a49ff1790df08b38dc"></h2>

## 2.2 Handling configuration

 - json file
    - `json.NewDecoder`
 - YAML
    - "github.com/kylelemons/go-gypsy/yaml"
 - INI
    - "gopkg.in/gcfg.v1"
 - Configuration via environment variables
    - `os.Getenv("PORT")`


<h2 id="1e5b504a7ecb0799f2b760c225242b19"></h2>

## 2.3 Working with real-world web servers

<h2 id="d1dfba069bae305472df676269e71aa9"></h2>

### 2.3.1 Starting up and shutting down a server

**A COMMON ANTIPATTERN: A CALLBACK URL**

A simple pattern (or rather antipattern) for development is to have a URL such as `/kill or /shutdown`, that will shut down the server when called. 

```go
// A special path registered to shut down the server
http.HandleFunc("/shutdown", shutdown)


func shutdown(res http.ResponseWriter, req *http.Request) {
    os.Exit(0)
}
```

 - The URL needs to be blocked in production

**Graceful shutdowns using manners**

 - To avoid data loss and unexpected behavior, a server may need to do some cleanup on shutdown
 - To handle these, you’ll need to implement your own logic or use a package such as
    - `github.com/braintree/manners`
 - Braintree, a division of PayPal, created the manners package that gracefully shuts down , while maintaining the same interface for ListenAndServe that the core http package uses. 
    - Internally, the package uses the core http server while keeping track of connections by using WaitGroup from the sync package. 
    -  WaitGroup is designed to keep track of goroutines. The following listing takes a look at a simple manners-based server.

```go
package main
import (
    "fmt"
    "net/http"
    "os"
    "os/signal"
    "github.com/braintree/manners"
)

func main() {
    // 1. Get instance of a handle
    handler := newHandler()

    // 2. Sets up monitoring of OS singals
    ch := make(chan os.Signal)
    signal.Notify(ch, os.Interrupt, os.Kill)
    go listenForShutdown(ch)

    // Starts the web server
    manners.ListenAndServe(":8080", handler)
} 

func newHandler() *handler {
    return &handler{}
}
type handler struct{}

// Handle responding to web requests
func (h *handler) ServeHTTP(res http.ResponseWriter, req *http.Request) {
    query := req.URL.Query()
    name := query.Get("name")
    if name == "" {
        name = "Inigo Montoya"
    }
    fmt.Fprint(res, "Hello, my name is ", name)
}

// Waits for shutdown signal and reacts
func listenForShutdown(ch <-chan os.Signal) {
    <-ch
    // After a signal comes in, it sends a message to Shutdown on the server. 
    // This tells the server to stop accepting new connections and shut down after all the current requests are completed.
    manners.Close()
}
```

 - The server waits only for request handlers to finish before exiting. 
 - If your code has separate goroutines that need to be waited on, that would need to happen separately, using your own implementation of WaitGroup

This approach has several advantages, including the following:

 - Allows current HTTP requests to complete rather than stopping them midrequest
 - Stops listening on the TCP port while completing the existing requests. 
    - This opens the opportunity for another application to bind to the same port and start serving requests. 
    - If you’re updating versions of an application, one version could shut down while completing its requests, and another version of the application could come online and start serving

A couple of disadvantages also exist under some conditions:

 - The manners package works for HTTP connections rather than all TCP connections.
    - If your application isn’t a web server, the manners package won’t work.
 - In some cases, one version of an application will want to hand off exiting socket connections currently in use to another instance of the same application or another application. For example, if you have long-running socket connections between a server and client applications, the manners package will attempt to wait or interrupt the connections rather than hand them off.  

<h2 id="daef946a510d0ed9c04cffe18d824726"></h2>

### 2.3.2 Routing web requests

 - To correctly route requests, a web server needs to be able to quickly and efficiently parse the path portion of a URL.
 - The `net/url` package, which contains the URL type, has many useful functions for working with URLs.
 - NOTE To differentiate between HTTP methods, check the value of `http.Request.Method`. This contains the method (for example, GET, POST, and so on).

**Handling complex paths with wildcards**

 - Go provides the path package with functionality to work with slash-separated paths
 - This package isn’t directly designed to work with URL paths. 
    - Instead, it’s a generic package intended to work with paths of all sorts.
    - In fact, it works well when coupled with an HTTP handler
 - page : 52


**URL pattern matching**

 - Simple path-based matching isn’t enough for an application that needs to treat a path more like a text string and less like a file path
 - This is particularly important when matching across a path separator (/).
 - The built-in path package enables simple path-matching schemes, but sometimes you may need to match complex paths or have intimate control over the path. 
 - For those cases, you can use regular expressions to match your paths. 
 - `"regexp"`
 - page 55

**Faster routing (without the work)**

Popular solutions include the following:

 - `github.com/julienschmidt/httprouter`
 - `github.com/gorilla/mux`
 - `github.com/bmizerany/pat`


<h2 id="16f99609cccf72d44e6fb4b00b7aa9b5"></h2>

# 3 Concurrency in Go

**Using multiple channels**

 - You want to use channels to send data from one goroutine to another, and
    - be able to interrupt that process to exit.  
 - Use `select` and multiple channels. 
    - It’s a common practice in Go to use channels to signal when something is done or ready to close(eg. a timeout).

**Closing channels**

 - What happens if you have a sender and receiver goroutine, and the sender finishes sending data?
    - Are the receiver and channel automatically cleaned up? 
 - Nope. The memory manager will only clean up values that it can ensure won’t be used again.
    - open channel and a goroutine can’t be safely cleaned
 - The straightforward answer to the question “How do I avoid leaking channels and goroutines?” is “Close your channels and return from your goroutines."
    - Although that answer is correct, it’s also incomplete. 
    - Closing channels the wrong way will cause your program to panic or leak goroutines
 - The predominant method for avoiding unsafe channel closing is to use additional channels to notify goroutines when it’s safe to close a channel.  
 - In Go, the close function should be closed only by a sender, and in general it should be done with some protective guards around it
    - write(send) to a closed channel will cause panic
    - read from a closed channel always return `nil` value ( eg. `false` value on a `bool` channel ).

```go
func main() {
    msg := make(chan string)
    // Adds an additional Boolean channel that 
    // indicates when you’re finished
    done := make(chan bool)
    until := time.After(5 * time.Second)

    // passes 2 channels into send
    go send(msg, done)
    for {
        select {
        case m := <-msg:
            fmt.Println(m)
        case <- until :
            // When you time-out, 
            // lets send know the process is done
            dont <- true
            time.Sleep( 500* time.Millisecond )  
            return  
        }    
    }
}

func send(ch chan<- string, done <-chan bool) {
    for {
        select {
        case <- done:    
            println("done")
            close(ch)
            return
        default:
            ch <- "hello"
            time.Sleep( 500* time.Millisecond )
        }    
    }   
}
```

**Locking with buffered channels**

 - Use a channel with a buffer size of 1, and share the channel among the goroutines you want to synchronize.
 - 替代 lock

```go
func main() {
    // create a buffered channel with one space
    lock := make(chan bool, 1)
    for i := 1; i < 7; i++ {
        go worker(i, lock)
    }
    time.Sleep(10 * time.Second)
}

func worker(id int, lock chan bool) {
    fmt.Printf("%d wants the lock\n", id)
    lock <- true
    fmt.Printf("%d has the lock\n", id)
    time.Sleep(500 * time.Millisecond)
    fmt.Printf("%d is releasing the lock\n", id)
    <-lock
}
```

<h2 id="5c14286df98cd800d088a14ee136b866"></h2>

# 4 Handling errors and panics

<h2 id="1a2bb328b5fa8ef5dcc6324dfc56d06d"></h2>

## 4.1 Error handling

 - `errors.New`  function from the errors package is great for creating simple new errors. 
 - `fmt.Errorf` function in the fmt package gives you the option of using a formatting string on the error message. 

**Custom error types**

 - Go’s error type is an interface that looks like the following listing.

```go
type error interface {
    Error() string
}
```

 - Anything that has an Error function returning a string satisfies this interface’s contract.
 - In some cases, you may want your errors to contain more information than a simple string. In such cases, you may choose to create a custom error type.
    - **Create a type that implements the error interface but provides additional functionality**

Imagine you’re writing a file parser. When the parser encounters a syntax error, it generates an error. Along with having an error message, it’s generally useful to have information about where in the file the error occurred. You could build such an error as shown in the following listing.

```go
type ParseError struct {
    Message string // error msg without location info
    Line, Char int  // the location info
}

// Implements the Error interface
func (p *ParseError) Error() string {
    format := "%s o1n Line %d, Char %d"
    return fmt.Sprintf(format, p.Message, p.Line, p.Char)
}
```

 - This technique is great when you need to return additional information
 - But what if you need one function to return different kinds of errors?

**Error variables**

 - One complex function may encounter more than one kind of error. 
 - One convention that’s considered good practice in Go (although not in certain other languages) is to create package-scoped error variables that can be returned whenever a certain error occurs. 
 - The best example of this in the Go standard library comes in the io package, which contains errors such as io.EOF and io.ErrNoProgress.
    - **create errors as package-scoped variables and reference those variables**

```go
// error instance
var ErrTimeout = errors.New("The request timed out")
var ErrRejected = errors.New("The request was rejected")

var random = rand.New(rand.NewSource(35))

func SendRequest(req string) (string, error) {
    // randomly generates behavior
    switch random.Int() % 3 {
    case 0:
        return "Success", nil
    case 1:
        return "", ErrRejected
    default:
        return "", ErrTimeout
    }
}

func main() {
    response, err := SendRequest("Hello")
    for err == ErrTimeout {
        fmt.Println("Timeout. Retrying.")
        response, err = SendRequest("Hello")
    }
    if err != nil {
        fmt.Println(err)
    } else {
        fmt.Println(response)
    }
}
```

<h2 id="e72b11fe4a7d7755c9bb9da078ed7c7a"></h2>

## 4.2 The panic system

<h2 id="948d52c1d352272f319d60422e92f251"></h2>

### 4.2.2 Working with panics

 - `panic(interface{})`
    - `panic(nil)`
    - `panic("Oops, I did it again.")`
 - The best thing to pass to a panic is an error. 
    - Use the error type to make it easy for the recovery function (if there is one).
    - `panic(errors.New("Something bad happened."))`
        - With this method, it’s still easy to print the panic message with print formatters:
        - `fmt.Printf("Error: %s", thePanic)`
        - And it’s just as easy to send the panic back through the error system. 
        - That’s why it’s idiomatic to pass an error to a panic

<h2 id="58be2510484c3a3b9626aaa5bcbc69c9"></h2>

### 4.2.3 Recovering from panics

**Recovering from panics**

```go
func main() {
    // Provides a deferred closure to handle panic recovery
    defer func() {
        if err := recover(); err != nil {
            fmt.Printf("Trapped panic: %s (%T)\n", err, err)
        }
    }()
    yikes() // Calls a function that panics
}
func yikes() {
    // Emits a panic with an error for a body
    panic(errors.New("Something bad happened."))
}
```

 - The recover function in Go returns a value (interface{}) if a panic has been raised, but in all other cases it returns nil. 

<h2 id="23ae8dbb31cc7891d0c3de597f0bc523"></h2>

### 4.2.4 Panics and goroutines

 - If a panic on a goroutine goes unhandled on that goroutine’s call stack, it crashes the entire program

a trivial little library (now part of github.com/Masterminds/cookoo) to protect us from accidentally unhandled panics on goroutines.

```go
// GoDoer is a simple parameterless function.
type GoDoer func()

// safely.Go runs a function as a goroutine 
// and handles any panics.
func Go(todo GoDoer) {
    go func() {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("Panic in safely.Go: %s", err)
            }
        }()
        todo()
    }()
}
```

 - to use 
    - `"github.com/Masterminds/cookoo/safely"`
    - `safely.Go( xxxx )`

<h2 id="b8ad4f9f531cf42a4bbe3bc9ecf746ab"></h2>

# 5 Debugging and testing

<h2 id="2c0ce02cb81521bcb1e13a7d2537d1dd"></h2>

## 5.2 Logging

<h2 id="0a06ab7d7bc94825761e4f71180d1739"></h2>

### 5.2.1 Using Go’s logge

 - two built-in packages for logging
    - log
        - provides basic support (mainly in the form of formatting) for writing log messages
    - log/syslog

**log**

 - the error messages are all sent to Standard Error
    - regardless of whether the message is an actual error or an informational message. 
 - When you call log.Fatalln or any of the other “fatal” calls, the library prints the error message and then calls os.Exit(1)
 - Additionally, log.Panic calls log an error message and then issue a panic

**Logging to an arbitrary writer**

 - You want to send logging messages to a file or to a network service without having to write your own logging system
 - Initialize a new log.Logger and send log messages to that.
 - log.Logger provides features for sending log data to any io.Writer, which includes things like file handles and network connections (net.Conn).

```go
//  Logging to a file

func main() {
    // Creates a log file
    logfile, _ := os.Create("./log.txt")
    // Makes sure it gets closed
    defer logfile.Close()

    // Creates a logger
    logger := log.New(logfile, "example ", log.LstdFlags|log.Lshortfile)
    // Sends it some messages
    logger.Println("This is a regular message.")
    logger.Fatalln("This is a fatal error.")
    // As before, this will never get called.
    logger.Println("This is the end of the function.")
}
```

```
$ cat log.txt
example 2015/05/12 08:42:51 outfile.go:16: This is a regular message.
example 2015/05/12 08:42:51 outfile.go:17: This is a fatal error.
```

> Components of a log file

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/GoInPracticeLogComponent.png)

 - You can control the prefix field with the second argument to log.New. 

**Logging to a network resource**
 
 - Streaming logs to a network service is error-prone, but you don’t want to lose log messages if you can avoid it.
 - By using Go’s channels and some buffering, you can vastly improve reliability

Before you can get going on the code, you need something that can simulate a log server. Netcat (nc) is such a simple tool.

 - to start a simple TCP server that accepts simple text messages and writes them to the console
    - `nc -lk 1902`
    - Now you have a listener (-l) listening continuously (-k) on port 1902.
        -  (Some versions of Netcat may also need the –p flag.) 

```go
// Network log client
func main() {
    // Connects to the log server
    conn, err := net.Dial("tcp", "localhost:1902")
    if err != nil {
        panic("Failed to connect to localhost:1902")
    }
    defer conn.Close()

    // Sends log messages to the network connection
    f := log.Ldate | log.Lshortfile
    logger := log.New(conn, "example ", f)
    logger.Println("This is a regular message.")
    logger.Panicln("This is a panic.")
}
```

 - It’s always recommended to close a network connection in a defer block.
 - If nothing else, when a panic occurs (as it will in this demo code), the network buffer will be flushed on close, and you’re less likely to lose critical log messages telling you why the code panicked.
 - Did you notice that we also changed log.Fatalln to a log.Panicln in this example?
    - the log.Fatal\* functions have an unfortunate side effect: the deferred function isn’t called. 
    - Because log.Fatal\* calls os.Exit, which immediately terminates the program without unwinding the function stack.

**Handling back pressure in network logging**

 - Network log services are prone to connection failures and back pressure. This leads to lost log messages and sometimes even service failures.
 - Build a more resilient logger that buffers data.
 - You’re likely to run into two major networking issues:
    - The logger’s network connection drops (either because the network is down or because the remote logger is down).
    - The connection over which the logs are sent slows down
 - One solution to the back-pressure problem is to switch from TCP to UDP

```go
    // Adds an explicit timeout
    timeout := 30 * time.Second
    // Dials a UDP connection instead of a TCP one
    conn, err := net.DialTimeout("udp", "localhost:1902", timeout)
```

 - to run the UDP logger , you also need to restart your nc server as a UDP server:
    - `nc -luk 1902`

 - advantages:
    - The app is resistant to back pressure and log server outages. 
        - If the log server hiccups, it may lose some UDP packets, but the client won’t be impacted.
    - Sending logs is faster even without back pressure.
    - The code is simple.
 - disadvantages.
    - Log messages can get lost easily
        - UDP doesn’t equip you to know whether a message was received correctly
    - Log messages can be received out of order. 
        - Large log messages may be packetized and then get jumbled in transition.
        - Adding a timestamp to the message (as you’ve done) can help with this, but not totally resolve it.
    - Sending the remote server lots of UDP messages may turn out to be more likely to overwhelm the remote server,because it can’t manage its connections and slow down the data intake. 
        - Although your app may be immune to back pressure, your log server may be worse off.

TCP logging is prone to back pressure, but UDP logging won’t guarantee data accuracy.


<h2 id="b11462d84b0c705a445bf62b0d7af407"></h2>

### 5.2.2 Working with system loggers

Syslogs provide some major advantages to creating your own. First, they’re mature and stable products that are optimized for dealing with latency, redundant messages, and archiving.

Most contemporary system loggers handle periodic log rotation,compression, and deduplication. These things make your life easier.

Additionally, system administrators are adept at using these log files for analysis, and many tools and utilities are available for working with the log files. These are compelling reasons to log to the standard facility rather than creating your own.


**Logging to the syslog**

 - You want to send application log messages into the system logger.
 - Configure Go’s syslog package and use it
    - a dedicated package is available for this: log/syslog

```go
// A logger directed to syslog
func main() {
    // Tells the logger how to appear to syslog
    priority := syslog.LOG_LOCAL3 | syslog.LOG_NOTICE
    // Sets the flags, as you’ve done before
    flags := log.Ldate | log.Lshortfile
    // Creates a new syslog logger
    logger, err := syslog.NewLogger(priority, flags)
    if err != nil {
        fmt.Printf("Can't attach to syslog: %s", err)
        return
    }
    // Sends a simple message
    logger.Println("This is a test log message.")
}
```

```
Jun 30 08:34:03 technosophos syslog_logger[76564]: 2015/06/30 syslog_logger.go:18: This is a test log message.
```

Using Go’s logger is convenient, but setting the severity correctly and using more of syslog’s capabilities would be more useful. You can do that by using the log/syslog logging functions directly.

```go
func main() {
    // Creates a new syslog client
    // prefix you want every message to begin with (narwhal)
    logger, err := syslog.New(syslog.LOG_LOCAL3, "narwhal")
    if err != nil {
        panic("Cannot attach to syslog")
    }
    defer logger.Close()

    // Sends the logger a variety of messages
    logger.Debug("Debug message.")
    logger.Notice("Notice message.")
    logger.Warning("Warning message.")
    logger.Alert("Alert message.")
}
```

```
Jun 30 08:52:06 technosophos narwhal[76635]: Notice message.
Jun 30 08:52:06 technosophos narwhal[76635]: Warning message.
Jun 30 08:52:06 technosophos narwhal[76635]: Alert message.
```

 - You logged four messages, but only three are displayed.  The call to syslog.Debug isn’t present. 
 - The reason is that the system log used to run the example is configured to not send debug messages to the log file. 
 - If you wanted to see debug messages, you’d need to alter the configuration of your system’s syslog facility. 

---

<h2 id="9c010432392bbfc8119a5ee9de0994a3"></h2>

## 5.3 Accessing stack traces

**Capturing stack traces**

 - You want to fetch a stack trace at a critical point in the application.
 - Use the runtime package, which has several tools.

If all you need is a trace for debugging, you can easily send one to Standard Output by using the runtime/debug function PrintStack.

```go
import (
    "runtime/debug"
)

func bar() {
    debug.PrintStack()
}
```

But if you want to capture the trace to send it somewhere else, you need to do something slightly more sophisticated. 

You can use the runtime package’s Stack function.


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

 - runtime.Stack 
    - 2nd argument ,  Setting it to true will cause Stack to also print out stacks for all running goroutines. 
    - This can be tremendously useful when debugging concurrency problems, but it substantially increases the amount of output. 

If all of this isn’t sufficient, you can use the runtime package’s Caller and Callers functions to get programmatic access to the details of the call stack. 

Both the `runtime` and the `runtime/debug` packages contain numerous other functions for analyzing memory usage, goroutines, threading, and other aspects of your program’s resource usage.  

---

<h2 id="8cdb7f7ceb9bff6df74283972fe543d7"></h2>

## 5.4 Testing

<h2 id="d6c479cf7ba6e15bc5b1d5044c047f6c"></h2>

### 5.4.1 Unit testing

```go
// A Simple Hello
package hello
func Hello() string {
    return "hello"
}
```

```go
// A hello test
// same package as the code it’s testing
package hello
// this package contains built-in testing tools
import "testing"
func TestHello(t *testing.T) {
    if v := Hello(); v != "hello" {
        t.Errorf("Expected 'hello', but got '%s'", v)
    }
}
```

 - The most frequently used functions on `testing.T` are as follows:
    - `T.Error(args …interface{}) or T.Errorf(msg string, args interface{})`
        - These log a message and then mark the test as failed.
        - The second version allows formatting strings
    - `T.Fatal(args …interface{}) or T.Fatalf(msg string, args interface{})`
        - These log a message, mark the test as failed, and then stop the testing. 
        - You should do this whenever one failed test indicates that no others will pass

**Using interfaces for mocking or stubbing**

 - You’re writing code that depends on types defined in external libraries, and you want to write test code that can verify that those libraries are correctly used
 - Create interfaces to describe the types you need to test. Use those interfaces in your code, and then write stub or mock implementations for your tests.
 - Say you’re writing software that uses a third-party library that looks like the following listing.

```go
// Listing 5.12 The message struct
type Message struct {
    // ...
}
func (m *Message) Send(email, subject string, body []byte) error {
    // ...
    return nil
}
```

 - This describes some kind of message-sending system. In your code, you use that library to send a message from your application. 
    - In the course of writing your tests, you want to ensure that the code that sends the message is being called, but you don’t want to send the message.
    - One way to gracefully deal with this is to write your own interface that describes the methods shown in listing 5.12, and have your code use that interface in its declarations instead of directly using the Message type, as the following listing shows.

```go
// Listing 5.13 Use an interface

// Defines an interface that describes the methods you use on Message
type Messager interface {
    Send(email, subject string, body []byte) error
}
// Passes that interface instead of the lib Message type
func Alert(m Messager, problem []byte) error {
    return m.Send("noc@example.com", "Critical Error", problem)
}
```


<h2 id="628a115ba69d21b430e18b21a0aa97a5"></h2>

#### TECHNIQUE 28: Verifying interfaces with canary tests  TODO , page 132

---



<h2 id="f226d92098f959d56447d8f0dceb5f79"></h2>

# 11 Reflection and code generation

 - *Reflection* ,  in software development, refers to a program’s ability to examine its own structure. 
 - As useful as Go’s reflection system is, though, sometimes it’s cleaner to avoid complex and expensive runtime reflection, and instead write code that writes code. 
    -  Code generation can accomplish some of the things that are typically done in other languages with generics. 

<h2 id="207d97ac8eab80209297f51985f3082d"></h2>

## 11.1 Three features of reflection

 - Software developers use reflection to examine objects during runtime. 
 - In a strongly typed language like Go, you may want to find out whether a particular object satisfies an interface. 
    - Or discover what its underlying kind is. 
    - Or walk over its fields and modify the data.
 - Go’s reflection tools are located inside the `reflect` package. 
 - You need to understand three critical features when working with Go’s reflection mechanism: values, types, and kinds.
    - value
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Go70_refect_value.png)
    - type
        - Each value in Go has a particular type associated with it. 
        - For example, with var b bytes.Buffer, the type is bytes.Buffer. 
        - For any reflect.Value in Go, you can discover its type. Type information is accessible through the reflect .Type interface
    - kinds
        - Go defines numerous primitive kinds, such as struct, ptr (pointer), int, float64, string, slice, func (function), and so on. 
        - The reflect package enumerates all of the possible kinds with the type reflect.Kind.
            - Note that in preceding picture, the value of type string also has the kind string.)

<h2 id="cc58f61e729a92813f5391cab7b2425c"></h2>

#### TECHNIQUE 66 Switching based on type and kind

One of the most frequent uses of Go’s reflection system is identifying either the type or kind of a value. 

 - You want to write a function that takes generic values (interface{}s), and then does something useful with them based on underlying types. 
 - Go provides various methods for learning this information, ranging from the type switch to the reflect.Type and reflect.Kind types. 

---

 - Say you want to write a function with the signature `sum(…interface{}) float64`. 
    - You want  to take any number of arguments of various types. And you want it to convert the values to float64 and then sum them.  
 - The most convenient tool that Go provides for doing this is the type switch. 
    - With this special case of the switch control structure, you can perform operations based on the type of a value, instead of the data contained in a value. 


```go
func sum(v ...interface{}) float64 {
    var res float64 = 0
    for _, val := range v {
        switch val.(type) {
        case int:
            res += float64(val.(int))
        case int64:
            res += float64(val.(int64))
        case uint8:
            res += float64(val.(uint8))
        case string:
            a, err := strconv.ParseFloat(val.(string), 64)
            if err != nil {
                panic(err)
            } 
            res += a
        default:
            fmt.Printf("Unsupported type %T. Ignoring.\n", val)
        }
    }
    return res
}
```

 - **it’s important to remember that type switches operate on types (not kinds).**
    - that is , if you defined a type `type MyInt int64` , and pass a `MyInt` to sum function, `case int64` will **NOT** match for a MyInt.
    - The solution to this problem is to use the reflect package, and work based on kind instead of type.

```go
func sum(v ...interface{}) float64 {
    var res float64 = 0
    for _, val := range v {
        // Gets the reflect.Value of the item
        ref := reflect.ValueOf(val)
        // From the value, you can switch on the Kind().
        switch ref.Kind() {
        case reflect.Int, reflect.Int64:
            // The reflect.Value type provides convenience functions 
            // for converting related subkinds to their biggest version
            // (e.g., int, int8, int16…to int64).
            res += float64(ref.Int())
        case reflect.Uint8:
            res += float64(ref.Uint())
        case reflect.String:
            a, err := strconv.ParseFloat(ref.String(), 64)
            if err != nil {
            panic(err)
            }
            res += a
        default:
            fmt.Printf("Unsupported type %T. Ignoring.\n", val)
        }
    }
    return res
}
```

 - One of the pieces of information you can learn from a reflect.Value is its underlying kind.
 - Another thing that the reflect.Value type gives you is a group of functions capable of converting related types to their largest representation. 
    -  A reflect.Value with a uint8 or uint16 can be easily converted to the biggest unsigned integer type by using the reflect.Value’s Uint() method.

<h2 id="a9ca11ee99ed6c97a08a7c7c459b6507"></h2>

#### TECHNIQUE 67: Discovering whether a value implements an interface

 - Given a particular type, you want to find out whether that type implements a defined interface
 - There are two ways to accomplish this.  Use the one that best meets your needs.
    - One is with a type assertion, 
    - and the other uses the reflect package. 

---

```go
// Listing 11.4 Checking and converting a type
func isStringer(v interface{}) bool {
    // Takes an interface{} value and 
    // runs a type assertion to the desired interface
    _, ok := v.(fmt.Stringer)
    return ok
}
```

 - Type assertions are one way of testing whether a given **value** implements an interface.
 - But what if you want to test whether a type implements an interface, but determine which interface at runtime? 
    - Go’s reflection package has no reflect.Interface type. 
    - Instead, reflect.Type (which is itself an interface) provides tools for querying whether a given type implements a given interface type.  

```go
// Listing 11.5 Determine whether a type implements an interface
func implements(concrete interface{}, target interface{}) bool {
    // Gets a reflect.Type that describes
    // the target of the pointer
    iface := reflect.TypeOf(target).Elem()
    
    // Gets the reflect.Type of the concrete type passed in
    v := reflect.ValueOf(concrete)
    t := v.Type()
    
    if t.Implements(iface) {
        fmt.Printf("%T is a %s\n", concrete, iface.Name())
        return true
    }
    fmt.Printf("%T is not a %s\n", concrete, iface.Name())
    return false
}

func main() {
    n := &Name{First: "Inigo", Last: "Montoya"}
    stringer := (*fmt.Stringer)(nil)
    implements(n, stringer)

    writer := (*io.Writer)(nil)
    implements(n, writer)
}
```

 - The implements() function takes two values. 
    - It tests whether the first value (concrete) implements the interface of the second (target). 
    - The implements() function does assume that the target is a pointer to a value whose dynamic type is an interface. 
 - To test whether concrete implements the target interface, you need to get the reflect.Type of both the concrete and the target. 
 - There are two ways of doing this.    
    - The first uses reflect.TypeOf() to get a reflect.Type, and a call to Type.Elem() to get the type that the target pointer points to:
        - `iface := reflect.TypeOf(target).Elem()`
    - The second gets the value of concrete, and then gets the reflect.Type of that value.
        - `v := reflect.ValueOf(concrete) ;  t := v.Type() `
 - The trickier part of this test, though, is getting a reference to an interface. 
    - There’s no way to directly reflect on an interface type.  Interfaces don’t work that way; you can’t just instantiate one or reference it directly
    - Instead, you need to find a way to create a placeholder that implements an interface.
        - The simplest way is to do something we usually recommend studiously avoiding: intentionally create a nil pointer. 
        - You need the Elem() call in order to get the type of the nil.

<h2 id="78a78128f589cf18b987ed6a4b0cf18c"></h2>

#### TECHNIQUE 68 Accessing fields on a struct

 - You want to learn about a struct at runtime, discovering its fields.
 - Reflect the struct and use a combination of reflect.Value and reflect.Type to find out information about the struct.
 - TODO



## 11.2 Structs, tags, and annotations

 - Go has no macros, and unlike languages such as Java and Python, Go has only Spartan support for annotations. 
 - But one thing you can easily annotate in Go is properties on a struct. 

### 11.2.1 Annotating structs

 - An example of using struct annotations with things like the JSON encoder. 


```
// Listing 11.8 Simple JSON struct
package main
import (
     "encoding/json"
     "fmt" 
)
type Name struct {
     First string `json:"firstName"`
     Last  string `json:"lastName "`
}
func main() {
     n := &Name{"Inigo", "Montoya"}
     data, _ := json.Marshal(n)
     fmt.Printf("%s\n", data)B
}

// result:  
//   {"firstName":"Inigo","lastName ":"Montoya"}
// without the annotation, it will output :  
//   {"First":"Inigo","Last":"Montoya"}
```

 - This code declares a single struct, `Name`, that’s annotated for JSON encoding. 
    - it maps the struct member `First` to the JSON field `firstName`, and the struct field `Last` to `lastName`. 
    - The struct annotations make it possible to control how your JSON looks.
 - Annotations are a free-form string enclosed in back quotes that follows the type declaration of a struct field.
 - Annotations play no direct functional role during compilation, but annotations can be accessed at runtime by using reflection. 
    - It’s up to the annotation parsers to fig- ure out whether any given annotation has information that the parser can use. 
    - For example, you could modify the preceding code to include different annotations, as shown in the next listing.

```
// Listing 11.9 A variety of annotations
type Name struct {
             First string `json:"firstName" xml:"FirstName"`
             Last  string `json:"lastName,omitempty"`
             Other string `not,even.a=tag`
}
```
 - These annotations are all legal, in the sense that the Go parser will correctly handle them. 
    - And the JSON encoder will be able to pick out which of those applies to it.
        - It will ignore the xml tag as well as the oddly formatted annotation on the `Other` field.
 - As you can see from the tags in listing 11.9, an annotation has no fixed format. Just about any string can be used.
    - But a certain annotation format has emerged in the Go community and is now a de facto standard. Go developers call these annotations tags.


### 11.2.2 Using tag annotations

 - The sample JSON struct you looked at earlier contained annotations of the form : `json: "NAME,DATA"`
    - where `NAME` is the name of the field (in JSON documents),
    - and `DATA` is a list of optional information about the field (omitempty or kind data)
 - Likewise, if you look at the encoding/xml package,  you’d see a pattern similar to annotations for converting structs to and from XML.
    - Tags for XML look like this:`xml:"body"` and `xml:"href,attr"`
    - where NAME is the field name, and DATA contains a list of information about the field. 




