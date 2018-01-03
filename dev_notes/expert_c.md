
# 1

## register keyword 是个错误

 - The `register` keyword.
    - 这被证明是一个错误，这只是把原本编译器应该做的事情，强加给程序员
    - 由编译器而不是程序员 来决定为哪个变量使用寄存器，将会得到更好的代码
 - C强调硬件直接支持的低级操作带来了速度和可移植性，反过来又有利于UNIX的良性循环


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

# 2 It's Not a Bug, It's a Language Feature

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


## sizeof is operator

 - when sizeof's operand is a type it has to be enclosed in parentheses 
 - when operand is variable , parentheses is not required .

```c
p = N * sizeof * q; // there is noly 1 multiplication
r = malloc( p ); 
```

## Some of the Operators Have the Wrong Precedence

```c
int i ;
i=1,2;
```

 - what value does i end up with?
    - 逗号表达式，所以i==2 ?
    - 错， assignment has higher precedence ， you actually get:
        - `(i=1),2;`   (1==1)


## Order of Evaluation is always undefined

```c
x = f() + g() * h();
```

 - The values returned by g() and h() will be grouped together for multiplication, but g and h might be called in any order. 
 - Similarly, f might be called before or after the multiplication, or even between g and h. 
 - All we can know for sure is that the multiplication will occur before the addition
 - Most programming languages don't specify the order of operand evaluation.
    - It is left undefined so that compiler-writers can take advantage of any quirks in the architecture, or special knowledge of values that are already in registers.

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


