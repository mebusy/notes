
# Chapter 8 : Code Generation

intermediate representation (IR)

The target pro­gram must preserve the semantic meaning of the source program and be of high quality; that is, it must make effective use of the available resources of the target machine. Moreover, the code generator itself must run efficiently.

The challenge is that, mathematically, the problem of generating an optimal target program for a given source program is undecidable; many of the subprob­lems encountered in code generation such as register allocation are computa­tionally intractable. In practice, we must be content with heuristic （启发式） techniques that generate good, but not necessarily optimal, code. Fortunately, heuristics have matured enough that a carefully designed code generator can produce code that is several times faster than code produced by a naive one.

Compilers that need to produce efficient target programs, include an op­timization phase prior to code generation. The optimizer maps the IR into IR from which more efficient code can be generated. In general, the code­ optimization and code-generation phases of a compiler, often referred to as the back end, may make multiple passes over the IR before generating the target program. Code optimization is discussed in detail in Chapter 9. The tech­niques presented in this chapter can be used whether or not an optimization phase occurs before code generation.

A code generator has three primary tasks: 

 - instruction selection
 - register allqcation and assignment
 - instruction ordering

The importance of these tasks is outlined in Section 8.1. 

 - Instruction selection involves choosing appro­priate target-machine instructions to implement the IR statements. 
 - Register allocation and assignment involves deciding what values to keep in which reg­isters. 
 - Instruction ordering involves deciding in what order to schedule the execution of instructions.

This chapter presents algorithms that code generators can use to trans­late the IR into a sequence of target language instructions for simple register machines. The algorithms will be illustrated by using the machine model in Sec­tion 8.2. Chapter 10 covers the problem of code generation for complex modern machines that support a great deal of parallelism within a single instruction.

After discussing the broad issues in the design of a code generator, we show what kind of target code a compiler needs to generate to support the abstrac­tions embodied in a typical source language. In Section 8.3, we outline imple­mentations of static and stack allocation of data areas, and show how names in the IR can be converted into addresses in the target code.

Many code generators partition IR instructions into "basic blocks," which consist of sequences of instructions that are always executed together. The partitioning of the IR into basic blocks is the subject of Section 8.4. The following section presents simple local transformations that can be used to transform basic blocks into modified basic blocks from which more efficient code can be generated. These transformations are a rudimentary form of code optimization, although the deeper theory of code optimization will not be taken up until Chapter 9. An example of a useful, local transformation is the discovery of common subexpressions at the level of intermediate code and the resultant replacement of arithmetic operations by simpler copy operations.

Section 8.6 presents a simple code-generation algorithm that generates code for each statement in turn, keeping operands in registers as long as possible. The output of this kind of code generator can be readily improved by peephole optimization techniques such as those discussed in the following Section 8.7.

The remaining sections explore instruction selection and register allocation.

---

## 8.1 Issues in the Desjgn of a Code Generator

While the details are dependent on the specifics of the intermediate represen­tation, the target language, and the run-time system, tasks such as instruction selection, register allocation and assignment, and instruction ordering are en­countered in the design of almost all code generators.

The most important criterion for a code generator is that it produce cor­rect code. Correctness takes on special significance because of the number of special cases that a code generator might face. Given the premium on correct­ness, designing a code generator so it can be easily implemented, tested, and maintained is an important design goal.

---

### 8.1.1 Input to the Code Generator

The input to the code generator is the intermediate representation of the source program produced by the front end, along with information in the symbol table that is used to determine the run-time addresses of the data objects denoted by the names in the IR.

The many choices for the IR include 

 - three-address representations such as quadruples, triples, indirect triples; 
 - virtual machine representations such as bytecodes and stack-machine code; 
 - linear representations such as postfix no­tation; 
 - and graphical representations such as syntax trees and DAG's. 

Many of the algorithms in this chapter are couched in terms of the representations considered in Chapter 6: three-address code, trees, and DAG's. 

The techniques we discuss can be applied, however, to the other intermediate representations as well.

In this chapter, we assume that the front end has scanned, parsed, and translated the source program into a relatively low-level IR, so that the values of the names appearing in the IR can be represented by quantities that the target machine can directly manipulate, such as integers and floating-point numbers. We also assume that all syntactic and static semantic errors have been detected, that the necessary type checking has taken place, and that type­ conversion operators have been inserted wherever necessary. The code generator can therefore proceed on the assumption that its input is free of these kinds of errors.

---

### 8.1.2 The Target Program

The most common target-machine architectures are RISC (reduced instruction set computer), CISC (complex instruction set computer), and stack based.

A RISC machine typically has many registers, three-address instructions, simple addressing modes, and a relatively simple instruction-set architecture. 

In contrast, a CISC machine typically has few registers, two-address instruc­tions, a variety of addressing modes, several register classes, variable-length instructions, and instructions with side effects.

In a stack-based machine, operations are done by pushing operands onto a stack and then performing the operations on the operands at the top of the stack. To achieve high performance the top of the stack is typically kept in registers. Stack-based machines almost disappeared because it was felt that the stack organization was too limiting and required too many swap and copy operations.

However, stack-based architectures were revived with the introduction of the Java Virtual Machine (JVM) . The JVM is a software interpreter for Java bytecodes, an intermediate language produced by Java compilers. The interpreter provides software compatibility across multiple platforms, a major factor in the success of Java.

To overcome the high performance penalty of interpretation, which can be on the order of a factor of 10, just-in-time (JIT) Java compilers have been created. These JIT compilers translate bytecodes during runtime to the native hardware instruction set of the target machine. Another approach to improving Java performance is to build a compiler that compiles directly into the machine instructions of the target machine, bypassing the Java bytecodes entirely.

Producing an absolute machine-language program as output has the ad­vantage that it can be placed in a fixed location in memory and immediately executed. Programs can be compiled and executed quickly.

Producing a relocatable machine-language program (often called an object module) as output allows subprograms to be compiled separately. A set of relocatable object modules can be linked together and loaded for execution by a linking loader. Although we must pay the added expense of linking and loading if we produce relocatable object modules, we gain a great deal of flexibility in being able to compile subroutines separately and to call other previously compiled programs from an object module. If the target machine does not handle relocation automatically, the compiler must provide explicit relocation information to the loader to link the separately compiled program modules.

Producing an assembly-language program as output makes the process of code generation somewhat easier. We can generate symbolic instructions and use the macro facilities of the assembler to help generate code. The price paid is the assembly step after code generation.

In this chapter, we shall use a very simple RISC-like computer as our target machine. We add to it some CISC-like addressing modes so that we can also discuss code-generation techniques for CISC machines. For readability, we use assembly code as the target language . As long as addresses can be calculated from offsets and other information stored in the symbol table, the code gener­ator can produce relocatable or absolute addresses for names just as easily as symbolic addresses.

---

### 8.1.3 Instruction Selection





