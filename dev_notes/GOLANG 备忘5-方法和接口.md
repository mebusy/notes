
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










