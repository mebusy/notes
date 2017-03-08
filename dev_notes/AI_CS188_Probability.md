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

In this grid, somewhere is ghost who is hiding. We don't know where the ghost is but we know there is exactly 1. If we happen to measure on top of the ghost , we don't know that we measure on top of the ghost. All we get is a color back -- we get red, orange, yellow, or green back.   These 4 colors, how does show up depends probabilisticly on how close we to the ghost. 

On top of ghost, we usually get red, but we could get green. We don't know ahead of time.  It's a nosiy sense. 


---

When we deal with an uncertainty usually we can split the random variables into 2 groups. one group is the group of random variables that would get to observe. We get to measure them and usually then we want to do is somehow  in first something about the variables we don't get to measure -- the hidden variables , the unobserved variables -- and do that in some structured way. And the way that is structures using a probability model that tells us measurements related a noisy way to these hidden variables that we don't get to observe. 

<h2 id="8a93f7814e04aeb4a3435d0667b581d7"></h2>
## Random Variables

driving time could be continuous.

<h2 id="65b393733707f82733184765aa503081"></h2>
## Probability Distribution 

<h2 id="7d5c8826b9086639339acd137cdef0cc"></h2>
## Joint Distributions

The reason we care about joint distribution is because we want to infer things about variables we haven't observed based on observations we made of these observed variables. 

dⁿ


vs CSP

Sometimes the main different is that here you have true/false values saying whether it's allowed to have an association or not. 


<h2 id="34b3d41097573990cabbad8ae1d9c969"></h2>
## Marginal Distributions

corresponds to a sub-table of the original joint distribution  where you consider only a subset of the random variables.

<h2 id="d22ece9f9682b018dfb17860cc5aedd7"></h2>
## Conditional Distribution

P(W|T)  is a set of tables -- one table for each value T can take on and then for a fixed value of T you get a conditional distribution table.

Each of these individual tables sums to 1. 

<h2 id="1a18f3ea65669c3a4a2a7eff540de62e"></h2>
## Normalization Trick

It's a way to go from joint distributions to conditional distributions and has slightly quicker way and also a little more mechanical. 

<h2 id="730a75b3c3a77c4efa7e801fc1f306ea"></h2>
## To Normalize 

 All entries sum to 1. 


<h2 id="314fa4378b3b188832e3f68fd46ac015"></h2>
## Inference by Enumeration

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












