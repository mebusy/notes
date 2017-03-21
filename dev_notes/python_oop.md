

# oop for python

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

