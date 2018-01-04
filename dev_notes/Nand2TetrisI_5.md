
# 5. Computer Architecture

## 5.1 Von Neumann Architecture

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_architexture_overall.png)

### Elements

 - CPU  
    - ALU
    - Register
 - Memoy
    - Program
    - Data

### Information Flows

 - control bus
 - data bus
 - address bus

### Buses

 - ALU loads information from the Data bus and manipulates it using the Control bits.
    - so it must connect to Data / Control bus
 - Register definitely connect to Data bus , and some time it used to specify some  address , so it connect to address bus as well
    - data / address are stored in registers
 - Memory is simular to Register 
    - There is an important thing, is the program instruction tell the system what to do, so we need to be able to actually take information from the next instruction , from the data output of program memory , and feed it into the control bus.   

---

## 5.2 The Fetch-Execute Cycle

 - we're going to talk about the very basic thing that a compute does, which is
    - execute one instruction after the other.
 - THe basic CPU loop
    - **Fetch** an instruction from the Program memory
    - **Execute** it

### Fetching

 -  Fetching
    - Put the location of the next instrution into the "address" of the program memory
    - Get the instruction code itself by reading the memory contents at that location
 - How do we actually go about putting the address of the next instruction  into the address input of the programm memory ?
    - we're going to have to put it somewhere , and that's going to be into some register, and that is usually called the Program Counter. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_the_PC.png)
    - The output of the PC , feeds into the address specification of our program memory,
    - and then the *out* of the program memory , comes the actual code of instructions , that we need to execute.
 
### Executing 
 
 - Executing the operation involves also accessing registers and/or data memory

### Fetch-Execute Clash 

 - There is a fact that we really have a clash between the fetch cycle and the execute cycle.
    - both the program and the data reside in memory 
    - In the fetch cycle , basically we need to get from the program memory the next instruction 
        - so we need to put into the address of the memory , the address of the next instruction and get the instruction output.  
    - On the other hand, in the execute cycle, we need to access data that also resides in memory.
        - we need to put into the address of the memory , the address of te data piece that we want to operate on
    - that is , the fetch part of the cycle reads from the program memory, and the execute part reads from data memory.
    - and because we have a single memory , that is a clash. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_fetch-execute_clash.png)


## 
 - How to solve it ?
    - basically we are going to do one after the other, that is the usual way. 
    - There is going to be a multiplexer that feeds into the address of the memory. 
    - In the first part of the cycle , the fetch cycle, we're going to actually set the multiplexer to plug into the address input of the memory, the program counter that is the location of the next instruction. 
    - while in the execute cycle, the multiplexer will actually set the memory to actually point into the data address that we need to access. 
 - so now ,in fetch cycle, we get the instruction , in executing cycle  we get the data.
    - but how we know the acutal instruction when we are in executing cycle?
    - we need at first store the instruction to a **instruction register**.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_instruction_register.png)

 - This is the usual way it's done. Now there is a shortcut.
 - Simple solution: Harvard Architecture
    - Variant of von Neumann Architecture
    - Keep Program and Data in 2 separate memory modules
        - each module has its own address.
    - Complication avoided.








