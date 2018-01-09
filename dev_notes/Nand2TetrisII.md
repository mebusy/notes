
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

