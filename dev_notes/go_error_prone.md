[](...menustart)

- [error-prone place in golang](#13bd409154e8c66bdbe621b5a6e511ca)
    - [1. `range`  will copy the value](#b0bae40f21223254e952e1d16b90806b)
    - [2. `range` will reuse same k,v variable when iterating](#7350871036e378fe4a506a200349ac5f)
    - [3. value method will copy the receiver](#8204b360f64157d1e621a87be4ce0358)
    - [4. if a map's value is array or struct, you can not modify only part of the value](#e57d94614f7c698df1752d2b4f729e35)

[](...menuend)


<h2 id="13bd409154e8c66bdbe621b5a6e511ca"></h2>

# error-prone place in golang


<h2 id="b0bae40f21223254e952e1d16b90806b"></h2>

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

<h2 id="7350871036e378fe4a506a200349ac5f"></h2>

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


<h2 id="8204b360f64157d1e621a87be4ce0358"></h2>

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

<h2 id="e57d94614f7c698df1752d2b4f729e35"></h2>

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





