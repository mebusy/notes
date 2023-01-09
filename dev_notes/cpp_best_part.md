
# The Best Parts of C++

https://www.youtube.com/watch?v=iz5Qx18H6lg


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


## #11 Return type deduction for normal functions (C++14)

```c++
auto get_thing() {
    struct Thing {};
    return Thing{};
}
```


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


## #13 Generic And Variadic Lambdas (C++14)

Create implicit templates by simply using the auto keyword.

```c++
#include <vector>
auto lambda = [/*captures*/](auto... params) {
    return std::vector<int>{params...};
};
```

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





