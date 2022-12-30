
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








