...menustart

 - [Approximate inference: Sampling](#cc9a4c958f31f481f18fcc2449a18506)
	 - [Sampling](#1d07814d12178c958e4233501cb0bdc7)
	 - [Sampling in Bayes’ Nets](#7bdab2b4b6b4f6a48cbf1e07f48c7f94)
	 - [Prior Sampling](#d9850ac369194d66ab390de368f1cf63)
		 - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
	 - [Rejection Sampling](#da3112458f911630996b5661ccd81e9d)

...menuend


<h2 id="cc9a4c958f31f481f18fcc2449a18506"></h2>

# Approximate inference: Sampling 

<h2 id="1d07814d12178c958e4233501cb0bdc7"></h2>

## Sampling

 - Sampling is a lot like repeated simulation
    - Predicting the weather, basketball games, …
 - Basic idea
    - Draw N samples from a sampling distribution S
    - Compute an approximate posterior probability
    - Show this converges to the true probability P
 - Why sample?
    - Learning: get samples from a distribution you don’t know
    - Inference: getting a sample is faster than computing the right answer (e.g. with variable elimination)

--- 

 - Sampling from given distribution
    - Step 1: Get sample *u* from uniform distribution over \[0, 1)
        - E.g. random() in python
    - Step 2: Convert this sample *u* that lies in \[0,1) interval  into an outcome from the distribution that we want a sample from

---

C | P(C)
--- | --- 
red | 0.6
green | 0.1
blue | 0.3

---
 
 - Example 
    - 0 ≤ u ≤ 0.6, → C = red
    - 0.6 ≤ u ≤ 0.7, → C = green
    - 0.7 ≤ u ≤ 1 , → C = blue
    - If random() returns u = 0.83, then our sample is C = blue
    - E.g, after sampling 8 times:
        - 5 reds , 2 blues , 1 green 
        - so what's the probability of blue ?  2/8 = 0.25 , that's our estimate of the probability of blue give this set of samples. 

---

<h2 id="7bdab2b4b6b4f6a48cbf1e07f48c7f94"></h2>

## Sampling in Bayes’ Nets

 - Prior Sampling
 - Rejection Sampling
 - Likelihood Weighting
 - Gibbs Sampling

In the order from simple to complex. Often you want end up using those last 2. 

<h2 id="d9850ac369194d66ab390de368f1cf63"></h2>

## Prior Sampling 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_sampling_prior_sampling.png)

We have a BNs, and we want to generate samples of the full joint distribution ,but without building full joint distribution. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_sampling_prior_sampling_1st_sample.png)

 - ordering: C → S → R → W , or  C → R → S → W 
 - we start with the 1st variable in the ordering **C** 
    - we generate the number in \[0,1) , then map it to +c , or -c. 
    - this case , we got +c 
 - then we pick up next variable , this case *S* 
    - C is already sampled as +c, so we just consider the highlighted part of this table. 
    - again we generate a number, and map it into either +s , or -s
    - this case , we got -s
 - next we have to proceed with R 
    - we can not proceed W yet, because W depends on both S and R 
    - this case , we got +r 
 - Now we can sample W 
    - this case , we got +w 
    - this generated our first sample from this BNs.   +c,-s,+r,+w
 - repeat this process , and build up a set of samples from this BNs distribution here.   
 - algorithm to generate 1 sample : 

```
// single sample
For i=1,2,...,n
    Sample xᵢ from P(Xᵢ| Parents(Xᵢ))
return (x₁,x₂,...,xn)
```

---

 - Question: are we sampling from the correct distribution ?
 - This process generates samples with probability:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_PS_sampling_distribution.png)
    - S<sub>PS</sub> : sampling distribution *S* using prior sampling 
    - i.e. the BN’s joint probability
 - Let the number of samples of an event be
    - N<sub>PS</sub> (x₁,x₂,...,x<sub>n</sub>)
 - if the number of samples goes to infinity then the number of samples you get for a particular event divided by N will converge to the actual probability for that event.
    -  ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_sampling_prior_limit.png)
 - I.e., the sampling procedure is ***consistent***.

---

<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>

### Example 

 - We’ll get a bunch of samples from the BN: (let's say we ended up with following samples)
    - +c, -s, +r, +w
    - +c, +s, +r, +w
    - -c, +s, +r, -w
    - +c, -s, +r, +w
    - -c, -s, -r, +w
 - If we want to know P(W)
    - We have counts :   +w:4 , -w:1
    - Normalize to get P(W) = <+w:0.8, -w:0.2>
    - This will get closer to the true distribution with more samples
    - Can estimate anything else, too
    - What about P(C| +w)?   P(C| +r, +w)?  P(C| -r, -w)?
        - P(+c|+w) = 3/4 , P(-c|+w) = 1/4
        - P(+c|+r,+w) = 1
        - P(-c|-r,-w) : not computable from the samples we have.  
    - Fast: can use fewer samples if less time 
        - what’s the drawback?  the accuracy of course. 

---

<h2 id="da3112458f911630996b5661ccd81e9d"></h2>

## Rejection Sampling 

Now we're going to look at a way to speed this up a little bit if we know ahead of time what the queries that were asked.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_sampling_reject_sampling.png)

 - Let’s say we want P(C)
    - No point keeping all samples around
    - Just tally counts of C as we go
        - we know we sampled top down through BNs, so we know once we sampled C and if later all interesting is counting how often we have +c/-c 
        - there's no need to still sample S,R and W. 
        - we just stop sampling after we got C. 
 - Let’s say we want P(C| +s)
    - Same thing: tally C outcomes, but ignore (reject) samples which don’t have S=+s
        - when you sampled -s , there is no point in continuing.
        - that sample is going to be going unused when you answer your query 
    - This is called rejection sampling
    - It is also consistent for conditional probabilities (i.e., correct in the limit)

```
// single sample 
IN: evidence instantiation
For i=1, 2, …, n
    Sample xᵢ from P(Xᵢ| Parents(Xᵢ))
    If xᵢ not consistent with evidence
        Reject: Return, and no sample is generated in this cycle
Return (x1, x2, …, xn)
```

---

### Sampling Example 

 - There are 2 cups
    - The frist contains 1 penny and 1 quarter
    - Then second contains 2 quaters
 - Say I pick a cup uniformly at random, then pick a coin randomly from that cup. It's a quarter ( yes!). 
    - What is the probability that the other coin in that cup is also a quarter ? 

 - One way to answer this question is to use essentially BNs inference to find the answer
 - another way to do it is to just run sampling : 2/3

---

## Likelihood Weighting

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_Sampling_LW.png)

Again, we know the query ahead of time, and see if we can further improve the procedure beyond what we did for a rejection sampling. 
 
 - Problem with rejection sampling:
    - If evidence is unlikely, rejects lots of samples
        - 证据发生的概率很低
    - Evidence not exploited as you sample
        - if the evidence variable are very deep in your BNs, you might have done all that work 
        - reach all the way to the bottom of you BNs, you sample your evidence variable , you sample it the wrong way , now you reject -- that sample can not use . 
    - Consider P(Shape|blue)
        - Shape → Color
            - ~~pyramid, green~~
            - ~~pyramid, red~~
            - sphere , blue
            - ~~cube, red~~
            - ~~sphere, green~~ 

 - Idea: fix evidence variables and sample the rest
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_Sampling_LW_fix_evidence.png)
    - Problem: sample distribution not consistent!
    - Solution: weight by probability of evidence given parents
        - you instantiated some shape to be blue, and the probability for blue was 0.2 for that shape 
        - you now weight that particular sample by a factor 0.2. 

### Example Likelihood Weighting

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_BNs_Sampling_LW_example.png)

 - evidence is +s , +w
 - we start with Cloudy , we got +c 
    - weight is 1.0
 - next we go to Sprinkler,  it is instantiated to be +s, we have weight P(+s|+c) = 0.1 
    - now weight is 1.0\*0.1 
 - next we look at rain, we sample , we got +r 
    - weight is still 1.0\*0.1  
 - last is WetGrass , it is instantiated to be +w , we weight it P(+w|+s,+r) = 0.99
    - now the weight is 1.0\*0.1\*0.99 = 0.099

## Likelihood Weighting Cont.

```
// single sample
IN: evidence instantiation
w = 1.0
for i=1, 2, …, n
    if Xᵢ is an evidence variable
        Xᵢ = observation xᵢ for X
        Set w = w * P(xᵢ | Parents(Xᵢ))
    else
        Sample xᵢ from P(Xᵢ | Parents(Xi))
Return (x1, x2, …, xn) , w
```

Are we still doing the right thing ?  Are we sampling from the right distribution ?

 - Proof:  ignore

---

 - Likelihood weighting is good
    - We have taken evidence into account as we generate the sample
        - E.g. here, W’s value will get picked based on the evidence values of S, R
    - More of our samples will reflect the state of the world suggested by the evidence
 - Likelihood weighting doesn’t solve all our problems
    - Evidence influences the choice of downstream variables, but not upstream ones (C isn’t more likely to get a value matching the evidence)
 - We would like to consider evidence when we sample every variable
    - -> Gibbs sampling

---











