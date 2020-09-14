...menustart

- [Application Of HMM](#707c429b9c8c69d66ffa62008078d67c)
    - [Robot Localization](#cb8f3326ecf05b343100368b1fce61b4)
    - [Robot Mapping](#456efe59f69acce2f3949ed5ec0af420)
    - [Dynamic Bayes Nets (DBNs)](#e2237c4bb83f0a39f439746f01a1814f)
    - [DBN Particle Filters](#8b6016f7e9c11348859d14b1b2968de6)
    - [Most Likely Explanation](#acde5ccfd9d402faf86e320b802cdf2e)
        - [HMMs: MLE Queries](#a6f1a19a2e48162ea4decdd5eebe0d71)
        - [State Trellis](#9505b7524724df56002d7434a8ab6d4d)
        - [Forward / Viterbi Algorithms](#d1b64f8404dac1019eb7a414a8e5f21c)
    - [Speech Recognition](#9a29398560f1a8666e7f69250d88245e)

...menuend


<h2 id="707c429b9c8c69d66ffa62008078d67c"></h2>


# Application Of HMM


<h2 id="cb8f3326ecf05b343100368b1fce61b4"></h2>


## Robot Localization 

 - In robot localization:
    - We know the map, but not the robot’s position
    - Observations may be vectors of range finder readings
    - State space and readings are typically continuous (works basically like a very fine grid) and so we cannot store B(X)
    - Particle filtering is a main technique
 

![](../imgs/cs188_hmm_app_robot_localization.png)

 - eg. 初始 40000 particles 
 - 随着evidence 收集，当大量 particle 聚集到一处时， 在 resample 的时候，可以减少 particle 的数量


<h2 id="456efe59f69acce2f3949ed5ec0af420"></h2>


## Robot Mapping 

You can not just localize the robot , you can also build a map at the same time. 

 - SLAM: Simultaneous Localization And Mapping
    - We do not know the map or our location
    - State consists of position AND map!
        - there is many many possible maps of a place you haven't seen 
        - as the robot moves it'll get a measurement it'll see how compatible is this measurement with the map and with my localtion in that map. 
    - Main techniques: Kalman filtering (Gaussian HMMs) and particle methods

---

<h2 id="e2237c4bb83f0a39f439746f01a1814f"></h2>


## Dynamic Bayes Nets (DBNs)

DBNs are a special form of HMM. At each time it can be more than one variable that's in the state and more than one variable that's in the evidence. 

![](../imgs/cs188_hmm_app_DBNs.png)

So you could have 2 ghosts , each of them has own state variable -- their location, and each of them has their own evidence variable -- something noise about where they might be. 

Then as time passes somehow the way to transition to next time where they might be is related. Ghost B might decide where to go based on where ghost A is. Same for ghost A. 


![](../imgs/cs188_hmm_app_DBNs_trans.png)

 - We want to track multiple variables over time, using multiple sources of evidence
 - Idea: Repeat a fixed Bayes net structure at each time
 - Variables from time t can condition on those from t-1
 - Dynamic Bayes nets are a generalization of HMMs

You can think G<sub>t</sub>ª , G<sub>t</sub>ᵇ combined as a big state, and think E<sub>t</sub>ª , E<sub>t</sub>ᵇ combined as a big evidence , then it would be a HMM again. But you would be ignoring the structure that's underneath.  And exploiting structure underneath allows you to become additonally more efficient.

<h2 id="8b6016f7e9c11348859d14b1b2968de6"></h2>


## DBN Particle Filters

You can again rul particle filtering in these. 

 - A particle is a complete sample for a time step
    - you don't have a particle per ghost , you have a particle for the entire state. there's 2 ghosts , one particle encodes location of both ghosts.
 - Initialize: Generate prior samples for the t=1 Bayes net
    - Example particle: G₁ª = (3,3) G₁ᵇ = (5,3)
 - Elapse time: Sample a successor for each particle 
    - Example successor: G₂ª = (2,3) G₂ᵇ = (6,3)
 - Observe: Weight each ***entire*** sample by the likelihood of the evidence conditioned on the sample
    - Likelihood: P(E₁ª |G₁ª ) * P(E₁ᵇ |G₁ᵇ ) 
 - Resample: Select prior samples (tuples of values) in proportion to their likelihood

Why is it important that your particles contain both ghost at once? You can imagine running 2 separate particle filtering, one for ghost A, one for ghost B. If you were to do that then you can not model the dependency. Your distribution will not represent the joint between the two ghosts. 

---

<h2 id="acde5ccfd9d402faf86e320b802cdf2e"></h2>


## Most Likely Explanation

quite important 

A different way of doing inference. 

![](../imgs/cs188_hmm_MLE.png)

So far what we've looked at is something that computes the distribution over possible states at the current time , given all the evidence we've seen so far.

Sometimes what you want to do is you see all the evidence and based on all the evidence you've seen you want to reconstruct the most likely sequence of events that explains that whole sequence of evidence.  What is the most likely sequence of states given the evidence I have observed ?  

<h2 id="a6f1a19a2e48162ea4decdd5eebe0d71"></h2>


### HMMs: MLE Queries

We're given an HMM still , and the query is what's the most likely explanation of the evidence we have observed. 

 - New query: most likely explanation:
    - ![](../imgs/cs188_hmm_app_mle_query.png)
    - we're trying to find what the most likely sequence of X variables. 
 - New method: the Viterbi algorithm


<h2 id="9505b7524724df56002d7434a8ab6d4d"></h2>


### State Trellis

 - State trellis: graph of states and transitions over time
    - ![][1]
    - evidence does not showed on this picture
 - Each arc represents some transition: x<sub>t-1</sub> → x<sub>t</sub>
 - Each arc has weight: P( x<sub>t</sub>|x<sub>t-1</sub> )·P(e<sub>t</sub> | x<sub>t</sub> )
    - the weight of red arc is : P(rain|sun)·P(e₂|rain)
 - Each path is a sequence of states
    - then you can start looking at path in this graph.
    - each path encodes the sequence of states , there are many many paths
    - if you multiply the weights , to put each of these edges together, for a given path, that gives us the probability of that particular state sequence jointly with the evidence. 
 - The product of weights on a path is that sequence’s probability along with the evidence
    - the path with highest probability , is the most likely explanation of the sequence of evidence we observe
 - Forward algorithm computes sums of paths, Viterbi computes best paths

<h2 id="d1b64f8404dac1019eb7a414a8e5f21c"></h2>


### Forward / Viterbi Algorithms

![][1]


 - Forward Algorithm (Sum)
    - ![](../imgs/cs188_hmm_app_forward_algorithm.png)
    - recursive computation 
    - we keep track of the probability of x<sub>t</sub> jointly with all the evidence so far . 
 - Viterbi Algorithm (Max)
    - ![](../imgs/cs188_hmm_app_viterbi_algorithm.png)
    - changed ∑ to max

---

<h2 id="9a29398560f1a8666e7f69250d88245e"></h2>


## Speech Recognition








    
     
    
    
















---

 [1]: ../imgs/cs188_hmm_app_state_trellis.png



