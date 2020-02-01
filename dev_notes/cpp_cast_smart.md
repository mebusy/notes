
## static_cast

static_cast means it works on compile-time.  

Finding the code is easy. 

Error found at compile-time.

1. replacing C-Style casting 
    - 
    ```c
    a = f ; // hard to find in code in case your app failed
    a = static_cast<int>(f);
    ```
2. more restrictive than C-Style
    - 
    ```c
    char c ;
    int *p = (int*)&c ;
     *p = 5 ; // PASS at compile-time but may FAIL at run-time.
    int *ip = static_cast<int*>*(&c) ; // FAIL , compile-time error
    ```
3. avoid cast from derived to private base pointer.
    - 
    ```c
    class Base();
    class Derived: private Base{};
    int main() {
        Derived d1;
        Base *bp1 = (Base*)&d1 ; // Allowed at compile-time
        Base *bp2 = static_cast<Base*>(&d1); // Not allowed at compile-time
    }
    ```
3. Use for all upcasts, but never use for confused down cast
    - 
    ```c
    Base *bp1 = static_cast<Base*>(&d1); //OK
    Base *bp2 = static_cast<Base*>(&d2); //OK

    Derived1 *d1p = static_cast<Derived1*>(bp2) ; //NEVER do that though compiling ok
    // should use dynamic_cast instead.
    ```
4. should be prefered when converting to `void*` OR from `void*`
    - 
    ```c
    int i = 10 ;
    void *v = static_cast<void*>(&i);
    int *ip = static_cast<int*>(v);
    ```


## dynamic_cast

Dynamic_cast is used for only 1 reason:  to find out correct down-cast(base -> derived).

- SYNTAX: `dynamic_cast<new_type>(expression)`
- NOTES:
    1. Need at least on virtual function in base class
        - works only on polymorphic base class
        - because it uses this information to decide about wrong down-cast
    2. If the cast is successful, dynamic_cast returns a value of new_type
    3. If the cast faild , and 
        - new_type is a pointer, it returns a null pointer of that type
        - new_type is a reference type, it throws an exception.


```c
Derived1 d1;
Base *bp = dynamic_cast<Base*>(&d1);

Derived2 *dp2 = dynamic_cast<Derived2*>(bp);
if (dp2 == nullptr)  ... ;

try {
    Derived1 &r1 = dynamic_cast<Derived1&>(d1) ;  
}
catch( std::exception& e) {
    ...
}
```

- using this cast has run-time overhead, because it checks object types at run-time using RTTI.
- if we are sure that we will never cast to wrong object then we should always avoid this cast and use static_cast instead.

## Smart Pointers

- NOTES
    1. smart pointer is a class which wraps a raw pointer, to manage the life time of the pointer
    2. The most fundamental job of smart pointer is to remove the chances of memory leak.
    3. It makes sure that the object is deleted if it is not reference any more.
- TYPES
    1. unique_ptr
        - Allows only one owner of the underlying pointer
    2. shared_ptr
        - Allows multiple owners of the same pointer ( Reference count is maintained )
    3. weak_ptr
        - It is special type of shared_ptr which doesn't count the reference.
        - The best use of this weak pointer when there is a cyclic dependency when we use shared_pointer. 


### Unique Pointer 

- NOTES
    1. unique_ptr is a class template, provided by c++11 to prevent memory leak
    2. unique_ptr wraps a raw pointer in it, and de-allocates the raw pointer when unique_ptr object goes out of scope.
    3. similar to actual pointers we can use `->` and `*` on the object of unique_ptr, because it is overloaded in unique_ptr class.
    4. when exception comes then also it will de-allocated the memory hence no memory leak
    5. Not only object we can create array of objects of unique_ptr.
- OPERATIONS
    - release, reset, swap, get, get_deleter


```cpp
#include<iostream>
#include<memory>
using namespace std;

class Foo {
    int x ;
public :
    explicit Foo(int x): x{x} {}
    int getX() {return x;}

    ~Foo() { cout << "Foo Dest" << endl ; }
}

int main() {
    // Foo *f = new Foo(10;
    // cout << f->getX() << endl ;
    // memory leak in case forgot to call `delete`

    // you don't have to call `delete` 
    // on pointers you created 
    std::unique_ptr<Foo> p(new Foo(10)) ;
    cout << p->getX() << endl ;
    
    // exception safe
    std::unique_ptr<Foo> p2 = make_unique<Foo>(20); 

    // p1 = p2 ; // FAIL: can not copy ownership
    unique ptr<Foo> p3 = std::move(p1); // PASS: moving ownership is allowed. 
    // now p1 is equal to nullptr

    Foo* p = p3.get() ;
    Foo* p4 = p3.release() ; // now p3 is nullptr.
    
    p2.reset(p4);  // the pervious pointer handled by p2 is deleted.
}
```


### Shared Pointer 

- NOTES
    1. can share the ownership of object
    2. It keep a reference count to maintain how many shared_ptr are pointing to the same object, and once last shared_ptr goes out of scope then the managed object gets deleted.
    3. shared_ptr is threads safe and not thread safe ?
        a. control block(which maintains the reference count) is thread safe 
        b. managed object is not.
    4. There are 3 ways shared_ptr will destory managed object 
        a. If the last shared_ptr goes out of scope
        b. If you initialize shared_ptr with some other shared_ptr
        c. If you reset shared_ptr


```cpp
int main() {
    std::shared_ptr<Foo> sp(new Foo(100)) ;
    cout << sp.use_count() << endl ; // 1

    // copy value
    std::shared_ptr<Foo> sp1 = sp ;
    cout << sp.use_count() << endl ; // 2

    // reference OR pointer (not value) doesn't work 
    std::shared_ptr<Foo> &sp2 = sp ;
    cout << sp.use_count() << endl ; // 2
}
```

## Weak Pointer 

- NOTES
    1. if we say unique_ptr is for unique ownership, and shared_ptr is for shared ownership, then weak_ptr is for non-ownership 
    2. It actually reference to an object which is managed by shared_ptr
    3. A weak_ptr is created as a copy of shared_ptr
    4. We have to convert weak_ptr to shared_ptr in order to use the managed object
    5. It is used to remove cyclic dependency between shared_ptr


```cpp
int main() {
    auto sharedPtr = std::make_shared<int>(100) ;
    std::weak_ptr<int> weakPtr(sharedPtr) ;
    
    // check whether this shade pointer is existing or not 
    // if exists , convert to an shared_ptr to prevent the managed object from deallocation.
    if (std::shared_ptr<int> sharedPtr1 = weakPtr.lock()) {
        std::cout << sharedPtr1.use_count() << std::endl; // 2 
    } else {
        std::cout << "don't get the resource" << std::endl;
    }
}
```






