


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

## 结构

 - input date , layer 0
 - hidden layer , 1 ≤ l ≤ L 
 - output layer , h(x)
 - apply *x* as ***input layer*** x⁽⁰⁾ , go through ***hidden layers*** to get x⁽ˡ⁾ , predict at output layer x₁⁽ᴸ⁾.
    - output x₁⁽ᴸ⁾ 的下表 1， 表示是第一个输出
 - each layer: transformation to be ***learned*** from data.
    - w向量和x向量 越平行，点积越大
    - whether *x* 'matches' weight vectors in pattern
 - NNet 是这样的一个模型，每一次都在做所谓的  ***pattern extraction***
    - pattern extraction with layers of ***connection weights***

---

# Deep Learning

## Challenges and Key Techniques for Deep Learning

 - difficult ***structural decisions***:
    - 怎么选择一个好的模型
    - subjective with ***domain knowledge***: like ***convolutional NNet*** for images
 - high model complexity:
    - no big worries if big enough data
    - regularization towards noise-tolerant: like
        - dropout ( tolerant when network corrupted ) 丢弃坏掉的神经元
        - denoising ( tolerant when input corrupted ) 丢弃坏掉的输入
 - hard optimization problem:
    - careful initialization to avoid bad local minimum: called **pre-training**. 而不是采用 random initialization.
 - huge computational complexity ( worsen with big data )
    - novel hardware / architecture: like mini-batch with GPU

---

 - Simple Deep Learning
    - for l=1,...,L , pre-train { w⁽ˡ⁾ } assuming w⁽¹⁾, ... ,w⁽ˡ⁻¹⁾ fixed
        - 一层一层 一次决定  初始 权重值
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TU_ml_dl_weight_init.png)
 
# Autodecoder

Autodecoder 是 实现好的 pre-training 的一个方式。

 - basic autoencoder :
    - d-d'-d NNet with error function: 平方差








 


---



