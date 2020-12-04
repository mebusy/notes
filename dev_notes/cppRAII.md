...menustart

- [RAII: Resource Acquisition Is Initialization](#f26eff55207e7d3e75dd433fb3bea50e)
    - [Class that manage resource](#89704b558d620a42da6f3fb287013337)
    - [A naive implementation of vector](#68d0de8134af58f84b26b54cce847329)
    - [Introducint the destructor](#3c0181679d945ebbb3b7e09bb65e1f7a)
    - [NaiveVector still has bugs, through](#c8bd322b3370a0cf6065967dada9dd9e)
    - [Introducing the copy constructor](#659fccd5f72eb5a0894644b8a1d6116c)
    - [Initialization is not assignment](#9bf86d3ea58605d5d1282b315e293b11)
    - [Assignment has the same problem](#093cffc689195cc53c30f62f4cbfa080)
    - [Introduce copy assignment](#7d22f4f9692217cf8fe16b77085d5704)
    - [The Rule of Three](#0ad44ce48a18ef8472213cc56b1af701)
    - [Why copy and swap ?](#134e6efbd59956afa739a02a8bbfcf12)
    - [Copy-and-swap to the rescue !](#bc49b8902d39605644e716a7ad6b25cf)
    - [RAII and exception safety](#99d36ab8ca82649dd45d031ec7b51af7)
    - [Deleted special member functions](#7fc345ca021f12885ee1a6584eb355fa)
    - [Defaulted special member functions](#6b8e4e759f7b6317b37053e154ec2cca)
    - [The Rule of Zeor](#f9e9f688971ef1d1ba03fcf81bf64ffc)
    - [Prefer Rule of Zero when possible](#dbc1ae88fff14526302363b01d66c487)
    - [Introducing rvalue references](#e7b7d62d43b6ea858a52373f4788f1a3)
    - [Rvalues won't be missed](#d768889d7e020d0d98995f6a0b767a00)
    - [The Rule of Five](#f011a8e9e70f15150907034b63f4968b)
    - [Copy-and-swawp leads to duplication(code)](#aa3b8ba4a468ede3379e377b3bfac4bf)
    - [By-value assignment operator ?](#2ea42900f804221f5c10869163cd9567)
    - [The Rule of Four ( and a half )](#057d1268e3059ec7f5d776868d57b2cd)
    - [No longer naive vector](#d38145fd1cbf6cb4abce34d34dd7b58c)
    - [Closer-to-Rule-of-Zero vector](#9b5bf33fbaca11d81d47400f567e9ca8)
    - [True Rule-of-Zero Vector](#0ffb8af72f459c3d1dd7890bd93a2695)
    - [Examples of resource management](#4714fa18ade679a29c7f1014d8c8e18a)

...menuend


<h2 id="f26eff55207e7d3e75dd433fb3bea50e"></h2>


# RAII: Resource Acquisition Is Initialization

<h2 id="89704b558d620a42da6f3fb287013337"></h2>


## Class that manage resource 

A "resource" for our purposes, is anything that requires special(manual) management.

C++ programs can manage different kinds of "resource".

- Allocated memory (malloc/free, new/delete, new[]/delete[])
- POSIX file handle (open/close)
- C FILE handle (fopen/fclose)
- Mutex locks (pthread_mutex_lock/pthread_mutex_unlock)
- C++ threads (spawn/join)
- Objective-C resource-counted objects (retain/release)

Some of these resources are intrinsically "unique" (e.g. mutex locks), and some are "duplicable" (e.g. heap allocations; POSIX file handles can be dup'ed).

For our purposes so far, this doesn't really matter. 

RAII can apply on not only heap allocations, but also any kind of resource.

<h2 id="68d0de8134af58f84b26b54cce847329"></h2>


## A naive implementation of vector

```cpp
class NaiveVector {
    int *ptr_ ;
    size_t size_ ;
public:
    // This constructor correctly (if trivially) 
    // initialize sptr_ with a resource.
    NaiveVector() : ptr_(nullptr), size_(0) {}
    void push_back(int newvalue) {
        // new
        int *newptr = new int[size+1];
        std::copy(ptr_, ptr_ + size_, newptr);
        // delete
        delete [] ptr_ ;
        ptr_ = newptr; 
        ptr_[size++] = newvalue;
    }
}
```

- This implementation has **memory leak**.

<h2 id="3c0181679d945ebbb3b7e09bb65e1f7a"></h2>


## Introducint the destructor

```cpp
class NaiveVector {
    int *ptr_ ;
    size_t size_ ;
public:
    // This constructor correctly (if trivially) 
    // initialize sptr_ with a resource.
    NaiveVector() : ptr_(nullptr), size_(0) {}
    void push_back(int newvalue) {
        // new
        int *newptr = new int[size+1];
        std::copy(ptr_, ptr_ + size_, newptr);
        // delete
        delete [] ptr_ ;
        ptr_ = newptr; 
        ptr_[size++] = newvalue;
    }
    ~NaiveVector() { delete [] ptr_ ;}
}
```

<h2 id="c8bd322b3370a0cf6065967dada9dd9e"></h2>


## NaiveVector still has bugs, through

```cpp
{
    NaiveVector v;
    v.push_back(1);
    {
        // make a copy, using the default constructor
        // just copies each members, 
        // a copy of size, a copy of the pointer.
        // so my new pointer points the same place as my old pointer
        NaiveVector w = v;
    }
    // that memory has already been freed. 
    // Undefined behavior
    std::cout << v[0] << "\n";

    // double free
}
```

<h2 id="659fccd5f72eb5a0894644b8a1d6116c"></h2>


## Introducing the copy constructor

Wheneven you write a destructor, you probably need to write a copy construct as well.

The destructor is responsible for freeing resources to avoid **leaks**.

The copy constructor is responsible for duplicating resources to avoid **double frees**.

This applies to memory, or any other resource you might be managing.

```cpp

class NaiveVector {
    int *ptr_ ;
    size_t size_ ;
public:
    // This constructor correctly (if trivially) 
    // initialize sptr_ with a resource.
    NaiveVector() : ptr_(nullptr), size_(0) {}
    ~NaiveVector() { delete [] ptr_ ;}

    NaiveVector( const NaiveVector& rhs ) {
        ptr_ = new int[rhs.size_];
        size_ = rhs.size_ ;
        std::copy( rhs.ptr_, rhs.ptr_ + size_, ptr_ );
    }
}
```

**This is why c++ has copy constructors!**

<h2 id="9bf86d3ea58605d5d1282b315e293b11"></h2>


## Initialization is not assignment

Don't confuse the `=` for **initialization** with **assignment**!.

- 
    ```cpp
    NaiveVector w=v;
    ```
    - an initialzation (**constrcutor**) of a **new** object.
    - It calls a copy constructor.
- 
    ```cpp
    NaiveVector w;
    w = v;
    ```
    - an **assignment** to the **existing** object w.
    - It calls the assignment operator.

<h2 id="093cffc689195cc53c30f62f4cbfa080"></h2>


## Assignment has the same problem

```cpp
{
    NaiveVector v;
    v.push_back(1);
    {
        NaiveVector w;
        // default operator= of NaiveVector
        w = v;
    }
    // that memory has already been freed. 
    // Undefined behavior
    std::cout << v[0] << "\n";

    // double free
}
```

<h2 id="7d22f4f9692217cf8fe16b77085d5704"></h2>


## Introduce copy assignment 

Whenever you write a destructor, you probably need to write a copy constructor **and a copy assignment operator**.

```cpp
    NaiveVector& operator=(const NaiveVector& rhs) {
        // this demonstrates the copy and swap idiom.
        // we need to write swap.

        // reuse copy constructor
        NaiveVector copy = rhs;
        copy.swap(*this);
        return *this;
    }
```

<h2 id="0ad44ce48a18ef8472213cc56b1af701"></h2>


## The Rule of Three

- If your class directly manages some kind of resource(such as a new'ed pointer), then you almost certainly need to hand-write three special number functions:
    1. A **destructor** to free the resource
    2. A **copy constructor** to copy the resource
    3. A **copy assignment operator** to free the left-hand resource and copy the right-hand one.
- Use the copy-and-swap idiom to implement assignent
    - the stardard library also provide swap method ?

<h2 id="134e6efbd59956afa739a02a8bbfcf12"></h2>


## Why copy and swap ?

You might simply overwrite each menber one at a time, like this.

```cpp
    NaiveVector& NaiveVector::operator=(const NaiveVector& rhs) {
        delete [] ptr_;
        ptr_ = new int[rhs.size_];
        size_ = rhs.size_;
        std::copy( rhs.ptr_, rhs.ptr_ + size_, ptr_ );
        return *this;
    }
```

But this code is not rebust against **self-assignment** `v=v;`.

Not self-move but still troublesome(for templated or recursive data structures.

```cpp
struct A {
    NaiveVector <shared_ptr<A>> m;
}

NaiveVector <shared_ptr<A>> v;
v = v[1] -> m;
```

<h2 id="bc49b8902d39605644e716a7ad6b25cf"></h2>


## Copy-and-swap to the rescue !

```cpp
    NaiveVector& operator=(const NaiveVector& rhs) {
        // reuse constructor initialize
        NaiveVector copy(rhs);
        copy.swap(*this);
        return *this;
    }
```

- We make a complete copy of rhs before the 1st modification to `*this`.
- So any aliasing relationship between rhs and `*this` cannot trip us up.

<h2 id="99d36ab8ca82649dd45d031ec7b51af7"></h2>


## RAII and exception safety

"Resource Acquisition Is Initialization." The slogan is about initialization, but its meaning is really about **cleanup**.

Destructors help us write code that is robust against exceptions

- C++ supports try/catch and throw
- when an exception is thrown, the runtime looks "up the call stack" until it finds a suitable catch handler for the type of the exception being thrown.Assuming it find one...
- The runtime performs **stack unwinding**. For every local scope between the throw and the catch handler, the runtime invokes the destructors of all local variables in that scope.
- To avoid leaks, place all your cleanup code in **destructors**.


The code below call `new`, but fails to call `delete` when an exception is thrown. Therefor it leaks memory. This is not good RAII code, no, it's bad code.

```cpp
try {
    int * arr = new int[4];
    throw std::runtime_error( "for example" );
    delete []arr ; // cleanup
} catch ( ... ) {
    ...
}
```

- Below code won't fail to call delete when an exception is thrown. But it is still relatively dangerous code because RAIIPtr has a defaulted copy constructor.

```cpp
struct RAIIPtr {
    int *ptr_;
    RAIIPtr(int *p) : ptr(p) {}
    ~RAIIPtr{ delete [] ptr_; }
};

int main() {
    try {
        RAIIPtr arr = new int[4];
        throw std::runtime_error( "for example" );
    } catch ( ... ) {
        ...
    }
}
```

So, how are we going to fix that? Do I want "RAIIPtr" to be copyable?

<h2 id="7fc345ca021f12885ee1a6584eb355fa"></h2>


## Deleted special member functions

We can improve our RAIIPtr by making it **non-copyable**.

When a function definition has the body `=delete;` instead of a curly-braced compound statement, the compiler will rejuect calls to that function at compile time.


```cpp
struct RAIIPtr {
    int *ptr_;
    RAIIPtr(int *p) : ptr_(p) {}
    ~RAIIPtr() { delete [] ptr_ ; }

    RAIIPtr( const RAIIPtr& ) = delete;
    RAIIPtr& operator=(const RAIIPtr&) = delete;
};
```

What else can we do with a member function besides deleting ?

<h2 id="6b8e4e759f7b6317b37053e154ec2cca"></h2>


## Defaulted special member functions

When a special member function has the body `=default;` instead of a curly-braced compound statement, the compiler will create a defaulted version of that function, just as were implicitly generated.

**Explicitly defaulting** your special members can help your code to be self-documenting.
    - "Yes, I considered the fact that I might need a copy constructor, or I might need an assignment operator, or I might need a destructor... and I have decided that the default ones work fine."

```cpp
class Book {
public:
    Book(const Book&) = default;
    Book& operator=(const Book&) = default;
    ~Book() = default;
}


```

<h2 id="f9e9f688971ef1d1ba03fcf81bf64ffc"></h2>


## The Rule of Zeor

- If you class does not directly manage any resource, but merely uses library components such as vector and string, then you should strive to write **NO** special member functions. Default them all!
    - Let the compiler implicitly generate a defaulted destructor
    - Let the compiler generate the copy constructor
    - Let the compiler generate the copy assignment operator
    - (But your own swap might improve performance)
        - if you write your own friend, overload, non-member `swap` with 2 arguments, then standard library algorithms will can that `swap`.


<h2 id="dbc1ae88fff14526302363b01d66c487"></h2>


## Prefer Rule of Zero when possible

There are 2 kinds of well-designed value-semantic C++ classes:

- **Business-logic classes** that do not manually manage any resources, and follow the Rule of Zero.
    - They delegate the job of resource management to data member of types such as `std::string`
- **Resource-management clases** (small, single-purpose) that follow the Rule of Three.
    - Acquire the resource in each constructor; free the resource in your destructor; copy-and-sway in your assignment operator.


<h2 id="e7b7d62d43b6ea858a52373f4788f1a3"></h2>


## Introducing rvalue references

- C++11 introduces **rvalue reference** type
- The references we've seen so far are **lvalue** references.

- `int&` is an **lvalue reference** to an int
- `int&&` (two ampersands) is an **rvalue reference** to an int
- As a general rule, lvalue reference parameters do not bind to rvalues, and rvalue reference parameters do not bind to lvalues.
- Special case for backward compatibility: a const lvalue reference will happily bind to an rvalue.

```cpp
void f(int&):   f(i);   // OK   
                f(42);  // ERROR
void g(int&&);  g(i);   // ERROR
                g(42);  // OK
void h(const int&); h(i);   // OK
                    h(42);  // OK!
```


<h2 id="d768889d7e020d0d98995f6a0b767a00"></h2>


## Rvalues won't be missed

Combine this with overload resolution...

```cpp
void foo(const std::string&); // takes lvalues
void foo(std::string&&);      // takes rvalues

std::string s = "hello";
foo(s);             // call foo #1
foo(s+" world");    // expressing call foo #2
foo("hi");          // call foo #2
foo(std::move(s));  // call foo #2
```

The most common application of rvalue references is the **move constructor**.

```cpp
class NativeVector {
    // copy constructor
    NaiveVector(const NaiveVector& rhs) {
        // new int is slow
        ptr_ = new int[rhs.size_];
        size_ = rhs.size_;
        // std::copy is slow
        std::copy(rhs.ptr_, rhs.ptr_+size_ , ptr_;
    }
    // The move constructor doesn;t need to do either
    // of those slow things!
    NaiveVector(NaiveVector&& rhs) {
        ptr_ = std::exchange( rhs.ptr_, nullptr );
        size_ = std::exchange( rhs.size_, 0);
    }
};
```

- Each STL container type has a move constructor in addition to its copy constructor.


<h2 id="f011a8e9e70f15150907034b63f4968b"></h2>


## The Rule of Five 

- If your class directly manages some kind of resource(such as a new'ed pointer), then you may need to hand-write **five** special member functions for correctness and performance:
    1. A **destructor** to free the resource
    2. A **copy constructor** to copy the resource
    3. A **copy assignment operator** to free the left-hand resource and copy the right-hand one.
    4. A **move constructor** to transfer ownership of the resource
    5. A **move assignment operator** to free the left-hand resource and transfer ownership of the right-hand one.

<h2 id="aa3b8ba4a468ede3379e377b3bfac4bf"></h2>


## Copy-and-swawp leads to duplication(code)

How do I write a MOVE assignment operator using copy-and-swap?

Rather than write these 2 assignment operators, whose code is almost identical ...

```cpp
    NaiveVector& operator=(const NaiveVector& rhs) {
        // reuse copy constructor
        NaiveVector copy(rhs);
        copy.swap(*this);
        return *this;
    }
    NaiveVector& operator=(const NaiveVector& rhs) {
        // reuse the move constructor
        NaiveVector copy(std::move(rhs));
        copy.swap(*this);
        return *this;
    }
```

<h2 id="2ea42900f804221f5c10869163cd9567"></h2>


## By-value assignment operator ?

So we had some duplication here. We had 2 bits of code that looked exactly the same. 

And c++ gives us a tool for eliminating code that looks exactly the same. It's templates... But that would be crazy. We're not going to do templates.

What if we just wrote one assignment operator and leave the copy up to our caller? 

I'm not aware of any problems with this idiom. However, it is relatively uncommon; writing copy assignment and move assignment separately is more frequently seen. In particular, the STL always writes them separately.

```cpp
    NaiveVector& NaiveVector::operator=(NaiveVector copy) {
        copy.swap(*this);
        return *this;
    }
```

<h2 id="057d1268e3059ec7f5d776868d57b2cd"></h2>


## The Rule of Four ( and a half )

- If your class directly manages some kind of resource(such as a new'ed pointer), then you may need to hand-write **four** special member functions for correctness and performance:
    1. A **destructor** to free the resource
    2. A **copy constructor** to copy the resource
    3. A **move constructor** to transfer ownership of the resource
    4. A **by-value assignment operator** to free the left-hand resource and transfer ownership of the right-hand one.
        - A nonmumber **swap** function, and ideally a mumber version too

<h2 id="d38145fd1cbf6cb4abce34d34dd7b58c"></h2>


## No longer naive vector

```cpp
#include <utility>
#include <algorithm>

class Vec {
    int *ptr_ ;
    size_t size_ ;

public:
    // copy constructor
    Vec(const Vec& rhs) {
        ptr_ = new int[rhs.size_];
        size_ = rhs.size_ ;
        std::copy( rhs.ptr_, rhs.ptr_ + size_, ptr_ );
    }
    ~Vec() {
        delete [] ptr_;
    }

    // move constructor
    Vec(Vec&& rhs) noexcept {                    // rvalue reference c++11
        ptr_ = std::exchange( rhs.ptr_, nullptr ); // std::exchange  c++14
        size_ = std::exchange( rhs.size_, 0 );
    }

    // by-value assignment operator
    Vec& operator=(Vec copy) {
        copy.swap(*this);
        return *this;
    }

    // two-argument swap, to make your type efficiently "std::swappable"
    friend void swap( Vec& a, Vec& b ) noexcept {
        a.swap(b);
    }
    // member swap too for simplicity
    void swap(Vec& rhs) noexcept {
        using std::swap;
        swap(ptr_, rhs.ptr_ );
        swap(size_, rhs.size_);
    }
} ;
```

<h2 id="9b5bf33fbaca11d81d47400f567e9ca8"></h2>


## Closer-to-Rule-of-Zero vector

```cpp
#include <utility>
#include <algorithm>

class Vec {
    std::unique_ptr<int[]> uptr_ ;
    size_t size_ ;

public:
    // copy constructor
    Vec(const Vec& rhs) {
        uptr_ = std::make_unique<int[]>(rhs.size_);
        size_ = rhs.size_ ;
        // need do some special for copy resource
        // because unique_ptr is not copyable by design
        // std::copy( rhs.ptr_, rhs.ptr_ + size_, ptr_ );
    }
    ~Vec() = default;

    // move constructor
    Vec(Vec&& rhs) noexcept = default;

    // no changed
    // by-value assignment operator 
    Vec& operator=(Vec copy) {
        copy.swap(*this);
        return *this;
    }

    // no changed
    // two-argument swap, to make your type efficiently "std::swappable"
    friend void swap( Vec& a, Vec& b ) {
        a.swap(b);
    }

    // nochanged
    // member swap too for simplicity
    void swap(Vec& rhs) noexcept {
        using std::swap;
        swap(uptr_, rhs.uptr_ );
        swap(size_, rhs.size_);
    }
} ;
```

<h2 id="0ffb8af72f459c3d1dd7890bd93a2695"></h2>


## True Rule-of-Zero Vector 

```cpp
#include <vector>

class Vec {
    std::vector<int> vec_ ;

    // copy constructor
    Vec(const Vec& rhs) = default;
    // move constructor
    Vec(Vec&& rhs) noexcept = default;
    // by-value assignment operator 
    Vec& operator=(const Vec& rhs) = default;
    Vec& operator=(Vec&& rhs) = default;
    ~Vec() = default;

    // two-argument swap, to make your type efficiently "std::swappable"
    friend void swap( Vec& a, Vec& b ) {
        a.swap(b);
    }
    // member swap too for simplicity
    void swap(Vec& rhs) noexcept {
        vec_.swap(rhs.vec_) ;
    }
} ;
```

You have not your default constructor now, but you can totally have other constructors.

<h2 id="4714fa18ade679a29c7f1014d8c8e18a"></h2>


## Examples of resource management

unique_ptr manages a raw pointer to a uniquely owned heap allocation.

- **Destructor** frees the resource
    - call `delete` on the raw pointer
- **Copy constructor** copies the resource
    - Copying doesn't make sense. We `=delete` this member function
- **Move constructor** transfers ownership of the resource
    - Transfers the raw pointer, then nulls out the right-hand side
- **Copy assignment operator** frees the left-hand resource and copies the right-hand one
    - Copying doesn't make sense. We `=delete` this member function
- **Move assignment operator** frees the left-hand resource and transfers ownership of the right-hand one
    - Calls `delete` on the left-hand ptr, transfers, then nulls out the right-hand ptr


shared_ptr manages a reference count.

- **Destructor** frees the resource
    - Decrements the refcount (and maybe cleans up if the refcount is now zero)
- **Copy constructor** copies the resource
    - Increments the refcount
- **Move constructor** transfers ownership of the resource
    - Leaves the refcount the same, then disengages the right-hand side
- **Copy assignment operator** frees the left-hand resource and copies the right-hand one
    - Decrements the old refcount, increments the new refcount
- **Move assignment operator** frees the left-hand resource and transfers ownership of the right-hand one
    - Decrements the oldf refcount, then disengages the right-hand side.





