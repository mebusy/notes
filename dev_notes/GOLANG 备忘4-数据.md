# 数据

## 4.1 Array

##### 数组是值类型,赋值和传参会复制整个数组
##### 数组长度必须是常量,且是类型的组成部分
##### [2]int 和 [3]int 是不同类型
##### 支持 "=="、"!=" 操作符
##### 指针数组 [n]*T,数组指针 *[n]T
##### 内置函数 len 和 cap  返回数组长度度

### 初始化

```go
a := [3]int{1, 2}   // 未初始化元素值为 0
b := [...]int{1, 2, 3, 4} // 通过初始化值确定数组长度
c := [5]int{2: 100, 4:200} // 使用索引号初始化元素
d := [...]struct {
    name string
    age uint8 
}{
    {"user1", 10},      // 可省略元素类型
    {"user2", 20},      // 别忘了最后  的逗号。
}
```

### 多维数组

```go
a := [2][3]int{{1, 2, 3}, {4, 5, 6}}
b := [...][2]int{{1, 1}, {2, 2}, {3, 3}}  //第二维需要确定长度
```

## 4.2 Slice

```go
struct Slice
{                        // must not move anything
    byte*    array;     // actual data
    uintgo   len;       // number of elements
    uintgo   cap;       // allocated number of elements
};
```

##### 属性 len 表示可用元素数量,读写操作不能超过该限制。
##### 属性 cap 表示最大扩张容量,不能超出数组限制
##### 如果 slice == nil,那么 len、cap 结果都等于 0

```go
--数组
data := [...]int{0, 1, 2, 3, 4, 5, 6}
--从已有数组创建slice
slice := data[1:4:5]         // 1. [low : high : max ]

--直接创建slice
s1 := []int{0, 1, 2, 3, 8: 100}  // 通过初始化表达式构造,可使用索引号
fmt.Println(s1, len(s1), cap(s1))  // [01230000100] 9 9

s2 := make([]int, 6, 8)         //使用 make 创建,指定 len 和 cap 值
fmt.Println(s2, len(s2), cap(s2))   //[000000] 6 8

s3 := make([]int, 6)   // 省略 cap,相当于 cap = len
fmt.Println(s3, len(s3), cap(s3))   //[000000] 6 6
```

    创建表达式1 使用的是 元素索引号，而非数量

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/go_slice.png)    

```go
--数组
data := [...]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```


expression | slice |   len |   cap |   comment
---|---|---|---|---
data[:6:8]  | [0 1 2 3 4 5] |6  | 8 |   省略 low
data[5:]    | [5 6 7 8 9]   |5  | 5 |   省略 high、max
data[:3]    | [0 1 2]       |3  |10 |   省略 low、max
data[:]     | [0123456789]  |10 |10 |   全部省略


##### [][]T,是指元素类型为 []T 

```go
data := [][]int{
    []int{1, 2, 3},
    []int{100, 200},
    []int{11, 22, 33, 44},
}
```


### 4.2.2 append

##### 向尾部添加数据,返回新的 slice 对象

##### 超出 slice.cap 限制, 重新分配底层数组

##### 及时释放不再使用的slice对象,避免过期引用


### 4.2.3 copy   copy( dst , src )

##### slice间复制数据，复制长度以 len 小的为准

##### 两个 slice 可以指向同一底层数组

##### 允许元素区间重叠


## 4.3 Map

##### 键必须是支持相等运算符(==,!=)类型

    比如: number,string,pointer, array, struct,以及对应的 interface

##### 预先给 make 函数一个合理cap 参数，有助于提升性能

```go
    m := make(map[string]int, 1000)
```

### 常见操作

##### if v, ok := m["a"]; ok {   // 判断key是否存在

##### 读取不存在的key 不会出错，直接返回 \0

##### delete(m, "c")   删除, key如果不存在,不会出错

##### map中取回的value是临时复制品,对array,struct类型value修改其成员是没有意义，且禁止的

```go
m0 := map[string] []int {
    "a": {1,2},
}
m0["a"][0]=3   // slice 可以正常修改
println( m0["a"][0]  )  // 3  

m := map[string] [4]int {
    "a": {1,2},
}
m["a"][0]=3   // cannot assign to m["a"][0]

m1 := map[string]struct{ name string }{
    "a": {"user1"},
}
m1["a"].name = "b"   // cannot assign to m1["a"].name

```

##### 正确修改array,struct类型value成员的做法是 整个替换 或 使用指针

```go
u := m1["a"]
u.name = "Tom"
m1["a"] = u
println( m1["a"].name )  // Tom 分步替换 value

m2 := map[string]*struct{ name string }{   //使用指针
    "a": & struct{ name string }{"user1"},
}
m2["a"].name = "Jack"
println( m2["a"].name  )  // Jack 
```

##### range 迭代期间可以安全删除键值, 但是新增键值会造成未知后果


## 4.4 Struct

##### 可用 _ 定义补位字段

##### 支持指向自身类型的指针成员

```go
type Node struct {
    _    int
    id   int
    data *byte
    next *Node
}
```

##### 使用字段名 部分初始化， 或提供全部字段值 顺序初始化

```go
n1 := Node{     // 有 _ 补位字段的struct 必须通过字段名初始化
    id: 1,      // 因为没有办法给 _ 字段 提供值
    data: nil, 
}

type User struct {
    name string
    age int 
}
u1 := User{"Tom", 20}
u2 := User{"Tom"}   // Error: too few values in struct initializer
```

##### 支持匿名结构，用作 结构成员，或 定义变量

```go
type File struct {
    name string
    size int
    attr struct {
	perm int
	owner int 
    }
}

f := File{
    name: "test.txt",
    size: 1025,
    //attr: {0755, 1},      //缺少type,无法初始化
}

f.attr.owner = 1
f.attr.perm = 0755

var attr = struct {
    perm  int
    owner int
}{2, 0755}

```


##### 支持"==", "!=" 操作, 可作 map 键类型

##### 可定义字段标签, 用反射读取。标签是类型的组成部分

```go
var u1 struct { name string "username" }
```

### 4.4.1 匿名字段

##### 匿名字段是语法糖, 实际就是一个和类型同名(不含包名)的字段

##### 编译器从外向内逐级查找所有层次匿名字段

```go
type Resource struct {
    id int
}
type User struct {
    Resource
    name string 
}
type Manager struct {
    User
    title string
}

var m Manager
m.id = 1
m.name = "Jack"
m.title = "Administrator"
```

##### 外层同名字段会遮蔽 嵌入字段成员,此时需要使用显式字段名

```go
type Resource struct {
    id   int
    name string 
}
type Classify struct {
    id int
}
type User struct {
    Resource      // Resource.id   Classify.id 在同一层次
    Classify
    name string     // 遮蔽Resource.name
}

u := User{
    Resource{1, "people"},
    Classify{100},
    "Jack",
}

println(u.name)     // User.name: Jack
println(u.Resource.name)    // people
// println(u.id)      // Error: ambiguous selector u.id
println(u.Classify.id)   // 100
```


##### 不能同时嵌入某一 类型 和其指针类型，因为它们名字相同


### 4.4.2 面向对象

##### go 没有 class 关键字, 没有继承，没有多态

##### go 仅支持封装，尽管匿名自断的内存布局和行为类似继承

