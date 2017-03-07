
# Probability

In part 2 we will assume that the models are given to us.


demo: ghost busters

In this grid, somewhere is ghost who is hiding. We don't know where the ghost is but we know there is exactly 1. If we happen to measure on top of the ghost , we don't know that we measure on top of the ghost. All we get is a color back -- we get red, orange, yellow, or green back.   These 4 colors, how does show up depends probabilisticly on how close we to the ghost. 

On top of ghost, we usually get red, but we could get green. We don't know ahead of time.  It's a nosiy sense. 


---

When we deal with an uncertainty usually we can split the random variables into 2 groups. one group is the group of random variables that would get to observe. We get to measure them and usually then we want to do is somehow  in first something about the variables we don't get to measure -- the hidden variables , the unobserved variables -- and do that in some structured way. And the way that is structures using a probability model that tells us measurements related a noisy way to these hidden variables that we don't get to observe. 

## Random Variables

driving time could be continuous.

## Probability Distribution 

## Joint Distributions

The reason we care about joint distribution is because we want to infer things about variables we haven't observed based on observations we made of these observed variables. 

dⁿ


vs CSP

Sometimes the main different is that here you have true/false values saying whether it's allowed to have an association or not. 


## Marginal Distributions

corresponds to a sub-table of the original joint distribution  where you consider only a subset of the random variables.

## Conditional Distribution

P(W|T)  is a set of tables -- one table for each value T can take on and then for a fixed value of T you get a conditional distribution table.

Each of these individual tables sums to 1. 

## Normalization Trick

It's a way to go from joint distributions to conditional distributions and has slightly quicker way and also a little more mechanical. 

## To Normalize 

 All entries sum to 1. 


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












