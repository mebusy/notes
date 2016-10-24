...menustart

 - [Reflect 反射](#139b6cfcf3c9439de790ce9742996f82)
	 - [没有运行期类型对象](#0318e04c3f2eb7a1984ee102d5a2ed1c)
 - [9.4.1 reflect.Type](#8c6859ae778598e709e07536f5173e72)
	 - [获取struct对象 成员字段信息，包括非导出和匿名字段](#b4f395a0193ad2063ac51bafe5bde7cb)
	 - [如果是指针，先使用 Elem方法获取目标类型](#68093d5b129ae6d66b666d017e2519a8)
	 - [value-inferface 和 point-interface 方法集存在差异](#b101897a62b1b9a5ce74504373ba727c)
	 - [直接使用名称 或 序号 访问字段](#b11cc2af540eb66182778242f042879b)
	 - [字段标签可实现简单元数据编程](#258b3955c18942a2557b3793fa3877d3)
	 - [可从基本类型获取所对应的复合类型](#b499e680690478b9e2d378d15701fdc2)
	 - [方法 Elem 可返回复合类型的 基类型](#0a7afa5b5f0c6e4ce1a3d2ac5ca84728)
	 - [方法 Implements 判断是否实现了某个接口](#0d8ba38963413fb3e0a37355baac5004)
	 - [获取对齐信息，对于内存自动分析很有用](#dfa77f624af44f20d93a02df20657a9f)
	 - [9.4.2 reflect.Value](#34ca7e92d333aacb70ded67fd6989dd0)
		 - [Value 和 Type 使用方法类似,包括 Elem方法](#e9fae0f567c7b19b714a1e0035740e52)
		 - [其他复合类型 array , slice ,map 取值示例](#bd597938c7e7c92297b5bbf47c1fbedf)
		 - [IsNil方法判断 接口 data值是否为空](#18917556ea9e2ef4a2d1352ea9490d13)
		 - [复合类型修改示例  TODO](#1646349e890242f255aca9e532cedfd6)
	 - [9.4.3 Method](#61e08fe2cac9cfa9a7ab1048eaa57974)
		 - [可获取方法参数, 返回值类型等信息](#82f01c4522eb5d25e3ab3e6f60bb72bb)
		 - [动态调用, 按 in 列表准备所需参数  TODO](#e4e8d5f98a70257af0a0544047a3b167)

...menuend


<h2 id="139b6cfcf3c9439de790ce9742996f82"></h2>
# Reflect 反射



<h2 id="0318e04c3f2eb7a1984ee102d5a2ed1c"></h2>
##### 没有运行期类型对象

<h2 id="8c6859ae778598e709e07536f5173e72"></h2>
# 9.4.1 reflect.Type

<h2 id="b4f395a0193ad2063ac51bafe5bde7cb"></h2>
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

<h2 id="68093d5b129ae6d66b666d017e2519a8"></h2>
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


<h2 id="b101897a62b1b9a5ce74504373ba727c"></h2>
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

<h2 id="b11cc2af540eb66182778242f042879b"></h2>
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

<h2 id="258b3955c18942a2557b3793fa3877d3"></h2>
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

<h2 id="b499e680690478b9e2d378d15701fdc2"></h2>
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

<h2 id="0a7afa5b5f0c6e4ce1a3d2ac5ca84728"></h2>
##### 方法 Elem 可返回复合类型的 基类型

```go
func main() {
    t := reflect.TypeOf(make(chan int)).Elem()
    fmt.Println(t)      // int
}
```

<h2 id="0d8ba38963413fb3e0a37355baac5004"></h2>
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

<h2 id="dfa77f624af44f20d93a02df20657a9f"></h2>
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

<h2 id="34ca7e92d333aacb70ded67fd6989dd0"></h2>
## 9.4.2 reflect.Value

<h2 id="e9fae0f567c7b19b714a1e0035740e52"></h2>
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

<h2 id="bd597938c7e7c92297b5bbf47c1fbedf"></h2>
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

<h2 id="18917556ea9e2ef4a2d1352ea9490d13"></h2>
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

<h2 id="1646349e890242f255aca9e532cedfd6"></h2>
##### 复合类型修改示例  TODO

---

<h2 id="61e08fe2cac9cfa9a7ab1048eaa57974"></h2>
## 9.4.3 Method

<h2 id="82f01c4522eb5d25e3ab3e6f60bb72bb"></h2>
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

<h2 id="e4e8d5f98a70257af0a0544047a3b167"></h2>
##### 动态调用, 按 in 列表准备所需参数  TODO


