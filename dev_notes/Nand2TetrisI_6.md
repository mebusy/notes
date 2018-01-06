
# 6 Assembler

## 6.1  Assembly Language and Assemblers

### Basic Asserbler Logic

```
Repeat:
    Read the next Assembly language command
        Load R1,18
    Break it into the different fields it is composed of
        Load  R1  18
    Lookup the binary code for each field
        11001  01 000010010
    Combine these codes into a single machine language command
        1100101000010010
    Output this machine language command
Until end-of-file
```

 - very simple

### Symbols

 - Used for 
    - Labels  `JMP loop`
    - Variables   `Load R1, weight`
 - Assembler must replace names with address 
 - use a symbol table < symbol name , memory address >
    - variables:  if in symbol table, use it; otherwise, alloc a new memory , and put the address in symbol table 
    - lable : remember the address of the instruction next to the label declaration.
        - but what if the label is used before declaration ?


## 6.2 The Hack Assembly Language 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_hack_assembler_symbols.png)

## 6.3 The Assembly Proces -- Handling Instructions 

### Translating A-instructions 

 - `@value`
 - binary: 0xxxxxxxxxxxxxxx 
 - where *value* is either
    - a non-negative decimal constant , or 
    - a symbol referring to such a constant
 - Translation to binary
    - if *value* is a decimal constant , generate the 15-bit binary constant
    - if *value* is a symbol, later.

### Translating C-instructions 

 - `dest = comp ; jump`
 - 111 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3 
