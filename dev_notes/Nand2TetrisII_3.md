...menustart

 - [3 Hight Level Language](#64f2c0effea1a3786937de24c80cfa13)
     - [3.1 The Jack Language in a nutshell](#0f52f783c1d62455885bcc16f6a696cf)
         - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
     - [3.2 Object-Based Programming](#56a104167bb72e560b1f54bc8e9ee773)
         - [OO programming: building a class](#eb8fed3241e22b795da243323dd0d9df)
         - [OO programming : object representation](#f42bc11c828b9e7b453ba5a2ea1dbc2f)

...menuend


<h2 id="64f2c0effea1a3786937de24c80cfa13"></h2>

# 3 Hight Level Language 

<h2 id="0f52f783c1d62455885bcc16f6a696cf"></h2>

## 3.1 The Jack Language in a nutshell

 - A simple, Java-like language 
 - Object-based , no inheritance
 - Multi-purpose
 - Lends itself to interactive apps
 - Can be learned in about an hour


<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>

### Example 

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_example_1.png)
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_example_2.png)
    - entry:  Main.main
    - flow of control:
        - if / if ... else
        - while
        - do
    - Array :
        - Array is implemented as part of the stardard class library
        - Jack arrays are not typed, they can contain any value of any type
    - OS services:
        - Keyboard.readInt
        - Output.printString
        - Output.printInt
        - More...
    - Jack data types:
        - Primitive:
            - int
            - char
            - boolean
        - Class types:
            - OS: Array, String, ...
            - Program extensions : as needed

<h2 id="56a104167bb72e560b1f54bc8e9ee773"></h2>

## 3.2 Object-Based Programming

 - Jack 的基本数据类型，数值方面的，只有int ，所有有必要扩充一下数值类型，比如 rational number.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_factionAPI.png)

<h2 id="eb8fed3241e22b795da243323dd0d9df"></h2>

### OO programming: building a class

 - filed, aka property, aka member variable
 - In Jack the only way to access field values from outside the class is through *accessor* methods.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_oop_1.png)

 - functions are equivalent to static methods in JAVA. 
 - Jack constructor must return  the base address or must return an object of the type( i.e. this)
    - Java construtors do exactly the same but they do it implicity. You don't have to say `return this`  in Java but actually , compiler will do it. 
 - Jack method must call `return`  as well

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_oop_2.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/v2t_jack_dispose.png)

 - dispose method is implemented using a call to the host OS -- `Memory.deAlloc(this)`
    - which takes an address in memory and disposes the memory block 
    - the memory resouces will be freed.
 - GC
    - Jack has no garbage collection
    - Objects must be disposed explicitly
    - every jack class with `at least` one constructor must have a dispose() method.


<h2 id="f42bc11c828b9e7b453ba5a2ea1dbc2f"></h2>

### OO programming : object representation 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_2.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_3.png)


## 3.3 List Processing 

 - List definition
    - the atom `null` , or
    - an atom , followed by a list 
 - Notation: `(atom, list)`
 - Examples:

```lisp
null
(3, (5,null)) 
(2, (3, (5,null)))
```

 - so the list is kind of a linked list, but it is indeed  one object 
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_list_example.png)
 - The list (2, (3, (5,null)))  commonly abbreviated as (2,3,5)
 - so how to create and manipulate such collection objects.

 - List API (partial)

```
/** Represents a linked list of integers */ 
class List {
    constructor List new(int car, List cdr) 
    method void print() {
    method void dispose() {
}
```

### List processing: creation

```
class List {
    field int data ;
    field List next ;
    
    constructor List new(int car, List cdr) {
        let data = car ; 
        let next = cdr ; 
        return this ; 
    }    
}
```


```
var list v;
let v = List.new(5,null) ;
let v = List.new(3,v) ;
let v = List.new(2,v) ;
```

### List processing: access

```
class List {
    field int data ;
    field List next ;
    
    method void print() {
        var List current ;
        let current = this ;
        whiel ( ~(current == null) ) {
            do Outout.printInt( current.getData() ) ;
            do Outout.printChar(32) ;   
            do current = current.getNext() ;    
        }    
        return ;
    }
    ...
}
```

```
var list v ; 
...
do v.print();
```

### List processing: recursive access

```
class List {
    field int data ;
    field List next ;
    
    method void dispose() {
        if (~(next==null)) {
            do next.dispose() ;    
        }    
        do Memory.deAlloc(this) ;
        return ;
    }
}
```

### List representation

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_list_representation.png)

 - who makes the magic work ?
    - high-level: the constructor
    - low-level: when compiling the constructor, the compiler plants calls to OS routines that find , and allocate , avaiable memory space for the new object.

