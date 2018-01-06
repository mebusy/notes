
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


