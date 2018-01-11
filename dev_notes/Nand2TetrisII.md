
# N2T II

# Week 1  Virtual Machine I:  Stack Arithmetic

## 1.0 The Road Ahead

 - From high-level to low-level
    - `*.jack` -> compile ->
    - `*.vm`  
        - in Java language, we use `java` command to execute the vm code
        - in our world, we use **VM translator** to translate the vm code into one assembly file `xxx.asm`
    - `xxx.asm` -> assembler ->  
    - `xxx.hack`  

 - The road ahead:
    - m1,m2, building a virtual machine
    - m3:  writing a compute game
    - m4,m5: developing a compiler
    - m6: developing an OS

## 1.1 Program Compilation Preview

 - Jack compilation 
    1. Jack program -> Jack compiler -> VM code
    2. VM code
        - a) run on **VM emulator** aside on you PC
        - b) use a **VM translator** to translate the VM code into machine language.

## 1.2 VM Abstraction: the Stack

 - VM code 设计可以选择 偏向 高级语言抽象，或 机器语言抽象
 - 一个平衡的比较好的设计是 Stack machine

 - Stack machine abstraction
    - Architecture : a Stack
    - Commands : a set of operations that can be applied to this architecture

### Stack

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stack.png)

 - stack pointer
    - points to the location in which the next value is going to be pushed.
 - Stack arithmetic
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ n2t_stack_arithmetic.png)
    - add: pop the 2 top most values , add them , then push the result back
    - neg: not simply negate , it will first of all pop the top value , negate it on the side and then push the result back.
 - Applying a function *f* on the stack:
    - pops the argument(s) from the stack
    - computes *f* on the arguments
    - Pushes the result onto the stack
 - Boolean operations
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stack_boolean_operation.png)

### Stack arithmetic , the big picture

 - Where do these commands come from ?
    - They come from the compiler. 
 - if you start with a high-level statement like `x=17+19` , the compile is going to translate it into , in this case :

```
push 17
push 19
add
pop x
```

 - Abstraction / implementation
    - The high-level language is an abstraction
    - It can be implemented by a stack machine
    - The stack machine is an abstraction 
    - It can be implemented by , ... something else 

### The stack machine model 

 - Stack machine , manipulated by 4 categories of commands:
    - Arithmetic / logical  commands
    - Memory segment commands 
    - Branching commands 
    - Function commands


### Arithmetic/Logical commands

 - example

```
// d=(2-x)+(y+9)
push 2
push x
sub
push y
push 9
add
add
pop d
```


```
// (x<7) or (y==8)
push x
push 7
lt
push y
push 8
eq 
or
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stack_commands.png)

 - Observation: Any arithmetic of logical expression can be expressed and evaluated by applying some sequence of the above operations on a stack.

## 1.3 VM Abstraction : Memory Segments

### The big picture 

 - Jack statments

```
static int s1, s2;
function int bar(int x, inty) 
    var int a,b,c ;
    ...
    let c = s1 +y ; 
    ...
}
```

 -  the compiler will translate the `let` statement  into

```
push s1
push y
add
pop c
```

 - something kinds of gets lost in the translation
    - we need some mechannism to record the different roles of different variables in one's program. 
    - we do this by introducing the notion of **memory segments**.
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_memory_segment.png)

 - now the vm code can be written as 

```
push static 0
push argument 1
add
pop local 2
```

 - something interesting has happened, we lost the variable names in the process. 
 - indeed, the VM does not recognize symbolic variable names. 
    - all variables are replaced by references to memory segments. 
    - and this is not something which is unique to our VM. 
 - 如果我们增加一个 virutal segment -- *constant* , it contains just 0,1,2,... 
 - 这样 Stack的 语法就可以 统一成:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_memory_segments2.png)

 - so why we need `push constant 17` , why can't we just say `push 17` ?
    - we do that, so we get a consistant syntax. 
    - this is a very small price to pay for this consistency
    - it also makes compilation easier.

---

 - in order to make life interesting , we actually have not 4, but 8 virtual memory segments
    - local / argument / this / that / constant / static / pointer / temp
 - why we need so many segments
    - to cover all the features of high-level language
 - all have the same syntax: 
    - push  segment index:  从指定segment 取第index地址的数据，压栈
    - pop   segment index:  出栈， 数据存入 指定segment index地址。


## 1.4: VM Implementation: the Stack

 - if we want to acutally execute the VM code in some concrete way, we have to realize it on some Von Neumann machine.
 - so what do we have to do ?
    - fist of all, you have to take these 4 or 8 memory segments, and we have to somehow map these memory segments on the single RAM that is available for us. 
    - once we come up with this mapping, we have to do something with the push / pop commands.
    - we have to translate them into a sequences machine labeling instructions that will operate on this world -- that we just built on the RAM.

### Stack machine

 - Implementation:  
    - Assumptions:
        - SP stored in RAM[0]
        - Stack base addr = 256 , that is , it will start begin in address 256

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stack_implementation.png)

```
// push constant 17
// logic in pseudo code
*sp = 17
sp++

