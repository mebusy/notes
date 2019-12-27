...menustart

 - [oop for python](#cad1f4790e85f2b08e65e3c6fd4ce14b)
     - [Singleton](#6ff5f73c8b5ebd311406568c8ef50bfd)
     - [disable dynamically define new fields to a class](#0b45bfca581dfd81b42b816b63798e78)
     - [disable dynamically del a field from a class](#d697d7eeb396fa20ed1c5109befb2a67)
     - [access like a dict](#45a042564f32c7d808e10eb2c157142b)
     - [assignment lick c struct](#b6a463819ebef130b1d9e14cc626eba5)
     - [readonly class field](#ff1e065fdd70b15412dc1f6a216d1405)

...menuend


<h2 id="cad1f4790e85f2b08e65e3c6fd4ce14b"></h2>


# oop for python

<h2 id="6ff5f73c8b5ebd311406568c8ef50bfd"></h2>


## Singleton 

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
class MyClass(BaseClass):
    __metaclass__ = Singleton

#Python3
class MyClass(BaseClass, metaclass=Singleton):
    pass
```


<h2 id="0b45bfca581dfd81b42b816b63798e78"></h2>


## disable dynamically define new fields to a class 

Python can we dynamically define new fields to a class during runtime. 

It's possible to restrict the instance attributes that can be added through the class attribute `__slots__`:

```python
>>> class B(object):
...     __slots__ = ['only_one_attribute']
...     def __init__(self):
...         self.only_one_attribute = 'one'
...     def add_attr(self):
...         self.another_attribute = 'two'
```

 - 注意： B的派生类也必须 显式 定义 `__slots__` , 即便 是空的
    - `__slots__ = {}` 

<h2 id="d697d7eeb396fa20ed1c5109befb2a67"></h2>


## disable dynamically del a field from a class 

```python
class A(object):
    def __delattr__(self, key) :         
        raise Exception( "can not delete "+key )
```

<h2 id="45a042564f32c7d808e10eb2c157142b"></h2>


## access like a dict 

```python
def __setitem__(self,key, value) :
    ...
def __getitem__(self,key) :
    ...
```

<h2 id="b6a463819ebef130b1d9e14cc626eba5"></h2>


## assignment lick c struct 

 - using a  setter method  to copy content value 

<h2 id="ff1e065fdd70b15412dc1f6a216d1405"></h2>


## readonly class field

```python
>>> class A(object):
...     def __init__(self, a):
...         self._a = a
...
...     @property
...     def a(self):
...         return self._a
... 
>>> a = A('test')
>>> a.a
'test'
>>> a.a = 'pleh'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```

 - more simple way ... 
    - https://github.com/oz123/oz123.github.com/blob/master/media/uploads/readonly_properties.py
    - this `readonly_properties` is  for python3 , if you use python2.7, you may need modify some code 

```
...
class NewClass(cls , object ):
    ...
        super( NewClass, self  ).__setattr__(name, value)
```


