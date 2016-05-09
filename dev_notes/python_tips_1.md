# python tips

---

## 语法技巧

### eval 环境
   
eval() 默认使用当前环境的名字空间，也可以带入自定义字典

```
ns=dict(x=10,y=20)
eval("x+y" , ns )
```

还可以使用 exec 来执行一个代码段


### 获取变量x的内存地址

```
id(x) 
```

### for i, v  枚举

```
for i, item in enumerate(  iterable ):
```

### 数组排序

```
autodances.sort( key = lambda x  :  x["time"] , reverse = False )
```

use `cmp` method

```
l.sort(cmp=lambda x,y:cmp( x.lower(), y.lower()  ))
```

### 字典排序 sorted

```
>>> d={"b":2, "a":3, "c":1}
>>> sorted(d)     #对 key 进行排序，输出一个key list
['a', 'b', 'c']      
>>> sorted(d.items())     #对key 进行排序，返回 元组 list
[('a', 3), ('b', 2), ('c', 1)]
>>> sorted(d.items() , key=lambda x:x[1])    # 对 值 进行排序， 返回 元组 list
[('c', 1), ('b', 2), ('a', 3)]
>>> dict(sorted(d.items() , key=lambda x:x[1]) )   # 对 值 进行排序，dict
{'a': 3, 'c': 1, 'b': 2}
```


### 迭代和组合

了解itertools模块：  该模块对迭代和组合是非常有效的

```
>>> import itertools 
>>> iter = itertools.permutations([1,2,3]) 
>>> list(iter) 
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

### bisect模块保持列表排序

这是一个免费的二分查找实现和快速插入有序序列的工具。你已將一个元素插入列表中, 而你不需要再次调用 sort() 来保持容器的排序, 因为这在长序列中这会非常昂贵. 

```
>>> import bisect 
>>> bisect.insort(list, element) 
```

### 使用dict 和 set 测试成员

hash实现, 查找效率可以达到O(1)

### url unescape

```
>>> import urllib
>>> url_unquote=urllib.unquote(a)
```

或

```
import HTMLParser
html_parser = HTMLParser.HTMLParser()
txt = html_parser.unescape(html)
```



### 序列 ()  

速度比列表快，  可以作为字典关键字

### 自省的核心 getattr 函数

```
getattr(obj, name [ ,  default_method_return_if_not_exist ] )

example:

for i in  dir( obj ):
    method = getattr( obj, i   )
    print i , method
```

### callable

```
methodList = [method for method in dir(object) if callable(getattr(object, method))]
```

### dict get

从字典中获取一个值 

```
if d.has_key('key'):
    print d['key']
else:
    print 'not found'
```

可以简化为:

```
print d.get('key', 'not found')
```    

### dict setdefault

dict 插入key-value时，如果key不存在，先初始化为默认值(一般用于value是list, dict 类型)

```
def addword2dict(word, pagenumber): 
    dict.setdefault(word, []).append(pagenumber)
```

### dict insection

找出两个字典的交集 

```
print "Intersects:", [k for k in some_dict if k in another_dict]
```

速度上取胜:

```
print "Intersects:", filter(another_dict.has_key, some_dict.keys())
```


### 类型判断

```
isinstance(u'a', unicode)
```

### 方法内全部局部变量

Python has a locals() function which gives you back a dictionary of local variables within the function

### python 下划线变量

核心风格：避免用下划线作为变量名的开始。

 - _xxx      
    - 不能用'from module import *'导入 
    - **保护变量**，意思是只有 类对象和子类对象自己 能访问到这些变量
 - __xxx    
    - 类中的私有变量名
    - **私有成员**，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据
 - __xxx__ 
    - 系统定义名字 
    - python里特殊方法专用的标识

### re.sub group: number after \number

```
re.sub(r'(foo)', r'\g<1>123', 'foobar')
```

----------


---

## 数字进制转换

### 10进制数字 => 2,8,16进制字符串

```
bin(123)  # 2
oct(18)   # 8
hex(10)   # 16
```

### 2,8,16进制字符串 ==> 10进制数字 

```
int('022',8)
```

### 格式化数字为16进制字符串

```
>>> "%x" % 108
'6c'
>>>
>>> "%X" % 108
'6C'
>>>
>>> "%#X" % 108
'0X6C'
>>>
>>> "%#x" % 108
'0x6c'
```

---

## 字符处理

### ascii列表 -> 字符串

good 1

```
import string
def f6(list):
    return string.joinfields(map(chr, list), "")
