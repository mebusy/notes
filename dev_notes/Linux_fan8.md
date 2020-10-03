...menustart

- [8 我是Makefile](#0a90d03ec88e2482664b9f0c6adc6631)
    - [8.2 基本概念](#4fd59a44db61539acebb9e94ce703e21)
        - [8.2.2 目标,条件和命令](#3dae9c4e7839d0a98e1a387f3f23ce72)
        - [8.2.4 工作方式](#fe0198d3d2568f2848eb86c256650721)
        - [8.2.5 基本语法](#851458679c96a263b7e9f5a9711397c8)
    - [8.3 认识规则](#64006e68160fb1df531eaa4e9d761742)
        - [8.3.3 变量](#b293d527ac15c52b704e3092f19ec9f1)
        - [8.3.4 自动变量](#ddd6f066f49236d2d17892373783ee8c)
        - [8.3.5 模式规则](#595d9b4dd1f915c7739946b264de73eb)
        - [8.3.6](#76d2cd2a5eb29facccd351abf19ed9c8)
        - [8.3.7 路径搜索](#a3e7b516db12b7c28683b3fc203886a9)
    - [8.4 高级特性](#7de7f543f7a0c66294d52d50a98b3ae0)
        - [8.4.1 文件包含](#4c6350b1d43adf2fe7174cd52807b0d3)
        - [8.4.2 命令](#3dfdafa4f93d237dd6fe476a8d7f8f89)
        - [8.4.3 深入变量](#991e6e00c1a762dd68a627f167a0f5be)
        - [8.4.4 宏与函数](#f610a17c766cc26f3e522a720231fa04)
        - [8.4.5 条件指令](#2075f0bead1510a75d102054610f9300)
    - [8.5 Makefile 实战](#c2e93709eebc4d5d8f767a4238b01310)
        - [8.5.1 自动产生依赖](#d3ae68d2c064323c91eb51fb33bd572c)
        - [8.5.2 递归式的Makefile](#8a18c8cddb6ee0f3b48312efbf4c5e72)
        - [8.5.3 自动产生 Makefile  TODO(p343)](#e36936613671d9d20738638097658e56)
- [A brief introduction to Makefiles](#ce6a22fb23eb895b8097f56f735740a1)

...menuend


<h2 id="0a90d03ec88e2482664b9f0c6adc6631"></h2>


# 8 我是Makefile

- make
    - make 会一次查找 GNUmakefile, makefile, Makefile 
        - 也可以使用 -f 指定一个工作文件
    - `-d` 参数用于调试 Makefile

<h2 id="4fd59a44db61539acebb9e94ce703e21"></h2>


## 8.2 基本概念

<h2 id="3dae9c4e7839d0a98e1a387f3f23ce72"></h2>


### 8.2.2 目标,条件和命令

```
# 目标 : 条件
#    命令
all: TinyEdit   

TinyEdit: main.o line.o ...
    ...
main.o : main.c line.h buffer.h tedef.h
    cc -c -o main.o main.c    
```


- 目标可以作为参数，直接传给 make 
    - i.e. `make main.o`
    - 默认执行 make all

<h2 id="fe0198d3d2568f2848eb86c256650721"></h2>


### 8.2.4 工作方式

- 一个规模宏大的项目，比如 Linux 内核，源码文件数量数十万计，编译一次内核大概需要几十分钟甚至数小时
- 如果每做一点修改，都要编译这么久，那简直就是灾难
- make 解决这个问题的方法 就是哪个文件进行了修改 就只编译它
    - make 会依次把所有的目标，以及它们所对应的依赖， 进行时间戳(文件最后的修改时间)的对比。
    - 当发现某一个目标 比它的某些依赖的时间戳小的时候，就重新生成它。


<h2 id="851458679c96a263b7e9f5a9711397c8"></h2>


### 8.2.5 基本语法

- Makefile的基本语法是:

```
目标1 目标2 目标3 ... : 条件1 条件2 条件3 ...
    命令 1
    命令 2
    命令 3
    ...
```


- 至少一个目标
- 0个或 多个条件
    - 如果 没有给定条件， 只有 目标文件不存在时， 才会执行相应的命令去生成目标
- 每个命令 必须以 制表符 `Tab` 开头
    - 如果在非命令行上不慎输入了 Tab的话，它之后的内容多数情况下会被当作命令来解释
- 注释
    - `#` 开始的部分为注释
    - 不过切记 Tab的问题，  只要在 Tab后， 就会被作为命令解释， 包括 `#` 后面的内容
- Makefile 支持 折行 
    - 在行尾 使用 `\` 


<h2 id="64006e68160fb1df531eaa4e9d761742"></h2>


## 8.3 认识规则

<h2 id="b293d527ac15c52b704e3092f19ec9f1"></h2>


### 8.3.3 变量

- 现在需要给 生成的程序加入调试信息， 以便在发现bug的时候可以调试
    - 可以在每个 命令中加入 `-g` 选项。 只是这是一个馊主意
    - 有什么办法 是的只修改一个地方就能搞定一切呢，就是变量

```
CC := gcc -g
```

- make 在解析 `${CC} 或 $(CC)` 时，就会展开为 `gcc -g`

<h2 id="ddd6f066f49236d2d17892373783ee8c"></h2>


### 8.3.4 自动变量

- Makefile 中有一种特殊的变量， 不用定义，而且还会随着上下文的不同而发生改变，我们称之为 自动变量
- 最为常用的6个自动变量

---

变量名 | 作用
--- | ---
`$@` | 目标的文件名
`$<` | 第一个条件的文件名
`$?` | 时间戳在目标之后的所有条件, 并以空格 隔开这些条件
`$^` | 所有条件的文件名，空格隔开，并且 去了重
`$+` | 与  `$^` 类似，只是 没有去重
`$*` | 目标的主文件名， 不包含扩展名


- 自动变量只能用于 命令中

```
buffer.o : buffer.c buffer.h tools.h
    $(CC) $(CFLAGS) -o $@  $<   
main.o : main.c line.h buffer.h tedef.h
    # cc -c -o main.o main.c    
    $(CC) $(CFLAGS) -o $@  $<
```

<h2 id="595d9b4dd1f915c7739946b264de73eb"></h2>


### 8.3.5 模式规则

- 我们发现，上面的 buffer.o , main.o 的命令完全一样
    - 很自然的，我们就会想用同一的规则来处理它们 , 这就是 模式规则

```
all: TinyEdit

TinyEdit: main.o line.o buffer.o ...
    $(LD) $(LDFLAGS) $^ -o $@

myless : myless.o line.o buffer.o ...
    $(LD) $(LDFLAGS) $^ -o $@

%.o : %.c 
    $(CC) $(CFLAGS) -o $@  $<
```

- 模式中的 `%` 类似通配符， 它可以放在 模式中的任意位置，但是**它只能出现一次**
- 限制：
    - 模式规则中的目标与条件 为 一对一关系， 无法处理 一对多关系.

- 使用 `make -p` 可以查看 所有内置变量

---

- 虽然前面使用了 模式规则的Makefile 很精简，但是并不推荐，因为作为C语言的头文件 无法成为条件, 毕竟头文件修改了也需要重新编译.
- 后面会介绍一种 既使用模式规则， 又能照顾好依赖关系的方法...

<h2 id="76d2cd2a5eb29facccd351abf19ed9c8"></h2>


### 8.3.6

- 假目标可以给 Makefile 提供十分强大的功能。比如
    - 对源代码进行经历
    - 将生成的最终目标 安装到 合适的地方
    - 进行反安装
    - 对生成的目标进行测试
    - 给使用者提供帮助信息，等等
- 条件一定会是文件，但是目标就未必。
- 我们把 不生成目标文件的规则中的目标，就称为 假目标。
    - 因为没有文件生成， 所以假目标的命令就一定会执行
    - 不过有的时候 虽然定义了一个不会生成目标文件的规则， 但很难保证项目中不会有 与这个目标重名的文件存在
        - 一旦有这种情况发生，我们的假目标就不会工作了。 需要进行一下特殊的处理
    - 这个特殊的处理方式， 就是让 这个假目标 成为一个特殊目标 .PHONY 的条件。
        - 这样无论项目中是否有重名的文件，这个目标对对应的命令都会被执行。

```
all: TinyEdit
    .PHONY all install uninstall clean

install: TinyEdit myless
    cp ...
    cp ...

uninstall: 
    rm -f ...
    rm -f ...

clean:
    rm -f *.o 
    rm -f TinyEdit myless

...
```
    
<h2 id="a3e7b516db12b7c28683b3fc203886a9"></h2>


### 8.3.7 路径搜索

- 现在我将代码重新组织了一下，建立 src , include 子目录， 并将 所有 .c 文件移动到 src 中， 所有 .h 移动到 include中
    - 这样就需要 修改 Makefile 规则中的条件，添加子目录。 但是这样很麻烦，还很容易出错
    - 于是 Makefile 引入了 VPATH 和 vpath
- VPATH  的值 是需要 make 搜索的 子目录， 以空格分割

```
LDFLAGS := -lcurses
VPATH := src include
...
```


- 虽然VPATH 可以解决路径的问题，但是有一个限制:
    - 如果在多个路径中找到同名文件， 会采用第一个被找到了。 这种问题在 .h 文件中经常出现， 会很麻烦
    - 为此 就需要 vpath
    
- vpath 使用 模式来指定 在某个具体的路径中，搜索哪些类型的文件

```
vpath %.c src
vpath %.h include
```

<h2 id="7de7f543f7a0c66294d52d50a98b3ae0"></h2>


## 8.4 高级特性

<h2 id="4c6350b1d43adf2fe7174cd52807b0d3"></h2>


### 8.4.1 文件包含

- Makefile 使用 `include` 指令来 包含其他文件，功能有二
    1. 类似与C语言那样引入一个头文件，实现代码服用
    2. 用来自动产生依赖关系的信息
- `include FILE1 FILE2 FILE3`
    - include 可以引入任意多个文件，且支持 shell的通配符和变量
- 当make 遇到include 指令，
    - 就会读取 它指定的文件
    - 一旦遇到一个不存在的，不要紧， 顶多抱怨一句，继续来。知道将所有文件读完
    - 这时候 它就要收拾刚才找不到的文件了。 怎么收拾呢？
        - 就是将这些文件 作为规则的目标，尝试去生成它。 生成一个读进来一个。
        - 但凡有一个没搞定，make就马上报错罢工。
    - 等到都读完了，就开始常规工作了。
    - 这个时候，一旦根据某些规则，将 include所指定的某个文件更新了，也会导致这个文件被重新读入。
        - 因为我们可以将整个include 指令看作一个特殊的规则， 只是这个规则没有中间的 `:` , include 就是目标，它所指定的文件都是条件.
        - 这条规则的命令， 即使逐一读取每个条件所对应的文件，并与其所在的Makefile 进行融合。
- include 搜索路径
    - 最优先 当前工作路径
    - 执行make 命令时 给定的 `-I 或 --include-dir` 选项所知名的路径

<h2 id="3dfdafa4f93d237dd6fe476a8d7f8f89"></h2>


### 8.4.2 命令

- Makefile 的命令有一个限制， 就是只能 单行处理bash 脚本

```
for d in a b c
do 
    echo $d/*
done > list.txt

在Makefile中用,需要改写成合法的bash格式

for d in a b d ;  do echo $$d/* ; done > list.txt
```

- 注意对变量d的引用上， 采用的是 `$$d` , 这样写是为了区别于 Makefile 的变量.

- Makefile 命令修饰符
    - `@` : 不输出命令本身
    - `-` : 忽略命令错误
    - `+` : 只显示命令 ， 而不去执行 
        - 这个看起来用处不大， 不过在编写递归式的Makefile 时会用到


<h2 id="991e6e00c1a762dd68a627f167a0f5be"></h2>


### 8.4.3 深入变量

- 1. 经简单扩展的变量 
    -  `:=` 复制运算符来定义的变量
    - 下面 MAKE_DEPEND 的值可能是 `gcc -M` , 如果 CC 没定义，则是 ` -M`
        - 一经定义，就有固定的值

```
MAKE_DEPEND := $(CC) -M
```

- 2. 经递归扩展的变量
    - `=`  delayed expand
    - 下面 MAKE_DEPEND 的值 会根据 CC 的定义，动态变化

```
MAKE_DEPEND := $(CC) -M
```

---

- 其他的赋值方式
- `?=`  附带条件的变量赋值运算符
    - 如果左边的变量 之前没有被定义过， 才会赋值
    - 如果左边定义过，就跳过
- `+=` 追加赋值
    - 给变量追加东西，我们可以 `A := $(A) B` 
    - 但是如果是 递归扩展的变量呢？  `A = $(A) B` 
        - 左递归 无限循环
        - 所以需要 `+=` 来解决这个问题  `A += B`

---

- 直接我们所说的变量都是 全局变量
    - Makefile  也有它的 局部变量 -- 并不是我们印象中的局部变量 -- ， 叫 目标专属变量

```
# myless 需要链接 curses 库
# TinyEdit 不需要 curses 库

LDFLAGS  :=

TinyEdit: ...
    $(LD) $(LDFLAGS) $^ -o $@
myless : LDFLAGS := -lcurses
myless : ... 
    $(LD) $(LDFLAGS) $^ -o $@
```

- 目标专属变量的值， 在处理对应目标的规则时 会进行改动， 当离开这个规则之后，变量值会被恢复。
- 除了 我们这些自定义的变量和make内建的一些变量之外，make还提供了几个非常有用的专有变量

---


变量名 | 作用
--- | ---
MAKE_VERSION | GNU make 版本好
CURDIR |  make的当前工作路径
MAKEFILE_LIST | 在make命令中给定的要生成的目标
VARIABLES | 所有已定义的变量名列表， 不包含目标专有变量。 只读


<h2 id="f610a17c766cc26f3e522a720231fa04"></h2>


### 8.4.4 宏与函数

- 宏的概念与经递归扩展的变量基本上是一致的。 只是写法不同
- 宏定义的语法:
    - 只要将你的命令，写在 `...` 那里就行了 , 不过要注意命令的写法

```
define MACRO_NAME
    ...
endef
```

- 使用定义好的宏:
    - `$(MACRO_NAME)`  or `${MACRO_NAME}`
- 宏还可以引用参数:
    - 使用这样的自动变量 `$1, $2, $3 ... ` 
    - 使用:   `$(call MACRO_NAME [, arg1, ... , argn])`
        - i.e. `$(call get_files_list,a,b,c)`
- 其实 Makefile中已经内置很多非常有用的函数，不过调用方法与我们自定义的函数不一样, 语法是这样的:
    - `$(function arg1,[,argn])`
    - 明显比我们自定义的要简单。
    - 这是因为 Makefile本不打算支持自定义函数的，只是需求太多了，也就得支持了。
        - 它并没有采用与 内置函数 相一致的语法， 取而代之的是一个巧妙的方法。 
        - 就是 提供了一个名为 `call` 的内置函数。  用这个函数使用一些技巧来扩展宏
        - 而且 `call` 函数不只是对 宏起作用， 对变量同样有效。
- 无论是宏还是函数，都是有返回值的。
    - 这个返回值就是宏或函数命令的标准输出。


<h2 id="2075f0bead1510a75d102054610f9300"></h2>


### 8.4.5 条件指令

```
ifdef, ifndef, ifeq, ifneq
else
endif
```


<h2 id="c2e93709eebc4d5d8f767a4238b01310"></h2>


## 8.5 Makefile 实战

<h2 id="d3ae68d2c064323c91eb51fb33bd572c"></h2>


### 8.5.1 自动产生依赖

- 依赖关系始终是一个特别烦人的事情，尤其是 C的头文件。
    - 因为只要修改了头文件， 那么所有引用的 .c 文件都应该被重新编译。
- 要手动维护这些依赖关系 既麻烦又容易出错。
- 如果能够自动维护生成，那就真是轻松愉快了。
- make 和 gcc 通过 狼狈为奸 成就了这种可能。

---

- gcc 提供了一个 `-M` 和 `-MM` 的命令选项
    - 前者可以输出一个 .c 文件所引入的所有头文件
    - 后者则排除掉了 系统提供的头文件，只保留 用户自定义的头文件。
- 它的输出差不多是这样:
    - 很熟悉吧，这不就是 Makefilede 目标和条件吗？ 可见gcc  与make 的关系不一般了.

```
# gcc -MM Stack.cpp
Stack.o: Stack.cpp Stack.h UMCMacros.h HTTPRequest.h
```

- 一个例子

```
SOURCES := $(wildcard *.cpp)

all: Stack.o
>---@echo $(SOURCES) , $$$$

-include $(subst .cpp,.d,$(SOURCES))
%.d:%.cpp
>---gcc -MM $< > $@.$$$$; \
>---sed 's,\($*\)\.o[:]*,\1.o $@:,g' < $@.$$$$ > $@; \
>---rm -rf $@.$$$$
```

---

- \*  说明
- `SOURCES := $(wildcard *.cpp)`
    - 列出当前目录下所有的 cpp 文件
    - i.e. `RobotMgr.cpp RobotLogin.cpp Stack.cpp RobotGetUserData.cpp RobotChallenge.cpp HTTPRequest.cpp RobotBattle.cpp`
- `gcc -MM $< > $@.$$$$;`
    - 根据 cpp 生成 类似 .d.9203  文件，文件的内容类似: `Stack.o: Stack.cpp Stack.h UMCMacros.h HTTPRequest.h`
    - `$$` 是 bash 里的一个变量，表示 process ID (PID) of the script itself.
- sed 语句 是往 .d 文件中 插入 .d文件名本身 
    - `Stack.o Stack.d: Stack.cpp Stack.h UMCMacros.h HTTPRequest.h`
- 注意 模版规则 的命令 需要写在 一行
    - 多行的话，每一行 `$$` 生成的数字都会不一样
- `-include $(subst .cpp,.d,$(SOURCES))`
    - subst 是字符串替换 ,  将参数1的内容，替换为参数2, 替换目标是参数3 , 并将结果返回
        - 将 SOURCE 变量中的 .cpp 替换为 .d 
    - 这里 include 就相当于 要引入所有的 .d 文件。 如果找不到，就 执行最后的模式规则来生成 .d 文件。
        - 这样之前产生的那些 依赖关系(位于.d 文件中) 就被引入到这个 Makefile 中了.
- 为什么 确定依赖关系的规则中 有一个 .d 做目标 ?
    - 为了保证当有文件被修改的时候， 不会遗漏依赖关系变化。 
    - 比如 你在 一个.cpp 的头文件中 又引入了新的头文件. 这时依赖关系 需要更新， 但是我们确没有 .h -> .d 的模式规则。 加入.d 就可以解决这个问题。
- 新版本的 gcc 又配合这个设计，提供了一个新的 `-MT` 选项。 可以直接在 依赖关系中 加入 .d 文件


```
SOURCES := $(wildcard *.cpp)

all: Stack.o
>---@echo $(SOURCES) , $$$$

-include $(subst .cpp,.d,$(SOURCES))
%.d:%.cpp
>---gcc -MM -MT "$@ $(@:.d=.o)" $<   > $@
```

<h2 id="8a18c8cddb6ee0f3b48312efbf4c5e72"></h2>


### 8.5.2 递归式的Makefile

- Makefile 里 再调用make 去执行另一个 Makefile.
- 为什么要递归呢？ 动机很简单： 
    - 处理单一目录的Makefile 可以非常简单， 目录越多越复杂。
    - 给每个目录准备一个 Makefile, 可以很好的降低复杂度。

```
语法:

cd subdir && $(MAKE)
或
$(MAKE) -C subdir
```

- 这两条命令是等价的。 需要注意的两个地方
    1. 一个被执行的 Makefile 在执行完毕后， 不需要类似 `cd ..` 这样的命令， 因为每个命令都有一个独立的 shell 环境
    2. 永远使用 $(MAKE) 这样的变量来执行make, 这可以保证在一个系统中 安装了 多个版本make时， 使用的make就是你想要的
- Makefile的 caller 和 callee  之间你一定不希望完全没有联系。 
    - 我们可能需要传递 1 变量 ， 2 命令行参数
    - 但是 如果什么变量都传递 也会带来不小的麻烦， 所以也就有了下面的这些规则：

---

 1. 在命令行上赋值的变量 默认传递， 并且仍以命令行方式传递
 2. Makefile 中定义的变量 默认不传递
 3. 用 export 命令可以 明确传递一个变量
    - 和 bash 中的 export 不是一回事，不过用法一样
    - `export CC CFLAGS`
 4. unexport 明确不传递某个变量
 5. 底层 Makefile 对上层 Makefile 传递的变量进行的修改，不会传递回上层。


<h2 id="e36936613671d9d20738638097658e56"></h2>


### 8.5.3 自动产生 Makefile  TODO(p343)

- 大多数 Linux 上以源代码发行的软件都没有 Makefile, 但是却带有一个 configure 文件
    - 这是一个使用bash 脚本写成的程序， 它也是自动生成, configure 的作用就是生成Makefile文件
- configure 常用命令选项

---

 选项名 | 描述
--- | ---
`--prefix=PREFIX` | 指定安装路径，默认 `/usr/local`
`--exec-prefix=EPREFIX` | 指定默认的可执行程序安装路径，默认 PREFIX
`--bindir=DIR`  |  可执行程序安装路径，默认 EPREFIX/bin
`--libcdir=DIR` | 库文件安装路径， 默认的是 EPREFIX/lib
`--sysconfdir=DIR` | 配置文件安装路径， 默认 PREFIX/etc
`--includedir=DIR` | 需要安装的头文件路径， 默认 PREFIX/include
`--disable-FEATURE`  | 是否关闭某个特性， 等同于 `--enable-FEATURE=no`
`--enable-FEATURE=[ARG]MAKE_VERSION`  | 是否开启某个特性， ARG 是 yes 或 no 


- configure 还可以决定 生成软件时 使用什么养的 连接器，编译器，乃至编译器选项
    - 这是通过命令中 给定的环境变量实现的


 configure常用环境变量 | 描述
--- | ---
CC | C编译器
CFLAGS | C 编译器选项
LDFLAGS | 连接器选项
CPPFLAGS | c++编译器选项


- configure 它是怎么生成的呢？  它又是怎么生成 Makefile的呢？
    - 这里就要用到 Autotools 工具了.


<h2 id="ce6a22fb23eb895b8097f56f735740a1"></h2>


# A brief introduction to Makefiles

```makefile
all: output
output: input1 input2 input3
    command --output $@ --inputs $^
```

CMake will turn it into 

```makefile
all: output
output: input1 input2 input3
    command --output output --inputs input1 input2 input3
```





