...menustart

 - [5. Computer Architecture](#82c3a1ecfb73757b332ca9d07818fea2)
     - [5.1 Von Neumann Architecture](#33999dda2fa6608276c40dda9517d0c1)
         - [Elements](#aa56a2e65d8106aef3c61e4f6bf94fdb)
         - [Information Flows](#4cddecdacbbc625f8b0abf04f6aa1e86)
         - [Buses](#4c7bdd90410042e10dd67436384e17aa)
     - [5.2 The Fetch-Execute Cycle](#44e3bf233a0e7a5decff0aaab2d17d15)
         - [Fetching](#7865d8f54c20047006223a67ab639b70)
         - [Executing](#63c4cc5944eb60b1969f2333ead70fc9)
         - [Fetch-Execute Clash](#24e481da85387c537c02bb45d1bbc147)
     - [5.3 CPU](#b43585e7acd4132480f7f36e8e58c499)
         - [The Hack CPU: Abstraction](#3fee1c0b6153717300bc562cf724cc03)
         - [Hack CPU Interface](#66265d28f431087151dad2e1471f5db8)
         - [Hack CPU Implementation](#fb18d6304583643441f45cc4da665c41)
         - [Instruction handling](#d0879da14db1669fd7cc551b67fe7b6f)
         - [ALU operation](#5dd0ed8d0cd686c9ca44dd3a0f3484a8)
         - [PC logic](#18af6f320c794ce703ecd7e4c44fbf96)
     - [5.4 The Hack Computer](#2d5b2381493e2e74b418ec4570b18f6c)
         - [Hack CPU Operation](#c366294d33d33ad8f41ff39d909e530f)
         - [Data Memory](#fdef999b11b2cf3acbf0df16e8882100)
         - [Instruction Memory (ROM)](#f94f42245da94b6b457000847ee3b0f7)
         - [Hack Computer implementatioin](#d1ab5781342f30b0410b1955380662e6)
     - [5.5 Project Overview](#6aa600c7db11b3f439b312fdeaab651c)

...menuend


<h2 id="82c3a1ecfb73757b332ca9d07818fea2"></h2>


# 5. Computer Architecture

<h2 id="33999dda2fa6608276c40dda9517d0c1"></h2>


## 5.1 Von Neumann Architecture

![](../imgs/n2t_architexture_overall.png)

<h2 id="aa56a2e65d8106aef3c61e4f6bf94fdb"></h2>


### Elements

 - CPU  
    - ALU
    - Register
 - Memoy
    - Program
    - Data

<h2 id="4cddecdacbbc625f8b0abf04f6aa1e86"></h2>


### Information Flows

 - control bus
 - data bus
 - address bus

<h2 id="4c7bdd90410042e10dd67436384e17aa"></h2>


### Buses

 - ALU loads information from the Data bus and manipulates it using the Control bits.
    - so it must connect to Data / Control bus
 - Register definitely connect to Data bus , and some time it used to specify some  address , so it connect to address bus as well
    - data / address are stored in registers
 - Memory is simular to Register 
    - There is an important thing, is the program instruction tell the system what to do, so we need to be able to actually take information from the next instruction , from the data output of program memory , and feed it into the control bus.   

---

<h2 id="44e3bf233a0e7a5decff0aaab2d17d15"></h2>


## 5.2 The Fetch-Execute Cycle

 - we're going to talk about the very basic thing that a compute does, which is
    - execute one instruction after the other.
 - THe basic CPU loop
    - **Fetch** an instruction from the Program memory
    - **Execute** it

<h2 id="7865d8f54c20047006223a67ab639b70"></h2>


### Fetching

 -  Fetching
    - Put the location of the next instrution into the "address" of the program memory
    - Get the instruction code itself by reading the memory contents at that location
 - How do we actually go about putting the address of the next instruction  into the address input of the programm memory ?
    - we're going to have to put it somewhere , and that's going to be into some register, and that is usually called the Program Counter. 
    - ![](../imgs/n2t_the_PC.png)
    - The output of the PC , feeds into the address specification of our program memory,
    - and then the *out* of the program memory , comes the actual code of instructions , that we need to execute.
 
<h2 id="63c4cc5944eb60b1969f2333ead70fc9"></h2>


### Executing 
 
 - Executing the operation involves also accessing registers and/or data memory

<h2 id="24e481da85387c537c02bb45d1bbc147"></h2>


### Fetch-Execute Clash 

 - There is a fact that we really have a clash between the fetch cycle and the execute cycle.
    - both the program and the data reside in memory 
    - In the fetch cycle , basically we need to get from the program memory the next instruction 
        - so we need to put into the address of the memory , the address of the next instruction and get the instruction output.  
    - On the other hand, in the execute cycle, we need to access data that also resides in memory.
        - we need to put into the address of the memory , the address of te data piece that we want to operate on
    - that is , the fetch part of the cycle reads from the program memory, and the execute part reads from data memory.
    - and because we have a single memory , that is a clash. 

![](../imgs/n2t_fetch-execute_clash.png)


 - How to solve it ?
    - basically we are going to do one after the other, that is the usual way. 
    - There is going to be a multiplexer that feeds into the address of the memory. 
    - In the first part of the cycle , the fetch cycle, we're going to actually set the multiplexer to plug into the address input of the memory, the program counter that is the location of the next instruction. 
    - while in the execute cycle, the multiplexer will actually set the memory to actually point into the data address that we need to access. 
 - so now ,in fetch cycle, we get the instruction , in executing cycle  we get the data.
    - but how we know the acutal instruction when we are in executing cycle?
    - we need at first store the instruction to a **instruction register**.

![](../imgs/n2t_instruction_register.png)

 - This is the usual way it's done. Now there is a shortcut.
 - Simple solution: Harvard Architecture
    - Variant of von Neumann Architecture
    - Keep Program and Data in 2 separate memory modules
        - each module has its own address.
    - Complication avoided.

<h2 id="b43585e7acd4132480f7f36e8e58c499"></h2>


## 5.3 CPU 

![](../imgs/n2t_cpu_architecture.png)

 - it is where all the calculations of the machine take place 
 - and it is also the seat on control.
    - this is where decisions are made about which instruction should be fetched and executed next.


<h2 id="3fee1c0b6153717300bc562cf724cc03"></h2>


### The Hack CPU: Abstraction 

 - A 16-bit processor, designed to
    - Execute the current instruction 
    - Figure out which instruction to execute next

<h2 id="66265d28f431087151dad2e1471f5db8"></h2>


### Hack CPU Interface 

![](../imgs/n2t_hack_cpu_interface.png)

 - Inputs
    - Data value , *inM* , from Data Memory
    - Instruction , *instruction* , from Instruction Memory
    - Reset bit, *reset* , From the user
 - at any time , there is always a selected memory both in Data memory and Instruction memory.

---

 - Outputs
    - Data value , *outM* , to Data Memory 
    - Write to memory ? (yes/no) , *writeM*, to Data Memory
    - Memory Address, *addressM*, to Data Memory
    - Address of next instruction, *pc*, **to Instruction Memory**
 - first of all, it the ALU wants to write something to the data memory, 
    - it has to specify 3 different things 
        1. what is that we want to write
        2. where we want to write it
        3. a load bit , that enables the data memory for write operation.
 - In addition , there's one extremely important output , pc , that holds the address of next instruction

<h2 id="fb18d6304583643441f45cc4da665c41"></h2>


### Hack CPU Implementation 

![](../imgs/n2t_hack_cpu_implementation.png)

 - the label *c* , represents the control bit.

<h2 id="d0879da14db1669fd7cc551b67fe7b6f"></h2>


### Instruction handling 

 - left-top part
 - CPU handling of an A-instruction
    - Decodes the instruction into op-code + 15-bit value
    - Stores the value in the A-register    
    - it also takes the output of the A-register , and emits it outside to the memory address output
        - i.e., `@100` 执行后， M[100] 就被选中了
 - CPU handling of an C-instruction
    - The instrcution bits are decoded into :
        - op-code , ALU control bits, dest bits, jump bits
    - op-code is 1, in this case we want to route the input of the A-register in such a way that the input will come from the ALU. 

<h2 id="5dd0ed8d0cd686c9ca44dd3a0f3484a8"></h2>


### ALU operation 

 - the entire top part, exclude *reset* line
 - so there is a C-instruction comes in
 - ALU data inputs :
    - 1.From the D-register
    - 2. From the A-register / M-register
 - the control bit of ALU's  multilexer is one of the bits in the instruction  
 - ALU control inputs:
    - 6 control bits  is also from the instruction 
 - ALU data output:
    - Result of ALU calculation ,fed simultaneously to:
        - D-register, A-register, M-register
    - the same ALU output knocking on 3 different doors
    - but the fact that it knocks on these doors does not necessailly means that the doors are going to open. 
    - the programmer has to decide , which door has to be opened.
    - which register *acutally* received the incoming value is determined by the instruction's *destination bits* 
    - ![](../imgs/n2t_dest_bits.png)
 - The ALU also output *zr*,*ng* bits.

<h2 id="18af6f320c794ce703ecd7e4c44fbf96"></h2>


### PC logic

![](../imgs/n2t_pc_logic.png)

 - Emites the address of the next instruction:
    - To start / restart the program's execution: PC=0
    - no jump:  PC++
    - goto :  PC=A
    - conditional goto:  if the condition is true  PC=A  else PC++ 


```
if (reset==1) PC=0
else
    load = f( jump bits, ALU control output ) 
    if (load==1) PC=A
    else        PC++ 
```

<h2 id="2d5b2381493e2e74b418ec4570b18f6c"></h2>


## 5.4 The Hack Computer

<h2 id="c366294d33d33ad8f41ff39d909e530f"></h2>


### Hack CPU Operation

The CPU executes the instruction according to the Hack Language specification

 - if the instruction includes D and A , the respective value are read from , and / ro write to , the CPU-resident D-register and A-register
    - D = D-A
 - if the instruction is `@x` , then x is stored in the A-register; this value is emitted by addressM
 - if the instrction's RHS includes M, this value is read from *imM*
    - M = M+1
 - if the instruction's LHS includes M, then the ALU output is emmited by *outM*, and the *writeM* bit is asserted.
 - if there is a jump
    - if (reset==0)
        - The CPU logic uses the instruction's jump bits, and the ALU output's to decide if there should be a jump
            - if there is a jump: PC is set to the value of the A-register 
            - else (no jump): PC++ 
        - The updated PC value is emitted by *pc*
    - if(reset==1)
        - PC is set to 0. *pc* emites 0 (cause a program restart)

<h2 id="fdef999b11b2cf3acbf0df16e8882100"></h2>


### Data Memory 

![](../imgs/n2t_hack_data_memory.png)

<h2 id="f94f42245da94b6b457000847ee3b0f7"></h2>


### Instruction Memory (ROM)

 - 32k ROM
 - To run a program on the Hack computer:
    - Load the program into the ROM
    - Press "reset"
    - The program starts running
 - Loading a program
    - Hardware implementation: plug-and-play ROM chips
        - i.e. 游戏卡带
    - Hardware simulation: 
        - programs are stored in text file
        - program loading is emulated by the built-in ROM chip
 - ROM interface
    - 15-bit address in ,  16-bit address out
    - the output of the ROM is always the contents of the register that is selected by the address input.
        - if I enter 17 into the address input, the contents of register number 17 comes out.
    - So, it makes a lot of sense to take this ROM and connect it to the program counterr.
        - because the PC always emits the address of the next instruction


<h2 id="d1ab5781342f30b0410b1955380662e6"></h2>


### Hack Computer implementatioin

![](../imgs/n2t_hack_compute_impl.png)

 - ROM - CPU
    - CPU PC 告诉 ROM 地址，ROM 输出 该地址的指令给CPU

 
![](../imgs/n2t_hack_compute_impl2.png)

 - CPU - RAM 
    - CPU 高速 RAM 地址， RAM 输出该地址内容给 CPU
    - 如果有写操作，CPU 同时提供 要写入的data

---

<h2 id="6aa600c7db11b3f439b312fdeaab651c"></h2>


## 5.5 Project Overview

 - Hack 并不是冯诺依曼架构的计算机。
 - 冯诺依曼架构 不区分 program ROM/data RAM , 你可以随时改变运行的程序。
 - 冯诺依曼架构 实现，一般是 增加一个 state 的输入， 使用有限状态机 来告诉CPU 这个周期做这件事，下个周期做 另外的事。



![](../imgs/n2t_hardware_project.png)




