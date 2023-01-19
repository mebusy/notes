[](...menustart)

- [Google Test](#d0787974e29f9f2120fed0d80f8ecd94)
    - [1. install](#14a76e12a26eab33b33df71bcc17d1ca)
    - [1.1  Or you may want to install from source ...](#887153ee6928ae477839b766df75177f)
    - [2. includes & libs](#b58307117bb118487b3241ced67bafed)
    - [2.1 includes & libs from source](#69953f7b34141e940324a5d01de0c9e7)
    - [3. most simple program](#7bb7dc3d1076c5f58804cdfa18add655)
    - [4. add a demo test](#ce41ea2d19a4d3a700aed0cd2aae6667)
    - [5. Assertions](#755be3c257d480a497a4fba1da95db48)

[](...menuend)


<h2 id="d0787974e29f9f2120fed0d80f8ecd94"></h2>

# Google Test

https://github.com/google/googletest


<h2 id="14a76e12a26eab33b33df71bcc17d1ca"></h2>

## 1. install

brew install googletest


<h2 id="887153ee6928ae477839b766df75177f"></h2>

## 1.1  Or you may want to install from source ...

<details>
<summary>
build from source
</summary>


- first, do some modification...
    - CMakeList.txt, line:127, add quotes around the $(GOOGLETEST_VERSION} variable.
    ```cmake
    set_target_properties(gtest PROPERTIES VERSION "${GOOGLETEST_VERSION}")
    cxx_library(gtest_main "${cxx_strict}" src/gtest_main.cc)
    set_target_properties(gtest_main PROPERTIES VERSION "${GOOGLETEST_VERSION}")
    ```

- build
    ```bash
    cd googletest
    mkdir build
    cd build
    cmake ..
    make
    ```

</details>

<h2 id="b58307117bb118487b3241ced67bafed"></h2>

## 2. includes & libs

```bash
$ brew --prefix googletest
/usr/local/opt/googletest
```

- include
    - `/usr/local/opt/googletest/include/gtest`
- lib
    - `/usr/local/opt/googletest/lib/`


<h2 id="69953f7b34141e940324a5d01de0c9e7"></h2>

## 2.1 includes & libs from source


<details>
<summary>
include / lib from source
</summary>



- include 
    - `build/../include/gtest/`
- lib
    - `build/lib/`


copy to /usr/local/

```bash
cp -a ../include/gtest /usr/local/include

mkdir /usr/local/lib/gtest
cp -a lib/*.a /usr/local/lib/gtest
```

to check 

```bash
ls /usr/local/include/gtest/
gtest-assertion-result.h gtest-message.h...

ls /usr/local/lib/gtest
libgtest.a      libgtest_main.a
```

</details>



<h2 id="7bb7dc3d1076c5f58804cdfa18add655"></h2>

## 3. most simple program

```c++
#include <gtest/gtest.h>

int main(int argc, char **argv) {

    testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}
```

```bash
$ c++ -std=c++17  -lgtest -lgtest_main  ./*.cpp && ./a.out

[==========] Running 0 tests from 0 test suites.
[==========] 0 tests from 0 test suites ran. (0 ms total)
[  PASSED  ] 0 tests.
```


<h2 id="ce41ea2d19a4d3a700aed0cd2aae6667"></h2>

## 4. add a demo test

```c++
TEST(TestName, Subtest_1) { 
    ASSERT_TRUE(1 == 1); 
}

int main(...)
```

```bash
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from TestName
[ RUN      ] TestName.Subtest_1
[       OK ] TestName.Subtest_1 (0 ms)
[----------] 1 test from TestName (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (0 ms total)
[  PASSED  ] 1 test.
```

<h2 id="755be3c257d480a497a4fba1da95db48"></h2>

## 5. Assertions

- Success
- Non-Fatal-Failure
    - `EXPECT_EQ()`
    - `EXPECT_NE()`
    - `EXPECT_LT()`
    - `EXPECT_LE()`
    - ...
- Fatal-Failure
    - `ASSERT_EQ()`
    - ...




