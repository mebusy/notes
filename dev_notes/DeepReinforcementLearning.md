

# Deep Reinforcement Learning , John Schulmann


## What is Deep Reinforcement Learning

 - Reinforcement Learning using neural networks to approximate functions 
    - Policies ( select next action )
    - Value functions ( measure goodnees of states or state-action pairs )
    - Models ( predict next states and rewards )
 
## Recent Success Stories in Deep RL

 - ATARI using deep Q-learning , policy gradients, DAGGER
 - Superhuman Go using supervised learning + policy gradients + Monte Carlo tree search + value functions
 - Robotic mainpulation using guided policy search
 - Robotic locomotion using policy gradients 
 - 3D games using policy gradients

## Definition 

 - MDP
 - Extra objects defined depending on problem setting
    - μ: Initial state distribution
 - Optimization problem: maximize expected cumulative reward

## Episodic Setting

 - In each episode, the initial state is sampled from μ, and the agent acts until the terminal state is reached. For example:
    - Taxi robot reaches its destination ( termination == good )
    - Waiter robot finishes a shift( fixed time ) 完成班次
    - Walking robot falls over ( termination == bad )

## Policies

 - Deterministic policies: a = π(s)
 - Stochastic policies: a ~ π(a|s)
    - the policy is conditional probability distribution
 
## Parameterized Policies

 - A family of policies indexed by parameter vector θ ∈ ℝᵈ
    - Deterministic : a = π(s,θ)
    - Stochastic policies : π( a | s,θ)
 - Analogous to classification or regression with input s , output a 
    - Discrete action space: network outputs vector of probabilities.
    - Continuous action space: network outputs mean and diagonal covariance of Gaussian
 
## Policy Gradient Methods

 - Problem :  maximize E[R|π<sub>θ</sub>]
    - maximize the total reward , given our parameterize policy π<sub>θ</sub> 
    - R : the sum of rewards of the whole episode
 - Intuitions: collect a bunch of trajectories , and ...
    - 1. Make the good trajectories more probable
    - 2. Make the good action more probable
    - 3. Push the actions towards good action 

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

### Derivation via Importance Sampleing

 - Alternative Derivation using Important Sampling

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_alternative_derivative.png)

### Score Function Gradient Esitmator: Intuition

 - ĝi = f(xᵢ)∇<sub>θ</sub>log p(xᵢ|θ).
 - f(x) measures how good the sample x is
 - Moving in the direction `ĝi` pushes up the log prob of the sample, in proportion to how good it is.
 - Valid even if f(x) is discontinuous , and unknown, or sample space (containing x) is a discrete set.

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DRL_score_function_gradient_estimator_pic.png)

 - so we have our function f(x) which were trying to maximize the expectation of , and then we have our probability -- p(x). So we just sample a bunch of values from our probability density -- those are the blue dots on the X-axis -- , and then we will look at the function values and we're trying to push the probability distribution so that the probability goes up at these samples in proportion to the function value. I'm over on the right side of the curve , that means we're trying to push that probability value up really hard, and on the left side we're pushing it up softly. So what's gonna happen is the probability density is going to slide to the right. 


### Score Function Gradient Estimator for Policies 

 - Now random variable x is a whole trajectory 
    - τ = (s₀,a₀,r₀,s₁,r₁, ..., s<sub>T-1</sub> , a<sub>T-1</sub> , r<sub>T-1</sub> , S<sub>T</sub> )
    - ∇<sub>θ</sub> E<sub>τ</sub> [R(τ)] = E<sub>τ</sub> [ ∇<sub>θ</sub>log p(τ|θ)R(τ) ]




