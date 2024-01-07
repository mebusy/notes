
# error-prone place in golang


## 1. `range`  will copy the value

```golang
type S struct {
	V int
}

func main() {
	var arr [2]S
	for i, v := range &arr {
		// v is a copy of arr[i]
		if i == 0 {
			v.V = 10
		} else if i == 1 {
			arr[i].V = 20
		}
	}
	fmt.Println(arr) // [{0} {20}]
}
```

## 2. `range` will reuse same k,v variable when iterating

```golang
type S struct {
	V int
}

func main() {
	var arr [2]S
	arr[0].V, arr[1].V = 10, 20

    // i, v variable will be reuse in each iteration
    // be careful when using `defer` in range loop
	for i, v := range &arr {
		defer func() {
			fmt.Println(i, v, &i, &v)
		}()
	}
	// 0 {20} 0xc0000120f0 &{20}
	// 1 {20} 0xc0000120f0 &{20}
}
```

if you really want to use `defer`  in range loop, copy the i,v value when calling `defer` function

```golang
type S struct {
	V int
}

func main() {
	var arr [2]S
	arr[0].V, arr[1].V = 10, 20

	for i, v := range &arr {
		defer func(i int, v S) {
			fmt.Println(i, v, &i, &v)
		}(i, v)
	}
	// 1 {20} 0xc000094018 &{20}
	// 0 {10} 0xc000094040 &{10}
}
```


## 3. value method will copy the receiver

```golang
type S struct {
	V int
}

func (s S) ValueSet(v int) {
	// s is a copy of the original s
	// modifying s will not modify the original s
	s.V = v
}

// if you want to modify the original s, use pointer receiver
func (s *S) PointerSet(v int) {
	s.V = v
}

func main() {
	var s S
	s.ValueSet(1)
	fmt.Println(s) // {0}
	s.PointerSet(2)
	fmt.Println(s) // {2}
}
```

## 4. if a map's value is array or struct, you can not modify only part of the value

```golang
func main() {
	var intArrMap = make(map[int][2]int)
	intArrMap[1] = [2]int{1, 2}

	// intArrMap[1][0] = 3 // error, can not assign
	arr := intArrMap[1] // what you can do is to get the copy of the array
	arr[0] = 3
	fmt.Println(intArrMap[1]) // [1 2]

    // can only replace the entire array
	intArrMap[0] = [2]int{3, 4}
	fmt.Println(intArrMap[0]) // [3 4]

}
```





