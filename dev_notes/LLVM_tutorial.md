...menustart

 - [LLVM Tutorial: Table of Contents](#b56cad0e202690071ef63f030c12fc18)
 - [Implementing a Language with LLVM](#5d92cbb1c83f3094343f6913b9a2aba1)
     - [1. Tutorial Introduction and the Lexer](#223a7ae77e03289fe4e7135306e273b5)
         - [1.2. The Basic Language](#8c3e7ff9f5a07b5ecc04dd9a7e7bba55)
         - [1.3. The Lexer](#8a9476222388ff60664b1598fe119cb6)
 - [llvm tools](#38d4148bfdd1ae5a9f94b2081008fa00)

...menuend


<h2 id="b56cad0e202690071ef63f030c12fc18"></h2>


# LLVM Tutorial: Table of Contents

<h2 id="5d92cbb1c83f3094343f6913b9a2aba1"></h2>


# Implementing a Language with LLVM

<h2 id="223a7ae77e03289fe4e7135306e273b5"></h2>


## 1. Tutorial Introduction and the Lexer

<h2 id="8c3e7ff9f5a07b5ecc04dd9a7e7bba55"></h2>


### 1.2. The Basic Language

Kaleidoscope is a procedural language that allows you to 

 - define functions, 
 - use conditionals, 
 - math, etc. 

Over the course of the tutorial, we’ll extend Kaleidoscope to support the 

 - if/then/else construct, 
 - a for loop, 
 - user defined operators, 
 - JIT compilation with a simple command line interface, etc.

Because we want to keep things simple, the only datatype in Kaleidoscope is a 64-bit floating point type (aka ‘double’ in C parlance). 

As such, all values are implicitly double precision and the language doesn’t require type declarations. This gives the language a very nice and simple syntax. For example, the following simple example computes Fibonacci numbers:


<h2 id="8a9476222388ff60664b1598fe119cb6"></h2>


### 1.3. The Lexer


---

<h2 id="38d4148bfdd1ae5a9f94b2081008fa00"></h2>


# llvm tools

install 

```
brew reinstall llvm --with-all-targets

brew info llvm 
```

查看 llc 支持的后端

```
llc --version
LLVM (http://llvm.org/):
  LLVM version 3.9.0
  Optimized build.
  Default target: x86_64-apple-darwin16.1.0
  Host CPU: sandybridge

  Registered Targets:
    amdgcn  - AMD GCN GPUs
    arm     - ARM
    armeb   - ARM (big endian)
    nvptx   - NVIDIA PTX 32-bit
    nvptx64 - NVIDIA PTX 64-bit
    r600    - AMD GPUs HD2XXX-HD6XXX
    thumb   - Thumb
    thumbeb - Thumb (big endian)
    x86     - 32-bit X86: Pentium-Pro and above
    x86-64  - 64-bit X86: EM64T and AMD64
```


生成字节码 .bc

```
clang -emit-llvm -c test.c
```

生成 .ll

```
# 从源文件
clang -emit-llvm -S test.c

# 从字节码
llvm-dis test.bc
```

生成 .s

```
llc test.ll
or 
llc test.bc
```




c -> cpp 

```
llc -mtriple=cpp hello.s -o hello.cpp 
```