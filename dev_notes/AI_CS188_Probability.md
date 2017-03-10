...menustart

 - [Probability](#0d2765b30694ee9f4fb7be2ae3b676dc)
	 - [Random Variables](#8a93f7814e04aeb4a3435d0667b581d7)
	 - [Probability Distribution](#65b393733707f82733184765aa503081)
	 - [Joint Distributions](#7d5c8826b9086639339acd137cdef0cc)
	 - [Marginal Distributions](#34b3d41097573990cabbad8ae1d9c969)
	 - [Conditional Distribution](#d22ece9f9682b018dfb17860cc5aedd7)
	 - [Normalization Trick](#1a18f3ea65669c3a4a2a7eff540de62e)
	 - [To Normalize](#730a75b3c3a77c4efa7e801fc1f306ea)
	 - [Inference by Enumeration](#314fa4378b3b188832e3f68fd46ac015)

...menuend



<h2 id="0d2765b30694ee9f4fb7be2ae3b676dc"></h2>
# Probability

In part 2 we will assume that the models are given to us.


demo: ghost busters

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_prob_ghostbuster.png)

 - A ghost is in the grid somewhere
 - Sensor readings tell how close a square is to the ghost
    - On the ghost: red
    - 1 or 2 away: orange
    - 3 or 4 away: yellow
    - 5+ away: green
 - On top of ghost, we usually get red, but we could get green.   It's a nosiy sense. 
 - Sensors are noisy, but we know P(Color | Distance)

---

 P( red|3 )| P( orange|3 )   | P( yellow|3 )   |P( green|3 )
 --- | --- | --- | --- 
 0.05 | 0.15 | 0.5 | 0.3 
   
---

## Uncertainty

When we deal with an uncertainty usually we can split the random variables into 2 groups. one group is the group of random variables that would get to observe. We get to measure them and usually then we want to do is somehow  in first something about the variables we don't get to measure -- the hidden variables , the unobserved variables -- and do that in some structured way. And the way that is structures using a probability model that tells us measurements related a noisy way to these hidden variables that we don't get to observe. 

 - General situation:
    - **Observed variables (evidence)**: 
        - Agent knows certain things about the state of the world (e.g., sensor readings or symptoms)
    - **Unobserved variables**: 
        - Agent needs to reason about other aspects (e.g. where an object is or what disease is present)
    - **Model**: 
        - Agent knows something about how the known variables relate to the unknown variables
 - Probabilistic reasoning gives us a framework for managing our beliefs and knowledge



<h2 id="8a93f7814e04aeb4a3435d0667b581d7"></h2>
## Random Variables

 - A random variable is some aspect of the world about which we (may) have uncertainty
    - R = Is it raining?
    - T = Is it hot or cold?
    - D = How long will it take to drive to work?
    - L = Where is the ghost?
 - We denote random variables with capital letters
 - Like variables in a CSP, random variables have domains
    - R in {true, false}   (often write as {+r, -r})
    - T in {hot, cold}
    - D in [0, ∞ )
        - could be continuous.
    - L in possible locations, maybe {(0,0), (0,1), …}



<h2 id="65b393733707f82733184765aa503081"></h2>
## Probability Distribution 

 - Associate a probability with each value

**Temperature:  P(T)**

 T | P 
 --- | --- 
 hot | 0.5
 cold | 0.5

**Weather: P(W)**

 W | P 
 --- | --- 
 sun | 0.6
 rain | 0.1
 fog | 0.3
 memeor | 0.0


 - A distribution is a TABLE of probabilities of values
 - A probability (lower case value) is a single number
    - P(W = rain ) = 0.1 
    - shorthand notation: P(rain) = P(W=rain), OK if all domain entries are unique
 - Must have:  ∀x P(X=x) ≥ 0 , and ∑ᵪ P(X=x) = 1



---



<h2 id="7d5c8826b9086639339acd137cdef0cc"></h2>
## Joint Distributions

The reason we care about joint distribution is because we want to infer things about variables we haven't observed based on observations we made of these observed variables. 

 - A joint distribution over a set of random variables: X₁,X₂, ... X<sub>n</sub> specifies a real number for each assignment (or outcome): 
    - P(X₁=x₁ ,X₂=x₂ , ... , X<sub>n</sub>=x<sub>n</sub>)
    - P(x₁ ,x₂ , ... , x<sub>n</sub>)
 - Size of distribution if n variables with domain sizes d :
    - dⁿ
    - For all but the smallest distributions, impractical to write out!

---

P(T,W)

T | W | P 
--- | --- | --- 
hot | sun | 0.4
hot | rain | 0.1
cold | sun | 0.2
cold | rain | 0.3 

---



## Probabilistic Models

 - A probabilistic model is a joint distribution over a set of random variables
    - see that ***Distribution over T,W*** in privous paragraph
 - Probabilistic models:
    - (Random) variables with domains 
    - Assignments are called outcomes
    - Joint distributions: say whether assignments (outcomes) are likely
    - Normalized: sum to 1.0
    - Ideally: only certain variables directly interact
 - Constraint satisfaction problems:
    - Variables with domains
    - Constraints: state whether assignments are possible
    - Ideally: only certain variables directly interact

 - Sometimes the main different is that here you have true/false values saying whether it's allowed to have an association or not. 

---

***Constraint over T,W***

T | W | P          
--- | --- | ---     
hot | sun | true     
hot | rain | false    
cold | sun | false  
cold | rain | true  

---

<h2 id="34b3d41097573990cabbad8ae1d9c969"></h2>
## Marginal Distributions

corresponds to a sub-table of the original joint distribution  where you consider only a subset of the random variables.

 - Marginal distributions are sub-tables which eliminate variables 
 - Marginalization (summing out): Combine collapsed rows by adding

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_prob_margial_distribution.png)





<h2 id="d22ece9f9682b018dfb17860cc5aedd7"></h2>
## Conditional Probabilities

 - A simple relation between joint and conditional probabilities
    - In fact, this is taken as the definition of a conditional probability
 - `P(a|b) = P(a,b) / P(b)`


## Conditional Distribution

 - Conditional distributions are probability distributions over some variables given fixed values of others

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_prob_conditional_distribution.png)

P(W|T)  is a set of tables -- one table for each value T can take on and then for a fixed value of T you get a conditional distribution table.

Each of these individual tables sums to 1. 

<h2 id="1a18f3ea65669c3a4a2a7eff540de62e"></h2>
## Normalization Trick

It's a way to go from joint distributions to conditional distributions and has slightly quicker way and also a little more mechanical. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_prob_normalize_trick.png)

<h2 id="730a75b3c3a77c4efa7e801fc1f306ea"></h2>
## To Normalize 

 All entries sum to 1. 

## Probabilistic Inference

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_prob_probabilistic_inference.png)

 - Probabilistic inference: compute a desired probability from other known probabilities (e.g. conditional from joint)
 - We generally compute conditional probabilities
    - P(on time | no reported accidents) = 0.90
    - These represent the agent’s beliefs given the evidence
 - Probabilities change with new evidence:
    - P(on time | no accidents, 5 a.m.) = 0.95
    - P(on time | no accidents, 5 a.m., raining) = 0.80
    - Observing new evidence causes beliefs to be updated




---

<h2 id="314fa4378b3b188832e3f68fd46ac015"></h2>
## Inference by Enumeration

 - General case:
    - All variables: X₁,X₂,...,X<sub>n</sub>
    - Evidence variables: E₁,...,E<sub>k</sub> = e₁,...,e<sub>k</sub>
    - Query<sup>\*</sup> variable: Q
    - Hidden variables: H₁, ..., Hᵣ




P(W)      Q=W, E=∅ , H={S,T}
                                
P(W) | / 
--- | ---
s   | 0.65
r   | 0.35




P(W|winter)    Q=W, E=S , H=T

P(W | winter) | /
--- | ---
s   |  0.25 / 0.5 = 0.5 
r   |  0.25 / 0.5 = 0.5


P(W| winter ,hot)    Q=W , E=winter,hot, H=∅

P(W| winter ,hot) | /
--- | ---
s   |  0.10/0.15 = 2/3
r   |  o.05/0.15 = 1/3












