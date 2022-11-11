[](...menustart)

- [Week 4 离散机率分布](#07e1b9e336ae6e129168b900f3158d5d)
    - [4.1 随机变数 (RANDOM VARIABLE)](#a4c3bd594c5ea4f3fc9fcce3586fbf18)
        - [探究它的本质!](#a33ac1d92bc31a31da5665a97aadb111)
        - [随机变数的种类](#e644c0d51064d3032fe3d27919ffe3da)
        - [神马叫可数?神马叫不可数?](#5bf91f651f94a7d5ba4a11ac547d51d6)
        - [随机变量的函数?](#1665de2424d65db6d533386753911167)
    - [4.2 累积分布函数 CDF (CUMULATIVE DISTRIBUTION FUNCTION)](#d6fd0c71fd9be392edd5a91921b0eaf3)
        - [CDF 有什么用?](#c3d3b89aedf13c4a6de6f558a6a0cfa9)
        - [离散随机变数的 CDF 长怎样?](#917493f1d72a878df54e59714b677430)
        - [连续随机变数的 CDF 长怎样?](#7f7cd8bcf7af60bb124933e0f7db3150)
        - [CDF 的性质](#d3f28a5c19885b5e4ef1cb86d56b356b)
    - [4.3 机率质量函数 PMF (PROBABILITY MASS FUNCTION)](#df629b43f1e17bdd8b59ff70feb570a8)
        - [PMF 跟 CDF 的关系?](#a8699842209b391b17b7623a4c1b85d8)
        - [机率分布 (Probability Distribution)](#5a70965e6e318af45220c5484c2b8dc4)
    - [4.4 离散机率分布 I (DISCRETE PROBABILITY DISTRIBUTIONS)](#68e8045f19a785d2e1b77ac7870d2076)
        - [Bernoulli 机率分布](#ed43ca1c9bb0671f81bb3bdeaf8c6095)
        - [Binomial 机率分布](#e0dc24e9ac7e53085bd7bc2a2775917e)
        - [Uniform 机率分布](#f7bf1cb803a0ab0539a6dc3ed526dd4f)
        - [Geometric 机率分布](#7903bb94dad83aeea3bf8559e6cdd143)
        - [Pascal 机率分布](#f7b44a579af87c25b4b1cf0b98602a56)
        - [Poisson 机率分布](#66e278878307932e688a55d600961fdf)
            - [和Binomial 的关系](#583ba9bfcbd2e04c6f0f65a92061f123)

[](...menuend)


<h2 id="07e1b9e336ae6e129168b900f3158d5d"></h2>

# Week 4 离散机率分布

<h2 id="a4c3bd594c5ea4f3fc9fcce3586fbf18"></h2>

## 4.1 随机变数 (RANDOM VARIABLE)

- 考虑前面费雯兄的例子, 若根据统计，费雯兄一楼推文 不同型态只有4种, 若
    - P(「你妈知道你在发废文吗」 ) = 0. 4
    - P( 「见此唉滴必嘘」) = 0. 2
    - P( 「在五楼...」) = 0. 1
    - 推测 P( 「妈!我在这!」) 的概率
    - P(「妈!我在这!」 ) = 1 − P( 「你妈知道你在发废文吗」) − P( 「见此 唉滴必嘘」) − P( 「在五楼...」) = 0. 3 
- 光写字就累翻了!!!
- 若改为:
    - 「你妈知道你在发废文吗」:X = 0
    - 「见此唉滴必嘘」:X = 1
    - 「在五楼...」:X = 2
    - 「妈!我在这!」:X = 3
    - 根据统计:  P(X=0)=0.4;P(X=1)=0.2;P(X=2)=0.1;P(X=3)=0.3
        - P(X=3) = 1 - P(X=0) - P(X=1) - P(X=2)
    - 跟前面比起来，你觉得如何呢? 这...这...真是太清爽、太给力了

---

- 随机变数 (Random Variable, R.V.) 这是一个用来把实验结果 (outcome) ***数字化*** 的表示方式
- 目的是可以让机率的推导更数学、更简明
- 前面例子中的 X 就是所谓的 ***随机变数***
- 随机变数通常都是用 ***大写的英文字母*** 表示!

<h2 id="a33ac1d92bc31a31da5665a97aadb111"></h2>

### 探究它的本质!

- 随机变量的本质是什么?
    - 本质是一个 ***函数***
    - 「你妈知道你在发废文吗」:X = 0  =>  X(「你妈知道你在发废文吗」 ) = 0
- 随机变数 X 其实是一种函数，喂 X 吃一个 outcome ，就吐出一个对应的数字。数学上的表示法:
    - X: S → ℝ

<h2 id="e644c0d51064d3032fe3d27919ffe3da"></h2>

### 随机变数的种类

- 离散随机变数 (Discrete R. V.)
    - Ex:宅vs.店员:X(微笑)=0,X(不笑)=1  => X = 0, X = 1
    - Ex:小明告白多少次才成功:X(0次)=0,X(1次)=1,X(2次)=2,...  => X = 0, X = 1, X = 2, ...
    - 离散 R.V. 的值是有限个，或是「可数的」无穷多个
- 连续随机变数 (Continuous R. V.)
    - 幸运之轮: X 可以是 0 到 1 间内的任意数字
    - 连续 R.V. 的值是有无穷多个，而且是「不可数」的无穷多个


<h2 id="5bf91f651f94a7d5ba4a11ac547d51d6"></h2>

### 神马叫可数?神马叫不可数?

- 重要性质:0 到 1 之间的所有数字的集合是不可数的!
- 「正整数的集合」 跟 「正偶整数」的集合 相比，哪个集合里面东西比较多?  一样多
- 「长度为一的线段上的点」跟「边长为一的正方形上的点」， 这两个集合，哪一个点的数量比较多?  一样多
- 因为都可以找到一对一对应的方法。

<h2 id="1665de2424d65db6d533386753911167"></h2>

### 随机变量的函数?

- 阿宅若看到店员微笑，就会点$200 的套餐。如果店员不笑，他就买 $15 的饮料。 请问阿宅的消费金额 W是随机变数吗?
    - 店员表情可以由随机变量 X 代表: X(微笑) = 0, X(不笑) = 1
    - W是 X 的函数:W(X(微笑)) = 200, W (X(不笑)) = 15
    - 所以 W也是喂 outcome 吐数字!因此 W也是一个随机变数!
    - 记住:随机变量的函数，也是一个随机变量喔!

---

<h2 id="d6fd0c71fd9be392edd5a91921b0eaf3"></h2>

## 4.2 累积分布函数 CDF (CUMULATIVE DISTRIBUTION FUNCTION)

- 对任一个随机变数 X ，我们定义 其 CDF 为函数:
    - F<sub>X</sub>(x) = P(X ≤ x) 
    - ![](../imgs/TU_probability_cdf.png)
    - 其中 X 是随机变数
- Ex 幸运之轮  F<sub>X</sub>(0.5) = P(X≤0.5) = 1/2
 
 
<h2 id="c3d3b89aedf13c4a6de6f558a6a0cfa9"></h2>

### CDF 有什么用?
 
- 最有用的用途: 计算 X 落在某范围内的机率
    - P(3< X≤ 5 ) = P(X≤ 5) - P( X<= 3)
    - **= F<sub>X</sub>(5) - F<sub>X</sub>(3)**
    - ![](../imgs/TU_probability_cdf_ab.png)
- P( a < X ≤ b ) = F<sub>X</sub>(b) - F<sub>X</sub>(a)
- P( a ≤ X ≤ b ) = F<sub>X</sub>(b) - F<sub>X</sub>(a) + P(X=a)

<h2 id="917493f1d72a878df54e59714b677430"></h2>

### 离散随机变数的 CDF 长怎样?

- Ex:X为骰子的点数，故P(X=1) =P(X=2) =P(X=3) =P(X=4) =P(X=5) =P(X=6) =1/6
- CDF: F<sub>X</sub>(x) = P(X ≤ x)
    - ![](../imgs/TU_probability_discrete_pdf.png)
- P( 3< X≤ 5 ) = F<sub>X</sub>(5) - F<sub>X</sub>(3) = 5/6 - 3/6 = 2/6
- P( 3< X< 5 ) = P( 3< X≤ 5⁻ ) = F<sub>X</sub>(5⁻) - F<sub>X</sub>(3)  = F<sub>X</sub>(5) - P(X=5) - F<sub>X</sub>(3) = 1/6

<h2 id="7f7cd8bcf7af60bb124933e0f7db3150"></h2>

### 连续随机变数的 CDF 长怎样?

- Ex: X 为幸运之轮所停下的数字，X ∈ [ 0,1 )    
    - CDF: F<sub>X</sub>(x) = P( X ≤ x )
    - ![](../imgs/TU_probability_conti_cdf.png)
- P( 0.3< X≤ 0.5 ) = F<sub>X</sub>(0.5) - F<sub>X</sub>(0.3) = 0.5 - 0.3 = 0.2
- P( 0.3< X< 0.5 ) = F<sub>X</sub>(0.5⁻) - F<sub>X</sub>(0.3) = 0.5 - 0.3 = 0.2


<h2 id="d3f28a5c19885b5e4ef1cb86d56b356b"></h2>

### CDF 的性质

- 离散随机变数之CDF:
    - F<sub>X</sub>(x⁺) = F<sub>X</sub>(x)
    - F<sub>X</sub>(x⁻) = F<sub>X</sub>(x) - P(X=x)
- 连续随机变数之CDF:
    - F<sub>X</sub>(x⁺) = F<sub>X</sub>(x⁻)  = F<sub>X</sub>(x) 
- 共同性质
    - F<sub>X</sub>(-∞) = P(X≤-∞) = 0
    - F<sub>X</sub>( ∞) = P(X≤ ∞) = 1  
    - 0 ≤ F<sub>X</sub>(x) ≤1
 
---

<h2 id="df629b43f1e17bdd8b59ff70feb570a8"></h2>

## 4.3 机率质量函数 PMF (PROBABILITY MASS FUNCTION)

- 只有 离散随机变数 有 PMF
- 对任一个整数值的 ***离散随机变数*** X , 我们定义其 PMF 为函数(小写p):
    - p<sub>X</sub>(x) = P(X=x)
- Ex: X 为公平骰子之点数
    - p<sub>X</sub>(3) = P(X=3) = 1/6

<h2 id="a8699842209b391b17b7623a4c1b85d8"></h2>

### PMF 跟 CDF 的关系?

- PMF -> CDF
    - ![](../imgs/TU_probability_cdf_pmf.png)
- CDF -> PMF
    - P<sub>X</sub>(x) = F<sub>X</sub>(x⁺) - F<sub>X</sub>(x⁻)


<h2 id="5a70965e6e318af45220c5484c2b8dc4"></h2>

### 机率分布 (Probability Distribution)

- 任何一个 PMF(或是之后介绍的 PDF)都称作是一种 ***机率分布*** (将总和为 1 的机率分布在点上之故)
    - ![](../imgs/TU_probability_PD.png)

---

<h2 id="68e8045f19a785d2e1b77ac7870d2076"></h2>

## 4.4 离散机率分布 I (DISCRETE PROBABILITY DISTRIBUTIONS)
 
- 观察一下
    - 丢掷铜板:非正面，即反面，正面机率为 0.5
    - 出门天气:非晴天，即雨天，晴天机率为 0.6
- 1 次实验，2 种结果。 在意某结果发生否  Bernoulli 机率分布
    

<h2 id="ed43ca1c9bb0671f81bb3bdeaf8c6095"></h2>

### Bernoulli 机率分布

- PMF: 若实验成功机率为 p , 作 1 次实验， X 表成功次数
- CDF 见右图

![](../imgs/TU_probability_bernoulli.png)

---

<h2 id="e0dc24e9ac7e53085bd7bc2a2775917e"></h2>

### Binomial 机率分布

- 观察一下
     - 阿宅鼓起勇气搭讪 10 人，若每次搭讪成 功机率为 0.6，10 次成功 8 次的机率为?
     - 一周 5 天午餐在晓福买魔石汉堡，若每次制作超时机率为 0.9 5 天中有 3 天制作超时的机率为?
     - 一周有 3 系夜，在活大乱停车 3 次，若每次遭阿伯拖之机率 为 0.8，那这 3 次被拖 2 次之机率为?
- 作 n 次实验，1 个机率，在意 n 次实验出 现某结果 k 次之机率 --> Binomial 机率分布
    
- 若实验成功几率为 0.6， 做10次实验， X表示成功次数
    - ![](../imgs/TU_probability_binomial1.png)
    - left is PMF, right is CDF
- PMF: 若实验成功机率为 p, 作 n 次实验， X 表成功次数
    - ![](../imgs/TU_probability_binomial2.png)

```python
import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.binomial( 10, 0.6 , 100000 )
# If you want the sum of all bars to be equal 1, weight each bin by the total number of values:
weights = np.ones_like(x1)/float(len(x1))
plt.hist(x1, normed=False, weights=weights, facecolor='green', alpha=0.5,bins=100)
plt.show()
```

![](../imgs/TU_probability_Binomial_10_06_graph.png)


- another method, use scipy

```python
import scipy, scipy.stats
x = scipy.linspace(0,10,11)
pmf = scipy.stats.binom.pmf(x,10,0.6)
import pylab
pylab.plot(x,pmf)
pylab.show()
```

![](../imgs/TaiU_probability_binom2.png)



<h2 id="f7bf1cb803a0ab0539a6dc3ed526dd4f"></h2>

### Uniform 机率分布

- 观察一下        
    - 丢公平骰:1 到 6 各点数出现机会均等
    - 混哥考试:作答 A, B, C, D 机会均等
    - 狡兔三窟:出现在窟 1、窟 2、窟 3 机会均等
- 1 次实验，n 种结果，各结果机率均等。在意某结果发生否 -->  Uniform 机率分布
- 如果 X 等于 3,4,...,7 的机率均等
    - ![](../imgs/TU_probability_uniform1.png)
- 如果X等于a,a+1...,b 的机率均等
    - ![](../imgs/TU_probability_uniform1.png)


<h2 id="7903bb94dad83aeea3bf8559e6cdd143"></h2>

### Geometric 机率分布

- 观察一下
    - 阿宅告白:成功机率为 0.3，不成功誓不休。 问到第 5 次才告白成功之机率?
    - 孙文革命:成功机率为 0.1，不成功誓不休。问到第 11 次才 成功之机率?
    - 六脉神剑:那纠缠狂妈宝废物段誉每次要打出六脉神剑，打 的出来的机率为 0. 1。他在 10 次才打出六脉神剑的机率?
- 实验中出现某结果机率已知，重复操作实验至该结果出现为止。 在意某结果是在第几次实验才首次出现 --> Geometric 机率分布
- 六脉神剑:那妈宝废物段誉每次要打 六脉神剑，打的出来的机率为 0.1。他在第 10 次 才打出六脉神剑的机率?
    - 败败败败败败败败败成 => 机率 = 0.9⁹ x 0.1
- 六脉神剑:那妈宝废物段誉每次要打 六脉神剑，打的出来的机率为 p 。他在第 X 次 尝试才成功打出六脉神剑。 X = x 的机率?
    - 机率 = (1-p)<sup>x-1</sup> · p
- 若实验成功机率为 p，尝 试到成功为止，作了 X 次尝试
    - ![](../imgs/TU_probability_geometric.png)
- 有失忆性！ 离散分布中唯一的失忆性分布

```python
import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.geometric( 0.3 , 100000  )
weights = np.ones_like(x1)/float(len(x1))
plt.hist(x1, normed=False,weights=weights, facecolor='green', alpha=0.5,bins=100)
plt.title('p = 0.3')
plt.show()
```

![](../imgs/TU_probability_geometric_03_graph.png)


```python
import scipy, scipy.stats
x = scipy.linspace(0,10,11)
pmf = scipy.stats.geom.pmf(x, 0.3 )
import pylab
pylab.plot(x,pmf)
pylab.show()
```

![](../imgs/TU_probability_geometric_03_graph2.png)




<h2 id="f7b44a579af87c25b4b1cf0b98602a56"></h2>

### Pascal 机率分布

- 观察一下   
    - 自尊阿宅:阿宅邀约店员失败机率为 0.9， 若邀约失败达 4 次，阿宅便会自尊有损而放弃追求。问在阿 宅第 7 次邀约时决定放弃追求之机率?
    - 六脉神剑:妈宝废物段誉每次打成功 5 次六脉神剑便功力耗 尽。若每次打的出来的机率为 0. 1。请问他在第 9 次时刚好 功力耗尽的机率?
- 实验中出现某结果机率已知，重复操作实验至该结果出现第 k 次 为止。在意到底在第几次实验才结束 --> Pascal 机率分布
- 六脉神剑:那妈宝废物段誉每次要打 六脉神剑，打的出来的机率为 0.1。成功 5 次便功 力耗尽。请问他在第 9 次时刚好功力耗尽的机率?
    - 可能情况之一:败 成 败 成 败 成 成 败 成
    - 此情况机率 = 0.9⁴ x 0.1⁵
    - 刚好第9次才成功第5次的情况有几种?  C(8,4)·C(1,1) = C(8,4)
    - 所求机率 =  C(8,4) x 0.9⁴ x 0.1⁵ 
- 六脉神剑:那妈宝废物段誉每次要打六脉神 剑，打的出来的机率为 p 。成功 k 次便功力耗尽。 他在第 X 次尝试才成功打出 k 次六脉神剑。 X = x 的机率?
    - C(x-1, k-1) x (1-p)<sup>x-k</sup> x pᵏ
- 若实验成功机率为 p , 到第 k 次成功为止共作了 X 次
    - ![](../imgs/TU_probability_pascal.png)

```python
import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.negative_binomial( 5, 0.1 , 100000  )
weights = np.ones_like(x1)/float(len(x1))
plt.hist(x1, normed=False, weights=weights, facecolor='green', alpha=0.5,bins=500)
plt.title('k=5, p=0.1')
plt.show()
```

![](../imgs/TU_probability_Pascal_k5_p01_graph.png)


```python
import scipy, scipy.stats
x = scipy.linspace(0,100,101)
pmf = scipy.stats.nbinom.pmf(x,5,0.1)
import pylab
pylab.plot(x,pmf)
pylab.show()
```

![](../imgs/TU_probability_Pascal_k5_p01_graph2.png)

<h2 id="66e278878307932e688a55d600961fdf"></h2>

### Poisson 机率分布
 
- 观察一下  
    - 转角夜宵:在晚上 平均每小时会有 10 人 来 跟转角哥买夜宵。 问摆摊 5 小时 有 60 人光顾之机率?
    - 费雯被嘘:费雯兄 po 文后， 平均每分钟会有 5 人嘘之 。 问发文后 二十分钟 变成 X 之机率?
- 某结果出现之平均速率(rate: 次数/时间)已知。问持续观察某 时间长度后，看到该结果出现 k 次之机率? --> Poisson 机率分布
- 已知某事发生速率为每单位时间 λ 次，观察时间为 T 时间单位。 X 为该观察时间 内发生该事的总次数。则:
    - PMF: ![](../imgs/TU_probability_poisson_PMF.png)
    - CDF: ![](../imgs/TU_probability_poisson_CDF.png)
- 费雯被嘘:费雯兄 po 文后，平均 每分钟会有 5 人嘘之。问发文后 20 分钟变 成 XX (80 嘘) 之机率?
    - λ = 5 嘘/分，若定义随机变量 X 为 20 分钟内的嘘数
    - => X ~ POI(λT) = POI(100) = e⁻¹⁰⁰·100⁸⁰ / 80! 
    - 若条件是 每小时 300人嘘之，答案一样
        ```python
        >>> scipy.stats.poisson.pmf( 80, 100 )
        0.005197854125980
        >>> (math.e**-100)*(100**80)/math.factorial(80)
        0.005197854125980
        ```
- 理解泊松分布的特性:
    - 它常用来描述大量随机试验中稀有事件出现的次数
    - 比如 抽卡抽到 詹姆斯卡次数 ?  


```python
# 被嘘
# u = 5 * 20 == 100
import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.poisson( 100 , 100000  )
weights = np.ones_like(x1)/float(len(x1))
plt.hist(x1, normed=False, weights=weights, facecolor='green', alpha=0.5,bins=100)
plt.show()
```


![](../imgs/TU_probability_poisson_dist_graph2.png)

```python
import scipy, scipy.stats
x = scipy.linspace(50,150,101)
pmf = scipy.stats.poisson.pmf(x, 100 )
import pylab
pylab.plot(x,pmf)
pylab.show()
```

![](../imgs/TU_probability_poisson_dist_graph3.png)


<h2 id="583ba9bfcbd2e04c6f0f65a92061f123"></h2>

#### 和Binomial 的关系

- 将T 划分成 长度为ΔT的小段 , 共有 n= T/ΔT 个小段
- 若发生速率为λ次/分, 每个小段会发生的机率 p= λΔT = λT/n
- 故 T时间内发生的次数 X~BIN(n,p) = BIN(n,λT/n)


- 泊松分布通常也用于二项分布的近似计算。
    - 当n很大，而p很小时，在没有计算机时，二项分布的计算是非常麻烦的，而用泊松分布来近似计算可以降低大量的计算量。
    - 一般来讲，n≥100，np≤10近似效果较好。



-----

 [1]: ../imgs/TU_probability_deduction_02.png





