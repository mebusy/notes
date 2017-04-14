
# Bayes' Nets II : Independence

## Recap: Bayes’ Nets

 - A Bayes’ net is an efficient encoding of a probabilistic model of a domain
 - Questions we can ask:
    - Inference: given a fixed BN, what is P(X | e)?
    - Representation: given a BN graph, what kinds of distributions can it encode?
    - Modeling: what BN is most appropriate for a given domain?

## Bayes’ Net Semantics

 - A directed, acyclic graph, one node per random variable
 - A conditional probability table (CPT) for each node
    - A collection of distributions over X, one for each combination of parents’ values
    - P(X|a₁...a<sub>n</sub>)
 - Bayes’ nets implicitly encode joint distributions
    - As a product of local conditional distributions
    - To see what probability a BN gives to a full assignment, multiply all the relevant conditionals together:
        - P(x₁,x₂,...,x<sub>n</sub>) = ∏ⁿ<sub>i=1</sub> P(xᵢ|parent(Xᵢ) )

## Size of a Bayes’ Net

 - How big is a joint distribution over N Boolean variables?
    - 2ᴺ
 - How big is an N-node net if nodes have up to k parents?
    - O(N \* 2k+1)
 - Both give you the power to calculate joint distribution
 - BNs: Huge space savings!  Also easier to elicit local CPTs
    - Also faster to answer queries (coming)    

## Bayes Nets: Assumptions

 - Assumptions we are required to make to define the Bayes net when given the graph:
    - P(xᵢ |x₁,...,x<sub>i-1</sub>) = P(xᵢ|parent(Xᵢ) ) 
 - Beyond above “chain rule → Bayes net” conditional independence assumptions 
    - Often additional conditional independences
    - They can be read off the graph
 - Important for modeling: understand assumptions made when choosing a Bayes net graph

### Example

 - (X) → (Y) → (Z) → (W)
 - Conditional independence assumptions directly from simplifications in chain rule:
    - P(X,Y,Z,W) = ***P(X)·P(Y|X)·P(Z|Y)·P(W|Z)*** = P(X)·P(Y|X)·P(Z|X,Y)·P(W|X,Y,Z) 
    - from the fomular , we get:
        - Z⫫X |Y
        - W⫫(X,Y) |Z
 - Additional implied conditional independence assumptions?
    - W⫫X |Y

P(W|X,Y) =?= P(W|Y) ?

 P(W,X,Y)/P(X,Y) 

= ∑<sub>z</sub> **P(X)·P(Y|X)**·P(Z|Y)·P(W|Z) / **P(X)·P(Y|X)** 

= ∑<sub>z</sub> P(Z|Y)·P(W|Z)    // 和Z无关项 约分约掉

= ∑<sub>z</sub> P(Z **|Y**)·P(W|Z, **Y**)  // ?

now Y shared everywhere.  product rule 的 |Y 版本  

= ∑<sub>z</sub> P(Z,W|Y) 

= P(W|Y) . Proof!

---

Math proof is annoying !  So what we're going to look at now is a way to read it off directly from the graph structure. 

---

## Independence in a BN

 - Important question about a BN:
    - Are two nodes independent given certain evidence?
    - If yes, can prove using algebra (tedious in general)
    - If no, can prove with a counter example
    - Example: (X) → (Y) → (Z)  
 - Question: are X and Z necessarily independent?
    - Answer: no.  Example: low pressure causes rain, which causes traffic.
    - X can influence Z, Z can influence X (via Y)
    - Addendum: they ***could*** be independent: how?
        - independence is possible , just by a special choice. eg. always be a uniform distribution.
        - but the question is : Is independence guaranteed ?

## D-separation: Outline

 - Study independence properties for triples
 - Analyze complex cases in terms of member triples
 - D-separation: a condition / algorithm for answering such queries

### Causal Chains 

 - This configuration is a “causal chain”
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_causal_chains_example.png)
    - P(x,y,z) = P(x)P(y|x)P(z|y)
 - Guaranteed X independent of Z ?   **No!**
 - Guaranteed X independent of Z given Y?  **Yes!**
    - **Evidence along the chain “blocks” the influence** !

```
P(z|x,y) = P(x,y,z) / p(x,y)
         = P(x)P(y|z)P(z|y) / ( P(x)P(y|z) )
         = P(z|y)
```

