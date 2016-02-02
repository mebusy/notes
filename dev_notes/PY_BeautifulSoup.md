...menustart

 * [BeautifulSoup](#c2ed0329d2d3cf54c78317b209d7c0d5)

	 * [bs 解析器](#06129a15a17f5bf8197a5a520e00a2cb)

	 * [对象的种类](#5316642266b09c1a37c74751ff570d00)

		 * [Tag](#c101058e7ea21bbbf2a5ac893088e90b)

 * [<class 'bs4.element.Tag'>](#379d263ac1f13fadf734576b207158f8)

			 * [Name](#49ee3087348e8d44e1feda1917443987)

 * [u'b'](#f3e42ecd2dbeec820b77af8f68e9afbe)

 * [<blockquote class="boldest">Extremely bold</blockquote>](#48eb0f7e0c8e683b47ce8398badc11d1)

			 * [Attributes](#287234a1ff35a314b5b6bc4e5828e745)

 * [u'boldest'](#818569ae898d77e819a49412dd3b36a2)

 * [{u'class': u'boldest'}](#6448c52afd2e39bd286642d013285e74)

				 * [多值属性](#f7c0b37da30bc4400b27198d2caf96f3)

 * [["body", "strikeout"]](#4ff388748a2fa6927182b872cd9f7962)

 * [["body"]](#bf8ad6bae11a712db6b4453016568d02)

 * ['my id'](#e9659ecbca012d8de395626344f935fb)

 * [u'body strikeout'](#bdbd95bc564c4e441f20eaf28120c5ea)

		 * [NavigableString 可以遍历的字符串](#379f03de69572c4d3aa54f8f8650f428)

 * [u'Extremely bold'](#c82db753232850157341caacbc6688b0)

 * [<class 'bs4.element.NavigableString'>](#852b6fadd30b225f6edd871b29131169)

 * [< blockquote >No longer bold</blockquote>](#7b4221a2d88e18c0c299a70bf53550b6)

		 * [BeautifulSoup](#c2ed0329d2d3cf54c78317b209d7c0d5)

 * [u'[document]'](#7b673885f8969d7917218b16ef51995d)

		 * [Comment 注释及特殊字符串](#0753968b4545fc501a4836fa6f324d04)

 * [<class 'bs4.element.Comment'>](#eaa59af538a938f563bc19a0979fc6d3)

 * [u'Hey, buddy. Want to buy a used parser'](#87d72d6f148478325d340583844ab545)

 * [< b >](#9fbd1472479a2c39613ab7f747f3a0d8)

 * [<![CDATA[A CDATA block]]>](#33c3a5339e8b45e4684f12903e087128)

 * [</b>](#5504ceea91e62031eccf9496eab44be7)

	 * [遍历文档树](#8e18b129f83a9689f747b1880e12ed33)

		 * [子节点](#315dcc9412a4499cf846736fdbaaa72a)

			 * [tag的名字](#974c48224a70145276128073c7c0b3e4)

 * [< b >The Dormouse's story</b>](#62bcc1918f92e442d7eb21df03512159)

 * [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>](#ce92f9e762eed98a5ff4e887ed5f9535)

 * [[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,](#dc437075ca01733bb6f67e3525b5bda5)

 * [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,](#ae47fe3861171e4ceef3c831a4d6ff5c)

 * [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]](#e3b53f78f3cf4c376d5d53403fcd00be)

			 * [.contents 和 .children 和 .descendants](#5ef69ba35fbd6c33a99a7bdc5c5992b1)

 * [[< title >The Dormouse's story</title>]](#c803a9044d0ac57ef4b8134c9af117ca)

			 * [.string](#826098db4d2fd79ad3b0ea00dc4424f8)

 * [u'The Dormouse's story'](#e0d478b67daac7d4b47b40003b94e605)

 * [[< title >The Dormouse's story</title>]](#c803a9044d0ac57ef4b8134c9af117ca)

 * [u'The Dormouse's story'](#e0d478b67daac7d4b47b40003b94e605)

 * [None](#6adf97f83acf6453d4a6a4b1070f3754)

			 * [.strings 和 stripped_strings](#f0f015a1c0a337a26cd3e058a356728e)

		 * [父节点](#50200948c0bbd9d2770e21cff2b43d01)

			 * [.parent](#7e9024fe9b16b6df01cb1178eccde435)

 * [< title >The Dormouse's story</title>](#a41741141f985f9447cf086d4e2f191b)

 * [< head >< title >The Dormouse's story</title></head>](#646b4d124f5facdc0d7ed1c6c9f76ea5)

			 * [.parents](#f84b68a3ba6dbdd825f4d2d61556be28)

 * [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>](#ce92f9e762eed98a5ff4e887ed5f9535)

 * [p](#83878c91171338902e0fe0fb97a8c47a)

 * [body](#841a2d689ad86bd1611447453c22c6fc)

 * [html](#fc35fdc70d5fc69d269883a822c7a53e)

 * [[document]](#3f45e7bbe073d6872606e0c892e60e9a)

 * [None](#6adf97f83acf6453d4a6a4b1070f3754)

		 * [兄弟节点](#6fa498651667a0c6b50860e2a59b3747)

			 * [.next_sibling 和 .previous_sibling](#0ab728758563d908f3cfd5c256c58368)

 * [< c >text2</c>](#77483548a9e589ca5534164e9d9e5e44)

 * [< b >text1</b>](#d74b99a05dd9960267afc595d6a729da)

			 * [.next_siblings 和 .previous_siblings](#78e321b204d8e94aad526caa22ccf129)

		 * [回退和前进](#2b1854c45093976077cd9e7e92817f93)

			 * [.next_element 和 .previous_element](#5f9f6a3e9a16fa700480d0adf0f83049)

			 * [.next_elements 和 .previous_elements](#f575adec86f5ee8b708ad4844c4809e9)

	 * [搜索文档树](#891834dc47e736b404e84e1fc9067127)

		 * [过滤器](#04bd0c61c9045f9144991ea380edbf3d)

			 * [字符串](#cc4dd1da7e1a754534215f02fb9ba85d)

 * [[< b >The Dormouse's story</b>]](#52c367baefec41d1cb18180ffc2edc25)

			 * [正则表达式](#2e576047ae509e55d8e86f36d730caf4)

			 * [列表](#3712972d84adf48acbd6ad24b4d75ad0)

 * [[< b >The Dormouse's story</b>,](#e9c3371eea86fc07cd5de26424688080)

 * [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,](#333e89849c4a0be964748acb7b45b155)

 * [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,](#ae47fe3861171e4ceef3c831a4d6ff5c)

 * [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]](#e3b53f78f3cf4c376d5d53403fcd00be)

			 * [True](#f827cf462f62848df37c5e1e94a4da74)

 * [html](#fc35fdc70d5fc69d269883a822c7a53e)

 * [head](#96e89a298e0a9f469b9ae458d6afae9f)

 * [title](#d5d3db1765287eef77d7927cc956f50a)

 * [body](#841a2d689ad86bd1611447453c22c6fc)

 * [p](#83878c91171338902e0fe0fb97a8c47a)

 * [b](#92eb5ffee6ae2fec3ad71c777531578f)

 * [p](#83878c91171338902e0fe0fb97a8c47a)

 * [a](#0cc175b9c0f1b6a831c399e269772661)

 * [a](#0cc175b9c0f1b6a831c399e269772661)

 * [a](#0cc175b9c0f1b6a831c399e269772661)

 * [p](#83878c91171338902e0fe0fb97a8c47a)

			 * [方法](#ea340b9dda8b893ddf2d9176220aac32)

		 * [find_all( name , attrs , recursive , text , **kwargs )](#9e9956ecd644adb40afec6ad79df7c4b)

			 * [name 参数](#620c64f80d81ac35f42b9200016164a5)

 * [[< title >The Dormouse's story</title>]](#c803a9044d0ac57ef4b8134c9af117ca)

			 * [keyword 参数 和 attrs](#7cd7d7c7f2d3bb007817c6c4d9ed06c6)

 * [[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]](#890ae64a45fd0ea294bc06f6bde22965)

 * [[<a class="sister" href="http://example.com/elsie" id="link1">three</a>]](#d0936af75a47dac228704ed07c987a9d)

 * [SyntaxError: keyword can't be an expression](#c01711c9a1216a6946f5323899fc8f9a)

 * [[<div data-foo="value">foo!</div>]](#419d9ef5cdb0be8566b3bd7a21098bf2)

			 * [按CSS搜索](#0317b50465de46c94b7d444218895e08)

 * [[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,](#dc437075ca01733bb6f67e3525b5bda5)

 * [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,](#ae47fe3861171e4ceef3c831a4d6ff5c)

 * [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]](#e3b53f78f3cf4c376d5d53403fcd00be)

 * [[<p class="body strikeout"></p>]](#7986c0da21818b08c1e8ef4708d03b63)

 * [[<p class="body strikeout"></p>]](#7986c0da21818b08c1e8ef4708d03b63)

			 * [text 参数](#b85ff64b46933e9f70850eb0d1c182a8)

			 * [limit 参数](#3b7c4439f88ee8659212d7d097af17ba)

 * [[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,](#dc437075ca01733bb6f67e3525b5bda5)

 * [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]](#ffb43f8496d2f195a26d74537d1fd9a9)

			 * [recursive 参数](#dfb1da32cfedce18e06febd3de8dfaa1)

		 * [像调用 find_all() 一样调用tag](#e87c304af3b634dd48a0c133d8f2d834)

		 * [find( name , attrs , recursive , text , **kwargs )](#eddd24d106b00f012296abf15aecdf7a)

 * [< title >The Dormouse's story</title>](#a41741141f985f9447cf086d4e2f191b)

		 * [find_parents() 和 find_parent()](#9a1af792c8edfcf1821778b793c1de1c)

		 * [find_next_siblings() 合 find_next_sibling()](#f0de90db60172672a319539d3c33328b)

		 * [find_previous_siblings() 和 find_previous_sibling()](#c287dbef8cf91421167b4294673a0540)

		 * [find_all_next() 和 find_next()](#aca730699d61e6508ac53886823adabb)

		 * [find_all_previous() 和 find_previous()](#a9427ebd054cb5e6b4869a2d711399c4)

		 * [CSS选择器](#4dab32e8ec6a7a43a9adb0fedaaa7afb)

	 * [修改 soup 文档](#f2fb137262eb44eb2a60a3a1858187f5)

		 * [get_text()](#13f7d242b154ae0c680ecf7cfb1acf7f)


...menuend



[markdown版本](https://www.zybuluo.com/qibinyi/note/208683)

<h2 id="c2ed0329d2d3cf54c78317b209d7c0d5"></h2>
# BeautifulSoup

    bs 使用 Unicode编码 
    

<h2 id="06129a15a17f5bf8197a5a520e00a2cb"></h2>
## bs 解析器

除了标准的 "html.parser" 解析器, 还支持第三方解析器：

**"lxml" (推荐) , "xml"**

```bash
    sudo pip install lxml	
```

**"html5lib"**
```bash
	sudo pip install html5lib
```


<h2 id="5316642266b09c1a37c74751ff570d00"></h2>
## 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: 
**Tag , NavigableString , BeautifulSoup , Comment**

<h2 id="c101058e7ea21bbbf2a5ac893088e90b"></h2>
### Tag

```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
<h2 id="379d263ac1f13fadf734576b207158f8"></h2>
# <class 'bs4.element.Tag'>
```

tag中最重要的属性: name和attributes

<h2 id="49ee3087348e8d44e1feda1917443987"></h2>
#### Name

每个tag都有自己的名字,通过 .name 来获取:
```python
tag.name
<h2 id="f3e42ecd2dbeec820b77af8f68e9afbe"></h2>
# u'b'
```

如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:
```python
tag.name = "blockquote"
tag
<h2 id="48eb0f7e0c8e683b47ce8398badc11d1"></h2>
# <blockquote class="boldest">Extremely bold</blockquote>
```


<h2 id="287234a1ff35a314b5b6bc4e5828e745"></h2>
#### Attributes

一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:
```python
tag['class']
<h2 id="818569ae898d77e819a49412dd3b36a2"></h2>
# u'boldest'
```

也可以直接”点”取属性, 比如: .attrs :

```python
tag.attrs
<h2 id="6448c52afd2e39bd286642d013285e74"></h2>
# {u'class': u'boldest'}
```

tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样


<h2 id="f7c0b37da30bc4400b27198d2caf96f3"></h2>
##### 多值属性

HTML 4定义了一系列可以包含多个值的属性. 
在HTML5中移除了一些,却增加更多.最常见的多值的属性是 class (一个tag可以有多个CSS的class). 还有一些属性 rel , rev , accept-charset , headers , accesskey .  
在Beautiful Soup中多值属性的返回类型是list:

```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
<h2 id="4ff388748a2fa6927182b872cd9f7962"></h2>
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
<h2 id="bf8ad6bae11a712db6b4453016568d02"></h2>
# ["body"]
```

如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
```python
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
<h2 id="e9659ecbca012d8de395626344f935fb"></h2>
# 'my id'
```

如果转换的文档是XML格式,那么tag中不包含多值属性
```python
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
<h2 id="bdbd95bc564c4e441f20eaf28120c5ea"></h2>
# u'body strikeout'
```

<h2 id="379f03de69572c4d3aa54f8f8650f428"></h2>
### NavigableString 可以遍历的字符串

字符串常被包含在tag内. 
Beautiful Soup用 NavigableString 类来包装tag中的字符串:

```python
tag.string
<h2 id="c82db753232850157341caacbc6688b0"></h2>
# u'Extremely bold'
type(tag.string)
<h2 id="852b6fadd30b225f6edd871b29131169"></h2>
# <class 'bs4.element.NavigableString'>
```

注意tag.string 和 tag.text 的不同

    tag.string    bs4.element.NavigableString
    tag.text      unicode

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:

```python
tag.string.replace_with("No longer bold")
tag
<h2 id="7b4221a2d88e18c0c299a70bf53550b6"></h2>
# < blockquote >No longer bold</blockquote>
```

<h2 id="c2ed0329d2d3cf54c78317b209d7c0d5"></h2>
### BeautifulSoup

BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象.
因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name

```python
soup.name
<h2 id="7b673885f8969d7917218b16ef51995d"></h2>
# u'[document]'
```

<h2 id="0753968b4545fc501a4836fa6f324d04"></h2>
### Comment 注释及特殊字符串

Comment 对象是一个特殊类型的 NavigableString 对象:

```python
markup = "< b ><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)
<h2 id="eaa59af538a938f563bc19a0979fc6d3"></h2>
# <class 'bs4.element.Comment'>

comment
<h2 id="87d72d6f148478325d340583844ab545"></h2>
# u'Hey, buddy. Want to buy a used parser'
```

Beautiful Soup中定义的其它类型都可能会出现在XML的文档中: CData , ProcessingInstruction , Declaration , Doctype .与 Comment 对象类似,这些类都是 NavigableString 的子类,只是添加了一些额外的方法的字符串独享.下面是用CDATA来替代注释的例子:

```python
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())
<h2 id="9fbd1472479a2c39613ab7f747f3a0d8"></h2>
# < b >
<h2 id="33c3a5339e8b45e4684f12903e087128"></h2>
#  <![CDATA[A CDATA block]]>
<h2 id="5504ceea91e62031eccf9496eab44be7"></h2>
# </b>
```

<h2 id="8e18b129f83a9689f747b1880e12ed33"></h2>
## 遍历文档树

<h2 id="315dcc9412a4499cf846736fdbaaa72a"></h2>
### 子节点

一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点. 
Beautiful Soup提供了许多操作和遍历子节点的属性.

    注意: Beautiful Soup中字符串节点不支持这些属性,因为字符串没有子节点

<h2 id="974c48224a70145276128073c7c0b3e4"></h2>
#### tag的名字

操作文档树最简单的方法就是告诉它你想获取的tag的name.
下面的代码可以获取< body >标签中的第一个< b >标签:
```python
soup.body.b
<h2 id="62bcc1918f92e442d7eb21df03512159"></h2>
# < b >The Dormouse's story</b>
```

通过点取属性的方式只能获得当前名字的第一个tag:
```python
soup.a
<h2 id="ce92f9e762eed98a5ff4e887ed5f9535"></h2>
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

如果想要得到所有的< a >标签,或是通过名字得到比*一个tag*更多的内容的时候, 
就需要用到 Searching the tree 中描述的方法,比如: find_all()

```python
soup.find_all('a')
<h2 id="dc437075ca01733bb6f67e3525b5bda5"></h2>
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<h2 id="ae47fe3861171e4ceef3c831a4d6ff5c"></h2>
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
<h2 id="e3b53f78f3cf4c376d5d53403fcd00be"></h2>
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

<h2 id="5ef69ba35fbd6c33a99a7bdc5c5992b1"></h2>
#### .contents 和 .children 和 .descendants

tag的 .contents 属性可以将tag的子节点以列表的方式输出:
通过tag的 .children 生成器,可以对tag的子节点进行循环:


.contents 和 .children属性仅包含tag的直接子节点. 例如,< head >标签只有一个直接子节点< title >

```python
head_tag.contents
<h2 id="c803a9044d0ac57ef4b8134c9af117ca"></h2>
# [< title >The Dormouse's story</title>]
```

但是< title >标签也包含一个子节点:字符串 “The Dormouse’s story”,这种情况下字符串 “The Dormouse’s story”也属于< head >标签的子孙节点. .descendants 属性可以对所有tag的子孙节点进行递归循环 [5] :

```python
for child in head_tag.descendants:
    print(child)
    # < title >The Dormouse's story</title>
    # The Dormouse's story
```

<h2 id="826098db4d2fd79ad3b0ea00dc4424f8"></h2>
#### .string

如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
```python
title_tag.string
<h2 id="e0d478b67daac7d4b47b40003b94e605"></h2>
# u'The Dormouse's story'
```

如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
```python
head_tag.contents
<h2 id="c803a9044d0ac57ef4b8134c9af117ca"></h2>
# [< title >The Dormouse's story</title>]

head_tag.string
<h2 id="e0d478b67daac7d4b47b40003b94e605"></h2>
# u'The Dormouse's story'
```

如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
```python
print(soup.html.string)
<h2 id="6adf97f83acf6453d4a6a4b1070f3754"></h2>
# None
```

<h2 id="f0f015a1c0a337a26cd3e058a356728e"></h2>
#### .strings 和 stripped_strings

如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:
```python
for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
    # u'Once upon a time there were three little sisters; and their names were\n'
    # u'Elsie'
    # u',\n'
    # u'Lacie'
    # u' and\n'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'\n\n'
    # u'...'
    # u'\n'
````

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
```python
for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
    # u'Once upon a time there were three little sisters; and their names were'
    # u'Elsie'
    # u','
    # u'Lacie'
    # u'and'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'...'
```    

<h2 id="50200948c0bbd9d2770e21cff2b43d01"></h2>
### 父节点

<h2 id="7e9024fe9b16b6df01cb1178eccde435"></h2>
#### .parent

通过 .parent 属性来获取某个元素的父节点.在例子“爱丽丝”的文档中,< head >标签是< title >标签的父节点:
```python
title_tag = soup.title
title_tag
<h2 id="a41741141f985f9447cf086d4e2f191b"></h2>
# < title >The Dormouse's story</title>
title_tag.parent
<h2 id="646b4d124f5facdc0d7ed1c6c9f76ea5"></h2>
# < head >< title >The Dormouse's story</title></head>
```

<h2 id="f84b68a3ba6dbdd825f4d2d61556be28"></h2>
#### .parents

通过元素的 .parents 属性可以递归得到元素的所有父辈节点,下面的例子使用了 .parents 方法遍历了< a >标签到根节点的所有节点.
```python
link = soup.a
link
<h2 id="ce92f9e762eed98a5ff4e887ed5f9535"></h2>
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
<h2 id="83878c91171338902e0fe0fb97a8c47a"></h2>
# p
<h2 id="841a2d689ad86bd1611447453c22c6fc"></h2>
# body
<h2 id="fc35fdc70d5fc69d269883a822c7a53e"></h2>
# html
<h2 id="3f45e7bbe073d6872606e0c892e60e9a"></h2>
# [document]
<h2 id="6adf97f83acf6453d4a6a4b1070f3754"></h2>
# None
```

<h2 id="6fa498651667a0c6b50860e2a59b3747"></h2>
### 兄弟节点

```python
sibling_soup = BeautifulSoup("< a >< b >text1</b>< c >text2</c></b></a>")
```

<h2 id="0ab728758563d908f3cfd5c256c58368"></h2>
#### .next_sibling 和 .previous_sibling

在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
```python
sibling_soup.b.next_sibling
<h2 id="77483548a9e589ca5534164e9d9e5e44"></h2>
# < c >text2</c>

sibling_soup.c.previous_sibling
<h2 id="d74b99a05dd9960267afc595d6a729da"></h2>
# < b >text1</b>
```

<h2 id="78e321b204d8e94aad526caa22ccf129"></h2>
#### .next_siblings 和 .previous_siblings

通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出:


<h2 id="2b1854c45093976077cd9e7e92817f93"></h2>
### 回退和前进

<h2 id="5f9f6a3e9a16fa700480d0adf0f83049"></h2>
#### .next_element 和 .previous_element

.next_element 属性指向解析过程中下一个被解析的对象(字符串或tag),结果可能与 .next_sibling 相同,但通常是不一样的.

<h2 id="f575adec86f5ee8b708ad4844c4809e9"></h2>
#### .next_elements 和 .previous_elements

通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样:


<h2 id="891834dc47e736b404e84e1fc9067127"></h2>
## 搜索文档树

Beautiful Soup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all() .其它方法的参数和用法类似,请读者举一反三.

使用 find_all() 类似的方法可以查找到想要查找的文档内容

<h2 id="04bd0c61c9045f9144991ea380edbf3d"></h2>
### 过滤器

介绍 find_all() 方法前,先介绍一下过滤器的类型,这些过滤器贯穿整个搜索的API. 
过滤器可以被用在tag的name中,节点的属性中,字符串中或他们的混合中.

    过滤器中的查找例子，都是查找 tag

<h2 id="cc4dd1da7e1a754534215f02fb9ba85d"></h2>
#### 字符串

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的< b >标签:
```python
soup.find_all('b')
<h2 id="52c367baefec41d1cb18180ffc2edc25"></h2>
# [< b >The Dormouse's story</b>]
```

<h2 id="2e576047ae509e55d8e86f36d730caf4"></h2>
#### 正则表达式

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容. 
下面例子中找出所有以b开头的标签,这表示< body >和< b >标签都应该被找到:
```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
```

下面代码找出所有名字中包含”t”的标签:
```python
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
```

    注意一下这里和 字符串过滤器的区别

<h2 id="3712972d84adf48acbd6ad24b4d75ad0"></h2>
#### 列表

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回. 
下面代码找到文档中所有< a >标签和< b >标签:
    
```python
soup.find_all(["a", "b"])
<h2 id="e9c3371eea86fc07cd5de26424688080"></h2>
# [< b >The Dormouse's story</b>,
<h2 id="333e89849c4a0be964748acb7b45b155"></h2>
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<h2 id="ae47fe3861171e4ceef3c831a4d6ff5c"></h2>
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
<h2 id="e3b53f78f3cf4c376d5d53403fcd00be"></h2>
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

<h2 id="f827cf462f62848df37c5e1e94a4da74"></h2>
#### True

True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
```python
for tag in soup.find_all(True):
    print(tag.name)
<h2 id="fc35fdc70d5fc69d269883a822c7a53e"></h2>
# html
<h2 id="96e89a298e0a9f469b9ae458d6afae9f"></h2>
# head
<h2 id="d5d3db1765287eef77d7927cc956f50a"></h2>
# title
<h2 id="841a2d689ad86bd1611447453c22c6fc"></h2>
# body
<h2 id="83878c91171338902e0fe0fb97a8c47a"></h2>
# p
<h2 id="92eb5ffee6ae2fec3ad71c777531578f"></h2>
# b
<h2 id="83878c91171338902e0fe0fb97a8c47a"></h2>
# p
<h2 id="0cc175b9c0f1b6a831c399e269772661"></h2>
# a
<h2 id="0cc175b9c0f1b6a831c399e269772661"></h2>
# a
<h2 id="0cc175b9c0f1b6a831c399e269772661"></h2>
# a
<h2 id="83878c91171338902e0fe0fb97a8c47a"></h2>
# p
```


<h2 id="ea340b9dda8b893ddf2d9176220aac32"></h2>
#### 方法

如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 , 
如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False

下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:
```python
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
```

下面代码找到所有被文字包含的节点内容:
```python
from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print tag.name
```


<h2 id="9e9956ecd644adb40afec6ad79df7c4b"></h2>
### find_all( name , attrs , recursive , text , **kwargs )


<h2 id="620c64f80d81ac35f42b9200016164a5"></h2>
#### name 参数

name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.

简单的用法如下:
```python
soup.find_all("title")
<h2 id="c803a9044d0ac57ef4b8134c9af117ca"></h2>
# [< title >The Dormouse's story</title>]
```

    重申: 搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True .

<h2 id="7cd7d7c7f2d3bb007817c6c4d9ed06c6"></h2>
#### keyword 参数 和 attrs

如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作 *指定名字tag的属性* 来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
```python
soup.find_all(id='link2')
<h2 id="890ae64a45fd0ea294bc06f6bde22965"></h2>
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

    搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True .

使用多个指定名字的参数可以同时过滤tag的多个属性:
```python
soup.find_all(href=re.compile("elsie"), id='link1')
<h2 id="d0936af75a47dac228704ed07c987a9d"></h2>
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
```

有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
```python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(data-foo="value")
<h2 id="c01711c9a1216a6946f5323899fc8f9a"></h2>
# SyntaxError: keyword can't be an expression
```

但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
```python
data_soup.find_all(attrs={"data-foo": "value"})
<h2 id="419d9ef5cdb0be8566b3bd7a21098bf2"></h2>
# [<div data-foo="value">foo!</div>]
```

<h2 id="0317b50465de46c94b7d444218895e08"></h2>
#### 按CSS搜索

按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误. 
从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:

```python
soup.find_all("a", class_="sister")
<h2 id="dc437075ca01733bb6f67e3525b5bda5"></h2>
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<h2 id="ae47fe3861171e4ceef3c831a4d6ff5c"></h2>
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
<h2 id="e3b53f78f3cf4c376d5d53403fcd00be"></h2>
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

    class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :

tag的 class 属性是 多值属性. 
按照CSS类名搜索tag时,可以分别搜索tag中的每个CSS类名:
```python
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.find_all("p", class_="strikeout")
<h2 id="7986c0da21818b08c1e8ef4708d03b63"></h2>
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
<h2 id="7986c0da21818b08c1e8ef4708d03b63"></h2>
# [<p class="body strikeout"></p>]
```

<h2 id="b85ff64b46933e9f70850eb0d1c182a8"></h2>
#### text 参数
通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, 

    text 参数接受 字符串 , 正则表达式 , 列表, True . 看例子:

<h2 id="3b7c4439f88ee8659212d7d097af17ba"></h2>
#### limit 参数

find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

```python
soup.find_all("a", limit=2)
<h2 id="dc437075ca01733bb6f67e3525b5bda5"></h2>
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<h2 id="ffb43f8496d2f195a26d74537d1fd9a9"></h2>
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

<h2 id="dfb1da32cfedce18e06febd3de8dfaa1"></h2>
#### recursive 参数

调用tag的 find_all() 方法时, Beautiful Soup会检索当前tag的所有子孙节点, 
如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

<h2 id="e87c304af3b634dd48a0c133d8f2d834"></h2>
### 像调用 find_all() 一样调用tag

find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用, 
这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:

```python
soup.find_all("a")
soup("a")
```

这两行代码也是等价的:

```python
soup.title.find_all(text=True)
soup.title(text=True)
```


<h2 id="eddd24d106b00f012296abf15aecdf7a"></h2>
### find( name , attrs , recursive , text , **kwargs )

find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.

find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .

下面的方法等价

```python
soup.head.title
<h2 id="a41741141f985f9447cf086d4e2f191b"></h2>
# < title >The Dormouse's story</title>
soup.find("head").find("title")
```

    tag 作为方法调用 等价 findall， tag 作为 键值调用 等价 find

<h2 id="9a1af792c8edfcf1821778b793c1de1c"></h2>
### find_parents() 和 find_parent()

find_parents( name , attrs , recursive , text , **kwargs )
find_parent( name , attrs , recursive , text , **kwargs )

搜索父辈节点的方法实际上就是对 .parents 属性的迭代搜索.


<h2 id="f0de90db60172672a319539d3c33328b"></h2>
### find_next_siblings() 合 find_next_sibling()

这2个方法通过 .next_siblings 属性对当tag的所有后面解析的兄弟tag节点进行迭代


<h2 id="c287dbef8cf91421167b4294673a0540"></h2>
### find_previous_siblings() 和 find_previous_sibling()

这2个方法通过 .previous_siblings 属性对当前tag的前面解析的兄弟tag节点进行迭代

<h2 id="aca730699d61e6508ac53886823adabb"></h2>
### find_all_next() 和 find_next()

这2个方法通过 .next_elements 属性对当前tag的之后的tag和字符串进行迭代

<h2 id="a9427ebd054cb5e6b4869a2d711399c4"></h2>
###find_all_previous() 和 find_previous()

这2个方法通过 .previous_elements 属性对当前节点前面的tag和字符串进行迭代

<h2 id="4dab32e8ec6a7a43a9adb0fedaaa7afb"></h2>
### CSS选择器

Beautiful Soup支持大部分的CSS选择器,在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,即可使用CSS选择器的语法找到tag:

<h2 id="f2fb137262eb44eb2a60a3a1858187f5"></h2>
## 修改 soup 文档

<h2 id="13f7d242b154ae0c680ecf7cfb1acf7f"></h2>
### get_text() 

指定tag的文本内容的分隔符，去除获得文本内容的前后空白
soup.get_text("|", strip=True)

和 使用 .stripped_strings 生成器 效果差不多

