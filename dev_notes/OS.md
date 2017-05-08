
# Operating Systems

https://cs162.eecs.berkeley.edu/

https://people.eecs.berkeley.edu/~kubitron/cs162/

# Lecture 2: Histroy 

## Virtual Machine Abstraction


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_vm_abstraction.png)

 - Software Engineering Problem:
    - Turn hardware/software quirks => what programmers want/need
    - Optimize for convenience, utilization, security, reliability, etc…
 - For Any OS area (e.g. file systems, virtual memory, networking, scheduling):
    - What’s the hardware interface? (physical reality)
    - What’s the application interface? (nicer abstraction)

## Protecting Processes from Each Other

 - Problem: Run multiple applications in such a way that they are protected from one another
 - Goal:
    - Keep User Programs from Crashing OS
    - Keep User Programs from Crashing each other
    - [Keep Parts of OS from crashing other parts?]
 - (Some of the required) Mechanisms:
    - Address Translation
    - Dual Mode Operation
 - Simple Policy:
    - Programs are not allowed to read/write memory of other Programs or of Operating System 


## Address Translation

 - Address Space
    - A group of memory addresses usable by something 
    - Each program (process) and kernel has potentially different address spaces.
 - Address Translation:
    - Translate from Virtual Addresses (emitted by CPU) into Physical Addresses (of memory)
    - Mapping often performed in Hardware by Memory Management Unit (MMU)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_address_translation.png)


### Example of Address Translation

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_example_address_translation.png)

here program 1 has its address space. In the code segment here those addresses which might be from 0 to some point 3F433F whatever, get translated to this part of the DRAM. 

The set of addresses that are translated to in the physical space don't overlap. 

There is a simple problem here:  that mapping need s to somehow be out of the realm of changable by the process.  


## The other half of protection: Dual Mode Operation

 - **Hardware** provides at least two modes:
    - “Kernel” mode (or “supervisor” or “protected”)
    - “User” mode: Normal programs executed 
 - Some instructions/ops prohibited in user mode:
    - Example: cannot modify page tables in user mod
        - Attempt to modify => Exception generated
 - Transitions from user mode to kernel mode:
    - System Calls, Interrupts, Other exceptions

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_histroy_dual_mode_operation.png)

## UNIX System Structure

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_unix_system_structure.png)

## a quick tour of OS Structures

### Operating Systems Components (What are the pieces of the OS)

 - Process Management
 - Main-Memory Management
 - I/O System management
 - File Management
 - Networking
 - User Interfaces


### Operating System Services (What things does the OS do?)

 - Services that (more-or-less) map onto components
    - Program execution
        - How do you execute concurrent sequences of instructions?
    - I/O operations
        - Standardized interfaces to extremely diverse devices
    - File system manipulation
        - How do you read/write/preserve files?
        - Looming concern: How do you even find files???
    - Communications
        - Networking protocols/Interface with CyberSpace?
 - Cross-cutting capabilities
    - Error detection & recovery
    - Resource allocation
    - Accounting
    - Protection

### System Calls (What is the API)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_system_calls.png)

### Operating Systems Structure (What is the organizational Principle?)

 - Simple
    - Only one or two levels of code
 - Layered
    - Lower levels independent of upper levels
 - Microkernel
    - OS built from many user-level processes
 - Modular
    - Core kernel with Dynamically loadable modules


---

# Lecture3 : Concurrency: Processes and Threads

## Concurrency

 - “Thread” of execution
    - Independent Fetch/Decode/Execute loop
    - Operating in some Address space
 - Uniprogramming: one thread at a time
    - **MS/DOS, early Macintosh, Batch processing**
    - Easier for operating system builder
    - Get rid concurrency by defining it away
    - Does this make sense for personal computers?
 - Multiprogramming: more than one thread at a time
    - **Multics, UNIX/Linux, OS/2, Windows NT/2000/XP, Mac OS X** 
    - Often called “multitasking”, but multitasking has other meanings (talk about this later)

## The Basic Problem of Concurrency

 - The basic problem of concurrency involves resources:
    - Hardware: single CPU, single DRAM, single I/O devices
    - Multiprogramming API: users think they have exclusive access to shared resources
 - OS Has to coordinate all activity
    - Multiple users, I/O interrupts, …
    - How can it keep all these things straight?
 - Basic Idea: Use Virtual Machine abstraction
    - Decompose hard problem into simpler ones
    - Abstract the notion of an executing program
    - Then, worry about multiplexing these abstract machines
 - Dijkstra did this for the “THE system”
    - Few thousand lines vs 1 million lines in OS 360 (1K bugs)

## How can we give the illusion of multiple processors?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_illusion_of_multiple_processors.png)

 - Assume a single processor. How do we provide the illusion of multiple processors?
    - Multiplex in time!
 - Each virtual “CPU” needs a structure to hold:
    - Program Counter (PC), Stack Pointer (SP)
    - Registers (Integer, Floating point, others…?)
 - How switch from one CPU to the next?
    - Save PC, SP, and registers in current state block
    - Load PC, SP, and registers from new state block
 - What triggers switch?
    - Timer, voluntary yield, I/O, other things

## Properties of this simple multiprogramming technique
 
 - All virtual CPUs share same non-CPU resources
    - I/O devices the same
    - Memory the same
 - Consequence of sharing:
    - Each thread can access the data of every other thread (good for sharing, bad for protection)
    - Threads can share instructions (good for sharing, bad for protection)
    - Can threads overwrite OS functions? 
 - This (unprotected) model common in:
    - Embedded applications
    - Windows 3.1/Machintosh (switch only with yield)
    - Windows 95—ME? (switch with both yield and timer)

## Modern Technique: SMT/Hyperthreading


 - Hardware technique 
    - Exploit natural properties of superscalar processors to provide illusion of multiple processors
    - Higher utilization of processor resources 
 - Can schedule each thread as if were separate CPU
    - However, not linear speedup!
    - If have multiprocessor, should schedule each processor first
 - Original technique called “Simultaneous Multithreading”
    - Alpha, SPARC, Pentium 4 (“Hyperthreading”), Power 5


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_hyperthreading.png)

 - modern processors all execute more than one thing at a time
    - more than 1 instruction on a cycle
 - what the picture is showing you here is 
    - time is going down
    - each slot(row?) represents a cycle ,each column represents a functional unit 
        - so there are 3 functional units 
    - the 1st cycle 
        - a) functional unit 1 and 3  are busy (colored), function unit 2 is not busy
        - b) you might put tow of these together , and each of them has idle slots.
        - c) you put two threads togethter into the same pipline and they share the slots as a result you end up filling up more the empty slots.  
            - this means that the hardware itself has got 2 sets of registers , 2 Program Counters, 2 branch predictores , and 2 of a few other things ...

## How to protect threads from one another?

Need three important things:

 1. Protection of memory
    - Every task does not have access to all memory
 2. Protection of I/O devices
    - Every task does not have access to every device
 3. Protection of Access to Processor: Preemptive switching from task to task 
    - Use of timer
    - Must not be possible to disable timer from usercode


## Recall: Program’s Address Space

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_program_address_space.png)








     

