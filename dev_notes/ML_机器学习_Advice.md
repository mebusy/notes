
    Evaluating a Learning Algorithm
        Evaluating a hypothesis
        training/testing procedure
        Model Selection and Train/Validation/Test Sets
    Bias vs. Variance
        Diagnosing Bias vs. Variance
        regularization in high-order polynomial
        choosing the regularization parameter λ
        Learning Curve
        What should you try next ?


# Advice for Applying Machine Learning

## Evaluating a Learning Algorithm

#### Evaluating a hypothesis 

    split the data we have into 2 portions.
    The 1st portion is going to be our usual training set. (70%)
    The 2nd portion is going to be our test set. (30%)
    
    It there is any sort of ordinary to the data.
    That should be better to shuffle training/test set randomly.


#### training/testing procedure

    - Learn parameter θ from training data.
    - use θ to compute test set error 
      
      for linear regression : error = J(θ) (with out regularization)
      for logistic regression:   set  err( h(x), y ) = (h(x)>=0.5, y=0 or h(x)<0.5, y=1) and 1 or 0
    	error = 1/m_test ∑ err( h(x_test), y_test )


#### Model Selection and Train/Validation/Test Sets

    Try serveral models with different degree of polynomial , such as:
    d=1, h(x)=θ₀+θ₁x
    d=2, h(x)=θ₀+θ₁x+θ₂x²
    ...
    d=10, h(x)=θ₀+θ₁x+ ... +θ₁₀x¹⁰

    split the data into 3 pieces.
    1st part, training set  (60%)
    2nd part, cross validation (CV) set  (20%)
    3rd part, test set  (20%)

    - Learn parameter θ from training data.
    - compute CV set error , pick the best model with lowest error.
    - estimate generalization error for test set.
    
    
## Bias vs. Variance

#### Diagnosing Bias vs. Variance

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/BiasVsVariance.png)

BiasVsVariance.png

    Bias(underfit)
    
        J(θ) of train set will be high,
        J(θ) of CV also will be high.
        
        J_train ≈ J_cv
    
    
    Variance(overfit)
    
        J(θ) of train set will be low,
        J(θ) of CV also will be high.
        
        J_cv >> J_train


#### regularization in high-order polynomial

λ	|		θ	|	fitting result
---|---|---
small (eg.0)	| no penalty  	|	  High variance (overfit)
intermediate 	|			|	just right
large (eg.100) | heavily penalized → 0 | High Bias(underfit)


---

#### choosing the regularization parameter λ

 - Try serveral different λs. eg. λ=0 , λ=0.01, λ=0.02, λ=0.04  , ... , λ=10.24 (start from no regularization, and with *2 step )
 - minimize J_train(θ) with regularization and computer the parameter θ with each λ
 - computer the J_cv(θ) with the different θ (without regularization), and pick the best θ with lowest error (eg. θ₄)
 - see how θ₄ works on test set (without regularization).

---

train / CV set affected by λ:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/regularization_BiasVsVariance.png)

---

#### Learning Curve

Plot learning curve give you a better sense of whether there is a bias or variance problem, or a bit of both.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LearnCurve_high_bias.png)

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/LearnCurve_high_variance.png)

**For** variance problem, if you provide more and more training sample, J_train / J_cv may be `converge` to each other.

--- 
 - learn paramete θ from training subset (i.e., X(1:n,:) and y(1:n))
 - compute the training set error on training subset
 - compute CV set error over the **entire** cross validation set

#### What should you try next ?

--- 

you implemented regularization linear regression to predict housing prices. 

But you find your hypothesis make unacceptable large errors in its prediction.

What should you try next ?

- Get more training examples  -> fix high variance
- Try smaller sets of features  -> fix high varinance
- Try getting additional features -> fix high bias
- Try adding polynomial features  -> fix high bias
- Try decreasing λ	-> fix high bias
- Try increasing λ	-> fix high variance

---

**neural network** case:

"small" neural network (fewer parameters): more prone to underfitting.

eg. 2-3-1 newwork , it's computationally cheaper.

`fewer parameters means fewer hidden layer, fewer hidden units`

"large" neural network (more parameters): more prone to overfitting.

eg.2-10-1 , 2-5-5-5-1, it's computationally more expensive.

**Using** a `large` neural network ,and using regularization(λ) to address overfitting, is often more effective than using a smaller neural network.


