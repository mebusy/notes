
# Reference

1. alias , same memory address
2. Reassignment is NOT possible with reference
3. can NOT make a reference with value NULL

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


# friend function

- mainly used for giving rights explicitly 
    - i.e. used for testing 
- friend function don't have the permission to access the parent Class.
    - you invited a friend , he can enter into your room, but not your parents' room.

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

# How to prevent someone from inheriting from your class ?

- just use `final` keyword 
- 
```cpp
class Base final {
    ...
}
```

# How to return mulitple values ?

1. use some struct/class and fill the values in that.
2. use std::tuple in c++11


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


# Why copy constructor take argument as reference ?

```cpp
    Foo(const Foo obj) {
        ...
    }
```

A: To avoid infinite recursive.


# Function Hiding in C++

- in a class, function with same name and different parameters will be overloaded.
- in a base class and a derived class,  same name function will be hidden from derived class.




