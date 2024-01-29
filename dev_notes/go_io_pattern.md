[](...menustart)

- [common I/O Patterns in Go](#1243f95d027b78a40f2a84b343b99a18)
- [IO Writer](#f7d8c7b4ef78dfd99158d1fc46392814)
    - [1 Write to standard output](#7ad297773c89571539683cfdd3ca784c)
    - [2 Write to a custom writer](#e518da047a9ca1b74571638b632ae15c)
    - [3 Write to multiple writers at once](#d667c14387f816da16b1e99b0d3e27e3)
- [IO Reader](#35de8666d58ac7a1e04e8965d6ccae1c)
    - [4 Create a simple reader](#048e711e31509d6bdcb8daf388c5a788)
    - [5 Read from multiple readers at once](#faa264f0fdc0d713dc86534a2875e34f)
- [Copying data from a reader to writer](#77bf87e07b7b5e1d6a844e22f8a18140)
    - [6 Reader pushes data to a writer (copy variant 1)](#615aabf915bb4a63c9fbd3bea2bb2cad)
    - [7 Writer pulls data from a reader (copy variant 2)](#9846e78200a51ab40be52f5e8e966fc2)
    - [8 Copy data from a reader to writer (copy variant 3, io.Copy)](#6d8dfd4cc9b22a35898ead2e72bcc97d)
    - [9 Create a data tunnel with io.Pipe](#b16e1bc359354693366f96ebe5caac5f)
    - [10 Capture stdout of a function into a variable with io.Pipe, io.Copy and io.MultiWriter](#68e70fd348079380e56cd0fa2b7cea1b)

[](...menuend)


<h2 id="1243f95d027b78a40f2a84b343b99a18"></h2>

# common I/O Patterns in Go

<h2 id="f7d8c7b4ef78dfd99158d1fc46392814"></h2>

# IO Writer

<h2 id="7ad297773c89571539683cfdd3ca784c"></h2>

## 1 Write to standard output

The most common example every Go programming tutorial teaches you:

```go
import "fmt"

func main() {
	fmt.Println("Hello Medium")
}
```

But, no one tells you the above program is a simplified version of this one:

```go
import (
	"fmt"
	"os"
)

func main() {
	fmt.Fprintln(os.Stdout, "Hello Medium")
}
```

The `Fprintln` method takes an `io.Writer` type and a string to write into a writer.  The `os.Stdout` satisfies `io.Writer` interface.


<h2 id="e518da047a9ca1b74571638b632ae15c"></h2>

## 2 Write to a custom writer

```go
import (
	"bytes"
	"fmt"
)

func main() {
	// Empty buffer (implements io.Writer)
	var b bytes.Buffer
	fmt.Fprintln(&b, "Hello Medium") // Don't forget &

	// Optional: Check the contents stored
	fmt.Println(b.String()) // Prints `Hello Medium`
}
```

<h2 id="d667c14387f816da16b1e99b0d3e27e3"></h2>

## 3 Write to multiple writers at once

```go
import (
	"bytes"
	"fmt"
	"io"
)

func main() {
	// Two empty buffers
	var foo, bar bytes.Buffer

	// Create a multi writer
	mw := io.MultiWriter(&foo, &bar)

	// Write message into multi writer
	fmt.Fprintln(mw, "Hello Medium")

	// Optional: verfiy data stored in buffers
	fmt.Println(foo.String())
	fmt.Println(bar.String())
}
```

The message "Hello Medium" will be written into both foo and bar at the same time internally.

<h2 id="35de8666d58ac7a1e04e8965d6ccae1c"></h2>

# IO Reader

<h2 id="048e711e31509d6bdcb8daf388c5a788"></h2>

## 4 Create a simple reader

```go
import (
	"fmt"
	"io"
	"strings"
)

func main() {
	// Create a new reader (Readonly)
	r := strings.NewReader("Hello Medium")

	// Read all content from reader
	b, err := io.ReadAll(r)
	if err != nil {
		panic(err)
	}

	// Optional: verify data
	fmt.Println(string(b))
}
```

Note: `os.Stdin` is a commonly used reader for collecting standard input.


<h2 id="faa264f0fdc0d713dc86534a2875e34f"></h2>

## 5 Read from multiple readers at once

```go
import (
	"fmt"
	"io"
	"strings"
)

func main() {
	// Create two readers
	foo := strings.NewReader("Hello Foo\n")
	bar := strings.NewReader("Hello Bar")

	// Create a multi reader
	mr := io.MultiReader(foo, bar)

	// Read data from multi reader
	b, err := io.ReadAll(mr)

	if err != nil {
		panic(err)
	}

	// Optional: Verify data
	fmt.Println(string(b))
}
```

The data is collected **sequentially in the order of readers** passed to `io.MultiReader`. It is like gathering information from various data stores at once but in the given order.

Note: Don’t use `io.ReadAll` for big buffers, as they can choke memory.


<h2 id="77bf87e07b7b5e1d6a844e22f8a18140"></h2>

# Copying data from a reader to writer

<h2 id="615aabf915bb4a63c9fbd3bea2bb2cad"></h2>

## 6 Reader pushes data to a writer (copy variant 1)

```go
import (
	"bytes"
	"fmt"
	"strings"
)

func main() {
	// Create a reader
	r := strings.NewReader("Hello Medium")

	// Create a writer
	var b bytes.Buffer

	// Push data
	r.WriteTo(&b) // Don't forget &

	// Optional: verify data
	fmt.Println(b.String())
}
```

<h2 id="9846e78200a51ab40be52f5e8e966fc2"></h2>

## 7 Writer pulls data from a reader (copy variant 2)

```go
import (
	"bytes"
	"fmt"
	"strings"
)

func main() {
	// Create a reader
	r := strings.NewReader("Hello Medium")

	// Create a writer
	var b bytes.Buffer

	// Pull data
	b.ReadFrom(r)

	// Optional: verify data
	fmt.Println(b.String())
}
```

<h2 id="6d8dfd4cc9b22a35898ead2e72bcc97d"></h2>

## 8 Copy data from a reader to writer (copy variant 3, io.Copy)

```go
import (
	"bytes"
	"fmt"
	"io"
	"strings"
)

func main() {
	// Create a reader
	r := strings.NewReader("Hello Medium")

	// Create a writer
	var b bytes.Buffer

	// Copy data
	_, err := io.Copy(&b, r) // Don't forget &

	if err != nil {
		panic(err)
	}
	// Optional: verify data
	fmt.Println(b.String())
}
```

<h2 id="b16e1bc359354693366f96ebe5caac5f"></h2>

## 9 Create a data tunnel with io.Pipe

The `io.Pipe` returns a reader and a writer pair, where writing data into a writer automatically allows programs to consume data from the Reader. It is like a Unix pipe.

Pipe creates a synchronous in-memory pipe. It can be used to connect code expecting an io.Reader with code expecting an io.Writer.

You must put writing logic into a separate go-routine.

```go
import (
	"fmt"
	"io"
)

func main() {
	pr, pw := io.Pipe()

	// Writing data to writer should be in a go-routine
	// because pipe is synchronous.
	go func() {
		defer pw.Close() // Important! To notify writing is done
		fmt.Fprintln(pw, "Hello Medium")
	}()

	// Code is blocked until someone writes to writer and closes it
	b, err := io.ReadAll(pr)

	if err != nil {
		panic(err)
	}
	// Optional: verify data
	fmt.Println(string(b))
}
```

<h2 id="68e70fd348079380e56cd0fa2b7cea1b"></h2>

## 10 Capture stdout of a function into a variable with io.Pipe, io.Copy and io.MultiWriter

Let’s say we are building a CLI application.

As part of that process, we should tap into the **standard output** generated by a function(to console) and capture the same information into a **variable**.

```go
import (
	"bytes"
	"fmt"
	"io"
	"os"
)
// Your function
func foo(w *io.PipeWriter) {
	defer w.Close()
	// Write a message to pipe writer
	fmt.Fprintln(w, "Hello Medium")
}

func main() {
	// Create a pipe
	pr, pw := io.Pipe()

	// Pass writer to function
	go foo(pw)

	// Variable to get standard output of function
	var b bytes.Buffer

	// Create a multi writer that is a combination of
	// os.Stdout and our variable byte buffer
	mw := io.MultiWriter(os.Stdout, &b)
	// Copies reader content to standard output
	_, err := io.Copy(mw, pr)

	if err != nil {
		panic(err)
	}

	// Optional: verify data
	fmt.Println(b.String())
}
```




