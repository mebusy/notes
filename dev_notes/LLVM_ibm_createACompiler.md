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

    - ~~llvm 5.0  release build 去掉 module->dump 的实现，只留下接口. 解决方法:~~
        - ~~`brew edit llvm`~~
        - ~~add `-DLLVM_ENABLE_DUMP=ON`~~
        - ~~add `brew reinstall --build-from-source llvm`~~ 
            - ~~force to recompile from source, not install from a pre-compiled binary~~

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
#include "llvm/IR/LLVMContext.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/Support/raw_ostream.h"

int main()
{
  llvm::LLVMContext context;
  llvm::Module* module = new llvm::Module("top", context);
  llvm::IRBuilder<> builder(context); 
 
  // module->dump( );
  module->print( llvm::errs() , nullptr ) ;
  
  return 0; 
}
```

 - maxosx 上要加上 `--system-libs`

```bash
$ clang++  `llvm-config --cxxflags --ldflags --libs --system-libs ` firstLLVM.cpp 
$ ./a.out
; ModuleID = 'top'
source_filename = "top"
```

 - 然后，您需要创建 main 方法
 - LLVM 提供了 llvm::Function 类来创建一个函数，并提供了 llvm::FunctionType 将该函数与某个返回类型相关联。
 - 将 main 方法添加至顶部模块

```cpp
    ...
    llvm::FunctionType *funcType =
        llvm::FunctionType::get(builder.getInt32Ty(), false);
    llvm::Function *mainFunc =
        llvm::Function::Create(funcType, llvm::Function::ExternalLinkage, "main", module);
    module->print( llvm::errs() , nullptr ) ; 
```

```bash
$ ./a.out
; ModuleID = 'top'
source_filename = "top"

declare i32 @main()
```

 - 您还尚未定义 main 要执行的指令集。 所以main被认为是 declare
 - 为此，您必须定义一个基础块并将其与 main 方法关联。
 - 基础块 是 LLVM IR 中的一个指令集合，拥有将标签（类似于 C 标签）定义为其构造函数的一部分的选项
 - builder.setInsertPoint 会告知 LLVM 引擎接下来将指令插入何处
 - 向 main 添加一个基础块

```cpp
    ... 
    llvm::BasicBlock *entry = llvm::BasicBlock::Create(context, "entrypoint", mainFunc);
    builder.SetInsertPoint(entry);
    module->print( llvm::errs() , nullptr ) ;
```

```bash
$ ./a.out
; ModuleID = 'top'
source_filename = "top"

define i32 @main() {
entrypoint:
}
```

 - 现在已经定义了 main 的基础块，所以 LLVM 将 main 看作为是一个方法定义，而不是一个声明。
 - 现在，向代码添加全局 hello-world 字符串

```cpp
llvm::Value *helloWorld = builder.CreateGlobalStringPtr("hello world!\n");
```

```bash
$ ./a.out
; ModuleID = 'top'
source_filename = "top"

@0 = private unnamed_addr constant [14 x i8] c"hello world!\0A\00"

define i32 @main() {
entrypoint:
}
```

 - 现在您需要做的就是声明 puts 方法，并且调用它。
 - 要声明 puts 方法，则必须创建合适的 FunctionType\*.
 - 声明 puts 方法:

```cpp
std::vector<llvm::Type *> putsArgs;
putsArgs.push_back(builder.getInt8Ty()->getPointerTo());
llvm::ArrayRef<llvm::Type*>  argsRef(putsArgs);

llvm::FunctionType *putsType = llvm::FunctionType::get(builder.getInt32Ty(), argsRef, false);
llvm::Constant *putsFunc = module->getOrInsertFunction("puts", putsType);
```

```bash
; ModuleID = 'top'
source_filename = "top"

@0 = private unnamed_addr constant [14 x i8] c"hello world!\0A\00"

define i32 @main() {
entrypoint:
}

declare i32 @puts(i8*)
```

 - 剩下要做的是调用 main 中的 puts 方法，并从 main 中返回。

```cpp
    builder.CreateCall(putsFunc, helloWorld);
    builder.CreateRetVoid();
