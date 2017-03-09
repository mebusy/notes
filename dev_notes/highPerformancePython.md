

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

## 4 Dictionaries and Sets 




