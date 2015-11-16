
    2.2 运算符
        表达式(Expressions)
            一元操作符
            二元操作符
            ^作为一元操作符是求反,作为2元操作符是异或，&^组合表示c中的&(~)
            ++ 和 –- 不再是表达式，而是语句. *p++是(*p)++，而不是*(p++)
    2.3 初始化
        初始化复合对象,必须使⽤用类型标签,且左⼤大括号必须在类型尾部。
        初始化值以 "," 分隔。可以多⾏,但最后一⾏必须以 "," 或 "}" 结尾。
    2.4 控制流
        2.4.1 if - else if - if
            支持初始化语句,可定义代码块局部变量
            不支持三元操作符 "a > b ? a : b"
        2.4.2 for
            常规循环 : for i, n := 0, len(s); i < n; i++ {
            替代while : for n > 0 {
            替代while(true) : for {
            在初始化语句中计算循环需要的数据是个好主意, 例如 计算长度
        2.4.3 Range 类似迭代器操作,返回 (索引, 值) 或 (键, 值)。
            for i := range s //忽略2nd value
            for _, c := range s { //忽略 1st value
            for range s { // 忽略返回值
            !!! 注意: range 会复制对象
        2.4.4 Switch
            分支表达式可以是任意类型，不限于常量
            自动 break
            使用 fallthrough 继续下一个分支，不再判断条件。
            可以省略条件表达式，当 if - else if - else 用
        2.4.5 Goto, Break, Continue
            配合标签，goto,break,continue可以在循环内跳转
            break 可用语 for, switch, select
            continue 只能用语 for 循环



## 2.2 运算符


#### 表达式(Expressions)

##### 一元操作符

& ! * + – ^  <- (channel) 

    PS.  ^作为一元操作符, 表示求反码, 同c里的 ~



##### 二元操作符

优先级  | 操作符   | 备注
------------- | ------------- | --------
5  |  \* / % << >> & &^ |  &^ 同c中的 &(~x)位清理
4  |  \+ – \| ^  |   ^ 作为2元表达式, 是异或(xor) 
3  |  == != < <= > >=  |    
2  |    &&      |
1  |    \|\|      |

##### ^作为一元操作符是求反,作为2元操作符是异或，&^组合表示c中的&(~)

##### ++ 和 –- 不再是表达式，而是语句. \*p++是(\*p)++，而不是\*(p++)  


## 2.3 初始化

#### 初始化复合对象,必须使⽤用类型标签,且左⼤大括号必须在类型尾部。

```go
var a = struct{ x int }{100}
var b = []int{1, 2, 3}
```

#### 初始化值以 "," 分隔。可以多⾏,但最后一⾏必须以 "," 或 "}" 结尾。

```python
a := []int{ 
    1,
    2,
}
```


## 2.4 控制流

#### 2.4.1 if - else if - if

##### 支持初始化语句,可定义代码块局部变量

```go
if n := "abc"; x > 0 {
```

##### 不支持三元操作符 "a > b ? a : b"

#### 2.4.2 for

支持三种循环⽅方式,包括类 while 语法

##### 常规循环 :     for i, n := 0, len(s); i < n; i++ {

##### 替代while :    for n > 0 {

##### 替代while(true) :   for {

##### 在初始化语句中计算循环需要的数据是个好主意, 例如 计算长度


#### 2.4.3 Range  类似迭代器操作,返回 (索引, 值) 或 (键, 值)。


类型| 1st value | 2nd value |备注
  ---|---|---|---
string|index|s[index]| unicode字符串2nd value是rune
array/slice|index|s[index]
map| key | m[key]
channel | element

##### for i := range s   //忽略2nd value
##### for _, c := range s {   //忽略 1st value
##### for range s {   // 忽略返回值

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


#### 2.4.4 Switch

##### 分支表达式可以是任意类型，不限于常量
##### 自动 break
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


#### 2.4.5 Goto, Break, Continue

##### 配合标签，goto,break,continue可以在循环内跳转
##### break 可用语 for, switch, select
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