## 3.4 Jack Language Specification: Syntax

 - Syntax elements
    - white space / comments
    - keywords
        - class, constructor, method , function  // program components
        - int , boolean , char, void     // primitive types
        - var, static , field     // variable declarations
        - let, do , if , else, while ,return   // statements
            - var, let, do make writing the compiler easy. 
        - true, false, null,      // constant values
        - this 
    - Symbols   
        - (),{},[] 
        - `,` , `;` , `=` 
        - `.`  (class membership) 
        - + - \* / & `|` ~ < > Operators.
    - Constants
        - integer constant
            - **must be positive**
            - negtive integers like `-13` are not constants, but rather expressions
        - string constant     "xxx"
        - boolean constant 
        - null
    - Identifiers


## 3.5 Jack Language Specification: Data Types

 - Primitive types
    - int
        - non-negative  , 16-bit, 0~32726
    - boolean
        - true / false
    - char 
        - Unicode character
 - Class types
    - OS types: String, Array
    - User-defined types: Fraction, List, .. 


### Type conversions 

 - characters and integers are converted into each other , as needed:
    - `var char c;  let c=65;   // 'A' `
    - `var String s; let s="A"; let c=s.charAt(0); `
    - Note that the idiom `c='A'` is **NOT** supported by the Jack Language. 
 - An integer can be assigned to a reference variables, in which case it is treated as a memory address
    - `var Array arr;   let arr=5000; `
    - 很危险，但对编写OS可以带来很大帮助
 - An object can be converted into an Array, and vice versa

```
var Fraction x; 
var Array arr ;
let arr = Array.new(2);
let arr[0] = 2; let arr[1] = 5 ;
// set x to the base address of the memory block 
// representing the array[2,5]
let x=  arr ; 
do x.print()   // 2/5
```


## 3.6  Jack Language Specification: Classes

 - Each class `Foo` is stored in a separate Foo.jack file
 - The class name's 1st character must be an uppercase letter
 - syntactics requirement 
    - field and static variables , if they exists, must appear before the subroutine declarations. 

```
class Foo {
    field variable declarations    
    static variable declarations    
    subroutine declarations
}
```

 - 2 kinds of classes
    - 1. Classes that provide functionality
        - Math class API (example)  
            - Provides various mathematical operations
            - `function int abs(int x)`
        - Contains functions only
        - no fields, constructors, or methods 
        - Offers a "library of services"
    
    - 2.  Classes that represent entites (objects)
        - Examples:  Fraction, List, String , ... 
        - A class that contains at least on method
        - Typically contains fields and methods.
        - Can also contain functions, recommended for "helper" purpoes only

### Jack's standard class library / OS

 - OS purpose:
    - Closes gaps between high-level programs and the host hardware
    - Provides efficient implementations of commonly-used functions
    - Provides efficient implementations of commonly-used ADT's.  (abstract data type ?)
 - OS implementation
    - A collection of classes
    - Similar to Java's standard class library , in spirit

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_std_os.png)


## 3.7 Jack Language Specification: Methods

### Subroutines

```
constructor | method | function  type subroutineName ( parameter-list ) {
    local variable declarations
    statements
}
```

 - Subroutine types and return values
    - Method and function type can be either `void` , a primitive data type, or a class name
    - Each subroutine must return a value 

 - Jack subroutines
    - Constructors: create new objects
        - 0,1, or more in a class
        - Common name : `new`
        - must be same type of class 
        - must return a reference to an object of this class type
    - Methods:  operate on the current object
    - Functions:  static methods

###  Variables

 - variable types
    - static variables
        - class-level variables, can be manipulated by the class subroutines
    - field variables
        - object properties, can be manipulated by the class constructors and methods
    - local variabbles
        - used by subroutines, for local computations
    - parameter variables
        - used to pass values to subroutines , behave like local variables

 - variables must be ...
    - Declared before they are used
    - Typed
    
### Statements

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_statement.png)

### Expressions

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_expressions.png)

### Arrays

 - Jack arrays are ...
    - instance (objects) of the OS class Array
    - not typed
    - uni-dimensional

```
var Array arr;
let arr = Array.new(4) ;
arr[0] = 12;
arr[1] = false ;
arr[2] = Fraction.new(314,100);
...
```

### End note:  peculiar features of Jack

 - `let`
    - must be used in assigments: `let x=0;`
 - `do`
    - must be used for calling a method or a function outside an expression:  `do reduce();`
 - The body of a statement must be within curly brackets , even if it contains a single statement:
    - `if (a>0) {return a} else {return -a};`   ?? is the syntax correct ?
 - All subroutine must end with a `return`
 - **No operator priority**.
    - you have to use parentheses
 - The language is weakly typed


## 3.8 Developing Apps using the Jack language and OS

### Handling output: text 

 - Textual apps:
    - Screen: 23 rows of 64 characters, b&w
    - Font: featured by the Jack OS
    - Output: Jack OS Output class
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_output_api.png)

### Handling output: Graphics

 - Graphical apps:
    - Screen: 256 rows of 512 pixels, b&w
    - Output: Jack OS Screen class ( or do your own )
 - 

















 













