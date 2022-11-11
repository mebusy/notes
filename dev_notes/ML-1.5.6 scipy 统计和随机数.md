[](...menustart)

- [1.5.6。统计数据和随机数：scipy.stats](#13f0949d6c57f6b2f15ff881b61d4308)
    - [1.5.6.1。直方图和概率密度函数](#52b76b5ffc0d467aa403fe05eb57cf02)

[](...menuend)


<h2 id="13f0949d6c57f6b2f15ff881b61d4308"></h2>

## 1.5.6。统计数据和随机数：scipy.stats

scipy.stats包含统计工具和随机过程的概率描述。各种随机过程的随机数生成可在numpy.random中找到。

可以使用下面的语句获得stats模块中所有的连续随机变量：

```python
from scipy import stats
[k for k,v in stats.__dict__.items() if isinstance(v, stats.rv_continuous)]

['genhalflogistic','triang','rayleigh','betaprime', ...]
```


连续随机变量对象都有如下方法：

rvs：对随机变量进行随机取值，可以通过size参数指定输出的数组的大小。 

pdf：随机变量的概率密度函数。 

cdf：随机变量的累积分布函数，它是概率密度函数的积分。

sf：随机变量的生存函数，它的值是1-cdf(t)。 

ppf：累积分布函数的反函数。 

stat：计算随机变量的期望值和方差。 

fit：对一组随机取样进行拟合，找出最适合取样数据的概率密度函数的系数。 



<h2 id="52b76b5ffc0d467aa403fe05eb57cf02"></h2>

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

