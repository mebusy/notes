
    反向传播
        代价函数 和 反向传播 Backpropagation
        为了计算导数项，我们采用反向传播算法Backpropagation
        只有一个训练样本的例子（不重要）:
        大量训练样本情况下，反向传播算法的应用:
    反向传播练习
        unrolling parameters
        Gradient checking
        应用 Gradient Checking的步骤
    随机初始化
    put all together
        选择神经网络架构
        训练神经网络
        

# 反向传播

#### 代价函数 和 反向传播 Backpropagation

一些标记:

 - L 标记 神经网络的总层数
 - S₄ 表示第4层的单元数，不包括偏差单元 `bias unit`
 - k 表示第几个输出单元

---


    logistic regression cost function:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/logistical_regression_cost.png)

    neural network cost function:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural_costFunc.png)

 - 使用前中传播计算出 h(x), 如果有多个输出单元，h(x)是一个向量: `h(x) ∊ ℝᴷ`, `(h(x))ᵢ = iᵗʰ output`
   ```
    % step 1
    a_1 = [ ones( m , 1)  X ];
    a_2 = sigmoid( a_1 * Theta1' );  % 2nd level
    
    a_2= [ ones( size(a_2,1),1 )  a_2 ];
    a_3 = sigmoid( a_2 * Theta2' );  % output level,hx
    
    hx=a_3;   
   ```
 - 左侧部分是对K个输出单元的代价函数的求和, 使用和 one-vs-all的一样的方法处理y
   ```
   % step 2
    J=0;
    for k = 1:num_labels
    	J +=  1/m * sum(  - (y==k) .* log( hx(:,k) )  - ( 1-(y==k) ) .* log( 1- hx(:,k) ) ) ;
    end
   ```

 - 右侧的正则化项，需要累加除输出层外的 所有层的 Θ, 
   
   eg: 三层神经网络，需要处理`Θ⁽¹⁾ , Θ⁽²⁾ ` , 且一般不处理 bias unit的权

   ```
   % step 3
   all_params = [Theta1(:,2:end)(:) ; Theta2(:,2:end)(:)];
   J +=  lambda/(2*m )* ( all_params' * all_params )  ; 
   ```
   
   
---


为了 min J(Θ)我们需要计算:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/9710b147c0a369ed8ee0fe284a8ed5373505dac6.png)

记住:

这项是一个实数 ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/71b7943041878e87ec9ad13ff72c8ef7cf7a54bd.png)


---

#### 为了计算导数项，我们采用反向传播算法`Backpropagation`

我们使用 ![][1] 来表示 l 层第 j 个节点的误差值。

这样对每一个节点，我们就有了 节点的激励值 ![][2] 和 误差![][1]:

![][1] = ![][2] - `yⱼ`  ,  其中 ![][2]= `h(x)ⱼ`

---

#### 只有一个训练样本的例子（不重要）:

以一个4层神经网络为例子:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_4Layer.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_step_2_delta.png)

 - 没有 `δ⁽¹⁾`, 因为第1层 是training set中的feature
 - 反向传播的名字，来源于 从输出层开始计算，依次反向推算
 - 最后一个公式，提供了计算 激励值a 导数的方法
   
   `g'(z) = d/dz(g(z)) = g(z)(1-g(z))`
   


δ的计算非常复杂 ，最终我们可以得到下面的公式: (ignoreλ  ,or if λ=0 )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_dirivative_J_Theta_ijl_no_lamda.png)


#### 大量训练样本情况下，反向传播算法的应用:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Backpropagation.png)

最后一步可以向量化:

![][3]

最后我们跳出循环,计算:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackPropagation_D.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackPropagation_Derivative.png)

D 就是 J(Θ)的偏导数, Δ的均值

    eg: 一个3层神经网络，反向传播计算流程， 注意第3步，需要使用 delta2=delta2(2:end) 去掉 bias unit 的误差

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/steps_4_3layers_network_computer_derivative.png)

---

