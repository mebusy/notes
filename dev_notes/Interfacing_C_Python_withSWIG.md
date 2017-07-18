
# Interfacing C/C++ and Python with SWIG

# Extending and Embedding Python

 - There are two basic methods for integrating C/C++ with Python
    - Extension writing.
        - Python access to C/C++.
    - Embedding
        - C/C++ access to the Python interpreter.


```
        Python 
          | ↑
Extending | | Embedding
          ↓ |
        C/C++
```

 - We are primarily concerned with “extension writing”

## Writing Wrapper Functions

 - “wrapper” functions are needed to access C/C++
    - Wrappers serve as a glue layer between languages.
    - Need to convert function arguments from Python to C.
    - Need to return results in a Python-friendly form

```c
// C Function
int fact(int n) {
    if (n <= 1) return 1;
    else return n*fact(n-1);
}
```

```c
// Wrapper
PyObject *wrap_fact(PyObject *self, PyObject *args) {
    int n, result;
    if (!PyArg_ParseTuple(args,”i:fact”,&n))
        return NULL;
    result = fact(n);  // key call
    return Py_BuildValue(“i”,result);
}
```

 - The conversion of data between Python and C is performed using two functions :
    - `int PyArg_ParseTuple(PyObject *args, char *format, ...)`
    - `PyObject *Py_BuildValue(char *format, ...)`
 - For each function, the format string contains conversion codes according to the following table :

```c
s = char *
i = int
l = long int
h = short int
c = char
f = float
d = double
O = PyObject *
(items) = A tuple
|items = Optional arguments
```

 - These functions are used as follows :

```
PyArg_ParseTuple(args,”iid”,&a,&b,&c); // Parse an int,int,double
PyArg_ParseTuple(args,”s|s”,&a,&b); // Parse a string and an optional string
Py_BuildValue(“d”,value); // Create a double
Py_BuildValue(“(ddd)”,a,b,c); // Create a 3-item tuple of doubles
```

 - Refer to the Python extending and embedding guide for more details.

## Module Initialization

 - All extension modules need to register wrappers with Python
    - An initialization function is called whenever you import an extension module.
    - The initialization function registers new methods with the Python interpreter
 - A simple initialization function :

```c
static PyMethodDef exampleMethods[] = {
     { "fact", wrap_fact, 1 },
      { NULL, NULL }
};
void initexample() {
    PyObject *m;
    m = Py_InitModule("example", exampleMethods);
}
```

 - When using C++, the initialization function must be given C linkage. For example :
    - `extern “C” void initexample() {`


## A Complete Extension Example

```c
#include <Python.h>
PyObject *wrap_fact(PyObject *self, PyObject *args) {
    int n, result;
    if (!PyArg_ParseTuple(args,”i:fact”,&n))
        return NULL;
    result = fact(n);
    return Py_BuildValue(“i”,result);
}
static PyMethodDef exampleMethods[] = {
    { "fact", wrap_fact, 1 },
    { NULL, NULL }
};
void initexample() {
    PyObject *m;
    m = Py_InitModule("example", exampleMethods);
}
``` 

## Compiling A Python Extension

 - There are two methods
    - Dynamic Loading
    - Static linking
 - Dynamic Loading
    - The extension module is compiled into a shared library or DLL.
    - When you type ‘import’, Python loads and initializes your module on the fly
 - Static Linking
    - The extension module is compiled into the Python core
    - The module will become a new “built-in” module
    - Typing ‘import’ simply initializes the module.
 - Given the choice, you should try to use dynamic loading
    - It’s usually easier
    - It’s surprisingly powerful if used right.

### Dynamic Loading

 - Unfortunately, the build process varies on every machine

```bash
// for Linux
gcc -fpic -c -I/usr/local/include/python1.5 \
    -I/usr/local/lib/python1.5/config \
    example.c wrapper.c
gcc -shared example.o wrapper.o -o examplemodule.so
```

Also ...

 - If your module is named ‘example’, make sure you compile it into a file named ‘example.so’ or ‘examplemodule.so’.
 - You may need to modify the extension to compile properly on all different platforms
 - Not all code can be easily compiled into a shared library (more on that later).

### Static Linking

 - How it works
    - You compile the extension module and link it with the rest of Python to form a new Python executable.
    - C Extensions + Python -> Custom python
 - When would you use it?
    - When running Python on esoteric machines that don’t have shared libraries
    - When building extensions that can’t be linked into a shared library
    - If you had a commonly used extension that you wanted to add to the Python core

## Using The Module

```python
>>> import example
>>> example.fact(4)
24
```

 - Summary
    - To write a module, you need to write some wrapper functions
    - To build a module, the wrapper code must be compiled into a shared library or staticly linked into the Python executable (this is the tricky part).
    - Using the module is easy.

---

