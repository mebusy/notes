# Reflect 反射

    Reflect 反射
        没有运行期类型对象
    9.4.1 reflect.Type
        获取struct对象 成员字段信息，包括非导出和匿名字段
        如果是指针，先使用 Elem方法获取目标类型
        value-inferface 和 point-interface 方法集存在差异
        直接使用名称 或 序号 访问字段
        字段标签可实现简单元数据编程
        可从基本类型获取所对应的复合类型
        方法 Elem 可返回复合类型的 基类型
        方法 Implements 判断是否实现了某个接口
        获取对齐信息，对于内存自动分析很有用
    9.4.2 reflect.Value
        Value 和 Type 使用方法类似,包括 Elem方法
        其他复合类型 array , slice ,map 取值示例
        IsNil方法判断 接口 data值是否为空
        复合类型修改示例 TODO
    9.4.3 Method
        可获取方法参数, 返回值类型等信息
        动态调用, 按 in 列表准备所需参数 TODO


##### 没有运行期类型对象

# 9.4.1 reflect.Type

##### 获取struct对象 成员字段信息，包括非导出和匿名字段

```go
type User struct {
    Username string
}
type Admin struct {
    User
    title string
}
func main() {
    var u Admin
    t := reflect.TypeOf(u)
    for i, n := 0, t.NumField(); i < n; i++ {
        f := t.Field(i)
        fmt.Println(f.Name, f.Type)
    }
}    
输出:
User main.User
title string
```

##### 如果是指针，先使用 Elem方法获取目标类型

```go
func main() {
    u := new(Admin)
    t := reflect.TypeOf(u)
    if t.Kind() == reflect.Ptr { // 是指针
        t = t.Elem()    // 进而获取 目标类型
    }
    for i, n := 0, t.NumField(); i < n; i++ {
        f := t.Field(i)
        fmt.Println(f.Name, f.Type)
    }
}
```


##### value-inferface 和 point-interface 方法集存在差异

```go
type User struct {
}
type Admin struct {
    User
}
func (*User) ToString() {}
func (Admin) test()     {}

func main() {
    var u Admin
    methods := func(t reflect.Type) {
        for i, n := 0, t.NumMethod(); i < n; i++ {
            m := t.Method(i)
            fmt.Println(m.Name)
        }
    }
    fmt.Println("--- value interface ---")
    methods(reflect.TypeOf(u))
    fmt.Println("--- pointer interface ---")
    methods(reflect.TypeOf(&u))
}
输出:
--- value interface ---
test        // 只有 test 方法
--- pointer interface ---
ToString
test
```

##### 直接使用名称 或 序号 访问字段

```go
type User struct {
    Username string
age int }
type Admin struct {
    User
    title string
}
func main() {
    var u Admin
    t := reflect.TypeOf(u)
    f, _ := t.FieldByName("title")
    fmt.Println(f.Name) // title
    f, _ = t.FieldByName("User")
    fmt.Println(f.Name) // User
    
    f, _ = t.FieldByName("Username")
    fmt.Println(f.Name)  // Username
    
    // Admin[0] -> User[1] -> age
    f = t.FieldByIndex([]int{0, 1})    
    fmt.Println(f.Name)     //age
}
```

##### 字段标签可实现简单元数据编程

```go
type User struct {
    Name string `field:"username" type:"nvarchar(20)"`
    Age  int    `field:"age" type:"tinyint"`
}
func main() {
    var u User
    t := reflect.TypeOf(u)
    f, _ := t.FieldByName("Name")
    fmt.Println(f.Tag)  
    //输出: field:"username" type:"nvarchar(20)"
    fmt.Println(f.Tag.Get("field")) // username
    fmt.Println(f.Tag.Get("type"))  // nvarchar(20)
}
```

##### 可从基本类型获取所对应的复合类型

```go
var (
    Int    = reflect.TypeOf(0)
    String = reflect.TypeOf("")
)
func main() {
    c := reflect.ChanOf(reflect.SendDir, String)
    fmt.Println(c)  // chan<- string
    m := reflect.MapOf(String, Int)
    fmt.Println(m)  // map[string]int
    s := reflect.SliceOf(Int)
    fmt.Println(s)  // []int
    t := struct{ Name string }{}
    p := reflect.PtrTo(reflect.TypeOf(t))
    fmt.Println(p)  // *struct { Name string }
}
```

##### 方法 Elem 可返回复合类型的 基类型

```go
func main() {
    t := reflect.TypeOf(make(chan int)).Elem()
    fmt.Println(t)      // int
}
```

