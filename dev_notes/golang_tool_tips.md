
# Go Tool Chain

## go list

```bash
$ go list -f '{{ .Name }} - {{ .Imports }}'

main - [container/heap fmt math math/bits os sort strconv]
```

```bash
# list imports in fmt module
$ go list -f '{{ join .Imports "\n" }}' fmt

errors
internal/fmtsort
io
math
os
reflect
sort
strconv
sync
unicode/utf8
```


## go tool

### list all GOOS/GOARCH

```bash
$ go tool dist list

aix/ppc64
android/386
android/amd64
android/arm
android/arm64
...
```


## go doc

```bash
$ go doc fmt printf  # case insensitive

package fmt // import "fmt"

func Printf(format string, a ...any) (n int, err error)
    Printf formats according to a format specifier and writes to standard
    output. It returns the number of bytes written and any write error
    encountered.
```

- options
    - `-c`  case sensitive when matching symbols.
    - `-src` show source code
        ```bash
        $ go doc bot Drone_t.Dimensions
        func (p *Drone_t) Dimensions() int
        $ go doc -src bot Drone_t.Dimensions
        func (p *Drone_t) Dimensions() int {
            return 2
        }
        ```

