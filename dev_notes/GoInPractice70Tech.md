
# Go In Practice , 70 Teches

# 2 A solid foundation

## 2.1 Working wiht CLI applications, the Go way

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

## 2.2 Handling configuration

 - json file
    - `json.NewDecoder`
 - YAML
    - "github.com/kylelemons/go-gypsy/yaml"
 - INI
    - "gopkg.in/gcfg.v1"
 - Configuration via environment variables
    - `os.Getenv("PORT")`


## 2.3 Working with real-world web servers

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

# 4 Handling errors and panics




