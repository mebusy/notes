
# 2 Modules and libraries


## 2.1 THE IMPORT SYSTEM

 - When importing modules, Python relies on a list of paths.
 - This list is stored in the `sys.path` variable and tells Python where to look for modules to load
 - There is 2 approaches to append the search path

```python
>>> import sys
>>> sys.path.append('/foo/bar')

$ PYTHONPATH=/foo/bar python
>>> import sys
>>> '/foo/bar' in sys.path
True
```

 - You can also add a custom module finder by appending a factory class to `sys.path_hooks`.

## 2.5


 - 在编写任何代码之前编写库的文档给我一种思考使用它的特性和工作流程的方法，而不必执行细节。


# 3 Documentation

 - The de facto standard documentation format for Python is *reStructuredText*
    - It’s a lightweight markup language (like the famous Markdown) that’s as easy to read and write for humans as it is for computers.
 - [sphinx](http://www.sphinx-doc.org/en/stable/) is the most com- monly used tool for working with this format:
    - it can read reST-formatted content and output documentation in a variety of other formats.
 - Your **project documentation** should include:
    - *The problem your project is intended to solve*, in one or two sentences.
    - *The license your project is distributed under.* 
    - *A small example of how it works.*
    - *Installation instructions.*
    - Links to community support, mailing list, IRC, forums, etc.
    - A link to your bug tracker system.
    - A link to your source code so that developers can download and start delving into it right away.
 - You should also include a README.rst file that explains what your project does.
    - This README will be displayed on your GitHub or PyPI project page; both sites know how to handle reST formatting.

## 3.1 Getting started with Sphinx and reST

# 7 Methods and decorators

 - 装饰器本质上是一个函数，它将另一个函数作为参数，并用一个新的，修改过的函数替换它。
 - 最简单的装饰器是 identity function ，它除了返回原始函数外什么都不做:

```python
def identity(f):
    return f

@identity
def foo():
    return 'bar'
```

 - 和原来的 foo 函数完全等效
 - identity function 没什么用，但它依然起作用了，只是什么都没做

```python
foo = identity(foo)
```

## 7.1

 - 装饰器本质上是一个函数，它将另一个函数作为参数，并用一个新的，修改的函数替换它。

---

Example 7.1   A registering decorator

```python
_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register 
def foo(): return 'bar'
```

 - 在这个例子中，我们注册函数, 把它们的名字存储在字典中，以便将来 通过名字访问它们.

---

 - 装饰器的 主要用例， 是 把需要在 多个函数 之前/之后/或周围 调用的 **通用代码** 分离出去。
 - 考虑一组类方法， 它们都需要 检验 传入的 username 参数

```python
class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to get food")
        self.storage.put(food)
```  

 - 首先，很容易考虑到的是，提出 公共的 checking code

```python
def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to get food")

class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)
    def put_food(self, username, food):
        check_is_admin(username)
        self.storage.put(food)
```

 - 代码干净了很多，使用装饰器我们可以做得更好
    - 显然，我们不能像  @register 那样直接返回 f , 那样无法处理 函数参数，我们需要一个wrapper

```python
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        # to make the check work
        # you need call like: 
        #   a.get_food( username="admin" , food="food")
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper   # f is wrapped

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)
    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)
```

 - 但是，上面这个实现有严重的缺陷， 装饰器返回了一个新的函数，这个函数丢失了 原来函数的信息
    - 比如 ，docstring 和 func.__name__

```python
>>> foobar.__doc__
>>> foobar.__name__
'wrapper'
```

 - 幸运的是， **functools** 模块 提供了一个 `update_wrapper` 方法 用来解决这个问题
 - `update_wrapper` 把这些属性 拷贝给了 wrapper 

```python
foobar = functools.update_wrapper(is_admin, foobar)
```

 - 很丑陋。 还好  **functools**  同时还提供了一个装饰器 `functools.wraps`

```python
def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
         if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
         return f(*args, **kwargs)
    return wrapper
```

 - 在这个例子中 ，我们总是假设 这个装饰器装饰的方法，以这种形式被调用
    - `func( ... , username = username  )`
 - 然后你无法保证这点。所以我们一个更加 聪明的做法

**Retrieving function arguments using inspect**

```python
import functools
import inspect
def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
         func_args = inspect.getcallargs(f, *args, **kwargs)
         print func_args
         if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
         return f(*args, **kwargs)
    return wrapper
    
@check_is_admin
def get_food(username, type='chocolate'):
    return type + " nom nom nom!"
```

 - inspect.getcallargs，它返回一个包含参数名称和值作为键值对的字典。

```python
>>> get_food( "admin"  )
{'username': 'admin', 'type': 'chocolate'}
'chocolate nom nom nom!'
```

## 7.2 

## 7.3 Static Method

 - Static methods are methods which belong to a class, 
    - but don’t actually operate on class instances.
 - 好处
    - P4thon doesn’t have to instantiate a bound method for each Pizza object we create
    - Bound methods are objects, too, and creating them has a cost.

```python
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y


>>> Pizza().cook is Pizza().cook
False
```

## 7.4 Class method

 - Class methods are methods that are bound directly to a class rather than its instances:


```python
class Pizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

>>> Pizza.get_radius is Pizza().get_radius
True
```

 - However you choose to access this method, it will be always bound to the class it is attached to, and its first argument will be the class itself
 - Class methods are mostly useful for creating factory methods
    - 用 classmethod实现工厂方法 比 用staticmethod 好的地方是，不用硬编码 类名

```python
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        # use cls, not hard-code class name
        return cls(fridge.get_cheese() + fridge.get_vegetables())
```

## 7.5 Abstract methods

 - 实现 Abstract methods 最简单的办法是

```python
class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError
```

 - 这个方法的缺点是， 你不知道你漏了 某个 抽象函数的实现，直到你在运行时碰到了这个 exception
 - 使用 **abc**模块 可以在你实例化一个 有抽象方法的对象时，给出警告


```python
import abc
class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
         """Method that should do something."""

>>> BasePizza()
TypeError: Can't instantiate abstract class BasePizza with abstract methods get_radius
```

## 7.6 Mixing static, class, and abstract methods





