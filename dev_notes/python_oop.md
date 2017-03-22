...menustart

 - [oop for python](#cad1f4790e85f2b08e65e3c6fd4ce14b)
	 - [Singleton](#6ff5f73c8b5ebd311406568c8ef50bfd)
	 - [disable dynamically define new fields to a class](#0b45bfca581dfd81b42b816b63798e78)
	 - [class property](#0766b2e74f5159a8c7d793f1f1cee8a6)

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


<h2 id="0766b2e74f5159a8c7d793f1f1cee8a6"></h2>

## class property 

 - readonly 
	- `@ClassProperty` , `@classmethod` 顺序很关键！ 

```python
class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()

class Foo(object):
    _var = 5

    @ClassProperty
    @classmethod
    def var(cls):
        return cls._var

    @var.setter
    @classmethod
    def var(cls, value):
        cls._var = value

assert foo.var == 5
```

