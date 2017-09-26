
# A Tour of Go

# Interface

## Printing Weekdays

```go
    day := time.Now().Weekday()
    fmt.Printf( "Hello, %s (%d)\n", day ,day )
    // Hello, Saturday (6)
    // time.Weekday is an int type , and it implements Stringer.
```

## Printing Durations

```go
    start := time.Now()
    fetch("https://www.google.com/")
    fmt.Println( time.Since(start) ) 
    // 190.090717ms
    fmt.Println( "%d\n", time.Hour +  time.Since(start) ) 
    // 3600190898331
``` 

## Write to a file 

```go
    fmt.Fprintf( os.Stdout , "hello\n" ) 
```

## Write to a hash

 - the nice thing about the writer interface of course is that you can substitute implementations besides OS files. 
 - for example hash functions in go are conventionally presented as writers 

```go
    h := crc32.NewIEEE()  // it is itself a writer
    fmt.Fprintf ( h, "hello, 世界\n" )
    fmt.Printf( "hash=%#X\n" , h.Sum32 ) // hash=0xe2ed6c48
```

## Print and hash , use MultiWriter

```go
    h := crc32.newIEEE()
    w := io.MultiWriter( h, os.Stdout ) 
    fmt.Fprintf ( w, "hello, 世界\n" )  // hello, 世界
    fmt.Printf( "hash=%#X\n" , h.Sum32 ) // hash=0xe2ed6c48
```

## Hex dump 

```go
    h := hex.Dumper( os.Stdout )
    defer h.Close()
    fmt.Fprintf( h, "Hello, 世界\n" )
```

---

 - fmt.Printf sport `%v` , which v means value 
 - how that works ?
 - This takes us to our 2nd topic -- **reflection**

# Reflection

 - In GO, reflection means that the implementation makes 
    - type information , basic operations available at run-time 
 - So if you have an unknown value, you can find out its type , the definition of that type, and perform the type's basic operations on that value.

## Printing basic types

```go
func main() {
    myPrint( "Hello", 42, "\n" )   
}

func myPrint( args ...interfaceP{} ) {
    for _, arg := range args {
        switch v := reflect.ValueOf(arg); v.Kind() {
        case reflect.String:
            os.Stdout.WriteString(v.String())
        case reflect.Int:
            os.Stdout.WriteString( strconv.FormatInt(v.Int(), 10) )   
        }
    }    
}
```

## Printing Structs

```go
type Lang struct {
    Name string
    Year int
    URL string     
}

func main() {
    lang := Lang{ "Go", 2009 , "https://golang.org/" }
    fmt.Printf( "%v\n" , lang )   // {Go 2009 https://golang.org/}
    fmt.Printf( "%+v\n" , lang )  // {Name:Go Year:2009 URL:https://golang.org/}  
    fmt.Printf( "%#v\n" , lang )  // main.Lang{Name:"Go" Year:"2009" URL:"https://golang.org/"}  
}
```

## Struct to JSON

```go
func main() {
    lang := Lang{ "Go", 2009 , "https://golang.org/" }
    data , err := json.Marshal(lang)
    if err != nil {
        log.Fatal(err)    
    }
    fmt.Printf( "%s\n" , data  )  // {"Name":"Go" "Year":"2009" "URL":"https://golang.org/"} 
}
```

## Struct to XML 


```go
func main() {
    lang := Lang{ "Go", 2009 , "https://golang.org/" }
    data , err := xml.Marshal(lang)
    if err != nil {
        log.Fatal(err)    
    }
    fmt.Printf( "%s\n" , data  ) 
}

<Lang>
    <Name>Go</Name>
    <Year>2009</Year>
    <URL>https://golang.org</URL>
</Lang>
```

## JSON to Struct 

```go
// this func basically implement `cat` tool
func main() {
    input, err := os.Open("lang.json")    
    if err != nil {
        log.Fatal(err)
    }
    io.Copy(os.Stdout, input)  // like mem cpy , but for I/O
}
```

```go
// decode json
func main() {
    input, err := os.Open("lang.json")    
    if err != nil {
        log.Fatal(err)
    }
    
    dec := json.NewDecoder(input)
    for {
        var Lang lang 
        err := dec.Decoder( &lang ) 
        if err != nil {
            if err == io.EOF {
                break 
            }    
            log.Fatal(err)
        }    
        fmt.Printf( "%v\n" , lang  )
    }    
}

{Python 1991 http://python.org/}
{Ruby 1995 http://www.ruby-lang.org/en/}
```

 - Abstracted version 

```go
func do( f func(Lang) ) {
    input, err := os.Open("lang.json")    
    if err != nil {
        log.Fatal(err)
    }
    
    dec := json.NewDecoder(input)
    for {
        var Lang lang 
        err := dec.Decoder( &lang ) 
        if err != nil {
            if err == io.EOF {
                break 
            }    
            log.Fatal(err)
        }    
        f(lang)
    }    
}

func main() {
    do( func( lang Lang )  {
        fmt.Printf( "%v\n" , lang )     
    }  )
}
```

