
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



   







