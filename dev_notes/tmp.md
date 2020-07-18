


一个常用的做法，是使用计数器, 并设置一个阈值，比如28。 玩家抽卡一次，计数器累加1， 如果玩家抽中了稀有卡，计数器清零。 当计数器累加到阈值的时候，也就是玩家已经连续28次抽卡都没有抽中的时候，按抽中处理，  同时计数器清零。

使用这个方式 看一下间隔的分布

```python

import numpy as np
import matplotlib.pyplot as plt

count = 0


def lottery( rand ):
    global count
    if rand <= 5:
        count = 0
        return True
    else:
        count += 1
        if count >= 28:
            count = 0
            return True
        return False


x1 = np.random.rand(50000) * 100
events = [ i for i,x in enumerate(x1) if lottery(x) ]
interval = np.diff( events )

print( len(events) / len(x1) )

plt.hist( interval, density=True, bins = 50)
plt.show()
```



这种实现好处就是简单。但是，这个方案仅仅是改善了 玩家抽很多次抽不到的体验，并且，总体上说，这种做法其实是增加了这张稀有卡的掉率。


计数器还有一个变种，改成慢慢地提高掉落的概率。比如大菠萝3 就是使用的这种方式。 他会记录你杀怪的时间，如果长时间没有掉落 Legendary 传奇装备，就会逐渐地提高 传奇装备的掉落概率。

y = e^(x-28)

```python

import numpy as np
import matplotlib.pyplot as plt
import math

count = 0


def lottery( rand ):
    global count
    if rand <= 0.05 + math.pow( math.e , count - 28  )  :
        count = 0
        return True
    else:
        count += 1
        return False


x1 = np.random.rand(50000)
events = [ i for i,x in enumerate(x1) if lottery(x) ]
interval = np.diff( events )

print( len(events) / len(x1) )

plt.hist( interval, density=True, bins = 50)
plt.show()
```


玩家确实高兴le，老板是不是高兴就不知道了。


最后一种方法是，预先生成掉落表。理想情况下，我们希望稀有掉落的间隔，能够服从正态分布。

我们先稍微看一下正态分布的概率密度图

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

mu = 0
sigma = 1
x = np.linspace(mu - 5*sigma, mu + 5*sigma, 200)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()
```



68.268949%的面积在平均数左右的一个标准差范围内
95.449974%的面积在平均数左右两个标准差
99.993666%的面积在平均数左右四个标准差


















十、注意点

需要保证每次随机的数字都相同，所以需要自己实现一套随机数，不能用unity自带的那个随机数接口，而且需要服务端发送相同的随机种子；因为非常微小的误差就有可能产生蝴蝶效应，所以所有float型的参数必须变成int型，保证计算结果一致。



浮点精度的问题在PC上就有跨平台的问题，因为语言编译器不同使用的寄存器和运算过程中的舍入方式不同。就会导致在不同平台下相同的float运算会出现不同的结果，这方面有很多文章阐述就不多做阐述。而在手机上IOS还好比较单纯，Android设备系统硬件千差万别就更容易出现精度问题了。

定点数 + 辅以三角函数查表

大菠萝3   tracks the amount of time you spend fighting creatures without finding a legendary and after a certain perion of time will slowling start increasing the legendary drop rate.


```python
>>> a = [2,1]
>>> b = [1,2]
>>> np.cross(a,b)
array(3)
>>> a = [2,1,0]
>>> b = [1,2,0]
>>> np.cross(a,b)
array([0, 0, 3])
>>>
```




