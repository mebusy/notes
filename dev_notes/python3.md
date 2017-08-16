
# Python3 Feature

## Feature 1: Advanced unpacking

```python
>>> a, b, *rest = range(10)
>>> rest
[2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> a, *rest, b = range(10)
>>> b
9
>>> rest
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
>>> *rest, b = range(10)
>>> rest
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> b
9
```

Get the first and last lines of a file

```python
>>> with open("using_python_to_profit") as f:
...     first, *_, last = f.readlines()
```

Refactor your functions

```python
def f(a, b, *args):
    stuff

=>

def f(*args):
    a, b, *args = args
    stuff
```

## Feature 2: Keyword only arguments

```python
def f(a, b, *args, option=True):
    ...
```

 - option comes after `*args`.
 - The only way to access `option` is to explicitly call `f(a, b, option=True)`
 - You can write just a `*` if you don't want to collect `*args`.

```python
def f(a, b, *, option=True):
    ...
```

---

```python
def sum(a, b, biteme=False):
    if biteme:
        shutil.rmtree('/')3
    else:
        return a + b

>>> sum(1,2,3) 
... 
```

Instead write

```python
def sum(a, b, * ,  biteme=False):
    if biteme:
        shutil.rmtree('/')3
    else:
        return a + b

>>> sum(1, 2, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: sum() takes 2 positional arguments but 3 were given
```

## Feature 5: Everything is an iterator

## Feature 6: No more comparison of everything to everything

## Feature 7: yield from

 - Pretty great if you use generators
 - Instead of writing

```python
for i in gen():
    yield i
```

 - Just write

```python
yield from gen()
```

 - Easily refactor generators into subgenerators.

---

 - Makes it easier to turn everything into a generator. See "Feature 5: Everything is an iterator" above for why you should do this.
 - Instead of accumulating a list, just yield or yield from.
 - for an example, we will create a list with dup numbers , like [0,0,1,1,2,2,3,3,...]

```python
# bad
def dup(n):
    A = []
    for i in range(n):
        A.extend([i, i])
    return A

# good
def dup(n):
    for i in range(n):
        yield i
        yield i

# better
def dup(n):
    for i in range(n):
        yield from [i, i]

```

## Feature 8: asyncio

## Feature 9: Standard library additions

 - faulthandler
 - ipaddress

```python
>>> ipaddress.ip_address('192.168.0.1')
IPv4Address('192.168.0.1')
>>> ipaddress.ip_address('2001:db8::')
IPv6Address('2001:db8::')
```

 - functools.lru_cache
    - A LRU cache decorator for your functions.

```python
@lru_cache(maxsize=32)
def get_pep(num):
    ... 

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```

 - enum
    - Finally, an enumerated type in the standard library.

```python
>>> from enum import Enum
>>> class Color(Enum):
...     red = 1
...     green = 2
...     blue = 3
...
```


## Feature 10: Fun

Function annotations

```python
def f(a: stuff, b: stuff = 2) -> result:
    ...
```

 - Annotations can be arbitrary Python objects.
 - Python doesn't do anything with the annotations other than put them in an `__annotations__` dictionary.

## Feature 11: Unicode and bytes

 - In Python 2, str acts like bytes of data.
 - There is also unicode type to represent Unicode strings.  
 - In Python 3, str is a string.  
 - bytes are bytes.  
 - There is no unicode. str strings are Unicode.

## Feature 12: Matrix Multiplication

```python
np.dot(a, b)

#in python 3

a @ b
```

## Feature 13: Pathlib

```python
filepath = os.path.join(directory, "test_file.txt")

# in python 3
filepath = directory / "test_file.txt"
```