## Wrapping a C Application

 - The process
    - Write a Python wrapper function for every C function you want to access
    - Create Python versions of C constants (not discussed).
    - Provide access to C variables, structures, and classes as needed.
    - Write an initialization function.
    - Compile the whole mess into a Python module.
 - The problem
    - Imagine doing this for a huge library containing hundreds of functions.
    - Writing wrappers is extremely tedious and error-prone
    - Consider the problems of frequently changing C code
    - Aren’t there better things to be working on?

## Extension Building Tools

 - Stub Generators (e.g. Modulator)
    - Generate wrapper function stubs and provide additional support code
    - You are responsible for filling in the missing pieces and making the module work.
 - Automated tools (e.g. SWIG, GRAD, bgen, etc...)
    - Automatically generate Python interfaces from an interface specification.
    - May parse C header files or a specialized interface definition language (IDL).
    - Easy to use, but somewhat less flexible than hand-written extensions.
 - Distributed Objects (e.g. ILU)
    - Concerned with sharing data and methods between languages
    - Distributed systems, CORBA, COM, ILU, etc...
 - Extensions to Python itself (e.g. Extension classes, MESS, etc...)
    - Aimed at providing a high-level C/C++ API to Python.
    - Allow for powerful creation of new Python types, providing integration with C++, etc...

---

# SWIG

## An Introduction to SWIG

 - SWIG (Simplified Wrapper and Interface Generator)
    - A compiler that turns ANSI C/C++ declarations into scripting language interfaces.
    - Completely automated (produces a fully working Python extension module).
    - Language neutral. SWIG can also target Tcl, Perl, Guile, MATLAB, etc...
    - Attempts to eliminate the tedium of writing extension modules.

### SWIG Features

 - Core features
    - Parsing of common ANSI C/C++ declarations
    - Support for C structures and C++ classes
    - Comes with a library of useful stuff
    - A wide variety of customization options
    - Language independence (works with Tcl, Perl, MATLAB, and others).
    - Extensive documentation.
 - The SWIG philosophy
    - There’s more than one way to do it (a.k.a. the Perl philosophy)
    - Provide a useful set of primitives.
    - Keep it simple, but allow for special cases
    - Allow people to shoot themselves in the foot (if they want to).

### A Simple SWIG Example

Some C code

```c
/* example.c */
double Foo = 7.5;
int fact(int n) {
    if (n <= 1) return 1;
    else return n*fact(n-1);
}
```

A SWIG interface file

```c
// example.i
%module example
%{
#include "headers.h"
%}

int fact(int n);
double Foo;
#define SPAM 42
```

 - `%module example`  : Module Name
 - `#include "headers.h" `  : Headers 
 - `int fact(int n);  ... `   : C declarations
 - “interface file” contains the ANSI C declarations of things you want to access,
    - but also contains SWIG directives (which are always preceded by ’%’)
 - The %module directive specifies the name of the Python extension module
 - Any code enclosed by %{ ... %} is copied verbatim into the wrapper code generated by SWIG 
    - (this is usually used to include header files and other supporting code).

### A Simple SWIG Example (cont...)

 - Building a Python Interface

```c
% swig -python example.i
Generating wrappers for Python
% cc -c example.c example_wrap.c \
    -I/usr/local/include/python1.5 \
    -I/usr/local/lib/python1.5/config
% ld -shared example.o example_wrap.o -o examplemodule.so
```

 - SWIG produces a file `example_wrap.c` that is compiled into a Python module
 - The name of the module and the shared library should match. 

---

 - Using the module

```python
>>> import example
>>> example.fact(4)
24
>>> print example.cvar.Foo
7.5
>>> print example.SPAM
42
```

 - The process of building a shared library differs on every machine. 
 - All global variables are accessed through a special object ‘cvar’ (for reasons explained shortly).

## What SWIG Does

 - Basic C declarations
    - C functions become Python functions (or commands).
    - C global variables become attributes of a special Python object ’cvar’.
    - C constants become Python variables.
 - Datatypes
    - C built-in datatypes are mapped into the closest Python equivalent.
    - int, long, short <---> Python integers.
    - float, double <---> Python floats
    - char, char * <---> Python strings.
    - void <---> None
    - long long, long double ---> Currently unsupported
 - SWIG tries to create an interface that is a natural extension of the underlying C code.
 - Notes
    - Python integers are represented as ’long’ values. All integers will be cast to and from type long when converting between C and Python.
    - Python floats are represented as ’double’ values. Single precision floating point values will be cast to type double when converting between the languages.
    - long long and long double are unsupported due to the fact that they can not be accurately represented in Python (the values would be truncated).


