...menustart

 - [Markov Models](#d656a155bed68a7dec83cd56ff973bbc)
	 - [Markov Models](#d656a155bed68a7dec83cd56ff973bbc)
		 - [Joint Distribution of a Markov Model](#2549029b268b93144235df84effeb97d)
		 - [Chain Rule and Markov Models](#1584c0069936b81fd7e2d00d4dc7186a)
		 - [Implied Conditional Independencies](#5627b13e1756dc92c82a9b3998e04960)
		 - [Markov Models Recap](#464ada4a5a716b995c9e27993b0c4662)
		 - [Example Markov Chain : Weather](#a3e9d92d013e8bd559c093cbca5a7684)
		 - [Example Run of Mini-Forward Algorithm](#913aa6b09921c6acd9c30a9b77986973)

...menuend


<h2 id="d656a155bed68a7dec83cd56ff973bbc"></h2>

# Markov Models


<h2 id="d656a155bed68a7dec83cd56ff973bbc"></h2>

## Markov Models

Markov model means sequence of random variables. 

 - Value of X at a given time is called the state
    - X₁ -> X₂ -> X₃ -> X₄ -> ...
    - X₁ has an influence on X₂ going to be , X₂ has an influcence on X₃ going to be , ... 
    - P(X₁)
    - P(X<sub>t</sub> | X<sub>t-1</sub>) 

 - Parameters: called ***transition probabilities*** or dynamics, specify how the state evolves over time (also, initial state probabilities)
 - Stationarity assumption: transition probabilities the same at all times
    - this means transition probabilities P(x<sub>t</sub> | x<sub>t-1</sub> ) don't depend on time, they are always the same. 
 - Same as MDP transition model, but no choice of action
    
<h2 id="2549029b268b93144235df84effeb97d"></h2>

### Joint Distribution of a Markov Model

This case let's look at just 4 variables. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_markov_4state_joint_distribution.png)

 - Joint distribution:
    - P(X₁, X₂, X₃, X₄) = P(X₁)·P(X₂|X₁)·P(X₃|X₂)·P(X₄|X₃)
 - More generally
    - P(X₁, X₂, ..., X<sub>T</sub>) = P(X₁)·P(X₂|X₁)·P(X₃|X₂)...P(X<sub>T</sub>|X<sub>T-1</sub>)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_markov_4state_joint_distribution_generally.png)
 - 简化版 Chain Rule

<h2 id="1584c0069936b81fd7e2d00d4dc7186a"></h2>

### Chain Rule and Markov Models

 - From the chain rule, every joint distribution over X₁, X₂, X₃, X₄ , can can be written as:
    - P(X₁, X₂, X₃, X₄) = P(X₁)·P(X₂|X₁)·P(X₃|X₁,X₂)·P(X₄|X₁,X₂,X₃)  
 - Assuming that
    - X₃ ⫫ X₁|X₂  
        - What dose that mean ?  That means that once somebody tells you the value of X₂,  you write the distribution of X₃ ; somebody then tells you what X₁ is and the distribution of X₃ doesn't change -- stays the same. 
    - X₄ ⫫ X₁,X₂ | X₃ 
 - results in the expression posited on the previous slide: 
    - P(X₁, X₂, X₃, X₄) = P(X₁)·P(X₂|X₁)·P(X₃|X₂)·P(X₄|X₃)

--- 

 - generally
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_markov_chain_rule_generally.png)


<h2 id="5627b13e1756dc92c82a9b3998e04960"></h2>

### Implied Conditional Independencies 

 - We assumed : `X₃ ⫫ X₁|X₂`  , and `X₄ ⫫ X₁,X₂ | X₃` 
 - We also have :  `X₁ ⫫ X₃,X₄ |X₂`
 - proof:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_markov_implied_conditional_probability.png)
 - Additional explicit assumption
    - P(X<sub>t</sub>|X<sub>t-1</sub>) is the same for all t   // TODO  why ?

### Conditional Independence

 - Basic conditional independence:
    - Past and future independent of the present
    - Each time step only depends on the previous
    - This is called the (first order) Markov property
 - Note that the chain is just a (growable) BN
    - We can always use generic BN reasoning on it if we truncate the chain at a fixed length





<h2 id="a3e9d92d013e8bd559c093cbca5a7684"></h2>

### Example Markov Chain : Weather

<h2 id="913aa6b09921c6acd9c30a9b77986973"></h2>

### Example Run of Mini-Forward Algorithm

the stationary distribution of Markov Model


