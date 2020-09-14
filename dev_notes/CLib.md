...menustart

- [理清gcc、libc、libstdc++的关系](#441e557a97e06dfaa2e6aeb7e6bfe8f7)
    - [libc](#e5823ba08cf6f8acc6662017ec572078)
    - [glibc](#0ded6244fb02e7fb8db8e873d25656c5)
    - [eglibc](#d99c3fe41c18c77615321392436de25b)
    - [glib](#380e406ab5ba1b6659ea00c4513cfc13)
    - [libc++/libstdc++](#c5cd131cf241c09f42050abdfc0fe15c)
    - [libstdc++，glibc的关系](#4769de7975850859f943d6ec1e83df57)
    - [g++是做什么的?](#e91bd64c7c0b2d24fbed4ed80f3d42f8)

...menuend


<h2 id="441e557a97e06dfaa2e6aeb7e6bfe8f7"></h2>


# 理清gcc、libc、libstdc++的关系

<h2 id="e5823ba08cf6f8acc6662017ec572078"></h2>


## libc

- libc是Linux下原来的标准C库，也就是当初写hello world时包含的头文件`#include <stdio.h>` 定义的地方。
- 后来逐渐被glibc取代，也就是传说中的GNU C Library
- 主流的一些linux操作系统如 Debian, Ubuntu，Redhat等用的都是glibc（或者其变种，下面会说到).

<h2 id="0ded6244fb02e7fb8db8e873d25656c5"></h2>


## glibc

- glibc是Linux系统中最底层的API，几乎其它任何的运行库都要依赖glibc
- glibc最主要的功能就是对系统调用的封装
- 除了封装系统调用，glibc自身也提供了一些上层应用函数必要的功能,如string,malloc,stdlib,linuxthreads,locale,signal等等。

<h2 id="d99c3fe41c18c77615321392436de25b"></h2>


## eglibc

- 就是前面说到的变种glibc
- e是Embedded的意思 
- eglibc的主要特性是为了更好的支持嵌入式架构，可以支持不同的shell(包括嵌入式)，但它是二进制兼容glibc的，就是说如果你的代码之前依赖eglibc库，那么换成glibc后也不需要重新编译。
- ubuntu系统用的就是eglibc

<h2 id="380e406ab5ba1b6659ea00c4513cfc13"></h2>


## glib

- glib跟glibc 并没有关系
- glib也是个c程序库，不过比较轻量级
- glib将C语言中的数据类型统一封装成自己的数据类型，提供了C语言常用的数据结构的定义以及处理函数，有趣的宏以及可移植的封装等
    - (注：glib是可移植的，说明你可以在linux下，也可以在windows下使用它）

<h2 id="c5cd131cf241c09f42050abdfc0fe15c"></h2>


## libc++/libstdc++

- 如果你写的是C++代码，这两个库也要非常重视
- 两个都是C++标准库
- libc++是针对clang编译器特别重写的C++标准库
- libstdc++自然就是gcc的事儿了 
- libstdc++与gcc的关系就像clang与libc++

<h2 id="4769de7975850859f943d6ec1e83df57"></h2>


## libstdc++，glibc的关系

- libstdc++与gcc是捆绑在一起的，也就是说安装gcc的时候会把libstdc++装上。 
- 那为什么glibc和gcc没有捆绑在一起呢？
- 相比glibc，libstdc++虽然提供了c++程序的标准库，但它并不与内核打交道。对于系统级别的事件，libstdc++首先是会与glibc交互，才能和内核通信。
- 相比glibc来说，libstdc++就显得没那么基础了。
 
<h2 id="e91bd64c7c0b2d24fbed4ed80f3d42f8"></h2>


## g++是做什么的? 

- 不要以为gcc只能编译C代码，g++只能编译c++代码
- 后缀为.c的
    - gcc把它当作是C程序
    - g++当作是c++程序；
- 后缀为.cpp的
    - 两者都会认为是c++程序 
- 编译
    - 在编译阶段，g++会调用gcc,对于c++代码，两者是等价的
- 链接
    - gcc命令不能自动和C++程序使用的库链接
        - 需要这样，`gcc -lstdc++`
        - 如果你的Makefile文件并没有手动加上libstdc++库，一般就会提示错误，要求你安装g++编译器了
    - g++ 能自动链接库



