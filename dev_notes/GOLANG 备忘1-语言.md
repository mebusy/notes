
[markdown版本](https://www.zybuluo.com/qibinyi/note/216622)

#1.1 变量

```go
var (
        a int
        b float32 
)
```

### 多变量赋值时, 先扫描表达式,计算出所有相关值, 然后再从左到右依次赋值。

```go
data, i := [3]int{0, 1, 2}, 0
i, data[i] = 2, 100                // (i = 0) -> (i = 2), (data[0] = 10
```

### 未使用的局部变量 会被编译器当做错误。可使用 "_ = i" 来规避

```go
var s string // 全局变量没问题。
func main() {
        i := 0 // Error: i declared and not used。
        ...
        _ = i
}
```

#1.2 常量

### 常量组中,如果不提供 类型和初始化值, 那么视作与上一个常量相同。
### 常量值还可以是 len、cap、unsafe.Sizeof 等编译期可确定结果的函数返回值

```go
const (
    s   = "abc"
    x        // x = "abc"
    c   = unsafe.Sizeof(b)
)
```

#1.3 枚举
### 关键字 iota 定义常量组中从 0 开始按 计数的 自增枚举值。
### 同一行常量组中，可以有多个 iota,它们各自自增 

```go
const (
    _   = iota                  // iota = 0
    KB  int64=1<<(10*iota) MB   //iota=1
    GB                          // 与 KB 表达式相同,但 iota = 2
    TB
    A,B  =iota,iota<<10         // 4, 4<<10 
    C,D                         // 5, 5 << 10
    
)
```

### 自定义枚举类型

```python
type Color int
const (
    Black Color = iota
    Red
    Blue
)
```

#1.4 基本类型

```go
bool
byte
rune                  Unicode // \uFFFF、\U7FFFFFFF、\xFF
int, int8, 16, 32 ,64         // 071 (8进制), 0x1F(16进制), 1e9, math.MinInt16
uint , ...
float32, 64
complex64, 128
uintptr                指针， nil
array                   值类型
struct                  值类型
string                  utf8字符串
slice                   引用类型
map                     引用类型
channel                 引用类型
interface               接口
function                函数
```

#1.5 引用类型

### 引用类型包括 slice、map 和 channel。
### new返回指针，make返回对象

内置函数 new 计算类型,为其分配零值内存,返回指针
make 会被编译器翻译 成具体的创建函数,由其分配内存和初始化成员结构,返回对象,而非指指针。

```go
a := []int{0, 0, 0}   //表达式初始化
b := make([]int, 3)          //make 创建
c := new([]int)                  //new 创建 　, c[1] = 10 会报错
```

#1.6 类型转换

### 命名类型(见1.9)不支持隐式类型转换，必须显示转换
### 不能将其他类型当 bool 值使用

#1.7 字符串

### 数据结构:
```python
struct String {
        byte* str;
        intgo len; 
};
```

### 字符串是 不可变值类型, 内部指针指向 UTF-8 字节数组。

索引号访问某字节,如 s[i]。
不能 获取字节元素指针,&s[i] 非法。
不可变类型, 无法修改字节数组
字节数组尾部不包含 NULL

### "`" 定义 不转义处理的 raw 字符串, 支持跨行

```go
s := `a
b\r\n\x00
c`
```

### "+" 跨行连接 两个 字符串

```go
s := "Hello, " +
     "World!"
```

### 支持 slice 获取子串， 子串依然指向原字节数组,仅修改了指针和长度属性

```go
s1 := s[:5]
```

### 单引号字符常量 'aaa' 表示 rune 类型 ( Unicode Code Point )

```python
	a:='我'
	b:="我"
	c:='a'
	fmt.Printf( "%T,%T,%T,%v,%v,%v", a,b,c ,a,b,c )
	// int32,string,int32,25105,我,97
```

### 要修改字符串,可先将其转换成 []rune 或 []byte, 完成后再转换为 string

```python
    s := "abcd"
    bs := []byte(s)
    bs[1] = 'B'
    println(string(bs))     //aBcd
    u := "电脑"
    us := []rune(u)
    us[1] = '话'
    println(string(us))     //电话
```

### byte ／ rune 方式遍历字符串

通过索引下标 取得的是 byte
for _,v in range 遍历, v 是 rune

#1.8 指针

###可以在 unsafe.Pointer 和任意类型指针间进行转换

```python
func main() {
    x := 0x12345678
    p := unsafe.Pointer(&x)
    n := (*[4]byte)(p)
    for i := 0; i < len(n); i++ {
        fmt.Printf("%X ", n[i])     //78 56 34 12
    } 
}
```

###指针不支持加减法, 但可将Pointer 转换成 uintptr,可变相实现指针运算。
```python
func main() {
    d := struct {
        s string
        x   int
    }{"abc", 100}        
    p := uintptr(unsafe.Pointer(&d))        // *struct -> Pointer -> uintptr
    p += unsafe.Offsetof(d.x)               // uintptr + offset
        p2 := unsafe.Pointer(p)
    px := (*int)(p2)
    *px = 200
    fmt.Printf("%#v\n", d)   //输出: struct { s string; x int }{s:"abc", x:200}
}
```

    注意:GC 把 uintptr 当成普通整数对象,它 法阻  "关联" 对象被回收。


###go函数内返回局部变量指针 是安全的，编译器会根据需要将其分配在GC Heap上
```python
func test() *int {
    x := 100
    return &x //在堆上分配内存, 但在内联时,也可能直接分配在目标栈。 
}
```

#1.9自定义类型

### go 类型分为 命名和未命名 两类。

命名类型包括 bool、int、string 等,  
array、slice、map 等和 具体元素类型、 长度等 有关,属于未命名类型。

### 具有相同声明的 未命名类型 被视为同一类型。

• 具有相同基类型的 指针。
• 具有相同元素类型和长度的 array。
• 具有相同元素类型的 slice。
• 具有相同键值类型的 map。
• 具有相同元素类型和传送方向的 channel。
• 具有相同字段序列 (字段名、类型、标签、顺序) 的匿名 struct。 
• 签名相同 (参数和返回值,不包括参数名称) 的 function。
• 方法集相同 ( 方法名、 方法签名相同,和次序无关) 的 interface

### type 在全局 或函数内 定义新类型。

```python
func main() {
    type bigint int64
    var x bigint = 100
    println(x)  //100
}
```

###新类型不是原类型的别名, 除拥有相同数据存储结构外,它们之间没有任何关系

不会持有原类型任何信息。
未命名类型, 可以显式转换。

```python
x := 1234
var b bigint = bigint(x) // 必须显式转换,除 是常量。
var s myslice = []int{1, 2, 3} // 未命名类型,隐式转换。
```

