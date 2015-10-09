## 1.5.6。统计数据和随机数：scipy.stats

scipy.stats包含统计工具和随机过程的概率描述。各种随机过程的随机数生成可在numpy.random中找到。

### 1.5.6.1。直方图和概率密度函数

给定一个随机过程的观察，他们的直方图是随机过程的概率密度函数（probability density function）的估计：

```python
a = np.random.normal(size=1000)
bins = np.arange(-4, 5)
histogram = np.histogram(a, bins=bins, normed=True)[0]
#注意 bins 和 histogram 的 shape不一致，调整bins
bins = 0.5*(bins[1:] + bins[:-1])
# array([-3.5, -2.5, -1.5, -0.5,  0.5,  1.5,  2.5,  3.5])
#画图
pl.plot(bins, histogram)

from scipy import stats
b = stats.norm.pdf(bins)  # norm is a distribution
pl.plot(bins, b)
```

![](http://scipy-lectures.github.io/_images/normal_distribution.png)

如果我们知道随机过程属于一个特定的随机过程家族，比如正态分布; 我们就可以对观测数据做 最大可能性的拟合，来估计底层分布的参数。
这里，我们对观测数据做一个正态拟合:

```python
# Parameter estimates for generic data.
>>> loc, std = stats.norm.fit(a)
>>> loc     
-0.045256707490...
>>> std     
0.9870331586690...
```

