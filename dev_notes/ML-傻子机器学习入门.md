
# 傻子机器学习入门
    observation 观测数据: 在机器学习领域，一般来说，一个观测数据 observation 是对 一个物体或某种情况 的说明。
    
[TOC]

## 分类 
举个 鸢尾花的例子。  
对于每朵 鸢尾花，我们测量它的4个值： 萼片和花瓣的长宽，这些值称为 属性。  
一般来说，属性被认为是两种类型：数字(例:花瓣长度)或类别(例:花瓣颜色)  

此外，对于每个观测（即每个鸢尾花），我们有一个“类” class 。 类 class 是 额外的观测信息。  
在我们的例子，让我们假设 类class 为鸢尾花的种类。 Setosa,Versicolour,Viginica。  

现在，我们有了一张观测表  
每个观测， 都有4个属性和一个类。  
这张表称为 "dataset"。  
![](http://blog.mathieu.guillame-bert.com/wp-content/uploads/2015/07/table.png)  

假设我们拥有 150个 鸢尾花观测，但是 最后一个观测，我们不知道他的种类class.  
我们使用其他的149个观测，和 不知道种类的鸢尾花比较，来最终获得 最后的鸢尾花的种类。  
这就是分类。  

为了完成最后一个鸢尾花的分类，我们 使用鸢尾花的属性来判断它的种类。  

## 分类方法
### 1. 相同的观测数据
从其他的149个观测数据，找到一个属性完全一样的,然后确定 150号鸢尾花的种类。  
实用性为0  

### 2. 1-nearest neighbors 
寻找属性相近的观测数据。  
distance = ((a-ai)^2 + (b-bi)^2 + (c-ci)^2 + (d-di)^2 )^0.5 。  
distance最小的就是 最相似的观测数据。  

### 3. k-nearest neighbors 
当测试数据中包含坏数据，或者不精确的数据时，方法2的结果也会存在很大误差。  
这种情况下，会找出n个最相思的观测数据，然后这n个观测数据中，某个种类的最大数量，即为第150个观测数据的 种类。  

---

## Random Forest 随机森林
    一个只有10年的年轻算法

k-nearest neighbors 方法中，所有属性都一样重要。  
而随机森林能够发现某些属性更加重要，或者某些属性根本无用。  
随机森林是“决策树”算法家庭的一部分。  
![](http://blog.mathieu.guillame-bert.com/wp-content/uploads/2015/07/exampledt.png)  

图示 展示了一个简单的 确定动物物种的 决策树。  
随机森林 算法会生成 *许多个* 决策树，并使用它们。  
鸢尾花分类问题上，决策树的问题 是对 鸢尾花的属性的提问， 回答则是 鸢尾花种类。  

要创建一个决策树，随机森林算法总是开始于一个空的决策树：红色的start。  
接下来，该算法会 发现 并开始构建树最好的第一个问题。  
在我们的例子中，第一个问题是“它有羽毛？”。  
每次算法找到一个新的很好的问题要问，它构建了树的两个分支。  
当没有更多的问题，算法简单地停止，决策树被认为是结束了。  

找到最好的问题的方法 比较复杂。  
当算法启动时，该算法不知道如何 对种类进行区分。换句话说，所有的种类都在同一个“袋子”中。   
为了找到最好的第一个问题，算法将尝试“一切可能”的问题。  
对于每个可能的问题，算法会评估 这个问题可以把多少个 种类分离出来，选择较好的一个提问。  
通过使用 信息增益“information gain” 来衡量一个问题有多好。  

![](http://blog.mathieu.guillame-bert.com/wp-content/uploads/2015/07/building-dt.png)  
图例显示了决策树生成的过程。 注意：这仅仅是1棵决策树。  

随机森林的诀窍是让 每一个决策树独立投票（像选举）。在投票结束后，最高数投票的答案 将被随机森林选中。  

为了确保不是所有的决策树是相同的，随机森林算法会随机使用一些观测数据作为样本。更精确的说，他会随机删除一些观测数据。  
从全局来看，修改后的观测数据 仍然非常接近原始的数据。但这些小的差异确保决策树都有点不同。这个过程被称为“引导程序” bootstrapping 。

真正确保生成的决策树彼此不同诀窍是，随机森林算法 生成决策树时， 会 故意的 随机避免 测试某几个问题。在这种情况下，如果 最好的问题没有被测试，一个次一点的问题，就会被选中测试。 这个过程被称为“属性采样”  attribute sampling 。  


## Scikit-Learn 随机森林例子

随机森林是集成学习的一个子类，由于它依靠于策率树的合并。你可以在这找到用python实现集成学习的文档：
[Scikit 学习文档](http://scikit-learn.org/dev/modules/ensemble.html)

Scikit-Learn是开始使用随机森林的一个很好的方式。

随机森林在scikit-learn中的实现最棒的特性是*n_jobs*参数。
这将会基于你想使用的核数自动地并行设置随机森林。

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
 
#print dir(pd)
iris =load_iris()

#feature data , feature name
#print iris.data, iris.feature_names
"""
[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]
 [ 4.7  3.2  1.3  0.2]]  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
"""
df =pd.DataFrame(iris.data, columns=iris.feature_names)

#print df 
"""
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8

[150 rows x 4 columns]
"""

# some data is used 4 trainint , some data used for test
df['is_train'] =np.random.uniform(0, 1, len(df)) <=.75

#print df['is_train']
"""
0       True
1      False
2       True
3       True
4      False
"""
#target data, target name 
#print iris.target, iris.target_names
"""
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2] ['setosa' 'versicolor' 'virginica']
"""
df['species'] =pd.Categorical.from_codes(iris.target, iris.target_names)
df.head()

#print df
"""
    is_train    species  
0       True     setosa  
1       True     setosa  
2      False     setosa 
""" 

train, test =df[df['is_train']==True], df[df['is_train']==False]
#print train, test
 
features =df.columns[:4]
"""
Index([u'sepal length (cm)', u'sepal width (cm)', u'petal length (cm)',
       u'petal width (cm)'],
      dtype='object')
"""

clf =RandomForestClassifier(n_jobs=2)
#print clf

y, _ =pd.factorize(train['species'])

clf.fit(train[features], y)
 
preds =iris.target_names[clf.predict(test[features])]

print pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])

"""
preds       setosa  versicolor  virginica
actual                                   
setosa          11           0          0
versicolor       0           9          0
virginica        0           2         12
"""

#save all trees to words
from sklearn.tree import export_graphviz
for i in xrange(len(clf.estimators_)):
    export_graphviz(clf.estimators_[i] , '%d.dot'%i)


#save all trees to pdf
from sklearn import tree  
from sklearn.externals.six import StringIO    
import pydot   
 
for i in xrange(len(clf.estimators_)):
    dot_data = StringIO()   
    tree.export_graphviz( clf.estimators_[i] , out_file=dot_data)  

    graph = pydot.graph_from_dot_data(dot_data.getvalue())   
    graph.write_pdf("iris%d.pdf" %  i )   
    
```

`
要打印 pdf， 需要安装graphviz ，以及一下python库
安装brew
sudo su
curl -L http://github.com/mxcl/homebrew/tarball/master | tar xz --strip 1 -C /usr/local

安装 graphviz
sudo brew install  graphviz


安装python库 必须按照顺序安装

sudo pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709

sudo pip install GraphViz

sudo pip install pydot2

`