// Hack assembly
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
```

 - Who will do above work :  vm code -> assembly code?
 - **VM translator** 
    - A program that translates VM code into machine language
    - Each VM command generates several assembly commands.


## 1.5 VM Implementation: Memory Segments

### Implementing local

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_local_seg_implementation.png)

```
// vm code: 
pop local 2

// pseudo code:
addr=LCL+2 , SP--,  *addr=*SP

// hack assembly 
You write it !
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_local_seg_operation.png)


### Implementing local, argument, this, that 

 - The big picture:  
 - When translating the high-level code of some method into VM code, the compile :
    - map the method's *local* and *argument* variables onto the local and argument segments
    - map the *object* fields and *array* entries that the method is currently processing onto the this and that segments.
 - local , argument , this and that are implemented precisely the same way.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_impl_local_argu_this_that.png)


### Memory segment: constant

 - The big picture:
 - When translating the high-level code of some method into VM code, the compile :
    - it translate high-level operations involving *constants* into VM operation involving the constant segment.
 - Implementation:
    - Supplies the specified constant
    - constant segment 并不真的存在
 - Caution: there is no *pop* for constant, it makes no sense.

```
// VM code
push constant i 

// Assembly code:
*SP=i , SP++
```

### Memory segment: static 

 - The big picture:
    - the compile maps the *static* variables that the method sees onto the static segment.
 - static variables should be seen by all the mothods in a program
    - Store them in some "global space"
    - Have the VM translator translate each VM reference *static i* (in file Foo.vm)  into an assembly reference *Foo.i*

```
// VM code 
// File Foo.vm
pop static 5
... 

// Generated assembly code:
// D=stack.pop (code omitted)
@Foo.5
M=D
...
```

 - Following assembly , the Hack assembler will map these references onto RAM[16],RAM[17], ..., RAM[255]
 - Therefore , the entries of the *static* segment will end up being mapped onto RAM[16], RAM[17], ..., RAM[255] , 
    - in the order in which they appear in the program. 
    - `push static i` , i 和 内存地址并没有什么关系

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_static_segment.png)

### Memory segment: temp

 - The big picture:  The compile
    - sometimes needs to use some variables for temporary storage
    - our VM provides 8 such temporary variables
 - Implementation:
    - a fixed, 8-place memory segment 
    - Mapped on RAM locations 5 to 12.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_ram_implementation.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_impl_temp.png)

### Memory segment: pointer

 - the pointer segment is a little bit obscure. 
    - you can't understand really why we need it until you begin to write the compiler. 
 - The big picture
    - the compiler generates code that keeps track of the base addresses of the *this* and *that* segments using the *pointer* segment. 
 - Implementing
    - Pointer is a fixed memory segment. It has only 2 entries -- 0 and 1.
    - `push pointer 0/1`  , `pop pointer 0/1`
    - accessing `pointer 0` should result in accessing THIS
    - accessing `pointer 1` should result in accessing THAT
 - Implementation: Supplies THIS or THAT. 

```
// VM code:
push pointer 0/1 

// Assembly code:
*SP=THIS/THAT, SP++
```

### VM Language Summary

 - Arithmetic / Logical commands
    - add, sub, neg, eq, gt, lt, and, or, not
 - Memory access commands
    - pop segment i
    - push segment i
 - Branching commands
    - label *label*
    - goto *label*
    - if-goto *label*
 - Function commands
    - function *functionName nVars*
    - call *functionName nArgs*
    - return 


## 1.7 VM Implementation on the Hack Platform

 - Standard VM mapping on the Hack platform

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stardard_vm_mapping.png)

## 1.A Perspective

 - out VM vs Java JVM
    - only 1 datatype : 16 bit integer , why JVM having integer, float, double ...
    - JVM also support multiplication , division , bit-wist operations
 - JVM on Android devices uses another abstract architecture -- register machine.
 - register machine is perhaps less elegant ,less beautiful than stack machine. but arguably, it generates code which is better optimized for processors of mobile devices.


---

# Week2:  Virutal Machine : Program Control

## 2.1 Program Contorl

 - Branching
 - Functions 
 - Function call-and-return
 - Dynamic memory management
 - Stack processing
 - Pointers
 - Completing the VM implementation

## 2.2 Branching

 - Branching commands
    - label *label*
    - goto *label*
        - jumps to execute the commands just after *label*.
    - if-goto *label*
        - *cond* = pop ,  执行 if-goto 会把栈顶单元弹出栈
        - if *cond* jump to execute the command just after *label*
        - (Requires pushing the condition to the stack just before the if-goto command)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_cond_jump.png)

 - Implementation:
    - simple: the assembly langauge has similar branching commands.


 












