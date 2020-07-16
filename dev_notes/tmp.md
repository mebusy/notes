...menustart


...menuend


在游戏开发中，经常需要使game play具备一些不确定性，比如抽奖中稀有物品的掉落，或者攻击的时候暴击的产生，等等。 这些情况下，我们一般就需要用到随机数。

Random Number


软件开发中, 随机数， 一般都是特值 伪随机数。

Pseudo random number


伪随机数，是指一组分布在某个特定范围内的数字序列。

```python
import numpy as np
[ np.random.randint( 64 ) for i in range(10)]
```

这些数字看起来毫无规律，但实际上是, 他们是由某个特定的数学算法生成的, 这个随机数序列是完全可以预测和重现的。 

生成随机数序列的算法有很多。 出于讲解方便的目的 ，


在这里，我们举例介绍一下其中的一个最古老简单的随机数算法, 线性同余生成器。

Linear Congruential Generator


线性同余生成器

需要选择4个魔术数字


1个种子  Seed, S

一个 乘数 multiplier , a ,

 一个增量increment  c , 

 一个模数modulus  m 

  ( S * a  + c ) mod m 

很简单的公式， 括号里的 就是线性的部分，右边的就是取余数。

S = ( S * a  + c ) mod m -> rand


计算结果 用于输出随机数  的同时，本身也会 会成为新的种子 S

```python
class LCG():
    def __init__( self, seed, mul, inc , mod ):
        self.seed = seed
        self.mul = mul
        self.inc = inc
        self.mod = mod

    def next(self):
        self.seed = (( self.mul * self.seed + self.inc ) % self.mod)
        return self.seed


if __name__ == "__main__":
    lcg = LCG( 7,7,7, 10  )
    print( [ lcg.next() for i in range(16) ] )


    lcg = LCG( 7, 5 ,1, 16  )
    print( [ lcg.next() for i in range(20) ] )
```

M,a,c 组合 并不总是随机的，

展示了一个事实，线性同于序列最终 总是会进入一个循环。

这是为什么呢？

因为这些输出， 本身又是作为下一次计算的 输入，所以当我们在 我们的输出序列中看到重复的数字的时候，那我们就知道，整个数列就进开始进入循环了。

所以我们的另一个任务，就是选择好的  s,m,a,c 的组合，使得我们的输出序列拥有尽可能大的循环周期。 这些数字选择的原则和证明比较冗长繁琐，有兴趣的同学可以去看 算法大师高德纳 计算机程序设计艺术 The Art of Computer Programming  第二卷。

这里我们直接使用选择好的一组数字.



现在我们已经对随机数是如何产生的，有了一个初步的了解。接下去，我们要探讨一下如何正确的在游戏中使用随机数。

------------------------------

我们先来看一下随机数的分布问题。

我们先来生成 50000个 0-100 随机数，

```
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(50000)*100
plt.hist( x1, density=True )
plt.show()
```

从直方图可以看到， 我们生成的随机数是呈均匀分布.

假设现在策划有一个抽卡的需求，他希望有5%概率 掉落稀有卡牌A。

很简单的需求，你不假思索，信手写下如下伪代码：

```
if math.random()<=0.05 then
    drop(card_A)
end
```

这个逻辑有没有什么潜在的问题呢？ 我们来深入这个问题看一下。

x1 是我们的生成随机数， 对于x1中的每个随机数x 当 x `<=` 5 , 则稀有卡牌掉落的事件发生。


```
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(50000)*100

events = [ i for i,x in enumerate( x1 ) if x <= 5 ]
# print(events, density=True)

interval = np.diff( events )
# print(interval)

plt.hist( interval , density=True )
plt.show()

x = np.linspace( 1,len(interval),num=len(interval) )
# plt.scatter(x,interval, s=2, c="#FF0000" )
# plt.plot( [ x[0] ,x[-1] ] , [ 20 , 20 ] , 'b' , linewidth=2  )
# plt.show()
```


这说明 掉落事件本身没有太大的问题，现在我们来看一下 两次稀有掉落的事件间隔


一个常用的做法，是使用计数器。 给每个玩家维护一个计数器，玩家抽卡一次，计数器加1， 如果抽中了稀有卡，计数器清零，并且设置一个阈值，比如25， 当计数器累加到阈值的时候，也就是玩家已经连续25次抽卡都没有抽中的时候，按抽中处理，  同时计数器清零。

这种实现好处就是简单。但是，这个方案仅仅是改善了 玩家抽很多次抽不到的体验，并且，总体上说，这种做法其实是增加了这张稀有卡的掉率。玩家确实高兴le，老板是不是高兴就不知道了。


计数器还有一个变种，改成慢慢地提高掉落的概率。比如大菠萝3 就是使用的这种方式。 他会记录你杀怪的时间，如果长时间没有掉落 Legendary 传奇装备，就会逐渐地提高 传奇装备的掉落概率。





直方图(Histogram)，又叫质量分布图, 可以很方便地把我们的数据的形状和分布 可视化出来。

















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




