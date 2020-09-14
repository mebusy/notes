...menustart

- [2. 内置类型](#b33f167abcf8b4fea4e2ba5443e349b2)
    - [2.1 数字](#cf71bcea952f7eaa06fcd87a3e27aac0)
        - [int](#fa7153f7ed1cb6c0fcf2ffb2fac21748)
        - [long](#0f5264038205edfb1ac05fbb0e8c5e94)
        - [float](#546ade640b6edfbc8a086ef31347e768)
    - [2.2 字符串](#e126f963213e63b926b5e449aa7d8f47)
        - [编码](#cc6c35a3e0f97fb9747905dc13e9b625)
        - [池化  intern](#e7c52d9da17cbf60fcd6d3a0e94d75bb)
        - [join vs '+'](#4ce061f35d90a97aaad3728502eff07a)
    - [2.3 列表](#007ed57d03ecfc2092e2457f0ca04afe)
        - [bisect](#7a80a08704eb791c461bba64aaf4acdc)
        - [array](#f1f713c9e000f5d3f280adbd124df4f5)
    - [2.4 元组](#235a8cc07f29ed0921fdcc62ff45c56e)
    - [2.5 字典](#bf25b61d72e7938907598910a7bb49f7)
        - [视图 : 判断两个字典间的差异](#b59d513731b6dcc69eebe7f54469b82f)
        - [defaultdict](#867581d324fac535bee50910683df843)
        - [OrderedDict: 元素添加顺序 迭代，操作](#2e84a3dcf01a447292d53bb47859c62f)
    - [2.6 集合](#64a98daa5e9ac47f4663e9fdefcb9169)
        - [判重公式](#2e4bd807b1c6821e16305c1f609403e2)
        - [复合类型里, 只有 tuple、frozenset 是可哈希对象](#b4d60a66fb439c819abc400cad6f2afd)

...menuend


<h2 id="b33f167abcf8b4fea4e2ba5443e349b2"></h2>


# 2. 内置类型

- 空值: None
- 数字: bool, int, long, float, complex
- 序列: str, unicode, list, tuple
- 字典: dict
- 集合: set, frozenset

<h2 id="cf71bcea952f7eaa06fcd87a3e27aac0"></h2>


## 2.1 数字

<h2 id="fa7153f7ed1cb6c0fcf2ffb2fac21748"></h2>


### int 

- 64位平台上，int类型是 64位整数
    - sys.maxint 
    - 是 c语言 long 的扩展
- 整数是虚拟机 特殊照顾对象
    - **small_ints** : 对于小整数，Python使用小整数对象池**small_ints** (固定数组) 缓存了`[-5，257）`之间的整数，该范围内的整数在Python系统中是共享的。
    - **PyIntBlock** : 对于超出了范围的其他整数，Python同样提供了专门的缓冲池，供这些所谓的大整数使用，避免每次使用的时候都要不断的malloc分配内存带来的效率损耗。这块内存空间就是**PyIntBlock**
        - 两个单链表 :  
            - `PyIntBlock *block_list` : 连接 PyIntBlock   
            - `PyIntObject *free_list` : 空闲的 PyIntObject
        - 每个 PyIntBlock , 也通过一个单链表 连接 PyIntObject
        - 按需申请 PyIntBlock 
        - ![](../imgs/python_PyIntBlock.png)
    - PyIntBlock 内存不会返还给操作系统，直至进程结束。
        - PyIntObject对象销毁时，它所占用的内存并不会释放，而是继续被Python使用，进而将free_list表头指向了这个要被销毁的对象上。
    - PyIntBlock 设计上像一个简化的 arena , 但不像 arena 那样有机会释放内存，它会⼀直存在
- summary: 
    - 不管大小 PyIntObject 都存储在 PyIntBlock 中
    - 小整数被全局变量 small_ints 持有，除了直接使用整数下标快速访问外，还导致它们的引用计数永远不可能为 0

```python
>>> a=15
>>> b=15
>>> a is b
True
>>> a=257
>>> b=257
>>> a is b
False
```

- 因 PyIntBlock 内存只复用不释放，同时持有大量整数对象将导致内存暴涨，且不会在这些对象被回收后释放内存，造成事实上的内存泄露
    - 用range 创建一个巨大的数字列表，这就需要足够多的 PyIntBlock 为数字对象提供存储空间
    - xrange 则不会，每次迭代后，数字对象被回收，其占用的内存空闲出来并被复用，内存也就不会暴涨了。


<h2 id="0f5264038205edfb1ac05fbb0e8c5e94"></h2>


### long 

- 当超出 int 限制时， 会自动转换成 long
- 作为变长对象，只要有内存足够， 可以存储无法想象的 天文数字。
- 使用long 的机会不多，Python 也就没有必要专门为其设计优化策略

```python
1 << 3000
1230231....229989376L
```

<h2 id="546ade640b6edfbc8a086ef31347e768"></h2>


### float

```python
typedef struct {
    PyObject_HEAD
    double ob_fval;
} PyFloatObject;
```

- 在内存管理上，float 也采用 PyFloatBlock 模式 , 基本上和 PyIntBlock 相同
    - 但没有特殊的 "小浮点数"
- 使用双精度浮点数 (double)，不能 "精确" 表示某些十进制的小数值
- 尤其是 "四舍五入 (round)" 的 结果，可能和预想不同。

```python
>>> 0.1*3 == 0.3
False
>>> round(2.675, 2)  # 没有4舍5入
2.67
```

- 如果需要，可用 Decimal 代替，它能精确控制运算精度、有效数位和 round 的结果。

```python
>>> from decimal import Decimal, ROUND_UP, ROUND_DOWN
>>> Decimal('0.1') * 3 == Decimal('0.3')
True
>>> Decimal('2.675').quantize(Decimal('.01'), ROUND_UP)
Decimal('2.68')
>>> Decimal('2.675').quantize(Decimal('.01'), ROUND_DOWN)
Decimal('2.67')
```

<h2 id="e126f963213e63b926b5e449aa7d8f47"></h2>


## 2.2 字符串

- 不可变类型，保存字符序列或二进制数据
- 使用 intern 机制 节约内存 , 同时提升效率
    - 短字符串存储在 arena 区域 ( 也做池化？ )
    - 对空字符串和 str、unicode 单字符做了 intern池化 和 永久缓存处理 。 
    - str没有缓存机制(只有池化),unicode 则保留 1024 个宽字符长度 ≤8 的复用对象。    
    - 内部包含 hash 值，str 另有标记用来判断是否被池化 
- 当池化的字符串不再有引用时，将被回收

<h2 id="cc6c35a3e0f97fb9747905dc13e9b625"></h2>


### 编码

- Python 2.x 默认采用 ASCII 编码 

```python
>>> import sys, locale
>>> sys.getdefaultencoding()  
'ascii'
```

- 可以改变编码

```python
reload(sys) # setdefaultencoding 在被初始化时被 site.py 删掉了
sys.setdefaultencoding('utf8') 
```

- str、unicode 都提供了 encode 和 decode 编码转换 法
    - encode: 将默认编码转换为其他编码
    - decode: 将默认或者指定编码字符串转换为 unicode

```python
>>> s = "中国人"; s # ascii编码无法处理汉字 使用utf8
'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'

>>> import sys
>>> reload(sys)
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf8')

>>> s = "中国人"; s
'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba' # 相同

# 注意，没有改变默认编码为utf8, 必须在decode中传入"utf8"
>>> u = s.decode(); u  # utf8->unicode
u'\u4e2d\u56fd\u4eba'

# 默认的ascii 编码下面会报错
>>> gb = s.encode("gb2312"); gb    # UTF-8 -> GB2312
'\xd6\xd0\xb9\xfa\xc8\xcb'

>>> gb.decode("gb2312")  # back to unicode, 必须指定相应的编码
u'\u4e2d\u56fd\u4eba'

>>> gb.decode("gb2312").encode()  # to utf8
'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'

>>> unicode(gb, "gb2312")  # gb2312 -> unicode
u'\u4e2d\u56fd\u4eba'

>>> u.encode()  # unicode -> utf8
'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xba\xba'
```

- 标准库另有 codecs 模块 来处理更复杂的编码转换， 如大小端和 BOM头。
- 另有 string.Template 模板可供使 。string 模块还定义了各种常 的字符序列。

```python
>>> from string import letters, digits, Template
>>> letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> digits
'0123456789'
>>> Template("$name, $age").substitute(name = "User1", age = 20)
'User1, 20'
>>> Template("${name},$age").safe_substitute(name="User1")
'User1,$age'
```

<h2 id="e7c52d9da17cbf60fcd6d3a0e94d75bb"></h2>


### 池化  intern

- 用 intern() 函数可以把运行期动态生成的字符串池化。

```python
>>> s = "".join(["a", "b", "c"])
>>> s is "abc"   # 动态生成的s 没有池化
False
>>> intern(s) is "abc" 
True
>>> s is "abc"
False
>>> intern(s) is intern(s)  # 以后intern 从池中获取字符串对象，就可以复用了
True

>>> a = "abc"*7
>>> b = "abc"*7
>>> a is b
False
>>> a = "abc"*6
>>> b = "abc"*6
>>> a is b
True
```

<h2 id="4ce061f35d90a97aaad3728502eff07a"></h2>


### join vs '+' 

- join 计算总长度后，⼀次性分配存储内存

<h2 id="007ed57d03ecfc2092e2457f0ca04afe"></h2>


## 2.3 列表

- 功能上列表 (list) 类似 Vector，实现上是 数组
    - 列表对象 和 存储元素指针的数组 是分开的两块内存，后者在堆上分配
    - 虚拟机会保留 80 个列表 复用对象，但其元素指针数组会被释放
    - 列表会动态调整指针数组大小，预分配内存多于实际元素数量
- append / pop : O(1)
- insert / remove : O(n)
- list 动态扩容 很影响效率。 解决方案： 预先申请足够大的地方，然后用 set_item 方式赋值，

```python
>>> import timeit
>>> import itertools, gc
>>> gc.disable()
>>> 
>>> def test(n):
...     return len([0 for i in xrange(n)])  # list first, then append
...
>>> def test2(n):
...     return len(list(itertools.repeat(0, n))) # alloc once
...
>>> timeit.timeit("test(10000)", setup="from __main__ import test" , number=1000)
0.32189512252807617
>>> timeit.timeit("test2(10000)", setup="from __main__ import test2" , number=1000)
0.060460805892944336
```

<h2 id="7a80a08704eb791c461bba64aaf4acdc"></h2>


### bisect

<h2 id="f1f713c9e000f5d3f280adbd124df4f5"></h2>


### array

<h2 id="235a8cc07f29ed0921fdcc62ff45c56e"></h2>


## 2.4 元组

- 只读对象，元组和元素指针数组内存是一次性连续分配的
- 虚拟机缓存 n 个元素数量 < 20 的元组复用对象。

<h2 id="bf25b61d72e7938907598910a7bb49f7"></h2>


## 2.5 字典

- 字典 (dict) 采用开放地址法的哈希表实现
    - 自带元素容量为 8 的 smalltable，只有 "超出" 时才到堆上额外分配元素表内存。
    - 虚拟机缓存 80 个字典复用对象，但在堆上分配的元素表内存会被释放
    - 按需动态调整容量。扩容或收缩操作都将重新分配内存，重新哈希。
    - 删除元素操作不会立即收缩内存



<h2 id="b59d513731b6dcc69eebe7f54469b82f"></h2>


### 视图 : 判断两个字典间的差异

```python
>>> d1 = dict(a = 1, b = 2)
>>> d2 = dict(b = 2, c = 3)

>>> v1 = d1.viewitems()
>>> v2 = d2.viewitems()

>>>v1&v2       # insect
set([('b', 2)])

>>>v1|v2   # union
set([('a', 1), ('b', 2), ('c', 3)])

>>>v1-v2   # difference
set([('a', 1)])

>>>v1^v2   
set([('a', 1), ('c', 3)])

>>> ('a', 1) in v1
True

# 不引入新数据项的情况下更新字典内容
# 即  只更新存在的key
>>> a = dict(x=1)
>>> b = dict(x=10, y=20)
>>> a.update({k:b[k] for k in a.viewkeys() & b.viewkeys()}

# 视图会和字典同步变更
# 只是个view， 并不是新对象
>>> d = {"a": 1}
>>> v = d.viewitems()
>>> d["b"] = 2
>>> v
dict_items([('a', 1), ('b', 2)])
```

<h2 id="867581d324fac535bee50910683df843"></h2>


### defaultdict

```python
>>> from collections import defaultdict
>>> d = defaultdict(list)
```

<h2 id="2e84a3dcf01a447292d53bb47859c62f"></h2>


### OrderedDict: 元素添加顺序 迭代，操作

```python
>>> from collections import OrderedDict
>>> od = OrderedDict()
```

<h2 id="64a98daa5e9ac47f4663e9fdefcb9169"></h2>


## 2.6 集合

- 不重复对象: 除了不是同一对象外，还包括 "值" 不能相同
- 集合只能存储可哈希对象， 
- 有只读版本 frozenset
- 集合和字典、列表最大的不同除了元素不重复外，还支持集合运算

<h2 id="2e4bd807b1c6821e16305c1f609403e2"></h2>


### 判重公式

```python
>>> (a is b)  or  (hash(a) == hash(b) and eq(a, b))
```

<h2 id="b4d60a66fb439c819abc400cad6f2afd"></h2>


### 复合类型里, 只有 tuple、frozenset 是可哈希对象

- 如果想把自定义类型放入集合，需要保证 hash 和 equal 的结果都相同才能去重。 

```python
>>> class User(object):
...     def __init__(self, name):
...         self.name = name
...
...     def __hash__(self):
...         return hash(self.name)
...
...     def __eq__(self, o):
...         if not o or not isinstance(o, User): return False
...         return self.name == o.name

```



