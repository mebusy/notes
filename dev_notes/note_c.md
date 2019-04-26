
# c 笔记

## 函数

默认全局可见，static 文件范围可见

返回值不能是 数组或函数，但可以是指向数组或函数的指针。

## 声明，定义

一处定义，到处声明

声明读法

 1. 从name 开始，
 2. 包在name外面的括号，
 3. 函数后缀(function returning)，数组后缀(array of)，
 4. 前缀指针(pointer to)

声明难读, typedef 是个好帮手

## compile

`-Wx` ，x is compile phase

动态链接：链接器 将库文件名或路径名放入可执行文件

## app 内存使用

unwrapped，text，data，bss，heap, stack  ( from low addr -> high addr )

用户进程 有页面交换，磁盘有 swap area

读取数据，“行”被带入缓存

Bus：atomic data数据项只能存放在 其大小倍数的地址处。而且肯定在单个缓存行中，或单个页面中。

## 数组

只有数组是引用传递（转成指针), 函数内无法知道外部究竟是什么形式调用的

## struct

struct tag: 以后声明可以不用 写完整 `struct {...}`

array in struct：你可以认为这个array是 first class type了：1.通过赋值copy 2.值传递参数 3. 通过函数返回

struct 是实现各种动态数据结构的关键，如 node of tree

内存对齐：成员起始地址，最大成员长度

## const 

紧挨着type，限定type；否则限定指针

## typedef

`typedef TYPE alias`

alias 可以存在于 TYPE 中.


## don't

不要 用一个 signed 和 unsigned 比较


