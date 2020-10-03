...menustart

- [cgo](#63e64fb7f6bfcedd6708e1b75126a6fb)
- [Cgo - Go under the hood](#6f4f121d679c89cf32d0ea88934c99db)
    - [go build](#cec36a9a2bd92e12e683c99d23b3a0fc)
    - [for callback](#83fec9a1c38557a5a493e84ac0a99521)
    - [Crossing the Chasem](#97f750032375877e095f758fc45a1867)
    - [Concurrency considerations](#eabd481c8a039ec36866de41247519f8)
    - [copy between C and Go](#5025b13f57d84277bcce817a407505ee)
    - [Call Go from Interpreter language](#16ad6798ad517309b1d4959fd9f2bfa2)
    - [指针 - unsafe 包的灵魂](#ed562296a9c5bcbe2d40b6a97f745940)
- [Examples](#ff7c0fcd6a31e735a61c001f75426961)
    - [macOS/iOS: Writing to NSLog using Golang (using Cgo)](#6895f5e89997716a5baf9162b803b053)

...menuend


<h2 id="63e64fb7f6bfcedd6708e1b75126a6fb"></h2>


# cgo

- build with shared library

```go
# cgo LDFLAGS: -laddlib
import "C"
```

- pkg-config

```go
// #cgo pkg-config: sqlite3
```


- The cgo rules:
    - you may pass a Go pointer ... if it doesn't point to other pointers ... and C can't keep a reference to it.
    - the "Go pointer" means the pointers to go memory

- Use C Memory

```go
    /*
    typedef struct {
        int a,b,c;
    } someStruct;
    */
    someCMemory := C.calloc(1, C.sizeof_someStruct)
    defer C.free( someCMemory )
    s := (*C.somestruct)(someCMemory)
    ...
```

```go
// typedef struct { uint8_t *data; size_t data_len; } someStruct ;

    s := (*C.somestruct)( C.calloc(1, C.sizeof_someStruct))
    defer C.free( unsafe.Pointer(s) )

    cMem := C.calloc( 1, C.size_t( len(data) ) )
    defer C.free( cMem )

    // copy object
    s.data = (*C.unit8_t)( C.memmove( 
        cMem, unsafe.Pointer( &data[0]) , C.size_t( len(data) ) )
    )
    s.data_len = C.size_t(len(data))

```

<h2 id="6f4f121d679c89cf32d0ea88934c99db"></h2>


# Cgo - Go under the hood

<h2 id="cec36a9a2bd92e12e683c99d23b3a0fc"></h2>


## go build

- `import "C"` triggers Cgo
- any non-Go files in the directory are compiled
    - if you use `//export` directive, your *exported* go file shouldn't include any definitions. Definitions should put in another either go file withou `//export` or *c* source file.

> Using //export in a file places a restriction on the preamble: since it is copied into two different C output files, it must not contain any definitions, only declarations. If a file contains both definitions and declarations, then the two output files will produce duplicate symbols and the linker will fail. To avoid this, definitions must be placed in preambles in other files, or in C source files.

- `#cgo` pseodu directives and environment variables to flag compiler and linker

<h2 id="83fec9a1c38557a5a493e84ac0a99521"></h2>


## for callback

- Go can keep the c function pointer, but can not directly call it.
    - go need to call a c wrapper function which actually take the function pointer and call it.


<h2 id="97f750032375877e095f758fc45a1867"></h2>


## Crossing the Chasem

- Go to C with runtime.cgocall
    - will not block other goroutines and GC
    - Runs on OS allocated stack
        - goroutine stack does not work for gcc compiler code
    - Outside of $GOMAXPROCS accouting
- C go GO with runtime.cgocallback
    - Runs on original goroutine's stack
    - $GOMAXPROCS accounting enforced
- Recursion allowd across the chasm
- Implemented in GO, C and Assembly

<h2 id="eabd481c8a039ec36866de41247519f8"></h2>


## Concurrency considerations

- Go multiplexes goroutines to GOMAXPROCS threads
- "Once a goroutine enters cgo , it's considered blocking, so not counted in $GOMAXPROCS limit and ... scheduler might need to **create new OS thread** to host other ready goroutines"
- 8 goroutines * GOMAXPROCS=1 , Go to C used all 
- 800k goroutines of GO to C got "pthread_create failed" (pure Go no problem)

<h2 id="5025b13f57d84277bcce817a407505ee"></h2>


## copy between C and Go

- C.CString uses C heap, you must free it

```go
package print

// #include <stdio.h>
// #include <stdlib.h>
import "C"
import "unsafe"

func Print(s string) {
    cs := C.CString(s)
    defer C.free(unsafe.Pointer(cs))
    C.fputs(cs, (*C.FILE)(C.stdout))
}
```

- A few special functions convert between Go and C types by making copies of the data. In pseudo-Go definitions:

```go
// Go string to C string
// The C string is allocated in the C heap using malloc.
// It is the caller's responsibility to arrange for it to be freed, 
// such as by calling C.free (be sure to include stdlib.h
// if C.free is needed).
func C.CString(string) *C.char

// Go []byte slice to C array
// The C array is allocated in the C heap using malloc.
// It is the caller's responsibility to arrange for it to be
// freed, such as by calling C.free (be sure to include stdlib.h
// if C.free is needed).
func C.CBytes([]byte) unsafe.Pointer

// C string to Go string
func C.GoString(*C.char) string

// C data with explicit length to Go string
func C.GoStringN(*C.char, C.int) string

// C data with explicit length to Go []byte
func C.GoBytes(unsafe.Pointer, C.int) []byte
```

<h2 id="16ad6798ad517309b1d4959fd9f2bfa2"></h2>


## Call Go from Interpreter language

Darwin -> .dylib

windows .dll ?

others: .so

c-shared


<h2 id="ed562296a9c5bcbe2d40b6a97f745940"></h2>


## 指针 - unsafe 包的灵魂

语言环境 | 无类型指针 | 数值化指针
--- | --- | --- 
Go | `var p unsafe.Pointer = nil` | `var q uintptr = uintptr(p)`
C  | `void *p = NULL;`  | `uintptr_t q = (unitptr_t)(p);` (c99)

- unsafe.Pointer 是Go指针和C指针 转化的媒介
- uintptr 是 Go  转化数值和指针的 中介


<h2 id="ff7c0fcd6a31e735a61c001f75426961"></h2>


# Examples

<h2 id="6895f5e89997716a5baf9162b803b053"></h2>


## macOS/iOS: Writing to NSLog using Golang (using Cgo)

```go
// example.go
package myapp

import "log"

  ...

mobilelog := MobileLogger{}
logger := log.New(mobilelog, "", 0)
```

```go
// mobilelogger.go
package myapp

/*
#cgo CFLAGS: -x objective-c
#cgo LDFLAGS: -framework Foundation
#import <Foundation/Foundation.h>
void Log(const char *text) {
  NSString *nss = [NSString stringWithUTF8String:text];
  NSLog(@"%@", nss);
}
*/
import "C"
import "unsafe"

type MobileLogger struct {
}

func (nsl MobileLogger) Write(p []byte) (n int, err error) {
	p = append(p, 0)
	cstr := (*C.char)(unsafe.Pointer(&p[0]))
	C.Log(cstr)
	return len(p), nil
}
```











