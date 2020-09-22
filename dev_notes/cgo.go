
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

