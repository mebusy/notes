
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

## 4.1 创建

 - python 函数 可以重载吗？
    - 不能。 因为 在名字空间内， 名字是唯一的主键。 在重载这一点上,函数参数并不能派上什么忙.
 - python  不进行 尾递归优化。最大递归深度 sys.getrecursionlimit()

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
    - 要不然类似 `if condition_variable:   global x ` 语句，就完全无法在编译器确定 x 的作用域了

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

## 4.4 闭包



