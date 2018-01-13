
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
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_stack_arithmetic.png)
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

 - boolean
    -  fales : 0, true: -1

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

 - Tip: 
    - 访问一个 base + offset 地址 (M1)的内容 ，需要使用全部的A/M/D 三个寄存器
    - 无法把M1的结果很另外一个 base + offset 地址(M2) 做运算
    - 但是 M1 和 可以直接寻址，或 直接寻址基础上 A+1 的地址 (Md)  做 运算
    - 所以可以把 M1的内容先寄存到 (M2+1) , 然后就可以 M2,M2+1 做运算

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


## 2.3 Functions Abstraction

 - Functions in the VM language
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_funcs_in_VM.png)
 - The VM language features:
    - primitive operations (fixed) : add, sub, ...
    - abstract operations (  extensible) : multiply , sqrt, ...
 - **Applying a primitive operator and calling a function have the same look-and-feel**
 - 这里这是抽象，并不是真正的 VM 语法

### defining 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_definition.png)

 - `function mult 2` 
    - 2 means the number of **local** variables which will be used !!! 

### executing

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_execute.png)

 - `call func n` , here *n* means the number arguments ?
 - after line 0 of `function mult 2` is executed:
    - First of all I get an empty stack
    - The 2nd thing that I get is an argument segment. 
        - it contains the exact 2 values that were pushed by the caller
    - then another thing that I get is 2 local variables which initialized to 0. 
        - why do I get 2 local variables ?
        - `function mult 2` , so the VM implementation prepared for me a segment called local. 
 - eventually we push the result to stack , because we want to return this vallue to the caller.
    - command `return` , the VM implementation knows how to handle return.
    - it takes the top most value in the stack of the callee , and just puts it on the stack of the caller instead of the arguments that were pushed previously.


### Making the abstraction work: implementation

 - For each function **call** during run-time, the implementation has to ...
    - Pass parameters from the calling function to the called function 
    - Determine the return address within the caller's code
    - Save the caller's return address , stack and memory segments
    - Jump to execute the called function.
 - For each function **return** during run-time, the implementation has to ...
    - Return to the caller the value computed by the called function
        - here there's an implicit assumption: it is required that the callee always pushes a value before it returns.
    - Recycle the memory resources used by the called functin
    - Reinstate the caller's stack and memory segments
    - Jump to the return address in the caller's code


### Function call and return :  units plan

 - 2.4 Implementation preview
 - 2.5 Run-time simulation
 - 2.6 Detailed implementation 



## 2.4 Function Call and Return: Implementation Preview

 - Function execution
    - Calling chain:  foo > bar > sqrt > ...
    - For each function in the calling chain during run-time , we must maintain the function's *state*
 - Function's state
    - During run-time
        - Each function uses a working stack + memory segments
    - The working stack and some of the segments should be:
        - Created when the function starts running
        - Maintained as long as the function is executing
        - Recycled when the function returns 
 - So in general , when a caller calls a callee, we will have now 2 states:
    - state of caller
    - state of callee

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_state_of_caller_callee.png)

 - How to maintain the states of all the functions up the calling chain ? 
    - The calling pattern is LIFO , it's a Stack

### the big picture 

 - Example: computing mult(17,212)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_example_17p212.png)

 - Net effect:
    - The function's arguments (17,212) were replaced by the function's value (3604)

### Function call and return: the detail

**call**


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_details_0.png)



 - VM implementaion
    1. Sets arg  
        - the ARG pointer should refer to the base address of the argument's segments in the memory
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_details_1.png)
    2. Saves the caller's frame
        - it consists of the working stack of the caller , and the current segment that it uses.
        - the working stack is safe. 
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_details_2.png)
        - and now I have to save the segments , and the return address . 
            - taken together, we call these things the function's frame.
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_details_3.png)
            - yes , the static, pointer, temp , constant   don't need to be saved  because they don't belongs to functions 
    3. Jumps to executed *foo*
    

**function**

 - we now hit the command `function foo nVars`
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_0.png)
 - VM implementation:
    - Sets up the local segment of the called function
        - I need *n* local variables , and I also need to initialized them to 0.
        - I push *n* 0s onto the stack , and set LCL.  
        - once I do it, I can refer to these values on the stack as locol 0, local 1, and so on.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_1.png)
    - Now the functions is ready to take off and start running. Let's assume that the function is running and doing its things. 
        - and in the process, it grows its working stack, and it now has a working stack of its own.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_2.png)  
    - And then at some point , it is going to return.  It need push a return value onto the stack, and then I say `return`.

