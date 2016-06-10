...menustart

 - [反向传播](#4ae61d8a3733358bcef0f73d62e69a15)
   - [代价函数 和 反向传播 Backpropagation](#b68af9a6b20fafa771e0f2abd6ebe283)
   - [为了计算导数项，我们采用反向传播算法`Backpropagation`](#86e1d05271f80ac28ff23624d6d7c00c)
   - [只有一个训练样本的例子（不重要）:](#4713b5e8c545b8a393cba2db968389fa)
   - [大量训练样本情况下，反向传播算法的应用:](#770ae2adf9aaa0cbd1da51d0d0c539ff)
 - [反向传播练习](#a44baf9d73c4a124326ffc5568a06903)
   - [unrolling parameters](#02baf1f861df96f5e3a87d3eef8116e4)
   - [Gradient checking](#2f05f3a13934eed796477b096390d62f)
   - [应用 Gradient Checking的步骤](#99527f4c4644eda2340faca80fba7724)
 - [随机初始化](#aec2a101c13136f3cdbe1dca6e8494da)
 - [put all together](#d1ce73089ce012666ab305131351d508)
   - [选择神经网络架构](#801876e7e97044976d75b835fac97ca3)
   - [训练神经网络](#67fd927dbbde24e0a4e33a49821346bd)

...menuend



        

<h2 id="4ae61d8a3733358bcef0f73d62e69a15"></h2>
# 反向传播

"误差反向传播" 的简称，是一种与最优化方法（如梯度下降法）结合使用的，用来训练人工神经网络的常见方法。

该方法计算对网络中所有权重计算损失函数的梯度。这个梯度会反馈给最优化方法，用来更新权值以最小化损失函数。

<h2 id="b68af9a6b20fafa771e0f2abd6ebe283"></h2>
#### 代价函数 和 反向传播 Backpropagation

一些标记:

 - L 标记 神经网络的总层数
 - S₄ 表示第4层的单元数，不包括偏差单元 `bias unit`
 - k 表示第几个输出单元

---


logistic regression cost function:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/logistical_regression_cost.png)

由于神经网络的输出层通常有多个输出，属于k维向量，因此用如下的方式定义神经网络的Cost function:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural_costFunc.png)

注意，对于训练集的每一个样本，都需要对输出层所有的输出单元计算cost并求和。

 - 使用前向传播计算出 h(x), 如果有多个输出单元，h(x)是一个向量: `h(x) ∊ ℝᴷ`, `(h(x))ᵢ = iᵗʰ output`
   ```
    % step 1
    a_1 = [ ones( m , 1)  X ];
    z_2 = a_1 * Theta1' ;  % you'd better work z_2 out, for later using
    a_2 = sigmoid( z_2 ) ;
    a_2 = [ ones( size(a_2,1),1 )  a_2 ];  % 2nd level
    
    z_3 = a_2 * Theta2' ;
    a_3 = sigmoid( z_3 );  % output level,hx
    
    hx=a_3;   
   ```
 - 左侧部分是对K个输出单元的代价函数的求和并累加, 使用和 one-vs-all的一样的方法处理y:
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

<h2 id="86e1d05271f80ac28ff23624d6d7c00c"></h2>
#### 为了计算导数项，我们采用反向传播算法`Backpropagation`

我们使用 ![][1] 来表示 l 层第 j 个节点的误差值。

这样对每一个节点，我们就有了 节点的激励值 ![][2] 和 误差![][1]:

![][1] = ![][2] - `yⱼ`  ,  其中 ![][2]= `h(x)ⱼ`

---

<h2 id="4713b5e8c545b8a393cba2db968389fa"></h2>
#### 只有一个训练样本的例子（不重要）:

以一个4层神经网络为例子:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_4Layer.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_step_2_delta.png)

 - 没有 `δ⁽¹⁾`, 因为第1层 是training set中的feature
 - 反向传播的名字，来源于 从输出层开始计算，依次反向推算
 - 最后一个公式，提供了计算 激励值a 导数的方法, !!!重要!!!
   
   `g'(z) = d/dz(g(z)) = g(z)(1-g(z))`
   
---

δ的计算非常复杂 ，最终我们可以得到下面的公式: (ignoreλ  ,or if λ=0 )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Neural2_dirivative_J_Theta_ijl_no_lamda.png)


<h2 id="770ae2adf9aaa0cbd1da51d0d0c539ff"></h2>
#### 大量训练样本情况下，反向传播算法的应用:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Backpropagation.png)

最后一步可以向量化:

![][3]

最后我们跳出循环,计算:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackPropagation_D.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackPropagation_Derivative.png)

D 就是 J(Θ)的偏导数, Δ的均值

    eg: 一个3层神经网络，反向传播计算流程， 注意第一步 y_k ∊ {0,1} ,第3步，需要使用 delta2=delta2(2:end) 去掉 bias unit 的误差

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/steps_4_3layers_network_computer_derivative.png)

---

再回顾一下 反向传播的计算步骤:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BackwardPropagation_desc.png)

 1. 熟悉微积分的，可以发现，δ 其实就是对 J(Θ)求 z的偏微分
 2. 对于 bias unit的δ， 可以计算，也可以不算，依赖于你想实现的算法

<h2 id="a44baf9d73c4a124326ffc5568a06903"></h2>
# 反向传播练习

<h2 id="02baf1f861df96f5e3a87d3eef8116e4"></h2>
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

---

<h2 id="2f05f3a13934eed796477b096390d62f"></h2>
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

<h2 id="99527f4c4644eda2340faca80fba7724"></h2>
#### 应用 Gradient Checking的步骤

 1. 应用 backprop 计算出 Dvec ( unrolled `D⁽ⁱ⁾`)
 2. 应用 Gradient Checking 计算出 gradApprox
 3. 确认 近似
 4. 去掉 gradient checking , 使用 backprop 代码进行学习


<h2 id="aec2a101c13136f3cdbe1dca6e8494da"></h2>
# 随机初始化

对于逻辑回归来说，初始化θ 为一个零向量是可行的， 但是对于神经网络，并不适用。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/randomInitialize.png)

如图所示, 如果所有的Θ都初始化为零向量, 那么所有隐藏层的激励值和误差，都会得到相同的结果，这就组织了神经网络学习出更多有价值的信息。

我们使用 `Random Initialization` 来打破上面的 `权重对称` Symmetry breaking 情况：

初始化Θ为 [-ε,ε] 之间的一个随机值, ε 是接近0的很小的值

`eg.`

```
INIT_EPSILON = 0.12;
Theta1 = rand(10,11)*(2*INIT_EPSILON)-INIT_EPSILON;
```

<h2 id="d1ce73089ce012666ab305131351d508"></h2>
# put all together

<h2 id="801876e7e97044976d75b835fac97ca3"></h2>
#### 选择神经网络架构

输入层: 一旦确定了特征集X， 输入单元的`数量`也就确定了
输出层: 输出单元`数量`,由分类器的类别个数决定
隐藏层: 如果>1 隐藏层，每层的单元数最好保持一致，个数稍多余输入单元数

<h2 id="67fd927dbbde24e0a4e33a49821346bd"></h2>
#### 训练神经网络

 - 随机初始化权值
 - 对每一个`x⁽ⁱ⁾` 使用前向传播算法计算 `h(x⁽ⁱ⁾)` (输出结果)
 - 计算代价函数 J(Θ) , 这里J(Θ)是非凸函数non-convex`
 - 使用反向传播算法计算 J(Θ) 对Θ的偏导数


    计算grad 代码:

```
% step 4

delta_3 = zeros(size(a_3));
% for k output units
for k = 1:num_labels
	delta_3(:,k) = a_3(:,k) - (y==k) ;
end

delta_2 =  delta_3 * Theta2 .* sigmoidGradient( [ ones( size(z_2,1),1 )  z_2 ] ) ;
delta_2 =  delta_2(:, 2:end) ;  % 去掉 bias 单元

Theta2_grad = (delta_3' * a_2 ) / m ;
Theta1_grad = (delta_2' * a_1 ) / m ;

% add regularization
Theta1_grad(:, (2:end)) += lambda/m * Theta1(:, (2:end));
Theta2_grad(:, (2:end)) += lambda/m * Theta2(:, (2:end));

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];
```







---

  [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/delta_j_l.png
  [2]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/activate_j_l.png
  [3]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/delta_vectorize.png
  [4]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/derivative_Theta_jkl.png
