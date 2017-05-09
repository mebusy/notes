
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

 - here's a zero up to whatever the max address 
    - we have the text area which is where the instructions are
    - we have data which is static data that's allocated at the beginning of the program
    - heap : dynamically allocated memory 
    - stack: local variables 
 - Address space => the set of accessible addresses + state associated with them: 
    - For a 32-bit processor there are 2³² = 4 billion addresses
 - What happens when you read or write to an address?  
    - Perhaps Nothing
        - you write data in the middle of an empty space , usually it will cause an segmentation fault because it is not real memory. 
    - Perhaps acts like regular memory
    - Perhaps ignores writes
        - you write data in the section called read-only , eg. the text segment , or they cause another segmentation fault.
    - Perhaps causes I/O operation
        - (Memory-mapped I/O)
    - Perhaps causes exception (fault)


## Traditional UNIX Process

 - **Process: Operating system abstraction to represent what is needed to run a single program**
    - Often called a “HeavyWeight Process”
    - Formally: a single, sequential stream of execution in its own address space
 - Two parts:
    - Sequential Program Execution Stream
        - Code executed as a single, sequential stream of execution
        - Includes State of CPU registers
    - Protected Resources:
        - Main Memory State (contents of Address Space)
        - I/O state (i.e. file descriptors)
 - **Important: There is no concurrency in a heavyweight process**
    - which means there's only one thread

## How do we multiplex processes?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_process_control_block.png)

 - The current state of process held in a process control block (PCB):
    - This is a “snapshot” of the execution and protection environment
    - Only one PCB active at a time
    - not quite multi-core world yet, we only have one process can be running at a time in this mode because we only have 1 cpu.
 - Give out CPU time to different processes (**Scheduling**):
    - Only one process “running” at a time
    - Give more time to important processes
 - Give pieces of resources to different processes (**Protection**):
    - Controlled access to non-CPU resources
    - Sample mechanisms: 
        - Memory Mapping: Give each process their own address space
        - Kernel/User duality: Arbitrary multiplexing of I/O through system calls


## CPU Switch From Process to Process

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_cpu_context_switch.png)

 - This is also called a “context switch”
 - executing instractuions of p₀,p₁  do not overlap because only 1 cpu
 - Code executed in kernel above is overhead
    - no process is making useful progress while OS is saving / reloading PCB, etc...
    - Overhead sets minimum practical switching time
    - Less overhead with SMT/hyperthreading, but… contention for resources instead
        - you could actually have 2 processes loaded at the same time ,and that overhead switching in the hardware , and there is no overhead they're pretty much because the hardware is doing it for you. 

## Diagram of Process State

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_diagram_of_process_state.png)

 - As a process executes, it changes state
    - new: The process is being created
    - The process is waiting to run
    - Instructions are being executed 
    - Process waiting for some event to occur
    - The process has finished execution


## Process Scheduling

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_process_scheduling.png)

 - PCBs move from queue to queue as they change state
    - Decisions about which order to remove from queues are **Scheduling** decisions
    - Many algorithms possible (few weeks from now)

## What does it take to create a process?

 - Must construct new PCB 
    - Inexpensive
 - Must set up new page tables for address space
    - More expensive
 - Copy data from parent process? (Unix fork() )
    - Semantics of Unix fork() are that the child process gets a complete copy of the parent memory and I/O state
    - Originally **very expensive**
    - Much less expensive with “copy on write”
 - Copy I/O state (file handles, etc)
    - Medium expense

## Process =? Program 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_process_vs_program.png)

 - More to a process than just a program:
    - Program is just part of the process state
    - I run emacs on lectures.txt, you run it on homework.java – Same program, different processes
 - Less to a process than a program:
    - A program can invoke more than one process
    - cc starts up cpp, cc1, cc2, as, and ld