## More on Global Variables

 - Why does SWIG access global variables through ’cvar’?
 - "Assignment" in Python
    - Variable "assignment" in Python is really just a renaming operation. 
    - Variables are references to objects.
    - A C global variable is not a reference to an object, it is an object.
    - To make a long story short, assignment in Python has a meaning that doesn’t translate to assignment of C global variables.
 - Assignment through an object
    - C global variables are mapped into the attributes of a special Python object
    - Giving a new value to an attribute changes the value of the C global variable
    - By default, the name of this object is ’cvar’, but the name can be changed.
        - `% swig -python -globals myvar example.i`   changes to `mybar` instead
 - Notes
    - If a SWIG module contains no global variables, the ’cvar’ variable will not be created
    - Some care is also in order for using multiple SWIG generated modules
        - if you use the Python ’from module import *’ directive, you will get a namespace collision on the value of ’cvar’ (unless you explicitly changed its name as described above).

## More on Constants

 - The following declarations are turned into Python variables
    - #define
    - const
    - enum
 - The type of a constant is inferred from syntax (unless given explicitly)
 - Constant expressions are allowed
 - Values must be defined. 
    - For example, ’#define FOO BAR’ does not result in a constant unless BAR has already been defined elsewhere.
 - Notes
    - SWIG only creates a constant if a #define directive looks like a constant. 
    - the following directives would create constants
        - #define READ_MODE 1
        - #define FOOBAR 8.29993
        - #define VALUE 4*FOOBAR
    - The following declarations would not result in constants
        - #define USE_PROTOTYPES // No value given
        - #define _ANSI_ARGS_(a) a // A macro
        - #define FOO BAR // BAR is undefined

## Pointers

 - Pointer management is critical!
    - Arrays
    - Objects
    - Most C programs have tons of pointers floating around.
 - The SWIG type-checked pointer model
    - C pointers are handled as opaque objects
    - Encoded with type-information that is used to perform run-time checking.
    - Pointers to virtually any C/C++ object can be managed by SWIG.
 - Advantages of the pointer model
    - Conceptually simple
    - Avoids data representation issues (it’s not necessary to marshal objects between a Python and C representation).
    - Efficient (works with large C objects and is fast)
    - It is a good match for most C programs.
 - Notes
    - The pointer model allows you to pass pointers to C objects around inside Python scripts, pass pointers to other C functions, and so forth. 
    - In many cases this can be done without ever knowing the underlying structure of an object or having to convert C data structures into Python data structures.
    - An exception to the rule : **SWIG does not support pointers to C++ member functions**. 
        - This is because such pointers can not be properly cast to a pointer of type ’void *’ (the type that SWIG uses internally).

## Pointer Encoding and Type Checking

 - Pointer representation
    - Currently represented by Python strings with an address and type-signature.
    - Pointers are opaque so the precise Python representation doesn’t matter much
 - Type errors result in Python exceptions
    - Type-checking prevents most of the common errors.
    - Has proven to be extremely reliable in practice.
 - Notes
    - The NULL pointer is represented by the string "NULL"
    - Python has a special object "CObject" that can be used to hold pointer values. SWIG does not use this object because it does not currently support type-signatures. 
    - Run-time type-checking is essential for reliable operation because the dynamic nature of Python effectively bypasses all typechecking that would have been performed by the C compiler. The SWIG run-time checker makes up for much of this
    - Future versions of SWIG are likely to change the current pointer representation of strings to an entirely new Python type. This change should not substantially affect the use of SWIG however

## Array Handling

 - Arrays are pointers
    - Same model used in C (the "value" of an array is a pointer to the first element).
    - Multidimensional arrays are supported
    - There is no difference between an ordinary pointer and an array.
    - However, SWIG does not perform bounds or size checking
    - C arrays are not the same as Python lists or tuples!
 - Notes
    - Effective use of arrays may require the use of accessor-functions to access individual members (this is described later).
    - If you plan to do alot of array manipulation, you may want to check out the Numeric Python extension.

## Complex Objects

 - SWIG manipulates all "complex" objects by reference
    - The definition of an object is not required.
    - Pointers to objects can be freely manipulated
    - Any "unrecognized" datatype is treated as if it were a complex object.
 - Examples :
    - `double dot_product(Vector *a, Vector *b);`
    - `FILE *fopen(char *, char *);`
    - `Matrix *mat_mul(Matrix *a, Matrix *b);`
 - Notes
    - Whenever SWIG encounters an unknown datatype, it assumes that it is a derived datatype and manipulates it by reference
    - Unlike the C compiler, SWIG will never generate an error about undefined datatypes
    - While this may sound strange, it makes it possible for SWIG to build interfaces with a minimal amount of additional information.
        - For example, if SWIG sees a datatype ’Matrix *’, it’s obviously a pointer to something (from the syntax).  
        - From SWIG’s perspective, it doesn’t really matter what the pointer is actually pointing to--that is, SWIG doesn’t need the definition of Matrix

