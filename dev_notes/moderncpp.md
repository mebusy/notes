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

- youtube
    - https://www.youtube.com/watch?v=9mZw6Rwz1vg&list=PLgnQpQtFTOGRM59sr3nSL8BmeMZR9GCIA&index=5
- STL algorithm
    - https://en.cppreference.com/w/cpp/algorithm
- C++ Utilities
    - https://en.cppreference.com/w/cpp/utility
- Google C++ Testing
    - https://www.youtube.com/watch?v=nbFXI9SDfbk



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
    - `m.count(key) > 0` 
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

```c++
    // can be either int or float, but not both
    std::variant <int, float > v1;
    v1 = 12; // v contains int
    cout << std::get <int >(v1) << endl; // 12
    // will raise error if you want to get float

    std::variant <int, float > v2 {3.14F};
    cout << std::get <1>(v2) << endl;  // 3.14

    v2 = std::get <int >(v1); // assigns v1 to v2
    v2 = std::get <0>(v1);  // same assignment
    v2 = v1;  // same assignment
    cout << std::get <int >(v2) << endl; // 12
```

<h2 id="68cdf81a296c17812f5703c4853431bf"></h2>

#### std::any

- `#include <any>`

```c++
    std::any a; // any type
    a = 1; // int
    std::cout << std::any_cast<int>(a) << std::endl;

    a = 3.14; // double
    std::cout << std::any_cast <double >(a) << std::endl;  // 3.14

    a = true; // bool
    std::cout << std::boolalpha << std::any_cast <bool >(a) << std::endl; // true
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
    std::tuple <double , char , string > student1;

    using Student = std::tuple <double , char , string >;
    Student student2 {1.4 , 'A', "Jose"};

    cout << std::get <string >( student2) << endl; // Jose
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

    std::chrono::duration <double > sec = end - start;
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










