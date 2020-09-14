...menustart

- [Python3 Feature](#95cf1c5f0ad17ace298a562cab2cc645)
    - [Feature 1: Advanced unpacking](#5e0f49a3b1558b75a741f2bf4c07d934)
    - [Feature 2: Keyword only arguments](#5b2106affc32d8704adfa53688755516)
    - [Feature 5: Everything is an iterator](#5305fcfeefb27109e0064596d336c738)
    - [Feature 6: No more comparison of everything to everything](#cc1c5df0e93af9c93e7b0ae946db572b)
    - [Feature 7: yield from](#591d0ac5e723e96893cd88c01fb953dd)
    - [Feature 8: asyncio](#a93b92af2ea8b01917f2773ee72d5d0d)
    - [Feature 9: Standard library additions](#34f534cb76010ba480101eb84a40e85e)
    - [Feature 10: Fun](#b8bef80b08cb6ee429e103a20e52040d)
    - [Feature 11: Unicode and bytes](#698af8e97e5d339b9bc0208c5cd2cde1)
    - [Feature 12: Matrix Multiplication](#cf11c0ff8d4c3fcefe67a49a11e934b1)
    - [Feature 13: Pathlib](#ff0bcfcf9c1a95986e475dc4239c591f)

...menuend


<h2 id="95cf1c5f0ad17ace298a562cab2cc645"></h2>


# Python3 Feature

<h2 id="5e0f49a3b1558b75a741f2bf4c07d934"></h2>


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

<h2 id="5b2106affc32d8704adfa53688755516"></h2>


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

<h2 id="5305fcfeefb27109e0064596d336c738"></h2>


## Feature 5: Everything is an iterator

<h2 id="cc1c5df0e93af9c93e7b0ae946db572b"></h2>


## Feature 6: No more comparison of everything to everything

<h2 id="591d0ac5e723e96893cd88c01fb953dd"></h2>


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

<h2 id="a93b92af2ea8b01917f2773ee72d5d0d"></h2>


## Feature 8: asyncio

<h2 id="34f534cb76010ba480101eb84a40e85e"></h2>


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


<h2 id="b8bef80b08cb6ee429e103a20e52040d"></h2>


## Feature 10: Fun

Function annotations

```python
def f(a: stuff, b: stuff = 2) -> result:
    ...
```

 - Annotations can be arbitrary Python objects.
 - Python doesn't do anything with the annotations other than put them in an `__annotations__` dictionary.

<h2 id="698af8e97e5d339b9bc0208c5cd2cde1"></h2>


## Feature 11: Unicode and bytes

 - In Python 2, str acts like bytes of data.
 - There is also unicode type to represent Unicode strings.  
 - In Python 3, str is a string.  
 - bytes are bytes.  
 - There is no unicode. str strings are Unicode.

<h2 id="cf11c0ff8d4c3fcefe67a49a11e934b1"></h2>


## Feature 12: Matrix Multiplication

```python
np.dot(a, b)

#in python 3

a @ b
```

<h2 id="ff0bcfcf9c1a95986e475dc4239c591f"></h2>


## Feature 13: Pathlib

```python
filepath = os.path.join(directory, "test_file.txt")

# in python 3
filepath = directory / "test_file.txt"
```


