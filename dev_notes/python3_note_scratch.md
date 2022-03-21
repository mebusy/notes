# 第2章 类型

## 2.1 基本环境

> Python 的复杂程度要远高出许多人 的设想，诸多概念被隐藏在看似简单的代码背后。



存活实例对象都有“唯一”ID 值

```python
>>> id(1234)
4376051760
```

> 不同 Python 实现使用不同算法，CPython 用内存地址作为 ID 值。因为内存地址会被复用。所以 不保证整个进程生命周期内的唯一。

### 2.1.2 名字

在通常认知里，变量是一段具有特定格式的内存，变量名则是内存别名。

静态编译器或链 接器会以固定地址，或直接、间接寻址指令代替变量名。也就是说变量名不参与执行过 程，可被剔除。

但在解释型动态语言里，名字和对象通常是两个运行期实体。名字不但 有自己的类型，还需分配内存，并介入执行过程。

```python
>>> x=100
1.准备好右值目标对象(100)。
2.准备好名字(x)。
3.在名字空间里为两者建立关联(namespace{x : 100})。
```

名字与目标对象之间也仅是引用关联。名字只负责找人，但对于此人一无所知。鉴于在运行期才能知道名字引用的目标类型，所以说 Python 是一种动态类型语言。

> Names have no type, but objects do.

名字空间

名字空间(namespace)是上下文环境里专门用来存储名字和目标引用关联的容器。

对 Python 而言，每个模块(源码文件)都有一个全局名字空间。而根据代码作用域，又 有当前名字空间或本地名字空间一说。如果直接在模块级别执行，那么当前名字空间和 全局名字空间相同。但在函数內，当前名字空间就专指函数作用域。

> 名字空间默认使用字典(dict)数据结构，由多个键值对(key/value)组成

内置函数 globals 和 locals 分别返回全局名字空间和本地名字空间字典。 globals 总是固定指向模块名字空间，而 locals 则指向当前作用域环境。

我们甚至可直接修改名字空间来建立关联引用。这与传统变量定义方式 有所不同。

```python
>>> globals()["hello"] = "hello, world!"
>>> hello
'hello, world!'
```


> 并非所有时候都能直接操作名字空间。函数执行使用缓存机制，直接修改本地名字空间未必 有效。在正常编码时，应尽可能避免直接修改名字空间。

```python
>>> print(globals())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 100}
```

becareful:

```python
>>> a = str(1)
>>> a
'1'
>>> str = "abcd"
>>>
>>> a = str(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```

赋值操作仅是让名字在名字空间里重新关联，而非修改原对象。


```
# before
x --> 100

# after
x \    100
   \-- "abc"
```

和一个名字只能引用一个对象不同，单个对象可以同时有多个名字

```python
>>> x = 1001
>>> y = x
>>> id(x) == id(y)
True
>>> x is y
True
```

必须使用 is 判断两个名字是否引用同一对象。== 操作符并不能确定两个名字指向同一 对象，

```python
>>> x = 1234
>>> y = 1234
>>> id(x) == id(y)
False
>>> x is y
False
>>> x == y
True
```

以下画线开头的名字，代表特殊含义。

- 模块成员以单下画线开头(_x)，属私有成员，不会被星号导入。
- 类型成员以双下画线开头，但无结尾(__x)，属自动重命名私有成员。 
- 以双下画线开头和结尾(__x__)，通常是系统成员，应避免使用。


### 2.1.3 内存

Python 里没有值类型、引用类型之分。事实上，每个对象都很重。即便是简单的数字， 也有标准对象头，以及保存类型指针和引用计数等信息。

```
x --> cnt:2 | type ptr | ... | 1234
y -->
```

```python
>>> import sys
>>> x = 1234
>>> sys.getsizeof(x)
28
```

> 基于性能考虑，像 Java、Go 这类语言，编译器优先在栈上分配对象内存。但考虑到闭包、接 口、外部引用等因素，原本在栈上分配的对象可能会“逃逸”到堆上。这势必会延长对象生 命周期，加大垃圾回收负担。所以，会有专门的逃逸分析(escape analysis)，用于代码和算 法优化。
> Python 解释器虽然也有执行栈，但不会在栈上为对象分配内存。可以认为所有原生对象(非 C、Cython 等扩展)都在“堆”上分配。


弱引用可用于一些特定场合，比如缓存、监控等。这类“外挂”场景不应该影响目标对 象，不能阻止它们被回收。弱引用的另一个典型应用是实现 Finalizer，也就是在对象被 回收时执行额外的“清理”操作。

```python
>>> import weakref
>>> a=X()
>>> def callback(w): print(w, w() is None)
>>> w = weakref.ref(a, callback)
>>> del a
4384343488 dead.
<weakref at 0x1057f2818; dead> True
# 创建弱引用时设置回调函数
# 回收目标对象时，回调函数被调用
```