## Passing Objects by Value

 - What if a program passes complex objects by value?
    - `double dot_product(Vector a, Vector b);`
    - SWIG converts pass-by-value arguments into pointers and creates a wrapper equivalent to the following :
    - This transforms all pass-by-value arguments into pass-by reference.

```c
double wrap_dot_product(Vector *a, Vector *b) {
     return dot_product(*a,*b);
}
```

 - Is this safe?
    - Works fine with C programs.
    - Seems to work fine with C++ if you aren’t being too clever.
 - Notes
    - Trying to implement pass-by-value directly would be extremely difficult---we would be faced with the problem of trying to find a Python representation of C objects (a problem we would rather avoid).
    - Make sure you tell SWIG about all typedefs. For example,
        - `Real spam(Real a); // Real is unknown. Use as a pointer`
    - versus
        - `typedef double Real;`
        - `Real spam(Real a); // Ah. Real is just a ’double’.`

## Return by Value

 - Return by value is more difficult...
    - `Vector cross_product(Vector a, Vector b);`
    - What are we supposed to do with the return value?
    - Can’t generate a Python representation of it (well, not easily), can’t throw it away.
    - SWIG is forced to perform a memory allocation and return a pointer.

```c
Vector *wrap_cross_product(Vector *a, Vector *b) {
    Vector *result = (Vector *) malloc(sizeof(Vector));
    *result = cross_product(*a,*b);
    return result;
}
```

 - Isn’t this a huge memory leak?
    - Yes. 
    - It is the user’s responsibility to free the memory used by the result
    - Better to allow such a function (with a leak), than not at all.
 - Notes
    - When SWIG is processing C++ libraries, it uses the default copy constructor instead. For example :

```c
Vector *wrap_cross_product(Vector *a, Vector *b) {
    Vector *result = new Vector(cross_product(*a,*b));
    return result;
}
```

## Renaming and Restricting

 - Renaming declarations
    - The %name directive can be used to change the name of the Python command.
        - `%name(output) void print();`
    - Often used to resolve namespace conflicts between C and Python.
 - Creating read-only variables
    - The %readonly and %readwrite directives can be used to change access permissions to variables.
    - Read-only mode stays in effect until it is explicitly disabled.

```c
double foo; // A global variable (read/write)
%readonly
double bar; // A global variable (read only)
double spam; // (read only)
%readwrite
```

## Code Insertion

 - The structure of SWIG’s output
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/swig_structure_of_swig_output.png)
 - Four directives are available for inserting code
    - %{ ... %} inserts code into the header section
    - %init %{ ... %} inserts code into the initialization function
    - %inline %{ ... %} inserts code into the header section and "wraps" it. 
 - Notes
    - These directives insert code verbatim into the output file. This is usually necessary.
    - The syntax of these directives is loosely derived from YACC parser generators which also use %{,%} to insert supporting code.
    - Almost all SWIG applications need to insert supporting code into the wrapper output.


### Code Insertion Examples

 - Including the proper header files (extremely common)

```c
%module opengl
%{
#include <GL/gl.h>
#include <GL/glu.h>
%}
// Now list declarations
```

 - Module specific initialization

```c
%module matlab
...
// Initialize the module when imported.
%init %{
     eng = engOpen("matlab42");
%}
```
     
## Helper Functions

 - Sometimes it is useful to write supporting functions
    - Creation and destruction of objects.
    - Providing access to arrays.
    - Accessing internal pieces of data structures.

```c
%module darray
%inline %{
double *new_darray(int size) {
    return (double *) malloc(size*sizeof(double));
}
double darray_get(double *a, int index) {
    return a[index];
}
void darray_set(double *a, int index, double value) {
    a[index] = value;
}
%}

%name(delete_darray) free(void *);
```

 - Notes
    - Helper functions can be placed directly inside an interface file by enclosing them in an %{,%} block
    - Helper functions are commonly used for providing access to various datatypes. 
        - For our example above, we would be able to use the functions from Python as follows. 
    - In many cases we may not need to provide Python access, but may need to manufacture objects suitable for passing to other C functions.

```python
from darray import *

# Turn a Python list into a C double array
def createfromlist(l):
    d = new_darray(len(l))
    for i in range(0,len(l)):
        darray_set(d,i,l[i])
    return d

# Print out some elements of an array
def printelements(a, first, last):
    for i in range(first,last):
        print darray_get(a,i)
```

## Conditional Compilation

 - Use C preprocessor directives to control SWIG compilation
    - The SWIG symbol is defined whenever SWIG is being run.
    - Can be used to make mixed SWIG/C header files

```
/* header.h
 A mixed SWIG/C header file */
#ifdef SWIG
%module example
%{
#include "header.h"
%}
#endif

/* C declarations */
...
#ifndef SWIG
/* Don’t wrap these declarations. */
#endif
...
```

 - Notes
    - SWIG includes an almost complete implementation of the preprocessor that supports #ifdef, #ifndef, #if, #else, #elif, and #endif directives.


