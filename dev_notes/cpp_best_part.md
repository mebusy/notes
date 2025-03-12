[](...menustart)

- [The Best Parts of C++](#2e13d677842eef043db60ae766d4a90d)
    - [#7 List Initialization  (C++11)](#09de7e0b1431dff7e5148fca1c932198)
    - [#8 Variadic Templates (C++11)](#28687fab746f50332ca0c853b55dd99a)
    - [#9 constexpr (C++ 14)](#e5f12eb8ae249a4ae062f20f3a08f46c)
    - [#10 auto (C++11)](#f85a38333552c1843e898be015951483)
    - [#11 Return type deduction for normal functions (C++14)](#0d8471844167aafee522ae1607244135)
    - [#12 Lambdas (C++11)](#45a91169c8c9f7427b688c6fe7673df6)
    - [#13 Generic And Variadic Lambdas (C++14)](#76005f0b9720124fdc4d06cf098f17fa)
    - [#14 range-based for loop (C++11)](#47f24a12632f1bc48ebb43dabd31844a)
    - [#15 Structured Bindings (C++17)](#d36ee5721e2136e8485d007b6908053d)
    - [#20 Class Template Argument Deduction (C++17)](#5104199984b3db0a9e5cb95cbb760f4a)
    - [#22: Guaranteed Copy Elision (C++17)](#5390d4b827185948e9f9a87999bd453a)

[](...menuend)


<h2 id="2e13d677842eef043db60ae766d4a90d"></h2>

# The Best Parts of C++

- youtube video: https://www.youtube.com/watch?v=iz5Qx18H6lg
- slides: https://nbviewer.jupyter.org/github/mebusy/cppcontalk/blob/main/pdfs/back_to_basics_the_best_parts_of_cpp__jason_turner__cppcon_2019.pdf


<h2 id="09de7e0b1431dff7e5148fca1c932198"></h2>

## #7 List Initialization  (C++11)

```c++
template <typename VT> std::array<VT, 2> get_data(const VT &v1, const VT &v2) {
    std::array<VT, 2> data;
    data[0] = v1;
    data[1] = v2;
    return data;
}
```

If only there was a way to initialize the array values in one step…

```c++
template <typename VT> std::array<VT, 2> get_data(const VT &v1, const VT &v2) {
    std::array<VT, 2> data{v1, v2}; // list initialization
    return data;
}
```

Code simplifies now to this, look better

```c++
template <typename VT> std::array<VT, 2> get_data(const VT &v1, const VT &v2) {
    return {v1, v2};
}
```


<h2 id="28687fab746f50332ca0c853b55dd99a"></h2>

## #8 Variadic Templates (C++11)


```c++
... 

template <typename VT>
std::array<VT, 3> get_data(const VT &v1, const VT &v2, const VT &v3) {
    return {v1, v2, v3};
}

template <typename VT>
std::array<VT, 4> get_data(const VT &v1, const VT &v2, const VT &v3,
                           const VT &v4) {
    return {v1, v2, v3, v4};
}
```

If only there was a way to avoid all this code duplication…


```c++
// require at least one parameter and it sets the type
// could be simplified more with c++17
template <typename VT, typename... Params>
std::array<VT, sizeof...(Params) + 1> get_data(const VT &v1,
                                               const Params &...params) {
    return {v1, params...};
}
```


<h2 id="e5f12eb8ae249a4ae062f20f3a08f46c"></h2>

## #9 constexpr (C++ 14)

- const
    - const 关键字用于声明 **运行时常量**，即变量的值在 **编译时不一定已知**，但在程序运行期间不可修改。
    - const 修饰的变量可以在运行时初始化，只要其值不会被修改即可。
    - const 变量的值不一定是编译期可计算的，它可能是由运行时计算得出的。
    ```c++
    const int a = 10; // 编译时常量
    int b = getValue();
    const int c = b; // 运行时常量，b 的值只有在运行时才能确定
    ```
- constexpr
    - constexpr 关键字用于声明 **编译时常量**，即它的值在 **编译期必须能确定**。
    - constexpr 变量 必须 由 **编译时可求值的表达式** 初始化。
    ```c++
    #include <iostream>

    constexpr int getConstValue() {
        return 84/2;  // 编译时计算
    }

    int main() {
        constexpr int a = 10;          // 编译时常量
        constexpr int b = getConstValue(); // 编译时计算

        std::cout << a << " " << b << std::endl;
        return 0;
    }
    ```


<h2 id="f85a38333552c1843e898be015951483"></h2>

## #10 auto (C++11)

```c++
#include <iostream>
constexpr auto calculate_pi() { ///
    return 22 / 7;              // or something more clever
}
constexpr auto pi = calculate_pi();
int main() {
    const auto radius = 1.5;
    const auto area = pi * radius * radius;
    std::cout << area;
}
```


<h2 id="0d8471844167aafee522ae1607244135"></h2>

## #11 Return type deduction for normal functions (C++14)

```c++
auto get_thing() {
    struct Thing {};
    return Thing{};
}
```


<h2 id="45a91169c8c9f7427b688c6fe7673df6"></h2>

## #12 Lambdas (C++11)

```c++
auto lambda = [/*captures*/](int param1){ return param1 * 10; };
```

```c++
#include <iostream>
#include <string>
template <typename Map>
void print_map(const Map &map, const std::string key_desc = "key",
               const std::string value_desc = "value") {
    for_each(begin(map), end(map),
             [&](const auto &data) { ///
                 std::cout << key_desc << ": '" << data.first << "' "
                           << value_desc << ": '" << data.second << "'\n";
             });
}
```

Capture Syntax | Description
--- | ---
`[&]` | Capture all used variables by **reference**
`[=]` | Capture all used variables by **value**
`[x, &y]` | Capture `x` by **value**, `y` by **reference**
`[this]` | Capture `this` pointer (used in member functions)
`[&x, =y]` | **C++20**: Capture `x` by reference, `y` by value




<h2 id="76005f0b9720124fdc4d06cf098f17fa"></h2>

## #13 Generic And Variadic Lambdas (C++14)

Create implicit templates by simply using the auto keyword.

```c++
#include <vector>
auto lambda = [/*captures*/](auto... params) {
    return std::vector<int>{params...};
};
```

<h2 id="47f24a12632f1bc48ebb43dabd31844a"></h2>

## #14 range-based for loop (C++11)

Iterates over all elements in a container. Works with anything that has begin() and end() members/functions and C-style arrays.

```c++
for (const auto &value : container) {
    // loops over each element in the container
}
```

```c++
#include <iostream>
#include <string>
template <typename Map>
void print_map(const Map &map, const std::string &key_desc = "key",
               const std::string &value_desc = "value") {
    for (const auto &data : map) {
        std::cout << key_desc << ": '" << data.first << "' " << value_desc
                  << ": '" << data.second << "'\n";
    }
}
```

<h2 id="d36ee5721e2136e8485d007b6908053d"></h2>

## #15 Structured Bindings (C++17)

```c++
const auto &[elem1, elem2] = some_thing;
```

```c++
#include <iostream>
#include <string>
template <typename Map>
void print_map(const Map &map, const std::string &key_desc = "key",
               const std::string &value_desc = "value") {
    for (const auto &[key, value] : map) /// structured binding
    {
        std::cout << key_desc << ": '" << key << "' " << value_desc << ": '"
                  << value << "'\n";
    }
}
```

The whole template syntax is a bit bulky. Is there any way to simplify that?

```c++
#include <iostream>
#include <string>

// C++20's auto concept or further constrained to something that
// has values that can be destructured into 2 elements.
void print_map(const auto &map, const std::string &key_desc = "key",
               const std::string &value_desc = "value") {
    for (const auto &[key, value] : map) {
        std::cout << key_desc << ": '" << key << "' " << value_desc << ": '"
                  << value << "'\n";
    }
}
```


## #17 std::string_view (C++17)

But there’s a potential ineﬀiciency hiding here.

We are constructing a std::string from a const char * for no particular reason.

If only there was a way to observe string-like things without actually constructing a std:string...

```c++
#include <iostream>
#include <string_view>

void print_map(const auto &map, const std::string_view &key_desc = "key",
               const std::string_view &value_desc = "value") {
    for (const auto &[key, value] : map) {
        std::cout << key_desc << ": '" << key << "' " << value_desc << ": '"
                  << value << "'\n";
    }
}
```

- A non-owning “view” of a string like structure.
    ```c++
    #include <string_ view>
    std::string_view sv{some_string_like_thing}; // no copy
    ```


## #18: Text Formatting (C++20)

std::cout is quite verbose, relatively slow, and diﬀicult to reason about. If only there was some easier way of formatting our output…

```c++
#include <format>
#include <string_view>

void print_map(const auto &map, const std::string_view &key_desc = "key",
               const std::string_view &value_desc = "value") {
    for (const auto &[key, value] : map) {
        std::puts(std::format("{}: '{}' {}: '{}'\n", key_desc, key, value_desc, value).c_str());
    }
}
```

- A subset of the excellent {fmt} library is being worked on for C++20, allowing for formatting of strings with positional, named, and python/printf style formatting options.
    ```c++
    #include <format>
    std::string s = fmt::format("I'd rather be {1} than {0}. " , "right" , "happy");
    // s == "I'd rather be happy than right. "
    ```




## #19 Ranges


Bringing together algorithms, text formatting, concepts, etc, our map printing routine might look something like this in C++20:

```c++
#include <format>
#include <string_view>

void print_map(const auto &map, const std::string_view &key_desc = "key",
               const std::string_view &value_desc = "value") {

    const auto print_key_value = [&](const auto data) {
        const auto &[key, value] = data;
        std::puts(std::format("{}: '{}' {}: '{}'\n", key_desc, key, value_desc, value).c_str());
    };

    for_each(begin(map), end(map), print_key_value);
}
```

Now if only there was some way to not have to do this begin(map), end(map) stuﬀ when using algorithms…

```c++
#include <format>
#include <string_view>

void print_map(const auto &map, const std::string_view &key_desc = "key",
               const std::string_view &value_desc = "value") {

    const auto print_key_value = [&](const auto data) {
        const auto &[key, value] = data;
        std::puts(std::format("{}: '{}' {}: '{}'\n", key_desc, key, value_desc, value).c_str());
    };

    std::ranges::for_each(map, print_key_value);
}
```




<h2 id="5104199984b3db0a9e5cb95cbb760f4a"></h2>

## #20 Class Template Argument Deduction (C++17)

```c++
std::vector vec{1,2,3}; // now possible
```

For types like `array` this has an even bigger impact.

```c++
#include <array>

template <typename... Params> 
auto get_data(const Params &...params) {
    return std::array{params...};
}
```

note: This might make using this function harder as it would result in a compile-time error if the types differ.

And with C++20’s auto concept we might get:

```c++
auto get_data(const auto & ... params)
    return std::array{params...};
}
```

The only problem now is that this code requires the types to be copyable.


## #21 rvalue References




If only there was a way to forward arguments and avoid copies…

```c++
auto get_data(auto && ... params) {
    return std::array{std::forward<decltype(params)>(params)...};
}
```

No unnecessary copies of params, guaranteed copy/move elision of return value.

- decltype is a C++ keyword that is used to **deduce the type of an expression at compile time**.


<h2 id="5390d4b827185948e9f9a87999bd453a"></h2>

## #22: Guaranteed Copy Elision (C++17)

- Copy Elision 和 Move Elision 都是 C++ 中的 优化技术，旨在避免不必要的复制和移动操作，从而提升程序的性能。这两种优化都属于 编译器优化，也就是说，编译器可以在特定情况下自动跳过拷贝和移动操作。
- Copy Elision（拷贝消除）
    - Copy Elision 是指编译器在某些情况下直接避免了对象的拷贝构造函数或赋值操作符的调用。
    - 常见的 Copy Elision 场景：
        - 返回值优化 (RVO, Return Value Optimization)： 当一个函数返回一个局部变量时，编译器通常会避免调用拷贝构造函数，直接在调用者的内存中构造返回值。
        - 函数参数传递时的优化： 当传递对象给函数时，如果传递的是临时对象（右值），编译器可能会跳过拷贝构造，而是直接将对象移动。
    - C++17 中的强制拷贝消除：
        - 在 C++17 中，引入了 强制拷贝消除（Mandatory Copy Elision）。根据 C++17 标准，在特定情况下（如返回局部变量）编译器必须执行拷贝消除，无法再对这些情况进行拷贝构造。
- Move Elision（移动消除）
    - Move Elision 是指在某些情况下，编译器也会避免调用移动构造函数或移动赋值操作符。和拷贝消除类似，移动消除的目的是避免不必要的资源转移操作。
    - 在 C++11 以后，编译器可以在右值传递时使用 移动语义，从而避免不必要的拷贝操作。移动消除发生时，编译器会直接跳过移动操作。
    - 常见的 Move Elision 场景：
        - 返回值优化（RVO）与移动构造函数： 当函数返回一个右值时，编译器会跳过对返回值的移动操作，直接在调用者的内存中构造返回值。
            ```c++
            MyClass createObject() {
                return MyClass(); // MyClass()是一个临时的无名对象，是右值，编译器会跳过移动构造
            }
            ```
            - 在此情况下，编译器会尝试 消除移动操作，直接在调用方内存中构造对象，避免移动构造函数的调用.
        - C++17 中的强制移动消除：
            - 在 C++17 中，如果函数返回局部变量的右值，编译器会强制消除移动操作，直接返回对象，类似于拷贝消除。



-----------

- Compilers have “always” done copy elision on return values, but C++17 guarantees it in some situations:

```c++
struct S {
    S() = default;
    S(S &&) = delete;
    S(const S &) = delete;
};
auto s_factory() {
    return S{}; // compiles in C++17, neither a copy nor a move
}
```

- This lets us teach simply “avoid naming return values” and you get the optimal code in all situations.


This was a copy on return in C++98 (But all compilers implemented copy elision, so it worked).

```c++
Double_Data get_data() {
    Double_Data data(3);
    data.data[0] = 1.1; data.data[1] = 2.2; data.data[2] = 3.3;
    return data; // copy, which means what ?
}
```

In **c++11**, it's a move, but by defining a destructor we made it a copy

```c++
Double_Data get_data() {
    Double_Data data(3);
    data.data[0] = 1.1; data.data[1] = 2.2; data.data[2] = 3.3;
    return data; // move 
}
```

We got double free :(  (Default move constructor will copy the pointer.)

If only there was some way to disable problematic operations…

```c++
#include <cstddef>
struct Double_Data {
    Double_Data(const std::size_t size) : data(new double[size]) { }
    ~Double_Data() { delete [] data; }
    Double_Data(Double_Data &&) = delete;
    Double_Data(const Double_Data &) = delete;
    Double_Data &operator=(Double_Data &&) = delete;
    Double_Data &operator=(const Double_Data &) = delete;
    double *data; 
};
```

Not very useful at the moment, but we know it’s safe.

## #23: Defaulted and Deleted Functions 

- Any special member function can be explicitly `= default`
- Any function can be `= delete`
- This can make you API harder to use wrong
    ```c++
    struct S {
        // by providing a constructor we have implicitly disable the default constructor
        S(int) {}
        // explicitly default the default constructor
        S() = default;
    };
    ```

If only there was a way of not even having to think about heap allocated memory…(other than containers mentioned previously, use those of course!)


## #24: `std::unique_ptr` and `std::make_unique`

```c++
#include <cstddef>
#include <memory>


struct Double_Data {
    Double_Data(const std::size_t size) 
        : data(std::make_unique<double[]>(size)) {
    }
    std::unique_ptr<double[]> data;
}
```

- Automatic, safe, very diﬀicult to use incorrectly.
- Interestingly, relies on:
    - `= delete` special member functions
    - destructor
    - r-value references
- And plays nicely with guaranteed copy/move elision for factory functions.

------

Let's make a quick sum function.

```c++
template <typename... T>
auto sum(const T &... t) {
    // sum recursively ?
}
```

We can do it with an interesting `initializer_list` trick.

```c++
#include <initializer_list>

template <typename First, typename ... T>
auto sum(const First &first, const T &... t) {
    // trick was first published by Sean Parent and Eric Niebler
    auto result = first;
    (void)std::initializer_list<int>{(result += t, 0)...};
    return result;
}
```

Avoids the recursion but fixes the result type as the type of the first parameter.

Corrected type version:

```c++
#include <initializer_list>
#include <type_traits>

template <typename First, typename ... T>
auto sum(const First &first, const T &... t) {
    typename std::common_type<First, T...>::type result = first;
    (void)std::initializer_list<int>{(result += t, 0)...};
    return result;
}
```

If only there was some way to ask the compiler to sum up the parameters for us…

## #25 Fold Expressions (C++17)


```c++
template <typename... T>
auto sum(const T &... t) {
    return (t + ...);
}
```

Fold expressions are for use in variadic expansions and can be used with any common operator.

-------


## Key C++ Features

- C++98
    1. A C++ Standard
    2. `const`
    3. Deterministic Object Lifetime and Destruction
    4. Templates
    5. Algorithms and Standard Template Library
- C++11
    1. std::array
    2. List Initialization
    3. Variadic Templates
    4. `constexpr`
    5. `auto`
    6. Lambdas
    7. Range-based for loop
    8. rvalue references
    9. Defaulted and Deleted Functions
    10. `std::unique_ptr`
- C++14
    1. relaxed `constexpr`
    2. generic and variadic lambdas
    3. return type deduction for normal functions
    4. `std::make_unique`
- C++17
    1. Structured Bindings
    2. `std::string_view`
    3. Class Template Argument Deduction
    4. Guaranteed Copy Elision
    5. Fold Expressions
- C++20
    1. Concepts
    2. Text Formatting
    3. Ranges


