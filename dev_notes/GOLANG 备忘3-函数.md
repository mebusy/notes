
    3.1 函数定义
        支持不定长变参
        支持多返回值
        支持返回参数命名
        支持匿名函数和闭包
        不支持嵌套 nested
        不支持重载 overload
        不支持默认参数 default parameter)
    3.2 变参
        变参本质上是 slice, 只能有一个,且必须最后一个
        使用 slice 做变参调用时，必须展开
    3.3 返回值
        多返回值可以直接作为其他函数调用实参
        命名返回参数可看作与形参类似的局部变量，最后由return隐式返回
        命名返回参数可被同名局部变量遮蔽，此时需要显式返回
        命名返回参数允许defer延迟调用通过闭包读取和修改
    3.4 匿名函数
        可以赋值给变量,作为结构字段,在channel里传送
        闭包复制的是原对象指针,这样就能解释延迟引用现象
    3.5 延迟调用
        defer语句负责在其所在的函数`返回`时执行一个`函数(或方法)`。通常 于释放资源或错误处理
        其参数在到达defer语句那个时刻被求值或复制, 可用指针或闭包 "延迟" 读取。
        其函数在返回时才被执行
        多个 defer 注册,按 FILO 次序执, 某个延迟调用出错，不会影响其他defer执行
        滥用 defer 可能会导致性能问题
    3.6 错误处理
        没有结构化异常, panic 抛出错误,recover 捕获错误
        panic、recover 参数类型为 interface{}, 因此可抛出任何类型对象
        延迟调用中引发的错误,可被后续延迟调用捕获,但仅最后1个错误可被捕获。
        recover 只有defer 语句中直接调用才会中止错误, 其他调用方式总是返回 nil
        使用前面的 延迟匿名函数 或 下面的调用, 都是有效的
        如果需要保护代码片段，可将代码块重构成匿名函数,确保后续代码被执行。
        除 panic 引发中断性错误外, 还可返回 error类型错误对象 来表示函数调用状态。
        导致关键流程出现不可修复性错误的 使 panic,其他使 error


# 函数

## 3.1 函数定义

```go
func test(x, y int, s string) (int, string) {
    //类型相同的相邻参数可合并
    n := x + y      // 多返回值必须使用括号
    return n, fmt.Sprintf(s, n)
}
```

##### 支持不定长变参
##### 支持多返回值
##### 支持返回参数命名
##### 支持匿名函数和闭包

##### 不支持嵌套 nested
##### 不支持重载 overload
##### 不支持默认参数 default parameter)

## 3.2 变参

##### 变参本质上是 slice, 只能有一个,且必须最后一个

```go
func test(s string, params ...int) string {
    var x int
    for _, i := range n {
        x += i
    }
    return fmt.Sprintf(s, x)
}
func main() {
    println(test("sum: %d", 1, 2, 3))
}
```

##### 使用 slice 做变参调用时，必须展开

```go
func main() {
    s := []int{1, 2, 3}
    println(test("sum: %d", s...))
}
```

## 3.3 返回值

##### 多返回值可以直接作为其他函数调用实参

##### 命名返回参数可看作与形参类似的局部变量，最后由return隐式返回

```go
func add(x, y int) (z int) { 
    z=x+y
    return 
}
func main() {
    println(add(1, 2))
}
```

##### 命名返回参数可被同名局部变量遮蔽，此时需要显式返回

```go
func add(x, y int) (z int) {
    {
        var z = x + y
        // return   // error
        return z    
    } 
}
```

##### 命名返回参数允许defer延迟调用通过闭包读取和修改

```go
func add(x, y int) (z int) {
    defer func() {
        z += 100 
    }()
    z=x+y
    return 
}
func main() {
    println(add(1, 2))  // 输出: 103
}
```


## 3.4 匿名函数

##### 可以赋值给变量,作为结构字段,在channel里传送

##### 闭包复制的是原对象指针,这样就能解释延迟引用现象

```go
func test() func() {
    x := 100
    fmt.Printf("x (%p) = %d\n", &x, x)
    return func() {
        fmt.Printf("x (%p) = %d\n", &x, x)
    }
}
func main() {
    f := test()
    f()
}
```

```
输出:

    x (0x2101ef018) = 100
    x (0x2101ef018) = 100
```

## 3.5 延迟调用

##### defer语句负责在其所在的函数`返回`时执行一个`函数(或方法)`。通常 于释放资源或错误处理

##### 其参数在到达defer语句那个时刻被求值或复制, 可用指针或闭包 "延迟" 读取。

```go
func test() {
    x, y := 10, 20
    defer func(i int) {
        println("defer:", i, y) // y 闭包引用 
    }(x) // x 被复制
    x += 10
    y += 100
    println("x =", x, "y =", y)
}
--输出
x = 20 y = 120
defer: 10 120
```

##### 其函数在返回时才被执行


##### 多个 defer 注册,按 FILO 次序执, 某个延迟调用出错，不会影响其他defer执行

```go
func test(x int) {
    defer println("a")
    defer println("b")
    defer func() {
        println(100 / x)  // div0 异常未被捕获,逐步往外传递,最终进程被panic中止
    }()
    defer println("c")
}
func main() {
    test(0)
}

--输出
c
b
a
panic: runtime error: integer divide by zero
```




##### 滥用 defer 可能会导致性能问题


## 3.6 错误处理

##### 没有结构化异常, panic 抛出错误,recover 捕获错误

```go
func test() {
    defer func() {
        if err := recover(); err != nil {
            println(err.(string))  // 将 interface{} 转型为具体类型
        } 
    }()    
    
    panic("panic error!")
}
```

##### panic、recover 参数类型为 interface{}, 因此可抛出任何类型对象

```go
func panic( v interface{} )
func recover() interface{} 
```


##### 延迟调用中引发的错误,可被后续延迟调用捕获,但仅最后1个错误可被捕获。

```go
func test() {
    defer func() {
        fmt.Println(recover())
    }()
    defer func() {
        panic("defer panic")
    }()
    panic("test panic")
}
func main() {
    test()
}
--输出
defer panic
```

##### recover 只有`defer` 语句中`直接`调用才会中止错误, 其他调用方式总是返回 nil

```go
func test() {
    defer recover()     //无效
    defer fmt.Println(recover())  //无效
    defer func() {  
        func() {
            println("defer inner")
            recover()   //无效
        }()
    }()
    
    panic("test panic")
}            
```

##### 使用前面的 延迟匿名函数 或 下面的调用, 都是有效的

```go
func except() {
    recover()
}
func test() {
    defer except()
    panic("test panic")
}
```

##### 如果需要保护代码片段，可将代码块重构成匿名函数,确保后续代码被执行。

```go
func test(x, y int) {
    var z int
    func() {
        defer func() {
            if recover() != nil { z = 0 }
        }()
        z=x/y
        return 
    }()
    println("x / y =", z)
}
```

##### 除 panic 引发中断性错误外, 还可返回 error类型错误对象 来表示函数调用状态。

```go
var ErrDivByZero = errors.New("division by zero")
func div(x, y int) (int, error) {
    if y == 0 { return 0, ErrDivByZero }
    return x / y, nil
}
func main() {
    switch z, err := div(10, 0); err {
    case nil:
        println(z)
    case ErrDivByZero:
        panic(err)
    } 
}
```

##### 导致关键流程出现不可修复性错误的 使  panic,其他使  error