再回顾一下 反向传播的计算步骤:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackwardPropagation_desc.png)

 1. 熟悉微积分的，可以发现，δ 其实就是对 J(Θ)求 z的偏微分
 2. 对于 bias unit的δ， 可以计算，也可以不算，依赖于你想实现的算法

# 反向传播练习

#### unrolling parameters

以前的 高级优化算法，我们使用θ向量 计算cost,gradient, 和应用于fminunc,
在神经网络中 Θ 是一个矩阵，

假设有3个 10x11 Theta 矩阵，把这3个矩阵转成一个列向量:

```
thetaVec=[ Theta1(:) ; Theta2(:) ; Theta3(:)  ]
```

从 thetaVec 中取回 Theta2

```
Theta2 = reshape( thetaVec(111:220), 10,11  )
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackwardPropagation_practics.png)

#### Gradient checking

反向传播的算法非常负责，很容易出错。为了确保反向传播的偏导数项计算正确性, 我们使用 `Gradient checking` 来帮助检查实现的算法的正确性。

`numerical gradient algorithm` : 使用 `ΔJ(θ)/Δ(θ)` 来近似计算J(θ)的导数。 

`注意:` `numerical gradient algorithm` 非常慢，只能用于检测。

---

`θ ∊ ℝ`  θ是实数的情况

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/gradientAprox.png)

ε一般取`10⁻⁴`

---

`θ ∊ ℝⁿ`  θ是向量的情况 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/GradientCheckVectorTheta.png)

`Octave 中具体的实现`

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/GradientCheck_Octave.png)

`检查 gradApprox ≈ Dvec`

Dvec 是通过反向传播算法计算出来的 J(Θ)对Θ的偏导数

---

#### 应用 Gradient Checking的步骤

 1. 应用 backprop 计算出 Dvec ( unrolled `D⁽ⁱ⁾`)
 2. 应用 Gradient Checking 计算出 gradApprox
 3. 确认 近似
 4. 去掉 gradient checking , 使用 backprop 代码进行学习


# 随机初始化

对于逻辑回归来说，初始化θ 为一个零向量是可行的， 但是对于神经网络，并不适用。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/randomInitialize.png)

如图所示, 如果所有的Θ都初始化为零向量, 那么所有隐藏层的激励值和误差，都会得到相同的结果，这就组织了神经网络学习出更多有价值的信息。

我们使用 `Random Initialization` 来打破上面的 `权重对称` Symmetry breaking 情况：

初始化Θ为 [-ε,ε] 之间的一个随机值, ε 是接近0的很小的值

`eg.`

```
Theta1 = rand(10,11)*(2*INIT_EPSILON)-INIT_EPSILON
```

# put all together

#### 选择神经网络架构

输入层: 一旦确定了特征集X， 输入单元的`数量`也就确定了
输出层: 输出单元`数量`,由分类器的类别个数决定
隐藏层: 如果>1 隐藏层，每层的单元数最好保持一致，个数稍多余输入单元数

#### 训练神经网络

 - 随机初始化权值
 - 对每一个`x⁽ⁱ⁾` 使用前向传播算法计算 `h(x⁽ⁱ⁾)` (输出结果)
 - 计算代价函数 J(Θ)
 - 使用反向传播算法计算 J(Θ) 对Θ的偏导数


`伪代码:`

```
% 第一次实现反向传播算法，建议使用 for循环逐个计算
for i=1:m {
    对每一个训练样本,使用 prop,backprop 计算 `a⁽ˡ⁾`,`δ⁽ˡ⁾` , l=2,...,L).
    累加计算 `Δ⁽ˡ⁾` (公式如下)
}
```
使用 Δ⁽ˡ⁾ 计算![][4] . (这时要考虑加入正则项)
(TODO: 老师这里为什么使用 jkl ?)

![][3]

 - 使用Gradient checking 检验 前面得到的 J(Θ)偏导数的值, 检验通过后,去掉gradient checking
 - 使用 梯度下降或高级优化算法，计算 Θ

`注意：这里J(Θ)是非凸函数non-convex`




---

  [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/delta_j_l.png
  [2]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/activate_j_l.png
  [3]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/delta_vectorize.png
  [4]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/derivative_Theta_jkl.png
