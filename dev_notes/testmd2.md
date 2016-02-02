...menustart

 * [Cmd Markdown 简明语法手册](#cbd31fa88ec252c7ec799a5f22cb3428)

		 * [1. 斜体和粗体](#eafb5a1f4e29e79bd2d2169a4104c96a)

		 * [2. 分级标题](#0a8ed7e3d7819b835481b9340a568bf2)

		 * [这是一个三级标题](#268581c78e71a2b005413ee989be3a46)

		 * [3. 外链接](#7135a8e1cd795cade72eba16ffdc7b2c)

		 * [4. 无序列表](#55181f6cad9736ac6dfa10f7b5c64f54)

		 * [5. 有序列表](#e9d089bcd0c9ca48ea1eb1560e84371c)

		 * [6. 文字引用](#15e3a6a3315f6f34e6464006b298ffc7)

		 * [7. 行内代码块](#c9be93a1cf7680b89f44ef942fc88909)

		 * [8.  代码块](#f66244c7004e030787af6ef182c2c241)

		 * [9.  插入图像](#a391373de1d10c79bdb13d953dd25808)

 * [Cmd Markdown 高阶语法手册](#93b060f03f70af5214a4a58e7d875250)

		 * [1. 内容目录](#a278c0f5772094d44371bf390b83fc46)

		 * [2. 标签分类](#abe60f5c6373cd801b2b3979c6c1ded6)

		 * [3. 删除线](#11efd56d3ea6e1cd6e0d70b622859719)

		 * [4. 注脚](#abb57f6b445af4f04b8d38b5f8efd210)

		 * [5. LaTeX 公式](#3009098fd39467289ee3ef379d7fec12)

		 * [6. 加强的代码块](#f9c6179b667c4229ad7e6aefd14e63da)

		 * [7. 流程图](#83d366b19e9953a74054eb9650424d34)

			 * [示例](#1a63ac23010e0573f7c0a8cd3314b8c6)

			 * [更多语法参考：[流程图语法参考](http://adrai.github.io/flowchart.js/)](#2464aee80728b47972620af84bf42491)

		 * [8. 序列图](#7f5551010a04c9080e1ec1ed029284bd)

			 * [示例 1](#1ee999b7a746baaeeefdac41f3d74e44)

			 * [示例 2](#3569926cb0d361708ef53bb49cdca79c)

			 * [更多语法参考：[序列图语法参考](http://bramp.github.io/js-sequence-diagrams/)](#87e764078b7c9de48e613888bd50f03f)

		 * [9. 表格支持](#74e7c8676cb7b4fd2694d308fc2f747d)

		 * [10. 定义型列表](#d1fa7e0d898e85ff862ec5eb0b8ddf2d)

		 * [11. Html 标签](#b31600d3a53dbc9f1ba3762e6688e33c)

		 * [12. 内嵌图标](#3fe816834026984092deb8bb5259c4f0)

		 * [13. 待办事宜 Todo 列表](#4a98422efd774fe54e88575df012b823)


...menuend


[『Cmd 技术渲染的沙箱页面，点击此处编写自己的文档』](https://www.zybuluo.com/mdeditor "作业部落旗下 Cmd 在线 Markdown 编辑阅读器")

<h2 id="cbd31fa88ec252c7ec799a5f22cb3428"></h2>
# Cmd Markdown 简明语法手册

标签： Cmd-Markdown

---

<h2 id="eafb5a1f4e29e79bd2d2169a4104c96a"></h2>
### 1. 斜体和粗体

使用 * 和 ** 表示斜体和粗体。

示例：

这是 *斜体*，这是 **粗体**。

<h2 id="0a8ed7e3d7819b835481b9340a568bf2"></h2>
### 2. 分级标题

使用 === 表示一级标题，使用 --- 表示二级标题。

示例：

```
这是一个一级标题
============================

这是一个二级标题
--------------------------------------------------

<h2 id="268581c78e71a2b005413ee989be3a46"></h2>
### 这是一个三级标题
```

你也可以选择在行首加井号表示不同级别的标题 (H1-H6)，例如：# H1, ## H2, ### H3，#### H4。

<h2 id="7135a8e1cd795cade72eba16ffdc7b2c"></h2>
### 3. 外链接

使用 \[描述](链接地址) 为文字增加外链接。

示例：

这是去往 [本人博客](http://ghosertblog.github.com) 的链接。

<h2 id="55181f6cad9736ac6dfa10f7b5c64f54"></h2>
### 4. 无序列表

使用 *，+，- 表示无序列表。

示例：

- 无序列表项 一
- 无序列表项 二
- 无序列表项 三

<h2 id="e9d089bcd0c9ca48ea1eb1560e84371c"></h2>
### 5. 有序列表

使用数字和点表示有序列表。

示例：

1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三

<h2 id="15e3a6a3315f6f34e6464006b298ffc7"></h2>
### 6. 文字引用

使用 > 表示文字引用。

示例：

> 野火烧不尽，春风吹又生。

<h2 id="c9be93a1cf7680b89f44ef942fc88909"></h2>
### 7. 行内代码块

使用 \`代码` 表示行内代码块。

示例：

让我们聊聊 `html`。

<h2 id="f66244c7004e030787af6ef182c2c241"></h2>
### 8.  代码块

使用 四个缩进空格 表示代码块。

示例：

    这是一个代码块，此行左侧有四个不可见的空格。

<h2 id="a391373de1d10c79bdb13d953dd25808"></h2>
### 9.  插入图像

使用 \!\[描述](图片链接地址) 插入图像。

示例：

![我的头像](https://www.zybuluo.com/static/img/my_head.jpg)

<h2 id="93b060f03f70af5214a4a58e7d875250"></h2>
# Cmd Markdown 高阶语法手册

<h2 id="a278c0f5772094d44371bf390b83fc46"></h2>
### 1. 内容目录

在段落中填写 `[TOC]` 以显示全文内容的目录结构。

[TOC]

<h2 id="abe60f5c6373cd801b2b3979c6c1ded6"></h2>
### 2. 标签分类

在编辑区任意行的列首位置输入以下代码给文稿标签：

标签： 数学 英语 Markdown

或者

Tags： 数学 英语 Markdown

<h2 id="11efd56d3ea6e1cd6e0d70b622859719"></h2>
### 3. 删除线

使用 ~~ 表示删除线。

~~这是一段错误的文本。~~

<h2 id="abb57f6b445af4f04b8d38b5f8efd210"></h2>
### 4. 注脚

使用 [^keyword] 表示注脚。

这是一个注脚[^footnote]的样例。

这是第二个注脚[^footnote2]的样例。

<h2 id="3009098fd39467289ee3ef379d7fec12"></h2>
### 5. LaTeX 公式

$ 表示行内公式： 

质能守恒方程可以用一个很简洁的方程式 $E=mc^2$ 来表达。

$$ 表示整行公式：

$$\sum_{i=1}^n a_i=0$$

$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$

$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$

访问 [MathJax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference) 参考更多使用方法。

<h2 id="f9c6179b667c4229ad7e6aefd14e63da"></h2>
### 6. 加强的代码块

支持四十一种编程语言的语法高亮的显示，行号显示。

非代码示例：

```
$ sudo apt-get install vim-gnome
```

Python 示例：

```python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
```

JavaScript 示例：

``` javascript
/**
* nth element in the fibonacci series.
* @param n >= 0
* @return the nth element, >= 0.
*/
function fib(n) {
  var a = 1, b = 1;
  var tmp;
  while (--n >= 0) {
    tmp = a;
    a += b;
    b = tmp;
  }
  return a;
}

document.write(fib(10));
```

<h2 id="83d366b19e9953a74054eb9650424d34"></h2>
### 7. 流程图

<h2 id="1a63ac23010e0573f7c0a8cd3314b8c6"></h2>
#### 示例

```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```

<h2 id="2464aee80728b47972620af84bf42491"></h2>
#### 更多语法参考：[流程图语法参考](http://adrai.github.io/flowchart.js/)

<h2 id="7f5551010a04c9080e1ec1ed029284bd"></h2>
### 8. 序列图

<h2 id="1ee999b7a746baaeeefdac41f3d74e44"></h2>
#### 示例 1

```seq
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

<h2 id="3569926cb0d361708ef53bb49cdca79c"></h2>
#### 示例 2

```seq
Title: Here is a title
A->B: Normal line
B-->C: Dashed line
C->>D: Open arrow
D-->>A: Dashed open arrow
```

<h2 id="87e764078b7c9de48e613888bd50f03f"></h2>
#### 更多语法参考：[序列图语法参考](http://bramp.github.io/js-sequence-diagrams/)

<h2 id="74e7c8676cb7b4fd2694d308fc2f747d"></h2>
### 9. 表格支持

| 项目        | 价格   |  数量  |
| --------   | -----:  | :----:  |
| 计算机     | \$1600 |   5     |
| 手机        |   \$12   |   12   |
| 管线        |    \$1    |  234  |


<h2 id="d1fa7e0d898e85ff862ec5eb0b8ddf2d"></h2>
### 10. 定义型列表

名词 1
:   定义 1（左侧有一个可见的冒号和四个不可见的空格）

代码块 2
:   这是代码块的定义（左侧有一个可见的冒号和四个不可见的空格）

        代码块（左侧有八个不可见的空格）

<h2 id="b31600d3a53dbc9f1ba3762e6688e33c"></h2>
### 11. Html 标签

本站支持在 Markdown 语法中嵌套 Html 标签，譬如，你可以用 Html 写一个纵跨两行的表格：

    <table>
        <tr>
            <th rowspan="2">值班人员</th>
            <th>星期一</th>
            <th>星期二</th>
            <th>星期三</th>
        </tr>
        <tr>
            <td>李强</td>
            <td>张明</td>
            <td>王平</td>
        </tr>
    </table>


<table>
    <tr>
        <th rowspan="2">值班人员</th>
        <th>星期一</th>
        <th>星期二</th>
        <th>星期三</th>
    </tr>
    <tr>
        <td>李强</td>
        <td>张明</td>
        <td>王平</td>
    </tr>
</table>

<h2 id="3fe816834026984092deb8bb5259c4f0"></h2>
### 12. 内嵌图标

本站的图标系统对外开放，在文档中输入

    <i class="icon-weibo"></i>

即显示微博的图标： <i class="icon-weibo icon-2x"></i>

替换 上述 `i 标签` 内的 `icon-weibo` 以显示不同的图标，例如：

    <i class="icon-renren"></i>

即显示人人的图标： <i class="icon-renren icon-2x"></i>

更多的图标和玩法可以参看 [font-awesome](http://fortawesome.github.io/Font-Awesome/3.2.1/icons/) 官方网站。

<h2 id="4a98422efd774fe54e88575df012b823"></h2>
### 13. 待办事宜 Todo 列表

使用带有 [ ] 或 [x] （未完成或已完成）项的列表语法撰写一个待办事宜列表，并且支持子列表嵌套以及混用Markdown语法，例如：

    - [ ] **Cmd Markdown 开发**
        - [ ] 改进 Cmd 渲染算法，使用局部渲染技术提高渲染效率
        - [ ] 支持以 PDF 格式导出文稿
        - [x] 新增Todo列表功能 [语法参考](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
        - [x] 改进 LaTex 功能
            - [x] 修复 LaTex 公式渲染问题
            - [x] 新增 LaTex 公式编号功能 [语法参考](http://docs.mathjax.org/en/latest/tex.html#tex-eq-numbers)
    - [ ] **七月旅行准备**
        - [ ] 准备邮轮上需要携带的物品
        - [ ] 浏览日本免税店的物品
        - [x] 购买蓝宝石公主号七月一日的船票
        
对应显示如下待办事宜 Todo 列表：
        
- [ ] **Cmd Markdown 开发**
    - [ ] 改进 Cmd 渲染算法，使用局部渲染技术提高渲染效率
    - [ ] 支持以 PDF 格式导出文稿
    - [x] 新增Todo列表功能 [语法参考](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
    - [x] 改进 LaTex 功能
        - [x] 修复 LaTex 公式渲染问题
        - [x] 新增 LaTex 公式编号功能 [语法参考](http://docs.mathjax.org/en/latest/tex.html#tex-eq-numbers)
- [ ] **七月旅行准备**
    - [ ] 准备邮轮上需要携带的物品
    - [ ] 浏览日本免税店的物品
    - [x] 购买蓝宝石公主号七月一日的船票
        
        
[^footnote]: 这是一个 *注脚* 的 **文本**。

[^footnote2]: 这是另一个 *注脚* 的 **文本**。

