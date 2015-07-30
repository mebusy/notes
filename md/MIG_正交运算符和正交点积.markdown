## 正交运算符和正交点积
正交点积是一种向量运算，它具有出乎意料的作用。

### 1. 垂直运算符  perp  ⟂
如果已有向量v， 则 $v^⟂$ 就是与v垂直的向量。  
2维空间中，存在两个和v垂直的向量：   一个位于顺时针$90^。$,一个位于逆时针$90^。$。  
因为习惯右手法则，一般选择逆时针$90^。$的垂直向量。  
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/MIG_perpVector.png)

图中， $v=\begin{bmatrix}
        1\\
        0.2\\
        \end{bmatrix}$    
        
则，$v^⟂=\begin{bmatrix}
        -0.2\\
        1\\
        \end{bmatrix}$    
直观的做法就是，交换向量的两个分量，然后对第一个分量取反。  
3维空间中，存在无数个和给定向量垂直的向量，这限制了垂直运算在3维空间中的应用。因此我们将集中讨论2维空间的情形。   

### 2. 性质
假设 $v^⟂$ 是 v 逆时针旋转$90^。$所得的变量。  
>  1. $v^⟂$ ⟂ v
>  2. 线性
>     a. $(u+v)^⟂ = u^⟂ + v^⟂ $
>     b. $(kv)^⟂ = k(v^⟂) $
>  3. $\|v^⟂\| = \|v\| $
>  4. $v^{⟂⟂} = -v $

### 3. 垂直点运算
如图
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/MIG_perpDot.png)
看一下, $u^⟂ 和 v$ 之间关系, 根据向量点积定义:  
$$cos\phi = \frac{u^⟂\cdot v}{\|u^⟂\| \|v\|}$$
已经证明，$\|u^⟂\| = \|u\| $
所以， $$cos\phi = \frac{u^⟂\cdot v}{\|u\| \|v\|}$$

因为垂直，所以 $\theta + \phi = \pi/2$,  则 $cos\phi = sin\theta$ 。
所以$$u^⟂\cdot v = \|u\| \|v\|sin\theta $$

看到这里，就很明白了， 垂直点积其实就是3维叉积的2维模拟。

也就是说，2维空间的点积， 不仅可以表示夹角的大小，还可以表示夹角的方向。  

| 角度      |   0 | 90 |180 |270 | 360  
| -------- |
| sin       |   0 | 1 |0 | -1 | 0 

对于 u x v
\begin{cases}
>0,  & \text{u到v的夹角为逆时针} \\
=0 , & \text{夹角为0或180, 顺逆随意} \\
<0, & \text{u到v的夹角为顺时针} \\
\end{cases}


