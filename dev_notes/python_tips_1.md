...menustart

 - [python tips](#e7c8aa5b143e53ecad41b3612dab23ed)
   - [语法技巧](#cd82da5cf3ee760792e950b087be3d29)
     - [eval 环境](#49bdb1b4a214a6bc00824eb4f7b2c5f1)
     - [获取变量x的内存地址](#f372cdc8f82db5bb3a311edc6743e412)
     - [for i, v  枚举](#5bd260e9c2d18f7f2ff4c30f274ebc6b)
     - [数组排序](#d4c8995bb39e2f93cb9604c56fa777d5)
     - [字典排序 sorted](#ab7c2e3bc42c80125290e5763dcad146)
     - [迭代和组合](#7b6bcc5e50cc1ddd83a25620f5739920)
     - [bisect模块保持列表排序](#04539cb02f80127546f36cb81567946d)
     - [使用dict 和 set 测试成员](#8ef97ea188949155eb5ac819fdaa6330)
     - [url unescape](#18bf7f45d4c0960b7a240195d229cdbc)
     - [序列 ()](#1c65ec66e824c6ab4c57603cf633a25d)
     - [自省的核心 getattr 函数](#95cc82c5a8eea453d65f25f13121bd7c)
     - [callable](#765d2ec94553b7cf4c971e7dfcf0e851)
     - [dict get](#f3fb87677ab41e55ff2069660fddcebf)
     - [dict setdefault](#f911a4fc9f3eb152b05e1a9f4b9269a2)
     - [dict insection](#2292cf7bac8199cfa91cb22160b26f76)
     - [类型判断](#ab8027b580ee885ee2c146add9957e1c)
     - [方法内全部局部变量](#76a7e51a79a55462350aaed109577894)
     - [python 下划线变量](#379e1d911a58f6e847ad68e52703c7eb)
     - [re.sub group: number after \number](#8160fc3170b680fdd05d32a93937bcb9)
   - [数字进制转换](#4155a2d7d71ebf1611555bda413d2961)
     - [10进制数字 => 2,8,16进制字符串](#4b65978fe4cba7b22aecf6375e8737db)
     - [2,8,16进制字符串 ==> 10进制数字](#819934946947aa7e3778247b469c1e4c)
     - [格式化数字为16进制字符串](#44ecb2e9ff829c50b0b0f9f4e9f7b918)
   - [字符处理](#fa931b43907b0ba8b8616487e1a14097)
     - [ascii列表 -> 字符串](#47785be60ccbe583a8c3f8a1c3b80d00)
     - [编码](#cc6c35a3e0f97fb9747905dc13e9b625)
       - [char <-> ascii](#837e36b7cae11bd0e8b44252a6d61d1f)
       - [unichr  <-> unicode string](#8f9892ac178f204eda8bbf3961d55d42)
       - [unicode -> special encoded string](#97293b0a09ebeed137930a0ca33f6e3a)
       - [special encoded string -> unicode](#f9b40cb363b4e4cd89aa132855dd8d41)
   - [中文处理](#c4e5abc4816842dea936c9f1f20b431e)
     - [改变脚本本地编码](#7ab8dd9eb1e1a86afb68efff05a2e355)
     - [写 带中文字符的文件](#771f3b745b95ab3097fd1242137e2912)
   - [encrypt](#53c82eba31f6d416f331de9162ebe997)
     - [base64](#95a1446a7120e4af5c0c8878abb7e6d2)
     - [md5](#1bc29b36f623ba82aaf6724fd3b16718)
   - [Misc](#74248c725e00bf9fe04df4e35b249a19)
     - [try - except 打印错误](#636a8076c1d8da426394e0c3e15c3ec2)
     - [run in 32bit mode](#61ca7c49201549fda5414272579e0413)
     - [python 并行任务技巧](#eadbf8dd738ffd6eb430b8630c92d74c)
     - [profile](#7d97481b1fe66f4b51db90da7e794d9f)
     - [强制浮点数运算](#74343fa59d92ff47cbb14750228abd8f)
     - [输出一个对象各个成员的名称和值](#dd6b35cfcf7bc2919f28aaba9e65fa92)
     - [读取文件特定行](#210dd2176d44f2bd7f0c112101e62490)
     - [文件修改／创建时间](#4b373365b500e18ab7c0b8f5a83dc802)
     - [python 写 只读文件](#3fbb096fc383c2a61ad0a6685b17c0de)

...menuend


<h2 id="e7c8aa5b143e53ecad41b3612dab23ed"></h2>
# python tips

---

<h2 id="cd82da5cf3ee760792e950b087be3d29"></h2>
## 语法技巧

<h2 id="49bdb1b4a214a6bc00824eb4f7b2c5f1"></h2>
### eval 环境
   
eval() 默认使用当前环境的名字空间，也可以带入自定义字典

```
ns=dict(x=10,y=20)
eval("x+y" , ns )
```

还可以使用 exec 来执行一个代码段


<h2 id="f372cdc8f82db5bb3a311edc6743e412"></h2>
### 获取变量x的内存地址

```
id(x) 
```

<h2 id="5bd260e9c2d18f7f2ff4c30f274ebc6b"></h2>
### for i, v  枚举

```
for i, item in enumerate(  iterable ):
```

<h2 id="d4c8995bb39e2f93cb9604c56fa777d5"></h2>
### 数组排序

```
autodances.sort( key = lambda x  :  x["time"] , reverse = False )
```

use `cmp` method

```
l.sort(cmp=lambda x,y:cmp( x.lower(), y.lower()  ))
```

<h2 id="ab7c2e3bc42c80125290e5763dcad146"></h2>
### 字典排序 sorted

```
>>> d={"b":2, "a":3, "c":1}
>>> sorted(d)     #对 key 进行排序，输出一个key list
['a', 'b', 'c']      
>>> sorted(d.items())     #对key 进行排序，返回 元组 list
[('a', 3), ('b', 2), ('c', 1)]
>>> sorted(d.items() , key=lambda x:x[1])    # 对 值 进行排序， 返回 元组 list
[('c', 1), ('b', 2), ('a', 3)]
>>> sorted(d.items() , key=lambda x:x[1] , reverse = True )
[('a', 3), ('b', 2), ('c', 1)]
```


<h2 id="7b6bcc5e50cc1ddd83a25620f5739920"></h2>
### 迭代和组合

了解itertools模块：  该模块对迭代和组合是非常有效的

```
>>> import itertools 
>>> iter = itertools.permutations([1,2,3]) 
>>> list(iter) 
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

<h2 id="04539cb02f80127546f36cb81567946d"></h2>
### bisect模块保持列表排序

这是一个免费的二分查找实现和快速插入有序序列的工具。你已將一个元素插入列表中, 而你不需要再次调用 sort() 来保持容器的排序, 因为这在长序列中这会非常昂贵. 

```
>>> import bisect 
>>> bisect.insort(list, element) 
```

<h2 id="8ef97ea188949155eb5ac819fdaa6330"></h2>
### 使用dict 和 set 测试成员

hash实现, 查找效率可以达到O(1)

<h2 id="18bf7f45d4c0960b7a240195d229cdbc"></h2>
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



<h2 id="1c65ec66e824c6ab4c57603cf633a25d"></h2>
### 序列 ()  

速度比列表快，  可以作为字典关键字

<h2 id="95cc82c5a8eea453d65f25f13121bd7c"></h2>
### 自省的核心 getattr 函数

```
getattr(obj, name [ ,  default_method_return_if_not_exist ] )

example:

for i in  dir( obj ):
    method = getattr( obj, i   )
    print i , method
```

<h2 id="765d2ec94553b7cf4c971e7dfcf0e851"></h2>
### callable

```
methodList = [method for method in dir(object) if callable(getattr(object, method))]
```

<h2 id="f3fb87677ab41e55ff2069660fddcebf"></h2>
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

<h2 id="f911a4fc9f3eb152b05e1a9f4b9269a2"></h2>
### dict setdefault

dict 插入key-value时，如果key不存在，先初始化为默认值(一般用于value是list, dict 类型)

```
def addword2dict(word, pagenumber): 
    dict.setdefault(word, []).append(pagenumber)
```

<h2 id="2292cf7bac8199cfa91cb22160b26f76"></h2>
### dict insection

找出两个字典的交集 

```
print "Intersects:", [k for k in some_dict if k in another_dict]
```

速度上取胜:

```
print "Intersects:", filter(another_dict.has_key, some_dict.keys())
```


<h2 id="ab8027b580ee885ee2c146add9957e1c"></h2>
### 类型判断

```
isinstance(u'a', unicode)
```

<h2 id="76a7e51a79a55462350aaed109577894"></h2>
### 方法内全部局部变量

Python has a locals() function which gives you back a dictionary of local variables within the function

<h2 id="379e1d911a58f6e847ad68e52703c7eb"></h2>
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

<h2 id="8160fc3170b680fdd05d32a93937bcb9"></h2>
### re.sub group: number after \number

```
re.sub(r'(foo)', r'\g<1>123', 'foobar')
```

----------


---

<h2 id="4155a2d7d71ebf1611555bda413d2961"></h2>
## 数字进制转换

<h2 id="4b65978fe4cba7b22aecf6375e8737db"></h2>
### 10进制数字 => 2,8,16进制字符串

```
bin(123)  # 2
oct(18)   # 8
hex(10)   # 16
```

<h2 id="819934946947aa7e3778247b469c1e4c"></h2>
### 2,8,16进制字符串 ==> 10进制数字 

```
int('022',8)
```

<h2 id="44ecb2e9ff829c50b0b0f9f4e9f7b918"></h2>
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

<h2 id="fa931b43907b0ba8b8616487e1a14097"></h2>
## 字符处理

<h2 id="47785be60ccbe583a8c3f8a1c3b80d00"></h2>
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

<h2 id="cc6c35a3e0f97fb9747905dc13e9b625"></h2>
### 编码

<h2 id="837e36b7cae11bd0e8b44252a6d61d1f"></h2>
#### char <-> ascii

```
>>> print ord('a')
97
>>> print chr(97)
a
```

`'2' == '\x32' == '\062'`

<h2 id="8f9892ac178f204eda8bbf3961d55d42"></h2>
#### unichr  <-> unicode string

```
>>> print ord(u"我")
25105
>>> print unichr( 25105 )
我
```

<h2 id="97293b0a09ebeed137930a0ca33f6e3a"></h2>
#### unicode -> special encoded string

```
unicodestring = u"Hello world"
utf8string = unicodestring.encode("utf-8")
asciistring = unicodestring.encode("ascii")
isostring = unicodestring.encode("ISO-8859-1")
utf16string = unicodestring.encode("utf-16")
```

<h2 id="f9b40cb363b4e4cd89aa132855dd8d41"></h2>
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

<h2 id="c4e5abc4816842dea936c9f1f20b431e"></h2>
## 中文处理

<h2 id="7ab8dd9eb1e1a86afb68efff05a2e355"></h2>
### 改变脚本本地编码

```
reload(sys)
sys.setdefaultencoding('utf8') 
```

<h2 id="771f3b745b95ab3097fd1242137e2912"></h2>
### 写 带中文字符的文件

```
fp = codecs.open( target_sheet_name + '.txt'  , "w", "utf-8")
fp.write(jsonObj )
fp.close()
```

---

<h2 id="53c82eba31f6d416f331de9162ebe997"></h2>
## encrypt

<h2 id="95a1446a7120e4af5c0c8878abb7e6d2"></h2>
### base64

```
import base64
# base 64 decode
data = base64.b64decode( data ) 
# base64 encode
result_data = base64.b64encode( result_data)
```

<h2 id="1bc29b36f623ba82aaf6724fd3b16718"></h2>
### md5

```
>>> import md5
>>> m = md5.new()
>>> m.update("Nobody inspects")
>>> m.update(" the spammish repetition")
>>> m.digest()
```

---

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>
## Misc

<h2 id="636a8076c1d8da426394e0c3e15c3ec2"></h2>
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

<h2 id="61ca7c49201549fda5414272579e0413"></h2>
### run in 32bit mode

```
arch -i386 python2.7
```

<h2 id="eadbf8dd738ffd6eb430b8630c92d74c"></h2>
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

<h2 id="7d97481b1fe66f4b51db90da7e794d9f"></h2>
### profile

```
python -m cProfile  xxx.py
```

or

```
import profile
profile.run ( 'func_name')
```

<h2 id="74343fa59d92ff47cbb14750228abd8f"></h2>
### 强制浮点数运算

```
>>> from __future__ import division
>>> 1/2
0.5
```

<h2 id="dd6b35cfcf7bc2919f28aaba9e65fa92"></h2>
### 输出一个对象各个成员的名称和值

```
>>> g = lambda m: '\n'.join([ '%s=%s'%(k, repr(v)) for k, v in m.__dict__.iteritems() ])
>>> g(obj)
```
<h2 id="210dd2176d44f2bd7f0c112101e62490"></h2>
### 读取文件特定行

```
import linecache
#thefiepath             文件路径
#desired_line_number    整数，文件的特定行 
theline = linecache.getline(thefilepath, desired_line_number)
```        

<h2 id="4b373365b500e18ab7c0b8f5a83dc802"></h2>
### 文件修改／创建时间

```
import   os,time 
time.ctime(os.stat( "d:/learn/flash.txt ").st_mtime)   #文件的修改时间 
time.ctime(os.stat( "d:/learn/flash.txt ").st_ctime)   #文件的创建时间
```

<h2 id="3fbb096fc383c2a61ad0a6685b17c0de"></h2>
### python 写 只读文件

读之前：

```
os.chmod(_path,  stat.S_IREAD)
```

写之前:

```
os.chmod(_path, stat.S_IWRITE | stat.S_IREAD)
```
