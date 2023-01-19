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

```c++
#include <iostream>
const double pi = 3.141593;
int main() {
    const double radius = 1.5;
    const double area = pi * radius * radius;
    std::cout << area;
}
```

If only there was some way to make a compile-time constant…

```c++
#include <iostream>
constexpr double pi = 3.141593;
int main() {
    const double radius = 1.5;
    const double area = pi * radius * radius;
    std::cout << area;
}
```

Or even generate it at compile-time.

```c++
#include <iostream>
constexpr double calculate_pi() {
    return 22. / 7; // or something more clever
}
constexpr double pi = calculate_pi();
int main() {
    const double radius = 1.5;
    const double area = pi * radius * radius;
    std::cout << area;
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

The whole template syntax is a bit bulky. Is there any way to simplify that?  C++20 Concepts !


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


<h2 id="5390d4b827185948e9f9a87999bd453a"></h2>

## #22: Guaranteed Copy Elision (C++17)

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





