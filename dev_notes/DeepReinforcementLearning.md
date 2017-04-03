...menustart

 - [Deep Reinforcement Learning , John Schulmann](#d5c6173d3b6d88effe999ae07dd5beb8)
	 - [What is Deep Reinforcement Learning](#840963d0a81ce0786ad65c4b03593d61)
	 - [Recent Success Stories in Deep RL](#86c7ba878799d234801a66038964c52a)
	 - [Definition](#0b890b1926b90387673882e6ccae7fdc)
	 - [Episodic Setting](#1d8d53c83c2d8cdd5b1c1e78c9da81f7)
	 - [Policies](#9e476387322a5c250893cf9c5c4ce78c)
	 - [Parameterized Policies](#b9bd77fcb34a314520a72c4b51503292)
	 - [Policy Gradient Methods](#e57fb87359a70504aa07e0f9c7db900b)
	 - [Score Function Gradient Esitmator](#c9f2f78ca7d465a24b65f3eca5eebe50)
		 - [Derivation via Importance Sampleing](#a21ad88ba863b86c9d1030d7cede5633)
		 - [Score Function Gradient Esitmator: Intuition](#3da8e19404ac159adb135368bfa5bbe2)
		 - [Score Function Gradient Estimator for Policies](#8688cd6001e825b099c69f523ababd09)
	 - [Policy Gradient: Use Temporal Structure](#df26dcf846140671f2ed1c479db2b90e)

...menuend


<h2 id="d5c6173d3b6d88effe999ae07dd5beb8"></h2>

# Deep Reinforcement Learning , John Schulmann


<h2 id="840963d0a81ce0786ad65c4b03593d61"></h2>

## What is Deep Reinforcement Learning

 - Reinforcement Learning using neural networks to approximate functions 
    - Policies ( select next action )
    - Value functions ( measure goodnees of states or state-action pairs )
    - Models ( predict next states and rewards )
 
<h2 id="86c7ba878799d234801a66038964c52a"></h2>

## Recent Success Stories in Deep RL

 - ATARI using deep Q-learning , policy gradients, DAGGER
 - Superhuman Go using supervised learning + policy gradients + Monte Carlo tree search + value functions
 - Robotic mainpulation using guided policy search
 - Robotic locomotion using policy gradients 
 - 3D games using policy gradients

<h2 id="0b890b1926b90387673882e6ccae7fdc"></h2>

## Definition 

 - MDP
 - Extra objects defined depending on problem setting
    - μ: Initial state distribution
 - Optimization problem: maximize expected cumulative reward

<h2 id="1d8d53c83c2d8cdd5b1c1e78c9da81f7"></h2>

## Episodic Setting

 - In each episode, the initial state is sampled from μ, and the agent acts until the terminal state is reached. For example:
    - Taxi robot reaches its destination ( termination == good )
    - Waiter robot finishes a shift( fixed time ) 完成班次
    - Walking robot falls over ( termination == bad )

<h2 id="9e476387322a5c250893cf9c5c4ce78c"></h2>

## Policies

 - Deterministic policies: a = π(s)
 - Stochastic policies: a ~ π(a|s)
    - the policy is conditional probability distribution
 
<h2 id="b9bd77fcb34a314520a72c4b51503292"></h2>

## Parameterized Policies

 - A family of policies indexed by parameter vector θ ∈ ℝᵈ
    - Deterministic : a = π(s,θ)
    - Stochastic policies : π( a | s,θ)
 - Analogous to classification or regression with input s , output a 
    - Discrete action space: network outputs vector of probabilities.
    - Continuous action space: network outputs mean and diagonal covariance of Gaussian
 
<h2 id="e57fb87359a70504aa07e0f9c7db900b"></h2>

## Policy Gradient Methods

 - Problem :  maximize E[R|π<sub>θ</sub>]
    - maximize the total reward , given our parameterize policy π<sub>θ</sub> 
    - R : the sum of rewards of the whole episode
 - Intuitions: collect a bunch of trajectories , and ...
    - 1. Make the good trajectories more probable
    - 2. Make the good action more probable
    - 3. Push the actions towards good action 

<h2 id="c9f2f78ca7d465a24b65f3eca5eebe50"></h2>

## Score Function Gradient Esitmator 

 - Consider an expectation E<sub>x~p(x|θ)</sub>[ f(x) ].  Want to compute gradient wrt(with respect to) θ
    - we're not going to talk about policies in RL at all ,  we're just assume we have some expectation of f(x). where :
    - x is sampled from some parameterized probability distribution.
 - so we want to compute the gradient of this expectation with respect to θ
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_gradient_estimator.png)
    - so we just write the expectation as an integral and then you just move some things around, you swap the integral with the derivative , and you turn it back into an expectation and what you get at the end is this bottom line , which says:
    - you take the expectation of f(x) times grad log probability.
 - Last expression gives us an unbiased gradient estimator. Just sample xᵢ ~ p(x|θ) , and compute ĝi = f(xᵢ)∇<sub>θ</sub>log p(xᵢ|θ).
 - Need to be able to compute and differentiate density p(x|θ) wrt θ.

<h2 id="a21ad88ba863b86c9d1030d7cede5633"></h2>

### Derivation via Importance Sampleing

 - Alternative Derivation using Important Sampling

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_alternative_derivative.png)

<h2 id="3da8e19404ac159adb135368bfa5bbe2"></h2>

### Score Function Gradient Esitmator: Intuition

 - ĝi = f(xᵢ)∇<sub>θ</sub>log p(xᵢ|θ).
 - f(x) measures how good the sample x is
 - Moving in the direction `ĝi` pushes up the log prob of the sample, in proportion to how good it is.
 - Valid even if f(x) is discontinuous , and unknown, or sample space (containing x) is a discrete set.

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_gradient_estimator_pic.png)

 - so we have our function f(x) which were trying to maximize the expectation of , and then we have our probability -- p(x). So we just sample a bunch of values from our probability density -- those are the blue dots on the X-axis -- , and then we will look at the function values and we're trying to push the probability distribution so that the probability goes up at these samples in proportion to the function value. I'm over on the right side of the curve , that means we're trying to push that probability value up really hard, and on the left side we're pushing it up softly. So what's gonna happen is the probability density is going to slide to the right. 


<h2 id="8688cd6001e825b099c69f523ababd09"></h2>

### Score Function Gradient Estimator for Policies 

 - Now random variable x is a whole trajectory 
    - τ = (s₀,a₀,r₀,s₁,r₁, ..., s<sub>T-1</sub> , a<sub>T-1</sub> , r<sub>T-1</sub> , S<sub>T</sub> )
    - ∇<sub>θ</sub> E<sub>τ</sub> [R(τ)] = E<sub>τ</sub> [ ∇<sub>θ</sub>log p(τ|θ)R(τ) ] 
 - Just need to write out p(τ|θ)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_gradient_estimator_for_policy.png)
 - Interpretation: using good trajectories (high R) as supervised examples in classification/regression

<h2 id="df26dcf846140671f2ed1c479db2b90e"></h2>

## Policy Gradient: Use Temporal Structure

 



