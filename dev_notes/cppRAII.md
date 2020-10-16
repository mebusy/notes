
# RAII: Resource Acquisition Is Initialization

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

## Introduce copy assignment 

Whenever you write a destructor, you probably need to write a copy constructor **and a copy assignment operator**.

```cpp
    NaiveVector& operator=(const NaiveVector& rhs) {
        // this demonstrates the copy and swap idiom.
        // we need to write swap.

        // reuse constructor initialize
        NaiveVector copy = rhs;
        copy.swap(*this);
        return *this;
    }
```

## The Rule of Three

- If your class directly manages some kind of resource(such as a new'ed pointer), then you almost certainly need to hand-write three special number functions:
    1. A **destructor** to free the resource
    2. A **copy constructor** to copy the resource
    3. A **copy assignment operator** to free the left-hand resource and copy the right-hand one.
- Use the copy-and-swap idiom to implement assignent

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

## The Rule of Zeor

- If you class does not directly manage any resource, but merely uses library components such as vector and string, then you should strive to write **NO** special member functions. Default them all!
    - Let the compiler implicitly generate a defaulted destructor
    - Let the compiler generate the copy constructor
    - Let the compiler generate the copy assignment operator
    - (But your own swap might improve performance)
        - if you write your own friend, overload, non-member `swap` with 2 arguments, then standard library algorithms will can that `swap`.


## Prefer Rule of Zero when possible






