

# Neural Network : Notivation

## Linear Aggregation of Perceptrons : Pictorial View 

 - Perceptrons 模型
    - 把你的输入 x 乘上 1堆权重，算出一个分数 
 - 一堆 perceptron 放在一起
    - x·W₁ -> g₁ , x·W₂ -> g₂ , ...
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_perceptron_model.png)

 - What boundary can G implement ?
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_mulitple_layer_perceptron.png)
 - Limitation: XOR not "linear separable"  
    - XOR 不是 线性可分
 - How to implement XOR(g₁,g₂) ?

## Multi-layer Perceptrons : Basic Neural Network

 - one more layer of AND transform ?
 - XOR(g₁,g₂) = OR( AND( -g₁,g₂ ) , AND(g₁,-g₂) )
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_aggressive_perceptron_model.png)

---


# Neural Network Hypothesis: Output

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_nn_output.png)

 - OUTPUT: simply a ***linear model*** with s = wᵀ· ϕ⁽²⁾(ϕ⁽¹⁾(x)) 

## Transformation function

 - s function
 - 中间层的转换函数 可以全部使用 linear transform 吗？
    - linear : whole network linear , thus less useful
        - 如果全部都是 linear transform function ， 那个整个网络也是一个 linear transform 转换，就蜕变成 单个perceptron 模型了. So :
 - 神经网络中，一般使用如下 转换函数， 和 逻辑回归总的 s 函数很有渊源
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_h_function_inNN.png)

---



