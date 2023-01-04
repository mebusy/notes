
# Modern C++


https://www.youtube.com/watch?v=9mZw6Rwz1vg&list=PLgnQpQtFTOGRM59sr3nSL8BmeMZR9GCIA&index=5


## Modern C++: Build and Tools (Lecture 1, I. Vizzo, 2020)

###  Compilation flags

- `-std=c++17`, `-o`, etc
- Enable all warnings, treat them as errors
    - `-Wall, -Wextra, -Werror`
- Optimization options
    - `-O0`  -- no optimizations [default]
    - `-O3` or `-Ofast`  -- full optimizations
- Keep debugging symbols
    - `-g`



### Header file

- `#pragma once`
    - In the C and C++ programming languages, `#pragma once` is a non-standard but widely supported preprocessor directive designed to cause the current source file to be included only once in a single compilation.
        ```hpp
        #progma once

        struct foo {
            int member;
        };
        ```
    - `#pragma once` serves the same purpose as **include guards**, but with several advantages

- include guards
    ```hpp
    #ifndef GRANDPARENT_H
    #define GRANDPARENT_H

    struct foo {
        int member;
    };

    #endif /* GRANDPARENT_H */ 
    ```


### Libraries

- Create a static library with
    - `ar rcs libname.a module.o module.o ...`
- Static libraries are just archives just like zip/tar/...
- Linking: to use a library we need
    1. A header file `library_api.h`
    2. The compiled library object `libmylibrary.a`

- Use modules and libraries
    - compile modules, `-c` to assemble and generate object file
        ```bash
        c++ -std=c++17 -c tools.cpp -o tools.o
        ```
    - organize modules into libraries
        ```bash
        ar rcs libtools.a tools.o <other_modules.o ...>
        ```
    - link libraries when building code
        ```bash
        c++ -std=c++17 main.cpp -L . -ltools -o main
        ```
        - `-L <dir>` tell compile to search libraries in this path
        - `-l` specify the library you want to link


### Build Systems

- They began as `shell` scripts
- They turn into `MakeFiles`
- And now into MetaBuild Systems like `CMake`
    - Accept it, CMake is not a build system
    - It's a build system generator
    - You need to use an actual build system like `Make` of `Ninja`


### Build a CMake project

- **Build process** from the user's perspective
    1. `cd <project_folder>`
    2. `mkdir build`
    3. `cd build`
    4. `cmake ..`
    5. `make`
- The build process is completely defined in `CMakeLists.txt`
- And childrens src/CMakeLists.txt, etc
    <details>

    <summary>
    <b>First CMakeLists.txt</b>
    </summary>

    ```cmake
    # first CMakeLists.txt
    cmake_minimum_required(VERSION 3.1)  # Mandatory.
    project(first_project)  # Mandatory.
    set(CMAKE_CXX_STANDARD 17)  # Optional.
    # export compile commands in a json file
    set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # Optional. important


    # tell cmake where to look for *.hpp, *.h files
    include_directories(include/)

    # create library "libtools"
    add_library(tools src/tools.cpp)  # creates libtools.a

    # create executable "main"
    add_executable(main src/main.cpp)  # creates main

    # tell the linker to link "main" with "libtools"
    target_link_libraries(main tools)
    ```

    </details>

- More CMake directive
    - set cxx flags
        ```cmake
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror")  # Optional.
        ```
    - set debug  & optimization
        ```cmake
        set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")
        ```
    - set build type if not set
        ```cmake
        if(NOT CMAKE_BUILD_TYPE)
          set(CMAKE_BUILD_TYPE "Release")
        endif()
        ```
- User pre-compiled library
    - For example, given `libtools.so` it can be used in the project as follows
        ```cmake
        # find library named tools in
        find_library(TOOLS
                    NAMES tools
                    PATHS ${LIBRARY_OUTPUT_PATH}
        )
        # use it for linking
        target_link_libraries(first_project ${TOOLS})
        ```
- Search for some_pkg.cmake file and load it
    ```cmake
    # search for some_pkg.cmake file and load it
    find_package(some_pkg REQUIRED)
    ```


## Modern C++: Core C++ (Lecture 2, I. Vizzo, 2020)

### Range for loop

- Iterating over a standard containers like array or vector has simple syntax
- Avoid mistakes with indices
- added in c++11
    ```cpp
    for (const auto& value: container) {
        // this happens for each value in the container
    }
    ```

### c++17, Iterating map in a pythonic way

