
# ML: Naive Bayes

 - Up until now: how use a model to make optimal decisions
 - Machine learning: how to acquire a model from data / experience
    - Learning parameters (e.g. probabilities)
    - Learning structure (e.g. BN graphs)
    - Learning hidden concepts (e.g. clustering)
 - Today: model-based classification with Naive Bayes


## Classification

### Example: Spam Filter
 
 - Input: an email
 - Output: spam/ham
 - Setup:
    - Get a large collection of example emails, each labeled “spam” or “ham”
    - Note: someone has to hand label all this data!
    - Want to learn to predict labels of new, future emails
 - Features: The attributes used to make the ham / spam decision
    - Words: FREE!
    - Text Patterns: $dd, CAPS
    - Non-text: SenderInContacts
    - ...



### Example: Digit Recognition

 - Input: images / pixel grids
 - Output: a digit 0-9
 - Setup:
    - Get a large collection of example images, each labeled with a digit
    - Note: someone has to hand label all this data!
    - Want to learn to predict labels of new, future digit images
 - Features: The attributes used to make the digit decision
    - Pixels: (6,8)=ON
    - Shape Patterns: NumComponents, AspectRatio, NumLoops
    - ...

## Model-Based Classification

 - Model-based approach
    - Build a model (e.g. Bayes’ net) where both the label and features are random variables
    - Instantiate any observed features
    - Query for the distribution of the label conditioned on the features
 - Challenges
    - What structure should the BN have?
    - How should we learn its parameters?


## Naïve Bayes for Digits

 - Naïve Bayes: Assume all features are independent effects of the label
    - ![][1] 
 - Simple digit recognition version:
    - One feature (variable) Fᵢⱼ for each grid position `<i,j>`
    - Feature values are on / off, based on whether intensity is more or less than 0.5 in underlying image
    - Each input maps to a feature vector, e.g.
        - 1 -> F<sub>0,0</sub>=0, F<sub>0,1</sub>=1, ... , F<sub>15,15</sub> =0
    - Here: lots of features, each is binary valued
 - Naïve Bayes model:
    - P(Y|F<sub>0,0</sub> ... <sub>15,15</sub>) ∝ P(Y)·∏<sub>i,j</sub> P(F<sub>i,j</sub>|Y)
 - What do we need to learn?

## General Naïve Bayes

 - A general Naive Bayes model:
    - ![][1]
    - P(Y,F₁...F<sub>n<sub>) = P(Y)·∏ᵢP(Fᵢ|Y)
        - from |Y|x|F|ⁿ values
        - to n x |F| x |Y| parameters
 - We only have to specify how each feature depends on the class
 - Total number of parameters is linear in n
 - Model is very simplistic, but often works anyway

### Inference for Naïve Bayes

 - Goal: compute posterior distribution over label variable Y
    - Step 1: get joint probability of label and evidence for each label
    - Step 2: sum to get probability of evidence
    - Step 3: normalize by dividing Step 1 by Step 2

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_naive_Bs_inference.png)


## General Naïve Bayes, Cont.

 - What do we need in order to use Naïve Bayes?
    - Inference method (we just saw this part)
        - Start with a bunch of probabilities: P(Y) and the P(Fᵢ|Y) tables
        - Use standard inference to compute P(Y|F₁…F<sub>n<sub>)
        - Nothing new here
    - Estimates of local conditional probability tables
        - P(Y), the prior over labels
        - P(Fᵢ|Y) for each feature (evidence variable)
        - These probabilities are collectively called the parameters of the model and denoted by θ
        - Up until now, we assumed these appeared by magic, but…
        - …they typically come from training data counts: we’ll look at this soon

### Example: Conditional Probabilities

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_naive_Bs_example_CP.png)


## Naïve Bayes for Text

 - Bag-of-words Naïve Bayes:
    - Features: Wᵢ is the word at positon i
    - As before: predict label conditioned on feature variables (spam vs. ham)
    - As before: assume features are conditionally independent given label
    - New: each Wᵢ is identically distributed
 - Generative model:
    - P(Y,W₁...W<sub>n</sub>) = P(Y)∏ᵢ P(Wᵢ|Y)
 - “Tied” distributions and bag-of-words
    - Usually, each variable gets its own conditional probability distribution P(F|Y)
    - In a bag-of-words model
        - Each position is identically distributed
        - All positions share the same conditional probs P(W|Y)
        - Why make this assumption?
    - Called “bag-of-words” because model is insensitive to word order or reordering

### Example: Spam Filtering

 - What are the parameters?
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_naive_Bs_example_spam.png)
 - Where do these tables come from?

 - example below
    - Tot field calculate the log value of total probability
        - log( P(Y,W₁, ... W<sub>n</sub>) ) = logP(Y) + ∑log( P(Wᵢ|Y) ) 
    - (prior) is P(Y)
    - the first word is `Gray`


Word | P(w\|spam) | P(w\|ham) | Tot Spam | Tot Ham 
--- | --- | --- | --- | --- 
(prior) | 0.33333 | 0.66666 | -1.1 | -0.4
Gary | 0.00002 | 0.00021 | -11.8 | -8.9 
world | 0.00069 | 0.00084 | -19.1 | -16.0
... | ... | ... | ... | ... 
sleep | 0.00006 | 0.00001 | -76.0 | -80.5


 - P(spam | w) = 98.9 
    - e<sup>-76.0</sup> / ( e<sup>-76.0</sup> + e<sup>-80.5</sup> ) = 98.9

## Training and Testing

### Important Concepts

 - Data: labeled instances, e.g. emails marked spam/ham
    - Training set
    - Held out set
    - Test set
 - Features: attribute-value pairs which characterize each x
 - Experimentation cycle
    - Learn parameters (e.g. model probabilities) on training set
    - (Tune hyperparameters on held-out set)
    - Compute accuracy of test set
    - Very important: never “peek” at the test set!
 - Evaluation
    - Accuracy: fraction of instances predicted correctly
 - Overfitting and generalization
    - Want a classifier which does well on test data
    - Overfitting: fitting the training data very closely, but not generalizing well
    - We’ll investigate overfitting and generalization formally in a few lectures


## Parameter Estimation

 - Estimating the distribution of a random variable
 - Elicitation: ask a human (why is this hard?)
 - Empirically: use training data (learning!)


## Smoothing

### Laplace Smoothing

 - Laplace’s estimate:
    - Pretend you saw every outcome once more than you actually did
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_ml_naive_laplace_smooth.png)
 - Can derive this estimate with Dirichlet priors (see cs281a)
 - for some purpose like zeor is not allowed.
 - example
    - samples: red, red, blue
    - P<sub>ML</sub>(X) = ( 2/3, 1/3 )
    - P<sub>LAP</sub>(X) = ( 3/5, 2/5 )  
        - adding 1 red, 1 blue





    


---

 [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_naive_BNs_bn4Digits.png








