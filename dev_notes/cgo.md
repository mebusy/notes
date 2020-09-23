
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

# Cgo - Go under the hood

## go build

- `import "C"` triggers Cgo
- any non-Go files in the directory are compiled
    - if you use `//export` directive, your *exported* go file shouldn't include any definitions. Definitions should put in another either go file withou `//export` or *c* source file.

> Using //export in a file places a restriction on the preamble: since it is copied into two different C output files, it must not contain any definitions, only declarations. If a file contains both definitions and declarations, then the two output files will produce duplicate symbols and the linker will fail. To avoid this, definitions must be placed in preambles in other files, or in C source files.

- `#cgo` pseodu directives and environment variables to flag compiler and linker

## for callback

- Go can keep the c function pointer, but can not directly call it.
    - go need to call a c wrapper function which actually take the function pointer and call it.


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



