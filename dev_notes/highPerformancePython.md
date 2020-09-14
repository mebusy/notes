...menustart

- [2 profile](#d105e42e2a2538a926e25076acc61be3)
    - [Cpu profile](#11e4ad9c685f7ebda02bf471870b42ec)
        - [use timeit](#3acd262af042ae4143c1e2e86b55ad52)
        - [use unix time command](#324369ebf4aa30c14eae18ba1231bcd9)
        - [use cprofile](#36a6ae8bfb5442419d701bb4af008274)
        - [use line_profile](#d7dd7fb89c8a9ffea55f74bc3a6018be)
    - [Memory profile](#ec8e55e3ee8a8f8049bf7d540a3679ec)
- [3 List and Tuple](#3a5f793d765efeae35bf8449952f7d01)
    - [binary search](#9c810920649050b97ee2f736d74355e9)
    - [6 Matrix and Vector Computation](#789315c7d328e462184bae7f5269422f)
        - [problem with  Allocating Too Much](#7c19d1264b48dbaef6f19b626ed16c2c)
        - [Memory Fragmentation](#5775736264cc198fd819593e551b8403)
        - [Enter numpy](#8670a80dcf372e8b7ad9cf6eb3168809)
        - [Memory Allocations and In-Place Operations](#228c682c9eb16b3494c7b3a67132cb7d)
        - [Making most numpy operations in-place](#56f456dc0e224555f1be6f250d7ce29a)
- [8 Concurrency   page 200](#851bb2aeae97198e18a9d391be7bbb1e)
- [9 The multiprocessing Module](#9ca43b7228989d90337fe842ce8ae131)
- [](#d41d8cd98f00b204e9800998ecf8427e)

...menuend


<h2 id="d105e42e2a2538a926e25076acc61be3"></h2>


# 2 profile

<h2 id="11e4ad9c685f7ebda02bf471870b42ec"></h2>


## Cpu profile

<h2 id="3acd262af042ae4143c1e2e86b55ad52"></h2>


### use timeit

```bash
python -m timeit -n 5 -r 5 -s "import julia1" "julia1.calc_pure_python(False, desired_width=1000, max_iterations=300)"
```

 - n 5  -- loop 5 times , default 10
 - r 5  -- repeat 5 times , default 5

<h2 id="324369ebf4aa30c14eae18ba1231bcd9"></h2>


### use unix time command

```bash
time -p python julia1_nopil.py

real 9.84
user 9.64
sys 0.11
```

 - real records the wall clock or elapsed time.
 - user records the amount of time the CPU spent on your task outside of kernel functions.
 - sys records the time spent in kernel-level functions.

By adding user and sys, you get a sense of how much time was spent in the CPU. The difference between this and real might tell you about the amount of time spent waiting for I/O; it might also suggest that your system is busy running other tasks that are distorting your measurements.

<h2 id="36a6ae8bfb5442419d701bb4af008274"></h2>


### use cprofile 

```bash
python -m cProfile -s cumulative julia1_nopil.py

         36221992 function calls in 14.959 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.033    0.033   14.959   14.959 julia1_nopil.py:1(<module>)
        1    0.745    0.745   14.926   14.926 julia1_nopil.py:23(calc_pure_python)
        1   11.452   11.452   14.044   14.044 julia1_nopil.py:9(calculate_z_serial_purepython)
 34219980    2.572    0.000    2.572    0.000 {abs}
  2002000    0.129    0.000    0.129    0.000 {method 'append' of 'list' objects}
        1    0.020    0.020    0.020    0.020 {range}
        1    0.007    0.007    0.007    0.007 {sum}
        4    0.000    0.000    0.000    0.000 {len}
        2    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

 - -s cumulative flag tells cProfile to sort by cumulative time spent inside each function;
    - this gives us a view into the slowest parts of a section of code


<h2 id="d7dd7fb89c8a9ffea55f74bc3a6018be"></h2>


### use line_profile 

line_profiler is the strongest tool for identifying the cause of CPU-bound problems in Python code. 

It works by profiling individual func‐ tions on a line-by-line basis, so you should start with cProfile and use the high-level view to guide which functions to profile with line_profiler.

 - `pip install line_profiler`
 - 在需要profile 的函数上， 加上 @profile   修饰
 - `python /Library/Python/2.7/site-packages/kernprof.py  -lv diffusion_python.py`
    - -l for line-by-line (rather than function-level) profiling
    - -v for verbose output. Without -v you receive an .lprof output that you can later analyze with the line_profiler module.


<h2 id="ec8e55e3ee8a8f8049bf7d540a3679ec"></h2>


## Memory profile 

 - install 
    - 'pip install memory_profiler'
    - already shipped in mac ?
 

<h2 id="3a5f793d765efeae35bf8449952f7d01"></h2>


# 3 List and Tuple 

<h2 id="9c810920649050b97ee2f736d74355e9"></h2>


## binary search

```python
def binary_search(needle, haystack):                                              
    # imin and imax store the bounds of the haystack that we are currently
    # considering.  This starts as the bounds of the haystack and slowly
    # converges to surround the needle.
    imin, imax = 0, len(haystack)
    while True:
        if imin >= imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint
```

 - 使用 bisect 可以更简单的实现 2分查找

<h2 id="789315c7d328e462184bae7f5269422f"></h2>


## 6 Matrix and Vector Computation


<h2 id="7c19d1264b48dbaef6f19b626ed16c2c"></h2>


### problem with  Allocating Too Much

 - memory allocations are not cheap, must take its time to talk to the operating system in order to allocate the new space.
 - reuse it if possible
 
<h2 id="5775736264cc198fd819593e551b8403"></h2>


### Memory Fragmentation
 
 - doing `grid[5][2]` requires us to first do a list lookup for index 5 on the list grid. This will return a pointer to where the data at that location is stored. Then we need to do another list lookup on this returned object, for the element at index 2.
    - The overhead for one such lookup is not big and can be, in most cases, disregarded.
 - However, if the data we wanted was located in one contiguous block in memory, we could move all of the data in one operation instead of needing two operations for each element. 
 - This is one of the major points with data fragmentation:
    - when your data is fragmented, you must move each piece over individually instead of moving the entire block over. 
    - This means you are invoking more memory transfer overhead, and you are forcing the CPU to wait while data is being transferred. 
 - The CPU does a good job with mechanisms called branch prediction and pipelining, which try to predict the next instruction and load the relevant portions of memory into the cache while still working on the current instruction. 
 - However, the best way to minimize the effects of the bottle‐ neck is to be smart about how we allocate our memory and how we do our calculations over our data.

  
<h2 id="8670a80dcf372e8b7ad9cf6eb3168809"></h2>


### Enter numpy

numpy stores data in contiguous chunks of memory and supports vectorized operations on its data. 

<h2 id="228c682c9eb16b3494c7b3a67132cb7d"></h2>


### Memory Allocations and In-Place Operations

> In-place operations reducing memory allocations

```bash
>>> import numpy as np
>>> array1 = np.random.random((10,10)) 
>>> array2 = np.random.random((10,10)) 
>>> id(array1)
140199765947424 # 1
>>> array1 += array2
>>> id(array1)
140199765947424 # 2
>>> array1 = array1 + array2
>>> id(array1)
140199765969792 # 3
```

<h2 id="56f456dc0e224555f1be6f250d7ce29a"></h2>


### Making most numpy operations in-place

```python
def evolve(grid, dt, out, D=1): 
    laplacian(grid, out) 
    out*=D*dt
    out += grid
```

<h2 id="851bb2aeae97198e18a9d391be7bbb1e"></h2>


# 8 Concurrency   page 200

<h2 id="9ca43b7228989d90337fe842ce8ae131"></h2>


# 9 The multiprocessing Module

<h2 id="d41d8cd98f00b204e9800998ecf8427e"></h2>


# 





