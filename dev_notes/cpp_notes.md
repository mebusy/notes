...menustart

- [Reference](#63d5049791d9d79d86e9a108b0a999ca)
    - [When should we use reference over pointer and vice versa ?](#15fd66c7db63e7108a1fd09bbd1d2cde)
- [friend function](#1444dfb74703eaade9660d234e949cf6)
- [difference between plain Enum and Enum class in C++ ?](#a0ab3cec5d48671dbfb8ec94af9abce6)
- [How to prevent someone from taking address of your object?](#b481cf231c83433850a9093fcad42a7b)
- [How to prevent someone from inheriting from your class ?](#bf5f87d9fd968d2a044309009ce2139b)
- [How to return mulitple values ?](#5e91e30f56f2071d31406f011e3e7181)
- [How to assign object to int ?](#74fed14e181e19aa7cda3c0fc0a41b08)
- [Why use `override` keyword ?](#f9e9c42f6b9d3238ad453faa75e19196)
- [Why copy constructor take argument as reference ?](#87759128b7fe62b12b7a07d2947f909a)
- [Function Hiding in C++](#a78a7dd142e4347a3c846d15ef09f39c)

...menuend


<h2 id="63d5049791d9d79d86e9a108b0a999ca"></h2>


# Reference

1. alias , same memory address
2. Reassignment is NOT possible with reference
3. can NOT make a reference with value NULL

<h2 id="15fd66c7db63e7108a1fd09bbd1d2cde"></h2>


## When should we use reference over pointer and vice versa ?

- Use reference in function parameter and return type(best use for reference)
    1. Pass big objects ( avoid object value copy )
        - 
        ```cpp
        void fun(BigClass& obj) {
            obj->_data ;
        }
        int main() {
            BigClass obj;
            fun(obj);
            return 0;
        }
        ```
    2. To modify local variable of caller function 
        - 
        ```cpp
        void change(int & x) {
            x = 10 ;
        }
        int main() {
            int x = 5 ;
            change(x); 
            return 0;
        }
        ```
    3. To achieve run-time polymorphism in a function
- Use pointers in algorithms and data structures like linked list, tree, graph etc...
    - Why?
        1. sometime we put NULL/nullptr in node
        2. sometime we change pointers to point some another node


<h2 id="1444dfb74703eaade9660d234e949cf6"></h2>


# friend function

- mainly used for giving rights explicitly 
    - i.e. used for testing 
- friend function don't have the permission to access the parent Class.
    - you invited a friend , he can enter into your room, but not your parents' room.

<h2 id="a0ab3cec5d48671dbfb8ec94af9abce6"></h2>


# difference between plain Enum and Enum class in C++ ?

```cpp
// plain Enum
enum Color1{red, green, blue};
Color1 c1 = red ;
```

```cpp
// Class Enum
enum class Color2{red, green, blue};
Color2 c2 = Color2::red ;
```

<h2 id="b481cf231c83433850a9093fcad42a7b"></h2>


# How to prevent someone from taking address of your object?

- A1. Overlaod `&` operateor and keep it private
    - 
    ```cpp
    class Base {
        int x; 
    public:
        Base() {}
        Base(int x):x{x} {} 
    private:
        Base* operator & () {
            return this ;
        }
    } ;
    ```
- A2. Delete `&` operator from you class.
    - 
    ```cpp
    class Base {
        int x ;
    public:
        Base () {} 
        Base (int x):x{x} {}
        Base* operator & () = delete ;
    } ;
    ```

<h2 id="bf5f87d9fd968d2a044309009ce2139b"></h2>


# How to prevent someone from inheriting from your class ?

- just use `final` keyword 
- 
```cpp
class Base final {
    ...
}
```

<h2 id="5e91e30f56f2071d31406f011e3e7181"></h2>


# How to return mulitple values ?

1. use some struct/class and fill the values in that.
2. use std::tuple in c++11


<h2 id="74fed14e181e19aa7cda3c0fc0a41b08"></h2>


# How to assign object to int ?

```cpp
class Base {
    ...
public:
    operator int() const {
        return var; 
    }
}
```

<h2 id="f9e9c42f6b9d3238ad453faa75e19196"></h2>


# Why use `override` keyword ?

```cpp
class Base {
    ...
public:
    virtual void fun() {
        ...
    }
}
class Derived: public Base {
    ...
public:
    void fun() override {
        ...
    }
}
```

1. Testing become easy with this ... ( easy maintainance )
2. Compile-time check can be performed. ( future error could be reduced )
    - `void fun(int a)` will pass compilation,  while `void fun(int a) override` failed.


<h2 id="87759128b7fe62b12b7a07d2947f909a"></h2>


# Why copy constructor take argument as reference ?

```cpp
    Foo(const Foo obj) {
        ...
    }
```

A: To avoid infinite recursive.


<h2 id="a78a7dd142e4347a3c846d15ef09f39c"></h2>


# Function Hiding in C++

- in a class, function with same name and different parameters will be overloaded.
- in a base class and a derived class,  same name function will be hidden from derived class.