## JSON to Struct to XML

```go
funct main() {
    do ( func(lang Lang) )  {
        data , err := xml.MarshIndent( lang, "", "  " ) 
        if err != nil {
            log.Fatal(err)
        }      
        fmt.Printf( "%s", data  )
    })
}
```

---

# Concurrency 

 - Goroutines let you run multiple computations simultaneously 
 - Channels let you coordinate the computations , by explicit communication
    - chanels communicate and synchronize a single operation.
    - but `Buffering` removes synchronization

## Generator: functions that returns a channel 

## Restoring sequencing 

(之前的例子，执行顺序乱了)

 - Send a channel on a channel , making goroutine wait its turn
 - Receive all messages, then enable them again by sending on a private channel 
 - First we define a mesage type that contains a channel for the reply

```go
type Message struct {
    str string
    wait chan bool     
}
```

 - str is the message that we want to print 
 - wait channel is like a singaler , the guy will block on the wait channel until person says, ok, I want you to go ahead

```go
waitForIt := make(chan bool)  // shared between all messages 

c <- Message{ "AAA" , waitForIt }
time.Sleep(  xxxxx  ) 
<- waitForIt 
```
 
## Select

 - all channels are evaluated 
 - selection blocks until one communication can proceed , which then dose 
     - select available 1 randomly
 - A default clause , if present, executes immediately if no channel is ready 

## Timeout using select 

 - this will timeout for every conversation

```go
for {
    select {
    case s := <-c :
        fmt.Println(s)    
    case <- time.After( 1* time.Second ) :
        fmt.Println( "you're too slow." )
        return 
    }   
}
```

## Timeout for whole conversation using select 


```go
timeout := time.After(5*time.Second)
for {
    select {
    case s := <-c :
        fmt.Println(s)    
    case <- timeout:
        fmt.Println( "you're too slow." )
        return 
    }   
}
```

## Quit channel 

 - instead of using a timeout , we can deterministically to stop it

```go
select {
    case c <- "AAA" :
        // do nothing
    case <- quit:
        cleanup()
        // more sophisticated 
        quit <- "See you!"
        return 
}

// in main func
quit <- "Bye"
<- quit
```

## Daisy-Chain

```go
func f(left, right chan int) {
    left <- 1 + <- right     
}
```

---

# Shape your data flow

 - Channels are streams of data 
 - Dealing with multiple streams is the true power of select 

```
Fan-out
   /
-> ->
   \
```

```
Funnel
 \
-> ->
 /
```

```Turnout
 \ /
-> ->
 / \
```

## Fan-out

 - you can use range , if you do , you will receive data all the time until the channel closed , and if it closed then the loop will discontinue and you won't process this last mesage 

```go
func Fanout( int <- chan int , OutA, OutB chan int ) {
    for data := range In { // Receive until closed
        select {  // Send to first non-blocking channel 
        case OutA <- data : 
        case OutB <- data : 
        }
    }    
}
```

## Turnout

```go
func Turnout ( InA, InB <-chan int, OutA, OutB chan int  ) {
    for {
        select {   // receive from first non-blocking
            case data , more = <- InA : 
            case data , more = <- InB :    
        }    
        if !more {
            return 
        }
        select {   // send to first non-blocking 
            case OutA <- data :
            case OutB <- data :   
        }
    }   
}
```

 - if you have a closed channel in there , it tends to be chosen all the time 
 - so if you close one channel , you will always get to that case and you'll never get to the other channel which might still have data 
 - so you can use a quit channel

###  Quit Channel 

```go
func Turnout( Quit <- chan int, InA, InB, OutA, OutB chan int   ) {
    for {
        select { 
            case data = <- InA : 
            case data = <- InB :    

            case <- Quit:   // remember : close generates a mesage 
                close(InA)  // Actually this is an anit-pattern  
                close(InB)  //    But you can argue that quit acts as a delegate
                
                Fanout( InA, OutA , OutB )  // Flush the remaining data 
                Fanout( InB, OutA,  OutB )
        }
    }
}
```

## Where channels fail 

 - You can create deadlocks with channels
 - Channels pass around copies, which can impact performace
 - Passing pointers to channel can create race conditions
 - What about "naturally shared" structures lick caches or registries ? Ugly

### Mutexes are not an optimal solution

 - Mutexes are like toilets
    - The longer you occupy them, the longer the queue gets
 - Read/Write mutexes can only *reduce* the problem
 - using multiple mutexes *will* cause deadlocks sooner or later
 - All-in-all not the solution we're looking for 

### Atomic operations

 - sync.atomic package
 - Store, Load, Add, Swap and CompareAndSwap 
 - Mapped to thread-safe CPU instructions
 - These instructions only work on integer types
 - Only about 10-69x slower than their non-atomic counterparts

