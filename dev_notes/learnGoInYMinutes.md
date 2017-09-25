
# Learn GO in Y Minutes

# import 

```go
import (
    "io/ioutil" // Implements some I/O utility functions.
    m "math"    // Math library with local alias m.
}
```

# function

```go
// Functions can have parameters and (multiple!) return values.
// Note that `x` and `sum` receive the type `int`.
func learnMultiple(x, y int) (sum, prod int) {
    return x + y, x * y // Return two values.
}

// named return values
func learnNamedReturns(x, y int) (z int) {
    z = x * y
    return // z is implicit here, because we named it earlier.
}
```

## variadic parameters

```go
// Functions can have variadic parameters.
func learnVariadicParams(myStrings ...interface{}) {
    // Iterate each value of the variadic.
    // The underbar here is ignoring the index argument of the array.
    for _, param := range myStrings {
        fmt.Println("param:", param)
    }

    // Pass variadic value as a variadic parameter.
    fmt.Println("params:", fmt.Sprintln(myStrings...))
}
```

# built-in types and literals

```go
    s2 := `A "raw" string literal
can include line breaks.`

    // Non-ASCII literal. Go source is UTF-8.
    g := 'Σ' // rune type, an alias for int32, holds a unicode code point.
    f := 3.14195 // float64, an IEEE-754 64-bit floating point number.
    c := 3 + 4i  // complex128, represented internally with two float64's.    

    // Conversion syntax with a short declaration.
    n := byte('\n') // byte is an alias for uint8.
```

## array and slice 

```go
    // Arrays have size fixed at compile time.
    var a4 [4]int           // An array of 4 ints, initialized to all 0.
    a5 := [...]int{3, 1, 5, 10, 100} // An array initialized with a fixed size 

    // Slices have dynamic size. Arrays and slices each have advantages
    // but use cases for slices are much more common.

    s3 := []int{4, 5, 9}    // Compare to a5. No ellipsis here.
    s4 := make([]int, 4)    // Allocates slice of 4 ints, initialized to all 0.
    var d2 [][]float64      // Declaration only, nothing allocated here.
    bs := []byte("a slice") // Type conversion syntax.

    // Commonly, it is updated in place
    s := []int{1, 2, 3}     // Result is a slice of length 3.
    s = append(s, 4, 5, 6)  // Added 3 elements. Slice now has length of 6.

    // To append another slice
    s = append(s, []int{7, 8, 9}...) // Second argument is a slice literal.
```

## map 

```go
    // Maps are a dynamically growable associative array type, like the
    // hash or dictionary types of some other languages.
    m := map[string]int{"three": 3, "four": 4}
    m["one"] = 1
```

## pointer

```go
// Go is fully garbage collected.
// It has pointers but no pointer arithmetic.
// You can make a mistake with a nil pointer, but not by incrementing a pointer
func learnMemory() (p, q *int) {
    // Named return values p and q have type pointer to int.
    p = new(int) // Built-in function new allocates memory.
    // The allocated int is initialized to 0, p is no longer nil.
    s := make([]int, 20) // Allocate 20 ints as a single block of memory.
    s[3] = 7             // Assign one of them.
    r := -2              // Declare another local variable.
    return &s[3], &r     // & takes the address of an object.
}
p, q := learnMemory() // Declares p, q to be type pointer to int.
fmt.Println(*p, *q)   // * follows a pointer. This prints two ints.
```

# flow control

## if 

```go
    // If statements require brace brackets, and do not require parentheses
    if true {
        fmt.Println("told ya")
    }
    // Formatting is standardized by the command line command "go fmt."
    if false {
        // Pout.
    } else {
        // Gloat.
    }
    // := in an if statement means to declare and assign first , then test
    if y := expensiveComputation(); y > x {
        x = y
    }    
```

## switch

```go
    // Use switch in preference to chained if statements.
    x := 42.0
    switch x {
    case 0:
    case 1:
    case 42:
        // Cases don't "fall through".
        // There is a `fallthrough` keyword however
    case 43:
        // Unreached.
    default:
        // Default case is optional.
    }
```

## for

 - For is the only loop statement in Go

```go
    // Like if, for doesn't use parens either.
    // Variables declared in for and if are local to their scope.
    for x := 0; x < 3; x++ { // ++ is a statement.
        fmt.Println("iteration", x)
    }    
    
    // alternate forms
    for { // Infinite loop.
        break    // Just kidding.
        continue // Unreached.
    }    
    
    // You can use range to iterate over an array, a slice, a string, a map, or a channel.
    // range returns one (channel) or two values (array, slice, string and map).
    for key, value := range map[string]int{"one": 1, "two": 2, "three": 3} {
        // for each pair in the map, print key and value
        fmt.Printf("key=%s, value=%d\n", key, value)
    }    
```

