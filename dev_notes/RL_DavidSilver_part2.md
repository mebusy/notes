...menustart

 - [RL David Silver , Part II](#642eadc816039c29a67ef129a6a090f6)
 - [Lecture 6:](#ecbcb5fe84f115baf7815f06a0042e1c)
	 - [Value Function Approximation](#d9bb6b898523b2ea131950f5ec3fc308)
	 - [Types of Value Function Approximation](#c6856fb88cde30004a30618776062a49)
	 - [Value Function Approx. By Stochastic Gradient Descent](#2a8b356b7c497a4fa82537430889ff7c)
	 - [TD(λ) with Value Function Approximation](#174cd9c9b503392d64f89edef582c758)

...menuend


<h2 id="642eadc816039c29a67ef129a6a090f6"></h2>

# RL David Silver , Part II

<h2 id="ecbcb5fe84f115baf7815f06a0042e1c"></h2>

# Lecture 6: 

<h2 id="d9bb6b898523b2ea131950f5ec3fc308"></h2>

## Value Function Approximation


<h2 id="c6856fb88cde30004a30618776062a49"></h2>

## Types of Value Function Approximation


 - for q(s,a,w) , you feature should be extracted from both state , action
    - eg. self.featExtractor.getFeatures(state, action )

 - 第二张图 action-in
 - 第三张图 action-out
    - Atari game ?

<h2 id="2a8b356b7c497a4fa82537430889ff7c"></h2>

## Value Function Approx. By Stochastic Gradient Descent

<h2 id="174cd9c9b503392d64f89edef582c758"></h2>

## TD(λ) with Value Function Approximation

 - When you useing Function Approximation , the size of eligibility traces is on the size of you parameters ?
    - it record all the features you have seen so far.

### Linear Action-Value Function Approximation

we might have 1 feature ,x₁, say how far am I far from the wall if I moving forwards. And I have another feature , x₂ , says how far am I far from this wall if I'm moving backwards. 







