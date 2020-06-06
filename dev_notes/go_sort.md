
# ways to sort in go

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


