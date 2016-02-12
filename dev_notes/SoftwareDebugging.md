# Software Debugging

## 1. How Debuggers work

assert

**assert 可以被 try-catc 捕捉**

### Explicit Debugging

笔记调试法，把你做的记下来，

### Problem set 1

```python
sys.settrace(traceit) 

def traceit(frame, event, trace_arg):
    ...
```

traceit函数框架参数:

 1. frame
    - python有frameobject，保存有代码信息。常用成员变量:
        - frame.f_lineno 行号, 从1开始
        - frame.f_code.co_name 执行到的函数名. 
        - f_code是code object
        - frame.f_locals 局部变量 dict
 2. event 事件
    - 调试中主要使用line
 3. arg 其他参数


traceit 会在程序每一行之行后，被调用。traceit 函数返回自身，才能继续下一行的执行。


### repr 

```
repr(obj) 
obj.__repr__()
```

## 2. Assertion

assertion 是自动化测试的关键。

```python
assert condition
```

### assertion 在测试中的作用:

```python
def test_square_root():
    assert square_root(4)==2
    assert square_root(9)==3
    # and so on
```

对于没有assert 方法的语言，你完全可以自己定义一个assert 方法。

### Built-in assert

 - indentification 告诉你是哪个断言失败
 - location 代码位置
 - optional 打开/关闭
 - standardize 
 

### assertion 在代码中的作用:

```python
def square_root( x ):
    assert x > =  # precondition
    ...
    assert y*y==x  # postcondition
    return y
```

precondition 的设置,可以迅速的判断出出错的上游。


### assertion can be turned off

 - python -O turn assertion **off**
 - c/c++ -DNDEBUG turn assertion **off**
 - jave -ea turn assertion **on**

**因为assertion是可以关闭的**, 所以一定要确保 完全去掉assertion语句不会影响到逻辑。

 - 错误写法: 
    - assert map.remove(location)==True
 - 正确写法：
    - localRemoved = map.remove(location)
    - assert localRemoved

### assertion should NOT check public preconditions

deposit = int(input)

~~assert deposit>=0~~

if deposit <0:
    raise IllegalDataException


一些会引发严重的后果的情形，比如宇宙飞船的控制程序，红绿灯控制系统，不应该使用assertion ，而应该 raise Exception, 因为 assertion 有可能会被关闭。


### Should assertion remain enable in product code? 

支持观点:

 - failing is better than bad data
 - Eases debugging
 - defect in the field are hard to debug
 
反对观点:

 - Performance
 - Not User Friendly


### System Invariants

对于全局变量, 可以在 traceit 方法中监听变量值。

eg. 很多模块都会修改全局变量 flag

```python
def traceit( ... ):
    global flag
    assert not flag
    return traceit
```

### Buffer Overflow

c/c++ 程序中，如何防止 访问未分配内存的区域?

 - electric fense , x86
 - Valgrind , x86



### Inferring Invariants 推断不变
  
加断言可以从数据不变量开始。 

不变量可以理解为 数据的某些不变的特征，比如 x 只可能是奇数，等等。

Define variants , precondition, postcondition 不是一件简单的事情，好在很多工具可以帮我们做这些。

工具 Daikon can dynamically detect invariants. 想法就是, 你要很多次地运行程序。


### Problem set 2

跟踪square_root 的执行，自动输出 precondition 和 postcondition语句。

依然是使用 sys.settrace(trace_it) 方法。

```python
def trace_it( frame, event, arg )
```

 - event
    - "call" 
    - "return" 
 - frame
    - frame.f_code.co_name 就是正在运行的函数名
    - frame.f_locals  所有的局部变量
 - arg
    - 如果 event是 "return", 传到arg里的就是返回值

跟踪 call square_root 和 return square_root , 以分析获得 precondition 和 postcondition.

eg.

```python
square_root(2)
square_root(4)
square_root(16)
```

==>

```python
call square_root():
    assert 2<=x<=16
    assert eps==10e-7
    
return sqaure_root():
    assert 1.42<=y<=4.0
    assert 1.42<=ret<=4.0
```

## 3. Simplifying Failures

找出与失败相关的因素，排出不相关因素。

###  Automated Simplification

手工简化乏味枯燥。

To Automated Simplification , we need:

 - a strategy that does the simplification for us
    - basically it tell us how to simplify 
 - an automated test
    - check whether our simplification succeeded of not 

### Delta Debugging

Delta debuggin returns a failure case.

[2分自动查错 ddmin](https://raw.githubusercontent.com/mebusy/codeLib/master/SofewareDebugging/unit3_ddmin.py)

## 4. Tracking Origins

### Automate Deduction

trace_it 跟踪 successful run 和 fail run, 比较各个变量值的不同，以此来自动检测出错变量的最小集合。

## 5. Reproducing Failures

Record the funcion call rather than recording the GUI operations.

使用 trace_it 方法 记录下 "call" event 的函数名和参数，使用 eval 方法来 reproduce.

```
"remove_html_markup(s = '<b>foo</b>')"
"square_root(x = 2)"
```

[evaluate_calls ](https://raw.githubusercontent.com/mebusy/codeLib/master/SofewareDebugging/unit5_eval_calls.py)

### Other Facets

 1. Time
    - if your program depends on real dates and times,  be sure to provide a means to set these, for diagnostic purposes
 2. Randomness
    - save random seed for pseudorandom generator
    - save sequence of random numbers for true random generator
 3. Schedule
    - Multithread program , find means to make these thread switches deterministic
 4. Physical influence
    -  
 5. Debugging Tools
    - Debugger instruments the code and alter its execution.  The least they do is to influence the real timing.

### Capturing Coverage

使用 trace_it 方法记录下行数, 保存到一个 set 中, 统计测试覆盖率。

**Application**:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/SoftwareDebugging_unit5_captureCoverage.png)

We can find that "quote=not quote" only executed in the failing runs. So all we need in **this situation** is to look at this condition.

Unfortunately , things are not always that easy.

If the input is `<"">` , "quote=not quote" is also executed , and the run is successfully.

So we can say the execution of this line,  "quote=not quote" , directly is related to passing or failing.

What we want to look for are lines that statistically correlate with failure. That is , they may occasionly pass , but more frequently fail than pass.

### Phi Coefficient

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/SoftwareDebugging_unit5_correlation.png)

In this table you count how frequently a line was covered in failling runs, as well as in passing runs.

And of course you also count how frequently it was not covered in failing / passing runs.

This is the **Phi Coefficient**.

∅ 越大, correlation 越强.

 1. compute ∅ for each line
 2. rank lines from high ∅ to low ∅
 
## 6. Learning from Mistakes


## 7. Overview

 - Track the problem
 - Reproduce it
 - Automate + Simplify
 - Find possible infection origins
 - Foucs on most likely origins
 - Isolate the infection chains
 - Correct the defect
 
