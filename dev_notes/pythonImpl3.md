
# 3. 表达式

 - 如果你喜欢 lua的end ...

```python
>>> # 自定义 end 伪关键字
>>> __builtins__.end = None
>>> def test(x):
>>>     pass
>>> end
```

## 3.2 命名规范

 - 模块中以 `_` 开头的名字视为私有
 - 以 `__` 开头的类成员名字视为私有
 - 同时以`__` 开头和结尾的名字，通常是特殊成员
 - 单一 `_` 代表最后表达式的返回值

```python
>>> s = set("abc")
>>> s.pop()
'a'
>>> _
'a'
```

## 3.3 赋值

 - 除非在函数中使用关键字 global、nolocal 指明外部名字 ， 否则赋值语句总是 **在当前名字空间创建或修改 {name:object} 关联**
 - 代码 block 不知 名字空间 ！！！ 这点和c不同

```python
>>> def test():
... while True:
...     x = 10
...     break
... print locals()
... print  # 这个写法c里会报错 

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

## 3.4 表达式

### while

 - else 分支
 - 可以用 else 分支标记循环逻辑被完整处理

```python
>>> while x > 0:
...     x -= 1
... else:
...     print "over!"

```

### del

 - 可删除名字、序列元素、字典键值，以及类对象成员

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

### 相等 , 操作符 "==" 可被重载

 - 操作符 "==" 可被重载，不适合用来判断两个名字是否指向同一对象
    - "==" 实际调用的是 `__eq__` 方法





