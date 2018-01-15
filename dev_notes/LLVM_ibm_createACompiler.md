...menustart

 - [IBM 使用 LLVM 框架创建一个工作编译器](#b666897e006a61952325fc4ce09a90e1)
     - [开始使用 LLVM](#3517e6ec6ef43c16c3fe3f8d02d813e1)
     - [使用 LLVM 编写 Hello World](#25d77db5980b5942f3d851c8b1cbafdf)
     - [理解 LLVM IR](#3c5a78647c25d722ab8cf911ac977066)
     - [创建一个自定义的 LLVM IR 代码生成器](#83cce5d6924f021359b95495b7562605)
         - [针对 LLVM 代码的链接](#b641743f3841c4148588d0e72f4ae123)
         - [LLVM 模块和上下文环境等](#bb79068e1b02332c2220d3189bcccc59)

...menuend


<h2 id="b666897e006a61952325fc4ce09a90e1"></h2>

# IBM 使用 LLVM 框架创建一个工作编译器

<h2 id="3517e6ec6ef43c16c3fe3f8d02d813e1"></h2>

## 开始使用 LLVM

 - 可执行代码 生成流程
    - 中间代码 -> 汇编  -> 目标机器的 汇编器，连接器 -> 可执行代码
 - 常见的 gcc 在后台实际上也经历了这几个过程，可以通过 -v 参数查看它的编译细节。
    - 如果想看某个具体的编译过程，则可以分别使用 -E，-S，-c 和 -O，
    - 对应的后台工具则分别为 cpp，cc1，as，ld。
 - llvm
    - brew install llvm 后， 检查一下 xcode-select --install
    - llvm 5.0  release build 去掉 module->dump 的实现，只留下接口. 解决方法:
        - `brew edit llvm` 
        - add `-DLLVM_ENABLE_DUMP=ON`
        - add `brew reinstall --build-from-source llvm` 
            - force to recompile from source, not install from a pre-compiled binary 

 - LLVM 本身是一个虚拟机
    - llc 将 LLVM 字节代码转换成特定于平台的汇编代码
    - lli  可以直接执行字节代码。  lli 可以通过解释器或使用高级选项中的即时 (JIT) 编译器执行此工作。
 - llvm-gcc (clang) 可以使用 -S -emit-llvm 选项运行时会生成 LLVM 字节代码 .ll  
    - 然后您可以使用 lli 来执行这个已生成的字节代码（也称为 LLVM 汇编语言）。

<h2 id="25d77db5980b5942f3d851c8b1cbafdf"></h2>

## 使用 LLVM 编写 Hello World

 - 第一个程序

```cpp
// helloworld.cpp
#include <stdio.h>
int main( )
{ 
  printf("Hello World!\n");
}
```

```bash
$ clang helloworld.cpp -S -emit-llvm
$ ls
helloworld.cpp  helloworld.ll
$ lli helloworld.ll
Hello World!
```

<h2 id="3c5a78647c25d722ab8cf911ac977066"></h2>

## 理解 LLVM IR

 - 注释 ;
 - 标识符 `[%@][a-zA-Z$._][a-zA-Z$._0-9]*`
    - 全局标识符要以 @ 字符开始。所有的函数名和全局变量都必须以 @ 开始。
    - 局部标识符以百分号 (%) 开始
 - 整数类型定义为 iN ， N 是整数占用的字节数
 - 数组:  `[ <no. of elements> X <size of each element> ]`
    - i.e. "Hello World!"，可以使用类型 [13 x i8] , 12 characters + null
    - `@hello = constant [13 x i8] c"Hello World!\00"`
 - LLVM 允许您声明和定义函数
    - `define return_type @func_name() {  }`
 - 函数声明
    - `declare i32 @printf(i8*, ...) #1`
 - 每个函数均以返回语句结尾。
    - 有两种形式的返回语句：`ret <type> <value> 或 ret void`
    - 对于 i32 @main() 方法， 使用 ret i32 0 就足够了
 - 函数调用
    - 使用 `call <function return type> <function name> <optional function arguments>` 来调用函数
    - 注意，每个函数参数都必须放在其类型的前面
    - 返回一个 6 位的整数并接受一个 36 位的整数的函数测试的语法如下
    - `call i6 @test( i36 %arg1 )`
 

 - 第一次尝试创建手动编写的 Hello World 程序

```ll
// test.ll

declare  i32 @puts(i8*) 
@global_str = constant [13 x i8] c"Hello World!\00"
define i32 @main() { 
  call i32 @puts( [13 x i8] @global_str )
  ret i32 0 
}
```

```bash
$ lli test.ll
lli: test.ll:4:29: error: global variable reference must have pointer type
  call i32 @puts( [13 x i8] @global_str )
```

 - 因为 puts 期望提供一个指向 i8 的指针，但是这里传了一个 i8 数组

```ll
declare i32 @puts (i8*)
@global_str = constant [13 x i8] c"Hello World!\00"
 
define i32 @main() {
  %temp = getelementptr  [13 x i8], [13 x i8]* @global_str, i32 0, i32 0  
  call i32 @puts(i8* %temp)
  ret i32 0
}
```

<h2 id="83cce5d6924f021359b95495b7562605"></h2>

## 创建一个自定义的 LLVM IR 代码生成器

 - 了解 LLVM IR 是件好事，但是您需要一个自动化的代码生成系统，用它来转储 LLVM 汇编语言
 - LLVM 提供了强大的应用程序编程接口 (API) 支持
 - 在您的开发计算机上查找 LLVMContext.h 文件；如果该文件缺失，那么可能是您安装 LLVM 的方式出错。

 - 现在，让我们创建一个程序，为之前 的 Hello World 程序生成 LLVM IR。 

<h2 id="b641743f3841c4148588d0e72f4ae123"></h2>

### 针对 LLVM 代码的链接

 - llvm-config
    - llvm-config --cxxflags   获取需要传递至 g++ 的编译标志
    - llvm-config --ldflags     链接器选项
    - llvm-config --libs engine bcreader scalaropts

```bash
$ llvm-config --cxxflags --ldflags --libs
-I/usr/local/Cellar/llvm/5.0.1/include  -stdlib=libc++ -fPIC -fvisibility-inlines-hidden -Werror=date-time -std=c++11 -Wall -W -Wno-unused-parameter -Wwrite-strings -Wcast-qual -Wmissing-field-initializers -pedantic -Wno-long-long -Wcovered-switch-default -Wnon-virtual-dtor -Wdelete-non-virtual-dtor ...
```

<h2 id="bb79068e1b02332c2220d3189bcccc59"></h2>

### LLVM 模块和上下文环境等

 - LLVM 模块类是其他所有 LLVM IR 对象的顶级容器
 - LLVM 模块类能够包含 全局变量、函数、该模块所依赖的其他模块 和符号表等对象的列表
 - 要构建您的程序，必须从创建 LLVM 模块开始。
 - LLVM 模块的构造函数：
    - `explicit Module(StringRef ModuleID, LLVMContext& C);`
 - 第一个参数是该模块的名称，可以是任何虚拟的字符串。
 - 第二个参数称为 LLVMContext
    - 该类在多线程的上下文环境中变得非常重要，您可能想为每个线程创建一个本地上下文环境，并且想让每个线程完全独立于其他上下文环境运行。
    - 目前，使用这个默认的全局上下文来处理 LLVM 所提供的代码。

```cpp
llvm::LLVMContext& context = llvm::getGlobalContext();
llvm::Module* module = new llvm::Module("top", context);
```

 - 您要了解的下一个重要类是能实际提供 API 来创建 LLVM 指令并将这些指令插入基础块的类：
    - `IRBuilder` 类。
 - IRBuilder 提供了许多华而不实的方法，但是我选择了最简单的可行方法来构建一个 LLVM 指令，即使用以下代码来传递全局上下文：

```cpp
llvm::LLVMContext& context = llvm::getGlobalContext();
llvm::Module* module = new llvm::Module("top", context);
llvm::IRBuilder<> builder(context);
```

 - 准备好 LLVM 对象模型后，就可以调用模块的 dump 方法来 打印内容。
 - 创建一个转储模块

```cpp
// firstLLVM.cpp

```

```bash
$ clang++ `llvm-config --cxxflags --ldflags --libs` firstLLVM.cpp

```