### Common Cause

 - This configuration is a “common cause”
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_common_causal_example.png)
    - P(x,y,z) = P(y)P(x|y)P(z|y) 
 - Guaranteed X independent of Z ?   **No!**
 - Guaranteed X and Z independent given Y?  **Yes!**
    - **Observing the cause blocks influence between effects**.

```
P(z|x,y) = P(x,y,z) / p(x,y)  
         = P(y)P(x|y)P(z|y) / ( P(x)P(y|z) )
         = P(z|y)  
```

### Common Effect

 - Last configuration: two causes of one effect (v-structures)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_common_effect_example.png)

 - Are X and Y independent?
    - **Yes**: the ballgame and the rain cause traffic, but they are not correlated
    - that is the basic assumptions of BNs : Xᵢ is independent of its preceding variables X₁ ... X<sub>i-1</sub> , except its parents Pa(X₁) , given its parents | Pa(X₁)
    - for X,Y,Z , Y is independent of it's preceding variables, which is X , minus its parents , wich is ∅ , so Y is independent of X and then given the parents , which is empty set ∅ 
        - Y⫫X | ∅

P(x,y,z) = P(y)P(y)P(z|x,y)  

∑<sub>z</sub> P(x,y,z) = ∑<sub>z</sub> P(y)P(y)P(z|x,y) 

∑<sub>z</sub> P(x,y,z) = P(x)P(y) · ∑<sub>z</sub> P(z|x,y) 

∑<sub>z</sub> P(x,y,z) = P(x)P(y) · 1

--- 

 - Are X and Y independent given Z?
    - **No**: seeing traffic puts the rain and the ballgame in competition as explanation.
    - 如果有 traffic , 如果 没下雨，那很高概率有球赛, 如果下雨了，有球赛的概率就会下降
 - **This is backwards from the other cases**
    - Observing an effect **activates** influence between possible causes.


### The General Case

 - General question: in a given BN, are two variables independent (given evidence)?
 - Solution: analyze the graph
 - Any complex example can be broken into repetitions of the three canonical cases

#### Reachability

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_reachability.png)

 - Recipe: shade evidence nodes, look for paths in the resulting graph
 - Attempt 1: if two nodes are connected by an undirected path not blocked by a shaded node, they are conditionally independent
    - to check whether there is a path between 2 variables
    - then we check whether that path is blocked by something being observed along the path 
 - Almost works, but not quite
    - Where does it break?
    - Answer: the v-structure at *T* (RBT) doesn’t count as a link in a path unless “active”


#### Active / Inactive Paths


 - Question: Are X and Y conditionally independent given evidence variables {Z}?
    - Yes, if X and Y “d-separated” by Z
    - Consider all (undirected) paths from X to Y
    - No active paths = independence!
 - A path is active if each triple is active:
    - Causal chain A → B → C where B is unobserved (either direction)
    - Common cause A ← B → C where B is unobserved
    - Common effect (aka v-structure)
        - A → B ← C where B or **one of its descendents** is observed
        - for last one of active triples, if the children are just deterministic copies of their parents , then observing the variable at the bottom is the same as observing the the variable up there. 
        - so we're in the same scenario we've shown that influence can propagate.
 - All it takes to block a path is a single inactive segment


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_active_inactive_triples.png)

 - for a long path
    - we look at every triple along the path 
    - if every triple along the path is active , we have an active path
    - if one of the triples along the path is not active , we have an inactiv path. 
    - eg. (A) → (B) → (C) → (D) → (E) → (F)
        - you should check all possible triples 
        - ABC, BCD, CDE , DEF
    - every node on that path, has to be a middle node in one of your triples.

---

## D-separation

 - Query: Xᵢ ⫫ Xⱼ | { X<sub>k1</sub> , ... , X<sub>kn</sub> } ?
 - Check all (undirected!) paths between Xᵢ and Xⱼ 
    - If one or more active, then independence not guaranteed
        - Xᵢ not ⫫ Xⱼ | { X<sub>k1</sub> , ... , X<sub>kn</sub> } 
    - Otherwise (i.e. if all paths are inactive), then independence is guaranteed
        - Xᵢ ⫫ Xⱼ | { X<sub>k1</sub> , ... , X<sub>kn</sub> } 

          












