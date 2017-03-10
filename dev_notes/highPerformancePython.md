

# 2 profile

## Cpu profile

### use timeit

```bash
python -m timeit -n 5 -r 5 -s "import julia1" "julia1.calc_pure_python(False, desired_width=1000, max_iterations=300)"
```

 - n 5  -- loop 5 times , default 10
 - r 5  -- repeat 5 times , default 5

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


### use line_profile 

line_profiler is the strongest tool for identifying the cause of CPU-bound problems in Python code. 

It works by profiling individual func‐ tions on a line-by-line basis, so you should start with cProfile and use the high-level view to guide which functions to profile with line_profiler.

 - `pip install line_profiler`
 - 在需要profile 的函数上， 加上 @profile   修饰
 - `python /Library/Python/2.7/site-packages/kernprof.py  -lv diffusion_python.py`
    - -l for line-by-line (rather than function-level) profiling
    - -v for verbose output. Without -v you receive an .lprof output that you can later analyze with the line_profiler module.


## Memory profile 

 - install 
	- 'pip install memory_profiler'
	- already shipped in mac ?
 

# 3 List and Tuple 

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

## 6 Matrix and Vector Computation


### problem with  Allocating Too Much

 - memory allocations are not cheap, must take its time to talk to the operating system in order to allocate the new space.
 - reuse it if possible
 
### Memory Fragmentation
 
 - doing `grid[5][2]` requires us to first do a list lookup for index 5 on the list grid. This will return a pointer to where the data at that location is stored. Then we need to do another list lookup on this returned object, for the element at index 2.
    - The overhead for one such lookup is not big and can be, in most cases, disregarded.
 - However, if the data we wanted was located in one contiguous block in memory, we could move all of the data in one operation instead of needing two operations for each element. 
 - This is one of the major points with data fragmentation:
    - when your data is fragmented, you must move each piece over individually instead of moving the entire block over. 
    - This means you are invoking more memory transfer overhead, and you are forcing the CPU to wait while data is being transferred. 
 - The CPU does a good job with mechanisms called branch prediction and pipelining, which try to predict the next instruction and load the relevant portions of memory into the cache while still working on the current instruction. 
 - However, the best way to minimize the effects of the bottle‐ neck is to be smart about how we allocate our memory and how we do our calculations over our data.

  
### Enter numpy

numpy stores data in contiguous chunks of memory and supports vectorized operations on its data. 

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

### Making most numpy operations in-place

```python
def evolve(grid, dt, out, D=1): 
	laplacian(grid, out) 
	out*=D*dt
	out += grid
```

# 8 Concurrency   page 200

# 9 The multiprocessing Module

# 





