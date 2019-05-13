

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
    - 

    



