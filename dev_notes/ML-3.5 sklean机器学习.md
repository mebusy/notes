[](...menustart)

- [3.5.1 加载一个数据集](#61f0c3c78cb774f4522759cb5b766e48)
- [3.5.1.1 学习和预测](#9042e2951924403f2563670df6a5907a)
- [3.5.2. 分类 Classification](#c5e9f6f031f38c79c84a12648b17e5bc)
    - [3.5.2.1. k-Nearest neighbors classifierK 最近邻(KNN)分类器](#a928bb9b5283c675ea5b0d403fa28ce6)
    - [训练集和测试集](#6b142be1538abf7c9b27eceb24a31693)
    - [3.5.2.2 支持向量机（SVM）进行分类](#7608de9c0b5c2ef3728f6a862c34be93)
    - [线性支持向量机](#21368cab7e6be750f6930f26872bdd34)
    - [3.5.2.2.2. Using kernels 使用内核](#30e6dc519b02a1c9361c44a4e728aa7d)
- [3.5.3. 聚类 Clustering ：将观测值分组](#df7233c170cd11b783e36cd881fe5f88)
    - [3.5.3.1  k均值聚类 K-means clustering](#4fcb97c71c13c4ea699fc9e733ed6b41)
    - [应用到图像压缩](#b6716bcc1f4eef556f17e78ffdcc6da2)
- [3.5.4. 用主成分分析(Principal Component Analysis)来降维](#0613c6a0178e373ecd734f761709b23d)
- [3.5.5。全部放在一起：人脸识别](#845933fcaeb6332543e41cb01e51c792)
- [3.5.6 线性模型：从回归稀疏](#07bc8d8f0c7abc03e7873690065e2bfd)
    - [稀疏模型](#8db4f290d806d5df45b60a1a83cddd4b)
    - [同一问题的不同算法](#137b0c419cd6ce6b57e7320eb41b5735)
- [3.5.7。型号选择：选择估值器及其参数](#130526ec2eb670f8b6aef37b9efe2535)
    - [3.5.7.1。网格搜索和交叉验证估计](#bcf64e07398790bedec0c72f9f2e7c0b)
    - [3.5.7.1.1 网格搜索](#bad9c05bf8d2f051d7ad419947e10e2b)
    - [3.5.7.1.2。交叉验证估计器](#0ad88aee957ce82d156a5b067bc31e61)

[](...menuend)


http://scipy-lectures.github.io/index.html

<h2 id="61f0c3c78cb774f4522759cb5b766e48"></h2>

### 3.5.1 加载一个数据集

载入 鸢尾花 数据：

```python
from sklearn import datasets
iris = datasets.load_iris()
```

数据存储在.data项中,是一个(n_samples,n_features)数组。

```python
>>> iris.data.shape
(150, 4)
```

种类存贮在数据集的.target属性中。这是一个长度为n_samples的整数一维数组:

```python
>>> iris.target.shape
(150,)
```

查看一共有多少可能种类

```python
>>> import numpy as np
>>> np.unique(iris.target)
array([0, 1, 2])
```

改变 数码数据集(digits datasets)  大小

数码数据集1包括1797个图像，每一个都是个代表手写数字的8x8像素图像
```python
digits = datasets.load_digits()
>>> digits.images.shape
(1797, 8, 8)
```

显示一个图像

```python
>>> import pylab as pl
>>> pl.imshow(digits.images[0], cmap=pl.cm.gray_r) 
<matplotlib.image.AxesImage object at 0x10f0a7e90>
>>> pl.show()
```

sklearn 只能接收2维输入数据，我们把每个8x8图像转换成长度为64的矢量

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```

或者直接用 digits.data，已经做好了处理

======================================

<h2 id="9042e2951924403f2563670df6a5907a"></h2>

### 3.5.1.1 学习和预测

在scikit-learn中，我们通过创建一个估计器(estimator)从已经存在的数据中学习，并且调用它的fit(X,Y)方法。

```python
from sklearn import svm
clf = svm.LinearSVC()
clf.fit(iris.data, iris.target) # learn from the data 
# LinearSVC(...)
```

一旦我们已经从数据学习，我们可以使用我们的模型来预测未观测数据最可能的结果。

```python
clf.predict([[ 5.0,  3.6,  1.3,  0.25]])
# array([0], dtype=int32)
```

通过它以下划线结束的属性 存取模型的参数

```python
>>> clf.coef_
array([[ 0.18423466,  0.45122537, -0.80794548, -0.45071632],
       [ 0.05352915, -0.88933666,  0.4020285 , -0.936181  ],
       [-0.85075702, -0.98675298,  1.38111773,  1.8655567 ]])
```

======================================
<h2 id="c5e9f6f031f38c79c84a12648b17e5bc"></h2>

### 3.5.2. 分类 Classification

<h2 id="a928bb9b5283c675ea5b0d403fa28ce6"></h2>

#### 3.5.2.1. k-Nearest neighbors classifierK 最近邻(KNN)分类器

最简单的可能的分类器是最近邻：给定一个新的观测值，将n维空间中最靠近它的训练样本标签给它。其中n是每个样本中特性(features)数。
k最近邻分类器 内部使用基于球树(ball tree) 来代表它训练的样本。

![](http://scipy-lectures.github.io/_images/iris_knn.png)

```python
# 创建并拟合fit一个 最近邻分类器
>>> from sklearn import neighbors
>>> knn = neighbors.KNeighborsClassifier()
>>> knn.fit(iris.data, iris.target) 
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_neighbors=5, p=2, weights='uniform')
>>> knn.predict([[0.1, 0.2, 0.3, 0.4]])
array([0])
```

<h2 id="6b142be1538abf7c9b27eceb24a31693"></h2>

#### 训练集和测试集
当验证学习算法时，不要用一个用来拟合估计器的数据来验证估计器的预测非常重要。
那样的话，使用kNN 我们总能获得 训练集完美的预测。

```python
#创建一个 随机的索引数组
>>> perm = np.random.permutation(iris.target.size)
#根据 perm数组，对数据重新排序
>>> iris.data = iris.data[perm]
>>> iris.target = iris.target[perm]
>>> knn.fit(iris.data[:100], iris.target[:100]) 
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_neighbors=5, p=2, weights='uniform')

>>> knn.score(iris.data[100:], iris.target[100:]) 
0.95999999999999996
```

=====================================

<h2 id="7608de9c0b5c2ef3728f6a862c34be93"></h2>

#### 3.5.2.2 支持向量机（SVM）进行分类

在机器学习领域，支持向量机SVM(Support Vector Machine）是一个有监督的学习模型，通常用来进行模式识别、分类、以及回归分析。
SVM的主要思想可以概括为两点：
⑴它是针对线性可分情况进行分析，对于线性不可分的情况，通过使用非线性映射算法将低维输入空间线性不可分的样本转化为高维特征空间使其线性可分，从而使得高维特征空间采用线性算法对样本的非线性特征进行线性分析成为可能
⑵它基于结构风险最小化理论之上在特征空间中建构最优分割超平面，使得学习器得到全局最优化，并且在整个样本空间的期望风险以某个概率满足一定上界。

<h2 id="21368cab7e6be750f6930f26872bdd34"></h2>

#### 线性支持向量机

SVMs 支持向量机尝试构建一个超平面，最大限度地发挥这两个类之间的空白。它选择输入数据的一个子集,即最靠近这个超平面的观测数据(称为支持向量)

![](http://scipy-lectures.github.io/_images/svm_margin.png)

```python
>>> from sklearn import svm
>>> svc = svm.SVC(kernel='linear')
>>> svc.fit(iris.data, iris.target)
SVC(...)

>>> svc.predict([[0.1, 0.2, 0.3, 0.4]])
array([0])
```

scikit-learn中有好几种支持向量机实现。
最普遍使用的是svm.SVC，svm.NuSVC和svm.LinearSVC;
“SVC”代表支持向量分类器(Support Vector Classifier)(也存在回归SVMs，在scikit-learn中叫作“SVR”)。


<h2 id="30e6dc519b02a1c9361c44a4e728aa7d"></h2>

#### 3.5.2.2.2. Using kernels 使用内核

类别 不总是可以用超平面分离，所以人们希望能有一些非线性的,多项式或指数的,决策函数：

线性核
```python
svc = svm.SVC(kernel=’linear’)
```

![](http://scipy-lectures.github.io/_images/svm_kernel_linear.png)

多项式核
```python
svc = svm.SVC(kernel=’poly’,degree=3) 
# degree: polynomial degree
```

![](http://scipy-lectures.github.io/_images/svm_kernel_poly.png)


RBF核(径向基函数 Radial Basis)
```python
svc = svm.SVC(kernel=’rbf’) 
# gamma: inverse of size of radial kernel
```
![](http://scipy-lectures.github.io/_images/svm_kernel_rbf.png)

PS.前两个对数字数据集有更好的预测性能

======================================

<h2 id="df7233c170cd11b783e36cd881fe5f88"></h2>

### 3.5.3. 聚类 Clustering ：将观测值分组

给定鸢尾花数据集，假如我们只知道共有三种鸢尾花，但是不知道每个数据 对应的种类。
我们可以尝试非监督学习：我们可以通过某些标准将观测值聚类到几个组别里。

<h2 id="4fcb97c71c13c4ea699fc9e733ed6b41"></h2>

#### 3.5.3.1  k均值聚类 K-means clustering 

最简单的聚类算法是k均值算法。
算法将数据集分成k个集群, 将一个观测数据赋予一个集群，以便该观测数据(n维空间中)到集群均值means的距离最小。然后均值重新被计算。这个操作递归运行直到聚类收敛。
(一个替代的k均值算法实现在scipy中的cluster包中。这个scikit-learn实现与之不同，通过提供对象API和几个额外的特性，包括智能初始化。)

```python
>>> from sklearn import cluster, datasets
>>> iris = datasets.load_iris()
>>> k_means = cluster.KMeans(n_clusters=3)
>>> k_means.fit(iris.data)
KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=3, n_init=10,
    n_jobs=1, precompute_distances='auto', random_state=None, tol=0.0001,
    verbose=0)
```

检验:

```python
>>> k_means.labels_[::10]
array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2], dtype=int32)
>>> iris.target[::10]
array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
```

![](http://scipy-lectures.github.io/_images/cluster_iris_truth.png)

![](http://scipy-lectures.github.io/_images/k_means_iris_3.png)

![](http://scipy-lectures.github.io/_images/k_means_iris_8.png)


<h2 id="b6716bcc1f4eef556f17e78ffdcc6da2"></h2>

#### 应用到图像压缩

Lena是经典的图像处理实例 图像, 8位灰度色深, 尺寸512 x 512

聚类可以被看作是一个从数据中选择出一小部分观测值的方法。例如，这个可以被用来posterize一个图像(将连续变化的色调转换成更少几个色阶)：

载入 lena 图像

```python
from scipy import misc
lena = misc.lena().astype(np.float32)
```

我们需要 一个 (n_sample, n_feature) 数组

```python
X = lena.reshape((-1, 1))
# X.shape -> (262144, 1)

k_means = cluster.KMeans(5)
k_means.fit(X)
```

```python
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

lena_compressed = np.choose(labels, values)
#lena_compressed.shape  (262144,)

lena_compressed.shape = lena.shape
#lena_compressed.shape  (512, 512)
```

看效果

```python
import matplotlib.pyplot as plt
plt.gray()  # 另一种制定cmap的方法
plt.imshow(lena_compressed)
plt.show()
```

![](http://scipy-lectures.github.io/_images/lena_compressed.png)

=========================================================

<h2 id="0613c6a0178e373ecd734f761709b23d"></h2>

### 3.5.4. 用主成分分析(Principal Component Analysis)来降维

PCA是将训练数据（向量形式）全部转化成其协方差，然后进行SVD拆分，之后它们的用法大致相同，
PCA是在最大的特征值所对应的的特征向量形成的矩阵基础上近似还原原有训练数据，这也就是用PCA方法表示出来的数据

![](http://scipy-lectures.github.io/_images/pca_3d_axis.jpg)

![](http://scipy-lectures.github.io/_images/pca_3d_aligned.jpg)

以上观测值的点云在一个方向上非常平坦，所以一个特性几乎可以用其它两个精确地计算出来。
PCA发现哪个方向的数据不是平的，并且它可以通过在一个子空间投影来降维。

```python
from sklearn import decomposition
pca = decomposition.PCA(n_components=2)
pca.fit(iris.data)

X = pca.transform(iris.data)
```

现在我们可以可视化(降维过的)鸢尾花数据集：

```python
import pylab as plt
plt.scatter(X[:, 0], X[:, 1], c=iris.target) 
plt.show()
```

![](http://scipy-lectures.github.io/_images/pca_iris.png)

PCA不仅在可视化高维数据集时非常有用。
它还可以作为预处理步骤来帮助加速对高维数据不那么有效率的监督方法。

<h2 id="845933fcaeb6332543e41cb01e51c792"></h2>

### 3.5.5。全部放在一起：人脸识别

一个使用PCA降维和SVM分类来进行人脸识别的例子

```python
import numpy as np
import pylab as pl
from sklearn import datasets, decomposition, svm
from sklearn import cross_validation as cross_val
```

手动下载 [数据](http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz) 并放到 ~/scikit_learn_data/lfw_home/  目录下

```python
# .. load data ..
lfw_people = datasets.fetch_lfw_people(min_faces_per_person=70, resize=0.4)
perm = np.random.permutation(lfw_people.target.size)
lfw_people.data = lfw_people.data[perm]
lfw_people.target = lfw_people.target[perm]
faces = np.reshape(lfw_people.data, (lfw_people.target.shape[0], -1))
#StratifiedKFold: 分层K-折叠交叉验证迭代器
#把数据分割为 训练／测试集
train, test = iter(cross_val.StratifiedKFold(lfw_people.target, n_folds=4)).next()

X_train, X_test = faces[train], faces[test]
y_train, y_test = lfw_people.target[train], lfw_people.target[test]


# .. 降维 ..
pca = decomposition.RandomizedPCA(n_components=150, whiten=True)
pca.fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# .. 分类 ..
clf = svm.SVC(C=5., gamma=0.001)
clf.fit(X_train_pca, y_train)

# .. 预测新图像 ..
for i in range(10):
    print lfw_people.target_names[clf.predict(X_test_pca[i])[0]]
    _ = pl.imshow(X_test[i].reshape(50, 37), cmap=pl.cm.gray)
    pl.show()
    _ = raw_input()
```

<h2 id="07bc8d8f0c7abc03e7873690065e2bfd"></h2>

### 3.5.6 线性模型：从回归稀疏

糖尿病数据集

糖尿病数据集包含442个病人的测量而得的10项生理指标(年龄，性别，体重，血压)，和一年后疾病进展的指示：

```python
diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]
```

现在的任务是用来从生理指标预测疾病

<h2 id="8db4f290d806d5df45b60a1a83cddd4b"></h2>

#### 稀疏模型

为了改善这个问题的处理，我们只关注有信息的特性, 将没有信息的特性设置为0。
这种惩罚方式称为 Lasso , 可以设定一些系数为零。这些方法叫作稀疏方法(sparse method)。
稀疏化可以被视作Occam’s razor的应用：相对于复杂模型更倾向于简单的。

```python
from sklearn import linear_model
regr = linear_model.Lasso(alpha=.3)
regr.fit(diabetes_X_train, diabetes_y_train) 
#regr.coef_ # very sparse coefficients
regr.score(diabetes_X_test, diabetes_y_test) 
# 0.55108354530029779
```

这个分数和线性回归(最小二乘法)非常相似：

```python
lin = linear_model.LinearRegression()
lin.fit(diabetes_X_train, diabetes_y_train) 
lin.score(diabetes_X_test, diabetes_y_test) 
# 0.58507530226905691
```

<h2 id="137b0c419cd6ce6b57e7320eb41b5735"></h2>

#### 同一问题的不同算法

同一数学问题可以用不同算法解决。例如,sklearn中的Lasso对象使用坐标下降(coordinate descent)方法 解决套索回归，这在大数据集时非常有效率。然而，sklearn也提供了LassoLARS对象，使用LARS 在解决权重向量估计非常稀疏，观测值很少的问题时很有效率。

<h2 id="130526ec2eb670f8b6aef37b9efe2535"></h2>

###3.5.7。型号选择：选择估值器及其参数

<h2 id="bcf64e07398790bedec0c72f9f2e7c0b"></h2>

#### 3.5.7.1。网格搜索和交叉验证估计

<h2 id="bad9c05bf8d2f051d7ad419947e10e2b"></h2>

#### 3.5.7.1.1 网格搜索

scikit-learn提供了一个对象，该对象给定数据，在拟合一个参数网格的估计器时计算分数，并且选择可以最大化交叉验证分数的参数。这个对象在构建时使用一个估计器并且暴露出估计器API：

```python
from sklearn import svm, grid_search
from sklearn import datasets
digits = datasets.load_digits()
gammas = np.logspace(-6, -1, 10)
svc = svm.SVC()
clf = grid_search.GridSearchCV(estimator=svc, param_grid=dict(gamma=gammas),
                   n_jobs=-1)
clf.fit(digits.data[:1000], digits.target[:1000]) 
clf.best_score
# 0.93200000000000005
clf.best_params_
# {'gamma': 0.00059948425031894088}
```

GridSearchCV默认使用三次(3-fold)交叉验证。如果它探测到一个分类器被传递，而不是一个回归量，它使用3次分层验证。

<h2 id="0ad88aee957ce82d156a5b067bc31e61"></h2>

#### 3.5.7.1.2。交叉验证估计器

交叉验证在 algorithm by algorithm基础上可以更有效地设定参数。 
这就是为什么，对特定的估计器，scikit-learn使用“CV”估计器，通过交叉验证自动设定参数。

```python
from sklearn import linear_model, datasets
lasso = linear_model.LassoCV()
diabetes = datasets.load_diabetes()
X_diabetes = diabetes.data
y_diabetes = diabetes.target
lasso.fit(X_diabetes, y_diabetes)

# The estimator chose automatically its lambda:
lasso.alpha_
# 0.012291895087486173
```

这些估计器都以‘CV’为它们名字的后缀。