- New in c++17
    ```cpp
    #include <map>

        std::map<char, int> my_dict{{'a', 1}, {'b', 2}};
        for (const auto &[key, value] : my_dict) {
            std::cout << key << " " << value << std::endl;
        }
    ```

- Similar to
    ```python
    for key, value in my_dict.items():
        print(key, value)
    ```


### References to variables

- We can create a **reference** to any variable
    ```cpp
    float& ref = original_variable;
    std::string& hello_ref = hello;
    ```
- Reference is part of type:  variable `ref` has type `float&`
- Whatever happens to a reference happens to the variable and vice versa
- Yields performance gain as references avoid **copying data**.


### stringstream

```cpp
    std::stringstream filename("205.txt");

    int num = 0;
    std::string ext;

    // split the string stream using simple syntax
    filename >> num >> ext;

    std::cout << "num: " << num << std::endl; // 205
    std::cout << "ext: " << ext << std::endl; // .ext
```


## Modern C++: C++ Functions (Lecture 3, I. Vizzo, 2020)

### string

- `#include <string>`
    ```cpp
    const std::string source("copy this!");
    std::string dest = source;
    ```

### Return type 

#### Automatic return type deduction C++14

```cpp
auto GetDictionary() {
    return std::map<char, int> my_dict{{'a', 1}, {'b', 2}};
}
```

#### return multiple value like python

- with the introduction of structured binding in c++17 you can now:
    ```cpp
    #include <tuple>

    auto Foo() {
        return make_tuple("Super Variable", 5);
    }

    int main() {
        auto [name, value] = Foo();
        ...
    }
    ```

#### WARNING: Never return reference to locally variables !!!


#### Argument List 

```cpp
void f(type arg1, type arg2) {
    // f holds a copy of arg1 and arg2 } 
}

void f(type& arg1, type& arg2) {
    // f holds a reference of arg1 and arg2 } 
    // f could possibly change the content of arg1 or arg2
}

void f(const type& arg1, const type& arg2) {
    // f can't change the content of arg1 or arg2
}
```


#### Default Arguments

- Only **set in declaration**, not in definition
- Cons:
    - Evaluated upon every call
    - Values are hidden in declaration
    - Can lead to unexpected behavior when overused
- Only use them when readability gets much better.

#### Passing big objects

- **Pass by reference** to avoid copy
- **Avoid using non-const ref**
    - use const refs to ensure the object passed in won't be modified unexpectedly
    - non-const refs are mostly used in older code written before c++11


#### Namespaces

- helps avoiding name conflicts
- group the project into logical moduels
    ```cpp
    namespace module_1 {
        int SomeFunc() {}
    }
    ```
    ```cpp
    namespace module_2 { int SomeFunc() {} }
    ```

- **Avoid** using namespace <name>
    ```cpp
    // Avoid !!!
    using namespace std;
    ```
- Only use what you need
    ```cpp
    using std::cout;  // explicitly use cout.
    using std::endl;
    ```
- **Never** use `using namespace <name>` in *.hpp files
    - Prefer using explicit `using` even in *.cpp files

#### Nameless namespace

- If you find yourself relying on some constants in a file and these constants should not be seen in any other file, put them into a **nameless namespace** on the top of this file
    ```cpp
    namespace {
        const int kLocalImportantInt = 13;
        const int kLocakImportantFloat = 13.0f;
    } // nameless
    ...
    ```

## Modern C++: The C++ STL Library (Lecture 4, I. Vizzo, 2020)

### std::array

- `#include <array>` to use std::array
- Store a collection of items of **same type**
- Create from data: `array<float, 3> arr = {1.0f, 2.0f, 3.0f};`
- Access items with `arr[i]`
- Number of stored items: `arr.size()`
- Useful access aliases:
    - First item: `arr.front() == arr[0]`
    - Last item: `arr.back() == arr[arr.size() - 1]`



<details>
<summary>
std::array
</summary>

```cpp
#include <array>
#include <iostream>

int main() {
    std::array<float, 3> data{10.0F, 100.0F, 1000.0F};
    for (const auto &elem : data) {
        std::cout << elem << std::endl;
    }
    // std::cout << std::boolalpha;
    std::cout << "Array empty: " << data.empty() << std::endl;
    std::cout << "Array size : " << data.size() << std::endl;
}
```

</details>


### std::vector

- `#include <vector>` to use std::vector
- Vector is implemented as a **dynamic table**
- Remove all elements: `vec.clear()`
- Add a new item in one of two ways:
    - `vec.emplace_back(value)` [preferred, c++11]
    - `vec.push_back(value)` [historically better known]
- **Use it! It is fast and flexible!**
    - Consider it to be a default container to store collections of items of any same type.

