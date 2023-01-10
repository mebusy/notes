
# Google Test

https://github.com/google/googletest


## 1. install

brew install googletest


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

## 2. includes & libs

```bash
$ brew --prefix googletest
/usr/local/opt/googletest
```

- include
    - `/usr/local/opt/googletest/include/gtest`
- lib
    - `/usr/local/opt/googletest/lib/`


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




