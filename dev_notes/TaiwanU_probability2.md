...menustart

 - [5-1: 机率密度函数 PDF (PROBABILITY DENSITY FUNCTION)](#fc548c0411701f3a57c7799ad18245e3)
	 - [PDF](#bcd1b68617759b1dfcff0403a6b5a8d1)
	 - [PDF 跟机率的关系](#0b821c7256491cd7494160a47d4a1023)
	 - [PDF 有哪些性质呢?](#5bc2e5b291e2fbe5196f9a425ad6a0c9)
 - [5-2: 连续机率分布 I (CONTINUOUS PROBABILITY DISTRIBUTION)](#423296d40fd5d59d1f076d73508c42e6)
	 - [Uniform 机率分布](#f7bf1cb803a0ab0539a6dc3ed526dd4f)
	 - [Exponential 机率分布](#894ad572b4888ac89196f741cd003480)
	 - [Erlang 机率分布](#7d09f590df9dfcbd10d1b8cbffce9514)
		 - [Erlang 和 Exponential  关系](#a37b5c85c6d082e170925dbe09051a82)
 - [Week6](#63995e860d87301917bfed4525e36993)

...menuend


<h2 id="fc548c0411701f3a57c7799ad18245e3"></h2>

# 5-1: 机率密度函数 PDF (PROBABILITY DENSITY FUNCTION)

<h2 id="bcd1b68617759b1dfcff0403a6b5a8d1"></h2>

## PDF 

 - 离散的随机变数有 PMF 告诉我们 某个数字发生的机率
 - 连续变数的机率分布常有不均等的情况发生， Ex: 睡觉的时间长度
 - 对连续的随机变量，我们也想知道某个数字 发生的机会多大，可以用 PMF 吗?

---

 - 连续Random Variable  的先天问题
 - 每个数字发生的机率都是 0!
 - 还是很想知道在某个数字发生的机会多大， 怎么办?
 - 先看个乱七八糟的例子
    - 因为拍戏，特别订做合金宝剑
    - 铜、金打造，如何得知有无偷工减料?
    - 整根有质量，但是每点质量都是零?好熟悉!
    - 不看质量看什么?看密度!
    - 密度 at x ≈ (质量 in [x,x+Δx])/Δx  (Δx→0)

---

 - 连续的东西，关键是密度!
 - 宝剑有密度，机率也可有密度!
 - 对随机变数 𝑿 而言，其机率密度:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_pdf.png)

<h2 id="0b821c7256491cd7494160a47d4a1023"></h2>

## PDF 跟机率的关系

 - 因为我们习惯处理机率，看到 PDF 如何把它跟机率连结呢?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_pdf_cdf_relation.png)
 
 - PDF 是 CDF 的微分, CDF 是 PDF 的积分
 - fₓ(x) = lim<sub>Δx→0</sub> P(x≤ X ≤x+Δx)/Δx 
 - 当 Δx 很小时：P(x≤ X ≤x+Δx) = fₓ(x)·Δx
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_pdf_calculus.png)

<h2 id="5bc2e5b291e2fbe5196f9a425ad6a0c9"></h2>

## PDF 有哪些性质呢?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_pdf_property.png)

---

<h2 id="423296d40fd5d59d1f076d73508c42e6"></h2>

# 5-2: 连续机率分布 I (CONTINUOUS PROBABILITY DISTRIBUTION)

<h2 id="f7bf1cb803a0ab0539a6dc3ed526dd4f"></h2>

## Uniform 机率分布

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability2_uniform_dist.png)

 - Ex: 已知1路公交车每十分钟一班。 小美随意出发到公车站，小美须等候公交 车之时间为 X

<h2 id="894ad572b4888ac89196f741cd003480"></h2>

## Exponential 机率分布

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability2_exp_dist.png)

 - 非常漂亮的CDF积分
 - Exponential 分布有失忆的性质 (memoryless)，常被用来 model 有这种性质 的事情
    - Ex: 小美出门化妆所需之时间
    - Ex: 某宅打LOL所花的时间
 - The only memoryless continuous probability distributions are the exponential distributions,
    - `P( X>t+s | X>t ) = P( X>s )`.
     
```
   P( X>t+s | X>t ) = P( X>s )
=> P( X>t+s , X>t ) / P(X>t) = P( X>s )
=> P( X>t+s  ) / P(X>t) = P( X>s )
   let G(t) = P(X>t) 
=> G(t+s) = G(t)G(s)
=> G(a) = G(1)ª  
```

G(a) = G(1)ª = e<sup>log(G(1))·a</sup>

<h2 id="7d09f590df9dfcbd10d1b8cbffce9514"></h2>

## Erlang 机率分布

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability2_Erlang_dist.png)

 - CDF:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability2_Erlang_cdf.pn.png)

--- 

<h2 id="a37b5c85c6d082e170925dbe09051a82"></h2>

### Erlang 和 Exponential  关系

 - Erlang(n,λ) 常被用来model 一件有多个关卡事情的总时间，而每个关卡所 需时间都是随机的 
    - 关卡数: n
    - 每关卡所需时间之机率分布: Exponential( λ )
    - Ex: 打电动过三关所需时间: Erlang(3, λ)
    - Ex: 写完五科作业所需时间

---

<h2 id="63995e860d87301917bfed4525e36993"></h2>

# Week6 

## 6-1: 连续微积分分布 II ( CONTINUOUS PROBABILITY DISTRIBUTIONS )

### Normal 机率分布(常态分布)

 - 常态分布在自然界很常出现
    - Ex: 人口身高分布、体重分布
 - 亦常被用作「很多随机量的总合」的机率模型
    - Ex: 100 人吃饭时间的总合
    - 原因:来自最后会讲到的「中央极限定理」
 - 常态分布，亦常被称作Gaussian (高斯) 机率分布 
 - X ~ Gaussian ( μ,σ )
    - 也常有人用 X ~ N( μ,σ² ) 表示
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_norm_pdf.png)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_norm_pdf_graph.png)
 - CDF是多少?
    - 很难算，积分根本算不出来!
    - 用数值积分法去建表?
        - 很难啊，因为不同的 μ,σ 就会造就 出不同的 常态分布 PDF，每个都要建一个表会要命啊!
    -  怎么办?
        - 有没有办法找到一组特别 μ,σ  ，先针对这组的 CDF 建表， 然后想办法把别的常态分布的 CDF 跟这组 CDF 牵上关系?
        - 若能牵扯上，再利用这表去算出别的常态分布的 CDF 值?

#### Standard Normal Distribution 标准常态分布

 - Z ~ N( 0,1 )
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_std_norm_pdf.png)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_probability_std_norm_pdf_graph.png)

















