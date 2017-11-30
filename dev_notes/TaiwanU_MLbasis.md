
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












