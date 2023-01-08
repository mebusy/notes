[](...menustart)

- [Modern C++](#091a6498eab3c508beea02f499f51f72)
    - [Modern C++: Build and Tools (Lecture 1, I. Vizzo, 2020)](#325510d6bba829b766911a52d3936c5c)
        - [Compilation flags](#62cd52fdf3d2a8bff72649fcd20e4eb7)
        - [Header file](#24c503e9d5c57f1eb6af12e9873a8842)
        - [Libraries](#aeb428554a0acc6cc503a2e4da6ae61a)
        - [Build Systems](#9062aef37682ecaeb79a2df3f3820105)
        - [Build a CMake project](#0458b03d5c8e257e5832ae13f35c64d4)
    - [Modern C++: Core C++ (Lecture 2, I. Vizzo, 2020)](#3e2af85ef3711cbd431c3a2a0e06d42a)
        - [Range for loop](#4bb1ad49e08a18886c3d80a8642067f0)
        - [c++17, Iterating map in a pythonic way](#e102f67b68837b497f8f248b27fe42f2)
        - [References to variables](#5ec0d21ae7ae7c4254aa1660eb6e4c65)
        - [stringstream](#65803f90b5371dc3b88b60a06713354b)
    - [Modern C++: C++ Functions (Lecture 3, I. Vizzo, 2020)](#a229d387ccd502315aeb3181517851e9)
        - [string](#b45cffe084dd3d20d928bee85e7b0f21)
        - [Return type](#0007c63d15df657b740c1ee3154c262e)
            - [Automatic return type deduction C++14](#d3cb767ab10f736c78010d8580888b03)
            - [return multiple value like python](#1e4c066fde8dc7dce4d43f7b12f8ecfb)
            - [WARNING: Never return reference to locally variables !!!](#535395200405220009c672236d3cd0f0)
        - [Argument List](#4b3473986e35c311d04c1f51e2364e5c)
        - [Default Arguments](#1cc836adaa1ff6687e4b7268d53fd690)
        - [Passing big objects](#97b1664f687df9ed0e3dfb1930a5e08b)
        - [Namespaces](#13d28e8dfc702e3456e0767dff9a128a)
        - [Nameless namespace](#2f456caae6a443a8904f3985a3b76b52)
    - [Modern C++: The C++ STL Library (Lecture 4, I. Vizzo, 2020)](#6559a7c277d5ab1e9354d0f6a688aaff)
        - [std::array](#326a83eb53ef155a2689ddafaebdc904)
        - [std::vector](#f0f1af1e35355df34019a2c3783b10b3)
            - [Optimize vector resizing](#3f074b0debc6864e448427c629c9244e)
        - [std::map](#1b3695f21224f3bbc288e793cf882f63)
        - [std::unordered_map](#dc7ff92730fbf5c6f11c3cf17606dbae)
        - [Iterating over maps](#aa703c156fde48ca1bd441cec6280929)
        - [Much More](#749a4adc947e16689fe9c879ee3c493a)
            - [Sequence containers](#d427f3a724f7121a73daa3141b530c54)
            - [Associative containers](#31d750310fd00290fe605fba289138f1)
            - [Unordered Associative containers](#b6666e72d36bedf79abe8f6f7df90a45)
            - [Container adaptors](#0b7e76082bd309e16701c104e9dac707)
        - [Iterators](#523a8681903bcf53bace35316c86fe33)
            - [Access Data](#e35ac241f07c82101c044391318203b2)
            - [Range Access Iterators](#e4ce2be0ecd34562628da38caf2ef7fc)
    - [STL Algorithms](#1bc9ae9db55fe7155f74151a7aa7c02c)
        - [std::sort](#6ae257cb23885f8b48f39b1b9d4231aa)
        - [std::find](#c4b7e2a44e8a44588292a31f9011f63f)
        - [std::fill](#2f4de93bdd1dd3d7dbf6e9921d8c5532)
        - [std::count](#38f03ac751e3f817af19626d93d8717c)
        - [std::count_if](#9b198cfb6790551429485d6acd2cf2e5)
        - [std::for_each](#0961a9c4c06073f32a96a680e3888619)
        - [std::all_of](#9c53a489806cc3a34873b4379eef31c8)
        - [std::rotate](#67f8cacb091969dc1c51ac79678a8e18)
        - [std::transform](#2a61c221f8277712d39ce802d9b6f952)
        - [std::accumulate](#26a950b3fc74670b811b42da3ab8a292)
        - [std::max](#18ae435191aaee20621eb10024fbbb34)
        - [std::min_element](#dd8ec9efd2fe56b7abf66f2a11daa933)
        - [std::minmax_element](#5f12a37961c2f3791b1cd8ed74dc0e8f)
        - [std::clamp](#a73735cb6e23b9a7b8336d2704580ebc)
        - [std::sample](#7d7e5802dcba0b7b9e4f9095d2ede15e)
    - [Modern C++: I/O Files, Intro to Classes (Lecture 5, I. Vizzo, 2020)](#ca60008ff3f9f37c01aa32cc26f27d57)
        - [C++ Utilities](#64329a7f7fdda209400a0e09e030b72a)
            - [std::swap](#4f1b4f40c11bae1ef7016617425c47ce)
            - [std::variant](#edfc81f5909201a3635b0510580efd59)
            - [std::any](#68cdf81a296c17812f5703c4853431bf)
            - [std::optional](#86a6516c2565ea4d02f523528704628c)
            - [std::tuple](#a0085eb6fbe44026d573660ddc6dfdb1)
            - [std::chrono](#c19047f100b3ef25731b892ae53676e7)
        - [Error Handling](#ef43236673ca0bb606b14091061ac271)
            - [Error handling with exceptions](#7510820b7a388de6f1d29fb1016855c6)
            - [throw exceptions](#ce13141dd4e4dce25cbb4332e6da68bd)
            - [catch exceptions](#db263daf8d9aaa24b3310e63e8a2039d)
        - [IO Library](#edde613ff4105afe6b46342e6349d4dc)
            - [Reading and writing to files](#1d76348345dba9e6f8aa5be00cd1ce47)
            - [Regular columns](#6d339878496ab35daf9a4791d88d3cfa)
            - [Reading files one line at a time](#9b554d6150f4065e7e97e9623ad9b663)
            - [Writing into text files](#62f2f943d940531f78915e94151c9f20)
            - [Writing to binary files](#71eb2af1d3698b17486be09467c11cf1)
            - [Reading from binary files](#0f30f0d2efdfcf48af794b13f6b23dd9)
        - [C++17 Filesystem library](#606b6a8c6de3d15095ae41e960390cea)
            - [directory_iterator](#60a3cb9955bbb37b1e6985ef26315afd)

[](...menuend)


<h2 id="091a6498eab3c508beea02f499f51f72"></h2>

# Modern C++

- This lecture
    - https://www.youtube.com/watch?v=9mZw6Rwz1vg&list=PLgnQpQtFTOGRM59sr3nSL8BmeMZR9GCIA&index=5
- Resources
    - STL algorithm
        - https://en.cppreference.com/w/cpp/algorithm
    - C++ Utilities
        - https://en.cppreference.com/w/cpp/utility
    - Google C++ Testing
        - https://www.youtube.com/watch?v=nbFXI9SDfbk
    - CPP-06 Modern C++: Static, Numbers, Arrays, Non-owning pointers, Classes (2018, Igor)
        - https://www.youtube.com/watch?v=mIrOcFf2crk&t=1729s


<h2 id="325510d6bba829b766911a52d3936c5c"></h2>

## Modern C++: Build and Tools (Lecture 1, I. Vizzo, 2020)

<h2 id="62cd52fdf3d2a8bff72649fcd20e4eb7"></h2>

###  Compilation flags

- `-std=c++17`, `-o`, etc
- Enable all warnings, treat them as errors
    - `-Wall, -Wextra, -Werror`
- Optimization options
    - `-O0`  -- no optimizations [default]
    - `-O3` or `-Ofast`  -- full optimizations
- Keep debugging symbols
    - `-g`



<h2 id="24c503e9d5c57f1eb6af12e9873a8842"></h2>

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


<h2 id="aeb428554a0acc6cc503a2e4da6ae61a"></h2>

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


<h2 id="9062aef37682ecaeb79a2df3f3820105"></h2>

### Build Systems

- They began as `shell` scripts
- They turn into `MakeFiles`
- And now into MetaBuild Systems like `CMake`
    - Accept it, CMake is not a build system
    - It's a build system generator
    - You need to use an actual build system like `Make` of `Ninja`


<h2 id="0458b03d5c8e257e5832ae13f35c64d4"></h2>

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


<h2 id="3e2af85ef3711cbd431c3a2a0e06d42a"></h2>

## Modern C++: Core C++ (Lecture 2, I. Vizzo, 2020)

<h2 id="4bb1ad49e08a18886c3d80a8642067f0"></h2>

### Range for loop

- Iterating over a standard containers like array or vector has simple syntax
- Avoid mistakes with indices
- added in c++11
    ```c++
    for (const auto& value: container) {
        // this happens for each value in the container
    }
    ```

<h2 id="e102f67b68837b497f8f248b27fe42f2"></h2>

### c++17, Iterating map in a pythonic way

- New in c++17
    ```c++
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


<h2 id="5ec0d21ae7ae7c4254aa1660eb6e4c65"></h2>

### References to variables

- We can create a **reference** to any variable
    ```c++
    float& ref = original_variable;
    std::string& hello_ref = hello;
    ```
- Reference is part of type:  variable `ref` has type `float&`
- Whatever happens to a reference happens to the variable and vice versa
- Yields performance gain as references avoid **copying data**.


<h2 id="65803f90b5371dc3b88b60a06713354b"></h2>

### stringstream

```c++
    std::stringstream filename("205.txt");

    int num = 0;
    std::string ext;

    // split the string stream using simple syntax
    filename >> num >> ext;

    std::cout << "num: " << num << std::endl; // 205
    std::cout << "ext: " << ext << std::endl; // .ext
```


<h2 id="a229d387ccd502315aeb3181517851e9"></h2>

## Modern C++: C++ Functions (Lecture 3, I. Vizzo, 2020)

<h2 id="b45cffe084dd3d20d928bee85e7b0f21"></h2>

### string

- `#include <string>`
    ```c++
    const std::string source("copy this!");
    std::string dest = source;
    ```

<h2 id="0007c63d15df657b740c1ee3154c262e"></h2>

### Return type 

<h2 id="d3cb767ab10f736c78010d8580888b03"></h2>

#### Automatic return type deduction C++14

```c++
auto GetDictionary() {
    return std::map<char, int> my_dict{{'a', 1}, {'b', 2}};
}
```

<h2 id="1e4c066fde8dc7dce4d43f7b12f8ecfb"></h2>

#### return multiple value like python

- with the introduction of structured binding in c++17 you can now:
    ```c++
    #include <tuple>

    auto Foo() {
        return make_tuple("Super Variable", 5);
    }

    int main() {
        auto [name, value] = Foo();
        ...
    }
    ```

<h2 id="535395200405220009c672236d3cd0f0"></h2>

#### WARNING: Never return reference to locally variables !!!


<h2 id="4b3473986e35c311d04c1f51e2364e5c"></h2>

### Argument List 

```c++
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


<h2 id="1cc836adaa1ff6687e4b7268d53fd690"></h2>

### Default Arguments

- Only **set in declaration**, not in definition
- Cons:
    - Evaluated upon every call
    - Values are hidden in declaration
    - Can lead to unexpected behavior when overused
- Only use them when readability gets much better.

<h2 id="97b1664f687df9ed0e3dfb1930a5e08b"></h2>

### Passing big objects

- **Pass by reference** to avoid copy
- **Avoid using non-const ref**
    - use const refs to ensure the object passed in won't be modified unexpectedly
    - non-const refs are mostly used in older code written before c++11


<h2 id="13d28e8dfc702e3456e0767dff9a128a"></h2>

### Namespaces

- helps avoiding name conflicts
- group the project into logical moduels
    ```c++
    namespace module_1 {
        int SomeFunc() {}
    }
    ```
    ```c++
    namespace module_2 { int SomeFunc() {} }
    ```

- **Avoid** using namespace `<name>`
    ```c++
    // Avoid !!!
    using namespace std;
    ```
- Only use what you need
    ```c++
    using std::cout;  // explicitly use cout.
    using std::endl;
    ```
- **Never** use `using namespace <name>` in *.hpp files
    - Prefer using explicit `using` even in *.cpp files

<h2 id="2f456caae6a443a8904f3985a3b76b52"></h2>

### Nameless namespace

- If you find yourself relying on some constants in a file and these constants should not be seen in any other file, put them into a **nameless namespace** on the top of this file
    ```c++
    namespace {
        const int kLocalImportantInt = 13;
        const int kLocakImportantFloat = 13.0f;
    } // nameless
    ...
    ```

<h2 id="6559a7c277d5ab1e9354d0f6a688aaff"></h2>

## Modern C++: The C++ STL Library (Lecture 4, I. Vizzo, 2020)

<h2 id="326a83eb53ef155a2689ddafaebdc904"></h2>

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

```c++
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


<h2 id="f0f1af1e35355df34019a2c3783b10b3"></h2>

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

```c++
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3};

    std::vector<std::string> names = {"Nacho", "Cyrill"};
    names.emplace_back("Roberto");

    std::cout << "First name : " << names.front() << std::endl;
    std::cout << "Last number: " << numbers.back() << std::endl;
    return 0;
}
```

</details>

<h2 id="3f074b0debc6864e448427c629c9244e"></h2>

#### Optimize vector resizing

- `reserve(n)` ensures that the vector has enough capacity to store n items
- This is a very **important optimization**
    ```c++
    vector <int> vec; // size 0, capacity 0
    vec.reserve(N); // size 0, capacity 100
    ```


<h2 id="1b3695f21224f3bbc288e793cf882f63"></h2>

### std::map

- `#include <map>`
- **sorted** associative container
- Contains **key-value** pairs
- keys are stored using the `<` operator
    - your **keys** should be comparable
- create from data
    ```c++
    std::map<KeyT, ValueT> m{{key1, value1}, {...} };
    ```
- check size: `m.size()`
- Add item to map: `m.emplace(key, value);`
- modify or add item: `m[key] = value;`
- Get const ref to an item: m.at(key);
- check if key present: 
    - `m.count(key)> 0` 
    - `m.contains(key) [bool]` starting in c++20


<details>
<summary>
std::map
</summary>

```c++
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



<h2 id="dc7ff92730fbf5c6f11c3cf17606dbae"></h2>

### std::unordered_map

- `#include <unordered_map>`
- implemented as a **hash table**
- key type has to be hashable
- faster to use than **std::map**


<h2 id="aa703c156fde48ca1bd441cec6280929"></h2>

### Iterating over maps

```c++
    for (const auto &student : students) {
        std::cout << student.first << " " << student.second << std::endl;
    }
```

New in **C++17**

```c++
    for (const auto &[id, name] : students) {
        std::cout << id << " " << name << std::endl;
    }
```

<h2 id="749a4adc947e16689fe9c879ee3c493a"></h2>

### Much More

<h2 id="d427f3a724f7121a73daa3141b530c54"></h2>

#### Sequence containers

container | desc
--- | --- 
array (c++11) | static contiguous array
vector | dynamic contiguous array
deque | double-ended queue
forward_list (c++11)  | single-linked list
list | doubly-linked list


<h2 id="31d750310fd00290fe605fba289138f1"></h2>

#### Associative containers

Associative containers implement sorted data structures that can be quickly searched (O(logn) complexity).

container | desc
--- | ---
set | sorted by keys
map | sorted by keys
multiset  | keys may be non-unique, sorted by keys
multimap | keys may be non-unique,  sorted by keys



<h2 id="b6666e72d36bedf79abe8f6f7df90a45"></h2>

#### Unordered Associative containers

container | desc
--- | ---
unordered_set | hashed by keys
unordered_map | hashed by keys
unordered_multiset  | keys may be non-unique, hashed by keys
unordered_multimap | keys may be non-unique,  hashed by keys


<h2 id="0b7e76082bd309e16701c104e9dac707"></h2>

#### Container adaptors

Container adaptors provide a different interface for sequential containers

adaptors | desc
--- | ---
stack | adapts a container to provide LIFO data structure
queue | adapts a container to provide  FIFO data structure
priority_queue | adapts a container to provide priority queue


<h2 id="523a8681903bcf53bace35316c86fe33"></h2>

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


<h2 id="e35ac241f07c82101c044391318203b2"></h2>

#### Access Data

- Access current element with `*iter`
- Acceptes `->` alike to pointers
- Move to next element in container `iter++`
- Prefer range-based for loops
- Compare iterators with `==, !=, <`


<h2 id="e4ce2be0ecd34562628da38caf2ef7fc"></h2>

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

```c++
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


<h2 id="1bc9ae9db55fe7155f74151a7aa7c02c"></h2>

## STL Algorithms

- About 80 standard algorithms
- Defined in `#include <algorithm>`
- They operate on sequences defined by a pair of iterators(for inputs ) or a single iterator (for outputs).
- **Don't reinvent the wheel**
    - before writting you own `sort` function ...
    - https://en.cppreference.com/w/cpp/algorithm
- When using STL containers, `std::vector, std::array`, etc. Try to avoid writing your own algorithms
- If you are not using STL containers, then providing implementations for the stardard iterators will give you access to all algorithms for free.


<h2 id="6ae257cb23885f8b48f39b1b9d4231aa"></h2>

### std::sort

```c++
    std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    std::sort(s.begin(), s.end());
```

<h2 id="c4b7e2a44e8a44588292a31f9011f63f"></h2>

### std::find

```c++
    std::array<int, 10> s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    auto result1 = std::find(s.begin(), s.end(), 7);
    if (result1 != s.end()) {
        std::cout << "Found 7 at index " << std::distance(s.begin(), result1)
                  << std::endl;
    } else {
        std::cout << "7 not found" << std::endl;
    }
```


<h2 id="2f4de93bdd1dd3d7dbf6e9921d8c5532"></h2>

### std::fill

```c++
    std::fill(v.begin (), v.end (), -1);
```

<h2 id="38f03ac751e3f817af19626d93d8717c"></h2>

### std::count

how many time a value appears in the container

```c++
    int num_items1 = std::count(v.begin (), v.end (), n1);
```

<h2 id="9b198cfb6790551429485d6acd2cf2e5"></h2>

### std::count_if

```c++
inline bool div_by_3(int i) { return i % 3 == 0; }
int main () {
    std::vector <int> v{1, 2, 3, 3, 4, 3, 7, 8, 9, 10};
    int n3 = std::count_if(v.begin (), v.end (), div_by_3);
    ...
}
```

<h2 id="0961a9c4c06073f32a96a680e3888619"></h2>

### std::for_each

```c++
    std::vector <int> nums {3, 4, 2, 8, 15, 267};
    // lambda expression
    auto print = [](const int& n) { cout << " " << n; };
    std::for_each(nums.cbegin (), nums.cend (), print);
```


<h2 id="9c53a489806cc3a34873b4379eef31c8"></h2>

### std::all_of

```c++
inline bool even(int i) { return i % 2 == 0; };
int main () {
    std::vector <int> v(10, 2); // 2 2 2 2 2  2 2 2 2 2
    std::partial_sum (v.cbegin (), v.cend (), v.begin ());
    // 2 4 6 8 10 12 14 16 18 20

    bool all_even = all_of(v.cbegin (), v.cend (), even);
    // true
```

<h2 id="67f8cacb091969dc1c51ac79678a8e18"></h2>

### std::rotate

```c++
std::vector <int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
std::rotate(v.begin (), v.begin () + 2, v.end ());
// before rotate: 1 2 3 4 5 6 7 8 9 10
// after rotate: 3 4 5 6 7 8 9 10 1 2
```

<h2 id="2a61c221f8277712d39ce802d9b6f952"></h2>

### std::transform

```c++
auto UpperCase (char c) { return std::toupper(c); }
int main () {
    const std::string s("hello");
    std::string S{s};
    std::transform (s.begin (), s.end (), S.begin (), UpperCase );
    // s: hello
    // S: HELLO
}
```

<h2 id="26a950b3fc74670b811b42da3ab8a292"></h2>

### std::accumulate

```c++
    std::vector <int> v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = std::accumulate (v.begin (), v.end (), 0); // 55
    int product = std::accumulate (v.begin (), v.end (), 1, std::multiplies ()); // 3628800
```

<h2 id="18ae435191aaee20621eb10024fbbb34"></h2>

### std::max

```c++
    using std::max;
    cout << "max(1, 9999) : " << max(1, 9999) << endl;
    cout << "max('a', 'b'): " << max('a', 'b') << endl;
```

<h2 id="dd8ec9efd2fe56b7abf66f2a11daa933"></h2>

### std::min_element

```c++
int main() {
    std::vector<int> v{3, 1, 4, 1, 0, 5, 9};
    auto result = std::min_element(v.begin(), v.end());
    std::cout << "The minimum element is " << *result << std::endl; // 0
    auto min_location = std::distance(v.begin(), result);
    std::cout << "min at: " << min_location << std::endl; // min at: 4
    return 0;
}
```

<h2 id="5f12a37961c2f3791b1cd8ed74dc0e8f"></h2>

### std::minmax_element

```c++
    using std::minmax_element ;
    auto v = {3, 9, 1, 4, 2, 5, 9};
    auto [min , max] = minmax_element (begin(v), end(v));
    cout << "min = " << *min << endl;
    cout << "max = " << *max << endl;
    // min = 1
    // max = 9
```


<h2 id="a73735cb6e23b9a7b8336d2704580ebc"></h2>

### std::clamp

```c++
    // value should be between [kMin ,kMax]
    const double kMax = 1.0F;
    const double kMin = 0.0F

    cout << std::clamp (0.5 , kMin , kMax) << endl; // 0.5
    cout << std::clamp (1.1 , kMin , kMax) << endl; // 1
    cout << std::clamp (0.1 , kMin , kMax) << endl; // 0.1
    cout << std::clamp (-2.1, kMin , kMax) << endl; // 0
```

<h2 id="7d7e5802dcba0b7b9e4f9095d2ede15e"></h2>

### std::sample

```c++
#include <algorithm>
#include <iostream> // I/O stream for simple input/output
#include <random>
#include <vector>

int main() {
    std::string in = "C++ is cool", out;
    auto rnd_dev = std::mt19937{std::random_device{}()};
    const int kNLetters = 5;
    std::sample(in.begin(), in.end(), std::back_inserter(out), kNLetters,
                 rnd_dev);
    std::cout << "from : " << in << std::endl;   // C++ is cool
    std::cout << "sample: " << out << std::endl; // sample: +  ol   // random
    return 0;
}
```

<h2 id="ca60008ff3f9f37c01aa32cc26f27d57"></h2>

## Modern C++: I/O Files (Lecture 5, I. Vizzo, 2020)

<h2 id="64329a7f7fdda209400a0e09e030b72a"></h2>

### C++ Utilities

- two groups libraries
    1. language support libraries
        - type support (`std::size_t`)
        - dynamic memory management (`std::shared_ptr`)
        - error handling (`std::exception, assert`)
        - initializer list(`std::vector{1,2}`)
        - much more...
    2. general-purpose libraries
        - program utilities (`std::abort`)
        - date and time (`std::chrono::duration`)
        - optional, variant and any (`std::variant`)
        - pairs and tuples (`std::tuple`)
        - swap, forward and move (`std::move`)
        - hash support (`std::hash`)
        - formatting library (coming in c++20)
        - much more...


<h2 id="4f1b4f40c11bae1ef7016617425c47ce"></h2>

#### std::swap

```c++
    int a = 3;
    int b = 5;

    std::swap(a, b); // a:5, b:3
```

<h2 id="edfc81f5909201a3635b0510580efd59"></h2>

#### std::variant

- safty union
- [如何优雅的使用 std::variant 与 std::optional](https://zhuanlan.zhihu.com/p/366537214)

```c++
    // can be either int or float, but not both
    std::variant <int, float> v1;
    v1 = 12; // v contains int
    cout << std::get <int>(v1) << endl; // 12
    // will raise error if you want to get float
    v1 = 1.0; // override value

    // get the index of stored type
    std::cout << "v1 - " << v1.index() << std::endl;

    std::variant <int, float> v2 {3.14F};
    cout << std::get <1>(v2) << endl;  // 3.14

    v2 = std::get <int>(v1); // assigns v1 to v2
    v2 = std::get <0>(v1);  // same assignment
    v2 = v1;  // same assignment
    cout << std::get <int>(v2) << endl; // 12
```

- when to use ?
    1. a function may return different types of return values.
        - For example: the formula for finding the root of a quadratic equation in one variable, 
        - the root may be one, or two, or none
        ```c++
        using Two = std::pair<double, double>;
        using Roots = std::variant<Two, double, void*>;

        Roots FindRoots(double a, double b, double c) {
            auto d = b*b-4*a*c;

            if (d> 0.0)
            {
                auto p = sqrt(d);
                return std::make_pair((-b + p) / 2 * a, (-b - p) / 2 * a);
            }
            else if (d == 0.0)
                return (-1*b)/(2*a);
            return nullptr;
        }

        struct RootPrinterVisitor
        {
            void operator()(const Two& roots) const
            {
                std::cout << "2 roots: " << roots.first << " " << roots.second << '\n';
            }
            void operator()(double root) const
            {
                std::cout << "1 root: " << root << '\n';
            }
            void operator()(void *) const
            {
                std::cout << "No real roots found.\n";
            }
        };

        TEST_F(TestFindRoot) {
            std::visit(RootPrinterVisitor(), FindRoots(1, -2, 1)); //(x-1)*(x-1)=0
            std::visit(RootPrinterVisitor(), FindRoots(1, -3, 2)); //(x-2)*(x-1)=0
            std::visit(RootPrinterVisitor(), FindRoots(1, 0, 2));  //x*x - 2 = 0
        }
        ```
    2. polymorphism
        ```c++
        using Draw = std::variant<Triangle, Circle>;
        Draw draw;
        std::vector<Draw> draw_list {Triangle{}, Circle{}, Triangle{}};
        auto DrawVisitor = [](const auto &t) { t.Draw(); };
        for (const auto &item : draw_list) {
            std::visit(DrawVisitor, item);
        }
        ```
- The time complexity of std::visit to obtain the type actually stored in std::variant is O(1), and the performance will not decrease with the increase of types in std::variant.


<h2 id="68cdf81a296c17812f5703c4853431bf"></h2>

#### std::any

- https://devblogs.microsoft.com/cppblog/stdany-how-when-and-why/
- `#include <any>`

```c++
    std::any a; // any type
    a = 1; // int
    std::cout << std::any_cast<int>(a) << std::endl;

    a = 3.14; // double
    std::cout << std::any_cast <double>(a) << std::endl;  // 3.14

    a = true; // bool
    std::cout << std::boolalpha << std::any_cast <bool>(a) << std::endl; // true
```


<h2 id="86a6516c2565ea4d02f523528704628c"></h2>

#### std::optional

- this is usually something we can solve using like `if/else`

```c++
#include <iostream> // I/O stream for simple input/output
#include <optional>

std::optional<std::string> StringFactory(bool create) {
    if (create) {
        return "C++17";
    }
    return {}; // return nothing
}

int main() {
    std::cout << StringFactory(true).value() << '\n';         // C++17
    std::cout << StringFactory(false).value_or(":(") << '\n'; // :(
    return 0;
}
```


<h2 id="a0085eb6fbe44026d573660ddc6dfdb1"></h2>

#### std::tuple

```c++
    std::tuple <double , char , string> student1;

    using Student = std::tuple <double , char , string>;
    Student student2 {1.4 , 'A', "Jose"};

    cout << std::get <string>( student2) << endl; // Jose
    cout << std::get <2>( student2) << endl; // Jose

    // C++17 structured binding:
    auto [gpa , grade , name] = make_tuple (4.4 , 'B', "");
```


<h2 id="c19047f100b3ef25731b892ae53676e7"></h2>

#### std::chrono

- there are much better ways of doing benchmarking but let's say that you want to benchmark a function...

```c++
    auto start = std::chrono::steady_clock::now ();
    cout << "f(42) = " << fibonacci (42) << '\n'; // f(42) = 267914296
    auto end = std::chrono::steady_clock::now ();

    std::chrono::duration <double> sec = end - start;
    cout << "elapsed time: " << sec.count () << "s\n"; // elapsed time: 1.84088s
```


<h2 id="ef43236673ca0bb606b14091061ac271"></h2>

### Error Handling

- Only used for **exceptional behavior**
- **Often misused** : e.g. wrong parameter should not lead to an exception
- **GOOGLE-STYLE** Don’t use exceptions

<h2 id="7510820b7a388de6f1d29fb1016855c6"></h2>

#### Error handling with exceptions

- We can **throw** an exception if there is an error
- STL defines classes that represent exceptions. Base `class:std::exception`
- `#include <stdexcept>`
- An exception can be **caught** at any point of the program (`try - catch`) and even **thrown** further (throw)
- The constructor of an exception receives a string error message as a parameter
    - This string can be called through a member function `what()`

<h2 id="ce13141dd4e4dce25cbb4332e6da68bd"></h2>

#### throw exceptions

- Runtime Error:
    ```c++
    string msg = "specific error string";
    throw runtime_error (msg);
    ```
- Logic Error: an error in logic of the user
    ```c++
    throw logic_error (msg);
    ```
    - they are due to errors in the internal logic of the program. In theory, they are preventable.


<h2 id="db263daf8d9aaa24b3310e63e8a2039d"></h2>

#### catch exceptions

```c++
    try {
        x = someUnsafeFunction (a, b, c);
    }
    // we can catch multiple types of exceptions
    catch ( runtime_error &ex ) {
        cerr << "Runtime error: " << ex.what () << endl;
    } catch ( logic_error &ex ) {
        cerr << "Logic error: " << ex.what () << endl;
    } catch ( exception &ex ) {
        cerr << "Some exception: " << ex.what () << endl;
    } catch ( ... ) { // all others
        cerr << "Error: unknown exception" << endl;
    }
```

<h2 id="edde613ff4105afe6b46342e6349d4dc"></h2>

### IO Library

<h2 id="1d76348345dba9e6f8aa5be00cd1ce47"></h2>

#### Reading and writing to files

- Use streams from STL
- Syntax similar to `std::cerr`, `ctd::cout`

```c++
#include <fstream>

using Mode = std :: ios_base :: openmode;

// ifstream: stream for input file
std :: ifstream f_in(string& file_name , Mode mode);
// ofstream: stream for output file
std :: ofstream f_out(string& file_name , Mode mode);
// stream for input and output file
std :: fstream f_in_out(string& file_name , Mode mode);
```

- **modes** under which a file can be opened
    Mode | Meaning
    --- | ---
    ios_base::app | append output
    ios_base::ate | seek to EOF when opened
    ios_base::binary | open file in binary mode
    ios_base::in | open file for reading
    ios_base::out | open file for writing
    ios_base::trunc | overwrite the existing file


<h2 id="6d339878496ab35daf9a4791d88d3cfa"></h2>

#### Regular columns

- Use it when:
    - The file contains organized data
    - Every line has to have all columns
    ```txt
    1 2.34 One 0.21
    2 2.004 two 0.23
    3 -2.34 string 0.22
    ```

```c++
#include <fstream>
#include <iostream>
#include <string>

int main() {
    int i;
    double a, b;
    std::string s;

    std::ifstream in("test.txt"); // default mode: std::ios_base::in
    // Read data, until it is there.
    // even if there are empty lines and leading spaces
    while (in >> i >> a >> s >> b) {
        std::cout << i << " " << a << " " << s << " " << b << std::endl;
    }
    return 0;
}
// 1 2.34 One 0.21
// 2 2.004 two 0.23
// 3 -2.34 string 0.22
```


<h2 id="9b554d6150f4065e7e97e9623ad9b663"></h2>

#### Reading files one line at a time

```c++
#include <fstream>
#include <iostream>

int main() {
    std::string line, file_name;
    std::ifstream input("test_bel.txt");
    // Read data line-wise
    while (std::getline(input, line)) {
        // std::cout << line << std::endl;
        // Strting has a find method
        std::string::size_type loc = line.find("filename");
        if (loc != std::string::npos) {
            // Get the file name
            file_name = line.substr(line.find("=", 0) + 1, std::string::npos);
            std::cout << "File name: " << file_name << std::endl;
            // File name:  /home/ivizzo /. bashrc
        }
    }
    return 0;
}
// line in file: `filename = /home/ivizzo /. bashrc`
```

<h2 id="62f2f943d940531f78915e94151c9f20"></h2>

#### Writing into text files

```c++
#include <fstream>
#include <iomanip> // for setprecision

int main() {
    std::string filename = "out.txt";
    std::ofstream out(filename);
    if (!out.is_open()) {
        return EXIT_FAILURE;
    }
    double a = 1.23456789;
    out << "Just string" << std::endl;
    out << std::setprecision(10) << a << std::endl;
    return 0;
}
// out.txt
// Just string
// 1.2345678899999998901
```

<h2 id="71eb2af1d3698b17486be09467c11cf1"></h2>

#### Writing to binary files

- fast
- No precision loss for floating point types
- syntax:
    ```c++
    file.write(reinterpret_cast <char*>(&a), sizeof(a));
    ```

```c++
00000000: 0200 0000 0300 0000 0000 0000 0000 0000
00000010: 0000 0000 0000 0000 0000 0000 0000 0000
00000020: 0a
```


<h2 id="0f30f0d2efdfcf48af794b13f6b23dd9"></h2>

#### Reading from binary files

- syntax
    ```c++
    file.read(reinterpret_cast <char*>(&a), sizeof(a));
    ```

```c++
#include <fstream>
#include <iostream>
#include <vector>

int main() {
    std::string filename = "image.dat";
    int r = 0, c = 0;
    std::ifstream in(filename, std::ios::binary);
    if (!in) {
        return EXIT_FAILURE;
    }
    in.read(reinterpret_cast<char *>(&r), sizeof(r));
    in.read(reinterpret_cast<char *>(&c), sizeof(c));
    std::cout << "r = " << r << ", c = " << c << std::endl;
    std::vector<float> data(r * c, 0);
    in.read(reinterpret_cast<char *>(data.data()), data.size() * sizeof(float));
    for (float d : data) {
        std::cout << d << " ";
    }
    std::cout << std::endl;
    return 0;
}
// r = 2, c = 3
// 0 0 0 0 0 0
```

<h2 id="606b6a8c6de3d15095ae41e960390cea"></h2>

### C++17 Filesystem library

- Use to perform operations on:
    - paths
    - regular files
    - directories
- like a utility library on top of the IO library
- Inspired in `boost::filesystem`
    - Makes your life easier.
    - https://en.cppreference.com/w/cpp/filesystem


<h2 id="60a3cb9955bbb37b1e6985ef26315afd"></h2>

#### directory_iterator


```c++
#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    // PS. it's create_directories, NOT create_directory
    fs::create_directories("sandbox/a/b"); // mkdir -p
    std::ofstream("sandbox/file1.txt");
    std::ofstream("sandbox/file2.txt");
    // walk
    for (auto &p : fs::recursive_directory_iterator("sandbox")) {
        std::cout << p.path() << std::endl;
    }
    fs::remove_all("sandbox"); // rm -rf sandbox
    return 0;
}
// "sandbox/file2.txt"
// "sandbox/file1.txt"
// "sandbox/a"
// "sandbox/a/b"
```


#### filename


```c++
#include <filesystem>
#include <iostream>

namespace fs = std ::filesystem;

int main() {
    std::cout << fs::path("/foo/bar.txt").filename() << '\n' // "bar.txt"
              << fs::path("/foo/.bar").filename() << '\n'    // ".bar"
              << fs::path("/foo/bar/").filename() << '\n'    // ""
              << fs::path("/foo/.").filename() << '\n'       // "."
              << fs::path("/foo/..").filename() << '\n'      // ".."
              << fs::path("//host").filename() << '\n';      // "host"

    return 0;
}
```

#### extension

```c++
#include <filesystem>
#include <iostream>

namespace fs = std ::filesystem;

int main() {
    std::cout << fs::path("/foo/bar.txt").extension() << '\n' // ".txt"
              << fs::path("/foo/bar.").extension() << '\n'    // "."
              << fs::path("/foo/bar").extension() << '\n'     // ""
              << fs::path("/foo/bar.png").extension() << '\n' // ".png"
              << fs::path("/foo/.").extension() << '\n'       // ""
              << fs::path("/foo/..").extension() << '\n'      // ""
              << fs::path("/foo/.hidden").extension() << '\n' // ""
              << fs::path("/foo/..bar").extension() << '\n';  // ".bar"
    return 0;
}
```


#### stem

```c++
#include <filesystem>
#include <iostream>

namespace fs = std ::filesystem;

int main() {
    std::cout << fs::path("/foo/bar.txt").stem() << std::endl   // "bar"
              << fs::path("/foo/00000.png").stem() << std::endl // "00000"
              << fs::path("/foo/.bar").stem() << std::endl;     // ".bar"
    return 0;
}
```

#### exists

```c++
#include <filesystem>
#include <fstream>
#include <iostream>

namespace fs = std ::filesystem;

void demo_exists(const fs::path &p) {
    std::cout << p;
    if (fs::exists(p))
        std::cout << " exists\n";
    else
        std::cout << " does not exist\n";
}

int main() {
    fs::create_directory("sandbox");
    std::ofstream("sandbox/file");
    demo_exists("sandbox/file");  // "sandbox/file" exists
    demo_exists("sandbox/cacho"); // "sandbox/cacho" does not exist
    fs::remove_all("sandbox");
    return 0;
}

```


### Type safety

- **bad – the unit is ambiguous**
    ```c++
    void blink_led_bad (int time_to_blink ) {
        // do something with time_to_blink
    }
    ```
- **good – the unit is explicit**
    ```c++
    void blink_led_good ( miliseconds time_to_blink ) {
        // do something with time_to_blink
    }
    ```

- **Usage**
    ```c++
    void use () {
        blink_led_good (100); // ERROR: What unit?
        blink_led_good (100ms); //
        blink_led_good (5s); // ERROR: Bad unit
    }
    ```


## Modern C++ Classes


### Example class definition

```c++
class Image { // Should be in Image.hpp
public:
    Image(const std ::string &file_name);
    void Draw();

private:
    int rows_ = 0; // New in C+=11
    int cols_ = 0; // New in C+=11
};
```


### What about structs?

- struct is a class where everything is public
- **GOOGLE-STYLE** Use **struct** as a **simple data container**, if it needs a function it should be a **class** instead.

### Always initialize structs using braced initialization

```c++
struct NamedInt {
    int num;
    std :: string name;
};

NamedInt var{1, std :: string{"hello"}};
```

### Constructors and Destructor

- Classes always have **at least one Constructor** and **exactly one Destructor**
- Constructors crash course:
    - Are functions with no **explicit** return type
    - Named exactly as the class
    - There can be many constructors
    - **If there is no explicit constructor an implicit default constructor will be generated**.
- Destructor for class SomeClass:
    - `~SomeClass()`
    - Last function called in the lifetime of an object
    - Generated automatically if not explicitly defined


### Many ways to create instances

```c++
class SomeClass {
public:
    SomeClass(){};               // Default constructor.
    SomeClass(int a){};          // Custom constructor.
    SomeClass(int a, float b){}; // Custom constructor.
    ~SomeClass(){};              // Destructor.
};
// How to use them?
int main() {
    SomeClass var_1;     // Default constructor
    SomeClass var_2(10); // Custom constructor
    // Type is checked when using {} braces. Use them!
    SomeClass var_3{10};          // Custom constructor
    SomeClass var_4 = {10};       // Same as var_3
    SomeClass var_5{10, 10.0};    // Custom constructor
    SomeClass var_6 = {10, 10.0}; // Same as var_5
    return 0;
}
```

### Setting and getting data

- Use **initializer list** to initialize data
- Name getter functions as the private member they return
- **Avoid setters**, set data in the constructor

```c++
class Student {
public:
    // initializer list
    Student(int id, std::string name) : id_{id}, name_{name} {}
    // getter
    int id() const { return id_; }
    const std::string &name() const { return name_; }

private:
    int id_;
    std::string name_;
};
```


### Declaration and definition

- Data members belong to declaration
- Class methods can be defined elsewhere
- Class name becomes part of function name
    ```c++
    SomeClass::SomeClass () {} // This is a constructor
    int SomeClass::var () const { return var_; }
    void SomeClass::DoSmth () {}
    ```

### Always initialize members for classes

- **C++ 11 allows to initialize variables in-place**
- **Do not initialize them in the constructor**
- No need for an explicit default constructor


```c++
class Student {
public:
    // No need for default constructor.
    // Getters and functions omitted.
private:
    int earned_points_ = 0;   // initialize in-place
    float happiness_ = 1.0f;
};
```

- **Note**: Leave the members of structs uninitialized as which will forbid using brace initialization


### Const correctness

- **const** after function states that this function **does not change the object**
    ```c++
    int var () const;
    ```
- Mark all functions that **should not** change the state of the object as **const**
- Ensures that we can pass objects by a **const** reference and still call their functions
    ```c++
    #include <iostream>
    #include <string>

    class Student {
    public:
        Student(std::string name) : name_(name) {}
        // This function might change the object
        // compilation error, you must add `const` after the function name()
        const std::string &name() { return name_; }

    private:
        std::string name_;
    };

    void Print(const Student &s) { std::cout << s.name() << std::endl; }

    // error: 'this' argument to member function 'name' has type 'const Student',
    // but function is not marked const
    ```

### Move semantics

#### Intuition lvalues, rvalues

- Every expression is an **lvalue** or an **rvalue**
- lvalues can be written on the **left** of assignment operator (=)
- rvalues are all the other expressions
- Explicit rvalue defined using **&&**
- Use `std::move(…)` to explicitly convert an lvalue to an rvalue

```c++
int a; // "a" is an lvalue
int& a_ref = a; // "a" is an lvalue
                // "a_ref" is a reference to an lvalue
a = 2 + 2;  // "a" is an lvalue ,
            // "2 + 2" is an rvalue
int b = a + 2;  // "b" is an lvalue ,
                // "a + 2" is an rvalue
int&& c = std::move(a); // "c" is an rvalue
```


#### std::move

- `std::move` is used to indicate that an object **t** may be “moved from”, i.e. allowing the efficient transfer of resources from **t** to another object.
- In particular, **std::move** produces an **xvalue expression** that identifies its argument **t**. It is exactly equivalent to a `static_cast` to an rvalue reference type.
- So, this is the definition, it's **impossible to understand**...

#### Important std::move

- The `std::move()` is a standard-library function returning an **rvalue** reference to its argument.
- `std::move(x)` means "give me an rvalue reference to x.""
- That is, `std::move(x)` does not move anything; instead, it allows a user to move **x**, taking ownership.

#### Hands on example

```c++
#include <iostream>
#include <string>

using namespace std; // Save space on slides.
void Print(const string &str) { cout << "lvalue: " << str << endl; }
// the parameter is a rvalue
void Print(string &&str) { cout << "rvalue: " << str << endl; }

int main() {
    string hello = "hi";
    Print(hello);            // lvalue: hi
    Print("world");          // rvalue: world
    Print(std::move(hello)); // rvalue: hi
    // DO NOT access "hello" after move!
    return 0;
}
```

#### Never access values after move

- The value after **move** is **undefined**

```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string str = "Hello";
    std::vector<std::string> v;

    // uses the push_back(const T&) overload , which means
    // we'll incur the cost of copying str
    v.push_back(str);
    std::cout << "After copy , str is " << str << std::endl;
    // After copy , str is Hello

    // uses the rvalue reference push_back(T&&) overload ,
    // which means no strings will be copied; instead ,
    // the contents of str will be moved into the vector.
    // This is less expensive , but also means str might
    // now be empty.
    v.push_back(std::move(str));
    std::cout << "After move , str is " << str << std::endl;
    // After move , str is
    return 0;
}
```

#### How to think about std::move

- Think about **ownership**
- Entity **owns** a variable if it deletes it, e.g.
    - A function scope owns a variable defined in it 
    - An object of a class owns its data members
- **Moving a variable transfers ownership** of its resources to another variable
- When designing your program think **who should own this thing?**.
- **Runtime**: better than copying, worse than passing by reference.


### Custom operators for a class

- Operators are functions with a signature:
    - `<RETURN_TYPE> operator<NAME>(<PARAMS>)`
- `<NAME>` represents the target operation, e.g. `>, <, =, ==, <<` etc.
- Have all attributes of functions
- All available operators: http://en.cppreference.com/w/cpp/language/operators

#### Example operator `<`

```c++
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

class Human {
public:
    Human(int kindness) : kindness_(kindness) {}
    bool operator<(const Human &other) const {
        return kindness_ < other.kindness_;
    }
    int kindness() const { return kindness_; }

private:
    int kindness_ = 100;
};

int main() {
    std::vector<Human> humans = {Human(40), Human(20), Human(30)};
    std::sort(humans.begin(), humans.end());
    for (const auto &human : humans) {
        std::cout << human.kindness() << std::endl;
    }
    // 20 30 40
    return 0;
}
```


#### Example operator `<<`


```c++
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

class Human {
public:
    Human(int kindness) : kindness_(kindness) {}
    int kindness() const { return kindness_; }

private:
    int kindness_ = 100;
};

std::ostream &operator<<(std::ostream &os, const Human &human) {
    return os << "Human with kindness " << human.kindness();
}

int main() {
    std::vector<Human> humans = {Human{0}, Human{10}};
    for (const auto &human : humans) {
        std::cout << human << std::endl;
    }
    return 0;
}
// Human with kindness 0
// Human with kindness 10
```


### Class Special Functions

#### Copy constructor

- **Called automatically** when the object is **copied**
- For a class `MyClass` has the signature: `MyClass(const MyClass& other)`
    ```c++
    MyClass a;      // Calling default constructor.
    MyClass b(a);   // Calling copy constructor.
    MyClass c = a;  // Calling copy constructor.
    ```

#### Copy assignment operator

- Copy assignment operator is **called automatically** when the object is **assigned a new value** from an **L**value
- For class `MyClass` has a signature: `MyClass& operator=(const MyClass& other)`
- **Returns a reference** to the changed object
- Use **this** from within a function of a class to get a reference to the current object
    ```c++
    MyClass a;     // Calling default constructor.
    MyClass b(a);  // Calling copy constructor.
    MyClass c = a; // Calling copy constructor.  ???
    a = b;         // Calling copy assignment operator.
    ```

#### Move constructor

- **Called automatically** when the object is **moved**
- For a class `MyClass` has a signature: `MyClass(MyClass&& other)`
    ```c++
    MyClass a;                  // Default constructors.
    MyClass b(std::move(a));  // Move constructor.
    MyClass c = std::move(a); // Move constructor.
    ```

#### Move assignment operator

- **Called automatically** when the object is **assigned a new value** from an **R**value
- For class *MyClass* has a signature: `MyClass& operator=(MyClass&& other)`
- **Returns a reference** to the changed object
    ```c++
    MyClass a;                  // Default constructors.
    MyClass b(std::move(a));  // Move constructor.
    MyClass c = std::move(a); // Move constructor.
    b = std::move(c);         // Move assignment operator.
    ```

#### Example

```c++
#include <iostream>

using std::cout;
using std::endl;

class MyClass {
public:
    MyClass() { cout << "default" << endl; }
    // Copy(&) and Move(&&) constructors
    MyClass(const MyClass &other) { cout << "copy" << endl; }
    MyClass(MyClass &&other) { cout << "move" << endl; }
    // Copy(&) and Move(&&) operators
    MyClass &operator=(const MyClass &other) {
        cout << "copy assignment" << endl;
        return *this;
    }
    MyClass &operator=(MyClass &&other) {
        cout << "move assignment" << endl;
        return *this;
    }
};

int main() {
    MyClass a;                 // default
    MyClass b = a;             // copy
    a = b;                     // copy assignment
    MyClass c = std ::move(a); // move
    c = std ::move(b);         // move assignment
    return 0;
}
```


#### Do I need to define all of them?

- The constructors and operators will be **generated automatically**
- **Under some conditions…**
- Six special functions for class `MyClass`:
    ```c++
    MyClass()
    MyClass(const MyClass& other)
    MyClass& operator=(const MyClass& other)
    MyClass(MyClass&& other)
    MyClass& operator=(MyClass&& other)
    ~MyClass()
    ```
- **None** of them defined: **all** auto-generated
- **Any** of them defined: **none** auto-generated


#### Rule of all or nothing

- Try to **define** none of the special functions
- If you **must** define one of them define **all**
- Use `=default` to use default implementation
    - because usually the compiler will give you a better implementation
    - for example, you have to define a destructor
        ```c++
        class MyClass {
        public:
            MyClass () = default;
            MyClass(MyClass && var) = default;
            MyClass(const MyClass& var) = default;
            MyClass& operator=( MyClass && var) = default;
            MyClass& operator=(const MyClass& var) = default;
        };
        ```

#### Deleted functions

- Any function can be set as **deleted**
    ```c++
    void SomeFunc (...) = delete;
    ```
- Calling such a function will result in compilation error
    - Example: remove copy constructors when only one instance of the class must be guaranteed (`Singleton Pattern`)
- Compiler marks some functions deleted automatically
    - Example: if a class has a constant data member, the `copy/move` constructors and `assignment` operators are implicitly deleted



### Static variables and methods

- **Static member variables of a class**
    - Exist exactly **once** per class, **not** per object
    - The value is equal across all instances
    - Must be defined in `*.cpp` files(before C++17)
- **Static member functions of a class**
    - Do not need to access through an object of the class
    - Can access private members but need an object
    - Syntax for calling:
        - `ClassName::MethodName(<params>)`

### `using` for type aliasing

- Use word `using` to declare new types from existing and to create type aliases
- Basic syntax: `using NewType = OldType`;
- `using` is a versatile word
    - When used outside of functions declares a new type alias
    - When used in function creates an alias of a type available in the current scope
- http://en.cppreference.com/w/cpp/language/type_alias

```c++
#include <array>
#include <memory>

template <class T, int SIZE> struct Image {
    // Can be used in classes.
    using Ptr = std ::unique_ptr<Image<T, SIZE>>;
    std ::array<T, SIZE> data;
};
// Can be combined with "template".
template <int SIZE> using Imagef = Image<float, SIZE>;

int main() {
    // Can be used in a function for type aliasing.
    using Image3f = Imagef<3>;
    auto image_ptr = Image3f ::Ptr(new Image3f);
    return 0;
}
```

### Enumeration classes

- Store an enumeration of options
- Usually derived from `int` type
- Options are assigned consequent numbers
- Mostly used to pick path in `switch`
    ```c++
    enum class EnumType { OPTION_1 , OPTION_2 , OPTION_3 };
    ```
- Use values as:
    ```c++
    EnumType::OPTION_1, EnumType::OPTION_2, …
    ```

```c++
#include <iostream>
#include <string>

using std::cout, std::cerr, std::endl, std::string;

enum class Channel { STDOUT, STDERR };

void Print(Channel print_style, const string &msg) {
    switch (print_style) {
    case Channel::STDOUT:
        cout << msg << endl;
        break;
    case Channel::STDERR:
        cerr << msg << endl;
        break;
    default:
        cerr << "Skipping\n";
    }
}
int main() {
    Print(Channel ::STDOUT, "hello");
    Print(Channel ::STDERR, "world");
    return 0;
}
```

#### Explicit values

- By default enum values start from 0
- We can specify custom values if needed
- Usually used with default values


```c++
enum class EnumType {
    OPTION_1 = 10,   // Decimal.
    OPTION_2 = 0x2, // Hexacedimal.
    OPTION_3 = 13
};
```


## Modern C++: Object Oriented Design (Lecture 7, I. Vizzo, 2020)


### C vs C++ Inheritance Example
- C code
    ```c
    // "Base" class , Vehicle
    typedef struct vehicle {
        int seats_;     // number of seats on the vehicle
        int capacity_ ; // amount of fuel of the gas tank
        char* brand_;   // make of the vehicle
    } vehicle_t ;
    ```
- C++ code
    ```c++
    class Vehicle {
        private:
            int seats_ = 0;    // number of seats on the vehicle
            int capacity_ = 0; // amount of fuel of the gas tank
            string brand_;     // make of the vehicle
    }
    ```


### Inheritance

- Class and struct can inherit data and functions from other classes
- There are 3 types of inheritance in C++:
    - public [used in this course] **GOOGLE-STYLE**
    - protected
    - private
- public inheritance keeps all access specifiers of the base class


### Public inheritance

- Allows Derived to use all **public** and **protected** members of Base
- **Derived** still gets its own special functions: constructors, destructor, assignment operators
    ```c++
    class Derived : public Base {
        // Contents of the derived class.
    };
    ```

```c++
#include <iostream>
using std::cout, std::endl;

class Rectangle {
public:
    Rectangle(int w, int h) : width_{w}, height_{h} {}
    int width() const { return width_; }
    int height() const { return height_; }

protected:
    int width_ = 0;
    int height_ = 0;
};

class Square : public Rectangle {
public:
    // initialize base class with initializer list, same as Rectangle(w, h)
    explicit Square(int size) : Rectangle{size, size} {}
};

int main() {
    Square sq(10); // Short name to save space.
    cout << sq.width() << " " << sq.height() << endl;
    return 0;
}
```

### Function overriding

- A function can be declared virtual: 
    - `virtual Func(<PARAMS>);`
- If function is virtual in `Base` class it can be overridden in `Derived` class:
    - `Func(<PARAMS>) override;`
- `Base` can **force** all `Derived` classes to override a function by making it **pure virtual**
    - `virtual Func(<PARAMS>) = 0;`
    - sometimes, you may not see the keywords `virtual`, but it is still a pure virtual function,  because
        - A member function that overrides a virtual funcction in the base class is automatically virtual even if the virtual keywors is not used


### Overloading vs overriding

- **Overloading**
    - Pick from all functions with the **same name**, but **different parameters**
    - Pick a function at **compile time**
    - Functions don’t have to be in a class
- **overriding**
    - Pick from functions with the **same arguments and names** in different classes of **one class hierarchy**
    - Pick **at runtime**


### Abstract classes and interfaces

- **Abstract class**: class that has at least one `pure virtual function`
- **Interface**: class that has only `pure virtual functions` and no data members

### How virtual works

- A class **with virtual functions** has a virtual table
- When calling a function the class checks which of the virtual functions that match the signature should be called
- Called **runtime polymorphism**
- Costs some time but is very convenient

### Using interfaces

- Use interfaces when you must **enforce** other classes to implement some functionality
- Allow thinking about classes in terms of **abstract functionality**
- **Hide implementation** from the caller
- Allow to easily extend functionality by simply adding a new class

```c++
#include <iostream>

using std ::cout, std ::endl;

struct Printable { // Saving space. Should be a class.
    virtual void Print() const = 0;
};
struct A : public Printable {
    void Print() const override { cout << "A" << endl; }
};
struct B : public Printable {
    void Print() const override { cout << "B" << endl; }
};

void Print(const Printable &var) { var.Print(); }

int main() {
    Print(A());
    Print(B());
    return 0;
}
```


### Polymorphism

- Allows morphing derived classes into their base class type:
    - `const Base& base = Derived(…)`
- Allows encapsulating the implementation inside a class only asking it to conform to a common interface
- Often used for:
    - Working with all children of some Base class in unified manner
    - Enforcing an interface in multiple classes to force them to implement some functionality
    - In **strategy** pattern, where some complex functionality is outsourced into separate classes and is passed to the object in a modular fashion


- GOOGLE-STYLE: **Prefer composition**
    - i.e. including an object of another class as a member of your class


### Type Casting

#### Casting type of variables

- Every variable has a type
- Types can be converted from one to another
- Type conversion is called **type casting**

- There are 5 ways of type casting:
    - `static_cast`
    - `reinterpret_cast`
    - `const_cast`
    - `dynamic_cast`
    - C-style cast(unsafe)
        - compile will try combination of those 4 casting, and you have no idea what's going on

#### static_cast

- `static_cast<NewType>(variable)`
- Convert type of a variable at **compile** time
- **Rarely needed to be used explicitly**
- Can happen implicitly for some types, e.g. float can be cast to int
- Pointer to an object of a Derived class can be **upcast** to a pointer of a Base class
- Enum value can be caster to int or float
- Full specification is complex!


#### dynamic_cast

- `dynamic_cast<Base*>(derived_ptr)`
- Used to convert a pointer to a variable of Derived type to a pointer of a Base type
- Conversion happens at runtime
- If derived_ptr cannot be converted to `Base*` returns a `nullptr`
- GOOGLE-STYLE **Avoid** using dynamic casting


#### reinterpret_cast

- `reinterpret_cast<NewType>(variable)`
- Reinterpret the bytes of a variable as another type
- We must know what we are doing!
- Mostly used when writing binary data


#### const_cast

- `const_cast<NewType>(variable)`
- Used to “constify” objects
- Used to “de-constify” objects
- Not widely used


#### Google Style

- `GOOGLE-STYLE` Do not use C-style casts.
- `GOOGLE-STYLE` Use brace initialization to convert arithmetic types (e.g. `int64{x}`).
    - This is the safest approach because code will not compile if conversion can result in information loss. The syntax is also concise.
- `GOOGLE-STYLE` Use `static_cast` as the equivalent of a C-style cast that does value conversion, 
    - when you need to explicitly up-cast a pointer from a class to its superclass, 
    - or when you need to explicitly cast a pointer from a superclass to a subclass. 
        - In this last case, you must be sure your object is actually an instance of the subclass.
- `GOOGLE-STYLE` Use `const_cast` to remove the const qualifier (see const).
- `google-style` use `reinterpret_cast` to do unsafe conversions of pointer types to and from integer and other pointer types. 
    - Use this only if you know what you are doing and you understand the aliasing issues.


### Using strategy pattern

- If a class relies on complex external functionality use strategy pattern
- Allows to **add/switch functionality** of the class without changing its implementation
- All strategies must conform to one strategy interface

```c++
#include <iostream>

using std::cout, std::endl;

class Strategy {
public:
    virtual void Print() const = 0;
};
class StrategyA : public Strategy {
public:
    void Print() const override { cout << "A" << endl; }
};

class StrategyB : public Strategy {
public:
    void Print() const override { cout << "B" << endl; }
};

// so far, nothing is new, just interface

class MyClass {
public:
    // 2. The strategy will be “picked” when
    //    we create an object of the class MyClass.
    explicit MyClass(const Strategy &s) : strategy_(s) {}
    void Print() const { strategy_.Print(); }

private:
    // 1. holds a const reference to Strategy object
    const Strategy &strategy_;
};
```


#### Do not overuse it

- Only use these patterns when you need to
- If your class should have a single method for some functionality and will never need another implementation don’t make it virtual
- Used mostly to avoid copying code and to make classes smaller by moving some functionality out.


### Singleton Pattern

- We want only one instance of a given class.
- Without C++ this would be a if/else mess.
- C++ has a powerfull compiler, we can use it.
- We can make sure that nobody creates more than 1 instance of a given class, **at compile time**.
- Don’t over use it, it’s easy to learn, but usually hides a **design** error in your code.
- Sometimes is still necessary, and makes your code better.


#### Singleton Pattern: How?

- We can `delete` any **class** member functions.
- This also holds true for the special functions:
    - `MyClass()`
    - `MyClass(const MyClass& other)`
    - `MyClass& operator=(const MyClass& other)`
    - `MyClass(MyClass&& other)`
    - `MyClass& operator=(MyClass&& other)`
    - `~MyClass()`
- Any `private` function can only be accessed by member of the class.

- Let’s **hide** the default Constructor and also the destructor.
    ```c++
    class Singleton {
        private:
            Singleton () = delete ;
            ~ Singleton () = delete ;
    };
    ```
    - This completely **disable** the possibility to create a Singleton object or destroy it.
- And now let’s delete any copy capability:
    - Copy Constructor.
    - Copy Assigment Operator.
    ```c++
    class Singleton {
        public:
            Singleton (const Singleton &) = delete;
            void operator=(const Singleton &) = delete;
    };
    ```
    - This completely **disable** the possibility to copy any existing Singleton object.


#### Singleton Pattern: What now?

- Now we need to create at least **one** instance of the `Singleton` class.
- **How?** Compiler to the rescue:
    - We can create **one unique** instance of the class.
    - At compile time …
    - Using `static` !.
    ```c++
    class Singleton {
        public:
            static Singleton& GetInstance () {
                static Singleton instance ;
                return instance;
            }
    };
    ```

#### Singleton Pattern: Completed

```c++
class Singleton {
private:
    Singleton() = default;
    ~Singleton() = default;

public:
    Singleton(const Singleton &) = delete;
    void operator=(const Singleton &) = delete;
    static Singleton &GetInstance() {
        static Singleton instance;
        return instance;
    }
};
```


#### Singleton Pattern: Usage

```c++
int main() {
    auto &singleton = Singleton ::GetInstance();
    // ...
    // do stuff with singleton , the only instance.
    // ...

    Singleton s1;             // Compiler Error!
    Singleton s2(singleton);  // Compiler Error!
    Singleton s3 = singleton; // Compiler Error!

    return 0;
}
```


## Modern C++: Memory Management (Lecture 8, I. Vizzo, 2020)

- cdtdebug

### Using pointers for classes

- You actually don't do this. If you do, then there's something else wrong...
    ```c++
    MyClass* obj_ptr = &obj;
    obj_ptr ->MyFunc ();
    ```
- `obj->Func()` ↔ `(*obj).Func()`

### Pointers are polymorphic

- Pointers are just like references, but have additional useful properties:
    - Can be reassigned
    - Can point to “nothing” (`nullptr`)
    - Can be stored in a vector or an array
- **Use pointers for polymorphism**
    ```c++
    Derived derived;
    Base* ptr = &derived;
    ```

### this pointer

- Every object of a class or a struct holds a pointer to itself
- This pointer is called `this`
- Allows the objects to:
    - Return a reference to themselves: **return *this;**
    - Create copies of themselves within a function
    - Explicitly show that a member belongs to the current object: `this->x();`
    - `this` is a C++ keyword

### Using const with pointers

- Pointers can **point to** a `const` variable:
    ```c++
    // Cannot change value , can reassign pointer.
    const MyType* const_var_ptr = &var;
    const_var_ptr = & var_other ;
    ```
- Pointers can be const:
    ```c++
    // Cannot reassign pointer , can change value.
    MyType* const var_const_ptr = &var;
    var_const_ptr ->a = 10;
    ```
- Pointers can do both at the same time:
    ```c++
    // Cannot change in any way, read -only.
    const MyType* const const_var_const_ptr = &var;
    ```
- Read from right to left to see which const refers to what


### Stack memory

- **Static** memory (compile time)
- Available for **short term** storage (scope)
- **Small / limited** (8 MB Linux typically)
    ```bash
    $ ulimit -a
    -t: cpu time (seconds)              unlimited
    -f: file size (blocks)              unlimited
    -d: data seg size (kbytes)          unlimited
    -s: stack size (kbytes)             8192
    ...
    ```
- Memory allocation is **fast**
- **LIFO** (Last in First out) structure
- Items added to top of the stack with `push`
- Items removed from the top with `pop`

### Heap memory

- **Dynamic** memory (runtime)
- Available for **long** time (program runtime)
- Raw modifications possible with `new` and `delete` (usually encapsulated within a class)
- Allocation is slower than stack allocations

#### Operators new and new[]

- User controls memory allocation (**unsafe**)
- Use `new` to allocate data:
    ```c++
    // pointer variable stored on stack
    int* int_ptr = nullptr;
    // 'new' returns a pointer to memory in heap
    int_ptr = new int;

    // also works for arrays
    float* float_ptr = nullptr;
    // 'new' returns a pointer to an array on heap
    float_ptr = new float[number ];
    ```
- `new` returns an address of the variable on the heap
- **Prefer using smart pointers!**


#### Operators delete and delete[]

- **Memory is not freed automatically!**
- User must remember to free the memory
- Use `delete` or `delete[]` to free memory:
    ```c++
    int* int_ptr = nullptr;
    int_ptr = new int;
    // delete frees memory to which the pointer points
    delete int_ptr;

    // also works for arrays
    float* float_ptr = nullptr;
    float_ptr = new float[number ];
    // make sure to use 'delete[]' for arrays
    delete[] float_ptr ;
    ```
- **Prefer using smart pointers!**


### Memory leak

- Can happen when working with Heap memory if we are not careful
- **Memory leak**: memory allocated on Heap access to which has been lost
    ```bash
                 heap
    ptr_1 ----> ▢▢▢▢▢▢▢▢▢
           /     LEAKED!
    ptr_2 /     ▨▨▨▨▨▨▨▨▨
    ```
- It will also raise a problem of double free.

### Dangling pointer

- Dangling Pointer: pointer to a freed memory
- Think of it as the opposite of a memory leak
- Dereferencing a dangling pointer causes **undefined behavior**

```c++
int* ptr_1 = some_heap_address ;
int* ptr_2 = some_heap_address ;
delete ptr_1;
ptr_1 = nullptr;
// Cannot use ptr_2 anymore! Behavior undefined!
```

### RAII

- Resource Allocation Is Initialization.
- New object → allocate memory
- Remove object → free memory
- Objects **own** their data!

- You say, ah, I know how to RAII now!
    ```c++
    class MyClass {
    public:
        MyClass() { data_ = new SomeOtherClass; }
        ~MyClass() {
            delete data_;
            data_ = nullptr;
        }

    private:
        SomeOtherClass *data_;
    };
    ```
- Does it work ?
    - No!
    - Still cannot copy an object of `MyClass`!!!
    ```c++
    int main() {
        MyClass a;
        MyClass b(a); // !! double free or corruption : 0 x0000000000877c20 ***
        return 0;
    }
    ```

### Shallow vs deep copy

- Shallow copy: just copy pointers, not data
- Deep copy: copy data, create new pointers
- Default copy constructor and assignment operator implement **shallow copying**
- RAII + shallow copy → **dangling pointer**
- RAII + **Rule of All Or Nothing** → **correct**
- **Use smart pointers instead!**


### Smart pointers

- Smart pointers wrap a raw pointer into a class and manage its lifetime (**RAII**)
- Smart pointers are **all about ownership**
- Always use smart pointers when the pointer should **own heap memory**
- **Only use them with heap memory!**.
- Still use raw pointers for non-owning pointers and simple address storing
- `#include <memory>` to use smart pointers


### C++11 smart pointers types

- **std::unique_ptr**
- **std::shared_ptr**
- std::auto_ptr
- std::weak_ptr
- We will focus on 2 types of smart pointers:
    - `std::unique_ptr` , `std::shared_ptr`


### Smart pointers manage memory!

- Smart pointers apart from memory allocation behave exactly as raw pointers(it is still poiner):
    - Can be set to `nullptr`
    - Use `*ptr` to dereference `ptr`
    - Use `ptr->` to access methods
    - Smart pointers are polymorphic
- **Additional functions of smart pointers:**
    - `ptr.get()` returns a raw pointer that the smart pointer manages
    - `ptr.reset(raw_ptr)` stops using currently managed pointer, freeing its memory if needed, sets `ptr` to `raw_ptr`


### std::unique_ptr 

- A Simple Example
    - Create an `unique_ptr` to a type `Vehicle`
        ```c++
        std :: unique_ptr <Vehicle> vehicle_1 = 
            std :: make_unique <Bus>(20 , 10, "Volkswagen", "LPM_");
        std :: unique_ptr <Vehicle> vehicle_2 = 
            std :: make_unique <Car>(4, 60, "Ford", "Sony");
        ```
    - Now you can have fun as we had with **raw pointers**
        ```c++
        // vehicle_x is a pointer , so we can us it as it is
        vehicle_1 ->Print ();
        vehicle_2 ->Print ();
        ```

---

- `unique_ptr` are **unique** (ownship is unique): This means that we can move stuff but **not copy**:
    - `vehicle_2 = std :: move( vehicle_1 );`
- Address of the pointers before the move:
    ```c++
    cout << "vehicle_1 = " << vehicle_1 .get () << endl;
    cout << "vehicle_2 = " << vehicle_2 .get () << endl;
    // vehicle_1 = 0x56330247ce70  (xxx70)
    // vehicle_2 = 0x56330247cec0  (xxxc0)
    ```
- Address of the pointers after the move:
    ```c++
    // vehicle_2 = 0 x56330247ce70
    // vehicle_1 = 0
    ```

- Wait, Didn't you use NEW and DELETE ?
    - No, we are smart now... right ?

#### Unique pointer (std::unique_ptr)

- Constructor of a unique pointer takes **ownership** of a provided raw pointer
- **No runtime overhead** over a raw pointer
- Syntax for a unique pointer to type Type: (Ugly!!)
    ```c++
    #include <memory>
    // Using default constructor Type();
    auto p = std :: unique_ptr <Type>(new Type);
    // Using constructor Type(<params>);
    auto p = std :: unique_ptr <Type>(new Type(<params>));
    ```
- From C++14 on:
    ```c++
    // Forwards <params> to constructor of unique_ptr
    auto p = std :: make_unique <Type>(<params>);
    ```

#### What makes it “unique”

- Unique pointer **has no copy constructor**
- Cannot be copied, **can be moved**
- Guarantees that memory is always owned by a single `std::unique_ptr`
- A non-null `std::unique_ptr` always owns what it points to.
- Moving a `std::unique_ptr` transfers ownership from the source pointer to the destination pointer. 
    - (The source pointer is set to `nullptr`.)


### Shared pointer (std::shared_ptr)

- What if we want to use the same `pointer` for different resources?
- An object accessed via `std::shared_ptrs` has its lifetime managed by those pointers through shared ownership.
- No specific `std::shared_ptr` owns the object.
    - because you just share the ownship
- When the last `std::shared_ptr` pointing to an object stops pointing there, that `std::shared_ptr` destroys the object it points to

- Constructed just like a `unique_ptr` 
- Can be copied
- Stores a usage counter and a raw pointer
    - Increases usage counter when copied
    - Decreases usage counter when destructed
- Frees memory when counter reaches 0 
- Can be initialized from a `unique_ptr`
- Syntax:
    ```c++
    #include <memory>
    // Using default constructor Type();
    auto p = std :: shared_ptr <Type>(new Type);
    auto p = std :: make_shared <Type>();

    // Using constructor Type(<params>);
    auto p = std :: shared_ptr <Type>(new Type(<params>));
    auto p = std :: make_shared <Type>(<params>);
    ```

#### Shared pointer Example

```c++
#include <iostream>

using std::cout, std::endl;

class MyClass {
public:
    MyClass() { cout << "I'm alive!\n"; }
    ~MyClass() { cout << "I'm dead... :(\n"; }
};

int main() {
    auto a_ptr = std ::make_shared<MyClass>();
    cout << a_ptr.use_count() << endl;
    {
        auto b_ptr = a_ptr;
        cout << a_ptr.use_count() << endl;
    }
    cout << "Back to main scope\n";
    cout << a_ptr.use_count() << endl;
    return 0;
}
// I'm alive!
// 1
// 2
// Back to main scope
// 1
// I'm dead... :(
```

### When to use what?

- Use smart pointers when the pointer **must manage memory**
- By default use `unique_ptr`
- If multiple objects must **share ownership** over something, use a `shared_ptr` to it
- Think of any free standing `new` or `delete` as of a memory leak or a dangling pointer:
    - Don’t use `delete`
    - Allocate memory with `make_unique`, `make_shared`
    - Only use `new` in smart pointer constructor if cannot use the functions above


### Typical beginner error

```c++
int main () {
    // Allocate a variable in the stack
    int a = 42;

    // Create a pointer to that part of the memory
    // first error: why you create a pointer to stack variable? just use reference!
    int* ptr_to_a = &a;

    // Know stuff about pointers eh?
    // 2nd error
    auto a_unique_ptr = std :: unique_ptr <int>( ptr_to_a);

    // Same happens with std::shared_ptr.
    // 3rd error
    auto a_shared_ptr = std :: shared_ptr <int>( ptr_to_a);

    std :: cout << "Program terminated correctly!!!\n";
    return 0;
}
```

- Create a **smart pointer** from a `pointer` to a stack-managed variable
- The variable ends up being owned both by the `smart pointer` and the `stack` and gets deleted twice → **Error!**


## Modern C++ Course: Templates (Lecture 9, I. Vizzo, 2020)

### Function Templates

```c++
template <typename T>
T abs(T x) {
    return (x>= 0) ? x : -x;
}
```

- Function templates are **not** functions.
    - **They are templates for making functions**
- You don’t pay for what you don’t use:
    - If nobody calls `abs<int>`, it won’t be instantiated by the compiler at all.
- A function template defines a **family** of functions.


#### Using Function Templates

```c++
int main () {
    const double x = 5.5;
    const int y = -5;

    auto abs_x = abs <double>(x);
    int abs_y = abs <int>(y);

    double abs_x_2 = abs(x); // type -deduction
    auto abs_y_2 = abs(y); // type -deduction
}
```

**Templates lives in a "static" world.**


### Template classes

```c++
template <class T> class MyClass {
public:
    MyClass(T x) : x_(x) {}

private:
    T x_;
};
```

- Classes templates are not classes.
    - **They are templates for making classes**
- You don’t pay for what you don’t use:
    - If nobody calls `MyClass<int>`, it won’t be instantiated by the compiler at all.

#### Template classes usage

```c++
int main() {
    MyClass<int> my_float_object(10);
    MyClass<double> my_double_object(10.0);
    return 0;
}
```

### Template Parameters

```c++
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

template <typename T, size_t N = 10>
T AccumulateVector (const T& val) {
    std::vector <T> vec(val , N);
    return std::accumulate (vec.begin (), vec.end (), 0);
}
```

- Every **template** is parameterized by one or more **template parameters**:
    - `template < parameter-list > declaration`
- Think the template parameters the same way as any function arguemnents, but at compile-time.

#### Usage

```c++
using std::cout, std::endl;
int main() {
    cout << AccumulateVector(1) << endl;             // 10
    cout << AccumulateVector<float>(2) << endl;      // 20
    cout << AccumulateVector<float, 5>(2.0) << endl; // 10
    return 0;
}
```

### Template Full Specialization

- Prefix the definition with `template<>`
- Then write the function **definition**.
- Usually means you don’t need to write any more angle brackets at all.
- Unless `T` can’t be deduced/defaulted:

```c++
template <typename T>
int my_sizeof () {
    return sizeof(T);
}

template <>
int my_sizeof <void >() {
    return 1;
}
```





