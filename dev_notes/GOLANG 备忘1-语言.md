[](...menustart)

- [1.1 变量](#8fbc175d60a5c9de4b3a0f7ac108f29b)
    - [多变量赋值时, 先扫描表达式,计算出所有相关值, 然后再从左到右依次赋值。](#3743f959d2c580efa869bfd9fc430a72)
    - [未使用的局部变量 会被编译器当做错误。可使用 "\_ = i" 来规避](#778d2797ed09783251016fbdb796c785)
- [1.2 常量](#b87257ff9d092da92c9880bdd52365ad)
    - [常量组中,如果不提供 类型和初始化值, 那么视作与上一个常量相同。](#34bf670019ccdd76134b064f0ea821fc)
    - [常量值还可以是 len、cap、unsafe.Sizeof 等编译期可确定结果的函数返回值](#d5378e4acfbc10d10116bb31107fe11b)
- [1.3 枚举](#af747dc4241b2ffee1b56cd712b20e35)
    - [关键字 iota 定义常量组中从 0 开始按 计数的 自增枚举值。](#cb7a8f084225d830d18f49a44720786f)
    - [同一行常量组中，可以有多个 iota,它们各自自增](#36e89a4379afe38a68470f5c1586aa4b)
    - [自定义枚举类型](#259c7fb47f2b676cb50d51ce5709cfbf)
- [1.4 基本类型](#0483e9765163d77a92313ac2f25659a7)
- [1.5 引用类型](#e607fa976dff12f265568440e58e7d5d)
    - [引用类型包括 slice、map 和 channel。](#830255f9fdec37463f7757256851ee61)
    - [new返回指针，make返回对象](#53ba22d755d44e8f059a651b76c097e7)
- [1.6 类型转换](#fd293f2181b0ffb55f80da69ff2fc14d)
    - [命名类型(见1.9)不支持隐式类型转换，必须显示转换](#19a08b3edcabf36dfb40c06e4921951a)
    - [不能将其他类型当 bool 值使用](#22f8f15a16a8d9133834963bc32e1793)
- [1.7 字符串](#f45d0a2a0f8415ccc9663c9934250c45)
    - [数据结构:](#2c8a6bb0da0655ef57c7f4a7d7c04a9e)
    - [字符串是 不可变值类型, 内部指针指向 UTF-8 字节数组。](#aed9cd2435d85190581083bf4fe4e016)
    - ["\`" 定义 不转义处理的 raw 字符串, 支持跨行](#e697fc0f511b592c802bdcc46f46ba94)
    - ["+" 跨行连接 两个 字符串](#d1fec79c79cb85efc5976f42368b6069)
    - [支持 slice 获取子串， 子串依然指向原字节数组,仅修改了指针和长度属性](#7bfde92759299d5b72d4ad2317e8e24b)
    - [单引号字符常量 'aaa' 表示 rune 类型 ( Unicode Code Point )](#90f188567a6c52aa41bf3676061db398)
    - [要修改字符串,可先将其转换成 \[\]rune 或 \[\]byte, 完成后再转换为 string](#ccb521ca513981599927b6810b21e861)
    - [byte ／ rune 方式遍历字符串](#5eb130bb12976effe61fb35ff118ce1b)
- [1.8 指针](#857d45164a3cbb81274fb49609198822)
    - [支持指针类型 \*T,指针的指针 \*\*T,以及包含包名前缀的 \*\<package\>.T](#15040a23c03bd2b797605ac1fcd0b764)
    - [可以在 unsafe.Pointer 和任意类型指针间进行转换](#70387375d9edb8e487dfb881e16265ab)
    - [指针不支持加减法, 但可将Pointer 转换成 uintptr,可变相实现指针运算。](#1ec74f7ca0f87b3463ec3d1847673fa2)
    - [go函数内返回局部变量指针 是安全的，编译器会根据需要将其分配在GC Heap上](#dcd6a7ce507ae8cd18821797704b2c97)
- [1.9 自定义类型](#9883f5dc5f990b9d926aff1d5c75cc60)
    - [go 类型分为 命名和未命名 两类。](#db3d104aae037c28465db9c90522ddde)
    - [具有相同声明的 未命名类型 被视为同一类型。](#3ec3036a69f373d7eecb499aa0752576)
    - [type 在全局 或函数内 定义新类型。](#440f5f15d6b11397e97175cdd5cc3adb)
    - [新类型不是原类型的别名, 除拥有相同数据存储结构外,它们之间没有任何关系](#434df8d5a94933f26bfb9f07825721c5)

[](...menuend)


<h2 id="8fbc175d60a5c9de4b3a0f7ac108f29b"></h2>

#1.1 变量

```go
var (
        a int
        b float32 
)
```

<h2 id="3743f959d2c580efa869bfd9fc430a72"></h2>

#### 多变量赋值时, 先扫描表达式,计算出所有相关值, 然后再从左到右依次赋值。

```go
data, i := [3]int{0, 1, 2}, 0
i, data[i] = 2, 100                // (i = 0) -> (i = 2), (data[0] = 10
```

<h2 id="778d2797ed09783251016fbdb796c785"></h2>

#### 未使用的局部变量 会被编译器当做错误。可使用 "\_ = i" 来规避

```go
var s string // 全局变量没问题。
func main() {
        i := 0 // Error: i declared and not used。
        ...
        _ = i
}
```

<h2 id="b87257ff9d092da92c9880bdd52365ad"></h2>

#1.2 常量

<h2 id="34bf670019ccdd76134b064f0ea821fc"></h2>

#### 常量组中,如果不提供 类型和初始化值, 那么视作与上一个常量相同。
<h2 id="d5378e4acfbc10d10116bb31107fe11b"></h2>

#### 常量值还可以是 len、cap、unsafe.Sizeof 等编译期可确定结果的函数返回值

```go
const (
    s   = "abc"
    x        // x = "abc"
    c   = unsafe.Sizeof(b)
)
```

<h2 id="af747dc4241b2ffee1b56cd712b20e35"></h2>

#1.3 枚举
<h2 id="cb7a8f084225d830d18f49a44720786f"></h2>

const 定义可以使用 iota 

```golang
package main

import "fmt"

const (
	// r 1: iota ignore comments line
	// r 2: the first constant must assign a right value
	// r 3: iota start from first line with value 0, and increment by 1
	a = iota // iota = 0 ,

	// r 1: iota ignore empty line
	_            // iota = 1 ,  r 1.1: _ is not empy line
	b = 2        // iota = 2
	c            // iota = 3, r4: if right value not provided, use the previous value (b)
	d = iota * 2 // iota = 4
)

// r5: iota is scoped to the constant block
const x = iota // iota = 0

func main() {
	fmt.Printf("c=%v\n", c) // c=2
	fmt.Printf("d=%v\n", d) // d=8
	fmt.Printf("x=%v\n", x) // x=0
}
```

<h2 id="259c7fb47f2b676cb50d51ce5709cfbf"></h2>

#### 自定义枚举类型

```python
type Color int
const (
    Black Color = iota
    Red
    Blue
)
```

<h2 id="0483e9765163d77a92313ac2f25659a7"></h2>

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

<h2 id="e607fa976dff12f265568440e58e7d5d"></h2>

#1.5 引用类型

<h2 id="830255f9fdec37463f7757256851ee61"></h2>

#### 引用类型包括 slice、map 和 channel。
<h2 id="53ba22d755d44e8f059a651b76c097e7"></h2>

#### new返回指针，make返回对象

内置函数new用于分配内存。其语法就是一个函数调用，以类型作为参数。

make 会被编译器翻译 成具体的创建函数,由其分配内存和初始化成员结构,返回对象,而非指指针。

```go
a := []int{0, 0, 0}   //表达式初始化
b := make([]int, 3)          //make 创建
c := new([]int)                  //new 创建 　, c[1] = 10 会报错

v := new(int)   // v的类型为*int
```

<h2 id="fd293f2181b0ffb55f80da69ff2fc14d"></h2>

#1.6 类型转换

<h2 id="19a08b3edcabf36dfb40c06e4921951a"></h2>

#### 命名类型(见1.9)不支持隐式类型转换，必须显示转换
<h2 id="22f8f15a16a8d9133834963bc32e1793"></h2>

#### 不能将其他类型当 bool 值使用

<h2 id="f45d0a2a0f8415ccc9663c9934250c45"></h2>

#1.7 字符串

<h2 id="2c8a6bb0da0655ef57c7f4a7d7c04a9e"></h2>

#### 数据结构:
```python
struct String {
        byte* str;
        intgo len; 
};
```

<h2 id="aed9cd2435d85190581083bf4fe4e016"></h2>

#### 字符串是 不可变值类型, 内部指针指向 UTF-8 字节数组。

索引号访问某字节,如 s[i]。

不能 获取字节元素指针,&s[i] 非法。

不可变类型, 无法修改字节数组

字节数组尾部不包含 NULL

<h2 id="e697fc0f511b592c802bdcc46f46ba94"></h2>

#### "\`" 定义 不转义处理的 raw 字符串, 支持跨行

```go
s := `a
b\r\n\x00
c`
```

<h2 id="d1fec79c79cb85efc5976f42368b6069"></h2>

#### "+" 跨行连接 两个 字符串

```go
s := "Hello, " +
     "World!"
```

<h2 id="7bfde92759299d5b72d4ad2317e8e24b"></h2>

#### 支持 slice 获取子串， 子串依然指向原字节数组,仅修改了指针和长度属性

```go
s1 := s[:5]
```

<h2 id="90f188567a6c52aa41bf3676061db398"></h2>

#### 单引号字符常量 'aaa' 表示 rune 类型 ( Unicode Code Point )

```python
    a:='我'
    b:="我"
    c:='a'
    fmt.Printf( "%T,%T,%T,%v,%v,%v", a,b,c ,a,b,c )
    // int32,string,int32,25105,我,97
```

<h2 id="ccb521ca513981599927b6810b21e861"></h2>

#### 要修改字符串,可先将其转换成 []rune 或 []byte, 完成后再转换为 string

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

<h2 id="5eb130bb12976effe61fb35ff118ce1b"></h2>

#### byte ／ rune 方式遍历字符串

通过索引下标 取得的是 byte

```
for _,v in range 遍历, v 是 rune
```

<h2 id="857d45164a3cbb81274fb49609198822"></h2>

#1.8 指针
<h2 id="15040a23c03bd2b797605ac1fcd0b764"></h2>

#### 支持指针类型 \*T,指针的指针 \*\*T,以及包含包名前缀的 \*\<package\>.T
<h2 id="70387375d9edb8e487dfb881e16265ab"></h2>

#### 可以在 unsafe.Pointer 和任意类型指针间进行转换

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

<h2 id="1ec74f7ca0f87b3463ec3d1847673fa2"></h2>

#### 指针不支持加减法, 但可将Pointer 转换成 uintptr,可变相实现指针运算。

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

> 注意:GC 把 uintptr 当成普通整数对象,它无法阻止"关联" 对象被回收。


<h2 id="dcd6a7ce507ae8cd18821797704b2c97"></h2>

#### go函数内返回局部变量指针 是安全的，编译器会根据需要将其分配在GC Heap上

```python
func test() *int {
    x := 100
    return &x //在堆上分配内存, 但在内联时,也可能直接分配在目标栈。 
}
```

<h2 id="9883f5dc5f990b9d926aff1d5c75cc60"></h2>

# 1.9 自定义类型

<h2 id="db3d104aae037c28465db9c90522ddde"></h2>

#### go 类型分为 命名和未命名 两类。

命名类型包括 bool、int、string 等,  

array、slice、map 等和 具体元素类型、 长度等 有关,属于未命名类型。

<h2 id="3ec3036a69f373d7eecb499aa0752576"></h2>

#### 具有相同声明的 未命名类型 被视为同一类型。

• 具有相同基类型的 指针。

• 具有相同元素类型和长度的 array。

• 具有相同元素类型的 slice。

• 具有相同键值类型的 map。

• 具有相同元素类型和传送方向的 channel。

• 具有相同字段序列 (字段名、类型、标签、顺序) 的匿名 struct。 

• 签名相同 (参数和返回值,不包括参数名称) 的 function。

• 方法集相同 ( 方法名、 方法签名相同,和次序无关) 的 interface


<h2 id="440f5f15d6b11397e97175cdd5cc3adb"></h2>

#### type 在全局 或函数内 定义新类型。

```python
func main() {
    type bigint int64
    var x bigint = 100
    println(x)  //100
}
```

<h2 id="434df8d5a94933f26bfb9f07825721c5"></h2>

#### 新类型不是原类型的别名, 除拥有相同数据存储结构外,它们之间没有任何关系

不会持有原类型任何信息。

未命名类型, 可以显式转换。

```python
x := 1234
var b bigint = bigint(x) // 必须显式转换,除 是常量。
var s myslice = []int{1, 2, 3} // 未命名类型,隐式转换。
```

