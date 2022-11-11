[](...menustart)

- [2.2 运算符](#d7e9882ce8a2f889bafef2117c8667bb)
    - [表达式(Expressions)](#0b979cb73203d216ffbb3993a2bf643f)
        - [一元操作符](#7484d50162059d14066232a8cbb86998)
        - [二元操作符](#1e202e667c0218b2f6330426d73cacfe)
        - [^作为一元操作符是求反,作为2元操作符是异或，&^组合表示c中的&(~)](#fdb85a456e7226704e307890b9446d95)
        - [++ 和 –- 不再是表达式，而是语句. \*p++是(\*p)++，而不是\*(p++)](#057af0322c05e59b76dd007c37a5c13a)
- [2.3 初始化](#c459b96bafbcc4a4c469f9f00042002f)
    - [初始化复合对象,必须使⽤用类型标签,且左⼤大括号必须在类型尾部。](#0bb24d12848bd64e2fb82543f4dcda37)
    - [初始化值以 "," 分隔。可以多⾏,但最后一⾏必须以 "," 或 "}" 结尾。](#97286d724de3e6165d46e43a4a18b418)
- [2.4 控制流](#b15b40e9d05cbe94fc6bd6896d9136af)
    - [2.4.1 if - else if - if](#b01fe2bf3fa1bed5b86531c4866e563c)
        - [支持初始化语句,可定义代码块局部变量](#36af91e25fc232048c212a5bbf29f2a2)
        - [不支持三元操作符 "a > b ? a : b"](#d1925d2e6cb2bfbc3a501ffcfc78c157)
    - [2.4.2 for](#8aa0bd95f0cc86fc223852c002086d3a)
        - [常规循环 :     for i, n := 0, len(s); i < n; i++ {](#ab9d52fb1c1bee70d8f67977a78e8bcd)
        - [替代while :    for n > 0 {](#ed71e3bbe6084ecde9488ed21a1e484e)
        - [替代while(true) :   for {](#b1e8d86321ac39495d2fc77b8dac0032)
        - [在初始化语句中计算循环需要的数据是个好主意, 例如 计算长度](#04018b8e76ce12d9a5023b19f56112ca)
    - [2.4.3 Range  类似迭代器操作,返回 (索引, 值) 或 (键, 值)。](#e0d816558ffc4792c8a509aeb5c7efae)
        - [for i := range s   //忽略2nd value](#3a96a4751afc70766cba116bca02846e)
        - [for _, c := range s {   //忽略 1st value](#23b556b705e9bd4aa86d27438755b39c)
        - [for range s {   // 忽略返回值](#d82c063d637c6fd4fcb8728c31c530b4)
        - [!!! 注意: range 会复制对象](#1c591819875c9b45c924efa13feab391)
    - [2.4.4 Switch](#c109c1c7301022ba813f68fc055e6b37)
        - [分支表达式可以是任意类型，不限于常量](#33d56261648203e4a47b5e3a0710efa1)
        - [自动 break](#1c6bced21bad0bd5e51e4f9f7b8b216e)
        - [使用 fallthrough 继续下一个分支，不再判断条件。](#df275fdaaff353cab275dd40a75ba8d7)
        - [可以省略条件表达式，当 if - else if - else 用](#d06346c8126a43e497f7a18453dd3038)
    - [2.4.5 Goto, Break, Continue](#c21a00ace187b3c94b1e068ef193beb4)
        - [配合标签，goto,break,continue可以在循环内跳转](#a8fa7070630271d391106a646fe3d925)
        - [break 可用语 for, switch, select](#49abfb509012d033ddc4d7e9b0ca88dc)
        - [continue 只能用语 for 循环](#2051956c6c43c8b5978310651ff760f3)

[](...menuend)


<h2 id="d7e9882ce8a2f889bafef2117c8667bb"></h2>

## 2.2 运算符


<h2 id="0b979cb73203d216ffbb3993a2bf643f"></h2>

#### 表达式(Expressions)

<h2 id="7484d50162059d14066232a8cbb86998"></h2>

##### 一元操作符

& ! * + – ^  <- (channel) 

    PS.  ^作为一元操作符, 表示求反码, 同c里的 ~



<h2 id="1e202e667c0218b2f6330426d73cacfe"></h2>

##### 二元操作符

优先级  | 操作符   | 备注
------------- | ------------- | --------
5  |  \* / % << >> & &^ |  &^ 同c中的 &(~x)位清理
4  |  \+ – \| ^  |   ^ 作为2元表达式, 是异或(xor) 
3  |  == != < <= > >=  |    
2  |    &&      |
1  |    \|\|      |

<h2 id="fdb85a456e7226704e307890b9446d95"></h2>

##### ^作为一元操作符是求反,作为2元操作符是异或，&^组合表示c中的&(~)

<h2 id="057af0322c05e59b76dd007c37a5c13a"></h2>

##### ++ 和 –- 不再是表达式，而是语句. \*p++是(\*p)++，而不是\*(p++)  


<h2 id="c459b96bafbcc4a4c469f9f00042002f"></h2>

## 2.3 初始化

<h2 id="0bb24d12848bd64e2fb82543f4dcda37"></h2>

#### 初始化复合对象,必须使⽤用类型标签,且左⼤大括号必须在类型尾部。

```go
var a = struct{ x int }{100}
var b = []int{1, 2, 3}
```

<h2 id="97286d724de3e6165d46e43a4a18b418"></h2>

#### 初始化值以 "," 分隔。可以多⾏,但最后一⾏必须以 "," 或 "}" 结尾。

```python
a := []int{ 
    1,
    2,
}
```


<h2 id="b15b40e9d05cbe94fc6bd6896d9136af"></h2>

## 2.4 控制流

<h2 id="b01fe2bf3fa1bed5b86531c4866e563c"></h2>

#### 2.4.1 if - else if - if

<h2 id="36af91e25fc232048c212a5bbf29f2a2"></h2>

##### 支持初始化语句,可定义代码块局部变量

```go
if n := "abc"; x > 0 {
```

<h2 id="d1925d2e6cb2bfbc3a501ffcfc78c157"></h2>

##### 不支持三元操作符 "a > b ? a : b"

<h2 id="8aa0bd95f0cc86fc223852c002086d3a"></h2>

#### 2.4.2 for

支持三种循环⽅方式,包括类 while 语法

<h2 id="ab9d52fb1c1bee70d8f67977a78e8bcd"></h2>

##### 常规循环 :     for i, n := 0, len(s); i < n; i++ {

<h2 id="ed71e3bbe6084ecde9488ed21a1e484e"></h2>

##### 替代while :    for n > 0 {

<h2 id="b1e8d86321ac39495d2fc77b8dac0032"></h2>

##### 替代while(true) :   for {

<h2 id="04018b8e76ce12d9a5023b19f56112ca"></h2>

##### 在初始化语句中计算循环需要的数据是个好主意, 例如 计算长度


<h2 id="e0d816558ffc4792c8a509aeb5c7efae"></h2>

#### 2.4.3 Range  类似迭代器操作,返回 (索引, 值) 或 (键, 值)。


类型| 1st value | 2nd value |备注
  ---|---|---|---
string|index|s[index]| unicode字符串2nd value是rune
array/slice|index|s[index]
map| key | m[key]
channel | element

<h2 id="3a96a4751afc70766cba116bca02846e"></h2>

##### for i := range s   //忽略2nd value
<h2 id="23b556b705e9bd4aa86d27438755b39c"></h2>

##### for _, c := range s {   //忽略 1st value
<h2 id="d82c063d637c6fd4fcb8728c31c530b4"></h2>

##### for range s {   // 忽略返回值

<h2 id="1c591819875c9b45c924efa13feab391"></h2>

##### !!! 注意: range 会复制对象

```go
a := [3]int{0, 1, 2}
for i, v := range a {
    // 因为a是值类型的数组
    // index, value 都从a的复制品中取出
    if i == 0 {
        a[1], a[2] = 999, 999 //修改a的值
        fmt.Println(a)  // [0, 999, 999]
    }
    a[i] = v + 100 // 用复制品中取出的v修改原数组
}
fmt.Println(a)   //[100, 101, 102]
```

    建议使用引用类型，其底层数据不会被复制。


<h2 id="c109c1c7301022ba813f68fc055e6b37"></h2>

#### 2.4.4 Switch

<h2 id="33d56261648203e4a47b5e3a0710efa1"></h2>

##### 分支表达式可以是任意类型，不限于常量
<h2 id="1c6bced21bad0bd5e51e4f9f7b8b216e"></h2>

##### 自动 break
<h2 id="df275fdaaff353cab275dd40a75ba8d7"></h2>

##### 使用 fallthrough 继续下一个分支，不再判断条件。

```go
x := []int{1, 2, 3}
i := 2
switch i {
    case x[1]:
        println("a")
        fallthrough
    case 1, 3:
        println("b")
    default:
        println("c")
}
```

<h2 id="d06346c8126a43e497f7a18453dd3038"></h2>

##### 可以省略条件表达式，当 if - else if - else 用

```go
switch {
    case x[1] > 0:
        println("a")
    case x[1] < 0:
        println("b")
    default:
        println("c")
}
switch i := x[2]; { 带初始化语句
    case i > 0:
        println("a")
    case i < 0:
        println("b")
    default:
        println("c")
}
```


<h2 id="c21a00ace187b3c94b1e068ef193beb4"></h2>

#### 2.4.5 Goto, Break, Continue

<h2 id="a8fa7070630271d391106a646fe3d925"></h2>

##### 配合标签，goto,break,continue可以在循环内跳转
<h2 id="49abfb509012d033ddc4d7e9b0ca88dc"></h2>

##### break 可用语 for, switch, select
<h2 id="2051956c6c43c8b5978310651ff760f3"></h2>

##### continue 只能用语 for 循环

```go
func main() {
L1:
    for x := 0; x < 3; x++ {
L2:
        for y := 0; y < 5; y++ {
            if y > 2 { continue L2 }
            if x > 1 { break L1 }
            print(x, ":", y, " ")
         }
        println()
    }
}
```

```go
x := 100
switch {
case x >= 0:
    if x == 0 { break }
    println(x)
}
```

