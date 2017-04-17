
# Bayes' Nets: Inference


## Recap: Example: Alarm Network

![][1]

## Inference

 - Inference: calculating some useful quantity from a joint probability distribution
 - Examples:
    - Posterior probability
        - P( Q| E₁=e₁,...,E<sub>k</sub>=e<sub>k</sub> )
        - computing the posterior probability of some set of query variables conditioned on some evidence having been observed 
    - Most likely explanation
        - argmax<sub>q</sub> P( Q=q | E₁=e₁...)
        - given some evidence has bee observed, what's the most likely association of some query variables.

## Inference by Enumeration

 - the first type of inference is the naive type of inference is inference by enumeration
 - we have some query , and the query has 
    - some evidence variables E₁...E<sub>k</sub> , 
    - some query variables Q , the ones which we want to distribution given the evidence variables.
    - some hidden variables. H₁...H<sub>r</sub> , the ones that are not query variables , not query variables, but yet still are in our joint distribution.
        - we have to deal with them, you will have to sum them out effectively to get rid of them.
 - see details in [Probability](https://github.com/mebusy/notes/blob/master/dev_notes/AI_CS188_Probability.md)

## Inference by Enumeration in Bayes’ Net

 - Given unlimited time, inference in BNs is easy
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_BNgraph_alarm_network.png)
 - Reminder of inference by enumeration by example:
    - P(B|+j,+m) ∝<sub>B</sub> P(B,+j,+m)
    - = ∑<sub>e,a</sub> P(B,e,a,+j,+m)
    - now we can use the definition if the joint distribution as its specified through the Bayes net :
    - = ∑<sub>e,a</sub> P(B)P(e)P(a|B,e)P(+j|a)P(+m|a)
    - = P(B)P(+e)P(+a|B,+e)P(+j|+a)P(+m|+a) + P(B)P(+e)P(-a|B,+e)P(+j|-a)P(+m|-a) + P(B)P(-e)P(+a|B,-e)P(+j|+a)P(+m|+a) + P(B)P(-e)P(-a|B,-e)P(+j|-a)P(+m|-a)

 - if we have 100 variables in the BNs , 50 of them are evidence variables,  means 50 of them not evidence variables that will look at 2⁵⁰ entries 
    - it gets very expensive,  exponential in a number of non-evidence variables ,  unless almost everything is evidence
 - It's not ideal to do it this way

## Inference by Enumeration vs. Variable Elimination

 - Why is inference by enumeration so slow?
    - You join up the whole joint distribution before you sum out the hidden variables
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_Inference_image_by_enumeration.png)
 - Idea: interleave joining and marginalizing!
    - Called "Variable Elimination"
    - Still NP-hard, but usually much faster than inference by enumeration
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_image_by_variable_elimination.png)
    - we'll find a way to interleave joining CPTs together and summing out over hidden variables. 
    - keep in mind it's not a silver bullet. Inference in BNs is np-hard. There are BNs where no matter what you do to compute the answer to the query is equivalent to solving a SAP(storage assignment problem) problem which is known that nobody has a efficient solution for. 
    - First we’ll need some new notation: factors

## Factor Zoo

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_factor_zoo.png)

### Factor Zoo I 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_factor_zoo_1.png)


 - Joint distribution: P(X,Y)
    - Entries P(x,y) for all x, y
    - Sums to 1

Example: P (T,W)

T | W | P
--- | --- | --- 
hot | sun | 0.4
hot | rain | 0.1
cold | sun | 0.2
cold | rain | 0.3


 - Selected joint: P(x,Y)
    - A slice of the joint distribution
    - Entries P(x,y) for fixed x, all y
    - Sums to P(x)
        - factors don't have to sum to 1

Example: P( cold , W)

T | W | P
--- | --- | --- 
cold | sun | 0.2
cold | rain | 0.3

 - Number of capitals = dimensionality of the table
 - So as we work in this variable elimination process , the game will be one of trying to keep the number of capitialized variables small in our factor. 

### Factor Zoo II 

 - Single conditional: P(Y | x)
    - Entries P(y | x) for fixed x, all y
    - Sums to 1
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_factor_zoo_20.png)


Example: P(W|cold)

T | W | P
--- | --- | ---
cold | sun | 0.4
cold | rain | 0.6

 - Family of conditionals: P(X |Y)
    - Multiple conditionals
    - Entries P(x | y) for all x, y
    - Sums to |Y|
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_factor_zoo_21.png)


Example : P(W|T)

T | W | P 
--- | --- | ---
hot | sun | 0.8
hot | rain | 0.2
cold | sun | 0.4
cold | rain | 0.6

### Factor Zoo III 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_factor_zoo_3.png)

 - Specified family: P( y | X )
    - Entries P(y | x) for fixed y, but for all x
    - Sums to … who knows!

Example: P(rain | T)

T | W | P
--- | --- | ---
hot | rain | 0.2
cold | rain | 0.6

### Factor Zoo Summary

 - In general, when we write P(Y₁ … Y<sub>N</sub> | X₁ … X<sub>M</sub>)
    - It is a “factor,” a multi-dimensional array
    - Its values are P(y₁ … y<sub>N</sub> | x₁ … x<sub>M</sub>)
    - Any assigned (=lower-case) X or Y is a dimension missing (selected) from the array
     
### Example : Traffic Domain 

 - R → T → L 
 - Random Variables
    - R: Raining
    - T: Traffic
    - L: Late for class!

