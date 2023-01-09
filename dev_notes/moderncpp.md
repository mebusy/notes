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
    - [Modern C++: I/O Files (Lecture 5, I. Vizzo, 2020)](#6b612f673c58c59f08dd9dff98921501)
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
            - [filename](#435ed7e9f07f740abf511a62c00eef6e)
            - [extension](#566bbee0f961ad71b54c3c2fd36db053)
            - [stem](#e730db5c29b7ba34f4d465b01bd33c5e)
            - [exists](#e087923eb5dd1310f5f25ddd5ae5b580)
        - [Type safety](#8c800c6bd66ee804c1102836b8f375be)
    - [Modern C++ Classes](#54bf25ff3921c0e5ebdc9205b7902c35)
        - [Example class definition](#75458cc99937a04c5e3353e144a7a992)
        - [What about structs?](#f09bc6faed74c3fbab3311f610c57565)
        - [Always initialize structs using braced initialization](#bdc1ff08b6ff00c1a6a5b95e9552c6a6)
        - [Constructors and Destructor](#fff7c892e0960645e398064e32ab6297)
        - [Many ways to create instances](#352771047fedbd7b0eb907c89c1634c6)
        - [Setting and getting data](#e043c979883e65dc381c618fbe7e1706)
        - [Declaration and definition](#b84d0e8580534792f9b7d25188b8283f)
        - [Always initialize members for classes](#80dfe513dea5b2ac3ea182d6b164675c)
        - [Const correctness](#3a1dedcb28865ffa846a83439ad98f4b)
        - [Move semantics](#6968e0c5ce7cf21cda6568106fc4ad90)
            - [Intuition lvalues, rvalues](#84be678c622eb3674adb2dadfa62d994)
            - [std::move](#c8926a02e9917ba20ca6e44cbee36963)
            - [Important std::move](#31fc7853dce961550bd94847833116d9)
            - [Hands on example](#0f8701acaf3e6cfc809cfa7d9be7a335)
            - [Never access values after move](#61bf40f95ea0221e41cd38fe7bb94ac5)
            - [How to think about std::move](#f98cc579cb1039871a752bcd0be13615)
        - [Custom operators for a class](#466d5122ff97297902e40b755d7a2ab1)
            - [Example operator `<`](#741d87ff4c970c140c8e12c122716da0)
            - [Example operator `<<`](#d40b75c8bf9d8972f500b8bb25637a1f)
        - [Class Special Functions](#2b04788ff820d22f5fd6cf3e87713bfe)
            - [Copy constructor](#9e81af005e7a42287f55a805bdaf3db9)
            - [Copy assignment operator](#b339bb2a7c67336b33c2f442e5207325)
            - [Move constructor](#04f69f35142789ab5f10ae43efab0a54)
            - [Move assignment operator](#c332414ee8b3a0feb6ea9a528ce3a46d)
            - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
            - [Do I need to define all of them?](#08cad8a0c7a42eca501678c7171f892a)
            - [Rule of all or nothing](#856d2d3cbcb99bdc02d67407467887e5)
            - [Deleted functions](#5312eb6759309d28c7ea2d239a4f7e72)
        - [Static variables and methods](#f258b4094c997d13c499fc50cc0138cf)
        - [`using` for type aliasing](#fbe24973f9df7e0a856ccd9d871c4b90)
        - [Enumeration classes](#d777b421635efebe637ee2f4726d5689)
            - [Explicit values](#a22b86e6d7d06811669d602bbb89e7c0)
    - [Modern C++: Object Oriented Design (Lecture 7, I. Vizzo, 2020)](#59427b00f0bc9e475e34732652d9395e)
        - [C vs C++ Inheritance Example](#adc9ad40993dd6a8ffd8c5ce60244c16)
        - [Inheritance](#e40489cd1e7102e35469c937e05c8bba)
        - [Public inheritance](#37f714fa982009c0f7f34a34222f19c6)
        - [Function overriding](#9838b3876aec076af99ebf663cfd7b7a)
        - [Overloading vs overriding](#8a88083322dc5c249a3dc33b350ee8b5)
        - [Abstract classes and interfaces](#4c7393aee7be19ada4689a7b266a1be1)
        - [How virtual works](#8fbbb2c24bf977e5ed7f81e2f229bc06)
        - [Using interfaces](#f6f847324f6a271ea8bd9e36a55511bd)
        - [Polymorphism](#371fedf6ee6747b1de368aafb08094e8)
        - [Type Casting](#479c01e471347f335628cee17db0bf54)
            - [Casting type of variables](#784be77baa4e7400b3b0e93738c5d66b)
            - [static_cast](#7788e276172dacc2d8d33631b670d026)
            - [dynamic_cast](#fe9be20b5d842a2d5963b97405c48505)
            - [reinterpret_cast](#dcb294fefdac1da8cef8bcd08d082ebf)
            - [const_cast](#cee88a63ff1bf6d523474d7541ef35d8)
            - [Google Style](#ca5cd6f7f005a605b98372084def1151)
        - [Using strategy pattern](#f158d755e5e03f201a3dc6a3afd64932)
            - [Do not overuse it](#bb58d1a88af40f4f934c4dffa00ed22c)
        - [Singleton Pattern](#685dbb4186ac6d36022cfce886a84a95)
            - [Singleton Pattern: How?](#a07d5ad4d01026b8866d306c2b5949f1)
            - [Singleton Pattern: What now?](#7678e529808ac059561fe6aacf2a7978)
            - [Singleton Pattern: Completed](#6a1ac8cfc4b7407c34517264846ea4b9)
            - [Singleton Pattern: Usage](#665b944a415c8ddbd9ed36ddbb7f82c9)
    - [Modern C++: Memory Management (Lecture 8, I. Vizzo, 2020)](#8cfd35dc9cd1d651af6f30e4c35cef61)
        - [Using pointers for classes](#6c0d5a1fc5c807937c9b607415342ca0)
        - [Pointers are polymorphic](#4d968934f6b4cb1379ef5be325f5893c)
        - [this pointer](#e88f1fdda31d52dc7548803ec585a30f)
        - [Using const with pointers](#6cd14f084543b2c4c8c156f51c0324e0)
        - [Stack memory](#83606af2c1b6fdc0c282316a2a0f7c7a)
        - [Heap memory](#c44d45c3605314ab2b325d1e136bda78)
            - [Operators new and new\[\]](#9efb2d5bad0c25e7b0adb30fd0ae501a)
            - [Operators delete and delete\[\]](#25f56d385df2991bc164c6a6b9cfe858)
        - [Memory leak](#c78f80d07a54f3c3d7e38298cc4a1786)
        - [Dangling pointer](#e83d85c788c205ca23e19b8c71e6b39b)
        - [RAII](#cc4f050d3506116dff9932e4a4757538)
        - [Shallow vs deep copy](#b18489be0d1214fc2a0f7a298e8c52c0)
        - [Smart pointers](#458ac9389d0193edc10ce1dfdd38f863)
        - [C++11 smart pointers types](#86971efe3c54c299f3907707bec8e9ad)
        - [Smart pointers manage memory!](#c2aba4da9cb163cfb67728508ee2ac9a)
        - [std::unique_ptr](#16f2e352c2cf12dca00e4dc91155f5da)
            - [Unique pointer (std::unique_ptr)](#f33f2c9b7326ad4e484bdbacb864c84b)
            - [What makes it “unique”](#8a41b856c1a73927ce95f110f3250ee7)
        - [Shared pointer (std::shared_ptr)](#45a58bbc7dc4952b58ee0a2b32e6b48f)
            - [Shared pointer Example](#dc9ef9971bc35a4001eca9017ef469e9)
        - [When to use what?](#e0cea2d9b07115ed4382ac3f387083dc)
        - [Typical beginner error](#203e97fd9b28daf2c3e09382bac0d780)
    - [Modern C++ Course: Templates (Lecture 9, I. Vizzo, 2020)](#767ee4093437fa55b8b907894fa83222)
        - [Function Templates](#a6b89f6ccba6b648ecd74450ed854270)
            - [Using Function Templates](#c2ec03a8417f8f4202a6a2932ad5e8c3)
        - [Template classes](#388f30d859ac3e81d44254f60c3db2f6)
            - [Template classes usage](#d44c55af7e30ae17cc73e9567c4cd549)
        - [Template Parameters](#ba2ee1ff0688e49bdc6a7a3588538c0d)
            - [Usage](#c64518704ce0c0d5501a45763f464276)
        - [Template Full/Partial Specialization](#2653777f97753f188dcfad2b7743ce47)
        - [Static code generatrion with constexpr](#9827d2ec485f02fcd7073d1cd9650f3a)

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
    - CppCon 2016: Arthur O'Dwyer “Template Normal Programming (part 1 of 2)”
        - https://www.youtube.com/watch?v=vwrXHznaYLA


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

<h2 id="6b612f673c58c59f08dd9dff98921501"></h2>

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


<h2 id="435ed7e9f07f740abf511a62c00eef6e"></h2>

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

<h2 id="566bbee0f961ad71b54c3c2fd36db053"></h2>

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


<h2 id="e730db5c29b7ba34f4d465b01bd33c5e"></h2>

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

<h2 id="e087923eb5dd1310f5f25ddd5ae5b580"></h2>

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


<h2 id="8c800c6bd66ee804c1102836b8f375be"></h2>

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


<h2 id="54bf25ff3921c0e5ebdc9205b7902c35"></h2>

## Modern C++ Classes


<h2 id="75458cc99937a04c5e3353e144a7a992"></h2>

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


<h2 id="f09bc6faed74c3fbab3311f610c57565"></h2>

### What about structs?

- struct is a class where everything is public
- **GOOGLE-STYLE** Use **struct** as a **simple data container**, if it needs a function it should be a **class** instead.

<h2 id="bdc1ff08b6ff00c1a6a5b95e9552c6a6"></h2>

### Always initialize structs using braced initialization

```c++
struct NamedInt {
    int num;
    std :: string name;
};

NamedInt var{1, std :: string{"hello"}};
```

<h2 id="fff7c892e0960645e398064e32ab6297"></h2>

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


<h2 id="352771047fedbd7b0eb907c89c1634c6"></h2>

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

<h2 id="e043c979883e65dc381c618fbe7e1706"></h2>

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


<h2 id="b84d0e8580534792f9b7d25188b8283f"></h2>

### Declaration and definition

- Data members belong to declaration
- Class methods can be defined elsewhere
- Class name becomes part of function name
    ```c++
    SomeClass::SomeClass () {} // This is a constructor
    int SomeClass::var () const { return var_; }
    void SomeClass::DoSmth () {}
    ```

<h2 id="80dfe513dea5b2ac3ea182d6b164675c"></h2>

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


<h2 id="3a1dedcb28865ffa846a83439ad98f4b"></h2>

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

<h2 id="6968e0c5ce7cf21cda6568106fc4ad90"></h2>

### Move semantics

<h2 id="84be678c622eb3674adb2dadfa62d994"></h2>

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


<h2 id="c8926a02e9917ba20ca6e44cbee36963"></h2>

#### std::move

- `std::move` is used to indicate that an object **t** may be “moved from”, i.e. allowing the efficient transfer of resources from **t** to another object.
- In particular, **std::move** produces an **xvalue expression** that identifies its argument **t**. It is exactly equivalent to a `static_cast` to an rvalue reference type.
- So, this is the definition, it's **impossible to understand**...

<h2 id="31fc7853dce961550bd94847833116d9"></h2>

#### Important std::move

- The `std::move()` is a standard-library function returning an **rvalue** reference to its argument.
- `std::move(x)` means "give me an rvalue reference to x.""
- That is, `std::move(x)` does not move anything; instead, it allows a user to move **x**, taking ownership.

<h2 id="0f8701acaf3e6cfc809cfa7d9be7a335"></h2>

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

<h2 id="61bf40f95ea0221e41cd38fe7bb94ac5"></h2>

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

<h2 id="f98cc579cb1039871a752bcd0be13615"></h2>

#### How to think about std::move

- Think about **ownership**
- Entity **owns** a variable if it deletes it, e.g.
    - A function scope owns a variable defined in it 
    - An object of a class owns its data members
- **Moving a variable transfers ownership** of its resources to another variable
- When designing your program think **who should own this thing?**.
- **Runtime**: better than copying, worse than passing by reference.


<h2 id="466d5122ff97297902e40b755d7a2ab1"></h2>

### Custom operators for a class

- Operators are functions with a signature:
    - `<RETURN_TYPE> operator<NAME>(<PARAMS>)`
- `<NAME>` represents the target operation, e.g. `>, <, =, ==, <<` etc.
- Have all attributes of functions
- All available operators: http://en.cppreference.com/w/cpp/language/operators

<h2 id="741d87ff4c970c140c8e12c122716da0"></h2>

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


<h2 id="d40b75c8bf9d8972f500b8bb25637a1f"></h2>

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


<h2 id="2b04788ff820d22f5fd6cf3e87713bfe"></h2>

### Class Special Functions

<h2 id="9e81af005e7a42287f55a805bdaf3db9"></h2>

#### Copy constructor

- **Called automatically** when the object is **copied**
- For a class `MyClass` has the signature: `MyClass(const MyClass& other)`
    ```c++
    MyClass a;      // Calling default constructor.
    MyClass b(a);   // Calling copy constructor.
    MyClass c = a;  // Calling copy constructor.
    ```

<h2 id="b339bb2a7c67336b33c2f442e5207325"></h2>

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

<h2 id="04f69f35142789ab5f10ae43efab0a54"></h2>

#### Move constructor

- **Called automatically** when the object is **moved**
- For a class `MyClass` has a signature: `MyClass(MyClass&& other)`
    ```c++
    MyClass a;                  // Default constructors.
    MyClass b(std::move(a));  // Move constructor.
    MyClass c = std::move(a); // Move constructor.
    ```

<h2 id="c332414ee8b3a0feb6ea9a528ce3a46d"></h2>

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

<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>

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


<h2 id="08cad8a0c7a42eca501678c7171f892a"></h2>

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


<h2 id="856d2d3cbcb99bdc02d67407467887e5"></h2>

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

<h2 id="5312eb6759309d28c7ea2d239a4f7e72"></h2>

#### Deleted functions

- Any function can be set as **deleted**
    ```c++
    void SomeFunc (...) = delete;
    ```
- Calling such a function will result in compilation error
    - Example: remove copy constructors when only one instance of the class must be guaranteed (`Singleton Pattern`)
- Compiler marks some functions deleted automatically
    - Example: if a class has a constant data member, the `copy/move` constructors and `assignment` operators are implicitly deleted



<h2 id="f258b4094c997d13c499fc50cc0138cf"></h2>

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

<h2 id="fbe24973f9df7e0a856ccd9d871c4b90"></h2>

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

<h2 id="d777b421635efebe637ee2f4726d5689"></h2>

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

<h2 id="a22b86e6d7d06811669d602bbb89e7c0"></h2>

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


<h2 id="59427b00f0bc9e475e34732652d9395e"></h2>

## Modern C++: Object Oriented Design (Lecture 7, I. Vizzo, 2020)


<h2 id="adc9ad40993dd6a8ffd8c5ce60244c16"></h2>

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


<h2 id="e40489cd1e7102e35469c937e05c8bba"></h2>

### Inheritance

- Class and struct can inherit data and functions from other classes
- There are 3 types of inheritance in C++:
    - public [used in this course] **GOOGLE-STYLE**
    - protected
    - private
- public inheritance keeps all access specifiers of the base class


<h2 id="37f714fa982009c0f7f34a34222f19c6"></h2>

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

<h2 id="9838b3876aec076af99ebf663cfd7b7a"></h2>

### Function overriding

- A function can be declared virtual: 
    - `virtual Func(<PARAMS>);`
- If function is virtual in `Base` class it can be overridden in `Derived` class:
    - `Func(<PARAMS>) override;`
- `Base` can **force** all `Derived` classes to override a function by making it **pure virtual**
    - `virtual Func(<PARAMS>) = 0;`
    - sometimes, you may not see the keywords `virtual`, but it is still a pure virtual function,  because
        - A member function that overrides a virtual funcction in the base class is automatically virtual even if the virtual keywors is not used


<h2 id="8a88083322dc5c249a3dc33b350ee8b5"></h2>

### Overloading vs overriding

- **Overloading**
    - Pick from all functions with the **same name**, but **different parameters**
    - Pick a function at **compile time**
    - Functions don’t have to be in a class
- **overriding**
    - Pick from functions with the **same arguments and names** in different classes of **one class hierarchy**
    - Pick **at runtime**


<h2 id="4c7393aee7be19ada4689a7b266a1be1"></h2>

### Abstract classes and interfaces

- **Abstract class**: class that has at least one `pure virtual function`
- **Interface**: class that has only `pure virtual functions` and no data members

<h2 id="8fbbb2c24bf977e5ed7f81e2f229bc06"></h2>

### How virtual works

- A class **with virtual functions** has a virtual table
- When calling a function the class checks which of the virtual functions that match the signature should be called
- Called **runtime polymorphism**
- Costs some time but is very convenient

<h2 id="f6f847324f6a271ea8bd9e36a55511bd"></h2>

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


<h2 id="371fedf6ee6747b1de368aafb08094e8"></h2>

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


<h2 id="479c01e471347f335628cee17db0bf54"></h2>

### Type Casting

<h2 id="784be77baa4e7400b3b0e93738c5d66b"></h2>

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

<h2 id="7788e276172dacc2d8d33631b670d026"></h2>

#### static_cast

- `static_cast<NewType>(variable)`
- Convert type of a variable at **compile** time
- **Rarely needed to be used explicitly**
- Can happen implicitly for some types, e.g. float can be cast to int
- Pointer to an object of a Derived class can be **upcast** to a pointer of a Base class
- Enum value can be caster to int or float
- Full specification is complex!


<h2 id="fe9be20b5d842a2d5963b97405c48505"></h2>

#### dynamic_cast

- `dynamic_cast<Base*>(derived_ptr)`
- Used to convert a pointer to a variable of Derived type to a pointer of a Base type
- Conversion happens at runtime
- If derived_ptr cannot be converted to `Base*` returns a `nullptr`
- GOOGLE-STYLE **Avoid** using dynamic casting


<h2 id="dcb294fefdac1da8cef8bcd08d082ebf"></h2>

#### reinterpret_cast

- `reinterpret_cast<NewType>(variable)`
- Reinterpret the bytes of a variable as another type
- We must know what we are doing!
- Mostly used when writing binary data


<h2 id="cee88a63ff1bf6d523474d7541ef35d8"></h2>

#### const_cast

- `const_cast<NewType>(variable)`
- Used to “constify” objects
- Used to “de-constify” objects
- Not widely used


<h2 id="ca5cd6f7f005a605b98372084def1151"></h2>

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


<h2 id="f158d755e5e03f201a3dc6a3afd64932"></h2>

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


<h2 id="bb58d1a88af40f4f934c4dffa00ed22c"></h2>

#### Do not overuse it

- Only use these patterns when you need to
- If your class should have a single method for some functionality and will never need another implementation don’t make it virtual
- Used mostly to avoid copying code and to make classes smaller by moving some functionality out.


<h2 id="685dbb4186ac6d36022cfce886a84a95"></h2>

### Singleton Pattern

- We want only one instance of a given class.
- Without C++ this would be a if/else mess.
- C++ has a powerfull compiler, we can use it.
- We can make sure that nobody creates more than 1 instance of a given class, **at compile time**.
- Don’t over use it, it’s easy to learn, but usually hides a **design** error in your code.
- Sometimes is still necessary, and makes your code better.


<h2 id="a07d5ad4d01026b8866d306c2b5949f1"></h2>

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


<h2 id="7678e529808ac059561fe6aacf2a7978"></h2>

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

<h2 id="6a1ac8cfc4b7407c34517264846ea4b9"></h2>

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


<h2 id="665b944a415c8ddbd9ed36ddbb7f82c9"></h2>

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


<h2 id="8cfd35dc9cd1d651af6f30e4c35cef61"></h2>

## Modern C++: Memory Management (Lecture 8, I. Vizzo, 2020)

- cdtdebug

<h2 id="6c0d5a1fc5c807937c9b607415342ca0"></h2>

### Using pointers for classes

- You actually don't do this. If you do, then there's something else wrong...
    ```c++
    MyClass* obj_ptr = &obj;
    obj_ptr ->MyFunc ();
    ```
- `obj->Func()` ↔ `(*obj).Func()`

<h2 id="4d968934f6b4cb1379ef5be325f5893c"></h2>

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

<h2 id="e88f1fdda31d52dc7548803ec585a30f"></h2>

### this pointer

- Every object of a class or a struct holds a pointer to itself
- This pointer is called `this`
- Allows the objects to:
    - Return a reference to themselves: **return *this;**
    - Create copies of themselves within a function
    - Explicitly show that a member belongs to the current object: `this->x();`
    - `this` is a C++ keyword

<h2 id="6cd14f084543b2c4c8c156f51c0324e0"></h2>

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


<h2 id="83606af2c1b6fdc0c282316a2a0f7c7a"></h2>

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

<h2 id="c44d45c3605314ab2b325d1e136bda78"></h2>

### Heap memory

- **Dynamic** memory (runtime)
- Available for **long** time (program runtime)
- Raw modifications possible with `new` and `delete` (usually encapsulated within a class)
- Allocation is slower than stack allocations

<h2 id="9efb2d5bad0c25e7b0adb30fd0ae501a"></h2>

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


<h2 id="25f56d385df2991bc164c6a6b9cfe858"></h2>

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


<h2 id="c78f80d07a54f3c3d7e38298cc4a1786"></h2>

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

<h2 id="e83d85c788c205ca23e19b8c71e6b39b"></h2>

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

<h2 id="cc4f050d3506116dff9932e4a4757538"></h2>

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

<h2 id="b18489be0d1214fc2a0f7a298e8c52c0"></h2>

### Shallow vs deep copy

- Shallow copy: just copy pointers, not data
- Deep copy: copy data, create new pointers
- Default copy constructor and assignment operator implement **shallow copying**
- RAII + shallow copy → **dangling pointer**
- RAII + **Rule of All Or Nothing** → **correct**
- **Use smart pointers instead!**


<h2 id="458ac9389d0193edc10ce1dfdd38f863"></h2>

### Smart pointers

- Smart pointers wrap a raw pointer into a class and manage its lifetime (**RAII**)
- Smart pointers are **all about ownership**
- Always use smart pointers when the pointer should **own heap memory**
- **Only use them with heap memory!**.
- Still use raw pointers for non-owning pointers and simple address storing
- `#include <memory>` to use smart pointers


<h2 id="86971efe3c54c299f3907707bec8e9ad"></h2>

### C++11 smart pointers types

- **std::unique_ptr**
- **std::shared_ptr**
- std::auto_ptr
- std::weak_ptr
- We will focus on 2 types of smart pointers:
    - `std::unique_ptr` , `std::shared_ptr`


<h2 id="c2aba4da9cb163cfb67728508ee2ac9a"></h2>

### Smart pointers manage memory!

- Smart pointers apart from memory allocation behave exactly as raw pointers(it is still poiner):
    - Can be set to `nullptr`
    - Use `*ptr` to dereference `ptr`
    - Use `ptr->` to access methods
    - Smart pointers are polymorphic
- **Additional functions of smart pointers:**
    - `ptr.get()` returns a raw pointer that the smart pointer manages
    - `ptr.reset(raw_ptr)` stops using currently managed pointer, freeing its memory if needed, sets `ptr` to `raw_ptr`


<h2 id="16f2e352c2cf12dca00e4dc91155f5da"></h2>

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

<h2 id="f33f2c9b7326ad4e484bdbacb864c84b"></h2>

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

<h2 id="8a41b856c1a73927ce95f110f3250ee7"></h2>

#### What makes it “unique”

- Unique pointer **has no copy constructor**
- Cannot be copied, **can be moved**
- Guarantees that memory is always owned by a single `std::unique_ptr`
- A non-null `std::unique_ptr` always owns what it points to.
- Moving a `std::unique_ptr` transfers ownership from the source pointer to the destination pointer. 
    - (The source pointer is set to `nullptr`.)


<h2 id="45a58bbc7dc4952b58ee0a2b32e6b48f"></h2>

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

<h2 id="dc9ef9971bc35a4001eca9017ef469e9"></h2>

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

<h2 id="e0cea2d9b07115ed4382ac3f387083dc"></h2>

### When to use what?

- Use smart pointers when the pointer **must manage memory**
- By default use `unique_ptr`
- If multiple objects must **share ownership** over something, use a `shared_ptr` to it
- Think of any free standing `new` or `delete` as of a memory leak or a dangling pointer:
    - Don’t use `delete`
    - Allocate memory with `make_unique`, `make_shared`
    - Only use `new` in smart pointer constructor if cannot use the functions above


<h2 id="203e97fd9b28daf2c3e09382bac0d780"></h2>

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


<h2 id="767ee4093437fa55b8b907894fa83222"></h2>

## Modern C++ Course: Templates (Lecture 9, I. Vizzo, 2020)

<h2 id="a6b89f6ccba6b648ecd74450ed854270"></h2>

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


<h2 id="c2ec03a8417f8f4202a6a2932ad5e8c3"></h2>

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


<h2 id="388f30d859ac3e81d44254f60c3db2f6"></h2>

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

<h2 id="d44c55af7e30ae17cc73e9567c4cd549"></h2>

#### Template classes usage

```c++
int main() {
    MyClass<int> my_float_object(10);
    MyClass<double> my_double_object(10.0);
    return 0;
}
```

<h2 id="ba2ee1ff0688e49bdc6a7a3588538c0d"></h2>

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

<h2 id="c64518704ce0c0d5501a45763f464276"></h2>

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

<h2 id="2653777f97753f188dcfad2b7743ce47"></h2>

### Template Full/Partial Specialization

TODO


<h2 id="9827d2ec485f02fcd7073d1cd9650f3a"></h2>

### Static code generatrion with constexpr

- `constexpr` specifies that the value of a variable or function can appear in constant expressions

```c++
#include <iostream>
constexpr int factorial(int n) {
    // Compute this at compile time
    return n <= 1 ? 1 : (n * factorial(n - 1));
}

int main() {
    // Guaranteed to be computed at compile time
    return factorial(10);
}
```

- It only works if the variable of function can be defined at **compile-time**:
    ```c++
    #include <array>
    #include <vector>

    int main() {
        std ::vector<int> vec;
        constexpr size_t size_err = vec.size(); // error

        std ::array<int, 10> arr;
        constexpr size_t size = arr.size(); // works!
    }
    ```




