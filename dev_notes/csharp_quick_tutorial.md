
# C# vs .NET

- C# is a programming language
- .NET is a framework for building applications on Windows
    - .NET framework is not limited to c#. There are different languages that can target that framework and build applications using that framwork, e.g. F#, vb.net.
    - .NET framework contains 2 components
        1. CLR(Common Language Runtime)
        2. Class Library

# CLR (Common Language Runtime)

- When you compile your C# code, the result is what we called IL(intermediate language) code. It is independent of the computer on which it's running.
    - Now we need something that would translate the IL code into the native code on the machine that running the application. And that is the job of CLR.
- So CLR is essentially an application that is sitting in the memory whose job is to translate the IL code into the machine code,
    - and this process is called just-in-time compilation or JIT.

# Architecture of .NET Applications

- Class
    - building blocks
- Namespace
    - a way to organize these classes
    - a container of related classes
- Assembly (DLL or EXE)
    - as the namespaces grow we need a different way of partitioning an application.
    - an assembly is a container for related namespaces 
    - physically it's a file on the disk. It can either be an executable or a DLL.


# Fundamental

## ref vs out

Both ref and out parameter treated same at compile-time but different at run-time.

scenario |  ref | out
--- |--- | ---
before entering method |  must initialize | 
before returning  |  |  must initialize inside the mothod
when to use | when the callee also want to change the value of passed parameter | when a method return multiple values





