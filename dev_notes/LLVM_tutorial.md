
# LLVM Tutorial: Table of Contents

# Implementing a Language with LLVM

## 1. Tutorial Introduction and the Lexer

### 1.2. The Basic Language

Kaleidoscope is a procedural language that allows you to 

 - define functions, 
 - use conditionals, 
 - math, etc. 

Over the course of the tutorial, we’ll extend Kaleidoscope to support the 

 - if/then/else construct, 
 - a for loop, 
 - user defined operators, 
 - JIT compilation with a simple command line interface, etc.

Because we want to keep things simple, the only datatype in Kaleidoscope is a 64-bit floating point type (aka ‘double’ in C parlance). 

As such, all values are implicitly double precision and the language doesn’t require type declarations. This gives the language a very nice and simple syntax. For example, the following simple example computes Fibonacci numbers:


### 1.3. The Lexer