<details>
<summary>
std::vector
</summary>

```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    std ::vector<int> numbers = {1, 2, 3};

    std ::vector<std ::string> names = {"Nacho", "Cyrill"};
    names.emplace_back("Roberto");

    std::cout << "First name : " << names.front() << std::endl;
    std::cout << "Last number: " << numbers.back() << std::endl;
    return 0;
}
```

</details>

#### Optimize vector resizing

- `reserve(n)` ensures that the vector has enough capacity to store n items
- This is a very **important optimization**
    ```cpp
    vector <int> vec; // size 0, capacity 0
    vec.reserve(N); // size 0, capacity 100
    ```


### std::map

- `#include <map>`
- **sorted** associative container
- Contains **key-value** pairs
- keys are stored using the `<` operator
    - your **keys** should be comparable
- create from data
    ```cpp
    std::map<KeyT, ValueT> m{{key1, value1}, {...} };
    ```
- check size: `m.size()`
- Add item to map: `m.emplace(key, value);`
- modify or add item: `m[key] = value;`
- Get const ref to an item: m.at(key);
- check if key present: 
    - `m.count(key) > 0` 
    - `m.contains(key) [bool]` starting in c++20


<details>
<summary>
std::map
</summary>

```cpp
#include <iostream> // I/O stream for simple input/output
#include <map>

int main() {
    using StudentList = std::map<int, std::string>;
    StudentList students;

    students.emplace(1509, "Nacho");
    students[1508] = "Paco";

    for (const auto &[id, name] : students) {
        std::cout << id << " " << name << std::endl;
    }
}
```

</details>



### std::unordered_map

- `#include <unordered_map>`
- implemented as a **hash table**
- key type has to be hashable
- faster to use than **std::map**


### Iterating over maps

```cpp
    for (const auto &student : students) {
        std::cout << student.first << " " << student.second << std::endl;
    }
```

New in **C++17**

```cpp
    for (const auto &[id, name] : students) {
        std::cout << id << " " << name << std::endl;
    }
```

### Much More

#### Sequence containers

container | desc
--- | --- 
array (c++11) | static contiguous array
vector | dynamic contiguous array
deque | double-ended queue
forward_list (c++11)  | single-linked list
list | doubly-linked list


#### Associative containers

Associative containers implement sorted data structures that can be quickly searched (O(logn) complexity).

container | desc
--- | ---
set | sorted by keys
map | sorted by keys
multiset  | keys may be non-unique, sorted by keys
multimap | keys may be non-unique,  sorted by keys



#### Unordered Associative containers

container | desc
--- | ---
unordered_set | hashed by keys
unordered_map | hashed by keys
unordered_multiset  | keys may be non-unique, hashed by keys
unordered_multimap | keys may be non-unique,  hashed by keys


#### Container adaptors

Container adaptors provide a different interface for sequential containers

adaptors | desc
--- | ---
stack | adapts a container to provide LIFO data structure
queue | adapts a container to provide  FIFO data structure
priority_queue | adapts a container to provide priority queue


### Iterators

Iterators are the **glue** that ties standard-library algorithms to their data. 

Iterators are the mechanism used to **minimize an algorithm's dependence** on the data structures on which it operates.

```
sort()      -----\            /-----  vector
find()      -----\            /-----  map
merge()     ------ Iterators  ------  list
...         ------            ------  ...
my_algo()   -----/            \-----  my_container
your_fct()  -----/            \-----  your_container
```

STL uses iterators to access data in containers

- Iterators are similar to pointers
- Allow quick navigation through containers
- Most algorithms in STL use iterators
- Defined for all using STL containers


#### Access Data

- Access current element with `*iter`
- Acceptes `->` alike to pointers
- Move to next element in container `iter++`
- Prefer range-based for loops
- Compare iterators with `==, !=, <`


#### Range Access Iterators

the leading `c` means **const**

- `begin, cbegin`
    - returns an iterator to the beginning of a container for array
- `end, cend`
    - returns an iterator to the end of a container for array
- `rbegin, crbegin`
    - return a **reverse** iterator to a container to array
- `rend, crend`
    - return a reverse end iterator for a container or array

<details>
<summary>
iter example
</summary>

```cpp
#include <iostream> // I/O stream for simple input/output
#include <map>
#include <vector>

int main() {
    std::vector<double> x{1, 2, 3};
    for (auto it = x.begin(); it != x.end(); ++it) {
        std::cout << *it << std::endl;
    }

    std::map<int, std::string> m = {{1, "one"}, {2, "two"}};
    std::map<int, std::string>::iterator it = m.find(1);
    std::cout << it->first << ":" << it->second << std::endl;

    auto it2 = m.find(1); // same thing
    std::cout << it2->first << ":" << it2->second << std::endl;

    if (m.find(3) == m.end()) {
        std::cout << "3 not found" << std::endl;
    }

    return 0;
}
```