## goto 

```go
    // When you need it, you'll love it.
    goto love
love:
```

# closure

```go
    x := 42.0

    // Function literals are closures.
    xBig := func() bool {
        return x > 10000 // References x declared above switch statement.
    }
    x = 99999
    fmt.Println("xBig:", xBig()) // true    

    // What's more is function literals may be defined and called inline,
    fmt.Println("Add + double two numbers: ",
        func(a, b int) int {
            return (a + b) * 2
        }(10, 2)) // Called with args 10 and 2
    // => Add + double two numbers: 24    
```

 - Decorators are common in other languages
 - Same can be done in Go
    - with function literals that accept arguments

```go
    func sentenceFactory(mystring string) func(before, after string) string {
        return func(before, after string) string {
            return fmt.Sprintf("%s %s %s", before, mystring, after) // new string
        }
    }
    d := sentenceFactory("summer")
    fmt.Println(d("A beautiful", "day!"))
    fmt.Println(d("A lazy", "afternoon!"))    
```

# defer

```go
func learnDefer() (ok bool) {
    // Deferred statements are executed just before the function returns.
    defer fmt.Println("deferred statements execute in reverse (LIFO) order.")
    defer fmt.Println("\nThis line is being printed first because")
    // Defer is commonly used to close a file, so the function closing the
    // file stays close to the function opening the file.
    return true
}
```

# struct / interface 

```go
// Define pair as a struct with two fields, ints named x and y.
type pair struct {
    x, y int
}
```

```go
// Define Stringer as an interface type with one method, String.
type Stringer interface {
    String() string
}
```

```go
    // Define a method on type pair. 
    // Pair now implements Stringer , because
    // Pair has defined all the methods in the interface.
    func (p pair) String() string { // p is called the "receiver"
        // Sprintf is another public function in package fmt.
        // Dot syntax references fields of p.
        return fmt.Sprintf("(%d, %d)", p.x, p.y)
    }

    // Brace syntax is a "struct literal". It evaluates to an initialized struct
    p := pair{3, 4}

    var i Stringer          // Declare i of interface type Stringer.
    i = p                   // Valid because pair implements Stringer
    // Call String method of i
    fmt.Println(i.String())
```

# error handling 

```go
    // ", ok" idiom used to tell if something worked or not.
    m := map[int]string{3: "three", 4: "four"}
    if x, ok := m[1]; !ok { // ok will be false because 1 is not in the map.
        fmt.Println("no one there")
    } else {
        fmt.Print(x) // x would be the value, if it were in the map.
    }
    // An error value communicates not just "ok" but more about the problem.
    if _, err := strconv.Atoi("non-int"); err != nil { // _ discards value
        // prints 'strconv.ParseInt: parsing "non-int": invalid syntax'
        fmt.Println(err)
    }            
```

# Concurrency

## channel 

```go
// c is a channel, 
// a concurrency-safe communication object.
func inc(i int, c chan int) {
    c <- i + 1 // <- is the "send" operator when a channel appears on the left.
}
```

```go
// We'll use inc to increment some numbers concurrently.

// Make allocates and  initializes slices, maps, and channels.
c := make(chan int)
go inc(0, c) // go is a statement that starts a new goroutine.

cs := make(chan string)       // Another channel, this one handles strings.
ccs := make(chan chan string) // A channel of string channels.
go func() { c <- 84 }()       // Start a new goroutine just to send a value.


// Select has syntax like a switch statement but
// each case involves a channel operation
// It selects a case at random out of the cases that are ready to communicate.
select {
    case i := <-c: // The value received can be assigned to a variable,
        fmt.Printf("it's a %T", i)
    case <-cs: // or the value received can be discarded.
        fmt.Println("it's a string")
    case <-ccs: // Empty channel, not ready for communication.
        fmt.Println("didn't happen.")
}
```

# web programming

```go
// A single function from package http starts a web server.
func learnWebProgramming() {

    // First parameter of ListenAndServe is TCP address to listen to.
    // Second parameter is an interface, specifically http.Handler.
    go func() {
        err := http.ListenAndServe(":8080", pair{})
        fmt.Println(err) // don't ignore errors
    }()

    requestServer()
}

// Make pair an http.Handler by implementing its only method, ServeHTTP.
func (p pair) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    // Serve data with a method of http.ResponseWriter.
    w.Write([]byte("You learned Go in Y minutes!"))
}

func requestServer() {
    resp, err := http.Get("http://localhost:8080")
    fmt.Println(err)
    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    fmt.Printf("\nWebserver said: `%s`", string(body))
}
```


