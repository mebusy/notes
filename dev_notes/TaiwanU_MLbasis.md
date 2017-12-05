...menustart

 - [Week1  The Learning Problem](#ecde0ae599ab9118d10cbcd51ecbaab0)
 - [Week2 Learning to Answer Yes/No](#5868daf5782375dc2181821611a1a15c)
     - [Perceptron Hypothesis Set](#85afcca55926ce0a29f0f6cb05850a9d)
         - [Perceptron](#d8d47e427c95153bb9f8bec1d2d1df94)
         - [Vector Form of Perceptron Hypothesis](#7f75552635f2c71b44d8ec37aefb9df7)
         - [Perceptrons in ℝ²](#b07c3735cd2797ec2b778d92a0adf769)
     - [Perceptron Learning Algorithm (PLA)](#0e7ff491a0fb09097115fb8590ecddb5)
         - [Practical Implementation of PLA](#03ed0e617baca54a8f30c4314b8395c6)
         - [Why PLA may work](#2c4c57a7143770c331971f4ce207c2e2)
     - [Guarantee of PLA](#e3f4c08eab2f66995b163ecf47f53898)
         - [Linear Separability](#fafcae75a7ed33e57480616db662b7ce)
         - [PLA Fact : W<sub>t</sub> Gets More Aligned with W<sub>f</sub>](#1e0adff1d0ebad51a3e3366ffd90c42a)
         - [PLA Fact : W<sub>t</sub> Does Not Grow Too Fast](#4881687a06277027c5043e17bc1b09df)
     - [Non-Separable Data](#3baec9e63797786ab9197c8328006b4c)
         - [Pocket Algorithm](#b84fec7e58d78ac3562f365b9a0ba808)
 - [Week 3 Types of Learning](#802179691269a6cfc6518c10b66d4776)
     - [Learning with Different Output Space](#e4561cdae64f2ab23476660e7fcd3596)
         - [Multiclass Classification: Coin Recognition Problem](#8aea726ae5a16d695949a7fdb31468f9)
         - [Structured Learning : Sequence Tagging Problem](#a5756f5557e96b4c381b0eff885d54ce)
     - [Learning with Different Data Label](#684c38a5e13528daec2ab3efa2097be3)
     - [Learning with Different Protocol](#6def4688e7d3b9cfc2f058ed2729c813)
     - [Learning with Different Input Space](#6ebd75d7ad445321e62d64acb494084a)
 - [Week 4 Feasibility of Learning](#cfd8a0e711b39b612b7fd7279a78d83e)
     - [Probability to the Rescue](#e2757331874147511e796bb57cd0130f)
         - [Hoeffding's Inequality](#2738a5bd77944b4f0a65a05dcf269384)
     - [Connection to Learning](#4d3ee8b9af56c703975b205e29f34cfa)
         - [The Formal Guarantee](#bc490f18155779c237c38b6532ca7b7f)
         - [Verification of One h](#911f375f353e71713d92e0e8d439e40e)
     - [Connection to Real Learning](#d9ee0f5ea86476845fea40190ab1462e)
         - [Coin Game](#9ba5efcb15754a3919e1c165c9746157)
         - [BAD Sample and BAD Data](#0f6ca2986821d310f080364af49eed46)
         - [BAD Data for Many h](#16553486c255ce8a5d8e557b67c3c9a6)
         - [Bound of BAD Data](#c82862b9ceccd7efd1ca9d2bab635903)
         - [The 'Statistical Learning Flow'](#d8634320f9db8392b907e680f3fbdeef)

...menuend


<h2 id="ecde0ae599ab9118d10cbcd51ecbaab0"></h2>

# Week1  The Learning Problem

 - *Algorithm* takes *Data* and *Hypothesis set*  to get final hypothesis *g*.
    - H: set of candidate formula , with different weights W

<h2 id="5868daf5782375dc2181821611a1a15c"></h2>

# Week2 Learning to Answer Yes/No

<h2 id="85afcca55926ce0a29f0f6cb05850a9d"></h2>

## Perceptron Hypothesis Set

<h2 id="d8d47e427c95153bb9f8bec1d2d1df94"></h2>

### Perceptron

 - x = { x₁,x₂,...,x<sub>d</sub> }
 - y = { +1 | -1  }
 - h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ - threshold  )

<h2 id="7f75552635f2c71b44d8ec37aefb9df7"></h2>

### Vector Form of Perceptron Hypothesis
    
 - 把 *threshold* 也当成是一个特殊的 w₀

```
h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ - threshold  )
h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ + (-threshold)*(+1)  )
h(x) = sign( ∑ᵈᵢ₌₀ wᵢxᵢ )
h(x) = sigh ( WᵀX )
```

<h2 id="b07c3735cd2797ec2b778d92a0adf769"></h2>

### Perceptrons in ℝ²

 - h(x) = sign( w₀ +w₁x₁ +w₂x₂ )
    - h(x) = 0 is a **lines** ( ir hyperplanes in ℝᵈ )

 - perceptrons <=> **linear (binary) clasifiers**
    - PS. (2D空间下) 二元分类也并不仅限与 直线划分的情况，h(x)=0 也可以是一条曲线。只是这个perceptron 是直线情况



<h2 id="0e7ff491a0fb09097115fb8590ecddb5"></h2>

## Perceptron Learning Algorithm (PLA)

 - will represent *g₀* by its weight verctor W₀ 
 - 如果 直线 *g*=0 还不完美，我们一定可以找得出 资料中的某一个点 ( x<sub>n(t)</sub> , y<sub>n(t)</sub>  ) , 在这个点上  *g* 犯了错 
 - 犯了错，我们就要想办法来修正它 ， 如何修正？
    - 如果 y 应该是正的，g 得到的是负的，说明 W,X 的角度太大， 那我们就把 向量W 转回来;反之，我们把向量W  转开
    - 这两种情况，可以统一的由 `W=W+yx` 处理
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_correct.png)
 - 算法伪代码如下:

i[](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_pseudo.png)

 - A fault confessed is half redressed.
 - Weight Space
    - A point in the space represents a particular setting of  W
    - each training case X can be represented as a hyperplane through the origin.
        - The plane goes through the origin and is perpendicular to the input vector X .
    - The weights must lie on one side of this hyper-plane to get the answer correct.
    - 更具体的 weight space 说明，见 [Neural Networks](https://github.com/mebusy/notes/blob/master/dev_notes/NeuralNetworks.md)
        - 实践中，也能把 W，X角色互换也可以？

<h2 id="03ed0e617baca54a8f30c4314b8395c6"></h2>

### Practical Implementation of PLA 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_CyclicPLA_pseudo.png)

<h2 id="2c4c57a7143770c331971f4ce207c2e2"></h2>

### Why PLA may work 

 - sign(WᵀX) != y<sub>n</sub> ,  W<sub>t+1</sub> <-  W<sub>t</sub> + y<sub>n</sub>X<sub>n</sub>
 - y<sub>n</sub>W<sub>t+1</sub>X<sub>n</sub> >=  y<sub>n</sub>W<sub>t</sub>X<sub>n</sub>
    - 如果y<sub>n</sub> 是负的，算法的作用是 努力使WᵀX往正的方向努力，使得更接近正确的 y

<h2 id="e3f4c08eab2f66995b163ecf47f53898"></h2>

## Guarantee of PLA

<h2 id="fafcae75a7ed33e57480616db662b7ce"></h2>

### Linear Separability

 - if PLA halts (i.e. no more mistakes) , ( **necessary condition** ) D allows some *W* to make no mistake 
 - call such D **linear separable**

<h2 id="1e0adff1d0ebad51a3e3366ffd90c42a"></h2>

### PLA Fact : W<sub>t</sub> Gets More Aligned with W<sub>f</sub>

 - linear separable D <=> exists perfect  W<sub>f</sub> such that y<sub>n</sub> = sign(  W<sub>f</sub>ᵀx<sub>n</sub> )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_fact1.png)

 - 由上可以，如果 W<sub>t</sub> 的长度没有变长的话，那么可以看到 PLA 使得  W<sub>t</sub> 更加接近W<sub>f</sub> 

<h2 id="4881687a06277027c5043e17bc1b09df"></h2>

### PLA Fact : W<sub>t</sub> Does Not Grow Too Fast 

 - W<sub>t</sub> changed only when mistake 
    - <=> sign( W<sub>t</sub>ᵀx<sub>n(t)</sub> ) ≠ y<sub>n(t)</sub> 
    - <=> y<sub>n(t)</sub> W<sub>t</sub>ᵀx<sub>n(t)</sub> ≤ 0  (WX和y 异号)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_fact2.png)

 - 综合这两条，我们可以得到

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_fact_conclude.png)

 - Guarantee
    - as long as *linear separable* and *correct by mistake*
    - inner product of W<sub>f</sub> and W<sub>t</sub> grows fast; length of W<sub>t</sub> grows slowly
    - PLA 'lines' are more and more aligned with W<sub>f</sub> => halts

<h2 id="3baec9e63797786ab9197c8328006b4c"></h2>

## Non-Separable Data

<h2 id="b84fec7e58d78ac3562f365b9a0ba808"></h2>

### Pocket Algorithm

 - modify PLA (black lines) by keeping best weights in pocket

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_modify_pseudo.png)


<h2 id="802179691269a6cfc6518c10b66d4776"></h2>

# Week 3 Types of Learning

<h2 id="e4561cdae64f2ab23476660e7fcd3596"></h2>

## Learning with Different Output Space

<h2 id="8aea726ae5a16d695949a7fdb31468f9"></h2>

### Multiclass Classification: Coin Recognition Problem 

 - classify US coins (1c,5c,10c,25c)
    - y = {1,2,...,K}
 - written digits => 0,1,...,9
 - picture => apple, orange , strawberry

<h2 id="a5756f5557e96b4c381b0eff885d54ce"></h2>

### Structured Learning : Sequence Tagging Problem

 - multiclass classification : word => word class
 - structured learning :
    - sentence => structure (class of each word)
 - y = { PVN,PVP,NVN,PV,... } , not including VVVVV
 - huge multiclass classification problem 
    - (structure ≡ hyperclass) without 'explicit' class definition

<h2 id="684c38a5e13528daec2ab3efa2097be3"></h2>

## Learning with Different Data Label

 - Supervised : all y<sub>n</sub>
 - Unsupervised : no y<sub>n</sub>
    - clustering :  {X<sub>n</sub>} => cluser(X)
    - density estimation : {X<sub>n</sub>} => density(X)
        - ≈ 'unsupervised bounded regression' 
        - i.e. traffic reports with location => dangerous areas
    - outlier detection {X<sub>n</sub>} => unusual(X) 
        - ≈ 'unsupervised binary regression' 
        - i.e. Internet logs => intrusion alert
    - ... and a lot more !
 - Semi-supervised : some y<sub>n</sub>
    - leverage unlabeled data to avoid 'expensive' labeling
    - eg.
        - face images with a few labeled => face identifier (Facebook)
        - medicine data with a few labeled => medicine effect predictor
 - Reinforcement Learning : implicit y<sub>n</sub>


<h2 id="6def4688e7d3b9cfc2f058ed2729c813"></h2>

## Learning with Different Protocol

 - Batch Learning
 - Online: hypothesis improves through receiving data instances sequeentially
    - PLA can be easily adapted to online protocol 
    - reinforment learning is often done online
 - Active Learning:  Learning by 'Asking'   
    - active: improve hypothesiis with fewer lables (hopefully) by asking questions **strategically**
    - 跟上面两个被动学习不同, label成本很高的情况 适合尝试

<h2 id="6ebd75d7ad445321e62d64acb494084a"></h2>

## Learning with Different Input Space

 - concrete features
    - 比如硬币分类，选择 大小，重量等等 作为feature
    - 通常带有人类的智慧对这个问题的描述
 - Raw Features: digit recognition problem
    - often need human or machines to convert to concrete ones
 - Abstract Features : Rating Prediction problem
    - given previous (userid, itemid, rating) tuples , predict the rating that some userid would give to itemid ?
    - 'no physical meaning' ; thus even more difficult for ML

<h2 id="cfd8a0e711b39b612b7fd7279a78d83e"></h2>

# Week 4 Feasibility of Learning

<h2 id="e2757331874147511e796bb57cd0130f"></h2>

## Probability to the Rescue

 - consider a bin of many many *orange* and *green* marbles
 - we don't know the *orange* portion (probability) 
 - can you **infer** the *orange* probability ?

 - Solution 1:  random sampling  ?

---

 - bin: assume
    - orange probability = μ
    - green probability = 1-μ
    - with μ **unknonw** 
 - sample 
    - N marbles sampled independently , with 
        - *orange* fraction = ν 
        - *green* fraction = 1-ν
    - now ν **known**
 - does **in-sample ν**  say anything about out-of-sample μ ?
    - **NO!**   possibly not: sample can be mostly *green* while bin is mostly *orange*
    - **YES!**  probably yes: in-sample ν likely close to unknown μ.
    - 没有办法有个确定的答案。
        - 没有办法说，我抽10颗起来，这10颗的比例就一定是罐子里面的比例。不过呢，大致上有很大的几率是这个样子。

<h2 id="2738a5bd77944b4f0a65a05dcf269384"></h2>

### Hoeffding's Inequality

 - sample of size N 
 - μ = *orange* probability in bin
 - ν = *orange* fraction in sample
 - in big sample (N large) , ν is probably close to μ ( within ε ) 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_MLbasis_hoeffding_ineq.png)
    - 当N很大是，μ和ν 相差很大的几率 很小
 - called **Hoeffding Inequality** , for marbles, coin, polling
 - The statement 'μ-ν' is **probably approximately correct** (PAC)

---

 - valid for all N and ε
    - 不管你选择的N 和 ε 是多少，这个式子都是对的
 - does not depend on μ , **no need to 'know' μ**
    - 等式右边不需要μ
 - large sample size N for looser gap ε => higher probability for `μ≈ν`
 - if large N , can probably infer unknown μ  by known ν.

---

 - Q: Let μ = 0.4. Use Hoeffding's Inequality to bound the probability that a sample of 10 marbles will have ν ≤ 0.1. What bound do you get?
    - (1) 0.67 , (2) 0.40 , (3) 0.33 , (4) 0.05
 - A: set N=10, and ε = 0.3, you will get the anwser (3)
    - `2* (math.e **(  -2*e*e*N  ) ) = 0.3305977764431732`
    - BTW, (4) is the actual probability and Hoeffding gives only an upper bound to that.

<h2 id="4d3ee8b9af56c703975b205e29f34cfa"></h2>

## Connection to Learning

bin | learning
--- | ---
unknown *orange* prob. μ | fixed hypothesis h(x) ?  target f(x)
marble ∈ bin | X ∈ 𝕏
orange marble | h is wrong <=> h(x) ≠ f(x)
green marble | h is right <=> h(x) = f(x)
size-N sample from bin | check h on ⅅ = { (X<sub>n</sub>, y<sub>n</sub>) } , if no noise , y<sub>n</sub>=f(X<sub>n</sub>)

 - if **large N** & **i.i.d X<sub>n</sub>** infer unknown [ h(x) ≠ f(x) ]  probability by known [ h(x<sub>n</sub>) ≠ y<sub>n</sub>  ]
 - for any fixed *h* ,  can probably infer
    - **unknown E<sub>out</sub>(h)** = ε<sub>X~P</sub> [ h(x) ≠ f(x) ]  , (μ)
    - by **known E<sub>in</sub>(h)** = 1/N·∑ᴺ<sub>n=1</sub> [ h(x<sub>n</sub>) ≠ y<sub>n</sub>  ] , (ν)

<h2 id="bc490f18155779c237c38b6532ca7b7f"></h2>

### The Formal Guarantee

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_MLb_fg.png)

same as the 'bin' analogy...

 - valid for all N and ε
 - does not depend on E<sub>out</sub>(h) , **no need to know E<sub>out</sub>(h)**
    - f and P can stay unknown
 - 'E<sub>in</sub>(h) = E<sub>out</sub>(h)' is **probably approximately correct (PAC)**.
 - if **E<sub>in</sub>(h) ≈ E<sub>out</sub>(h)** and **E<sub>in</sub>(h) small** 
    - => E<sub>out</sub>(h) small.
    - => h ≈ f with respect to P 

<h2 id="911f375f353e71713d92e0e8d439e40e"></h2>

### Verification of One h

 - for any fixed *h*, when data large enough,  E<sub>in</sub>(h)  ≈ E<sub>out</sub>(h) 
    - can we claim 'good learning' ( g ≈ f  ) ?
 - Yes: if E<sub>in</sub>(h)  small for the fixed h , and **A pick the h as g** => 'g = f' PAC
 - No: if **A forced to pick THE h as g** which has not small E<sub>in</sub>(h)

<h2 id="d9ee0f5ea86476845fea40190ab1462e"></h2>

## Connection to Real Learning

<h2 id="9ba5efcb15754a3919e1c165c9746157"></h2>

### Coin Game

 - if everyone in size-150 , flip a  coin 5 times , one will get 5 heads with large probability
    - 1 - (31/32)¹⁵⁰ > 99%
 - BAD sample:  E<sub>in</sub> and E<sub>out</sub> **far away**

<h2 id="0f6ca2986821d310f080364af49eed46"></h2>

### BAD Sample and BAD Data

 - BAD Sample
    - e.g. E<sub>out</sub> = 1/2, but getting all heads ( E<sub>in</sub> = 0 )
 - BAD Data for One h
    - E<sub>in</sub> and E<sub>out</sub> **far away** 
    - e.g. E<sub>out</sub> big (far from f) , but E<sub>in</sub>  small ( correct on most examples )
 - Hoeffding 保证的是，BAD Data for h 的总体概率比较小

<h2 id="16553486c255ce8a5d8e557b67c3c9a6"></h2>

### BAD Data for Many h

 - BAD data for many h
    - <=> **no 'freedom of choice'** by A
    - <=> there exists some h such that E<sub>in</sub> and E<sub>out</sub> **far away** 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_MLb_bad_data.png)

 - for M hypotheses , bound of ℙ<sub>D</sub>[BAD D] ?

<h2 id="c82862b9ceccd7efd1ca9d2bab635903"></h2>

### Bound of BAD Data

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_MLb_bound_of_baddata.png)

 - 比原来的 Hoeffding 大了100倍

 - finite-bin version of Hoeffding , valid for all **M**, N , and ε
 - does not depend on E<sub>out</sub>(h<sub>m</sub>) , **no need to know E<sub>out</sub>(h<sub>m</sub>)**
    - f and P can stay unknown
 - 'E<sub>in</sub>(g) = E<sub>out</sub>(g)' is PAC , regardless of A 
    - 如果资料量D 够多，可以说 每一个h都是安全的： 也就是说
        - 如果 hypothesis set只有有限多種選擇 我的資料量夠多，那麼不管我的演算法A怎麼选 Ein跟Eout都會接近
 - most reasonable A (like PLA/pocket) : pick the h<sub>m</sub> with **lowest E<sub>in</sub>(h<sub>m</sub>)** as g

<h2 id="d8634320f9db8392b907e680f3fbdeef"></h2>

### The 'Statistical Learning Flow'

 - if |H| = M finite , N large enough
    - for whatever *g* picked by A , E<sub>out</sub>(g) ≈ E<sub>in</sub>(g)
 - if A finds one *g* with E<sub>in</sub>(g) ≈ 0,
    - PAC guarantee for  E<sub>out</sub>(g) ≈ 0
 - M = ∞ ? (like perceptrons) 
    - see next lecture











  















        