## Multiple Processes Collaborate on a Task

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_processes_collaborate_on_a_task.png)

 - this is kind of the beginnings of parallelism 
    - there are 3 processes they want to collaborate together , they got to talk to each other.
 - High Creation/memory Overhead
 - (Relatively) High Context-Switch Overhead
 - Need Communication mechanism:
    - Separate Address Spaces Isolates Processes
        - it's not like you can write in the memory of one process and read it in the memory of the other 
    - Shared-Memory Mapping ( one way to talk to each other )
        - Accomplished by mapping addresses to common DRAM
        - Read and Write through memory
    - Message Passing ( another one )
        - send() and receive() messages
        - Works across network

### Shared Memory Communication

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_shared_memory_communication.png)

 - Communication occurs by “simply” reading/writing to shared address page
    - Really low overhead communication
    - Introduces complex synchronization problems 

### Inter-process Communication (IPC)

 - Mechanism for processes to communicate and to synchronize their actions
 - Message system – processes communicate with each other without resorting to shared variables
 - IPC facility provides two operations:
    - send(message) – message size fixed or variable 
    - receive(message)
 - If P and Q wish to communicate, they need to:
    - establish a communication link between them
    - exchange messages via send/receive
 - Implementation of communication link
    - physical (e.g., shared memory, hardware bus, systcall/trap)
    - logical (e.g., logical properties)


## Modern “Lightweight” Process with Threads

A modern process has more than one thread. The idea is the process still has one address space , but it has multiple threads in it. 
 
 - Thread: a sequential execution stream within process (Sometimes called a “Lightweight process”)
    - Process still contains a single Address Space
    - No protection between threads
    - threads in the same process all share the same memory
 - Multithreading: a single program made up of a number of different concurrent activities 
    - Sometimes called multitasking, as in Ada…
 - Why separate the concept of a thread from that of a process?
    - Discuss the “thread” part of a process (concurrency)
    - Separate from the “address space” (Protection)
    - Heavyweight Process  ==  Process with one thread 

### Single and Multithreaded Processes

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_single_multithreaded_process.png)

 - each thread has its own registers and stack. 
 - Threads encapsulate concurrency: “Active” component
 - Address spaces encapsulate protection: “Passive” part
    - Keeps buggy program from trashing the system
 - Why have multiple threads per address space?
    
### Examples of multithreaded programs

 - Embedded systems 
    - Elevators, Planes, Medical systems, Wristwatches
    - Single Program, concurrent operations
 - Most modern OS kernels
    - Internally concurrent because have to deal with concurrent requests by multiple users
    - But no protection needed within kernel
 - Database Servers
    - Access to shared data by many concurrent users
    - Also background utility processing must be done
 - Network Servers
    - Concurrent requests from network
    - Again, single program, multiple concurrent operations
    - File server, Web server, and airline reservation systems
 - Parallel Programming (More than one physical CPU)
    - Split program into multiple threads for parallelism
    - This is called Multiprocessing
 - Some multiprocessors are actually uniprogrammed:
    - Multiple threads in one address space but one program at a time


## Thread State

 - State shared by all threads in process/addr space
    - Contents of memory (global variables, heap)
    - I/O state (file system, network connections, etc)
 - State “private” to each thread
    - Kept in TCB -- Thread Control Block
    - CPU registers (including, program counter)
    - Execution stack – what is this?
 - Execution Stack
    - Parameters, Temporary variables
    - return PCs are kept while called procedures are executing

### Execution Stack Example

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_execution_stack_example.png)

 - Stack holds temporary results
 - Permits recursive execution
 - Crucial to modern languages

## Summary

 - Processes have two parts
    - Threads (Concurrency)
    - Address Spaces (Protection)
 - Concurrency accomplished by multiplexing CPU Time:
    - Unloading current thread (PC, registers)
    - Loading new thread (PC, registers)
    - Such context switching may be voluntary (yield(), I/O operations) or involuntary (timer, other interrupts)
 - Protection accomplished restricting access:
    - Memory mapping isolates processes from each other
    - Dual-mode for isolating I/O, other resources
 - Book talks about processes 
    - When this concerns concurrency, really talking about thread portion of a process
    - When this concerns protection, talking about address space portion of a process

# Lecture 4: Thread Dispatching 

## MIPS: Software conventions for Registers

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/os_MIPS_software_conventions_for_register.png)











     