## File Inclusion

 - The %include directive
    - Includes a file into the current interface file.
    - Allows a large interface to be built out of smaller pieces.
    - Allows for interface libraries and reuse.

```c
%module opengl.i

%include gl.i
%include glu.i
%include aux.i
%include "vis.h"
%include helper.i
```


 - File inclusion in SWIG is really like an "import." 
    - Files can only be included once and include guards are not required (unlike C header files).
 - Notes
    - Like the C compiler, SWIG library directories can be specified using the -I option. For example :
        - `swig -python -I/home/beazley/SWIG/lib example.i`
    - Two other directives, %extern and %import are also available, but not described in detail. 

## Quick Summary

 - You now know almost everything you need to know
    - C declarations are transformed into Python equivalents
    - C datatypes are mapped to an appropriate Python representation.
    - Pointers can be manipulated and are type-checked.
    - Complex objects are managed by reference.
    - SWIG provides special directives for renaming, inserting code, including files, etc...
 - This forms the foundation for discussing the rest of SWIG
    - Handling of structures, unions, and classes
    - Using the SWIG library.
    - Python wrapper classes
    - Customization.
    - And more.

---

# A SWIG Example

## Building a Python Interface to OpenGL
 
 - OpenGL
    - A widely available library/standard for 3D graphics.
    - Consists of more than 300 functions and about 500 constants.
    - Available on most machines (Mesa is a public domain version).
        - http://www.ssec.wisc.edu/~brianp/Mesa.html
 - Interface Building Strategy (in a nutshell)
    - Copy the OpenGL header files
    - Modify slightly to make a SWIG interface file
    - Clean up errors and warning messages.
    - Write a few support functions
    - Build it.
 - Why OpenGL?
    - It’s a significant library that does something real.
    - It’s available everywhere.
    - Can build a simple Python interface fairly quickly


## Preparing the Files

```c
// gl.i
%{
#include <GL/gl.h>
%}
%include "GL/gl.h"

// glu.i
%{
#include <GLU/glu.h>
%}
%include "GL/glu.h"

// glut.i
%{
#include <GLU/glut.h>
%}
%include "GL/glut.h"
%include "GL/freeglut_std.h"


// opengl.i

// OpenGL Interface
%module opengl
%include gl.i
%include glu.i
%include glut.i
```

 - for opengl header files, we use those int `/opt/X11/include/GL`

```bash
swig -Wall -python -c++ -I/opt/X11/include/ opengl.i 
c++ -c -fPIC  opengl_wrap.cxx -I/opt/X11/include/ -I/usr/include/python2.7/
c++ -dynamiclib -lpython -framework OpenGL -framework GLUT opengl_wrap.o   -o _opengl.so 
```

---

# Objects

## Manipulating Objects

 - The SWIG pointer model (reprise)
    - SWIG manages all structures, unions, and classes by reference (i.e. pointers)
    - Most C/C++ programs pass objects around as pointers
    - In many cases, writing wrappers and passing opaque pointers is enough.
    - However, in some cases you might want more than this.
 - Issues
    - How do you create and destroy C/C++ objects in Python ?
    - How do you access the internals of an object in Python?
    - How do you invoke C++ member functions from Python?
    - How do you work with objects in a mixed language environment?
 - Concerns
    - Don’t want to turn Python into C++.
    - Don’t want to turn C++ into Python (although this would be an improvement).
    - Keep it minimalistic and simple in nature.

## Creating and Destroying Objects

 - Objects can be created and destroyed by writing special functions :

```c
typedef struct {
    double x,y,z;
} Vector; 
```

```c
%inline %{
    Vector *new_Vector(double x, double y, double z) {
        Vector *v = (Vector *) malloc(sizeof(Vector));
        v->x = x; v->y = y; v->z = z;
        return v;
    }
    void delete_Vector(Vector *v) {
        free(v);
    }
%}
```

## Accessing the Internals of an Object

 - This is also accomplished using accessor functions
 - Admittedly crude, but conceptually simple

```c
%inline %{
    double Vector_x_get(Vector *v) {
        return v->x;
    }
    void Vector_x_set(Vector *v, double val) {
        v->x = val;
    }
%}
```

## Accessing C++ Member Functions

 - You guessed it ....
 - Basically, we just create ANSI C wrappers around C++ methods

```c
class Stack {
public:
    Stack();
    ~Stack();
    void push(Object *);
    Object *pop();
};
```

```c
%inline %{
    void Stack_push(Stack *s, Object *o) {
        s->push(o);
    }
    Object *Stack_pop(Stack *s) {
        return s->pop();
    }
%}
```

## Automatic Creation of Accessor Functions

 - SWIG automatically generates accessor functions if given structure, union or class definitions.
 - Avoids the tedium of writing the accessor functions yourself

