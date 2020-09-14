...menustart

- [3. 表达式](#680c8f0fc92b0567222e133e40862ee0)
    - [3.2 命名规范](#10bc14b9093cc6c13287e1716eae2314)
    - [3.3 赋值](#ee3f6f66dd85c01d0cc7a47853768819)
    - [3.4 表达式](#012bcc3676254ba476bef97e1d28c099)
        - [while](#901889f4f34f8ca18ac2f53d1fed346e)
        - [del](#d2bcc286168bf8e040885c5cb7b6df13)
        - [Generator](#92a8f0b9d28a89b480bd1d29f46f0484)
        - [Slice](#d140d37ad98c12ccd8e1c432f548bcdb)
        - [相等 , 操作符 "==" 可被重载](#1596d63c8ed6ef83ea2fee5f847baca9)

...menuend


<h2 id="680c8f0fc92b0567222e133e40862ee0"></h2>


# 3. 表达式

 - 如果你喜欢 lua的end ...

```python
>>> # 自定义 end 伪关键字
>>> __builtins__ 名字空间，可以在任何模块中访问
>>> __builtins__.end = None
>>> def test(x):
>>>     pass
>>> end
```

<h2 id="10bc14b9093cc6c13287e1716eae2314"></h2>


## 3.2 命名规范

 - 模块中以 `_` 开头的名字视为私有
    - `from xxx import *` 不会导入这些 变量和函数
    - 但是仍然可以这样访问它们  `import xxx;  xxx._yyy`
 - 以 `__` 开头的类成员名字视为私有
    - Name Mangling
    - 如果有一 Test 类里有一成员 `__x`，那么 dir(Test) 时会看到 `_Test__x` 而非 `__x`
 - 同时以`__` 开头和结尾的名字，通常是特殊成员
 - 单一 `_` 代表最后表达式的返回值

```python
>>> s = set("abc")
>>> s.pop()
'a'
>>> _
'a'
```

<h2 id="ee3f6f66dd85c01d0cc7a47853768819"></h2>


## 3.3 赋值

 - 除非在函数中使用关键字 global、nolocal 指明外部名字 ， 否则赋值语句总是 **在当前名字空间创建或修改 {name:object} 关联**
 - 代码 block 不是 名字空间 ！！！ 这点和c不同

```python
>>> def test():
... while True:
...     x = 10
...     break
... print locals()
... print x # 这个写法c里会报错 

>>> test()
{'x': 10}
10
```

 - 支持用序列类型或迭代器对多个名字同时赋值

```python
>>> a, b, _ = xrange(3)

# Python 3 对此提供了更好的支持。
>>> a, *b, c = "a1234c"
>>> a, b, c
('a', ['1', '2', '3', '4'], 'c')
```

<h2 id="012bcc3676254ba476bef97e1d28c099"></h2>


## 3.4 表达式

<h2 id="901889f4f34f8ca18ac2f53d1fed346e"></h2>


### while

 - else 分支
 - 可以用 else 分支标记循环逻辑被完整处理

```python
>>> while x > 0:
...     x -= 1
... else:
...     print "over!"

```

<h2 id="d2bcc286168bf8e040885c5cb7b6df13"></h2>


### del

 - 可删除名字、序列元素、字典键值，以及类对象成员

<h2 id="92a8f0b9d28a89b480bd1d29f46f0484"></h2>


### Generator

 - 用一种优雅的方式创建列表、字典或集合

```python
>>> [x for x in range(10) if x % 2]
[1, 3, 5, 7, 9]

>>> {x for x in range(10)}
set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> {c:ord(c) for c in "abc"}
{'a': 97, 'c': 99, 'b': 98}

>>> (x for x in range(10))
<generator object <genexpr> at 0x10328a690>
```

 -  多个for子句 可实现嵌套

```python
>>> ["{0}{1}".format(c, x) for c in "abc" for x in range(3)]
['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']
```

 - 每个子句都可有条件表达式，内层可引用外层名字。

```python
>>> ["{0}{1}".format(c, x) \
...     for c in "aBcD" if c.isupper() \
...     for x in range(5) if x%2  ]    
['B1', 'B3', 'D1', 'D3']
```

<h2 id="d140d37ad98c12ccd8e1c432f548bcdb"></h2>


### Slice

```python
>>> x = range(10) 

# reverse
>>> x[7:3:-2]
[7, 5]

# 可按切片范围删除序列元素
>>> x = range(10)
>>> del x[4:8]; x
[0, 1, 2, 3, 8, 9]

# 甚至不等长的切片替换
>>> a = [1, 2, 3]
>>> a[:1] = ["a", "b", "c"]
>>> a
['a', 'b', 'c', 2, 3]
```

<h2 id="1596d63c8ed6ef83ea2fee5f847baca9"></h2>


### 相等 , 操作符 "==" 可被重载

 - 操作符 "==" 可被重载，不适合用来判断两个名字是否指向同一对象
    - "==" 实际调用的是 `__eq__` 方法





