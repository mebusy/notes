[](...menustart)

- [sklearn 随机森林简单介绍](#d611c199fb56f4cc3ceece27ebc41a8a)
    - [1. 决策树](#ac3f05d5330e044468fd526d476de188)
        - [构造决策树 Sklearn.tree](#417242c55236c9c531e82c5425894faf)
        - [输出决策树结果](#6b00a3fa8d6c11d615b68019cfea518b)
        - [使用建议](#1381cce03d257acf549790c944080017)
    - [随机森林](#a60f6c59122509d3df75f4ed6a768b2e)

[](...menuend)


<h2 id="d611c199fb56f4cc3ceece27ebc41a8a"></h2>

#sklearn 随机森林简单介绍

<h2 id="ac3f05d5330e044468fd526d476de188"></h2>

## 1. 决策树

<h2 id="417242c55236c9c531e82c5425894faf"></h2>

### 构造决策树 Sklearn.tree

在强大的机器学习库sklearn中已经集成了决策树模型，所以我们可以利用该模块方便的实施决策树学习。下面介绍一些常用的方法：  

class sklearn.tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2,min_samples_leaf=1, max_features=None, random_state=None, min_density=None, compute_importances=None,max_leaf_nodes=None)  

> * criterion ：规定了该决策树所采用的的最佳分割属性的判决方法，有两种：“gini”，“entropy”。  
> * max_depth ：限定了决策树的最大深度，对于防止过拟合非常有用。  
> * min_samples_leaf ：限定了叶子节点包含的最小样本数，这个属性对于防止上文讲到的数据碎片问题很有作用。 (因为随着树的深度增加，叶子上的样本数会越来越少)  


模块中一些重要的属性方法：  
> * n_classes_ ：决策树中的类数量。  
> * classes_ ：返回决策树中的所有种类标签。  
> * feature_importances_ ：feature的重要性，值越大那么越重要。  
> * fit(X, y, sample_mask=None, X_argsorted=None, check_input=True,   sample_weight=None):   将数据集x，和标签集y送入分类器进行训练，这里要注意一个参数是：sample_weright，它和样本的数量一样长，所携带的是每个样本的权重。
> * get_params(deep=True) 得到决策树的各个参数。
> * set_params(**params)  调整决策树的各个参数。
> * predict(X)   送入样本X，得到决策树的预测。可以同时送入多个样本。
> * transform(X, threshold=None): 返回X的较重要的一些feature，相当于裁剪数据。
> * score(X, y, sample_weight=None)   返回在数据集X,y上的测试分数，正确率。

下面是一个应用的例子：
```python
from sklearn import tree  
X = [[0, 0], [1, 1]]  
Y = [0, 1]  
clf = tree.DecisionTreeClassifier()  
clf = clf.fit(X, Y)  
clf.predict([[2., 2.]])  
```

<h2 id="6b00a3fa8d6c11d615b68019cfea518b"></h2>

### 输出决策树结果
利用python中的pydot模块可以方便的输出决策树的效果图，不过需要注意的是pyparsing必须是旧版本的，比如1.5，另外需要在电脑商安装Graphviz软件。下面是一个例子：
```python
from sklearn.externals.six import StringIO    
import pydot   
dot_data = StringIO.StringIO()   
tree.export_graphviz(clf, out_file=dot_data)   
graph = pydot.graph_from_dot_data(dot_data.getvalue())   
graph.write_pdf("iris.pdf")   
```

<h2 id="1381cce03d257acf549790c944080017"></h2>

### 使用建议
> * 当我们数据中的feature较多时，一定要有足够的数据量来支撑我们的算法，不然的话很容易overfitting
> * 善用max_depth参数，缓慢的增加并测试模型，找出最好的那个depth。
> * 善用min_samples_split和min_samples_leaf参数来控制叶子节点的样本数量，防止overfitting。
> * 平衡训练数据中的各个种类的数据，防止被一个种类的数据支配。

---

<h2 id="a60f6c59122509d3df75f4ed6a768b2e"></h2>

## 随机森林

RandomForestClassifier 的一些重要属性，方法:
```python
#拆分训练集和测试集
feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.1, random_state=42)

#分类型决策树
clf = RandomForestClassifier(n_estimators = 8)

#训练模型
s = clf.fit(feature_train , target_train)
print s

#评估模型准确率
r = clf.score(feature_test , target_test)
print r

print '判定结果：%s' % clf.predict(feature_test[0])
#print clf.predict_proba(feature_test[0])

print '所有的树:%s' % clf.estimators_

print clf.classes_
print clf.n_classes_

print '各feature的重要性：%s' % clf.feature_importances_

print clf.n_outputs_

```