## Parsing Support for Objects

 - SWIG provides parsing support for the following
    - Basic structure and union definitions.
    - Constructors/destructors.
    - Member functions.
    - Static member functions.
    - Static data.
    - Enumerations.
    - C++ inheritance.
 - Not currently supported (mostly related to C++)
    - Template classes (what is a template in Python?)
    - Operator overloading.
    - Nested classes.
 - However, SWIG can work with incomplete definitions
    - Just provide the pieces that you want to access
    - SWIG is only concerned with access to objects, not the representation of objects

## Renaming and Restricting Members

 - Structure members can be renamed using %name

```c
struct Foo {
    %name(spam) void bar(double);
    %name(status) int s;
};
```

 - Access can be restricted using %readonly and %readwrite

```c
class Stack {
public:
    Stack();
    ~Stack();
    void push(Object *);
    Object *pop();
    %readonly // Enable read-only mode
    int depth;
    %readwrite // Re-enable write access
};
```

## C++ Inheritance and Pointers

 - SWIG encodes C++ inheritance hierarchies
    - The run-time type checker knows the inheritance hierarchy.
    - Type errors will be generated when violations are detected.
    - C++ pointers are properly cast when necessary.

## Shadow Classes

 - Writing a Python wrapper class
    - Can encapsulate C structures or C++ classes with a Python class
    - The Python class serves as a wrapper around the underlying C/C++ object (and is said to “shadow” the object).
    - Easily built using pointers and low-level accessor functions.
    - Contrast to writing a new Python type in C


```c
class Stack {
public:
    Stack();
    ~Stack();
    void push(Object *);
    Object *pop();
    int depth;
};
```

```python
class Stack:
    def __init__(self):
        self.this = new_Stack()
    def __del__(self):
        delete_Stack(self.this)
    def push(self,o):
        Stack_push(self.this,o)
    def pop(self):
        return Stack_pop(self.this)
    def __getattr__(self,name):
        if name == 'depth':
            return Stack_depth_get(self.this)
        raise AttributeError,name
```

## Automatic Shadow Class Generation

 - moduelname.py
 - Shadow classes are just an interface extension
    - They utilize pointers and accessor functions.
    - No changes to Python are required
 - `import example`  will load the Python wrappers (and implicitly load the C extension module as well).
 - `import examplec `   # Load original C interface.

## The Anatomy of a Shadow Class

```python
# This file was created automatically by SWIG.
import stackc
class StackPtr:
    def __init__(self, this) :
        self.this = this
        self.thisown = 0
    ...
    def push(self,arg0):
        stackc.Stack_push(self.this,arg0)
    ...
class Stack(StackPtr):
    def __init__(self):
        self.this = stackc.new_Stack()
        self.thisown = 1

```

 - class StackPtr
    - defines the methods available for a generic Stack object (given as a pointer)
    - The constructor for this class simply takes a pointer to an existing object and encapsulates it in a Python class
 - class Stack
    - This class is used to create a new Stack object.
    - The constructor calls the underlying C/C++ constructor to generate a new object.


## Using a Shadow Class

 - This is the easy part--they work just like a normal Python class

```python
>>> import stack
>>> s = Stack()
>>> s.push(“Dave”)
>>> s.push(“Mike”)
>>> s.push(“Guido”)
>>> s.pop()
Guido
>>> s.depth
2
>>> print s.this
_1008fe8_Stack_p
>>>
```

 - In practice this works pretty well
    - A natural interface to C/C++ structures and classes is provided.
    - C++ classes work like Python classes (you can even inherit from them)
    - The implementation is relatively simple (it’s just a layer over the SWIG pointer mechanism and accessor functions)
    - Changes to the Python wrappers are easy to make---they’re written in Python

## Nested Objects

 - Shadow classing even works with nested objects

```c
struct Vector {
    double x;
    double y;
    double z;
};
struct Particle {
    Particle();
    ~Particle();
    int type;
    Vector r;
    Vector v;
    Vector f;
};
```

```python
>>> p = Particle()
>>> p.r
<C Vector instance>
>>> p.r.x = 0.0
>>> p.r.y = -7.5
>>> p.r.z = -1.0
>>> print p.r.y
-7.5
>>> p.v = p.r
>>> print p.v.y
-7.5
>>> 
```

## Managing Object Ownership

 - Who owns what?
    - Objects created by Python are owned by Python (and destroyed by Python)
    - Everything else is owned by C/C++.
    - The ownership of an object is controlled by the ‘thisown’ attribute.
        - self.thisown = 1 # Python owns the object
        - self.thisown = 0 # C/C++ owns the object.
    - The owner of an object is responsible for its deletion!
 - Caveat : sometimes you have to explicitly change the ownership

```c
struct Node {
    Node();
    ~Node();
    int value;
    Node *next;
};
```

