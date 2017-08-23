...menustart

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

...menuend


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

```c++
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

```c++
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

```c++
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

```c++
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

```c++
Complex &operator=(const Complex &c);

Complex operator+=(const Complex &c) const;
Complex operator+(const Complex &c) const;
Complex operator-(const Complex &c) const;
Complex operator*(const Complex &c) const;
Complex operator-() const;
```

 - One restriction with operator overloading support is that SWIG is not able to fully handle operators that aren't defined as part of the class. For example, if you had code like this

```c++
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

```c++
class Foo {
    public:
        int x;
        int bar();
};
```

A smart pointer would be used in C++ as follows:

```c++
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

```c++
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

```c++
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

```c++
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