**return**

 - now VM implementation has to service the return command.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_3.png)    
 - VM implementation:  
    - First of all, we have to take the topmost value from the stack, the return value,  and we have to 
        - **copy the return value onto argument 0**.   See the *net effect* above.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_4.png)   
    - THe next thing that we do is 
        - **restore the segment pointers of the caller**
        - take the saved CLC, ARG, THIS, THAT ,  and turn them into current ones. 
    - Then to 
        - **clear the stack** 
        - call the stack of the called function, which is no longer relevant. 
    - Then I have to **set the SP for the caller**. 
        - the SP for the caller should be located just after the return value, just after argument 0. 
    - After I do this, I have to finally 
        - **jumps to the return address within the caller's code**. 
        - and continue executing the caller's code. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_5.png)   

### The global stack 

 - block
    - I can refer to some segment or some subsets of this global stack here, using the term **block** , which I just made up.
    - It is the world of the currently running function.
 - The block contains :
    - my argument segment
    - caller frame. 
    - my local segments 
    - and my working statck

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_global_stack.png)


## 2.5 Function Call and Return: Run-time Simulation

 - Example: factorial         

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_example_factorial.png)

### Runtime 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_runtime1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_runtime2.png)
         

## 2.6: Function Call and Return Implementation

 - A function may call another function which historically belongs to a different class.
 - But once everything is compiled into VM code , we lose this notion of classes and what we get is just a long list of functions that have a full name. i.e. Bar.mult

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_class_function.png)

 - caller's view
    - Before calling another function , I must push as many arguments as the function expects to get
    - Next, I invoke the function using `call functionName nArgs` 
    - After the called function returns , the argument values have disappeared from the stack ,and a *return value* (that always exists) appears at the top of the statck
    - After the called function returns , all my memory segment are exactly the same as they were before the call.
        - (except that *temp* is undefined and some values of my *static* segment may have changed )
 - callee's view
    - Before I start executing , my *argument* segment has been initialized with the argument values passed by the caller
    - My *local* variables segment has been allocated and initialized to zeroes
    - My *static* segment has been set to the static segment of the VM file to which I belong.
        - ( memory segments this, that , pointer and temp are undefined upon entry )
    - My working statck is empty.
    - Before returning , I must push a value onto the stack
        - even if the function prototype is 'void f()' , you also need return a value. You may push a 0 to the stack.
        - it's the caller's responsibility to do something with returned value.

 - The VM implementation view
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_func_class_assembly_code.png)
 - When `Foo.main` call `Bar.mult`,  the VM translator , as we saw in above picture, is going to 
    - save the caller's state , the state of the Foo.main function
    - do a few more things to set up for the function call
    - and finally , it's going to say "go to the name of the function "
 - So, presumably , the VM translator at some point will generate a label which is the name of this function
    - `(Bar.mult)`
    - this is how we represent the entry point to a function in the translated  assembly code.




### Handling call

 - the caller is running ,doing some work .   and then all of a sudden , we encounter a call .
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_handel_call1.png)
    - VM实现上，push arguments 的事情，在 call 语句之前就做好了
 - VM command : `call functionName nArgs`
    - calls the function, informing that nArgs arguments have been pushed onto the stack
 - Assembly code (generated by the translator) :
    - the first thing is I push a label onto the stack and later on I'm going to use the same label as the label to which I'm going to return after the callee terminates.
    - then I push LCL to save the state of my local segment 
    - and the ARG  , THIS , THAT
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_handel_call2.png)
    - now, ARG should be reposition for the callee.  obviously we should reposition it at the beginning of the nArgs arguments.  where is this address ? I can calcuate because I know how many things I pushed -- nArgs + 5. 
    - then resposition LCL : LCL = SP
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_handel_call3.png)
    - finally , I goto execute the called function.  
    - And now I do something very tricky, I insert into the generated code stream the label that I **pushed before** . 

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_function_handel_call4.png)

### Handling function

 - whenever we hit a function command , the 1st thing the translator does is it takes the function name and generates a lable, and this label will serve as the entry point to the translated assembly code of this function. 
 - and then we simply have to write some assembly code that handles the setting up of the function's execution. 
 - **VM command**: `function functionName nVars` ( starts a function that has nVars local variables )
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_handle_function1.png)
 - **Assembly code** (generated by the translatro):
    - first of all I take the function name , and generate this label. 
    - and then I repeat nVars times *push 0 to local segment* , now the function can start doing its thing. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_handle_function2.png)
    - at some point , it will want to return.
        - I have to generate assembly code that moves the return value to the caller, reinstates the caller's state, and then does a `goto` Foo's return address. 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_vm_handle_function3.png)












