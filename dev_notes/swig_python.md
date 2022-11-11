[](...menustart)

- [SWIG PYTHON](#2f5f97b74dad99089e4d7ba36620e26e)
    - [36.3 A tour of basic C/C++ wrapping](#28253a47df2d59cca6fb97610aa2399c)
        - [36.3.3 Global variables](#864317df539bc6cd7a48701b91191c24)
        - [36.3.4 Constants and enums](#3ed1580636bb56cb368078416522781c)
        - [36.3.5 Pointers](#6c5d46b4c027b854d6f3b7b4a039ee27)
        - [36.3.6 Structures](#9e239ae42956495be216233b838ca77d)
        - [36.3.7 C++ classes](#289abb576803b40537aaf88cd30ea1b7)
        - [36.3.10 C++ overloaded functions](#20b5f7f6dfaff2c338c4b49bd2b53f52)
        - [36.3.11 C++ operators](#7fbad72828bffaf316f22c67e8b5b849)
        - [36.3.12 C++ namespaces](#2329b407fe1d5482f5e412a6502ecebe)
        - [36.3.13 C++ templates](#3ae5ee54a6d57c34cf29f39e935f13d2)
        - [36.3.14 C++ Smart Pointers](#375e31e2cbdc8887003fa50adfa38d67)
            - [36.3.14.1 The shared_ptr Smart Pointer](#0fd3d38db929aa36de6a011c60d87de1)
            - [36.3.14.2 Generic Smart Pointers](#584698ebaec253169b5dbc351c353e00)
    - [36.5 Cross language polymorphism](#8edc31645b1d72709e2a78ce42b80295)
        - [36.5.1 Enabling directors](#299f5530bbe369a25a8a9399abd64a44)
    - [36.6 Common customization features](#37b33f14f7ff3d5724be48045de26423)
        - [36.6.1 C/C++ helper functions](#8ed34b4d93e1ce67e4c5cdf57ac714f3)
        - [36.6.2 Adding additional Python code](#73f0c0b516a9a6466ff6f66d16f7aea1)
        - [36.6.3 Class extension with %extend](#d4f88a6538a37f876d6944cfddd37993)
        - [36.6.4 Exception handling with %exception](#6a994f76d514c7ea64b0080007f925bc)
    - [36.7 Tips and techniques](#15f329eb7bd57310ae05525a7560cb18)
        - [25.8.1 Input and output parameters using primitive pointers and references](#53e526b93ef9246ff51cd84f5debb919)
        - [36.7.2 Simple pointers](#515f4e8a06c359c5238034b0a0855efc)
        - [36.7.3 Unbounded C Arrays](#ea9fec0c4e11762f471b1cffa262b7a4)
        - [36.7.4 String handling](#c5928dddfc2c9487ddc042e45caa4576)
        - [36.7.5 Default arguments](#63b4f48acae0ba35e6576fce9fa8fdad)
    - [36.8 Typemaps](#2b130f8e243eb10cbc270985854ccbc7)
        - [36.8.1 What is a typemap?](#90a5be3942738a92f3991cb7d19710be)
        - [36.8.2 Python typemaps](#e4f724210edaab8c16c023cca34e2473)
        - [36.8.3 Typemap variables](#e729302bd9b4ccdceabc3c5587c9c140)
        - [36.8.4 Useful Python Functions](#427eb1b71112c2157f5763050c06240b)
    - [36.9 Typemap Examples](#c6ea35fbba443421bec5662d98c4a56d)
        - [36.9.1 Converting Python list to a char \*\*](#a0b62f2001104e30cea14cc3d978eb00)
        - [36.9.2 Expanding a Python object into multiple arguments](#e1aba4dac0c081ca9e1c9689b39f0b9d)
        - [36.9.3 Using typemaps to return arguments](#b0b0ba8683c797f778cbd3d40d7ecd4b)
        - [36.9.4 Mapping Python tuples into small arrays](#9e2e54e3b2717314d68b1cf84e329a8e)
        - [36.9.5 Mapping sequences to C arrays](#7933ae9020049f067c537253e1610be8)
        - [36.9.6 Pointer handling](#6568ccb24614cc5e9c0d0730be8a3837)
- [常见问题](#50d52dd929a75bb9b0f4afb0b7d879e1)

[](...menuend)


<h2 id="2f5f97b74dad99089e4d7ba36620e26e"></h2>

# SWIG PYTHON

<h2 id="28253a47df2d59cca6fb97610aa2399c"></h2>

## 36.3 A tour of basic C/C++ wrapping

<h2 id="864317df539bc6cd7a48701b91191c24"></h2>

### 36.3.3 Global variables

- there is no direct way to map variable assignment in C (a==b) to variable assignment in Python
    - because for python, variables are just names that refer to some object
- To provide access to C global variables, SWIG creates a special object called `cvar' that is added to each SWIG generated module.`
- If a variable is declared as *const*, it is wrapped as a read-only variable. 
    - To make ordinary variables read-only, you can use the *%immutable* directive. For example:

```
%{
    extern char *path;
%}
%immutable;
    extern char *path;
%mutable;
```

- If you just want to make a specific variable immutable, supply a declaration name. For example:

```
%{
    extern char *path;
%}
%immutable path;
...
extern char *path;      // Read-only (due to %immutable)
```

<h2 id="3ed1580636bb56cb368078416522781c"></h2>

### 36.3.4 Constants and enums

- C/C++ constants are installed as Python objects containing the appropriate value.
- To create a constant, use #define, enum , or the %constant directive. For example:

```
#define PI 3.14159
#define VERSION "1.0"

enum Beverage { ALE, LAGER, STOUT, PILSNER };

%constant int FOO = 42;
%constant const char *path = "/usr/local";
```

- Note: declarations declared as const are wrapped as read-only variables and will be accessed using the cvar object described in the previous section
- Constants are not guaranteed to remain constant in Python---the name of the constant could be accidentally reassigned to refer to some other object. 
    - Unfortunately, there is no easy way for SWIG to generate code that prevents this. You will just have to be careful.

<h2 id="6c5d46b4c027b854d6f3b7b4a039ee27"></h2>

### 36.3.5 Pointers

- the '0' or NULL pointer is always represented by None, no matter what type swig is addressing. In the previous example, you can call:
    - `example.fclose(None)`
 
<h2 id="9e239ae42956495be216233b838ca77d"></h2>

### 36.3.6 Structures

- If you wrap a C structure, it is wrapped by a Python class. 

```cpp++
struct Vector {
    double x, y, z;
};
```

```python
>>> v = example.Vector()
>>> v.x = 3.5
```

- This pointer can be passed around to functions that expect to receive an int \* (just like C). 
- You can also set the value of an array member using another pointer. For example:

```python
>>> c = example.Bar()
>>> c.x = b.x             # Copy contents of b.x to c.x
```

- When a member of a structure is itself a structure, it is handled as a pointer. For example, suppose you have two structures like this:

```cpp++
struct Foo {
    int a;
};

struct Bar {
    Foo f;
};
```

```python
>>> b = Bar()
>>> x = b.f
```




<h2 id="289abb576803b40537aaf88cd30ea1b7"></h2>

### 36.3.7 C++ classes

Static class members present a special problem for Python

```cpp++
class Spam {
    public:
        static void foo();
        static int bar;
};
```

In Python, the static member can be access in three different ways: 

```python
>>> example.Spam_foo()    # Spam::foo()
>>> s = example.Spam()
>>> s.foo()               # Spam::foo() via an instance
>>> example.Spam.foo()    # Spam::foo(). Python-2.2 and later only
```

Static member variables are currently accessed as global variables. This means, they are accessed through cvar like this:

```python
>>> print example.cvar.Spam_bar
7
```

<h2 id="20b5f7f6dfaff2c338c4b49bd2b53f52"></h2>

### 36.3.10 C++ overloaded functions

- C++ overloaded functions, methods, and constructors are mostly supported by SWIG
- Overloading support is not quite as flexible as in C++. Sometimes there are methods that SWIG can't disambiguate. For example:

```cpp++
void spam(int);
void spam(short);

or 

void foo(Bar *b);
void foo(Bar &b);
```

- If declarations such as these appear, you will get a warning message

```
example.i:12: Warning 509: Overloaded method spam(short) effectively ignored,
example.i:11: Warning 509: as it is shadowed by spam(int).
```

- To fix this, you either need to ignore or rename one of the methods. For example:

```
%rename(spam_short) spam(short);
...
void spam(int);    
void spam(short);   // Accessed as spam_short

or

%ignore spam(short);
...
void spam(int);    
void spam(short);   // Ignored
```

<h2 id="7fbad72828bffaf316f22c67e8b5b849"></h2>

### 36.3.11 C++ operators

- Certain C++ overloaded operators can be handled automatically by SWIG

```cpp++
Complex &operator=(const Complex &c);

Complex operator+=(const Complex &c) const;
Complex operator+(const Complex &c) const;
Complex operator-(const Complex &c) const;
Complex operator*(const Complex &c) const;
Complex operator-() const;
```

- One restriction with operator overloading support is that SWIG is not able to fully handle operators that aren't defined as part of the class. For example, if you had code like this

```cpp++
class Complex {
    ...
    friend Complex operator+(double, const Complex &c);
    ...
};
```

- then SWIG ignores it and issues a warning. You can still wrap the operator, but you may have to encapsulate it in a special function. For example:

```
%rename(Complex_add_dc) operator+(double, const Complex &);
```

- There are ways to make this operator appear as part of the class using the %extend directive. Keep reading.
- Also, be aware that certain operators don't map cleanly to Python. 
    - For instance, overloaded assignment operators don't map to Python semantics and will be ignored.

<h2 id="2329b407fe1d5482f5e412a6502ecebe"></h2>

### 36.3.12 C++ namespaces

- SWIG is aware of C++ namespaces, but namespace names do not appear in the module nor do namespaces result in a module that is broken up into submodules or packages.

```
%module example

namespace foo {
    int fact(int n);
    struct Vector {
        double x, y, z;
    };
};
```

It works in Python as follows:

```python
>>> import example
>>> example.fact(3)
6
>>> v = example.Vector()
```

- If your program has more than one namespace, name conflicts (if any) can be resolved using %rename

```
%rename(Bar_spam) Bar::spam;
namespace Foo {
    int spam();
}
namespace Bar {
    int spam();
}
```
 
- If you have more than one namespace and your want to keep their symbols separate, consider wrapping them as separate SWIG modules.


<h2 id="3ae5ee54a6d57c34cf29f39e935f13d2"></h2>

### 36.3.13 C++ templates

- C++ templates don't present a huge problem for SWIG.
- However, in order to create wrappers, you have to tell SWIG to create wrappers for a particular template instantiation
- To do this, you use the %template directive. For example:

```
%module example
%{
#include "pair.h"
%}

template<class T1, class T2>
struct pair {
    typedef T1 first_type;
    typedef T2 second_type;
    T1 first;
    T2 second;
    pair();
    pair(const T1&, const T2&);
    ~pair();
};

%template(pairii) pair<int, int>;
```

```python
>>> import example
>>> p = example.pairii(3, 4)
```


<h2 id="375e31e2cbdc8887003fa50adfa38d67"></h2>

### 36.3.14 C++ Smart Pointers

<h2 id="0fd3d38db929aa36de6a011c60d87de1"></h2>

#### 36.3.14.1 The shared_ptr Smart Pointer

<h2 id="584698ebaec253169b5dbc351c353e00"></h2>

#### 36.3.14.2 Generic Smart Pointers

- In certain C++ programs, it is common to use classes that have been wrapped by so-called "smart pointers."
- Generally, this involves the use of a template class that implements operator->() like this:

```
template<class T> class SmartPtr {
    ...
    T *operator->();
    ...
}
```

Then, if you have a class like this,

```cpp++
class Foo {
    public:
        int x;
        int bar();
};
```

A smart pointer would be used in C++ as follows:

```cpp++
SmartPtr<Foo> p = CreateFoo();   // Created somehow (not shown)
...
p->x = 3;                        // Foo::x
int y = p->bar();                // Foo::bar
```

To wrap this in Python, simply tell SWIG about the SmartPtr class and the low-level Foo object. 

Make sure you instantiate SmartPtr using %template if necessary. For example:


```
%module example
...
%template(SmartPtrFoo) SmartPtr<Foo>;
...
```

Now, in Python, everything should just "work":

```python
>>> p = example.CreateFoo()          # Create a smart-pointer somehow
>>> p.x = 3                          # Foo::x
>>> p.bar()                          # Foo::bar
```


<h2 id="8edc31645b1d72709e2a78ce42b80295"></h2>

## 36.5 Cross language polymorphism

<h2 id="299f5530bbe369a25a8a9399abd64a44"></h2>

### 36.5.1 Enabling directors

- The director feature is disabled by default
- To use directors you must make two changes to the interface file

First, add the "directors" option to the %module directive, like this:

```
%module(directors="1") modulename
```

Second, you must use the %feature("director") directive to tell SWIG which classes and methods should get directors. 

The %feature directive can be applied globally, to specific classes, and to specific methods, like this:

```
// generate directors for all classes that have virtual methods
%feature("director");         

// generate directors for all virtual methods in class Foo
%feature("director") Foo;      
```

You can use the %feature("nodirector") directive to turn off directors for specific classes or methods. So for example,

```
%feature("director") Foo;
%feature("nodirector") Foo::bar;
```

Directors can also be generated implicitly through **inheritance**. 

In the following, class Bar will get a director class that handles the methods one() and two() (but not three()):

```cpp++
%feature("director") Foo;
class Foo {
    public:
        Foo(int foo);
        virtual ~Foo();
        virtual void one();
        virtual void two();
};

class Bar: public Foo {
    public:
        virtual void three();
};
```

---

<h2 id="37b33f14f7ff3d5724be48045de26423"></h2>

## 36.6 Common customization features

This section describes some common SWIG features that are used to improve your the interface to an extension module.

<h2 id="8ed34b4d93e1ce67e4c5cdf57ac714f3"></h2>

### 36.6.1 C/C++ helper functions

Sometimes when you create a module, it is missing certain bits of functionality. For example, if you had a function like this

```cpp++
void set_transform(Image *im, double m[4][4]);
```

it would be accessible from Python, but there may be no easy way to call it. For example, you might get errors like this:

```python
>>> a = [
...   [1, 0, 0, 0],
...   [0, 1, 0, 0],
...   [0, 0, 1, 0],
...   [0, 0, 0, 1]]
>>> set_transform(im, a)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  TypeError: Type error. Expected _p_a_4__double
```

The problem here is that there is no easy way to construct and manipulate a suitable double `[4][4]` value to use. 

To fix this, you can write some extra C helper functions. Just use the %inline directive. For example:

```cpp++
%inline %{
    /* Note: double[4][4] is equivalent to a pointer to an array double (*)[4] */
    double (*new_mat44())[4] {
        return (double (*)[4]) malloc(16*sizeof(double));
    }
    void free_mat44(double (*x)[4]) {
        free(x);
    }
    void mat44_set(double x[4][4], int i, int j, double v) {
        x[i][j] = v;
    }
    double mat44_get(double x[4][4], int i, int j) {
        return x[i][j];
    }
%}
```

From Python, you could then write code like this:

```python
>>> a = new_mat44()
>>> mat44_set(a, 0, 0, 1.0)
>>> mat44_set(a, 1, 1, 1.0)
>>> mat44_set(a, 2, 2, 1.0)
...
>>> set_transform(im, a)
```

Admittedly, this is not the most elegant looking approach. However, it works and it wasn't too hard to implement.

It is possible to clean this up using Python code, typemaps, and other customization features as covered in later sections.

<h2 id="73f0c0b516a9a6466ff6f66d16f7aea1"></h2>

### 36.6.2 Adding additional Python code

If writing support code in C isn't enough, it is also possible to write code in Python. 

This code gets inserted in to the .py file created by SWIG. 


```
void set_transform(Image *im, double x[4][4]);

...
/* Rewrite the high level interface to set_transform */
%pythoncode %{
def set_transform(im, x):
    a = new_mat44()
    for i in range(4):
        for j in range(4):
            mat44_set(a, i, j, x[i][j])
    _example.set_transform(im, a)
    free_mat44(a)
%}
```

```python
>>> a = [
...   [1, 0, 0, 0],
...   [0, 1, 0, 0],
...   [0, 0, 1, 0],
...   [0, 0, 0, 1]]
>>> set_transform(im, a)
```

Admittedly, this whole scheme for wrapping the two-dimension array argument is rather ad-hoc. 

There is also %pythonbegin which is another directive very similar to %pythoncode, but generates the given Python code at the beginning of the .py file.

This provides an opportunity to add your own description in a comment near the top of the file as well as Python imports that have to appear at the top of the file, such as "from __future__ import" statements.

The following shows example usage for Python 2.6 to use print as it can in Python 3, that is, as a function instead of a statement:

```
%pythonbegin %{
# This module provides wrappers to the Whizz Bang library
%}

%pythonbegin %{
from __future__ import print_function
print("Loading", "Whizz", "Bang", sep=' ... ')
%}
```

As an alternative to providing a block containing Python code, you can include python code from a file. 

```
%pythoncode "somecode.py"
```

Sometimes you may want to replace or modify the wrapper function that SWIG creates in the proxy .py file. The Python module in SWIG provides some features that enable you to do this.

First, to entirely replace a proxy function you can use %feature("shadow"). For example:

```
%module example

// Rewrite bar() python code

%feature("shadow") Foo::bar(int) %{
def bar(*args):
    #do something before
    $action
    #do something after
%}

class Foo {
public:
    int bar(int x);
};
```

where $action will be replaced by the call to the C/C++ proper method.

Often the proxy function created by SWIG is fine, but you simply want to add code to it without touching the rest of the generated function body. 

For these cases SWIG provides the pythonprepend and pythonappend features which do exactly as their names suggest. 

The pythonprepend feature will insert its value at the beginning of the proxy function, and pythonappend will insert code at the end of the proxy, just before the return statement.


```
%module example

// Add python code to bar() 

%feature("pythonprepend") Foo::bar(int) %{
    #do something before C++ call
%}

%feature("pythonappend") Foo::bar(int) %{
    #do something after C++ call
%}


class Foo {
public:
    int bar(int x);
};
```

Notes: Usually the pythonappend and pythonprepend features are safer to use than the shadow feature.

Also, from SWIG version 1.3.28 you can use the directive forms %pythonappend and %pythonprepend as follows:

```
%pythonprepend Foo::bar(int) %{
    #do something before C++ call
%}

%pythonappend Foo::bar(int) %{
    #do something after C++ call
%}
```

Note that when the underlying C++ method is overloaded, there is only one proxy Python method for multiple C++ methods. 

In this case, only one of parsed methods is examined for the feature. You are better off specifying the feature without the argument list to ensure it will get used, as it will then get attached to all the overloaded C++ methods. For example:

```
%module example

// Add python code to bar()

%pythonprepend Foo::bar %{
    #do something before C++ call
%}

%pythonappend Foo::bar %{
    #do something after C++ call
%}

class Foo {
public:
    int bar(int x);
    int bar();
};
```

<h2 id="d4f88a6538a37f876d6944cfddd37993"></h2>

### 36.6.3 Class extension with %extend

One of the more interesting features of SWIG is that it can extend structures and classes with new methods--at least in the Python interface. 

```
%module example
%{
#include "someheader.h"
%}

struct Vector {
    double x, y, z;
};

%extend Vector {
    char *__str__() {
        static char tmp[1024];
        sprintf(tmp, "Vector(%g, %g, %g)", $self->x, $self->y, $self->z);
        return tmp;
    }
    Vector(double x, double y, double z) {
        Vector *v = (Vector *) malloc(sizeof(Vector));
        v->x = x;
        v->y = y;
        v->z = z;
        return v;
    }
};
```

Now , in Python

```python
>>> v = example.Vector(2, 3, 4)
>>> print v
Vector(2, 3, 4)
```

%extend can be used for many more tasks than this.

For example, if you wanted to overload a Python operator, you might do this:

```
%extend Vector {
    Vector __add__(Vector *other) {
        Vector v;
        v.x = $self->x + other->x;
        v.y = $self->y + other->y;
        v.z = $self->z + other->z;
        return v;
    }
};
```

```python
>>> import example
>>> v = example.Vector(2, 3, 4)
>>> w = example.Vector(10, 11, 12)
>>> print v+w
Vector(12, 14, 16)
```

<h2 id="6a994f76d514c7ea64b0080007f925bc"></h2>

### 36.6.4 Exception handling with %exception

If a C or C++ function throws an error, you may want to convert that error into a Python exception. 

To do this, you can use the %exception directive.

%exception simply lets you rewrite part of the generated wrapper code to include an error check.

In C, a function often indicates an error by returning a status code (a negative number or a NULL pointer perhaps). Here is a simple example of how you might handle that:

```
%exception malloc {
    $action
    if (!result) {
        PyErr_SetString(PyExc_MemoryError, "Not enough memory");
        SWIG_fail;
    }
}
void *malloc(size_t nbytes);
```

In Python,

```python
>>> a = example.malloc(2000000000)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  MemoryError: Not enough memory
```

If a library provides some kind of general error handling framework, you can also use that. For example:

```
%exception {
    $action
    if (err_occurred()) {
        PyErr_SetString(PyExc_RuntimeError, err_message());
        SWIG_fail;
    }
}
```

No declaration name is given to %exception, it is applied to all wrapper functions.

C++ exceptions are also easy to handle. For example, you can write code like this:

```
%exception getitem {
    try {
        $action
    } catch (std::out_of_range &e) {
        PyErr_SetString(PyExc_IndexError, const_cast<char*>(e.what()));
        SWIG_fail;
    }
}

class Base {
public:
    Foo *getitem(int index);      // Exception handled added
    ...
};
```

When raising a Python exception from C, use the PyErr_SetString() function as shown above followed by SWIG_fail . 

The following exception types can be used as the first argument.

```
PyExc_ArithmeticError
PyExc_AssertionError
PyExc_AttributeError
PyExc_EnvironmentError
PyExc_EOFError
PyExc_Exception
PyExc_FloatingPointError
PyExc_ImportError
PyExc_IndexError
PyExc_IOError
PyExc_KeyError
PyExc_KeyboardInterrupt
PyExc_LookupError
PyExc_MemoryError
PyExc_NameError
PyExc_NotImplementedError
PyExc_OSError
PyExc_OverflowError
PyExc_RuntimeError
PyExc_StandardError
PyExc_SyntaxError
PyExc_SystemError
PyExc_TypeError
PyExc_UnicodeError
PyExc_ValueError
PyExc_ZeroDivisionError
```

The language-independent exception.i library file can also be used to raise exceptions. See the SWIG Library chapter.

<h2 id="15f329eb7bd57310ae05525a7560cb18"></h2>

## 36.7 Tips and techniques

Although SWIG is largely automatic, there are certain types of wrapping problems that require additional user input. 

Examples include dealing with output parameters, strings, binary data, and arrays. 

This chapter discusses the common techniques for solving these problems.

<h2 id="53e526b93ef9246ff51cd84f5debb919"></h2>

### 25.8.1 Input and output parameters using primitive pointers and references

A common problem in some C programs is handling parameters passed as simple pointers or references. For example:

```cpp
void add(int x, int y, int *result) {
    *result = x + y;
}
```

or perhaps

```cpp
int sub(int *x, int *y) {
    return *x-*y;
}
```

The typemaps.i library file will help in these situations. For example:

```
%module example
%include "typemaps.i"

void add(int, int, int *OUTPUT);
int  sub(int *INPUT, int *INPUT);
```

In Python, this allows you to pass simple values. For example:

```python
>>> a = add(3, 4)
>>> print a
7
>>> b = sub(7, 4)
>>> print b
3
>>>
```

Notice how the INPUT parameters allow integer values to be passed instead of pointers and how the OUTPUT parameter creates a return result.

If you don't want to use the names INPUT or OUTPUT , use the %apply directive. For example:


```
%module example
%include "typemaps.i"

%apply int *OUTPUT { int *result };
%apply int *INPUT  { int *x, int *y};

void add(int x, int y, int *result);
int  sub(int *x, int *y);
```

---

If a function mutates one of its parameters like this,

```cpp
void negate(int *x) {
    *x = -(*x);
}
```

you can use INOUT like this:

```cpp
%include "typemaps.i"
...
void negate(int *INOUT);
```

```python
>>> a = negate(3)
>>> print a
-3
```

---

The most common use of these special typemap rules is to handle functions that return more than one value.

For example, sometimes a function returns a result as well as a special error code:

```cpp
/* send message, return number of bytes sent, along with success code */
int send_message(char *text, int len, int *success);
```

To wrap such a function, simply use the OUTPUT rule above. For example:

```
%module example
%include "typemaps.i"
%apply int *OUTPUT { int *success };
...
int send_message(char *text, int *success);  // ? where does 'len' go ?
```

Be aware that the primary purpose of the typemaps.i file is to support primitive datatypes. Writing a function like this

```
void foo(Bar *OUTPUT);
```

MAY NOT  have the intended effect since typemaps.i does not define an OUTPUT rule for Bar.

<h2 id="515f4e8a06c359c5238034b0a0855efc"></h2>

### 36.7.2 Simple pointers

If you must work with simple pointers such as int \* or double \* and you don't want to use typemaps.i, consider using the cpointer.i library file. For example:

```
%module example
%include "cpointer.i"

%inline %{
    extern void add(int x, int y, int *result);
%}

%pointer_functions(int, intp);
```

The %pointer_functions(type, name) macro generates five helper functions that can be used to create, destroy, copy, assign, and dereference a pointer. In this case, the functions are as follows:

```cpp
int  *new_intp();
int  *copy_intp(int *x);
void  delete_intp(int *x);
void  intp_assign(int *x, int value);
int   intp_value(int *x);
```

In Python, you would use the functions like this:

```python
>>> result = new_intp()
>>> print result
_108fea8_p_int
>>> add(3, 4, result)
>>> print intp_value(result)
7
```

If you replace %pointer_functions() by %pointer_class(type, name), the interface is more class-like.

```python
>>> result = intp()
>>> add(3, 4, result)
>>> print result.value()
7
```

<h2 id="ea9fec0c4e11762f471b1cffa262b7a4"></h2>

### 36.7.3 Unbounded C Arrays

Sometimes a C function expects an array to be passed as a pointer. For example,

```cpp
int sumitems(int *first, int nitems) {
    int i, sum = 0;
    for (i = 0; i < nitems; i++) {
        sum += first[i];
    }
    return sum;
}
```

To wrap this into Python, you need to pass an array pointer as the first argument. A simple way to do this is to use the carrays.i library file. For example:

```
%include "carrays.i"
%array_class(int, intArray);
```
The %array_class(type, name) macro creates wrappers for an unbounded array object that can be passed around as a simple pointer like int \* or double \*. 
For instance, you will be able to do this in Python:

```python
>>> a = intArray(10000000)         # Array of 10-million integers
>>> for i in xrange(10000):        # Set some values
...     a[i] = i
>>> sumitems(a, 10000)
49995000
```

- The array "object" created by %array_class() does not encapsulate pointers inside a special array object. In fact, there is no bounds checking or safety of any kind (just like in C). 
- Because of this, the arrays created by this library are extremely low-level indeed.
- You can't iterate over them nor can you even query their length. 
- In fact, any valid memory address can be accessed if you want (negative indices, indices beyond the end of the array, etc.). 
- Needless to say, this approach is not going to suit all applications . On the other hand, this low-level approach is extremely efficient and well suited for applications in which you need to create buffers, package binary data, etc.

<h2 id="c5928dddfc2c9487ddc042e45caa4576"></h2>

### 36.7.4 String handling

If a C function has an argument of `char *`, then a Python string can be passed as input. For example:

```
// C
void foo(char *s);
-------
# Python
>>> foo("Hello")
```

Since Python strings are immutable, it is illegal for your program to change the value. In fact, doing so will probably crash the Python interpreter.

If your program modifies the input parameter or uses it to return data, consider using the cstring.i library file 

When functions return a `char *`, it is assumed to be a NULL-terminated string. Data is copied into a new Python string and returned.

If your program needs to work with binary data, you can use a typemap to expand a Python string into a pointer/length argument pair. As luck would have it, just such a typemap is already defined. Just do this:

```
%apply (char *STRING, int LENGTH) { (char *data, int size) };
...
int parity(char *data, int size, int initial);
```

<h2 id="63b4f48acae0ba35e6576fce9fa8fdad"></h2>

### 36.7.5 Default arguments

- C++ default argument code generation is documented in the main Default arguments section
- There is also an optional Python specific feature that can be used called the python:cdefaultargs feature flag
- By default, SWIG attempts to convert C++ default argument values into Python values and generates code into the Python layer containing these values.

For example:

```cpp++
struct CDA {
    int fff(int a = 1, bool b = false);
};
```

From Python this can be called as follows:

```
>>> CDA().fff()        # C++ layer receives a=1 and b=false
>>> CDA().fff(2)       # C++ layer receives a=2 and b=false
>>> CDA().fff(3, True) # C++ layer receives a=3 and b=true
```

The default code generation in the Python layer is:

```python
class CDA(object):
    ...
    def fff(self, a=1, b=False):
        return _default_args.CDA_fff(self, a, b)
```

Adding the feature:

```
%feature("python:cdefaultargs") CDA::fff;
struct CDA {
    int fff(int a = 1, bool b = false);}
```

results in identical behaviour when called from Python, however, it results in different code generation:

```python
class CDA(object):
    ...
    def fff(self, *args):
        return _default_args.CDA_fff(self, *args)
```

The default arguments are obtained in the C++ wrapper layer instead of the Python layer. 

Note that not all default arguments can be converted into a Python equivalent. When SWIG does not convert them, it will generate code to obtain them from the C++ layer as if python:cdefaultargs was specified. This will happen if just one argument cannot be converted into a Python equivalent. This occurs typically when the argument is not fully numeric, such as int(1):

```cpp
struct CDA {
    int fff(int a = int(1), bool b = false);
};
```

**Compatibility Note**: SWIG-3.0.6 introduced the python:cdefaultargs feature. Versions of SWIG prior to this varied in their ability to convert C++ default values into equivalent Python default argument values.

---

<h2 id="2b130f8e243eb10cbc270985854ccbc7"></h2>

## 36.8 Typemaps

This section describes how you can modify SWIG's default wrapping behavior for various C/C++ datatypes using the %typemap directive. 

Before proceeding, it should be stressed that typemaps are not a required part of using SWIG---the default wrapping behavior is enough in most cases.

Typemaps are only used if you want to change some aspect of the primitive C-Python interface or if you want to elevate your guru status.

<h2 id="90a5be3942738a92f3991cb7d19710be"></h2>

### 36.8.1 What is a typemap?

A typemap is nothing more than a code generation rule that is attached to a specific C datatype.

For example, to convert integers from Python to C, you might define a typemap like this:

```cpp
%module example

%typemap(in) int {
  $1 = (int) PyLong_AsLong($input);
  printf("Received an integer : %d\n", $1);
}
%inline %{
extern int fact(int n);
%}
```

- In this case, the "in" method refers to the conversion of input arguments to C/C++
- The datatype int is the datatype to which the typemap will be applied.  
- In this code a number of special variable prefaced by a $ are used
    - The $1 variable is placeholder for a local variable of type int
    - The $input variable is the input object of type PyObject *

When this example is compiled into a Python module, it operates as follows:

```python
>>> from example import *
>>> fact(6)
Received an integer : 6
720
```

In this example, the typemap is applied to all occurrences of the int datatype. You can refine this by supplying an optional parameter name. For example:

```
%module example

%typemap(in) int nonnegative {
  $1 = (int) PyLong_AsLong($input);
  if ($1 < 0) {
    PyErr_SetString(PyExc_ValueError, "Expected a nonnegative value.");
    SWIG_fail;
  }
}
%inline %{
extern int fact(int nonnegative);
%}
```
 
- In this case, the typemap code is only attached to arguments that exactly match int nonnegative.

When you define a typemap for int, that typemap applies to int and qualified variations such as const int. In addition, the typemap system follows typedef declarations. For example:

```
%typemap(in) int n {
  $1 = (int) PyLong_AsLong($input);
  printf("n = %d\n", $1);
}
%inline %{
typedef int Integer;
extern int fact(Integer n);    // Above typemap is applied
%}
```

Typemaps can also be defined for groups of consecutive arguments. For example:

```
%typemap(in) (char *str, int len) {  // 注意这里有个括号
  $1 = PyString_AsString($input);
  $2 = PyString_Size($input);
};

int count(char c, char *str, int len);
```

- When a multi-argument typemap is defined, the arguments are always handled as a single Python object. This allows the function to be used like this
    - notice how the length parameter is omitted

```
>>> example.count('e', 'Hello World')
1
>>>
```

<h2 id="e4f724210edaab8c16c023cca34e2473"></h2>

### 36.8.2 Python typemaps

The previous section illustrated an "in" typemap for converting Python objects to C.

A variety of different typemap methods are defined by the Python module. 

For example, to convert a C integer back into a Python object, you might define an "out" typemap like this:

```
%typemap(out) int {
    $result = PyInt_FromLong((long) $1);
}
```

> A detailed list of available methods can be found in the " Typemaps" chapter.

However, the best source of typemap information (and examples) is probably the Python module itself.

In fact, all of SWIG's default type handling is defined by typemaps. You can view these typemaps by looking at the files in the SWIG library.


<h2 id="e729302bd9b4ccdceabc3c5587c9c140"></h2>

### 36.8.3 Typemap variables

Within typemap code, a number of special variables prefaced with a $ may appear.

A full list of variables can be found in the " Typemaps" chapter. This is a list of the most common variables:

variable  |  describe
--- | --- 
$1 | A C local variable corresponding to the actual type specified in the %typemap directive. For input values, this is a C local variable that's supposed to hold an argument value. For output values, this is the raw result that's supposed to be returned to Python.
$input | A PyObject \* holding a raw Python object with an argument or variable value.
$result | A PyObject \* that holds the result to be returned to Python.
$1_name | The parameter name that was matched.
$1_type | The actual C datatype matched by the typemap.
$1_ltype | An assignable version of the datatype matched by the typemap (a type that can appear on the left-hand-side of a C assignment operation).  This type is stripped of qualifiers and may be an altered version of $1_type. All arguments and local variables in wrapper functions are declared using this type so that their values can be properly assigned.
$symname | The Python name of the wrapper function being created. 


<h2 id="427eb1b71112c2157f5763050c06240b"></h2>

### 36.8.4 Useful Python Functions

When you write a typemap, you usually have to work directly with Python objects. The following functions may prove to be useful.

Python Integer Functions

```
PyObject *PyInt_FromLong(long l);
long      PyInt_AsLong(PyObject *);
int       PyInt_Check(PyObject *);
```

Python Floating Point Functions

```
PyObject *PyFloat_FromDouble(double);
double    PyFloat_AsDouble(PyObject *);
int       PyFloat_Check(PyObject *);
```

Python String Functions

```
PyObject *PyString_FromString(char *);
PyObject *PyString_FromStringAndSize(char *, lint len);
int       PyString_Size(PyObject *);
char     *PyString_AsString(PyObject *);
int       PyString_Check(PyObject *);
```

Python List Functions

```
PyObject *PyList_New(int size);
int       PyList_Size(PyObject *list);
PyObject *PyList_GetItem(PyObject *list, int i);
int       PyList_SetItem(PyObject *list, int i, PyObject *item);
int       PyList_Insert(PyObject *list, int i, PyObject *item);
int       PyList_Append(PyObject *list, PyObject *item);
PyObject *PyList_GetSlice(PyObject *list, int i, int j);
int       PyList_SetSlice(PyObject *list, int i, int , PyObject *list2);
int       PyList_Sort(PyObject *list);
int       PyList_Reverse(PyObject *list);
PyObject *PyList_AsTuple(PyObject *list);
int       PyList_Check(PyObject *);
```

Python Tuple Functions

```
PyObject *PyTuple_New(int size);
int       PyTuple_Size(PyObject *);
PyObject *PyTuple_GetItem(PyObject *, int i);
int       PyTuple_SetItem(PyObject *, int i, PyObject *item);
PyObject *PyTuple_GetSlice(PyObject *t, int i, int j);
int       PyTuple_Check(PyObject *);
```

Python Dictionary Functions

```
PyObject *PyDict_New();
int       PyDict_Check(PyObject *);
int       PyDict_SetItem(PyObject *p, PyObject *key, PyObject *val);
int       PyDict_SetItemString(PyObject *p, const char *key, PyObject *val);
int       PyDict_DelItem(PyObject *p, PyObject *key);
int       PyDict_DelItemString(PyObject *p, char *key);
PyObject* PyDict_Keys(PyObject *p);
PyObject* PyDict_Values(PyObject *p);
PyObject* PyDict_GetItem(PyObject *p, PyObject *key);
PyObject* PyDict_GetItemString(PyObject *p, const char *key);
int       PyDict_Next(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue);
Py_ssize_t PyDict_Size(PyObject *p);
int       PyDict_Update(PyObject *a, PyObject *b);
int       PyDict_Merge(PyObject *a, PyObject *b, int override);
PyObject* PyDict_Items(PyObject *p);
```

Python File Conversion Functions

```
PyObject *PyFile_FromFile(FILE *f);
FILE     *PyFile_AsFile(PyObject *);
int       PyFile_Check(PyObject *);
```

---

<h2 id="c6ea35fbba443421bec5662d98c4a56d"></h2>

## 36.9 Typemap Examples

This section includes a few examples of typemaps.

For more examples, you might look at the files "python.swg" and "typemaps.i " in the SWIG library.

<h2 id="a0b62f2001104e30cea14cc3d978eb00"></h2>

### 36.9.1 Converting Python list to a char \*\*

A common problem in many C programs is the processing of command line arguments, which are usually passed in an array of NULL terminated strings.

The following SWIG interface file allows a Python list object to be used as a char \*\* object.

TODO

<h2 id="e1aba4dac0c081ca9e1c9689b39f0b9d"></h2>

### 36.9.2 Expanding a Python object into multiple arguments

Suppose that you had a collection of C functions with arguments such as the following:

```cpp
int foo(int argc, char **argv);
```

In the previous example, a typemap was written to pass a Python list as the char \*\*argv. This allows the function to be used from Python as follows.


```python
>>> foo(4, ["foo", "bar", "spam", "1"])
```

尽管这是可行的, 但是指定参数计数(4) 有点笨拙。

To fix this, a multi-argument typemap can be defined. This is not very difficult--you only have to make slight modifications to the previous example:

TODO

With the above typemap in place, you will find it no longer necessary to supply the argument count. This is automatically set by the typemap code. For example:

```python
>>> foo(["foo", "bar", "spam", "1"])
```

If your function is overloaded in C++, for example:

```cpp
int foo(int argc, char **argv);
int foo();
```

don't forget to also provide a suitable [typecheck typemap for overloading](http://www.swig.org/Doc3.0/SWIGDocumentation.html#Typemaps_overloading) such as:

```
%typecheck(SWIG_TYPECHECK_STRING_ARRAY) (int argc, char **argv) {
  $1 = PyList_Check($input) ? 1 : 0;
}
```

<h2 id="b0b0ba8683c797f778cbd3d40d7ecd4b"></h2>

### 36.9.3 Using typemaps to return arguments

A common problem in some C programs is that values may be returned in arguments rather than in the return value of a function. For example:

```cpp
/* Returns a status value and two values in out1 and out2 */
int spam(double a, double b, double *out1, double *out2) {
  ... Do a bunch of stuff ...
  *out1 = result1;
  *out2 = result2;
  return status;
}
```

TODO

<h2 id="9e2e54e3b2717314d68b1cf84e329a8e"></h2>

### 36.9.4 Mapping Python tuples into small arrays


In some applications, it is sometimes desirable to pass small arrays of numbers as arguments. For example :

```cpp
extern void set_direction(double a[4]);       // Set direction vector
```

This too, can be handled used typemaps as follows :

```
// Grab a 4 element array as a Python 4-tuple
%typemap(in) double[4](double temp[4]) {   // temp[4] becomes a local variable
  int i;
  if (PyTuple_Check($input)) {
    if (!PyArg_ParseTuple($input, "dddd", temp, temp+1, temp+2, temp+3)) {
      PyErr_SetString(PyExc_TypeError, "tuple must have 4 elements");
      SWIG_fail;
    }
    $1 = &temp[0];
  } else {
    PyErr_SetString(PyExc_TypeError, "expected a tuple.");
    SWIG_fail;
  }
}
```

This allows our set_direction function to be called from Python as follows :

```python
>>> set_direction((0.5, 0.0, 1.0, -0.25))
```

Since our mapping copies the contents of a Python tuple into a C array, such an approach **would not be recommended for huge arrays**, but for small structures, this approach works fine.


<h2 id="7933ae9020049f067c537253e1610be8"></h2>

### 36.9.5 Mapping sequences to C arrays

Suppose that you wanted to generalize the previous example to handle C arrays of different sizes. To do this, you might write a typemap as follows:

TODO

<h2 id="6568ccb24614cc5e9c0d0730be8a3837"></h2>

### 36.9.6 Pointer handling

Occasionally, it might be necessary to convert pointer values that have been stored using the SWIG typed-pointer representation.

Since there are several ways in which pointers can be represented, the following two functions are used to safely perform this conversion:

```cpp
int SWIG_ConvertPtr(PyObject *obj, void **ptr, swig_type_info *ty, int flags)
```

Converts a Python object obj to a C pointer.

TODO


----

<h2 id="50d52dd929a75bb9b0f4afb0b7d879e1"></h2>

# 常见问题

 1. base class unknown, ignore
    - provide the header file which define that needed class as well the module name 
    - i.e., `%import(module="paramengine") "ParamEngine.h"`
 2. virtual method
    - use the feature "director"
 3. class field declare as  `CLASS &name`
    - and initialized by constructor , but the swig will wrap xxxx_set method , and will leader to compile error
    - use %immutable to tell swig not to wrapxxxx_set method
 4. template class
    - define template for further using
    - %template(BehaviorPlannerBase_A) BehaviorPlannerBase< BehaviorAttackData >;