```python
# Convert a Python list to a linked list
def listtonode(l):
    n = NodePtr("NULL");
    for i in l:
        m = Node()
        m.value = i
        n.next = m
        n.thisown = 0
        n = m
    return n
```

 - In the example, we are saving pointers to objects in the ‘next’ field of each data structure
 - consider the use of the variables ‘n’ and ‘m’ in the Python code above
    - ‘n’ will be assigned to a new object on each iteration of the loop
    - Any previous value of ‘n’ will be destroyed (because there are no longer any Python references to it)
    - Had we not explicitly changed the ownership of the object, this destruction would have also destroyed the original C object. 
    - This, in turn, would have created a linked list of invalid pointer values---probably not the effect that you wanted.
 - When the ‘thisown’ variable is set to 0
    - Python will still destroy ‘n’ on each iteration of the loop, 
    - but this destruction only applies to the Python wrapper class--not the underlying C/C++ object.

## Extending Structures and Classes

 - Object extension : A cool trick for building Python interfaces
    - You can provide additional “methods” for use only in Python
    - Debugging.
    - Attach functions to C structures (i.e. object-oriented C programming) .

A C structure

```c
struct Image {
    int width;
    int height;
     ...
};
```

Some C functions

```c
Image *imgcreate(int w, int h);
void imgclear(Image *im, int color);
void imgplot(Image *im,int x,int y,int color);
...
```

=> 

A Python wrapper class 

```python
class Image:
    def __init__(self,w,h):
        self.this = imgcreate(w,h)
    def clear(self,color):
        imgclear(self.this,color)
    def plot(self,x,y,c):
        imgplot(self.this,x,y,c)
    ...

>>> i = Image(400,400)
>>> i.clear(BLACK)
>>> i.plot(200,200,BLUE)
```

## Class Extension with SWIG

 - The %addmethods directive 

```c
%module image
struct Image {
    int width;
    int height;
    ...
};
%addmethods Image {
    Image(int w, int h) {
        return imgcreate(w,h);
    }
    void clear(int color) {
        return imgclear(self,color);
    }
    void plot(int x, int y, int color) {
        return imgplot(self,x,y,color);
    }
};
```

 - Same syntax as C++
 - Just specify the member functions you would like to have (constructors, destructors, member functions).
 - SWIG will combine the added methods with the original structure or class.

## Adding Methods (cont...)

 - Works with both C and C++
    - Added methods only affect the Python interface--not the underlying C/C++ code.
    - Does not rely upon inheritance or any C++ magic
 - How it works (in a nutshell)
    - SWIG creates an accessor/helper function, but uses the code you supply.
    - The variable ‘self’ contains a pointer to the corresponding C/C++ object.

```c
%addmethods Image {
    ...
    void clear(int color) {
        clear(self,color);
    }
    ...
}
```

=>

