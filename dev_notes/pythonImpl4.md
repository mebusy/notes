...menustart

 - [4. 函数](#8cd7054fb7a85f44fc74a35376860214)
     - [4.1 创建](#1623b5e1ae4a521c5b23729d002020bd)
         - [lambda](#945f3fc449518a73b9f5f32868db466c)
     - [4.2 参数](#8b2b5184e327df133bfd017ad04a3f60)
     - [4.3 作用域](#416013af2072858d19949ec722058389)
     - [4.4 闭包](#e4f33957d3d056b09ebec5b81b966605)
         - [延迟获取](#ec73f536153946064715628cc1da2b34)
     - [4.5 堆栈帧](#2feedbb718e5dfcf31198bd610ef6765)
         - [权限管理](#23bbdd59d0b1d94621fc98e7f533ad9f)
         - [上下文](#50f198f07fc820a4911d1c97a0ceb8c2)

...menuend


<h2 id="8cd7054fb7a85f44fc74a35376860214"></h2>


# 4. 函数

 - 当编译器遇到 def，会生成创建函数对象指令
 - 也就是说 def 是执行指令， 不仅仅是个语法关键字

 - 一个完整的函数对象由函数和代码两部分组成:
    - PyCodeObject 包含了字节码等执行数据
    - PyFunctionObject 为 PyCodeObject 提供了状态信息

 - 函数声明:

```python
def name([arg,... arg = value,... *arg, **kwarg]):
    suite
```

 - 结构定义:

```c
typedef struct {
    PyObject_HEAD
    PyObject *func_code;     // PyCodeObject
    PyObject *func_globals;  // 所在模块的全局名字空间
    PyObject *func_defaults; // 参数默认值列表
    PyObject *func_closure;  // 闭包相关设置
    PyObject *func_doc;      // __doc__
    PyObject *func_name;     // __name__
    PyObject *func_dict;     // __dict__
    PyObject *func_weakreflist; // 弱引用链表
    PyObject *func_module;   // 所在 Module
} PyFunctionObject;
```

 - PyCodeObject 本质上 是⼀种静态源代码, 只不过以字节码方式存储
    - 它面向虚拟机
    - Code 关注的是如何执行这些字节码，比如栈空间大小，各种常量变量符号列表，以及字节码与 源码行号的对应关系等等
 - PyFunctionObject 是运行期产生的
    - 它提供⼀个动态环境，让 PyCodeObject 与运行环境关联起来。
    - 同时为函数调用提供⼀系列的上下文属性，诸如所在模块、全局名字空间、参数默认值等等
    - PyFunctionObject 让函数面向逻辑，而不仅仅是虚拟机。

<h2 id="1623b5e1ae4a521c5b23729d002020bd"></h2>


## 4.1 创建

 - python 函数 可以重载吗？
    - 不能。 因为 在名字空间内， 名字是唯一的主键。 在重载这一点上,函数参数并不能派上什么忙.
 - python  不进行 尾递归优化。最大递归深度 sys.getrecursionlimit()

<h2 id="945f3fc449518a73b9f5f32868db466c"></h2>


### lambda

```python
>>> add = lambda x, y = 0: x + y
```

 - lambda 内使用多条语句？
    - 使用 and / or
    - 你要确保 每个语句都不会返回任何东西

```python
from __future__ import print_function
>>> f = lambda : (print(1) and False) or (print(2) and False) or (print(3) and False)
>>> f()
1
2
3
```

<h2 id="8b2b5184e327df133bfd017ad04a3f60"></h2>


## 4.2 参数

 - 可不关心顺序，用 命名传参数

```python
>>> def test(a, b):
...     print a,b

>>> test(b = "x", a = 100)
100 x
```

 - 支持参数默认值
 - 不过要小心，**默认值对象在创建函数时生成**    
    - 所有调用都使用 同一对象
    - 如果该默认值是 可变类型，那么就如同 c 局部静态变量

```python
>>> def test(x, ints = []):
...     ints.append(x)
...     return ints

>>> test(1)
[1]

>>> test(2)        
[1, 2]

>>> test(1, [])
[1]

>>> test(3)
[1, 2, 3]
```

 - `*args` 收集 "多余" 的位置参数，`**kwargs` 收集 "额外" 的命名参数
 - 可 "展开" 序列类型和字典，将全部元素当做多个实参使用
    - `单个 "*" 展开序列类型，或者仅是字典的主键列表`
    - `"**" 展开字典键值对`

```python
>>> def test(a, b, *args, **kwargs):
...     print a, b
...     print args
...     print kwargs

>>> test(*range(1, 5), **{"x": "Hello", "y": "World"})
1 2
(3, 4)
{'y': 'World', 'x': 'Hello'}
```

<h2 id="416013af2072858d19949ec722058389"></h2>


## 4.3 作用域

 - 函数形参和内部变量都存储在 locals 名字空间中
 - 除非使用 global、nonlocal(python3) 特别声明, 否则在函数内部使 **赋值语句**，总是在 locals 名字空间中 新建一个对象关联。
    - 注意:"赋值" 是指名字指向新的对象，而非通过名字改变对象状态

 - 如果仅仅是引用外部变量，那么按 LEGB 顺序在不同作用域查找该名字
    - 名字查找顺序: locals -> enclosing function -> globals -> __builtins__
 - 如果将对象引入 __builtins__ 名字空间，那么就可以在任何模块中直接访问, 如同内置函数一样
    - 不过 这并不是一个好主意

```
27.3. __builtin__ — Built-in objects
CPython implementation detail: Most modules have the name __builtins__ (note the 's') made available as part of their globals. The value of __builtins__ is normally either this module or the value of this modules’s __dict__ attribute. Since this is an implementation detail, it may not be used by alternate implementations of Python.
```

 - 需要注意，名字作用域是在 **编译时** 确定的

```
>>> def test():
...     locals()["x"] = 10
...     print x
>>> test()
NameError: global name 'x' is not defined
```

 - 要解决这个问题，可动态访问名字，或使用 exec 语句，解释器会做动态化处理

```python
>>> def test():
...     exec ""        #空语句。
...     locals()["x"] = 10
...     print x

>>> test() 
10
```

 - 实际运行时， 解释器会将 locals 名字复制到 FAST 区域来优化访问速度
    - 因此直接修改 locals 名字空间并不会 影响该区域 ，及 运行结果
    - 解决办法还是 exec

```python
>>> def test():
...     x=10 
...
...     locals()["x"] = 100  # 该操作不会影响 FAST 区域，只不过指向一个新对象
...     print x    # 使用 LOAD_FAST 访问 FAST 区域名字，依然是原对象
...
...     exec "x = 100"   # 同时刷新 locals 和 FAST
...     print x

>>> test()
10
100
```

 - 另外，编译期作用域不受执行期条件影响。
    - 要不然类似 `if condition_variable:   global x ` 语句，就完全无法在编译期间确定 x 的作用域了

```python
>>> x = 10
>>> def test():
...     if False:
...         global x    # 尽管此语句永不执 ，但编译器依然会将 x 当做 globals 名字。
...     x=10
...     print globals()["x"] is x  
...
>>> test()
True

>>> def test():
...     if False:
...         x = 10  # 同理，x 是 locals 名字。后面出错也就很正常了
...     print x
...
>>> test()
UnboundLocalError: local variable 'x' referenced before assignment
```

<h2 id="e4f33957d3d056b09ebec5b81b966605"></h2>


## 4.4 闭包

 - 闭包是指:当函数离开创建环境后，依然持有其上下文状态

```python
>>> def test():
...     x=[1,2]
...     print hex(id(x))
...
...     def a():
...         x.append(3)
...         print hex(id(x))
...
...     def b():
...         print hex(id(x)), x
...
...     return a, b

>>> a, b = test()
0x109b925a8
>>> a()
0x109b925a8
>>> b()
0x109b925a8 [1, 2, 3]
```

 - test 在创建 a 和 b 时，将它们所引用的外部对象 x 添加到 func_closure 列表中。
 - 因为 **x的引用计数增加了**, 所以就算 test 堆栈帧没有了，x 对象也不会被回收。

```python
>>> a.func_closure
(<cell at 0x109e0aef8: list object at 0x109b925a8>,)
>>> b.func_closure
(<cell at 0x109e0aef8: list object at 0x109b925a8>,)
>>> a.func_closure[0].cell_contents
[1, 2]
```

```python
>>> def test(x):
...     def a():
...         print x
...     print hex(id(a))
...     return a

>>> a1 = test(100)
0x102f4dc08
>>> a2 = test(100)
0x102f4d578
>>> a3 = test("hi") # 每次返回的函数对象并不相同
0x102f5c578
>>> a1()   # a1 的对象状态并没有被 a2 破坏
100

>>> a1.func_closure
(<cell at 0x102f5f7f8: int object at 0x7fe723d03940>,)
>>> a2.func_closure   # 持有的闭包列表是不同的
(<cell at 0x102f5f830: int object at 0x7fe723d03940>,)
>>> a3.func_closure
(<cell at 0x102f5f910: str object at 0x102f025f8>,)

>>> a1.func_code is a3.func_code  # 这个很好理解, 字节码没必要有多个
True
```

 - 通过 func_code, 可以获知闭包所引用的外部名字
 - 编译器在生成 PyCodeObject test 时就已经确定了被内层函数引用的变量，并将它们的名字保存在 co_cellvars 字段里
    - co_cellvars: 被内部函数引用的名字列表
    - co_freevars: 当前函数引用外部的名字列表

```python
>>> test.func_code.co_cellvars  # test被内部函数a 引用的名字
('x',)
>>> a.func_code.co_freevars     # a 引用外部函数 test中的名字
('x',)
```

<h2 id="ec73f536153946064715628cc1da2b34"></h2>


### 延迟获取

 - 使用闭包，还需注意 "延迟获取" 现象

```python
>>> def test():
...     for i in xrange(3):
...         def a():
...             print i
...         yield a
... 
>>> a,b,c = test()
>>> >>> id(a),id(b)
(4344564744, 4344628720)
>>> a(), b(), c()
2
2
2
```

<h2 id="2feedbb718e5dfcf31198bd610ef6765"></h2>


## 4.5 堆栈帧

 - Python 堆栈帧基本上就是对 x86 的模拟, 用指针对应 BP、SP、IP 寄存器。
 - 堆栈帧成员包括函数执行所需的 名字空间、调用堆栈链表、异常状态等。

```python
typedef struct _frame {
    PyObject_VAR_HEAD
    struct _frame *f_back;  // 调用堆栈 call stack 链表
    PyCodeObject *f_code;   // PyCodeObject
    PyObject *f_builtins;   // builtins 名字空间
    PyObject *f_globals;        
    PyObject *f_locals;    
    PyObject **f_valuestack;  // 相当于 BP 基址寄存器BP
    PyObject **f_stacktop;    // 运行栈顶，相当于 SP 堆栈寄存器
    PyObject *f_trace;      // Trace function
    // 记录当前栈帧的异常信息
    PyObject *f_exc_type, *f_exc_value, *f_exc_traceback;
    PyThreadState *f_tstate;    // 所在线程状态
    ...
    PyObject *f_localsplus[1];   // 动态申请的一段内存， 用来模拟 x86 堆栈帧所在内存段
} PyFrameObject;
```

 - 可使  `sys._getframe(0)` 或 `inspect.currentframe()` 获取当前堆栈帧。
 - 除用于调试外，还可利用堆栈帧做些有意思的事情。

<h2 id="23bbdd59d0b1d94621fc98e7f533ad9f"></h2>


### 权限管理

 - 检查函数 Caller，以实现权限管理

```python
>>> import sys
>>> def save():
...     f = sys._getframe(1)
...     if not f.f_code.co_name.endswith("_logic"):
...         raise Exception("Error!")
...     print "ok"
... 
>>> def test(): save()
... 
>>> def test_logic(): save()
... 
>>> test()
Exception: Error!
>>> test_logic()
ok
```

<h2 id="50f198f07fc820a4911d1c97a0ceb8c2"></h2>


### 上下文

 - 通过call stack , 我们可以隐式向整个执行流程传递上下文对象
 - `inspect.stack` 比  `frame.f_back` 更方便一些。

```python
>>> import inspect
>>> def get_context():
...     for f in inspect.stack(): 
...         context = f[0].f_locals.get("context")
...         if context: return context   
... 
>>> def controller():
...     context = "ContextObject" 
...     model()
... 
>>> def model():
...     print get_context()  
... 
>>> controller() 
ContextObject
```

 - `sys._current_frames` 返回所有线程的当前堆栈帧对象
 - 虚拟机会缓存 200 个堆栈帧复用对象，以获得更好的执行性能