##### 方法 Implements 判断是否实现了某个接口

```go
type Data struct {
}
func (*Data) String() string {
    return ""
}
func main() {
    var d *Data
    t := reflect.TypeOf(d)
    it := reflect.TypeOf((*fmt.Stringer)(nil)).Elem()
    fmt.Println(t.Implements(it))
}
```

##### 获取对齐信息，对于内存自动分析很有用

```go
type Data struct {
    b   byte
x int32 }
func main() {
    var d Data
    t := reflect.TypeOf(d)
    fmt.Println(t.Size(), t.Align())    // 8 4
    f, _ := t.FieldByName("b")
    fmt.Println(f.Type.FieldAlign())    // 1
}
```

## 9.4.2 reflect.Value

##### Value 和 Type 使用方法类似,包括 Elem方法

```go
type User struct {
    Username string
    age int 
}
type Admin struct {
    User
    title string
}
func main() {
    u := &Admin{User{"Jack", 23}, "NT"}
    v := reflect.ValueOf(u).Elem()
    
    fmt.Println(v.FieldByName("title").String()) // NT
    fmt.Println(v.FieldByName("age").Int())   // 23
    fmt.Println(v.FieldByIndex([]int{0, 1}).Int()) // 23
}
```

除返回具体的 .String() .Int(), 还可返回.Interface()

.Interface() 非导出字段不能用，用CanInterface判断一下。

```go
type User struct {
    Username string
    age int 
}
func main() {
    u := User{"Jack", 23}
    v := reflect.ValueOf(u)
    fmt.Println(v.FieldByName("Username").Interface())
    //输出: Jack
    fmt.Println(v.FieldByName("age").Interface())
    //输出: panic: unexported field 
    
    // 转化成具体类型却不会 引发panic
    fmt.Println(v.FieldByName("age").Int())
    // 输出: 23
}
```

##### 其他复合类型 array , slice ,map 取值示例

```go
func main() {
    // slice
    v := reflect.ValueOf([]int{1, 2, 3})
    for i, n := 0, v.Len(); i < n; i++ {
        fmt.Println(v.Index(i).Int())
    }
    
    // map
    fmt.Println("---------------------------")
    v = reflect.ValueOf(map[string]int{"a": 1, "b": 2})
    for _, k := range v.MapKeys() {
        fmt.Println(k.String(), v.MapIndex(k).Int())
    }
}
输出:
1
2
3 
--------------------------- 
a1
b2
```

需要注意, Value某些方法没有遵循'comma ok'模式,

而是返回zero value, 要用 IsValid 判断一下.

```go
type User struct {
    Username string
    age int 
}
func main() {
    u := User{}
    v := reflect.ValueOf(u)
    f := v.FieldByName("a")
    fmt.Println(f.Kind(), f.IsValid()) // invalid false
}
```

#####  IsNil方法判断 接口 data值是否为空

```go
func main() {
    var p *int
    var x interface{} = p
    fmt.Println(x == nil)   // false
    v := reflect.ValueOf(p)
    fmt.Println(v.Kind(), v.IsNil()) // ptr true
}
```

##### 复合类型修改示例  TODO

---

## 9.4.3 Method

##### 可获取方法参数, 返回值类型等信息

```go
type Data struct {
}
func (*Data) Test(x, y int) (int, int) {
    return x + 100, y + 100
}
func (*Data) Sum(s string, x ...int) string {
    c := 0
    for _, n := range x {
        c += n
    }
    return fmt.Sprintf(s, c)
}
func info(m reflect.Method) {
    t := m.Type
    fmt.Println(m.Name) // 方法名
    // 参数类型
    for i, n := 0, t.NumIn(); i < n; i++ {
        fmt.Printf("  in[%d] %v\n", i, t.In(i))
    }
    // 返回值类型
    for i, n := 0, t.NumOut(); i < n; i++ {
        fmt.Printf("  out[%d] %v\n", i, t.Out(i))
    } 
}

func main() {
    d := new(Data)
    t := reflect.TypeOf(d)
    
    // 反射获取方法
    test, _ := t.MethodByName("Test")
    info(test)
    
    sum, _ := t.MethodByName("Sum")
    info(sum) 
}
输出:
Test
  in[0] *main.Data
  in[1] int
  in[2] int
  out[0] int
  out[1] int
Sum
  in[0] *main.Data
  in[1] string
  in[2] []int
  out[0] string
```

##### 动态调用, 按 in 列表准备所需参数  TODO


