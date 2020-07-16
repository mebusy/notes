...menustart

 - [ways to sort in go](#13e5e9dd069e344545ecde826aadd758)
     - [1 Sort a slice of ints, float64s or strings](#a7078ee300282b0116b6cca37b638a11)
     - [2 Sort slice with custom comparator](#088ffc615fd30a00b2c5a7fc01a545ff)
     - [3 Implement `sort.Interface` interface for custom data structure](#d2d35ec725f17267135de166e66b8897)

...menuend


<h2 id="13e5e9dd069e344545ecde826aadd758"></h2>


# ways to sort in go

<h2 id="a7078ee300282b0116b6cca37b638a11"></h2>


## 1 Sort a slice of ints, float64s or strings

- Use one of the functions
    - 
    ```go
    sort.Ints
    sort.Float64s
    sort.Strings
    ```
- example

```go
import "fmt"
import "sort"

func main() {
    s := []int{4, 2, 3, 1}
    sort.Ints(s)
    fmt.Println(s) // [1 2 3 4]
}
```

<h2 id="088ffc615fd30a00b2c5a7fc01a545ff"></h2>


## 2 Sort slice with custom comparator

- Use the function `sort.Slice`.
    -  It sorts a slice using a provided function `less(i, j int) bool`
- To sort the slice while keeping the original order of equal elements,use `sort.SliceStable` instead.

- example

```go
    s := []float64{4, 2, 3, 1}
    sort.SliceStable(s, func(i, j int) bool {
        return s[i] > s[j]
    })
    fmt.Println(s) // [4 3 2 1]
```

<h2 id="d2d35ec725f17267135de166e66b8897"></h2>


## 3 Implement `sort.Interface` interface for custom data structure

```go
type Interface interface {
        // Len is the number of elements in the collection.
        Len() int
        // Less reports whether the element with
        // index i should sort before the element with index j.
        Less(i, j int) bool
        // Swap swaps the elements with indexes i and j.
        Swap(i, j int)
}
```


