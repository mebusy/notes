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

User attention:

let's say you tried to follow where you just pay attention on the screen you attract your attention to your advertising , for example.

---


<h2 id="d656a155bed68a7dec83cd56ff973bbc"></h2>

## Markov Models

Markov model means sequence of random variables. 

X₁ has an influence on X₂ going to be , X₂ has an influcence on X₃ going to be , ... 


 - Parameters: called ***transition probabilities*** or dynamics, specify how the state evolves over time (also, initial state probabilities)
 - Stationarity assumption: transition probabilities the same at all times
    - this means transition probabilities P(x<sub>t</sub> | x<sub>t-1</sub> ) don't depend on time, they are always the same. 
 - Same as MDP transition model, but no choice of action
    
<h2 id="2549029b268b93144235df84effeb97d"></h2>

### Joint Distribution of a Markov Model

This case let's look at just 4 variables. 

<h2 id="1584c0069936b81fd7e2d00d4dc7186a"></h2>

### Chain Rule and Markov Models

X₃ ⫫ X₁|X₂  

What dose that mean ?  That means that once somebody tells you the value of X₂,  you write the distribution of X₃ ; somebody then tells you what X₁ is and the distribution of X₃ doesn't change -- stays the same. 


<h2 id="5627b13e1756dc92c82a9b3998e04960"></h2>

### Implied Conditional Independencies 



<h2 id="464ada4a5a716b995c9e27993b0c4662"></h2>

### Markov Models Recap 

<h2 id="a3e9d92d013e8bd559c093cbca5a7684"></h2>

### Example Markov Chain : Weather

<h2 id="913aa6b09921c6acd9c30a9b77986973"></h2>

### Example Run of Mini-Forward Algorithm

the stationary distribution of Markov Model


