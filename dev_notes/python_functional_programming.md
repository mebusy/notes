
# Python 函数编程

functools, itertools, operator是Python标准库为我们提供的支持函数式编程的三大模块

# 1 functools

functools 提供了一些非常有用的高阶函数。

## 1.1 partial

```python
>>> from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo('10010')
18
```

basetwo('10010')实际上等价于调用int('10010', base=2)


## 1.2 wraps

 - 装饰器会遗失被装饰函数的__name__和__doc__等属性，可以使用@wraps来恢复。

```python
from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper():
        """wrapper_doc"""
        print('Calling decorated function')
        return f()
    return wrapper

@my_decorator
def example():
    """example_doc"""
    print('Called example function')

>>> example.__name__
'example'
>>> example.__doc__
'example_doc'
```

---

# 2 itertools

itertools 提供了非常有用的用于操作迭代对象的函数

## 2.1 无限迭代器

### count  无限迭代器

 - count(start=0, step=1) 会返回一个无限的整数iterator

```python
from itertools import count
>>> for i in zip(count(1), ['a', 'b', 'c']):
...     print i
... 
(1, 'a')
(2, 'b')
(3, 'c')
```

### cycle  序列无限重复迭代 

 - cycle(iterable) 

```python
>>> from itertools import cycle
>>> for i in zip(range(6), cycle(['a', 'b', 'c'])):
...     print i
... 
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'a')
(4, 'b')
(5, 'c')
```

### repeat   单个元素无限重复

 - repeat(object[, times]) 

```python
>>> from itertools import repeat
>>> for i in zip(count(1), repeat('over-and-over', 5)):
...     print i
... 
(1, 'over-and-over')
(2, 'over-and-over')
(3, 'over-and-over')
(4, 'over-and-over')
(5, 'over-and-over')
```

## 2.2 chain 

 - itertools.chain( \* iterables)可以将多个iterable组合成一个iterator。

```python
>>> from itertools import chain
>>> list(chain([1, 2, 3], ['a', 'b', 'c']))
[1, 2, 3, 'a', 'b', 'c']
```

 - chain.from_iterable(iterable)和chain类似
	- 但是只是接收单个iterable，然后将这个iterable中的元素组合成一个iterator。

```python
>>> from itertools import chain
>>> list(chain.from_iterable(['ABC', 'DEF']))
['A', 'B', 'C', 'D', 'E', 'F']
```

## 2.3 compress

 - compress(data, selectors)
	- 接收两个iterable作为参数,只返回selectors中对应的元素为True的data
	- 当data/selectors之一用尽时停止

```python
>>> from itertools import compress
>>> list(compress([1, 2, 3, 4, 5], [True, True, False, False, True]))
[1, 2, 5]
```


## 2.4 islice

 - islice(iterable, stop) 
 - islice(iterable, start, stop[, step]) 
	- 与python切片类似， 只是不能对start、start和step使用负值。

```python
>>> from itertools import islice
>>> for i in islice(range(40), 0, 100, 10):
...     print i
... 
0
10
20
30
```

## 2.5 tee

 - tee(iterable, n=2) 
	- 返回n个独立的iterator

```
>>> from itertools import islice, tee
>>> r = islice(count(), 5)
>>> i1, i2 = tee(r)
# tee 调用后， r 失效
```

## 2.6 starmap

 - 和 map 类似，只是 把list 中的每个元素 作为迭代器， 迭代结果 作为函数调用参数

```python
>>> from itertools import starmap
>>> list(starmap(os.path.join, [ ("a","b") ]))
['a/b']
>>> list(starmap(os.path.join, [ "abc" , "cdf" ]))
['a/b/c', 'c/d/f']
```

## 2.7 takewhile

 - takewhile(predicate, iterable) 
	- 只要predicate返回True，不停地返回iterable中的元素
	- 知道 predicate返回False

```python
def less_than_10(x):
    return x < 10
itertools.takewhile(less_than_10, itertools.count())
=> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
itertools.takewhile(is_even, itertools.count())
=> 0
```

## 2.8 dropwhile

 - dropwhile(predicate, iterable) 
	- 和 takewhile 相反
	- 在predicate返回True时舍弃元素，然后返回其余迭代结果

```python
itertools.dropwhile(less_than_10, itertools.count())
=> 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ...
itertools.dropwhile(is_even, itertools.count())
=> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...
```

## 2.9 groupby

 - groupby(iterable, key=None)
 	- 把iterator中 ***相邻***的***重复***元素挑出来放在一起 

```python
>>> from itertools import groupby
>>> for key, group in itertools.groupby('AAAABBBCCDAABBB'):
...     print key , list(group)
... 
A ['A', 'A', 'A', 'A']
B ['B', 'B', 'B']
C ['C', 'C']
D ['D']
A ['A', 'A']
B ['B', 'B', 'B']
```

---

## 2.10 排列组合 generators

### product

 - product( \* iterables, repeat=1)
	- product(A, B) returns the same as ((x,y) for x in A for y in B)
	- product(A, repeat=4) means the same as product(A, A, A, A)
	- 数数中的 可重复选取 的排列

```python
>>> from itertools import product
>>> from itertools import product
>>> list(product(range(3), repeat=2))
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

### permutations

 - permutations(iterable, r=None)
	- 返回长度为r的所有可能的排列 P(n,r)

```python
>>> from itertools import permutations
>>> list( permutations( range(3) ) )
[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
>>> list( permutations( range(3) , r=2) )
[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
>>> list( permutations( range(3) , r=1) )
[(0,), (1,), (2,)]
```

### combinations

 - combinations(iterable, r) 
	- 返回长度为r的所有可能的组合 C(n,r)

```python
>>> from itertools import combinations
>>> list( combinations( range(3) , 2) )
[(0, 1), (0, 2), (1, 2)]
>>> list( combinations( range(3) , 1) )
[(0,), (1,), (2,)]
>>> list( combinations( range(3) , 3) )
[(0, 1, 2)]
```

### combinations_with_replacement 

 - 可重复选取的 组合

```python
>>> from itertools import combinations_with_replacement
>>> list( combinations_with_replacement( range(3) , 2) )
[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
>>> list( combinations_with_replacement( range(3) , 1) )
[(0,), (1,), (2,)]
>>> list( combinations_with_replacement( range(3) , 3) )
[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
```

# 3 operator

这个模块提供了一系列的函数操作。比如，operator.add(x, y)等于x+y 

```python
'abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf', 'delitem', 'delslice', 'div', 'eq', 'floordiv', 'ge', 'getitem', 'getslice', 'gt', 'iadd', 'iand', 'iconcat', 'idiv', 'ifloordiv', 'ilshift', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irepeat', 'irshift', 'isCallable', 'isMappingType', 'isNumberType', 'isSequenceType', 'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'repeat', 'rshift', 'sequenceIncludes', 'setitem', 'setslice', 'sub', 'truediv', 'truth', 'xor'
``` 

```python
and_(a,b)  -- Same as a & b.
iadd(a, b) -- Same as a += b.
index(a) -- Same as a.__index__()
indexOf(a, b) -- Return the first index of b in a.
inv(a) -- Same as ~a.
invert(a) -- Same as ~a.
irepeat(a, b) -- Same as a *= b, where a is a sequence, and b is an integer.
isCallable(a) -- Same as callable(a).
is_(a, b) -- Same as a is b.
is_not(a, b) -- Same as a is not b.
itruediv(a, b) -- Same as a /= b when __future__.division is in effect.
truth(a) -- Return True if a is true, False otherwise.
```



