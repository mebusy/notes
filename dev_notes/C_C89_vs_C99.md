...menustart

 - [C89 和 C99 比较](#450405f98e9635439bbd6010923b4cad)
     - [1. 增加restrict指针](#f1d0fcec526877132177ac75b396e81c)
     - [2. inline（内联）关键字](#869dfd943e003f9d2ff0ba3f8219cb44)
     - [3. 新增数据类型　](#1d37ba5f1f550c082a50668f180d2273)
     - [4. 对数组的增强](#6b05da7de175665bd05994af316b9dc6)
     - [5. 单行注释](#b8f1477527727ecba89b32e093a29d65)
     - [6. 分散代码与声明](#d1dda3c5ac49594d19e6428e5ae285a0)
     - [7. 预处理程序的修改](#ba50340ac28ebac0d8323aa248af26ef)
     - [8. for语句内的变量声明](#41c0bfd2ea5f3724a2e77b8bafce5043)
     - [9. 复合赋值](#e819e085f13ea2a58efadd5ab4e8e55c)
     - [10. 柔性数组结构成员](#d2b31a7213fc43f7fb1d6870db3d732c)
     - [11. 指定的初始化符](#ccf00ae77f6a9bf6d2ef4651243d7e02)
     - [12. printf()和scanf()函数系列的增强](#e36cc81e560fd58e8e6cb48fdc3d8879)
     - [13. C99新增的库](#828b2be559c7ab56d297a88861254564)
     - [14. __func__预定义标识符](#1c4bef5ec3a05ee3d6ab3b84c8e895b5)
     - [15. 其它特性的改动](#dba30adb295b494114aa9d4c8d1345e5)

...menuend


<h2 id="450405f98e9635439bbd6010923b4cad"></h2>


## C89 和 C99 比较


- GCC支持C99, 通过 --std=c99 命令行参数开启
    - `gcc --std=c99 test.c`
- FFMPEG使用的是C99。而VC支持的是C89（不支持C99）。因此VC一般情况下是无法编译FFMPEG的源代码的。 

---

<h2 id="f1d0fcec526877132177ac75b396e81c"></h2>


### 1. 增加restrict指针

- C89中 `void *memcpy (void *s1, const void *s2, size_t size);` 如果s1和s2所指向的对象重叠， 其操作就是未定义的。 
- C99中memcpy()函数原型如下： `void *memcpy(void *restrict s1, const void *restrict s2,size_t size);`　　通过使用restrict 修饰s1和s2变元，可确保它们在该原型中指向不同的对象。

<h2 id="869dfd943e003f9d2ff0ba3f8219cb44"></h2>


### 2. inline（内联）关键字

- C89，并没有inline。C++语言先引入了这个关键字，后来的C语言标准，如C99，将其借鉴了进来。 在inline关键字进入C语言标准之前，很多C编译器，例如GCC，已经把它作为一项编译器扩展支持了。但问题是，这些编译器扩展中inline关键字的意义与后来的C99标准并不一致。这就导致了代码兼容性的问题。
- [C/C++中的inline关键字](http://blog.shengbin.me/posts/inline-keyword-in-c-c++/)

<h2 id="1d37ba5f1f550c082a50668f180d2273"></h2>


### 3. 新增数据类型　

- _Bool　 值是0或1 
    - 用来定义bool、true以及false宏的头文件夹`<stdbool.h>`，以便程序
员能够编写同时兼容于C与C++的应用程序。
- 复数类型_Complex and _Imaginary   
    - `<complex.h>`
- long long int
    - long long int能够支持的整数长度为64位。 

<h2 id="6b05da7de175665bd05994af316b9dc6"></h2>


### 4. 对数组的增强

- 可变长数组 

<h2 id="b8f1477527727ecba89b32e093a29d65"></h2>


### 5. 单行注释

- 引入了单行注释标记 "//" , 可以象C++一样使用这种注释了。

<h2 id="d1dda3c5ac49594d19e6428e5ae285a0"></h2>


### 6. 分散代码与声明

<h2 id="ba50340ac28ebac0d8323aa248af26ef"></h2>


### 7. 预处理程序的修改

- 变元列表
    - 宏可以带变元，在宏定义中用省略号（...）表示。内部预处理标识符__VA_ARGS__决定变元将在何处得到替换。
    - 例：`#define MySum(...) sum(__VA_ARGS__)` 语句MySum(k,m,n); 将被转换成：sum(k, m, n);
    - 例： `#define compare(compf, ...) compf(__VA_ARGS__)` 其中的compare(strcmp,"small", "large"); 将替换成：strcmp("small","large");
- _Pragma运算符  `_Pragma("directive") `
    - 其中directive是要满打满算的编译指令。_Pragma运算符允许编译指令参与宏替换。
- 内部编译指令
    - STDCFP_CONTRACT ON/OFF/DEFAULT 若为ON，浮点表达式被当做基于硬件方式处理的独立单元。默认值是定义的工具。
    -  STDCFEVN_ACCESS ON/OFF/DEFAULT 告诉编译程序可以访问浮点环境。默认值是定义的工具。 
    -  STDC CX_LIMITED_RANGE ON/OFF/DEFAULT 若值为ON，相当于告诉编译程序某程序某些含有复数的公式是可靠的。默认是OFF。
- 新增的内部宏
    - __STDC_HOSTED__ 若操作系统存在，则为1
    - __STDC_VERSION__ 199991L或更高。代表C的版本
    - __STDC_IEC_599__ 若支持IEC 60559浮点运算，则为1
    - __STDC_IEC_599_COMPLEX__ 若支持IEC 60599复数运算，则为1
    - __STDC_ISO_10646__ 由编译程序支持，用于说明ISO/IEC 10646标准的年和月格式：yyymmmL

<h2 id="41c0bfd2ea5f3724a2e77b8bafce5043"></h2>


### 8. for语句内的变量声明

- C99中，程序员可以在for语句的初始化部分定义一个或多个变量，这些变量的作用域仅于本for语句所控制的循环体内。比如： `for(int i=0; i<10; i++){`

<h2 id="e819e085f13ea2a58efadd5ab4e8e55c"></h2>


### 9. 复合赋值

- `double *fp = (double[]) {1.1, 2.2, 3.3};`
- 在文件域内建立的复合赋值只在程序的整个生存期内有效。在模块内建立的复合赋值是局部对象，在退出模块后不再存在。

<h2 id="d2b31a7213fc43f7fb1d6870db3d732c"></h2>


### 10. 柔性数组结构成员

- C99中，结构中的最后一个元素允许是未知大小的数组，这就叫做柔性数组成员
- 但结构中的柔性数组成员前面必须至少一个其他成员。
- 柔性数组成员允许结构中包含一个大小可变的数组
- sizeof返回的这种结构大小不包括柔性数组的内存。
- 包含柔性数组成员的结构用malloc()函数进行内存的动态分配，并且分配的内存应该大于结构的大小，以适应柔性数组的预期大小。

<h2 id="ccf00ae77f6a9bf6d2ef4651243d7e02"></h2>


### 11. 指定的初始化符

- C99中，该特性对经常使用稀疏数组的程序员十分有用。
- 例如: `int x[10] = {[0] = 10, [5] = 30};`
- 例如: `struct example{ int k, m, n; } object = {m = 10,n = 200}; `

<h2 id="e36cc81e560fd58e8e6cb48fdc3d8879"></h2>


### 12. printf()和scanf()函数系列的增强

- 引进了处理long long int和unsigned long long int数据类型的特性。
- long long int 类型的格式修饰符是ll。ll适用于d, i, o, u 和x格式说明符
- 还引进了hh修饰符。当使用d, i, o, u和x格式说明符时，hh用于指定char型变元。
- ll和hh修饰符均可以用于n说明符。
- 格式修饰符a和A用在printf()函数中时，结果将会输出十六进制的浮点数。
    - `格式如下：[-]0xh, hhhhp + d` 使用A格式修饰符时，x和p必须是大写。`
- A和a格式修饰符也可以用在scanf()函数中，用于读取浮点数。

<h2 id="828b2be559c7ab56d297a88861254564"></h2>


### 13. C99新增的库

- C89 标准的头文件
    - `<assert.h>` 定义宏assert()
    - `<ctype.h>` 字符处理
    - `<errno.h>` 错误报告
    - `<float.h>` 定义与实现相关的浮点数
    - `<limits.h>` 定义与实现相关的各种极限值
    - `<locale.h>` 支持函数setlocale()
    - `<math.h>` 数学函数库使用的各种定义
    - `<setjmp.h>` 支持非局部跳转
    - `<signal.h>` 定义信号值
    - `<stdarg.h>` 支持可变长度的变元列表
    - `<stddef.h>` 定义常用常数
    - `<stdio.h>` 支持文件输入和输出
    - `<stdlib.h>` 其他各种声明
    - `<string.h>` 支持串函数
    - `<time.h>` 支持系统时间函数
- C99 新增的头文件和库
    - `<complex.h>` 支持复数算法
    - `<fenv.h>` 给出对浮点状态标记和浮点环境的其他方面的访问
    - `<inttypes.h>` 定义标准的、可移植的整型类型集合。也支持处理最大宽度整数的函数（常见）
    - `<iso646.h>` 首先在此1995年第一次修订时引进，用于定义对应各种运算符的宏
    - `<stdbool.h>` 支持布尔数据类型类型。定义宏bool，以便兼容于C++
    - `<stdint.h>` 定义标准的、可移植的整型类型集合。该文件包含在`<inttypes.h>`中（常见）
    - `<tgmath.h>` 定义一般类型的浮点宏
    - `<wchar.h>` 首先在1995年第一次修订时引进，用于支持多字节和宽字节函数
    - `<wctype.h>` 首先在1995年第一次修订时引进，用于支持多字节和宽字节分类函数 

<h2 id="1c4bef5ec3a05ee3d6ab3b84c8e895b5"></h2>


### 14. __func__预定义标识符

- 用于指出__func__所存放的函数名，类似于字符串赋值。

<h2 id="dba30adb295b494114aa9d4c8d1345e5"></h2>


### 15. 其它特性的改动

- 不再支持隐含式的int规则
- 删除了隐含式函数声明
- 对返回值的约束
    - C99中,非空类型函数必须使用带返回值的return语句. 
- 扩展的整数类型
    - int16_t 整数长度为精确16位
    - int_least16_t 整数长度为至少16位
    - int_fast32_t 最稳固的整数类型,其长度为至少32位
    - intmax_t 最大整数类型
    - uintmax_t 最大无符号整数类型
- 对整数类型提升规则的改进
    - C89中,表达式中类型为char,short int或int的值可以提升为int或unsigned int类型.
    - C99中,每种整数类型都有一个级别.例如:long long int 的级别高于int, int的级别高于char
    - 在表达式中,其级别低于int或unsigned int的任何整数类型均可被替换成int或unsigned int类型.
