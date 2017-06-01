
# Neural Networks

# Lecture 1 

## Some simple models of neurons 

### Linear neurons

y = b + ∑ᵢ xᵢwᵢ

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_linear_neurons.png)

### Binary threshold neurons 

 - First compute a weighted sum of the inputs
 - Then send out a fixed size spike of activity if the weighted sum exceeds a threshold. 


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_bin_threshold_neurons.png)


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_bin_threshold_neurons2.png)

### Rectified Linear Neurons

 - sometimes called linear threshold neurons
 - compute a **linear** weighted sum of their inputs.
 - The output **is a non-linear** function of the total input. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_rectified_neurons.png)

### Sigmoid neurons 

 - give a real-valued output that is a smooth and bounded function of their total input. 
    - Typically they use the logistic function 
    - They have nice derivatives which make learning easy (see lecture 3). 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_sigmoid_neurons.png)

### Stochastic binary neurons 

 - These use the same equations as logistic units. 
    - But they treat the output of the logistic as the **probability** of producing a spike in a short time window.  
    

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_stochastic_bin_neurons.png)


---

# Lecture 2

## Types of neural network architectures

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

### Recurrent Networks 

 - These have directed cycles in their connection graph.
    - That means you can sometimes get back to where you started by following the arrows. 
 - They can have complicated dynamics and this can make them very difficult to train. 
    - There is a lot of interest at present in finding efficient ways of training recurrent nets. 
 - They are more biologically realistic. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_recurrent_nnet.png)


 - Recurrent nets with multiple hidden layers are just a special case that has some of the hidden -> hidden connections missing. 

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

#### An example of what recurrent neural nets can now do (to whet your interest!) 

 - Ilya Sutskever (2011) trained a special type of recurrent neural net to predict the next character in a sequence. 
 - After training for a long time on a string of half a billion characters from English Wikipedia, he got it to generate new text. 
    - It generates by predicting the probability distribution for the next character and then sampling a character from this distribution. 

### Symmetrically connected networks

 - These are like recurrent networks, but the connections between units are symmetrical (they have the same weight in both directions)
    - John Hopfield (and others) realized that symmetric networks are much easier to analyze than recurrent networks. 
    - They are also more restricted in what they can do. because they obey an energy function. 
        - **For example, they cannot model cycles**.
 - Symmetrically connected nets without hidden units are called “Hopfield nets”

---

## A geometrical view of perceptrons

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_perceptron_architecture.png)

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


### The cone of feasible solutions

 - To get all training cases right we need to find a point on the right side of all the planes. 
    - There may not be any such point! 
 - If there are any weight vectors that get the right answer for all cases, they lie in a hyper-cone with its apex at the origin. 
    - So the average of two good weight vectors is a good weight vector. 
        - **The problem is convex** 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space_con.png)

 - consider two inputs that both have a label of 1. we use a yellow arrow to represent a weight vectors which correctly classify the 2 inputs.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/NNet_weight_space_con2.png)

## What perceptrons can’t do 

### The limitations of Perceptrons

 - If you are allowed to choose the features by hand and if you use enough features, you can do almost anything
    - For binary input vectors, we can have a separate feature unit for each of the exponentially many binary vectors and so we can make any possible discrimination on binary input vectors. (feature mapping ?)
        - This type of table look-up won’t generalize. 
 - But once the hand-coded features have been determined, there are very strong limitations on what a perceptron can learn.  

### What binary threshold neurons cannot do 

 - A binary threshold output unit cannot even tell if two single bit features are the same! 
    - Positive cases (same): (1,1) -> 1; (0,0) -> 1 
    - Negative cases (different): (1,0) -> 0; (0,1) -> 0 
 - The four input-output pairs give four inequalities that are impossible to satisfy: 
    - w₁+w₂ >= θ , 0 >= θ
    - w₁<θ , w₂<θ 

### Learning with hidden units 

 - Networks without hidden units are very limited in the input-output mappings they can learn to model. 
    - More layers of linear units do not help. Its still linear. 
    - Fixed output non-linearities are not enough. 
 - We need multiple layers of **adaptive**,  non-linear hidden units. But how can we train such nets? 
    - We need an efficient way of adapting **all** the weights, not just the last layer.  This is hard.
    - Learning the weights going into hidden units is equivalent to learning features
    - This is difficult because nobody is telling us directly what the hidden units should do. 

---

# Lecture 3 



 


