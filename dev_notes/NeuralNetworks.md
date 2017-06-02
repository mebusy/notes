...menustart

 - [Neural Networks](#6b347be0e79381eeb5689396d9e59438)
 - [Lecture 1](#b685b2632f64514a84fc8cbb0b4b7d2c)
	 - [Some simple models of neurons](#b02cb3fa93ab8f0e6485b0d13bc303cc)
		 - [Linear neurons](#1ed293fed5b9ae1cf9d961b5ce17cff8)
		 - [Binary threshold neurons](#60d743bd92d01784da86912ef3e9d3fa)
		 - [Rectified Linear Neurons](#bea9f293a1d10dc9a09ab31410552fc2)
		 - [Sigmoid neurons](#5dfb3a910337bd052071a460b50f17d7)
		 - [Stochastic binary neurons](#9fa3726b2244619bd1b4f0a6f3c0ad10)
 - [Lecture 2](#2cd2c77c9f81b7be54284357f2c55290)
	 - [Types of neural network architectures](#b553e95fb37e615918e131140aec36b1)
		 - [Feed-forward neural networks](#27403055d079f8f5057e91999fe9ff29)
		 - [Recurrent Networks](#3aa835dbc7f8ec8429d7671acae6aab5)
			 - [Recurrent neural networks for modeling sequences](#ab481de40578ba1e54e09346c919fe23)
			 - [An example of what recurrent neural nets can now do (to whet your interest!)](#ac843506e5b9c5acc3c517304fae2ab6)
		 - [Symmetrically connected networks](#bd53760cfb4568281010b21ad9f4c944)
	 - [A geometrical view of perceptrons](#b2f07d14cff56667ff8ce65beaa92ace)
		 - [Weight-space](#18fbaaed2b269781105b0c38d7d03d1f)
		 - [The cone of feasible solutions](#d70801a1a8a06ad3250060f4a42e0b7d)
	 - [What perceptrons can’t do](#f6493b60fa9aa860686d995485132458)
		 - [The limitations of Perceptrons](#8bac84924ecd4f05b2ef5fb5415cda08)
		 - [What binary threshold neurons cannot do](#14461318bc8dca1452e9768872689b06)
		 - [Learning with hidden units](#b984ea836f81bad4a3764c2908f793ec)
 - [Lecture 3](#28b761e5205ba2e17062ee27b6958d08)

...menuend


<h2 id="6b347be0e79381eeb5689396d9e59438"></h2>

# Neural Networks

<h2 id="b685b2632f64514a84fc8cbb0b4b7d2c"></h2>

# Lecture 1 

<h2 id="b02cb3fa93ab8f0e6485b0d13bc303cc"></h2>

## Some simple models of neurons 

<h2 id="1ed293fed5b9ae1cf9d961b5ce17cff8"></h2>

### Linear neurons

y = b + ∑ᵢ xᵢwᵢ

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_linear_neurons.png)

<h2 id="60d743bd92d01784da86912ef3e9d3fa"></h2>

### Binary threshold neurons 

 - First compute a weighted sum of the inputs
 - Then send out a fixed size spike of activity if the weighted sum exceeds a threshold. 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_bin_threshold_neurons.png)


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_bin_threshold_neurons2.png)

<h2 id="bea9f293a1d10dc9a09ab31410552fc2"></h2>

### Rectified Linear Neurons

 - sometimes called linear threshold neurons
 - compute a **linear** weighted sum of their inputs.
 - The output **is a non-linear** function of the total input. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_rectified_neurons.png)

<h2 id="5dfb3a910337bd052071a460b50f17d7"></h2>

### Sigmoid neurons 

 - give a real-valued output that is a smooth and bounded function of their total input. 
    - Typically they use the logistic function 
    - They have nice derivatives which make learning easy (see lecture 3). 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_sigmoid_neurons.png)

<h2 id="9fa3726b2244619bd1b4f0a6f3c0ad10"></h2>

### Stochastic binary neurons 

 - These use the same equations as logistic units. 
    - But they treat the output of the logistic as the **probability** of producing a spike in a short time window.  
    

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_stochastic_bin_neurons.png)


---

<h2 id="2cd2c77c9f81b7be54284357f2c55290"></h2>

# Lecture 2

<h2 id="b553e95fb37e615918e131140aec36b1"></h2>

## Types of neural network architectures

<h2 id="27403055d079f8f5057e91999fe9ff29"></h2>

### Feed-forward neural networks

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_feedforward_nnet.png)

 - These are the commonest type of neural network in practical applications. 
    - The first layer is the input and the last layer is the output. 
    - If there is more than one hidden layer, we call them “deep” neural networks. 
 - They compute a series of transformations that change the similarities between cases
    - so at each layer, you get a new representation of the input , in which 
        - things that were similar in the previous layer may have become less similar
        - or things that were dissimilar in the previous layer may have become more similar
    - So in speech recognition, for example, we'd like the same thing said by different speaker to become more similar , and different things said by the same speaker to be less similar as we go up through the layers of the network
    - In order to achieve this, The activities of the neurons in each layer are a **non-linear** function of the activities in the layer below

<h2 id="3aa835dbc7f8ec8429d7671acae6aab5"></h2>

### Recurrent Networks 

 - These have directed cycles in their connection graph.
    - That means you can sometimes get back to where you started by following the arrows. 
 - They can have complicated dynamics and this can make them very difficult to train. 
    - There is a lot of interest at present in finding efficient ways of training recurrent nets. 
 - They are more biologically realistic. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_recurrent_nnet.png)


 - Recurrent nets with multiple hidden layers are just a special case that has some of the hidden -> hidden connections missing. 

<h2 id="ab481de40578ba1e54e09346c919fe23"></h2>

#### Recurrent neural networks for modeling sequences

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_recurrent_nnet2.png)

 - Recurrent neural networks are a very natural way to model sequential data: 
    - They are equivalent to very deep nets(feed-forward)  with one hidden layer per time slice.
        - so at each time step , the states of the hidden units determines the states of the hidden units the next time step
    - Except that they use the same weights at every time slice and they get input at every time slice. 
        - this is one way they differ from feed-forward NNet. 
        - the weight matrix depicted by each red arrow is same at each time step
 - They have the ability to remember information in their hidden state for a long time. 
    - But its very hard to train them to use this potential.

<h2 id="ac843506e5b9c5acc3c517304fae2ab6"></h2>

#### An example of what recurrent neural nets can now do (to whet your interest!) 

 - Ilya Sutskever (2011) trained a special type of recurrent neural net to predict the next character in a sequence. 
 - After training for a long time on a string of half a billion characters from English Wikipedia, he got it to generate new text. 
    - It generates by predicting the probability distribution for the next character and then sampling a character from this distribution. 

<h2 id="bd53760cfb4568281010b21ad9f4c944"></h2>

### Symmetrically connected networks

 - These are like recurrent networks, but the connections between units are symmetrical (they have the same weight in both directions)
    - John Hopfield (and others) realized that symmetric networks are much easier to analyze than recurrent networks. 
    - They are also more restricted in what they can do. because they obey an energy function. 
        - **For example, they cannot model cycles**.
 - Symmetrically connected nets without hidden units are called “Hopfield nets”

---

<h2 id="b2f07d14cff56667ff8ce65beaa92ace"></h2>

## A geometrical view of perceptrons

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_perceptron_architecture.png)

<h2 id="18fbaaed2b269781105b0c38d7d03d1f"></h2>

### Weight-space

 - This space has one dimension per weight. 
 - A point in the space represents a particular setting of all the weights. 
    - 坐标系各个轴代表 wᵢ
 - Assuming that we have eliminated the threshold, each training case can be represented as a hyperplane through the origin. 
    - The weights must lie on one side of this hyper-plane to get the answer correct. 

--- 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space.png)

 - Each training case defines a plane (shown as a black line) 
    - The plane goes through the origin and is perpendicular to the **input vector**. 
        - input vector 就是 sample，training case 超平面 由它定义
        - input also represents constraints 
            - so we can think of the inputs as partitioning the space into 2 halves
            - weights lying in one half will get the answer corrent
            - the inputs will constrain the set of weights that give the correct classification result.
    - On one side of the plane the output is **wrong** because the scalar product of the weight vector with the input vector has the wrong sign. 
        - 同侧点积为正，异侧点积为负

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space2.png)


<h2 id="d70801a1a8a06ad3250060f4a42e0b7d"></h2>

### The cone of feasible solutions

 - To get all training cases right we need to find a point on the right side of all the planes. 
    - There may not be any such point! 
 - If there are any weight vectors that get the right answer for all cases, they lie in a hyper-cone with its apex at the origin. 
    - So the average of two good weight vectors is a good weight vector. 
        - **The problem is convex** 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space_con.png)

 - consider two inputs that both have a label of 1. we use a yellow arrow to represent a weight vectors which correctly classify the 2 inputs.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space_con2.png)

<h2 id="f6493b60fa9aa860686d995485132458"></h2>

## What perceptrons can’t do 

<h2 id="8bac84924ecd4f05b2ef5fb5415cda08"></h2>

### The limitations of Perceptrons

 - If you are allowed to choose the features by hand and if you use enough features, you can do almost anything
    - For binary input vectors, we can have a separate feature unit for each of the exponentially many binary vectors and so we can make any possible discrimination on binary input vectors. (feature mapping ?)
        - This type of table look-up won’t generalize. 
 - But once the hand-coded features have been determined, there are very strong limitations on what a perceptron can learn.  

<h2 id="14461318bc8dca1452e9768872689b06"></h2>

### What binary threshold neurons cannot do 

 - A binary threshold output unit cannot even tell if two single bit features are the same! 
    - Positive cases (same): (1,1) -> 1; (0,0) -> 1 
    - Negative cases (different): (1,0) -> 0; (0,1) -> 0 
 - The four input-output pairs give four inequalities that are impossible to satisfy: 
    - w₁+w₂ >= θ , 0 >= θ
    - w₁<θ , w₂<θ 

<h2 id="b984ea836f81bad4a3764c2908f793ec"></h2>

### Learning with hidden units 

 - Networks without hidden units are very limited in the input-output mappings they can learn to model. 
    - More layers of linear units do not help. Its still linear. 
    - Fixed output non-linearities are not enough. 
 - We need multiple layers of **adaptive**,  non-linear hidden units. But how can we train such nets? 
    - We need an efficient way of adapting **all** the weights, not just the last layer.  This is hard.
    - Learning the weights going into hidden units is equivalent to learning features
    - This is difficult because nobody is telling us directly what the hidden units should do. 

---

<h2 id="28b761e5205ba2e17062ee27b6958d08"></h2>

# Lecture 3 

## Learning the weights of a linear neuron 

### Why the perceptron learning procedure cannot be generalised to hidden layers 
    
 - The perceptron convergence procedure works by ensuring that every time the weights change, they get closer to every “generously feasible” set of weights
    - This type of guarantee cannot be extended to more complex networks in which the average of two good solutions may be a bad solution
 - So “multi-layer” neural networks do not use the perceptron learning procedure
    - They should never have been called multi-layer perceptrons. 

### A different way to show that a learning procedure makes progress 

 - Instead of showing the weights get closer to a good set of weights, show that the actual output values get closer the target values. 
    - This can be true even for non-convex problems in which there are many quite different sets of weights that work well and averaging two good sets of weights may give a bad set of weights. 
    - It is not true for perceptron learning. 
 - The simplest example is a linear neuron with a squared error measure. 

### Linear neurons (also called linear filters) 

y = ∑<sub>ᵢ</sub> wᵢxᵢ = wᵀx 


 - The neuron has a realvalued output which is a weighted sum of its inputs 
 - The aim of learning is to minimize the error summed over all training cases. 
    - The error is the squared difference between the desired output and the actual output. 

### Why don’t we solve it analytically? 

 - 为什么不用矩阵直接求近似解？
 - Scientific answer: We want a method that real neurons could use. 
 - Engineering answer: We want a method that can be generalized to multi-layer, non-linear neural networks
    - The analytic solution relies on it being linear and having a squared error measure. 
    - Iterative methods are usually less efficient but they are much easier to generalize. 

### A toy example to illustrate the iterative method 

每天你在自助餐厅吃午饭。你的饮食包括鱼fish，薯条chips 和番茄酱ketchup 。每样你都会视心情拿几个。收银员只会告诉你膳食的总价格.几天后，您应该可以弄清每种食物的价格。

 - The iterative approach: 
    - Start with random guesses for the prices and
    - then adjust them to get a better fit to the observed prices of whole meals. 

### Solving the equations iteratively

 - price = x<sub>fish<sub>w<sub>fish<sub> + x<sub>chips<sub>w<sub>chips<sub> + x<sub>ketchup<sub>w<sub>ketchup<sub>
 - We will start with guesses for the weights w=( w<sub>fish<sub>, w<sub>chips<sub>, w<sub>ketchup<sub> )
    - and then adjust the guesses slightly
    - to give a better fit to the prices given by the cashier. 




minus sign in front of ε cuz we want the error to go down.

 