```

---

# 使用 LLVM 框架创建有效的编译器，第 2 部分

 - 本文将介绍代码测试，即向生成的最终可执行的代码添加信息。

## LLVM pass

 - LLVM 以其提供的优化特性而著名。
 - 优化被实现为 pass
 - LLVM 为您提供了使用最少量的代码创建 utility pass 的功能。
    - 例如，如果不希望使用 “hello” 作为函数名称的开头，那么可以使用一个 utility pass  来实现这个目的。

## 了解 LLVM opt 工具

 - opt 命令是模块化的 LLVM 优化器和分析器
 - 一旦您的代码支持定制 pass , 您将使用 opt 把代码编译为一个共享库并对其进行加载 
 - opt 命令接受 LLVM IR（扩展名为 .ll）和 LLVM 位码格式（扩展名为 .bc），可以生成 LLVM IR 或位码格式的输出。
 - 下面展示了如何使用 opt 加载您的定制共享库：

```bash
$ opt –load=mycustom_pass.so –help –S  // untested
```

 - opt –help 会生成一个 LLVM 将要执行的阶段的细目清单


## 创建定制的 LLVM pass

 - 您需要 Pass.h 文件中声明的 LLVM pass
    - for brew llvm, `/usr/local/opt/llvm/include/llvm/Pass.h`
 - 各个pass的类型都从 Pass 中派生，也在该文件中进行了声明。pass类型包括：
    - BasicBlockPass 类。用于实现本地优化，优化通常每次针对一个基本块或指令运行
    - FunctionPass 类。用于全局优化，每次执行一个功能
    - ModulePass 类。用于执行任何非结构化的过程间优化
 - 由于您打算创建一个阶段，该阶段拒绝任何以 “Hello ” 开头的函数名，因此需要通过从 FunctionPass 派生来创建自己的阶段。
    - Pass.h 中FunctionPass 部分代码...

```cpp
class FunctionPass : public Pass {
    ...
  /// runOnFunction - Virtual method overriden by subclasses to do the
  /// per-function processing of the pass.
  ///
  virtual bool runOnFunction(Function &F) = 0;
  ...
};
```

 - 回到 runOnFunction 方法中的Function 类型。LVM 使用 Function 类封装了一个 C/C++ 函数的功能
 - 创建一个定制 LLVM pass

```cpp
// pass.cpp
#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include <iostream>

class TestClass : public llvm::FunctionPass {
public:
    virtual bool runOnFunction(llvm::Function &F) {
        llvm::StringRef r = F.getName();
        if ( r.startswith("hello")) {
            std::cout  << "Function name starts with hello\n";
        }
        return false;
    }
};

```

 - 这段代码溜掉了两个细节
    - FunctionPass 构造函数需要一个 char，用于在 LLVM 内部使用。
        - LLVM 使用 char 的地址，因此您可以使用任何内容对它进行初始化。
    - 您需要通过某种方式让 LLVM 系统理解您所创建的类是一个新阶段。
        - 这正是 RegisterPass LLVM 模板发挥作用的地方
        - 在 PassSupport.h 头文件中声明了 RegisterPass 模板；该文件包含在 Pass.h 中

 - 完整的代码:

```cpp
#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include <iostream>

class TestClass : public llvm::FunctionPass {
public:
    virtual bool runOnFunction(llvm::Function &F) {
        llvm::StringRef r = F.getName();
        if ( r.startswith("hello")) {
            std::cout  << "Function name starts with hello\n";
        }
        return false;
    }
    static char ID; // could be a global too
};

char TestClass::ID = 'a';
static llvm::RegisterPass<TestClass> global_("test_llvm", "test llvm", false, false);
```

 - RegisterPass 模板中的参数 template 是将要在命令行中与 opt 一起使用的阶段的名称
 - 您现在所需做的就是 在上面这段代码 之外， 创建一个共享库， 然后 运行 opt 来 加载该库。
    - 之后是使用 RegisterPass 注册的命令的名称 ( "test_llvm" in this case) 
    - 最后是一个位码文件，您的定制阶段将在该文件中与其他阶段一起运行.

```bash

```