```c
void Image_clear(Image *self, int color) {
     clear(self,color);
};
```

 - If no code is supplied, SWIG assumes that you have already written a function with the required name (methods always have a name like ‘Class_method’
 - SWIG treats the added method as if it were part of the original structure/class definition (from Python you will not be able to tell).

## Adding Special Python Methods

 - %addmethods can be used to add Python specific functions

```c
typedef struct {
    double x,y,z;
} Vector;

%addmethods Vector {
...
char *__str__() {
    static char str[256];
    sprintf(str,”[%g, %g, %g]”,
        self->x,self->y,self->z);
    return str;
}
};
```

=> 

```python
>>> v = Vector(2,5.5,9)
>>> print v
[2, 5.5, 9]
>>> 
```

 - Most of Python’s special class methods can be implemented in C/C++ and added to structures or classes.
 - Allows construction of fairly powerful Python interfaces
 - Notes
    - The use of a static variable above insures that the `char *` returned exists after the function call. 
        - Python will make a copy of the returned string when it converts the result to a Python object.
    - A safer approach would also include some bounds checks on the result string.

## Accessing Arrays of Objects

 - Added methods to the rescue...

```c
typedef struct {
    double x,y,z;
} Vector;
...
Vector *varray(int nitems);
%addmethods Vector {
    ...
    Vector *__getitem__(int index) {
        return self+index;
    }
    ...
};
```

=>

```python
>>> a = varray(1000)
>>> print a[100]
[0, 0, 0]
>>> for i in range(0,1000):
... a[i].x = i
>>> print a[500]
[500, 0, 0]
>>> 
```

 - Accesing arrays of any kind of object is relatively easy
 - Provides natural access (arrays can be manipulated like you would expect)
 - Similar tricks can be used for slicing, iteration, and so forth




## Making Sense of Objects (Summary)

 - SWIG uses a layered approach
    - Python Shadow Classes
        - High Level Access to C/C++ structures and objects
    - C/C++ Accessor Functions
        - Helper/Accessor functions that provide access to objects
    - ANSI C Wrappers
        - Manipulation of objects as opaque pointer values
 - All three modes are useful and may be mixed in the same program
    - Use opaque pointers when access to an object’s internals is unnecessary
    - Use C/C++ accessor functions when occasional access to an object is needed
    -  Use Python shadow classes when you want an interface that closely mimics the underlying C/C++ object.

---

# The SWIG Library

 - SWIG is packaged with a standard “library”
    - Think of it as the SWIG equivalent of the Python library
 - Contents of the library :
    - Interface definitions to common C libraries.
    - Utility functions (array creation, pointer manipulation, timers, etc...)
    - SWIG extensions and customization files.
    - Support files (Makefiles, Python scripts, etc...)
 - Using the library is easy--just use the %include directive.
    -  Code from the library files is simply inserted into your interface

```c
%module example

%include malloc.i
%include pointer.i
%include timers.i
...
```

## TODO

---

# Advanced SWIG Features

## Exception Handling

 - Python has a nice exception handling mechanism...we should use it.
    - Translating C error conditions into Python exceptions.
    - Catching C++ exceptions.
    - Improving the reliability of our Python modules.
 - The %except directive
    - Allows you to define an application specific exception handler
    - Fully configurable (you can do anything you want with it).
    - Exception handling code gets inserted into all of the wrapper functions.

```c
%except(python) {
    try {
        $function /* This gets replaced by the real function call */
    }
    catch(RangeError) {
        PyErr_SetString(PyExc_IndexError,”index out-of-bounds”);
        return NULL;
    }
}
```

### SWIG Exception Library

 - SWIG includes a library of generic exception handling functions
    - Language independent (works with Python, Tcl, Perl5, etc...)
    - Mainly just a set of macros and utility functions.

```c
%include exceptions.i
%except(python) {
    try {
        $function
    }
    catch(RangeError) {
        SWIG_exception(SWIG_IndexError,”index out-of-bounds”);
    }
}
```

 - Other things to note
    - Exception handling greatly improves the reliability of C/C++ modules
    - However, C/C++ applications need to be written with error handling in mind.
    - SWIG can be told to look for errors in any number of ways--as long as there is an error mechanism of some sort in the underlying application
 - Notes
    - SWIG is not limited to C++ exceptions or formal exception handling mechanisms. 
    - An exception handling might be something as simple as the following :
        - where check_error() and get_error_msg() are C functions to query the state of an application.

```c
%except(python) {
    $function
    if (check_error()) {
        char *msg = get_error_msg();
        SWIG_exception(SWIG_RuntimeError,msg);
    }
}
```

## Typemaps

 - Typemaps allow you to change the processing of any datatype
    - Handling of input/output values
    - Converting Python objects into C/C++ equivalents (tuples,lists, etc...)
    - Telling SWIG to use new Python types
    - Adding constraint handling (the constraint library is really just typemaps)
 - Very flexible, very powerful
    - You can do almost anything with typemaps.
    - You can even blow your whole leg off (not to mention your foot).
    - Often the topic of discussion on the SWIG mailing list
 - Caveats
    - Requires knowledge of Python’s C API to use effectively
    - It’s possible to break SWIG in bizarre ways (an interface with typemaps might not even work).
    - Impossible to cover in full detail here.

### Typemaps : In a Nutshell

 - What is a typemap?
    - A special processing rule applied to a particular (datatype,name) pair. 
    - `double spam(int a, int);`
        - => (double,”spam”) (int,”a”) (int,””) 
 - Pattern Matching Rules
    - SWIG looks at the input and tries to apply rules using a pattern matching scheme
    - Examples :
        - (int,””) # Matchs all integers
        - (int,”a”) # Matches only ‘int a’
        - (int *,””) # Matches ‘int *’ and arrays.
        - (int [4],””) # Matches ‘int[4]’
        - (int [ANY],””) # Matches any 1-D ‘int’ array
        - (int [4][4],”t”) # Matches only ‘int t[4][4]’
    - Multiple rules may apply simultaneously
    - SWIG always picks the most specific rule.

### The Typemap Library

 - typemaps.i
    - A SWIG library file containing a variety of useful typemaps.
    - Handling input/output arguments and other special datatypes.

```c
%module example
%include typemaps.i

void add(double *INPUT,double *INPUT, double *OUTPUT);

%apply int OUTPUT { int *width, int *height };
void get_viewport(Image *im, int *width, int *height);
```

=> 

```python
>>> add(3,4)
7.0
>>> a = get_viewport(im)
>>> print a
[500,500]
>>>
```

 - Hmmm. This is much different than the standard pointer model we saw before
 - Typemaps allow extensive customization!
 - The typemaps.i file contains a number of generally useful typemaps. You should check here before writing a new typemap from scratch.



