...menustart

 - [1](#c4ca4238a0b923820dcc509a6f75849b)
     - [register keyword 是个错误](#e540c9df86ffde8f8d8443c5347dab50)
     - [`char **argv` 和 `const char **p` 并不匹配](#f478e0a5be9950a75d566a3de6949efa)
     - [隐式类型转换的坑](#7441ae385364f96b273420fec579d734)
 - [2 It's Not a Bug, It's a Language Feature](#7e14dfcaec2adef0aa128a546178eb6b)
     - [空格连接字符串](#9b2b1da3319fe706936ecc07f63165b3)
     - [Too Much Default Global Visibility](#57627d14558e5f49e76b214f3cedf6bb)
     - [sizeof is operator](#8c120ee8f50200d57dc2c236a4aea6c2)
     - [Some of the Operators Have the Wrong Precedence](#892ab9a4c1d171fd57439aa763e50a23)
     - [Order of Evaluation is always undefined](#646b355af48a02490fb7d836806d222e)
 - [3. Unscrambling Declarations in C](#72b031c516a7abf0388911bba461224a)

...menuend


<h2 id="c4ca4238a0b923820dcc509a6f75849b"></h2>

# 1

<h2 id="e540c9df86ffde8f8d8443c5347dab50"></h2>

## register keyword 是个错误

 - The `register` keyword.
    - 这被证明是一个错误，这只是把原本编译器应该做的事情，强加给程序员
    - 由编译器而不是程序员 来决定为哪个变量使用寄存器，将会得到更好的代码
 - C强调硬件直接支持的低级操作带来了速度和可移植性，反过来又有利于UNIX的良性循环


<h2 id="f478e0a5be9950a75d566a3de6949efa"></h2>

## `char **argv` 和 `const char **p` 并不匹配

```c
foo(const char **p) { }

main(int argc, char **argv) {
    // line 5: warning: argument is incompatible with prototype
    foo(argv);
}
```

 - So doesn't argument `char **argv` match parameter `const char **p` ?
    - no, it does not.
    - 这要从赋值说起。
 - 函数传参是 赋值操作. 其中有一条限制 constraint:
    - Both operands are pointers to qualified or unqualified versions of compatible types
    - and the type pointed to by the left has all the qualifiers of the type pointed to by the right. 
 - 所以下面的语句是 完全合法的

```c
char * cp;
const char *ccp;
ccp = cp;
```

 - 因为
    1. The left operand is a pointer to "char qualified by const". (  qualifiers: const )
    2. The right operand is a pointer to "char" unqualified.   ( qualifiers: none )
    3. The type char is a compatible type with char, and
        - the type pointed to by the left operand has all the qualifiers of the type pointed to by the right operand (none) , plus one of its own (const)
 - 但是 operand 反过来 就会触发一个编译警告

```c
cp = ccp; /* results in a compilation warning */
```

 - 但是前面的 `const char ** = char **` 也由警告呢？
    - 简单说，`const float *` 是一个指针(pointer to const-qualified float)，他不是一个 qualified type！！  
    - 同样的 `const char **` is a pointer to an unqualified pointer 
        - `const char **` 的类型是  a pointer to a pointer to a qualified type. 
 - 所以，`char **` and `const char **` 都是 指针, 但指向的是不同的 类型
 - 关于const
    - const 限定的是 type, 不是 variable, 因为const的功能是得到“限定的类型” 
    - C 引入const关键字的目的是优化代码，这是程序员和编译器间的约定： 
        - 他不会改变对象的值，所以可以直接使用对象的初始值而不用费工夫去读对象。

<h2 id="7441ae385364f96b273420fec579d734"></h2>

## 隐式类型转换的坑

 - Operands with different types get converted when you do arithmetic. 
    - Everything is converted to the type of the floatiest, longest operand, signed if possible without losing bits.
 - A Subtle Bug:
    - 下面程序的打印语句并不会被执行到
    - `sizeof` 的返回值是 unsigned int (maybe long) , 
    - The test is comparing a signed int with an unsigned int quantity.
    - So d is promoted to unsigned int, yields a big positive number


```c
int array[] = { 23, 34, 12, 17, 204, 99, 16 };
#define TOTAL_ELEMENTS (sizeof(array) / sizeof(array[0]))

int main(int argc, char **argv) {
    int d = -1;
    if (d <= TOTAL_ELEMENTS-2)
        printf( "can I be here ?\n" );
}
```

<h2 id="7e14dfcaec2adef0aa128a546178eb6b"></h2>

# 2 It's Not a Bug, It's a Language Feature

<h2 id="9b2b1da3319fe706936ecc07f63165b3"></h2>

## 空格连接字符串 

```c
    printf(  "a" 
             "b" 
             "c"  ) ;  // $ abc

    char * str = "d" "e" ;
    printf( "%s" , str ) ; //de
```

 - 这个特性 在以下情况下有可怕的后果：
 
```c
char *available_resources[] = {
  "color monitor",
  "big disk",
  "Cray" /*           whoa! no comma! */
  "on-line drawing routines",
  "mouse",
  "keyboard",
  "power cables",     /* and what's this extra comma? */
};
```
 
<h2 id="57627d14558e5f49e76b214f3cedf6bb"></h2>

## Too Much Default Global Visibility

 - C函数，默认是全局可见。
    - The function is visible to anything that links with that object file
 - 如果你想限制对函数的访问，你必须指定static关键字。

```c
       function apple (){ /* visible everywhere */ }
extern function pear () { /* visible everywhere */ }
static function turnip(){ /* not visible outside this file */ }
```

 - 太多的全局可见性会导致 方法名很容易和 库函数同名。


<h2 id="8c120ee8f50200d57dc2c236a4aea6c2"></h2>

## sizeof is operator

 - when sizeof's operand is a type it has to be enclosed in parentheses 
 - when operand is variable , parentheses is not required .

```c
p = N * sizeof * q; // there is noly 1 multiplication
r = malloc( p ); 
```

<h2 id="892ab9a4c1d171fd57439aa763e50a23"></h2>

## Some of the Operators Have the Wrong Precedence

```c
int i ;
i=1,2;
```

 - what value does i end up with?
    - 逗号表达式，所以i==2 ?
    - 错， assignment has higher precedence ， you actually get:
        - `(i=1),2;`   (1==1)


<h2 id="646b355af48a02490fb7d836806d222e"></h2>

## Order of Evaluation is always undefined

```c
x = f() + g() * h();
```

 - The values returned by g() and h() will be grouped together for multiplication, but g and h might be called in any order. 
 - Similarly, f might be called before or after the multiplication, or even between g and h. 
 - All we can know for sure is that the multiplication will occur before the addition
 - Most programming languages don't specify the order of operand evaluation.
    - It is left undefined so that compiler-writers can take advantage of any quirks in the architecture, or special knowledge of values that are already in registers.

<h2 id="72b031c516a7abf0388911bba461224a"></h2>

# 3. Unscrambling Declarations in C

 - C's declaration syntax is trivial for a compiler (or compiler-writer) to process, but hard for the average programmer.
 - The BCPL language (the grandfather of C) was type-poor, having the binary word as its only data type, so C drew on a base that was deficient. 
 - And then, there is the C philosophy that the declaration of an object should look like its use.
    - An array of pointers-to-integers is declared by `int * p[3];`
    - and an integer is referenced or used in an expression by writing `*p[i]`
    - so the declaration resembles the use.
 - The advantage of this is that the precedence of the various operators in a "declaration" is the same as in a "use".
 - The disadvantage is that operator precedence
    - Programmers have to remember special rules to figure out whether int `*p[3]` is an array of pointers-to-int, or a pointer to an array of ints.
 - A better idea would have been to declare a pointer as 
    - `int &p;`
    - which at least suggests that p is the address of an integer. 
    - This syntax has now been claimed by C++ to indicate a call by reference parameter.
 - But the biggest problem is that you can no longer read a declaration from left to right, as people find most natural. 
    - The situation got worse with the introduction of the `volatile` and `const` keywords with ANSI C; 
    - since these keywords appear only in a declaration (not in a use), there are now fewer cases in which the use of a variable mimics its declaration. 
 - If you want to cast something to the type of pointer-to-array, you have to express the cast as:

```c
char (*j)[20]; /* j is a pointer to an array of 20 char */
j = (char (*)[20]) malloc( 20 );
```

 - What exactly, for example, does the following declaration (adapted from the telnet program) declare?

```c
char* const *(*next)();
```

 - see [c declaration,struct/union/enums/typedef](https://github.com/mebusy/notes/blob/master/dev_notes/c_declaration.md) 


# 4 C Arrays and Pointers Are NOT the Same!

## Arrays Are NOT Pointers!

```c
extern int *x;
extern int y[];
```

 - The first declares x to be a pointer to int;
 - the second declares y to be an array of int of unspecified size (an incomplete type),
    - the storage for which is defined elsewhere.

## What's a Declaration? What's a Definition?

· | · | ·
--- | --- | --- 
definiton | occurs in only on place |  specifies the type of an object; reserves storage for it; is used to create new objects
· | · | example: `int my_array[100];`
declaration | can occur multiple times | describes the type of an object; is used to refer to objects defined elsewhere (e.g., in another file)
· | · | example: `extern int my_array[];`


## How Arrays and Pointers Are Accessed

 - address y and contents of address y

```c
x = y ;
```

x | y
--- | ---
x, in this context, means the **address** that x represents | y, in this context, means the **contents of the address** that y represents
This is termed **l-value**  | This is termed **r-value**
An **l-value** is known at compiletime | an **r-value** is not known until runtime. 
An **l-value** says where to store the result | "The value of y" means the **r-value**  unless otherwise stated

 - A "modifiable l-value" is a term introduced by C. 
 - It means an l-value that is permitted to appear on the left-hand side of an assignment statement. 
 - This weirdness was introduced to cope with arraynames which are l-values that locate objects, but in C may not be assigned to.
 - Hence , an arrayname is an l-value but not a modifialbe l-value.  
 - The standard stipulates that an assignment operator must have a modifiable l-value as its left operand. 
 - **You can only assign into things that you can change.**.

---

 - The compiler allocates an address (or l-value) to each variable (x , y).
 - This address is known at compiletime, and is where the variable will be kept at runtime. 
 - In contrast, the value stored in a variable at runtime (its r-value) is not known until runtime.
    - If the value stored in a variable is required, the compiler emits code to read the value from the given address and put it in a register.
 - The key point here is that the address of each symbol is known at compiletime. 
    - 所以，如果编译器需要用地址做一些事情（可能是增加一个偏移量），它可以直接做到这一点，不需要植入代码来首先取到地址。
    - In contrast, the current value of a pointer must be retrieved at runtime before it can be dereferenced
 - A Subscripted Array Reference:

```c
char a[9] = "abcdefg" ; 
...
c = a[i] ;
``` 

 - compiler symbol table has *a* as address 9980
    - runtime step1:  get value i , add add it to 9980
    - runtime step2:  get the contents from address (9980+i)
 - That's why you can equally write `extern char a[];` as well as `extern char a[100];`

    
## What Happens When You "Define as Pointer/Reference as Array"

 - Consider the case of an external declaration
    - `extern char *p;`
 - but a definition of 
    - `char p[10];`
 - When we retrieve the contents of `p[i]` using the extern, we get characters, but we treat it as a pointer.
 - Interpreting ASCII characters as an address is garbage . and 
    - if you're lucky the program will coredump at that point. 
    - If you're not lucky it will corrupt something in your address space, causing a mysterious failure at some later point in the program.


 - **Match Your Declarations to the Definition**

## Other Differences Between Arrays and Pointers

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_diff_array_pointer.png)

---

# Thinking of Linking

 - A Compiler is Often Split into Smaller Programs
    - C Preprocessor  : Phase p
    - Front-end   : Phase 0
    - Back-end (code generator) : Phase c
    - Optimizer : Phase 2
    - Assembler : Phase a
    - Link-loader : Phase l 
 - You can look at the individual phases of compilation by using the `-v` option.
 - You can pass options to each phase, by giving the compiler-driver a special `-W` option
    - that says "pass this option to that phase." 
    - The "W" will be followed by a *character indicating the phase*, a *comma*, and then the *option*. 
 - So to pass any option through the compiler driver to the linker, you have to prefix it by "-Wl," to tell the compiler driver that this option is intended for the link editor , not the others.
 - The command 
    - `cc -Wl,-m main.c > main.linker.map`
    - will give ld the "-m" option, telling it to produce a linker map. 

## The Benefits of Dynamic Linking

 - Dynamic linking permits easy versioning of libraries. 
    - New libraries can be shipped; once installed on the system, old programs automatically get the benefit of the new versions without needing to be relinked.
 - Dynamic linking is "just-in-time" linking. It does mean that programs need to be able to find their libraries at runtime.
    - 链接器通过将库文件名或路径名放入可执行文件来完成此操作;
    - and this in turn, means that libraries cannot be moved completely arbitrarily.
    - 当你在 与编译的机器 不同的机器上执行时，这也是一个问题。 
        - 执行机器必须包含所有链接的库，并且必须将它们放在您告诉链接器的目录中。 
        - 对于标准系统库，这不是问题。
 - The main reason for using shared libraries is to get the benefit of the ABI
    - freeing your software from the need to recompile with each new release of a library or OS. 
    - As a side benefit, there are also overall system performance advantages.
 - 任何人都可以创建一个静态或动态库。 
    - 只需编译一些没有 main routine 的代码，然后 使用正确的工具来处理 生成的.o文件
    - ar for static library
    - ld for dynamic library

## Five Special Secrets of Linking with Libraries
 
 1. Dynamic libraries are called lib something.so , and static libraries are called lib something.a
 2. You tell the compiler to link with, for example, `libthread.so` by giving the option `-lthread`
 3. The compiler expects to find the libraries in certain directories
    - 编译器会查找一些特殊的地方，例如`/usr/lib/`
    - 编译器选项-Lpathname用于告诉链接器其他目录的列表，用于搜索已经使用 `-l`选项指定的库
 4. Identify your libraries by looking at the header files you have used
 5. Symbols from static libraries are extracted in a more restricted way than symbols from dynamic libraries


# 6. Poetry in Motion: Runtime Data Structures

## Segments

 - 就 object files 而言, they are simply areas within a binary file , where all the information of a particular type (e.g., symbol table entries) is kept.
 - The term *section* is also widely used. 
 - A segment typically contains several sections.

--- 

 - Don't confuse the concept of segment on UNIX with the concept of segment on the Intel x86 architecture.
    - A segment on UNIX is *a section of related stuff in a binary*.
    - A segment in the Intel x86 memory model is *the result of a design in which (for compatibility reasons) the address space is not uniform, but is divided into 64-Kbyte ranges known as segments.*

 - When you run size on an executable, it tells you the size of three segments known as text, data, and bss in the file:

```bash
# size a.out
text       data     bss     dec     hex filename
1134        540       4    1678     68e a.out
```

 - Another way to examine the contents of an executable file is to use the *nm* or *dump* utilities. 


