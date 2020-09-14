...menustart

- [函数](#870a51ba2a9edfadc62ce99af52cabd1)
    - [3.1 函数定义](#c12799e982852e4e19b2c3afddcf265b)
        - [支持不定长变参](#6b1ece767ec627c33b23ef33f7f130ff)
        - [支持多返回值](#93f1466b882df0265159a9c64524704f)
        - [支持返回参数命名](#8aa862e9fbf2a37aa787cf2ea2f6515b)
        - [支持匿名函数和闭包](#91f77fc3e07e5916ea7aba9ef6ce2985)
        - [不支持嵌套 nested](#017823a03ed6eddeba014f3250c56e38)
        - [不支持重载 overload](#a9fe03720cecb6f29ac53248744e0fd9)
        - [不支持默认参数 default parameter)](#86d105499c94114eab08a5e99c9550a4)
    - [3.2 变参](#288a51e0d8a97a004c3e964667f7bb80)
        - [变参本质上是 slice, 只能有一个,且必须最后一个](#580ff914a883306238e3d43572b9a2e4)
        - [使用 slice 做变参调用时，必须展开](#4444d1f4fb2060bdd4d39f341cb27574)
    - [3.3 返回值](#572562ff91a0c849992e9fa3f8d97e3c)
        - [多返回值可以直接作为其他函数调用实参](#7af6bec22b6a7431ab75ff7dead56697)
        - [命名返回参数可看作与形参类似的局部变量，最后由return隐式返回](#064ebb2a2b70879a64f0a239f3ed4571)
        - [命名返回参数可被同名局部变量遮蔽，此时需要显式返回](#809bae1685ec98b97a20afe28e7ebd38)
        - [命名返回参数允许defer延迟调用通过闭包读取和修改](#1308e0c8b52c9eb96ffbb64436bdcbcb)
    - [3.4 匿名函数](#52f6f3d48f58efeb20ef696a58d52049)
        - [可以赋值给变量,作为结构字段,在channel里传送](#25bffa305bf3cffc921bdee39b75616c)
        - [闭包复制的是原对象指针,这样就能解释延迟引用现象](#eabf7dade0caa9ac3f5c8f928b40faa2)
    - [3.5 延迟调用](#1f016538f2121f87c69bd99e55b03b62)
        - [defer语句负责在其所在的函数`返回`时执行一个`函数(或方法)`。通常 于释放资源或错误处理](#ffc54bbd6d265fe81a6206355a4dcf4a)
        - [其参数在到达defer语句那个时刻被求值或复制, 可用指针或闭包 "延迟" 读取。](#656191fa443f8560a5dd6f3001c80a58)
        - [其函数在返回时才被执行](#6943746e0f19f257d36274e00035675f)
        - [多个 defer 注册,按 FILO 次序执, 某个延迟调用出错，不会影响其他defer执行](#5c124fb1c0ac6e2fee07eb017bbed33c)
        - [滥用 defer 可能会导致性能问题](#d95061647bcc3e8e44bd8e2e915fa46f)
    - [3.6 错误处理](#1ea010fbf9f6ee56e3f62131242505f4)
        - [没有结构化异常, panic 抛出错误,recover 捕获错误](#4cbf49d27c3bd4e9536e577682188c10)
        - [panic、recover 参数类型为 interface{}, 因此可抛出任何类型对象](#a66cebc765b8b25cb4a975c26bdf6f83)
        - [延迟调用中引发的错误,可被后续延迟调用捕获,但仅最后1个错误可被捕获。](#10c1de3264a95fe75f4d9c103358f3fd)
        - [recover 只有`defer` 语句中`直接`调用才会中止错误, 其他调用方式总是返回 nil](#fd1722d28270f4c115d3f3d87194ba71)
        - [使用前面的 延迟匿名函数 或 下面的调用, 都是有效的](#5907e4f16ae7ab21d99963556aeed548)
        - [如果需要保护代码片段，可将代码块重构成匿名函数,确保后续代码被执行。](#0a5cb369a93acf915773425c56f64e1e)
        - [除 panic 引发中断性错误外, 还可返回 error类型错误对象 来表示函数调用状态。](#4d19dc649fd597dc6a1a59be9fc03da2)
        - [导致关键流程出现不可修复性错误的 使  panic,其他使  error](#f333271d774dc517cf559daeff89f9c0)

...menuend


<h2 id="870a51ba2a9edfadc62ce99af52cabd1"></h2>


# 函数

<h2 id="c12799e982852e4e19b2c3afddcf265b"></h2>


## 3.1 函数定义

```go
func test(x, y int, s string) (int, string) {
    //类型相同的相邻参数可合并
    n := x + y      // 多返回值必须使用括号
    return n, fmt.Sprintf(s, n)
}
```

<h2 id="6b1ece767ec627c33b23ef33f7f130ff"></h2>


##### 支持不定长变参
<h2 id="93f1466b882df0265159a9c64524704f"></h2>


##### 支持多返回值
<h2 id="8aa862e9fbf2a37aa787cf2ea2f6515b"></h2>


##### 支持返回参数命名
<h2 id="91f77fc3e07e5916ea7aba9ef6ce2985"></h2>


##### 支持匿名函数和闭包

<h2 id="017823a03ed6eddeba014f3250c56e38"></h2>


##### 不支持嵌套 nested
<h2 id="a9fe03720cecb6f29ac53248744e0fd9"></h2>


##### 不支持重载 overload
<h2 id="86d105499c94114eab08a5e99c9550a4"></h2>


##### 不支持默认参数 default parameter)

<h2 id="288a51e0d8a97a004c3e964667f7bb80"></h2>


## 3.2 变参

<h2 id="580ff914a883306238e3d43572b9a2e4"></h2>


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

<h2 id="4444d1f4fb2060bdd4d39f341cb27574"></h2>


##### 使用 slice 做变参调用时，必须展开

```go
func main() {
    s := []int{1, 2, 3}
    println(test("sum: %d", s...))
}
```

<h2 id="572562ff91a0c849992e9fa3f8d97e3c"></h2>


## 3.3 返回值

<h2 id="7af6bec22b6a7431ab75ff7dead56697"></h2>


##### 多返回值可以直接作为其他函数调用实参

<h2 id="064ebb2a2b70879a64f0a239f3ed4571"></h2>


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

<h2 id="809bae1685ec98b97a20afe28e7ebd38"></h2>


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

<h2 id="1308e0c8b52c9eb96ffbb64436bdcbcb"></h2>


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

    这个特性应该只是 `defer` 的副作用, 
    具体在什么场景使用就要由开发者自己决定了



<h2 id="52f6f3d48f58efeb20ef696a58d52049"></h2>


## 3.4 匿名函数

<h2 id="25bffa305bf3cffc921bdee39b75616c"></h2>


##### 可以赋值给变量,作为结构字段,在channel里传送

<h2 id="eabf7dade0caa9ac3f5c8f928b40faa2"></h2>


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

<h2 id="1f016538f2121f87c69bd99e55b03b62"></h2>


## 3.5 延迟调用

<h2 id="ffc54bbd6d265fe81a6206355a4dcf4a"></h2>


##### defer语句负责在其所在的函数`返回`时执行一个`函数(或方法)`。通常 于释放资源或错误处理

<h2 id="656191fa443f8560a5dd6f3001c80a58"></h2>


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

<h2 id="6943746e0f19f257d36274e00035675f"></h2>


##### 其函数在返回时才被执行


<h2 id="5c124fb1c0ac6e2fee07eb017bbed33c"></h2>


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




<h2 id="d95061647bcc3e8e44bd8e2e915fa46f"></h2>


##### 滥用 defer 可能会导致性能问题


<h2 id="1ea010fbf9f6ee56e3f62131242505f4"></h2>


## 3.6 错误处理

<h2 id="4cbf49d27c3bd4e9536e577682188c10"></h2>


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

<h2 id="a66cebc765b8b25cb4a975c26bdf6f83"></h2>


##### panic、recover 参数类型为 interface{}, 因此可抛出任何类型对象

```go
func panic( v interface{} )
func recover() interface{} 
```


<h2 id="10c1de3264a95fe75f4d9c103358f3fd"></h2>


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

<h2 id="fd1722d28270f4c115d3f3d87194ba71"></h2>


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

<h2 id="5907e4f16ae7ab21d99963556aeed548"></h2>


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

<h2 id="0a5cb369a93acf915773425c56f64e1e"></h2>


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

<h2 id="4d19dc649fd597dc6a1a59be9fc03da2"></h2>


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

<h2 id="f333271d774dc517cf559daeff89f9c0"></h2>


##### 导致关键流程出现不可修复性错误的 使  panic,其他使  error


