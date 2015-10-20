# 你真的会用随机数么

## 随机数
生成 50000个 0-100 随机数

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x1 = np.random.rand(50000)*100
plt.hist(x1, normed=1,  facecolor='green', alpha=0.5)
plt.title('Histogram')
plt.show()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/random_1.png)

分布地很均匀，似乎一切都很美好。


## 随机分布

一只策划狗过来对你说：“我希望5%的概率掉落卡牌A，巴拉巴拉巴拉”。 

你不假思索，信手写下如下伪代码：

```lua
if math.random()<0.05 then
    drop(card_A)
end
```
看上去似乎很完美 
###吗？

我们来观察一下用这种方式产生的 两次卡牌A掉落间隔次数的情况：

先把间隔次数计算出来：

```python
#创建 delta 数据
delta = []
cnt = 0
for i in x1:
    cnt +=1
    if i <= 5 :
           delta.append( cnt ) 
           cnt = 0
```

观察散列图：
```python
x = np.linspace( 1,len(delta),num=len(delta) )

#轴命名
plt.xlabel('drop times')
plt.ylabel('delta')


#画散列图
plt.scatter(x,delta  , s=2 ,   c="#FF0000" )


# 画水平线
plt.plot( [ x[0] ,x[-1] ] ,  [ 20 , 20 ] , 'b' , linewidth=2  )


# title
plt.title('Scatter'  )
plt.show()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/random_2.png)

上图绘制的是卡牌A的掉落间隔，X轴是第几次掉落，Y 轴是 两次掉落 的间隔。

因为卡牌A 的掉率概率是 5%， 所以理想情况是，每20次左右，可以掉落一件。
图中蓝色的线， 就是 20次间隔线。

可以看到，分布并不是我们所期望的在蓝线附近，
出现连续掉落的频率非常高（间隔0），而最坏的情况，要间隔160次才会有下一次掉落，这就是大R们吐槽抽卡纯看脸的原因了。

下图很清晰的反映了这一点

```python
plt.hist( delta , normed=1,  facecolor='blue', alpha=0.5)
plt.title('Histogram')
plt.show()
```
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/random_3.png)

delta 的概率密度图，X轴是间隔数，Y 轴 是各间隔次数 出现的频率 

这样的分布很糟糕，我们期望的分布是 20 出现的概率最大， 20左右概率逐渐减小。 

正态分布 正好符合我们的期望。

## 正态分布
为了方便，直接生成5%掉落率的卡牌A的掉落间隔，检验下正态分布的效果。 

我们使用 位置参数 mu＝20  , 尺度参数 sigma = mu /3.0,  看下分布情况。

```python
np.random.seed(0)
NN = int(50000 *0.05)
mu, sigma = 20, 20/3.0
delta = [int(np.random.normal(mu, sigma)) for i in xrange(NN)]
plt.hist( delta , normed=1,  facecolor='blue', alpha=0.5)
plt.title('Histogram')
plt.show()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/random_4.png)

效果非常好，也是我们想要的。


## 根据权值计算掉落
现在有3种卡牌，掉落的权重分别 20, 30, 50 
我们来计算出一个合理的掉落分布

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

N= 50000
wt = [20, 30, 50 ]
wtp = [1.*x/sum(wt) for x in wt]
result = []
p = [np.random.normal( 1./x, 1./x/3.) for x in wtp]
for i in xrange(N):
	minp = 1.e9
	minj = -1
	for j, pp in enumerate(p):
		if pp < minp:
			minp = pp
			minj = j
	result.append(minj)
	for j, pp in enumerate(p):
		p[j] -= minp
	p[minj] = np.random.normal(1./wtp[minj], 1./wtp[minj]/3.)
```


测试生成的数据

```python
#计算各个权重的 delta
deltas = []
for j in xrange( len( set( result ) ) ):
	delta = []
	deltas.append( delta )
	cnt = 0
	for i in result:
		cnt +=1
		if i==j :
			delta.append( cnt ) 
			cnt = 0


plt.title('Histogram')
colors = [  "b" , 'g',"r" , "c" , "m" , "y" , "k" , "#FF00FF" , "#800080"  ]

#plt.ylim(0, 0.5)

plt.hist( deltas ,histtype='barstacked' ,  normed=1,     alpha=0.5  ) #facecolor= colors[j]
plt.show()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/random_5.png)


## 移植到lua

lua 标准库没有正态分布的实现(np.random.normal)，我们可以简单的实现一个

```lua
local NV_MAGICCONST = 1.71552776992

local function normalvariate(random, mu, sigma)
    --[[Normal distribution.
    
    mu is the mean, and sigma is the standard deviation.
    
    --]]
    -- mu = mean, sigma = standard deviation
    
    -- Uses Kinderman and Monahan method. Reference: Kinderman,
    -- A.J. and Monahan, J.F., "Computer generation of random
    -- variables using the ratio of uniform deviates", ACM Trans
    -- Math Software, 3, (1977), pp257-260.
    
    while true do
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST*(u1-0.5)/u2
        zz = z*z/4.0
        if zz <= -math.log(u2) then
            break
        end
    end
        
    return mu + z*sigma

end
```
