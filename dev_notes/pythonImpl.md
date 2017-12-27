
# python 实现笔记

# 1 基本环境

## 1.2 类型和对象

 - 万物皆对象
 - Type 也是对象
 - 每个对象都有一个标准头， 通过头部信息就能 知道Type
    - 头部信息由 引用计数, 和 类型指针 组成
 - 以 int 为例

```c
#define PyObject_HEAD                   \
    Py_ssize_t ob_refcnt;               \
    struct _typeobject *ob_type;

typedef struct _object {
    PyObject_HEAD
} PyObject;

typedef struct {
    PyObject_HEAD    // 在 64 位版本中，头 度为 16 字节。 
    long ob_ival;    // long 是 8 字节。
} PyIntObject;
```

 - 所以，一个 python int 64位系统上，占 24字节

```python
>>> import sys
>>> x = 0x1234   # don't use small integer here
>>> sys.getsizeof(x)
24
>>> sys.getrefcount(x) # 注意形参也会增加1次引用
2 
```

 - 类型指针则指向具体的类型对象
    - 是的，Type 也是对象
    - 其中包含了继承关系、静态成员等信息
    - 所有 内置类型对象 都能从 types 模块中找到， int ,long, str 这些 都是简短别名

```python
>>> import types
>>> x = 20
>>> type(x) is types.IntTyp
True

>>> x.__class__  # __class__ 通过类型指针来获取类型对象
<type 'int'>

>>> x.__class__ is type(x) is int is types.IntType
True
```

 - 除了 int 这样的固定长度类型外，还有 long、str 这类变长对象。
    - 其头部多出 1个记录元素项数量的字段。
    -  如 str 的字节数量，list 列表的长度等等

```c
define PyObject_VAR_HEAD \
    PyObject_HEAD \
    Py_ssize_t ob_size;   /* Number of items in variable part */

typedef struct {
    PyObject_VAR_HEAD
} PyVarObject;
```

## 1.3 名字空间

```python
>>> x 
NameError: name 'x' is not defined
```

 - 和 C 变量名是内存地址别名不同 , Python 的名字实际上是1个字符串对象
    - 它和所指向的目标对象  一起 在名字空间中构成一项 {name: object} 关联
 - Python 有多种名字空间
    - 模块名字空间 : globals
    - locals
        - 在函数外部，locals() 和 globals() 作用完全相同
        - 在函数内部, locals() 则是获取当前 函数堆栈帧的名字空间, 函数参数、局部变量等信息 
    - class
    - instance 等

```python
>>> x = 123 
>>> globals() 
{'x': 123, ......}
```

 - 可以看出，名字空间就是一个 dict 
    - 我们完全可以直接在名字空间添加项来创建名字 

```python
>>> globals()["y"] = "Hello, World!"
>>> y 
'Hello, World!'
```

### Names have no type, but objects do.

 - 正是因为 名字的弱类型特征， 我们可以在运行期随时将其关联到任何类型对象
 - 使用名字空间管理上下文对象，带来无与伦比的灵活性, 但也牺牲了执行性能。 

## 1.4 内存管理

### 内存池

 - 减少操作系统内存分配和回收操作
 - 那些 ≤ 256 字节对象，将直接从内存池中获取存储空间
 - 根据需要，虚拟机每次从操作系统申请1块 256KB，取名为 arena 的大块内存。 
    - 并按系统页大小  ，划分成多个 pool。
    - 每个 pool 继续分割成 n 个 大小相同的 block .
        - block 是内存池 最小存储单位
 - 