> 为什么不使用析构方法(__del__)?
> 很简单，析构方法作为目标成员，其用途是完成对象内部资源清理。它无法感知，也不应该 处理与之无关的外部场景。但在实际开发中，外部关联场景有很多，那么用 Finalizer 才是合 理设计，因为这样只有一个不会侵入的观察员存在。


## 2.2 内置类型

### 2.2.1 整数

Python 3 将原 int、long 两种整数类型合并为 int，采用变长结构。虽然这会导致更多的 内存开销，但胜在简化了语言规则。

> 同样不再支持表示 long 类型的 L 常量后缀。

对于较长数字，为便于阅读，习惯以千分位进行分隔标记。但逗号在 Python 语法中有特 殊含义，故改用下画线表示，且不限分隔位数。

```python
>>> 7,654,321
(7, 654, 321)
>>> 7_654_321
7654321
>>> 765_4321
7654321
```

```python
>>> 0b110_0100    # bin
100
>>> 0144    # oct
  File "<stdin>", line 1
    0144    # oct
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> 0o144    # oct
100
>>> 0x64    # hex
100
```

> 八进制不再支持 012 这样的格式，只能以 0o(或大写)前缀开头。

```python
>>> int("144", 8)
100
>>> int("64", 8)
52
```

小整数

对于常用的小数字，解释器会在初始化时进行预缓存。稍后使用，直接将名字关联到这 些缓存对象即可。如此一来，无须创建实例对象，可提高性能，且节约内存开销。

[-5, 256]

```python
>>> x = -6
>>> y = -6
>>> x is y
False
>>> 
>>> x = 5
>>> y = 5
>>> x is y
True
```

在创建 Decimal 实例时，应该传入一个准确数值，比如整数或字符串等。如果是 float 类 型，那么在构建之前，其精度就已丢失。

```python
>>> Decimal(0.1) 
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal("0.1")
Decimal('0.1')
```

> 除非有明确需求，否则不要用 Decimal 替代 float，要知道其运算速度会慢许多。

```python
>>> ord( "我" )
25105
>>> hex(25105)
'0x6211'
>>> "\u6211"
'我'
```

格式化: f-strings

使用 f 前缀标志，解释器解析大括号内的字段或表达式，在上下文名字空间查找同名对象进
行值替换。

> f-strings 类模板方式更加灵活，其一定程度上将输出样式与数据来源分离。 但其缺点是与上下文名字耦合，导致模板内容与代码必须保持同步修改。而 format 的序号与 主键匹配方式可避开这一点，且支持静态分析工具检查，只可惜它不支持表达式。

内存试图

bytearray  引用字节数据的某个片段， 是否会有数据复制 行为?是否能同步修改? 鉴于 Python 没有指针概念，外加内存安全模型的限制，要做到这一点似乎并不容易。因 此，须借助一种名为内存视图(Memory Views)的方式来访问底层内存数据。

> 内存视图还为我们提供了一种内存管理手段。
> 比如，通过 bytearray 预申请很大的一块内存，随后以视图方式将不同片段交由不同逻辑使用。 因逻辑不能越界访问，故此可实现简易的内存分配器模式。对于 Python 这种限制较多的语言， 合理使用视图可在不使用 ctypes 等复杂扩展的前提下，改善算法性能。
> 可使用 memoryview.cast、struct.unpack 将字节数组转换为目标类型。


视图
与早期版本复制数据并返回列表不同，Python 3 默认以视图关联字典内容。如此一来， 既能避免复制开销，还能同步观察字典变化。

链式字典(ChainMap)以单一接口访问多个字典内容，其自身并不存储数据。读操作按 参数顺序依次查找各字典，但修改操作(新增、更新、删除)仅针对第一字典。

> 可利用链式字典设计多层次上下文(context)结构。
> 合理上下文类型，须具备两个基本特征。首先是继承，所有设置可被调用链的后续函数读取。 其次是修改仅针对当前和后续逻辑，不应向无关的父级传递。如此，链式字典查找次序本身 就是继承体现。而修改操作被限制在当前第一字典中，自然也不会影响父级字典的同名主键 设置。


集合存储非重复对象。所谓非重复，是指除不是同一对象外，值也不能相等。

# 3.表达式

### 3.2.3 作用域 作为隐式规则，赋值操作默认总是针对当前名字空间。

```python
>>> x = 10
>>> def test():
...     print(x) # ok
...     x += 2 # error
...
```

如要对外部变量赋值，须显式声明变量位置。关键字 global 指向全局名字空间， nonlocal 为外层嵌套(enclosing)函数, 自内向外依次检索嵌套函数，但不包括全局名字空间。

> 不同于 global 运行期行为，nonlocal 要求在编译期绑定，所以目标变量须提前存在。

> 作为写操作的赋值，其规则与读操作 LEGB 完全不同，注意区别对待。

```python
>>> cond = True
>>> 1 if cond else 2
1
>>> 1 if not cond else 2
2
>>> cond and 1 or 2
1
>>> not cond and 1 or 2
2
>>> cond and 0 or 1
1
```

> 显然，当 T 和 F 是动态数据时，条件表达式更安全一些。


