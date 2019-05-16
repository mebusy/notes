## Nand2Tetris 笔记



## Boolean Functions and Gate Logic

<details>
<summary>根据真值表 , 写出 布尔函数</summary>

1. 关注真值表中 f=1 的行, 比如 1,3,5 行的f=1
2. 写一个范式, 只满足 第一行， 也即，这个范式, 只有1st row 结果是1; 3rd,5th row 都是0
3. 给其他 f=1的行，写出同样的 范式
4. 把所有的 范式相加
</details>

<details>
<summary>很长的范式，我们怎么能得到一个 最小范式呢？</summary>

 - NP-hard 
</details>

定理: 所有的布尔函数，都可以只用 AND,NOT 操作表示

NAND: 可以使用仅包含 NAND操作的表达式来表示任何布尔函数。

<details>
<summary>NAND 如何表示 AND/NOT 操作?</summary>

1. NOT(x) == (x NAND x)
2. (x AND y) = NOT( x NAND y )
</details>


## Code Generation

 - 简化问题
    1. 每个class 独立编译
    2. 每个类分为2部分: 类成员 和函数
 - 这个 mutiple class的编译 简化为 同一时间处理一个 subroutine
 
---

 - 变量
    - 为了生成VM code, 我们需要知道变量:
        - which kind ?  field,static(class level) ,  argument,local(subroutine level)
        - index in segment ?
    - 变量有多个 properties
        - name (identifier)
        - type (i.e. int, class name)
        - kind (i.e. field)
        - scope (class level subroutine level)
    - symbol table:
        - 使用 symbol table 管理 variable property
        - 1 symbol table for current class, 1 for current subroutine
        - 变量声明的时候，加入 symbol table 


 name | type | kind | #
--- | --- | --- | ---
x | int | field | 0
pointCount | int | static | 0
this  |	Point | argument | 0 (argument 0 in every method)


 - 表达式
    - Jack VM is based on Stack.  Postfix is Stack oriented.
    - 所以，后序遍历  parse tree 生成表达式的 VM code.
 - Flow of Control
    - 同时生成 VM label 用于跳转
    - **IF** 
        - 先把 if条件 取反(not) , 生成代码更简单紧凑
    - **WHILE**
        - 同if, 先 条件 取反
 - Compiling constructors
    - 编译器 调用 系统函数 申请内存空间
 - Compiling method calls
    - VM 是过程语言，所以编译器 需要把 OO调用 obj.foo(x1,x2,...) 重写成 foo(obj,x1,x2,...)
 - Compiling methods
    - access the object's fields:  
        - access the object's i-th field by accessing `this i`
        - But first, anchor the *this* segment on the object's data
    - compile method must return a value, caller of *void*  is responsible for removing the returned value from the stack
 - Handling Arrays
    - use 'pointer 1' and 'that 0'


    