P(R)

+r | 0.1
--- | ---
-r | 0.9

P(T|R)

+r | +t | 0.8
--- | --- | ---
+r | -t | 0.2
-r | +t | 0.1
-r | -t | 0.9

P(L|T)

+t | +l | 0.3
--- | --- | ---
+t | -l | 0.7
-t | +l | 0.1
-t | -l | 0.9

 - query: P(L) = ?
    - for inference enumertation:
    - P(L) = ∑<sub>r,t</sub> P(r,t,L) 
    - = ∑<sub>r,t</sub> P(r)P(t|r)P(L|t)

## Inference by Enumeration: Procedural Outline

 - Track objects called factors
 - Initial factors are local CPTs (one per node)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_RTL_1.png)
 - Any known values are selected
    - E.g. if we know L = +l  , the initial factors are
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_RTL_2.png)
 - Procedure: Join all factors, then eliminate all hidden variables

### Operation 1: Join Factors

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op1_joinFactors.png)

 - First basic operation: ***joining factors***
 - Combining factors:
    - Just like a ***database join***
    - Get all factors over the joining variable
    - Build a new factor over the union of the variables involved
 - Example: Join on R
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op1_joinfactors_example_joinOnR.png)
 - Computation for each entry: pointwise products
    - ∀<sub>r,t</sub> : P(r,t) = P(r)·P(t|r)

#### Example: Multiple Joins

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op1_example_multiple_joins_1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op1_example_multiple_joins_2.png)
 
 - we call "Join on R" means that you grab all tables that have `R` in them. 
 - need 1 joint table, 1 conditinal table to "join" ?

### Operation 2: Eliminate

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op2_eliminate_example.png)

 - Second basic operation: ***marginalization***
 - Take a factor and sum out a variable
    - Shrinks a factor to a smaller one
    - A ***projection*** operation
        - get rid of the variables that don't matter -- the hidden variables
        - why do we even have hidden variables ? 
            - the reason we have it because we started with a joint distribution that was over more than the variables that appear in our query. 
 - Example:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op2_eliminate.png)

 
#### Multiple Elimination

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_op2_multiple_elimination.png)

--- 

 - Thus Far: Multiple Join, Multiple Eliminate (= Inference by Enumeration)
 - Marginalizing Early (= Variable Elimination)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_marginalize_early.png)
    - switch the some order of join/eliminate 
 - intuition
    - if you want to eliminate a variable , you can not do this until you have joined on that variable.  

### Example:  Traffic Domain again

 - R → T → L 
 - P(L) = ?
    - Inference by Enumeration
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_traffic_inference_by_enumeration.png)
    - Variable Elimination
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_traffic_inference_by_variable_elimination.png)

#### Marginalizing Early! (aka VE)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_marginalize_early_RTL_example.png)

 - so that is variable elimination .
 - what if your evidence ?
    - just like with the inference by enumeration , when there is evidence you just look at your tabels and you only retain those entries consistent with your evidence. 

### Evidence

 - If evidence, start with factors that select that evidence
    - No evidence  looks like this : uses these initial factors
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_no_evidence.png)
    - with evidence looks like this: computing P(L|+r) the initial factors become
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_with_evidence.png)
 - We eliminate all vars other than query + evidence
 - Result will be a selected joint of query and evidence
    - E.g. for P(L | +r), we would end up with:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_with_evidence_L+r.png)
 - To get our answer, just normalize this!
 - That's it!


---

## General Variable Elimination

 - Query: P( Q| E₁=e₁,...,E<sub>k</sub>=e<sub>k</sub> )
 - Start with initial factors:
    - Local CPTs (but instantiated by evidence) 
 - While there are still hidden variables (not Q or evidence):
    - Pick a hidden variable H
        - any ordering of hidden variables is valid
        - but some orderings will lead to very big factors being generated along the way 
        - and some orderings might be able to keep the factors generated along the way very small 
    - Join all factors mentioning H
    - Eliminate (sum out) H
 - Join all remaining factors and normalize

### Example 

![][1]

 - P(B|j,m) ∝ P(B,j,m)
 - P(B) , P(E) , P(A|B,E) , P(j|A) , P(m|A) 

---

 - Choose *A* 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_example_A.png)
    - the size of the tables generated along the way is 2³,  in this case it wasn't too bad , it's possible to handle. but if you have a very large BNs you need to be careful about your orderingto make sure you keep it low. 
    - P(B) , P(E) , P(j,m|B,E)
 - Choose *E*
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_example_E.png)
    - P(B) , P(j,m|B)
 - Finish with B
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_example_B.png)
 

### Same Example in Equations

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_VE_same_example_in_equations.png)

 - equations from top to bottom 
    1. marginal can be obtained from joint by summing out
    2. use Bayes' net joint distribution expression
    3. use `x*(y+z) = xy + xz`
    4. joining on *a* , and then summing out give f₁
    5. use `x*(y+z) = xy + xz` 
    6. joining on *e* , and then summing out give f₂
 - **All we are doing is exploiting uwy + uwz + uxy + uxz + vwy + vwz + vxy +vxz = (u+v)(w+x)(y+z) to improve computational efficiency** !
 - how do you decide which variables to pick first ?  
    - suggestion here was **a variable with very few connections** .  Connections means that it is participating in a factor. 

### Another Variable Elimination Example










 




--- 

 [1]: https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_inference_example_BNgraph_alarm_network.png



