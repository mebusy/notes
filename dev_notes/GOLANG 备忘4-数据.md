[TOC]

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


    expressionslice |   len |   cap |   comment
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