### Spinning CAS 

 - You need a **state** variable and a **free** constant 
 - Use CAS(CompareAndSwap) in a loop:
    - if state is **not free**,  try again until it is 
    - if state is **free** , set it to something else 
 - if you managed to change the state , you *own* it.
 - sync.mutex use this pattern 

```go
type Spinlock struct {
    state *int32    
}

const free = int32(0)

func( l *Spinlock ) Lock() {
    for !atomic.CompareAndSwapInt32( l.state , free, 42 )  // 42 or any other value but 0
        runtime.Gosched()                   // Poke the scheduler
    }   
}

func( l *Spinlock ) Unlock() {
    atomic.StoreInt32( l.state , free )   // Once atomic , always atomic !    
}
```

### Ticket storage 

 - We need an **indexed data structure** (like a slice), a **ticket** and a **done** variable 
 - A function draws a new ticket by adding 1 to the ticket
 - Every ticket number is unique as we nerver decrement
 - Treat the **ticket as an index** to store your data
 - Increase done to extend the *ready to read* range 

```go
type TicketStore struct {
    ticket *uint64 
    done *unit64
    slots []string // for simpicity, imagine this to be infinite    
}

func (ts *TicketStore) Put(s string) {
    t := atomic.AddUint64(ts.ticket, 1) -1 // draw a ticket 
    slots[s]  = s   // store your data 
    for !atomic.CompareAndSwapUint64( ts.done, t , t+1 ) {  // increase done
        runtime.Gosched()          
    }   
}

func (ts *TicketStore) GetDone() []string {  // wait free, return immediately
    return ts.slots[ :atomic.LoadUnit64( ts.done )+1 ]   // read up to done    
}
```

### Guidelines for non-blocking code

 - Don't switch between atomic and non-atomic functions
    - just always use atomic functions 
 - Target and exploit situations which enforce uniqueness 
 - Avoid changing 2 things at a time 
    - sometimes you can exploit bit operations
    - sometimes intelligent ordering can do the trick 
    - sometimes it's just not possible at all 

## Concurrency in practice 

 - Avoid blocking, avoid race conditions 
    - the easiest way to do that is by using CSP 
 - Use channels to avoid shared state
    - Use select to manage channels 
 - Where channels don't work:
    - Try to use tools from the sync package first 
    - In simple case or when *really* needed: try lockless code 

---

# 7 common mistakes 

## 1. Not Accepting Interface 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_10.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_11.png)

## 2. Not using io.Reader & io.Writer 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_20.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_21.png)


## 3. Requiring Broad Interfaces 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_30.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_31.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_32.png)


## 4. Methods Vs Functions 

 - Methods, by definition, are **bound** to a specific **type**
 - Functions can **accept interfaces** as input 


**Functions Can Be Used With Interface**

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_40.png)

## 5. Pointer vs Values 

 - It's **not** a question of **performance** (generally) , but on of **shared access**
 - If you want to **share** the value with a function or method, then **use a pointer**
 - if you **don't want** to **share** it, then use **a value** (copy)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_50.png)

### Pointer Receivers 

 - If you want to share a value with it's method, use  a **pointer receiver**
 - Since methods commonly manage state , this is the **common usage**
 - **Not safe** for concurrent access 



### Value Receivers

 - If you want to share the **value copied** (not shared), use values 
 - If the type is an empty struct ( stateless, just behavior ) ... then just use value 
 - **safe**  for concurrent aceess 
 - eg. `func(t Time)`


## 6. Thinking of Errors As Strings 

### Error is An Interface 

```go
type error interface {
   Error() string   
}
```

### Standard Errors 

 - `errors.New( "error here" )` is usually sufficient
 - Exported Error Variables can be **easily checked**

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_60.png)

 - this is fine it works, but how do you compare that ?  usually people use string comparison and that's generally not the best way to do things 
 - so better is to export it with the variable and now we can check values 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_61.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_62.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_63.png)

### Custom Errors

 - Can **provide context** to guarantee consistent feedback
 - Provide a type which can be **different from the error value**
 - Can provide **dynamic values** (based on internal error state)


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_64.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_65.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_mistake_66.png)

## 7. To Be Safe Or Not To Be 

### Consider Concurrency

 - If you provide a library someone will use it **concurrently**
 - Data structures are **not safe** for concurrent access
 - Values aren't safe , you need to **create safe behavior** around them 

### making it safe 

 - **sync package** provides behavior to make a value safe (Atomic/Mutex) 
 - **Channels** coordinate values across goroutines by permitting one go routinue to acces at a time

### Keeping It Unsafe

 - **Safety comes at a cost**
 - Imposes behaviors on consumer 
 - **Proper API** allows consumers to **add safety as needed**
 - Consumers can use channels or mutexes


