...menustart

- [5 迭代器](#8007985f1ff8a2c3ae3abb1775b4ce2b)
    - [5.1 迭代器](#14926a66d27e071bd4821a2d86af55fa)
    - [5.2 生成器](#71364882befa312cee5d34aeb80f07ab)
        - [协程](#ebe9865478157ea2f0762aa24f6a85f5)
    - [5.3 模式](#0bae6d90ea71b1bd81064b43a6880b48)
    - [5.4 宝藏](#1881f62b5fd451873d1bc5b9e9db67ea)

...menuend


<h2 id="8007985f1ff8a2c3ae3abb1775b4ce2b"></h2>


# 5 迭代器

<h2 id="14926a66d27e071bd4821a2d86af55fa"></h2>


## 5.1 迭代器

- 迭代器协议，仅需要 `__iter__()` 和 `next()` 两个方法
    - 前者返回迭代器对象
    - 后者依次返回数据，直到引发 StopIteration 异常结束
- 最简单的做法是 内置函数 `iter()`， 它返回常用类型的迭代器包装对象。

```python
>>> class Data(object):
...    def __init__(self):
...        self._data = []
...
...    def add(self, x):
...        self._data.append(x)
...
...    def data(self):
...        return iter(self._data)
```

- 返回迭代器对象代替 `self._data` 列表, 可避免对象状态被外部修改。
    - 或许你会尝试返回 tuple，但这需要复制整个列表，浪费更多的内存。
- `iter()` 很方便，但无法让迭代中途停 ，这需要自己实现迭代器对象。
    - 在设计原则上，通常会将迭代器从数据对象中分离出去。
    - 因为迭代器需要维持状态，且可能有多个迭代器在同时操控数据，这些不该成为数据对象的负担.

```python
>>> class Data(object):
...     def __init__(self, *args):
...         self._data = list(args)
...
...     def __iter__(self):
...         return DataIter(self)

>>> class DataIter(object):
...     def __init__(self, data):
...         self._index = 0
...         self._data = data._data
...
...     def next(self):
...         if self._index >= len(self._data): raise StopIteration()
...         d = self._data[self._index]
...         self._index += 1
... return d

>>> d = Data(1, 2, 3)
>>> for x in d: print x
1
2
3
```

- Data 仅仅是数据容器，只需 `__iter__` 返回迭代器对象
- 由 DataIter 提供 next 方法

- 除了 for 循环，迭代器也可以直接用 `next()` 操控。

```python
>>> d = Data(1, 2, 3)
>>> it = iter(d)
>>> it
<__main__.DataIter object at 0x10dafe850>
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
StopIteration
```

<h2 id="71364882befa312cee5d34aeb80f07ab"></h2>


## 5.2 生成器

- 基于索引实现的迭代器有些丑陋
- 更合理的做法是用 yield 返回实现了迭代器协议的 Generator 对象。

```python
>>> class Data(object):
...     def __init__(self, *args):
...         self._data = list(args)
...
...     def __iter__(self):
...         for x in self._data:
...             yield x

>>> d = Data(1, 2, 3)
>>> for x in d: print x
1
2
3
```

- 编译器 会将包含 yield 的方法 (或函数) 重新打包, 使其返回 Generator 对象.
    - 无须再费力地维护迭代器类型了.

```python
>>> d.__iter__()
<generator object __iter__ at 0x10db01280>
>>> iter(d).next()
1
```

<h2 id="ebe9865478157ea2f0762aa24f6a85f5"></h2>


### 协程

- yield 为何能实现这样的魔法?
- 这涉及到协程 (coroutine) 的工作原理。
- `msg = yield return_result `

```python
>>> def coroutine():
...     print "coroutine start..."
...     result = None
...     while True:
...         s = yield result
...         result = s.split(",")
...

>>> c = coroutine()
>>> c.send(None)  # send(None) or next() 启动
coroutine start...
>>> c.send("c,d")    # send msg to coroutine , resume it
['c', 'd']
>>> c.send("e,f")
['e', 'f']
>>> c.close()  # close
>>> c.send("a,b")
StopIteration
```

- 执行流程
    - 创建协程后对象，必须使用 send(None) 或 next() 启动
    - 协程在执行 yield result 后让出执行，等待消息
    - 调用方发送 send("a,b") 消息，协程恢复执行， 将接收到的数据保存到 s，执行后续流程
    - 再次循环到 yeild，协程返回前面的处理结果，并再次让出执行。
    - 直到关闭或被引发异常

- 虽然生成器 yield 能轻松实现协程机制，但离真正意义上的高并发 完全不是一回事。
    - 可使用 gevent/eventlet库，或直接用 greenlet

<h2 id="0bae6d90ea71b1bd81064b43a6880b48"></h2>


## 5.3 模式

- 异步编程同步化
    - 不再需要回调
- Python官方的例子，利用一个@gen.coroutine装饰器来简化代码编写，原本调用-回调两段逻辑，现在被放在了一起，yield充当了回调的入口。这就是异步编程同步化！

```python
class AsyncHandler(RequestHandler):
    @asynchronous
    def get(self):
        http_client = AsyncHTTPClient()
        http_client.fetch("http://example.com",
                          callback=self.on_fetch)

    def on_fetch(self, response):
        do_something_with_response(response)
        self.render("template.html")
```

```python
class GenAsyncHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://example.com")
        do_something_with_response(response)
        self.render("template.html")
```


<h2 id="1881f62b5fd451873d1bc5b9e9db67ea"></h2>


## 5.4 宝藏

- 标准库 itertools 模块 是一块宝藏

---



