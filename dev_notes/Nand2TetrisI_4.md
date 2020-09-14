...menustart

- [Week 4  Machine Language](#2176a3b0fd81007e70e0dab6fdf6b1e2)
    - [4.1 Overview](#d14ae9a46f5db30f2e3671e3260bad56)
        - [Mnemonics](#e7e3a5617750708cf2c2d2bd66835df3)
    - [4.2 Machine Languages : Elements](#7572d5e2c2cbff0b74dffe9eb8f946af)
        - [Machine Language : Operations](#90c98ad75c6e684802b11191a6ee1e48)
        - [Machine Language : Addressing](#b00adf6a12808f6581dab31c33b53648)
            - [Registers](#a9682ea50df45368189078864618a7cd)
            - [Addressing Modes](#011ddc58d58d2714f6ab1823a833a279)
            - [Input / Output](#6a8b3c75d2b148310a110bf194c67f26)
        - [Machine Language : Flow Control](#785a7f6de7d8cc20365a065384792be0)
    - [4.3 The Hack Computer and Machine Language](#bb308f6cd7b0bcbd8347e07247272ed7)
        - [Hack computer : hardware](#59440b54dcccb2580f829b511a3ab454)
        - [Hack computer: registers](#6bccf7c3f8c59b04ccbc9be6a8917a0f)
        - [The A-instruction](#7a47f762af8bb05b5c4b7663c365bbdc)
        - [The C-instruction](#2656df8b06102adadd0f4e8d28ca7d3b)
        - [为什么要划分 A/C 两套 指令？](#8bfeef857873fbe94ceeca536b8ba8df)
    - [4.4 Hack Language Specification](#07f3d75ea1037290fb379184f55486ac)
        - [The A-instruction: symbolic and binary syntax](#a74da8b3478acd4a7ca3b8c93f7a0d15)
        - [The C-instruction: symbolic and binary syntax](#fb409005082bcbc783a0b8c36745ee7a)
    - [4.5 Input/Output](#3ee61240a785681403c329e4721faa17)
        - [Hack Computer platform: Output](#88654d0d30b3eafe4fcc2c9fc29c0a7f)
        - [Hack computer platform: Input](#4bdb00d0e3d6c18d3f264fd18717ff21)
    - [4.6 Hack Programming, Part1](#a18eff3da7a07aee87a273f3fa131a52)
        - [Working with register and memory](#43ac21454f5d3b1ba15c3c9070c3574b)
        - [Hack program example: add two numbers](#e4e5a06fdd10851c3e7b7c0c5a04052c)
        - [How to terminate a program properly?](#fa7826a41e60188c3d9aa40c67875a2e)
        - [Built-in symbols](#c6485feeba4ed4c45bed624bd9d153e1)
    - [4.7: Hack Programming , Part 2](#433672a84dd80f224b715113f64d6b2f)
        - [Branching](#cec9f877aea82b580a4bd8292d6fd05b)
        - [Variables](#03df896fc71cd516fdcf44aa699c4933)
        - [Iterative processing](#f26bb1b6fe9c2cee3fb09973ed60da69)
    - [4.8 Hack Programming , Part 3](#0fbcaf38632f1b7a6eb86b99e1e1ea63)
        - [Pointers](#7bba5d01d3778f550d69f87dca50fc3f)

...menuend


<h2 id="2176a3b0fd81007e70e0dab6fdf6b1e2"></h2>


# Week 4  Machine Language

<h2 id="d14ae9a46f5db30f2e3671e3260bad56"></h2>


## 4.1 Overview

 - elements 
    - Operation : how are we going to specify the instructions ? 
    - Program Counter: how do we know which instruction to perform at any given stage and time ?
    - Addressing : have to tell the hardware what to operate on.


<h2 id="e7e3a5617750708cf2c2d2bd66835df3"></h2>


### Mnemonics

![](../imgs/n2t_mlang_mnemonics.png)

 - Interpretation 1: The "symbolic form" doesn't really exist but is just a convenient mnemonic to present machine language instructions to humans. 
 - Interpretation 2: We will allow humans to write machine language instructions using this "*assembly language*" and will have an "Assembler" program convert it to the bit-form.


<h2 id="7572d5e2c2cbff0b74dffe9eb8f946af"></h2>


## 4.2 Machine Languages : Elements

 - Specification of the Hardware/Software Interface
    - What are the supported operations ?
    - What do they operate on ?
    - How is the program controlled ?
 - Usually is close correspondence to actual Hardware Architecture
    - Not necessarily so
 - Cost-Performance Tradeoff
    - Silicon Area
    - Time to Complete Instruction

<h2 id="90c98ad75c6e684802b11191a6ee1e48"></h2>


### Machine Language : Operations 

 - Each machine language defines a set of operations
 - Those operations usually correspond to what's implemented in Hardware
    - Arithmetic Operations: add, subtract, ...
    - Logical Operations: and , or , ...
    - Flow Control : "goto instruction X", "if C ten goto instruction Y" 
 - Differences between machine languages 
    - Richness of the set of operations ( divisions? bulk copy? ... )
    - Data types ( width, floating point, ...  )

<h2 id="b00adf6a12808f6581dab31c33b53648"></h2>


### Machine Language : Addressing 

 - Accessing a memory location is exprensive
    - Need to supply a long address
    - Getting the memory contents into the CPU take time 
        - 从内存取值到CPU ，和CPU本身做算数运算相比，要花费非常多的时间
 - Solution: Memory Hierachy

![](../imgs/n2t_memory_hierarchy.png)

 - Faster access means smaller memory size

<h2 id="a9682ea50df45368189078864618a7cd"></h2>


#### Registers

 - CPUs usually contain a few , easily accessed "registers"
 - Their number and functions are are a central part of the machine language
 - Data Register
    - Add R1, R2
        - R1:10 , R2:20, result 30
 - Address Registers
    - Store R1, @A 
        - A:137 , means store R1's value (say 77)  to Mem[137]
        - Mem[137] = 77

<h2 id="011ddc58d58d2714f6ab1823a833a279"></h2>


#### Addressing Modes

 - Register 
    - Add R1, R2     // R2 <- R2 + R1
 - Direct 
    - Add R1, M[200]  // Mem[200] <- M[200] + R1
 - Indirect
    - Add R1, @A      // Mem[A] <- Mem[A] + R1
 - Immediate 
    - Add 73 , R1     // R1 <- R1 + 73

<h2 id="6a8b3c75d2b148310a110bf194c67f26"></h2>


#### Input / Output

 - Many types of Input and Output Devices
    - keyboard, mouse, camera , sensors, printers, screen, speaker, ...
 - CPU needs some kind of protocal to talk to each of them
    - Software "Drivers" know these protocols
 - One general method of interaction use "memory mapping"
    - Memory Location 12345 holds the direction of the last movement of the mouse
    - Memory Location 45678 is not a real memory location but a way to tell the printer which paper to use.
   
<h2 id="785a7f6de7d8cc20365a065384792be0"></h2>


### Machine Language : Flow Control 

 - Usually the CPU executes machine instructions in sequence
 - Sometimes we need to "jump" unconditionally to another location, e.g. loop
 - Sometimes we need to jump only if some condition is met

<h2 id="bb308f6cd7b0bcbd8347e07247272ed7"></h2>


## 4.3 The Hack Computer and Machine Language 

<h2 id="59440b54dcccb2580f829b511a3ab454"></h2>


### Hack computer : hardware 

![](../imgs/n2t_hack_compute_archi.png)

 - A 16-bit machine means  the atomic unit of operation is 16-bit. 
 - A 16-bit machine consising of :
    - Data memory (RAM): a sequence of 16-bit registers:
        - RAM[0], RAM[1], RAM[2] , ... 
    - Instruction memory(ROM): a sequence of 16-bit register:
        - ROM[0], ROM[1], ROM[2] , ...
    - Central Processing Unit (CPU): preforms 16-bit instrcutions
        - using mostly the ALU which resides inside the CPU.
    - Instruction bus / data bus / address bus

 - How do we control the computer ?
    - Software !
 - Hack machine language :
    - 16-bit A-instructions
    - 16-bit C-instructions

![](../imgs/n2t_hack_computer_archi2.png)

 - Control:
    - The ROM is loaded with a Hack program
    - The *reset* button is pushed
    - The program starts running

<h2 id="6bccf7c3f8c59b04ccbc9be6a8917a0f"></h2>


### Hack computer: registers 

![](../imgs/n2t_hack_computer_register.png)

 - The Hack machine language recognizes 3 registers :
    - D holds a 16-bit value : data
    - A holds a 16-bit value : data or address
    - M represents the 16-bit RAM register addressed by A


<h2 id="7a47f762af8bb05b5c4b7663c365bbdc"></h2>


### The A-instruction

 - Syntax : `@value`
 - Where *value* is either:
    - a non-negative decimal constant , or
    - a symbol referring to such a constant (later)
 - Semantics:
    - Sets the A register to *value*
    - Side effect: RAM[A] becomes the selected RAM register 
        - very important side effect , once set, 
        - it automatically selectes a particular register from the data memory , what we called M.
 - Example :  `@21`     
    - Effect:
        - Sets the A register to 21
        - RAM[21] becomes the selected RAM register 

 -  Usage example 

```
// Set RAM[100] to -1
@100   // A=100
M=-1   // RAM[100] = -1
```

 - so we always have to address the memory by using an A instruction. 

<h2 id="2656df8b06102adadd0f4e8d28ca7d3b"></h2>


### The C-instruction

 - the workhorse of the language 
 - that's where most of the action takes place and the syntax of this instruction consists of 3 different fields 
    - desination
    - computation
    - jump directive

```
dest = comp ; jump  // both dest and jump are optional
```

 - here is how it works:
    - First of all ,we compute something 
    - and then we do one of two things. 
        - we can either store the result of computation in some destination ,
        - or we can use this computation to decide if we want to jump to some other instruction in the program.

![](../imgs/n2t_c_instruction_comp.png)
        
dest = `null, M, D, MD, A, AM, AD, AMD`

 - we can store it simultaneously both in  M , and D

jump = `null, JGT, JEQ, JGE, JLT, JNE, JLE, JMP`

 - those 8 possible conditions , they always compare the result of the computation to **zero**.
 - Semantics:
    - Compute the value of *comp*
    - Store the result in *dest*
    - if the Boolean expression (comp *jump* 0) is true , 
        - jumps to execute the instruction stored in ROM[A].
 - Example:

```
// set the D regist to -1
D = -1

// set RAM[300] to the value of D-1
@300  // A=300
M=D-1

// if (D-1==0) jump to execute the instrction stored in ROM[56]
@56
D-1; JEQ  //  if (D-1 EQ 0) Jump to 56
```

<h2 id="8bfeef857873fbe94ceeca536b8ba8df"></h2>


### 为什么要划分 A/C 两套 指令？

 - Hack 是16bit 系统
 - 一条指令要处理 dest comp jump 3部分，没有足够 bit 处理 大的整数，或地址
 - 所以分出了单独的 A instruction， 可以处理15bit的整数 或 地址

<h2 id="07f3d75ea1037290fb379184f55486ac"></h2>


## 4.4 Hack Language Specification 

<h2 id="a74da8b3478acd4a7ca3b8c93f7a0d15"></h2>


### The A-instruction: symbolic and binary syntax

 - Symbolic syntax :
    - `@value` 
    - i.e. `@21`
 - Binary syntax:
    - `0value`
    - where the *value* is a 15-bit binary number
    - i.e.  ***0***00000000010101

<h2 id="fb409005082bcbc783a0b8c36745ee7a"></h2>


### The C-instruction: symbolic and binary syntax


 - Symbolic syntax :
    - `dest = comp ; jump ` 

--- 


![](../imgs/n2t_c_instruction_binary_syntax.png)

 - Binary syntax :
    - 
    - op code: 1 means a C-instruction, while 0 means an A-instruction
    - comp bit: to specify what computation to achieve. 
        - these are the control bits that will be sent later to the ALU  (ALU 不是6位 control bits 吗 ?)
        
![](../imgs/n2t_c_binary_comp.png)

 - impossible to compute with A and M !!

![](../imgs/n2t_c_binary_dest.png)

 - d1 means writing to A enable
 - d2 means D 
 - d3 means M 

![](../imgs/n2t_c_binary_jump.png)

 - j1 means less than 0
 - j2 means equals 0
 - j3 means great than 0

---

<h2 id="3ee61240a785681403c329e4721faa17"></h2>


## 4.5 Input/Output 

<h2 id="88654d0d30b3eafe4fcc2c9fc29c0a7f"></h2>


### Hack Computer platform: Output 

![](../imgs/n2t_screen_mem_map.png)

 - Screen Memroy Map
    - A designated memory area, dedicated to manager a display unit
    - The physical display is continuously *refreshed* from the memory map, many times per second
    - Output is effected by writing code that manipulates the screen memory map.

 -  Display Unit
    - ![](../imgs/n2t_display_unit_hack.png)
    - use a bit that represents the pixel in screen memory map
    - so we need 8k, 16-bit words : `8*1024*16 = 256*512 = 131072`
 - we are going to implement the screen memory map using a 8k chip called Screen.
 - To set pixel (row,col) on/off:
    1. word = Screen[ 32 \* row + col/16 ]   , or
        - word = RAM[ 16384 + 32 \* row + col/16 ]  // 假设 Screen base address 为16384
    2. Set the (col%16)th bit of work to 0 or 1.
    3. commit *word* to the RAM 

<h2 id="4bdb00d0e3d6c18d3f264fd18717ff21"></h2>


### Hack computer platform: Input

 - The physical keyboard is associated with a *keyboard memory map.*
    - like the scrren memory map, it is a part of RAM
 - The keyboard memory map is a single 16-bit register, which is called *keyboard*
 - When a key is pressed on the keyboard , the key's *scan code* appears in the *keyboard memory map*.

 - The Hack character set :
    - it is a subset of the keys that you have on you regular keyboard.

![](../imgs/n2t_hack_character_set.png)

 - To check which key is currently pressed: 
    - Probe the contents of the `keyboard` chip
    - In the Hack computer: probe the contents of RAM[24576].


<h2 id="a18eff3da7a07aee87a273f3fa131a52"></h2>


## 4.6 Hack Programming, Part1

<h2 id="43ac21454f5d3b1ba15c3c9070c3574b"></h2>


### Working with register and memory

 - Typical operations:

```
// D=10
@10
D = A

// D++
D = D+1

// D=RAM[17]
@17
D = M 

// RAM[17] = 10
@10
D=A
@17
M=D

// RAM[5] = RAM[3]
@3
D=M
@5
M=D
```

<h2 id="e4e5a06fdd10851c3e7b7c0c5a04052c"></h2>


### Hack program example: add two numbers

![](../imgs/n2t_hack_program_add2numbers.png)

<h2 id="fa7826a41e60188c3d9aa40c67875a2e"></h2>


### How to terminate a program properly?

 - Best practice:
    - To terminate a program safely , end it with an infinite loop.

```
M=D  // RAM[2] =D 

// above is privous code
@6
0; JMP
```

<h2 id="c6485feeba4ed4c45bed624bd9d153e1"></h2>


### Built-in symbols

 - The Hack assembly language features *built-in* symbols:

 - Virtual Registers
    - when the assembler or the translator sees a label like R3 , 
    - it will replace it with a number 3

symbol | value
--- | ---
R0  |  0
R1  |  1
R2  |  2
... | ...
R15 |  15

![](../imgs/n2t_virtual_register.png)

---

 - other built-in symbols

symbol | value
--- | ---
SCREEN | 16384
KBD  |  24576
SP | 0
LCL | 1
ARG | 2
THIS | 3
THAT | 4

 - the last 5 symbols are used in the implementation of Hack virtual machine , discussed in N2T part II.


<h2 id="433672a84dd80f224b715113f64d6b2f"></h2>


## 4.7: Hack Programming , Part 2

<h2 id="cec9f877aea82b580a4bd8292d6fd05b"></h2>


### Branching

![](../imgs/n2t_ml_branching.png)

 - 这个程序可以很好的工作，但是 如果没有这些 左边的这些行号， 这段代码就是个噩梦
 - Fortunately , we have a very nice feature in assembly languages , which called symbolic references. 
    - declare a label :  `( LABEL )`
    - `@LABEL` translates to `@n` , where *n* is the instruction number following the `(LABLE)` declaration.
 - Label declarations are not translated ( to machine language ). 
 - Each reference to a label is replaced with a reference to the instruction number following that label's declaration.

![](../imgs/n2t_symbolic_reference.png)

<h2 id="03df896fc71cd516fdcf44aa699c4933"></h2>


### Variables

 - in the lower level of the Hack machine language , we have only 1 variable type.
 - we have only 16-bit values to worry about. 
 - we use a single register to represent every one of our variables, if we want to create variables in our program.
 - Example: use temp to exchange the content of  R0 and R1

![](../imgs/n2t_variable.png)

 - here , `temp` don't have a corresponding label called temp.  how it works ?
 - Basically , we present the following pledge to the computer: 
    - Please goto the memory unit, find some available memory register , say register  *n* . 
    - so from now on, each occurance of `@temp` in the program will be translated into `@n`
 - Rules:
    - A reference to a symbol that has no corresponding lable declaration is treated as a reference to a variable.
    - Variable are allocated to the RAM from adderss 16 onward. 
        - in this example , we have only 1 variable, so it ends up being allocated to RAM 16.

![](../imgs/n2t_variable_rom.png)

 - let's take a look at our program.
 - This program has another very nice virtue, which is more subtle. 
 - This program is what is known as **relocatable code**.
    - I can take this program , and load it into memory **not necessary to address zero**. 
    - I can put it anywhere I want in memory as long as I remember what is the base address that they used for this program. 
 - Once we write this program carefully useing symbolic references, we don't have to worry about where they will be located in memory. 
    - We can write something called **loader** that takes care of this technical detail. 
 
<h2 id="f26bb1b6fe9c2cee3fb09973ed60da69"></h2>


### Iterative processing 

 - Example 
    - Compute 1+2+...+n
 - how to do ?
    1. write pseudo code 
    2. debug your pseudo code, ensure it works
    3. simply translating from pseudo code to machine language 

<h2 id="0fbcaf38632f1b7a6eb86b99e1e1ea63"></h2>


## 4.8 Hack Programming , Part 3

<h2 id="7bba5d01d3778f550d69f87dca50fc3f"></h2>


### Pointers 

```
// some pseudo code
for(i=0; i<n; i++) {
    arr[i] = -1    
}
// suppose that arr=100 , and n=10
```

 - when assembler translate this piece of pseudo code into machine language, the machine language no longer recognizes the array obstruction. 
 - As far as the machine language is concerned , the array is just a segment in memory of which we know the base address of this segment and the length of the array.


```
    // arr = 100
    @100
    D=A
    @arr  // 16 ,maybe
    M=D

    // n=10
    @10
    D=A
    @n      // 17
    M=D

    // i=0
    @i       // 18
    M=0

    // code continue 
(LOOP)
    // if (i==n) goto END
    @i
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    // RAM[arr+i] = -1
    @arr
    D=M
    @i
    A=D+M //RAM[arr+i] -- new M
    M=-1

    // i++
    @i
    M=M+1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP
```

 - Variables that store memory addresses like *arr* are called pointers. 
 - Hack pointer logic: 
    - whenever we have to access memory using a pointer , we need an instruction like `A=M` , something that comes from some memory register.  