## 3.4 控制流

和普通循环语句不同，3.x 推导式临时变量不影响上下文名字空间。

> 因为推导式变量在编译器自动生成的函数内使用，而非 test 函数。

```python
def test():
    x = 10
    if x == 10:
        y = [i for i in range(3)]


    print( locals() )

test()
print( locals() )
```


在推导式语法中使用小括号，结果并非创建元组，而是创建生成器(generator)对象。

```python
>>> (x for x in range(3))
<generator object <genexpr> at 0x102109e60>
```

# 第4章 函数

- 函数由两部分组成:
    - 代码对象持有字节码和指令元数据(诸如 源码行、指令操作数，以及参数和变量名等)，负责执行, 为只读模式
    - 函数对象则为上下 文提供调用实例，并管理 运行期 的状态数据。 

```python
import dis
>>> dis.dis( compile( "def test_func( arg1 ): pass", "", "exec" ) )
  1           0 LOAD_CONST               0 (<code object test_func at 0x104154b30, file "", line 1>)
              2 LOAD_CONST               1 ('test_func')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (test_func)
              8 LOAD_CONST               2 (None)
             10 RETURN_VALUE

Disassembly of <code object test_func at 0x104154b30, file "", line 1>:
  1           0 LOAD_CONST               0 (None)
              2 RETURN_VALUE
>>> dis.dis( compile( "def test_func( arg1 ): print(arg1)", "", "exec" ) )
  1           0 LOAD_CONST               0 (<code object test_func at 0x104154870, file "", line 1>)
              2 LOAD_CONST               1 ('test_func')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (test_func)
              8 LOAD_CONST               2 (None)
             10 RETURN_VALUE

Disassembly of <code object test_func at 0x104154870, file "", line 1>:
  1           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (arg1)
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> def test_func( arg1 ): print(arg1)
...
>>> test_func
<function test_func at 0x104617250>
>>> test_func.__code__
<code object test_func at 0x104143940, file "<stdin>", line 1>
>>> test_func.__code__.co_varnames
('arg1',)
```

事实上，def 是运行期指令。以代码对象为参数，创建函数实例，并在当前上下文中与 指定的名字相关联。

伪码

test_func = make_function("test_func", code)


```python
>>> for i in range(3):
...     def test():
...             print("hello")
...     print(id(test), id(test.__code__))
...
4368462128 4363300944
4368462560 4363300944
4368462128 4363300944
```

正因如此，可用 def 以单个代码对象为模板创建多个函数实例。

用列表持有多实例，阻止临时变量 test 被回收，避免因内存复用而出现相同的 id 值。


```python
>>> funcs = []
>>> for i in range(3):
...     def test():
...             print("hello")
...     print(id(test), id(test.__code__))
...     funcs.append( test )
...
4368462560 4363471664  # 不同实例，相同代码
4368461984 4363471664
4368462128 4363471664
```

默认值在函数对象创建时生成，保存在__defaults__，为每次调用所共享。 

如此一来，其行为类似于静态局部变量，会“记住”以往的调用状态。

如默认值为可变类型，且在函数内做了修改，那么后续调用会观察到本次改动，这导致 默认值失去原本的含义。


```python
>>> def test( a = [] ):
...     a.append(1)
...     print(a)
...
>>>
>>> test()
[1]
>>> test()
[1, 1]
```

故建议默认值选用不可变类型，或以 None 表示可忽略。


```python
>>> def test( a = None ):
...     a = a or []
...     a.append(1)
...     print(a)
...
>>> test()
[1]
>>> test()
[1]
```


## 4.4 作用域

在函数内访问变量，会以特定顺序依次查找不同层次的作用域。

LEGB

local > enclosing > global > builtins

> 这与赋值语句默认针对当前名字空间，或用 global、nonlocal 关键字做外部声明完全不同。赋 值操作的目标位置是明确的，即便是 enclosing，也需要在编译时静态绑定。而 LEGB 则在运 行期动态地从多个位置按特定顺序查找。


闭包所引用的环境变量也被称作自由变量，它被保存在函数对象的__closure__属性中。

创建闭包等于“新建函数对象，附加自由变量”。


延迟绑定

闭包只是绑定自由变量，并不会立即计算引用内容。只有当闭包函数执行时，才访问所 引用的目标对象。这样就有所谓的延迟绑定(late binding)现象。

class 不构 成 E/enclosing 作用域。

官方文档将成员统称为 Attribute，不过本书按惯例将数据当作字段。

私有字段  :

如果成员名字以双下画线开头，但没有以双下画线结尾，那么编译器会自动对其重命 名。


getter / setter

多个方法名必须相同。默认从读方法开始定义属性，随后以属性名定义写和删除操作。


```python
@property
def name(self):
    return self.__name

@name.setter
def name(self, value): 
    self.__name = value

@name.deleter # del o.name
def name(self):
    raise AttributeError("can't delete attribute")
```

静态方法 class method

```python
@classmethod
def set(cls, value):
    cls.__data = value
```




