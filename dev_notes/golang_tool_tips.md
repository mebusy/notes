[](...menustart)

- [Go Tool Chain](#125e912e5b4d16be23474018aa68afef)
    - [go list](#a7e1d632b7f0f204484907aaedbcdba6)
    - [go tool](#1c2eb2d3edc197362fa18a3512057756)
        - [list all GOOS/GOARCH](#e761880bea8f1f8b4c77ba1e0662b258)
    - [go doc](#97dafa559620d720a718b8756436b45d)
    - [trace](#04a75036e9d520bb983c5ed03b8d0182)

[](...menuend)


<h2 id="125e912e5b4d16be23474018aa68afef"></h2>

# Go Tool Chain

<h2 id="a7e1d632b7f0f204484907aaedbcdba6"></h2>

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

list all modules 

```bash
$ go list -m all
bot
github.com/davecgh/go-spew v1.1.0
github.com/jupp0r/go-priority-queue v0.0.0-20160601094913-ab1073853bde
github.com/kyroy/kdtree v0.0.0-20200419114247-70830f883f1d
github.com/kyroy/priority-queue v0.0.0-20180327160706-6e21825e7e0c
github.com/pmezard/go-difflib v1.0.0
```

<h2 id="1c2eb2d3edc197362fa18a3512057756"></h2>

## go tool

<h2 id="e761880bea8f1f8b4c77ba1e0662b258"></h2>

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


<h2 id="97dafa559620d720a718b8756436b45d"></h2>

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

<h2 id="04a75036e9d520bb983c5ed03b8d0182"></h2>

## trace

```bash
go test -trace=trace.out
go tool trace trace.out
```