</details>


## STL Algorithms

- About 80 standard algorithms
- Defined in `#include <algorithm>`
- They operate on sequences defined by a pair of iterators(for inputs ) or a single iterator (for outputs).
- **Don't reinvent the wheel**
    - before writting you own `sort` function ...
    - https://en.cppreference.com/w/cpp/algorithm
- When using STL containers, `std::vector, std::array`, etc. Try to avoid writing your own algorithms
- If you are not using STL containers, then providing implementations for the stardard iterators will give you access to all algorithms for free.


### std::sort

```cpp
    std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    std::sort(s.begin(), s.end());
```

### std::find

```cpp
    std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    auto result1 = std::find(s.begin(), s.end(), 7);
    if (result1 != s.end()) {
        std::cout << "Found 7 at index " << std::distance(s.begin(), result1)
                  << std::endl;
    } else {
        std::cout << "7 not found" << std::endl;
    }
```


### std::fill

```cpp
    std::fill(v.begin (), v.end (), -1);
```

### std::count

how many time a value appears in the container

```cpp
    int num_items1 = std::count(v.begin (), v.end (), n1);
```

### std::count_if

```cpp
inline bool div_by_3(int i) { return i % 3 == 0; }
int main () {
    std::vector <int> v{1, 2, 3, 3, 4, 3, 7, 8, 9, 10};
    int n3 = std::count_if(v.begin (), v.end (), div_by_3);
    ...
}
```

### std::for_each

```cpp
    std::vector <int> nums {3, 4, 2, 8, 15, 267};
    // lambda expression
    auto print = [](const int& n) { cout << " " << n; };
    std::for_each(nums.cbegin (), nums.cend (), print);
```


### std::all_of

```cpp
inline bool even(int i) { return i % 2 == 0; };
int main () {
    std::vector <int> v(10, 2); // 2 2 2 2 2  2 2 2 2 2
    std::partial_sum (v.cbegin (), v.cend (), v.begin ());
    // 2 4 6 8 10 12 14 16 18 20

    bool all_even = all_of(v.cbegin (), v.cend (), even);
    // true
```

### std::rotate

```cpp
std::vector <int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
std::rotate(v.begin (), v.begin () + 2, v.end ());
// before rotate: 1 2 3 4 5 6 7 8 9 10
// after rotate: 3 4 5 6 7 8 9 10 1 2
```

### std::transform

```cpp
auto UpperCase (char c) { return std::toupper(c); }
int main () {
    const std::string s("hello");
    std::string S{s};
    std::transform (s.begin (), s.end (), S.begin (), UpperCase );
    // s: hello
    // S: HELLO
}
```

### std::accumulate

```cpp
    std::vector <int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = std::accumulate (v.begin (), v.end (), 0); // 55
    int product = std::accumulate (v.begin (), v.end (), 1, std::multiplies ()); // 3628800
```

### std::max

```cpp
    using std::max;
    cout << "max(1, 9999) : " << max(1, 9999) << endl;
    cout << "max('a', 'b'): " << max('a', 'b') << endl;
```

### std::min_element

```cpp
int main() {
    std::vector<int> v{3, 1, 4, 1, 0, 5, 9};
    auto result = std::min_element(v.begin(), v.end());
    std::cout << "The minimum element is " << *result << std::endl; // 0
    auto min_location = std::distance(v.begin(), result);
    std::cout << "min at: " << min_location << std::endl; // min at: 4
    return 0;
}
```

### std::minmax_element

```cpp
    using std::minmax_element ;
    auto v = {3, 9, 1, 4, 2, 5, 9};
    auto [min , max] = minmax_element (begin(v), end(v));
    cout << "min = " << *min << endl;
    cout << "max = " << *max << endl;
    // min = 1
    // max = 9
```


### std::clamp

```cpp
    // value should be between [kMin ,kMax]
    const double kMax = 1.0F;
    const double kMin = 0.0F

    cout << std :: clamp (0.5 , kMin , kMax) << endl; // 0.5
    cout << std :: clamp (1.1 , kMin , kMax) << endl; // 1
    cout << std :: clamp (0.1 , kMin , kMax) << endl; // 0.1
    cout << std :: clamp (-2.1, kMin , kMax) << endl; // 0
```

