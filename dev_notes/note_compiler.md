...menustart

- [Nand2Tetris 笔记](#6cda5e46c1ef1aef8449764e0d9a327f)
- [Boolean Functions and Gate Logic](#deb69b5e23e0f74aea56d42c2df9b438)
- [Assembler](#17890d645ed41b2a5b1166f427d0e31c)
- [Virtual Machine](#b19292cad601553e06435e12582db069)
- [Code Generation](#0138da8da6c96a41001c44e79c105ba8)

...menuend


<h2 id="6cda5e46c1ef1aef8449764e0d9a327f"></h2>


## Nand2Tetris 笔记



<h2 id="deb69b5e23e0f74aea56d42c2df9b438"></h2>


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


<h2 id="17890d645ed41b2a5b1166f427d0e31c"></h2>


## Assembler

- 汇编器
    1. 处理指令    
        - `dest=comp;jump`  => binary machine code 
    2. 处理符号 symbol 

- 汇编语言中会出现 Symbol , 汇编器 要负责把 symbol 转成地址
    1. Variables : `Load R1, weight`
        - 使用一个 symbol table <symbol name , memory address>
        - 如果 label 在 表中，直接使用; 如果不在，分配一个新的地址(static memory of Hack RAM), 并将 条目<symbol,address> 放入表中
    2. Labels : `JMP loop`
        - 记录 label 下一条指令的地址.
        - 但如果在声明之前 使用标签怎么办？
            - 2 pass
            - 1st pass , 提取 汇编code行(非注释和label定义)，添加 lable 到 symbol table
            - 2nd pass , 翻译 code 

<h2 id="b19292cad601553e06435e12582db069"></h2>


## Virtual Machine

- The stack machine model
    - Arithmetic / logical commands
        - add,sub,neg, eq,gt,lt,and,or,not
    - Memory segment commands
        - local / argument / this / that (这4个segment的地址是动态分配的) / constant / static / pointer / temp
        - push/pop *segment i*
    - Branching commands
        - 声明: label *label*
        - 直接跳转: goto *label*
        - 条件跳转: if-goto *label*  
            - *cond* = pop,  会先把 条件出栈
    - Function commands 
        - definition/executing: `function mult 2`  (2 means it will use 2 **local** variable)
            - 高级语言编译函数的时候，就需要确定 函数需要几个 local变量
            - 这个时候，我应该有 一个空的堆栈，caller 已经把 *n*个参数压入了 argument segment, local segement中有两个 local variabel which initialized to 0.
            - *return*: 最后，把结果压入堆栈
        - 调用: `call mult n`  ( here n means the number of arguments ) 
- VM Implementation
    - Misc
        - you may create LABEL in order to do branch
        - goto / if-goto / VM Lable
    - Function
        - For each function **call** during run-time
            - 从 caller 传递参数给 callee
            - 保存 caller的返回值，stack, memory segment
            - 跳转 执行 被调用函数
        - For each function start executing 
            - 创建 working stack and some of the segments
        - For each **function return** during run-time
            - 返回结果给 caller
            - 回收 callee 使用的内存
            - 恢复 caller的  stack and memory segments
            - 跳转到 return address


<h2 id="0138da8da6c96a41001c44e79c105ba8"></h2>


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
this  | Point | argument | 0 (argument 0 in every method)


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


变量声明 加入 symbol table -> local ， 可能有多条， 可能需要统计nLocal
参数  加入 symbol table   -> argument
static/field , 加入 symbol table

函数定义，  需要预先计算 local 变量的个数
	构造函数 还要计算 实例内存大小 (field个数)
	method / constructor 要先 anchor this

函数return  , 对应vm return, 如果 return后没有表达式，需要 压一个值进堆栈

函数调用 ,  call function , 需要统计 paramlist 的 实参个数
	函数调用后，总会在 堆栈上存放结果， do 需要清理掉
	如果是 类方法调用 var.Func() , 则需要把这个var先压栈，调用时 nParam+1


表达式 term [op term] 中的op ， 直接 输出对应的 vm 指令(i.e. add)，或函数调用(i.e. call Math.divide 2) , 表达式的最终结果，总会在栈上

let 赋值  , 先处理表达式， 在复制

整数常量   push constant x

id :  一般情况 push ， 赋值号= 左侧 pop


    



