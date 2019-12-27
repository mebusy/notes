...menustart

 - [方法](#ea340b9dda8b893ddf2d9176220aac32)
     - [5.1 方法定义](#89f5575dc3c2d8e39f009c792002201c)
         - [只能为当前包内 命名类型 定义方法](#cb59a58fa426f9999a2a17b5f08aba80)
         - [没有构造和析构方法，通常用简单工程模式返回对象实例](#2b00cc26a62167782e3d966d32c080af)
         - [参数 receiver 可任意命名，也可以省略](#c2ef42bd331baf36f20e9646dea6da58)
         - [参数receiver类型可以是 T 或 *T](#81c78f04cb7560388e0d55ffd7f07b19)
         - [基类型T 不能是 接口或 指针](#a7f75662d9520457764fd01c033612e5)
         - [可以实例value或pointer调用全部方法，编译器自动转换](#6d460b8c25a84cf1de1c34750000e3a8)
     - [5.2 匿名字段](#ffbbf5b406bd2210266968745ac2c02d)
         - [可以像字段成员那样访问匿名字段方法，编译器负责查找](#15476f84b5c24be29d50dd22d19ae525)
         - [通过匿名字段，可获得和继承类似的复用能力](#6c9541f41311ab1eebf28a6706b41224)
         - [在外层定义同名方法, 就可以实现 override](#c3d0e8c0bea5d8c8f0e3a7b227709d8c)
     - [5.3 表达式](#1abc1bf6c23243be621b4263e46fe771)
         - [注意: 方法value会复制receiver](#d1c71e5a0cf2f121067f46bd2d73fae8)
         - [method value和闭包 实现方式相同,实际返回FuncVal类型对象](#62d1e1b4496f4bc6655d3fa0ca283c01)
     - [5.4 方法集](#18a3640f058cbdbbab8f2c73abcdbf32)
         - [使用 方法表达式 的时候，需要注意方法集](#7890ce32dbf3f41637771765ed06aee7)
         - [类型T 方法集包含 receiver T 方法](#80c52cc54adcaa6401e1f84c1802e504)
         - [类型*T 方法集包含 receiver T + receiver *T 方法](#7b87dd62941aeee66f3b724ed347de57)
         - [类型 S包含匿名 T, 则S方法集包含 T 方法](#dcd56429ed2339afccdc4e4ede7e08d0)
         - [类型 S包含匿名 *T, 则S方法集包含 T + *T 方法](#65aa5e87b85df7b4923ef6cc856194a6)
         - [不论嵌入 T或*T, *S 方法集总是包含 T + *T 方法](#3b702da3bdd1ba387db099309dcceb72)
         - [用实例value或 pointer调用方法不受方法集约束](#3e12f098448b6572e3192cf7e7846461)
 - [接口 interface](#57f2ffaf14788e0050594f8ce0c6a134)
     - [6.1 接口定义](#6a72925f32afa3ff12617d249a0f86ff)
         - [接口是方法签名的集合](#692de9b0a54655802f83e4974bfe57ce)
         - [类型方法集中 拥有与接口对应的全部方法，就实现了该接口](#e66632238ab3e4115c7db3d54c0afd3c)
         - [接口命名习惯以 er 结尾，结构体](#e56b1ae641e9775362a66915aa5534df)
         - [接口中可以嵌入其他接口](#bb05456de1d5da54d0e099786a833846)
         - [空接口 interface{} 没有任何方法签名, 任何类型都实现了空接口](#529226f855a6548337ed66083f4c5ca8)
         - [匿名接口可用作变量类型, 或结构成员](#f17c0e3cb5964cfec0b082d50d8e36d2)
     - [6.2 执行机制](#d24b5171452124598b04254b5cb0572d)
         - [接口对象由接口表(interface table)指针 和数据指针组成](#b2d36ea79da4d01531b631b81ecfd3ec)
         - [数据指针持有的是目标对象的只读复制品, 复制完整对象 或指针](#e54c78ab99f2ef0f785e9d5061e99317)
         - [接口类型返回临时对象，只有指针才能修改其状态 (参考map 取值)](#11be92b9ff3c1d0e298e8a1434ce4351)
         - [只有 tab 和 data 都为 nil 时,接⼝才等于 nil](#0dad826b0a889e64861135de276fc1b9)
     - [6.3 接⼝转换](#da9e2eae4d985d6ab55ece99faf75d43)
         - [利用类型推断, 判断接口对象是否是 某个具体的接口或类型](#8397c802bcfa8ebabd50167063cd6766)
         - [用 switch 做批量 类型判断,不支持 fallthrough](#7ef91bde805ff5a99acc4869a3e892b1)
         - [超集接口对象 可以转为 子集接口， 反之出错](#e22517a0a99fccfc40fa94916db115ff)
     - [6.4 接口技巧](#d14e02b0e2f5b36b976f6adcdba535ee)
         - [让编译器检查，确保某个类型实现 接口](#e51931e1b204267a72cf1f21b8185b9c)
         - [让函数直接"实现"接口](#271a34f0fb6d790c4f6cb6f932c41bbe)

...menuend


<h2 id="ea340b9dda8b893ddf2d9176220aac32"></h2>


# 方法

<h2 id="89f5575dc3c2d8e39f009c792002201c"></h2>


## 5.1 方法定义

<h2 id="cb59a58fa426f9999a2a17b5f08aba80"></h2>


##### 只能为当前包内 命名类型 定义方法

```go
type Queue struct {
    elements []interface{}
}
```

<h2 id="2b00cc26a62167782e3d966d32c080af"></h2>


##### 没有构造和析构方法，通常用简单工程模式返回对象实例

```go
func NewQueue() *Queue {
    return &Queue{make([]interface{}, 10)}
}
```

<h2 id="c2ef42bd331baf36f20e9646dea6da58"></h2>


##### 参数 receiver 可任意命名，也可以省略

```go
func (*Queue) Push(e interface{}) error {
    panic("not implemented")
}
func (self0 *Queue) length() int {
    return len(self.elements)
}
```

<h2 id="81c78f04cb7560388e0d55ffd7f07b19"></h2>


##### 参数receiver类型可以是 T 或 *T

<h2 id="a7f75662d9520457764fd01c033612e5"></h2>


##### 基类型T 不能是 接口或 指针

<h2 id="6d460b8c25a84cf1de1c34750000e3a8"></h2>


##### 可以实例value或pointer调用全部方法，编译器自动转换

```go
type Data struct{
    x int
}
func (self Data) ValueTest() {
    fmt.Printf("Value: %p\n", &self)
}
func (self *Data) PointerTest() {
    fmt.Printf("Pointer: %p\n", self)
}
func main() {
    d := Data{}
    p := &d
    fmt.Printf("Data: %p\n", p)    // 0x2101ef018
    
    d.ValueTest()    // ValueTest(d)    0x2101ef028
    d.PointerTest()  // PointerTest(&d) 0x2101ef018
    p.ValueTest()    // ValueTest(*p)   0x2101ef030 
    p.PointerTest()  // PointerTest(p)  0x2101ef018
}
```

    PS: 因为是值类型，所以 valueTest 每次的地址都不一样


<h2 id="ffbbf5b406bd2210266968745ac2c02d"></h2>


## 5.2 匿名字段

<h2 id="15476f84b5c24be29d50dd22d19ae525"></h2>


##### 可以像字段成员那样访问匿名字段方法，编译器负责查找

<h2 id="6c9541f41311ab1eebf28a6706b41224"></h2>


##### 通过匿名字段，可获得和继承类似的复用能力

<h2 id="c3d0e8c0bea5d8c8f0e3a7b227709d8c"></h2>


##### 在外层定义同名方法, 就可以实现 override

```go
type User struct {
    id   int
    name string 
}
type Manager struct {
    User
    title string
}
func (self *User) ToString() string {
    return fmt.Sprintf("User: %p, %v", self, self)
}
func (self *Manager) ToString() string {
    return fmt.Sprintf("Manager: %p, %v", self, self)
}
func main() {
    m := Manager{User{1, "Tom"}, "Administrator"}
    fmt.Println(m.ToString())
    fmt.Println(m.User.ToString())
}
输出:
Manager: 0x2102271b0, &{{1 Tom} Administrator}
User   : 0x2102271b0, &{1 Tom}
```


<h2 id="1abc1bf6c23243be621b4263e46fe771"></h2>


## 5.3 表达式

方法分为两种表现形式

```go
instance.method(args...)        //方法 value
<type>.func(instance, args...)  //方法表达式
```

<h2 id="d1c71e5a0cf2f121067f46bd2d73fae8"></h2>


##### 注意: 方法value会复制receiver

```go
package main

import "fmt"

type User struct {
    id   int
    name string 
}
func (self User) Test() {
    fmt.Println(self)
}
func main() {
    u := User{1, "Tom"}
    mValue := u.Test  //receiver会被立即复制
    u.id, u.name = 2, "Jack"
    u.Test()        // 方法value调用
    mValue()        // 这个还是方法value调用
    User.Test( u )  // 方法表达式调用
}
输出:
{2 Jack}
{1 Tom}
{2 Jack}
```

<h2 id="62d1e1b4496f4bc6655d3fa0ca283c01"></h2>


##### method value和闭包 实现方式相同,实际返回FuncVal类型对象

```
FuncVal { method_address, receiver_copy }
```


<h2 id="18a3640f058cbdbbab8f2c73abcdbf32"></h2>


## 5.4 方法集

<h2 id="7890ce32dbf3f41637771765ed06aee7"></h2>


##### 使用 方法表达式 的时候，需要注意方法集

<h2 id="80c52cc54adcaa6401e1f84c1802e504"></h2>


##### 类型T 方法集包含 receiver T 方法

<h2 id="7b87dd62941aeee66f3b724ed347de57"></h2>


##### 类型*T 方法集包含 receiver T + receiver *T 方法

<h2 id="dcd56429ed2339afccdc4e4ede7e08d0"></h2>


##### 类型 S包含匿名 T, 则S方法集包含 T 方法

<h2 id="65aa5e87b85df7b4923ef6cc856194a6"></h2>


##### 类型 S包含匿名 *T, 则S方法集包含 T + *T 方法

<h2 id="3b702da3bdd1ba387db099309dcceb72"></h2>


##### 不论嵌入 T或*T, *S 方法集总是包含 T + *T 方法

<h2 id="3e12f098448b6572e3192cf7e7846461"></h2>


##### 用实例value或 pointer调用方法不受方法集约束


```go
type Data struct{}
func (Data) TestValue()    {}
func (*Data) TestPointer() {}

func main() {
    var p *Data = nil
    p.TestPointer()
    (*Data)(nil).TestPointer()  // method value
    (*Data).TestPointer(nil)    // method expression
    // p.TestValue()   //空指针
    // Data.TestValue(nil)  // nil不能转为Data
    // Data.TestPointer() //T方法集里没有receiver *T方法
}
```

---
---

<h2 id="57f2ffaf14788e0050594f8ce0c6a134"></h2>


# 接口 interface

<h2 id="6a72925f32afa3ff12617d249a0f86ff"></h2>


## 6.1 接口定义

<h2 id="692de9b0a54655802f83e4974bfe57ce"></h2>


##### 接口是方法签名的集合

<h2 id="e66632238ab3e4115c7db3d54c0afd3c"></h2>


##### 类型方法集中 拥有与接口对应的全部方法，就实现了该接口

    所谓对应方法，是指 方法名，参数类型，返回值类型 都相同。

<h2 id="e56b1ae641e9775362a66915aa5534df"></h2>


##### 接口命名习惯以 er 结尾，结构体

<h2 id="bb05456de1d5da54d0e099786a833846"></h2>


##### 接口中可以嵌入其他接口

```go
type Stringer interface {
    String() string
}
type Printer interface {
    Stringer            // 借口嵌入
    Print() 
}


func (self *User) String() string {
    return fmt.Sprintf("user %d, %s", self.id, self.name)
}
func (self *User) Print() {
    fmt.Println(self.String())
}
func main() {
    var t Printer = &User{1, "Tom"}  // *User 实现了 Printer接口
    t.Print()       // user 1, Tom
}
```

<h2 id="529226f855a6548337ed66083f4c5ca8"></h2>


##### 空接口 interface{} 没有任何方法签名, 任何类型都实现了空接口 

    interface{} 作用类似其他语言中的根对象 object


```go
func Print(v interface{}) {
    fmt.Printf("%T: %v\n", v, v)
}
func main() {
    Print(1)                // int: 1
    Print("Hello, World!")  // string: Hello, World!
}
```

<h2 id="f17c0e3cb5964cfec0b082d50d8e36d2"></h2>


##### 匿名接口可用作变量类型, 或结构成员

```go
type Tester struct {
    s interface {
        String() string
    }
}
```

<h2 id="d24b5171452124598b04254b5cb0572d"></h2>


## 6.2 执行机制

<h2 id="b2d36ea79da4d01531b631b81ecfd3ec"></h2>


##### 接口对象由接口表(interface table)指针 和数据指针组成

```go
struct Iface
{
    Itab* tab;
    void*    data;
};
```

---
<h2 id="e54c78ab99f2ef0f785e9d5061e99317"></h2>


##### 数据指针持有的是目标对象的只读复制品, 复制完整对象 或指针

```go
type User struct {
    id   int
    name string 
}

func main() {
    u := User{1, "Tom"}
    var i interface{} = u   // 复制 结构体
    u.id = 2
    u.name = "Jack"
    fmt.Printf("%v\n", u)           // {2 Jack}
    fmt.Printf("%v\n", i.(User))    // {1 Tom}
}
```

---
<h2 id="11be92b9ff3c1d0e298e8a1434ce4351"></h2>


##### 接口类型返回临时对象，只有指针才能修改其状态 (参考map 取值)

```go
type User struct {
    id   int
    name string 
}
func main() {
    u := User{1, "Tom"}
    var vi, pi interface{} = u, &u
    // vi.(User).name = "Jack"   // cannot assign to vi.(User).name
    pi.(*User).name = "Jack"
    fmt.Printf("%v\n", vi.(User))   // {1 Tom}
    fmt.Printf("%v\n", pi.(*User))  // &{1 Jack}
}
```

---
<h2 id="0dad826b0a889e64861135de276fc1b9"></h2>


##### 只有 tab 和 data 都为 nil 时,接⼝才等于 nil

```go
var a interface{} = nil         // tab = nil, data = nil
var b interface{} = (*int)(nil) // tab 包含 *int 类型信息, data = nil
```

<h2 id="da9e2eae4d985d6ab55ece99faf75d43"></h2>


## 6.3 接⼝转换

<h2 id="8397c802bcfa8ebabd50167063cd6766"></h2>


##### 利用类型推断, 判断接口对象是否是 某个具体的接口或类型

```go
type User struct {
    id   int
    name string
}
func (self *User) String() string {
    return fmt.Sprintf("%d, %s", self.id, self.name)
}
func main() {
    var o interface{} = &User{1, "Tom"}  
    if i, ok := o.(fmt.Stringer); ok {  // ok-idiom
        fmt.Println(i)   // 1, Tom 
    }
    u := o.(*User)
    // u := o.(User)  // panic: *main.User, not main.User
    fmt.Println(u)    // 1, Tome
}
```

---
<h2 id="7ef91bde805ff5a99acc4869a3e892b1"></h2>


##### 用 switch 做批量 类型判断,不支持 fallthrough

```go
func main() {
    var o interface{} = &User{1, "Tom"}
    switch v := o.(type) {
    case nil:                   // o == nil
        fmt.Println("nil")
    case fmt.Stringer:          // interface
        fmt.Println(v)
    case func() string:         // func
        fmt.Println(v())
    case *User:                 // *struct
        fmt.Printf("%d, %s\n", v.id, v.name)    
    default:
        fmt.Println("unknown")
    } 
}
```

<h2 id="e22517a0a99fccfc40fa94916db115ff"></h2>


##### 超集接口对象 可以转为 子集接口， 反之出错

<h2 id="d14e02b0e2f5b36b976f6adcdba535ee"></h2>


## 6.4 接口技巧

<h2 id="e51931e1b204267a72cf1f21b8185b9c"></h2>


##### 让编译器检查，确保某个类型实现 接口

```go
// 确保 *Data 实现 fmt.Stringer 接口
var _ fmt.Stringer = (*Data)(nil)
```

---

<h2 id="271a34f0fb6d790c4f6cb6f932c41bbe"></h2>


##### 让函数直接"实现"接口

```go
type Tester interface {  // Tester接口，需要实现 Do()方法
    Do()
}
type FuncDo func()      // 定义一个方法类型 FuncDo
func (self FuncDo) Do() { self() }  // FuncDo 实现了 Tester 接口

func main() {
    // 匿名方法转为 FuncDo 类型，再赋值给 Tester接口对象
    var t Tester = FuncDo(func() { println("Hello, World!") })
    t.Do()
}
```










