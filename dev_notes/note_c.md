[](...menustart)

- [c 笔记](#eed06c033cde767faa02ef27643d337a)
    - [函数](#870a51ba2a9edfadc62ce99af52cabd1)
    - [声明，定义](#ce7fd94261a99ab0ff14f1d0fe507ffc)
    - [compile](#03638f60b1ca9b72e82ca23e29daf48c)
    - [app 内存使用](#c27d7133d76323625ad6705ae704cbd4)
    - [数组](#0e67d4b0e351b00f4bea9840aa6b99d7)
    - [struct](#0f8d6fb56fe6cdf55ad0114ec5b51dbb)
    - [const](#6680dba00f3a88f66f8029a93d71d93c)
    - [typedef](#87ea20565caee58f2e8ba1ef56426ff1)
    - [don't](#5970929a425637241abb7a44591e32b3)

[](...menuend)


<h2 id="eed06c033cde767faa02ef27643d337a"></h2>

# c 笔记

<h2 id="870a51ba2a9edfadc62ce99af52cabd1"></h2>

## 函数

默认全局可见，static 文件范围可见

返回值不能是 数组或函数，但可以是指向数组或函数的指针。

<h2 id="ce7fd94261a99ab0ff14f1d0fe507ffc"></h2>

## 声明，定义

一处定义，到处声明

声明读法

 1. 从name 开始，
 2. 包在name外面的括号，
 3. 函数后缀(function returning)，数组后缀(array of)，
 4. 前缀指针(pointer to)

声明难读, typedef 是个好帮手

<h2 id="03638f60b1ca9b72e82ca23e29daf48c"></h2>

## compile

`-Wx` ，x is compile phase

动态链接：链接器 将库文件名或路径名放入可执行文件

<h2 id="c27d7133d76323625ad6705ae704cbd4"></h2>

## app 内存使用

unwrapped，text，data，bss，heap, stack  ( from low addr -> high addr )

用户进程 有页面交换，磁盘有 swap area

读取数据，“行”被带入缓存

Bus：atomic data数据项只能存放在 其大小倍数的地址处。而且肯定在单个缓存行中，或单个页面中。

<h2 id="0e67d4b0e351b00f4bea9840aa6b99d7"></h2>

## 数组

只有数组是引用传递（转成指针), 函数内无法知道外部究竟是什么形式调用的

<h2 id="0f8d6fb56fe6cdf55ad0114ec5b51dbb"></h2>

## struct

struct tag: 以后声明可以不用 写完整 `struct {...}`

array in struct：你可以认为这个array是 first class type了：1.通过赋值copy 2.值传递参数 3. 通过函数返回

struct 是实现各种动态数据结构的关键，如 node of tree

内存对齐：成员起始地址，最大成员长度

<h2 id="6680dba00f3a88f66f8029a93d71d93c"></h2>

## const 

紧挨着type，限定type；否则限定指针

<h2 id="87ea20565caee58f2e8ba1ef56426ff1"></h2>

## typedef

`typedef TYPE alias`

alias 可以存在于 TYPE 中.


<h2 id="5970929a425637241abb7a44591e32b3"></h2>

## don't

不要 用一个 signed 和 unsigned 比较


