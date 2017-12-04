
# Week1  The Learning Problem

 - *Algorithm* takes *Data* and *Hypothesis set*  to get final hypothesis *g*.
    - H: set of candidate formula , with different weights W

# Week2 Learning to Answer Yes/No

## Perceptron Hypothesis Set

### Perceptron

 - x = { x₁,x₂,...,x<sub>d</sub> }
 - y = { +1 | -1  }
 - h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ - threshold  )

### Vector Form of Perceptron Hypothesis
    
 - 把 *threshold* 也当成是一个特殊的 w₀

```
h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ - threshold  )
h(x) = sign( ∑ᵈᵢ₌₁ wᵢxᵢ + (-threshold)*(+1)  )
h(x) = sign( ∑ᵈᵢ₌₀ wᵢxᵢ )
h(x) = sigh ( WᵀX )
```

### Perceptrons in ℝ²

 - h(x) = sign( w₀ +w₁x₁ +w₂x₂ )
    - h(x) = 0 is a **lines** ( ir hyperplanes in ℝᵈ )

 - perceptrons <=> **linear (binary) clasifiers**
    - PS. (2D空间下) 二元分类也并不仅限与 直线划分的情况，h(x)=0 也可以是一条曲线。只是这个perceptron 是直线情况



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

### Practical Implementation of PLA 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_CyclicPLA_pseudo.png)

### Why PLA may work 

 - sign(WᵀX) != y<sub>n</sub> ,  W<sub>t+1</sub> <-  W<sub>t</sub> + y<sub>n</sub>X<sub>n</sub>
 - y<sub>n</sub>W<sub>t+1</sub>X<sub>n</sub> >=  y<sub>n</sub>W<sub>t</sub>X<sub>n</sub>
    - 如果y<sub>n</sub> 是负的，算法的作用是 努力使WᵀX往正的方向努力，使得更接近正确的 y

## Guarantee of PLA

### Linear Separability

 - if PLA halts (i.e. no more mistakes) , ( **necessary condition** ) D allows some *W* to make no mistake 
 - call such D **linear separable**

### PLA Fact : W<sub>t</sub> Gets More Aligned with W<sub>f</sub>

 - linear separable D <=> exists perfect  W<sub>f</sub> such that y<sub>n</sub> = sign(  W<sub>f</sub>ᵀx<sub>n</sub> )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_fact1.png)

 - 由上可以，如果 W<sub>t</sub> 的长度没有变长的话，那么可以看到 PLA 使得  W<sub>t</sub> 更加接近W<sub>f</sub> 

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

## Non-Separable Data

### Pocket Algorithm

 - modify PLA (black lines) by keeping best weights in pocket

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ML_PLA_modify_pseudo.png)


# Week 3 Types of Learning

## Learning with Different Output Space

### Multiclass Classification: Coin Recognition Problem 

 - classify US coins (1c,5c,10c,25c)
    - y = {1,2,...,K}
 - written digits => 0,1,...,9
 - picture => apple, orange , strawberry

### Structured Learning : Sequence Tagging Problem

 - multiclass classification : word => word class
 - structured learning :
    - sentence => structure (class of each word)
 - y = { PVN,PVP,NVN,PV,... } , not including VVVVV
 - huge multiclass classification problem 
    - (structure ≡ hyperclass) without 'explicit' class definition

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


## Learning with Different Protocol

 - Batch Learning
 - Online: hypothesis improves through receiving data instances sequeentially
    - PLA can be easily adapted to online protocol 
    - reinforment learning is often done online
 - Active Learning:  Learning by 'Asking'   
    - active: improve hypothesiis with fewer lables (hopefully) by asking questions **strategically**
    - 跟上面两个被动学习不同, label成本很高的情况 适合尝试

## Learning with Different Input Space

 - concrete features
    - 比如硬币分类，选择 大小，重量等等 作为feature
    - 通常带有人类的智慧对这个问题的描述
 - Raw Features: digit recognition problem
    - often need human or machines to convert to concrete ones
 - Abstract Features : Rating Prediction problem
    - given previous (userid, itemid, rating) tuples , predict the rating that some userid would give to itemid ?
    - 'no physical meaning' ; thus even more difficult for ML

# Week 4 Feasibility of Learning

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

### Hoeffding's Inequality

 - sample of size N 
 - μ = *orange* probability in bin
 - ν = *orange* fraction in sample
 - in big sample (N large) , ν is probably close to μ ( within ε ) 
    - 










        














