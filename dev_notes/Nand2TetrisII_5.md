...menustart

 - [Compiler II: Code Generation](#4e3d80bb847df80512b978ab205afa7b)
     - [Unit 5.1: Code Generation](#94eb2461a577c6a4ba5ecb1f34c254c8)
     - [Unit 5.2: Handling Variables](#af37fa1db159e0c88611301daf974619)
         - [Variables](#03df896fc71cd516fdcf44aa699c4933)
         - [Symbol tables](#c2d6782cdc5b56e19beaaca9864ee842)
         - [Handling nested scoping](#68293a27f79e370f88514d80226ebd17)
     - [Unit 5.3: Handling Expressions](#59051b9e08782ffd6d31280501c339eb)

...menuend


<h2 id="4e3d80bb847df80512b978ab205afa7b"></h2>

# Compiler II: Code Generation

<h2 id="94eb2461a577c6a4ba5ecb1f34c254c8"></h2>

## Unit 5.1: Code Generation

 - when you set out to develop something complicated like a compiler , it always helps to try to simplify matters as mush as possible.
 - So I'm going to make some simplification observations. 
    - the first one is , **each class file is compiled separately**. 
        - Each Jack class file, just like each Java class file, is a separate and standalone compilation unit. 
        - So, the overall task of compiling a multi-class program has been reduced to the more sort of limited task of compiling one class at a time. 
        - So that's my first observation. 
    - the second one is based on going into the class itself. 
        - First of all, the class consists of two main modules. 
            - class declaration :  class / field / static  ... 
                - we have some preamble code that defines the class in some class level variables. 
            - zero or more subroutine called declarations
        - Now, the simplifying assumption is such that compilation can once again be viewed as two separate processes when you go down to the class level. 
            - First, you compile the class level code that we see here on the top. 
            - And then you compile each subroutine one at a time. 
            - These two compilation tasks are relatively separate and standalone. 
            - And, therefore, once again, the overall and rather formidable past of writing a compiler for multi-class program has been reduced to compiling one subroutine at a time. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compiler2_jack_observe.png)

 - Compilation challenges
    - Handling procedural code 
        - variables
        - expressions
        - flow of control
    - Handling objects
    - Handling arrays
 - The challenge: expressing the above semantics in the VM language

<h2 id="af37fa1db159e0c88611301daf974619"></h2>

## Unit 5.2: Handling Variables

 - example source code

```
sum = x * ( 1+rate )
```

 - translate to VM code (pseudo) 

```
push x
push 1
push rate
push +
push *
pop sum 
```

 - for now , let us focus only on the variables
 - we have sum, x, and rate
 - remember that the VM langauge does not have symbolic variables. 
    - it only has things like local , argument, this , that, and so on.
 - So in order to resolve this pseudo VM code into final executable VM code, I have to map these symbolic variables on what we called the virtual memory segments. 
 - In order to generate *actual* VM code, we must know (among other things):
    - Whether each variable is a *field,static,local,or argument*
    - Whether each variable is the *first,second,third...* variable of its kind

 - VM code (actual)
    - (making some arbitrary assumptions about the variable )

```
push argument 2
push constant 1
push static 0
add
call Math.multiply 2
pop local 3
```

<h2 id="03df896fc71cd516fdcf44aa699c4933"></h2>

### Variables

 - We have to handle:
    - class-level variables
        - field
        - static
    - subroutine-level variables
        - argument
        - local 
 - Every one of these variables has some properties:
    - name (identifier)
    - type (int, char, boolean, class name)
    - kind (field, static, local, argument)
    - scope (class level subroutine level)
 - Variable properties
    - Needed for code generation
    - Can be managed efficiently using a **symbol table**


<h2 id="c2d6782cdc5b56e19beaaca9864ee842"></h2>

### Symbol tables

```
class Point {
    field int x,y;
    static int pointCount;    
    ...
}
```

 name | type | kind | #
--- | --- | --- | ---
x | int | field | 0
y | int | field | 1
pointCount | int | static | 0


```
class Point {
    ...
    method int distance( Point other ) {
        var int dex, dy; 
        ...    
    }    
}
```

 - note `distance` is a class method, so it will always contain a `this` variable

 name | type | kind | #
--- | --- | --- | ---
this | Point | argument | 0 (argument 0 in every method)
other | Point | argument | 1
dx | int | local | 0 
dy | int | local | 1

 - Class-level symbol table:
    - can be reset each time we start compiling a new class
        - in Jack, or Java, or C# , classes are standalone compilation units
 - Subroutine-level symbol table:
    - can be reset each time we start compiling a new subroutine

 - It turns out that when you compiling anything in Jack , you always have to maintain just 2 symbol tables.
    - the class symbol talbe, and the current subroutine symbol table. 

 - Handling variable declarations:
    - field/static/var type varName; 
        - Add the variable and its properties to the symbol table
    - parameter list 
 - Handling variable usage:
    - example :  `let dx=x-other.getx();`
    - look up the variable in the subroutine-level symbol table; if not found, look it up in the class-level symbol table.
        - if not found, throw an error. 

 - so expression `let y=y + dy ` will be translated into VM code :

```
push this 1  // y
push local 1  // dy
add 
pop this 1   // y
```

<h2 id="68293a27f79e370f88514d80226ebd17"></h2>

### Handling nested scoping

 - not in Jack, but often in other language like Jave, C ...
 - Some languages feature unlimited nested scoping
 - Can be managed using a linked list of symbol tables.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_symbol_tables_4_nested_scoping.png)

 - Variable lookup: 
    - start in the 1st table
    - if not found , look up the next table, and so on.


<h2 id="59051b9e08782ffd6d31280501c339eb"></h2>

## Unit 5.3: Handling Expressions

### Parse tree

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2d_compile2_parse_tree.png)

 - prefix 
    - `* a + b c`
    - functional 
 - infix
    - `a * (b+c)`
    - human oriented , most source code are infix.
 - postfix 
    - `a b c + *`
    - stack oriented 
    - **this postfix notation is intimately related to our stack machine, because our stack language is also postfix.**
    - our target language , the VM language , is postfix. so the compiler has to translate from infix to postfix.

### Generating code for expressions: a two-stage approach

 1. source code -> parse tree  ( The XML file we output in project 10 is a parse tree )
 2. go throuth every node in this parse tree in a certain order , and then you generate the stack machine code.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compiler2_generate_code_2step.png)

 - 生成 parse tree 的代价是很大的，实践中一般不会这么做。

### Generating code for expressions: a one-stage approach

 - The following algorithm is  going to generate the VM code on the fly without having to create  the whole parse tree in the process.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compiler2_generate_code_1step.png)


## Unit 5.4: Handling Flow of Control

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compile2_handle_flow.png)

 - we have 5 statements
    - let, do, return are trivial statements to translate
    - translating `while` and `if` are far more challenging.

### Compiling if statements

```
if (expression) 
    statement1
else
    statement2
```

 - before I generate code for this statement, I would like to rewrite it using a flow chart.
    - the first thing to do is to take the expression and **negate** it. 
    - why to do this negation ? Because once you negate the expression in such a way , code generation becomes far simpler and tighter. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compile_if_flow_chart.png)  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compile_if_vm_code.png)

 - where are these labels (L1,L2) come from ?
    - the compiler generates these labels


### Compiling while statements

```
while (expression)
    statements
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compile_while_flow_chart.png)   ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_compile_while_vm_code.png)

### Some (minor) complications

 - A program typically contains multiple `if` and `while` statements.
     - we have to make sure that the compiler generates unique labels


## Unit 5.5: Handling Objects: Low-Level Aspects

### Handling local and argument variables 

 - local, argument
    - represent *local* and *argument* variables
    - located on the *stack*
 - Implementation
    - Base addresses: LCL and ARG
    - Managed by the VM implementation

### Handling object and array data

 - this, that
    - represent *object* and *array* data
    - localted on the *heap*
    - you may well have numerous objects and quite a few arrays.
 - Implementation
    - Base address: THIS and THAT
    - Set using `pointer 0 (this)` , `pointer 1 (that)`  
    - Managed by VM code.

### Accessing RAM data

 - suppose we wish to access RAM words 8000, 8001, 8002, ...

VM code (commands) | VM implementation (resulting effect)
--- | ---
push 8000  | sets THIS to 8000
pop pointer | 
push/pop this 0 | accessing RAM[8000]

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_5_access_RAM_data.png)





