```

the best 1

```
import array
def f7(list):
    return array.array('B', list).tostring()
```

### 编码

#### char <-> ascii

```
>>> print ord('a')
97
>>> print chr(97)
a
```

`'2' == '\x32' == '\062'`

#### unichr  <-> unicode string

```
>>> print ord(u"我")
25105
>>> print unichr( 25105 )
我
```

#### unicode -> special encoded string

```
unicodestring = u"Hello world"
utf8string = unicodestring.encode("utf-8")
asciistring = unicodestring.encode("ascii")
isostring = unicodestring.encode("ISO-8859-1")
utf16string = unicodestring.encode("utf-16")
```

#### special encoded string -> unicode

```
plainstring1 = unicode(utf8string, "utf-8")
plainstring2 = unicode(asciistring, "ascii")
plainstring3 = unicode(isostring, "ISO-8859-1")
plainstring4 = unicode(utf16string, "utf-16")
```

unicode 可以使用 u"\uxxxx" 表示，但是当我们从某处获取 "\uxxxx"， 并不能直接还原成 unicode，需要通过  "\uxxxx".decode("unicode-escape") 来转成 unicode， 注意， xxxx 必须保证有4个，不足以0补全

反之 ，通过  uni.encode("unicode-escape")  来 获得 "\uxxxx"  形式的字符串



---

## 中文处理

### 改变脚本本地编码

```
reload(sys)
sys.setdefaultencoding('utf8') 
```

### 写 带中文字符的文件

```
fp = codecs.open( target_sheet_name + '.txt'  , "w", "utf-8")
fp.write(jsonObj )
fp.close()
```

---

## encrypt

### base64

```
import base64
# base 64 decode
data = base64.b64decode( data ) 
# base64 encode
result_data = base64.b64encode( result_data)
```

---

## Misc

### try - except 打印错误

```
import traceback
traceback.print_exc()
```

或者

```
s=sys.exc_info()
print "Error '%s' happened on line %d" % (s[1],s[2].tb_lineno)

```

### run in 32bit mode

```
arch -i386 python2.7
```

### python 并行任务技巧

 - 使用带有并发功能的map
 - Dummy是一个多进程包的完整拷贝
 - 唯一不同的是，多进程包使用进程，而dummy使用线程
 - 简言之，IO 密集型任务选择multiprocessing.dummy，CPU 密集型任务选择multiprocessing

```
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool( [#Pool] )
results = pool.map( func ,  param_set_list  )
pool.close()
pool.join()
```

### profile

```
python -m cProfile  xxx.py
```

or

```
import profile
profile.run ( 'func_name')
```

### 强制浮点数运算

```
>>> from __future__ import division
>>> 1/2
0.5
```

### 输出一个对象各个成员的名称和值

```
>>> g = lambda m: '\n'.join([ '%s=%s'%(k, repr(v)) for k, v in m.__dict__.iteritems() ])
>>> g(obj)
```
### 读取文件特定行

```
import linecache
#thefiepath             文件路径
#desired_line_number    整数，文件的特定行 
theline = linecache.getline(thefilepath, desired_line_number)
```        

### 文件修改／创建时间

```
import   os,time 
time.ctime(os.stat( "d:/learn/flash.txt ").st_mtime)   #文件的修改时间 
time.ctime(os.stat( "d:/learn/flash.txt ").st_ctime)   #文件的创建时间
```

### python 写 只读文件

读之前：

```
os.chmod(_path,  stat.S_IREAD)
```

写之前:

```
os.chmod(_path, stat.S_IWRITE | stat.S_IREAD)
```

