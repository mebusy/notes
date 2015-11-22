
    5.1 方法定义
        只能为当前包内 命名类型 定义方法
        没有构造和析构方法，通常用简单工程模式返回对象实例
        参数 receiver 可任意命名，也可以省略
        参数receiver类型可以是 T 或 *T
        基类型T 不能是 接口或 指针
        可以实例value或pointer调用全部方法，编译器自动转换
    5.2 匿名字段
        可以像字段成员那样访问匿名字段方法，编译器负责查找
        通过匿名字段，可获得和继承类似的复用能力
        在外层定义同名方法, 就可以实现 override
    5.3 表达式
        注意: 方法value会复制receiver
        method value和闭包 实现方式相同,实际返回FuncVal类型对象
    5.4 方法集
        使用 方法表达式 的时候，需要注意方法集
        类型T 方法集包含 receiver T 方法
        类型*T 方法集包含 receiver T + receiver *T 方法
        类型 S包含匿名 T, 则S方法集包含 T 方法
        类型 S包含匿名 *T, 则S方法集包含 T + *T 方法
        不论嵌入 T或*T, *S 方法集总是包含 T + *T 方法
        用实例value或 pointer调用方法不受方法集约束
        
    6.1 接口定义
        接口是方法签名的集合
        类型方法集中 拥有与接口对应的全部方法，就实现了该接口
        接口命名习惯以 er 结尾，结构体
        接口中可以嵌入其他接口
        空接口 interface{} 没有任何方法签名, 任何类型都实现了空接口
        匿名接口可用作变量类型, 或结构成员
    6.2 执行机制
        接口对象由接口表(interface table)指针 和数据指针组成
        数据指针持有的是目标对象的只读复制品, 复制完整对象 或指针
        接口类型返回临时对象，只有指针才能修改其状态 (参考map 取值)
        只有 tab 和 data 都为 nil 时,接⼝才等于 nil
    6.3 接⼝转换
        利用类型推断, 判断接口对象是否是 某个具体的接口或类型
        用 switch 做批量 类型判断,不支持 fallthrough
        超集接口对象 可以转为 子集接口， 反之出错
    6.4 借口技巧
        让编译器检查，确保某个类型实现 接口
        让函数直接"实现"接口

# 方法

## 5.1 方法定义

##### 只能为当前包内 命名类型 定义方法

```go
type Queue struct {
    elements []interface{}
}
```

##### 没有构造和析构方法，通常用简单工程模式返回对象实例

```go
func NewQueue() *Queue {
    return &Queue{make([]interface{}, 10)}
}
```

##### 参数 receiver 可任意命名，也可以省略

```go
func (*Queue) Push(e interface{}) error {
    panic("not implemented")
}
func (self0 *Queue) length() int {
    return len(self.elements)
}
```

##### 参数receiver类型可以是 T 或 *T

##### 基类型T 不能是 接口或 指针

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


## 5.2 匿名字段

##### 可以像字段成员那样访问匿名字段方法，编译器负责查找

##### 通过匿名字段，可获得和继承类似的复用能力

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


## 5.3 表达式

方法分为两种表现形式

```go
instance.method(args...)        //方法 value
<type>.func(instance, args...)  //方法表达式
```

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

##### method value和闭包 实现方式相同,实际返回FuncVal类型对象

```
FuncVal { method_address, receiver_copy }
```


## 5.4 方法集

##### 使用 方法表达式 的时候，需要注意方法集

##### 类型T 方法集包含 receiver T 方法

##### 类型*T 方法集包含 receiver T + receiver *T 方法

##### 类型 S包含匿名 T, 则S方法集包含 T 方法

##### 类型 S包含匿名 *T, 则S方法集包含 T + *T 方法

##### 不论嵌入 T或*T, *S 方法集总是包含 T + *T 方法

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

# 接口 interface

## 6.1 接口定义

##### 接口是方法签名的集合

##### 类型方法集中 拥有与接口对应的全部方法，就实现了该接口

    所谓对应方法，是指 方法名，参数类型，返回值类型 都相同。

##### 接口命名习惯以 er 结尾，结构体

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

##### 匿名接口可用作变量类型, 或结构成员

```go
type Tester struct {
    s interface {
        String() string
    }
}
```

## 6.2 执行机制

##### 接口对象由接口表(interface table)指针 和数据指针组成

```go
struct Iface
{
    Itab* tab;
    void*    data;
};
```

---
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
##### 只有 tab 和 data 都为 nil 时,接⼝才等于 nil

```go
var a interface{} = nil         // tab = nil, data = nil
var b interface{} = (*int)(nil) // tab 包含 *int 类型信息, data = nil
```

## 6.3 接⼝转换

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

##### 超集接口对象 可以转为 子集接口， 反之出错

## 6.4 接口技巧

##### 让编译器检查，确保某个类型实现 接口

```go
// 确保 *Data 实现 fmt.Stringer 接口
var _ fmt.Stringer = (*Data)(nil)
```

---

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










