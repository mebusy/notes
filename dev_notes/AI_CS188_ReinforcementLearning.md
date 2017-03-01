
# Reinforcement Learning I

The basic idea is you have an agent who's acting as always. The agent has actions available to it and choose an action. The environment then does what it always does which is it resolves in some way that's not entirely determined by the action. 

When the action is resolved what the agent receive back is 2 things: one is the reward , the other things is a percept -- we get a state back in the simplest formulation.

For now we take an action which we essentially submit to the environment by doing it and the environment returns to us a state which is the result and a reward which we want to maximize.   

We want to act ot maximize our rewards but we have to learn to do that , because in this setting we won't know what actions will produce rewards until we try them. 

Because we're actually trying things in the environment ,all of the learning  all of the ways we have available to us  to make decision, are mediated by what we experience -- which are samples of outcomes.  

When you take an action you see what happens but you don't see everything that might have happended.  


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_rl_1.png)


 - Basic idea:
    - Receive feedback in the form of ***rewards***
    - Agent’s utility is defined by the reward function
    - Must (learn to) act so as to ***maximize expected rewards***
    - All learning is based on observed samples of outcomes!
 

    


## Reinforcement Learning

We don't know the transition function , we don't know the rewards , that is even though based on my state in my action there's certain set of outcomes with a certain probability distribution , I don't know which probability and distribution it is. The only way we really know  what our actions do and where the rewards come from , is to try things out and then learn from our samples that we experience. 

Of course because we're trying things out from a state of partial information , we're gonna make some mistakes and so there is always going to be this process of trying things out not all of which work optimally. 

For the race car example -- you still know whether you'er cool , warmer, overheated, and you still know that you can move faster or slow. 

What you don't know is what fast and slow do. So far all you know fast is the best idea ever or slow is the best idea ever.  You try some things maybe you end up going too slow or maybe you overheat. And you have to try things again and slowly learn what these actions do from each state. 

 - Still assume a Markov decision process (MDP):
    - A set of states s ∈ S
    - A set of actions (per state) A
    - A model T(s,a,s’)
    - A reward function R(s,a,s’)
 - Still looking for a policy π(s)
 - New twist: ***don’t know T or R***
    - I.e. we don’t know which states are good or what the actions do
    - Must actually try actions and states out to learn
    

## Offline (MDPs) vs. Online (RL)

 - Offline Solution
    - Offline solution is when you know what your actions will do and in computation in simulation in your head you think about consequences , you realize the jumping into the pit is a bad idea because you know it has negative reward. so you never actually do it. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_rl_online_solution.png)
 - Online Learning
    - When you do online learning , you have to actually jump into the pit before you know it is bad. you might imagine that over time this increases the cost of the robots. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_rl_online_learning.png)


## Model-Based Learning

The question is how are we going to be able to learn how to act when we don't know what the actions do or what rewards will get. 

You might think we can just reduce this to what we had before -- we can somehow still use value iteration and expectimax. That's true. What we're gonna talk about now is model-based learning. 

In model-based learning we reduce the reinforcement learning problem to the previous case of a know MDP. 

So how do we do that ? 

When we try to build a model we try to figure out what the transitions and rewards do , and then pretend that's the truth. 
 
 - Model-based Idea:
    - Learn an approximate model based on experiences
    - Solve for values as if the learned model were correct


So first step is to learn some MDP that we can use to run things like value iteraction. How can we do that ?  We're going to at times find youself in certain state *s* and take certain action *a* -- let's not worry for now about how we decide what action to take. Whenever we're in state *s* and we take action *a* , various things happen. So we end up with various s' outcomes.

Overtime we count them up -- some of them happen more and some of them happen less. When we take those counts and normalize them we get probabilities. That is our estimate of the transition function for (s,a).  We do that for all (state , action)  pairs. In addition we discover the rewards that are associated with (s,a) and s' whenever we experience that transition.  

So we're going to act for a while , we're gonna accumulate counts of various things , we're gonna turn them into probabilities. Once that's all done we have a transition function T and a rewards function R. They're probably not correct but they are structurally what we need to run things like value iteration. So we learned a MDP. And then we solve it.

 - Step 1: Learn empirical MDP model
    - Count outcomes s' for each s, a
    - Normalize to give an estimate of T̂(s,a,s')
    - Discover each  R̂(s,a,s') when we experience (s, a, s')
 - Step 2: Solve the learned MDP
    - For example, use value iteration, as before



Now there are a lot of small points here that are very important like how do you know how to act , how do you know how many counts you need , how do you know how close you're gonna be. We're not going to get very much into those details now , we'll come back to the idea of how to learn a good model. 

### Example : Model-Based Learning 

 - Input Policy π , Assume: λ = 1
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_rl_grid_input_policy.png)
 - Observed Episodes (Training) , and  Learned Model
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_rl_grid_learnedmodel.png)
  

Let's say we're in a grid world , and somebody gives us this policy π and so we're going to be following this policy. I'm trying to find out how we know how to act. 

We're going to look at this policy and say 'alright we're going to do this'. We image our γ is 1 so there is no discount to make this example simple. and we have some experiences. 


4 times playing this game

for example in episode 1, we started B , we go east to C , we go east to D, and we take exit action we transition to the terminal state where the game is over , and we receive a big reward +10. In this particular case you should get a -1 living reward and +10 good exit reward. 

So those 4 episode is what we've got to work with. 

In a model-based setting what we do with all of this experience which is not everythings that could happen -- it's just what we personally have seen. What we do with this experience as we try to figure out what the transitions must be. 

So we think alright I've been in B, I've taken the action EAST , and what's happended ? So fa a 100 percent of time we've ended up C. So I'll write down. To the best of my knowledge right now -- and will be improved on future -- let's just say that east EAST from B has a 100% chance of resulting in C. That's a transition function. 

Similarly EAST from C we know that 3/4 of the time it actually went EAST into D but 1/4 time it went NORTH to A. Are those the right probabilities? Almost surely not. But they are reasonable starting point for this simplistic version. 

So what comes out ? We've learned now a model where we have transitions and reward functions. 

see  T, R in the picture.

Of course we've only learned about the things we've actually. But let's set that aside until later. 

Now we have a MDP,  maybe a wrong  MDP  , but we still know how to solve it.

---

### Example: Expected Age 

My goal was to compute the average age of people in cs188 class. So I want to compute the expected age -- the weighted average. How would I do that. We all know how to compute expectations. For example if I know the probability distribution over ages -- how many people are each age -- then I would have a straight forward way of computing this weighted average. The way I do that is I say "well , the expectation of this random variable A , I sum over all of the possible ages weighted by its probability". Easy ! In fact this kind of expectation  is all really going on in these MDPs. 

Now what happens if we don't know the distribution. We're forced to rely on samples. We could take a few samples ,we could take a lot of samples. Obviously the more samples the more accurate these things will be.  We're going to collect samples instead of the probability distribution. 

The model-based view is  I don't know the distribution over ages but I've got samples. What do I do with the samples?  The model-based view is I use the samples to reconstruct an approximation of what I didn't know -- the empirical distrubtion over ages. Now I reduced it to the case of the known distribution and I compute the expectations. 

Why does this model-based thing work ? The reason it works is because eventually you learn the right model. 

There's something else you can do with the samples rather than trying to reconstruct the probability distribution. What could we do? 

We could do what is called "model-free" approaches here. We average the samples directly giving each sample equal weight. When I do this model-free stuff the averages are unweighted. Why does that work ? Because samples appear with the right frequencies -- ages are more frequent show up in more samples. 

This is the high level view of model-based vs model-free. In model-based you learn the probability distributions and then you reduce it the case of solving a known MDP. In model-free case we just take our sample as they come and average them together. 

 - Goal: Compute expected age of cs188 students
    - Known P(A) : E[A] =  ∑ₐ P(a)·a
    - Unknown P(A): instead collect samples [a₁, a₂, … a<sub>n</sub>]
        - Model Based
            - P̂(a) = num(a)/N
            - E[A] ≈  ∑ₐ P̂(a)·a  
        - Model Free
            - E[A] ≈ 1/N·∑ᵢ aᵢ 

## Model-Free Learning

In model-free learning we don't construct a model of the transition function. What we do is we take actions , and every time we take an action we compare what we thought was going to happen to what actually did happen. Whenever something is better or worse than what we expected we adjust our values up and down. 

So what we track in a model-free approach is the values of interest themselves , not the transition functins and the rewards.  


## Passive Reinforcement Learning 

The idea is things are happening in the real world , some agent is taking actions and getting specific outcomes that are partially determined by chance. You have to learn from there samples you observe but you don't control the actions. Someone else is choosing the actions and you're just sitting there with your notebook trying to figure out based on the policy that is being followed what are the values of all the states. 

You can think about this here is this agent it's watching real things happen. It can't rewind and try something else. The things are not in the agent's control and it is just monitoring. 

So the task we're going to think about int the passive case is this simplified task we're not going to try to figure out how to act optimally , we're going to try to figure out essentially exactly what policy evaluation did. The input is a fixed policy. In previous example the agent is just watching some other execute this policy. but in any case it's a fixed policy. The agent does no know the transitions and the rewards. Our goal is to learn the state values. Of course because we're watching this policy π execute we're going to learn the values under the policy π. If π is really bad we're probably going to learn values that are also really bad. 

This is policy evaluation. We're watching or executing a fixed policy and we're trying to figure out how good each state is under that policy execution. In this case the learner is along for the ride. It doesn't get to actually control things even if it's already learned they're bad.  We have no choice about the actions , we're just executing the policy. It's still not offline planning. 

## Direct Evaluation

The simplest way you could imagine doing model-free is what's called ***direct evaluation***.

The idea of direct evaluation is super simple. All we're gonna do is watch action unfold. We're going to act according to π and every time we visit a state we're going to write down what the sum of discounted rewards the utility turned out to be in the end. In acting we will have been in many states , and for each one we might have been there many times , we're just going to record what happend, not in one step but all the way to the end. When we average those samples together , that will be an average achieved score for that state --that is the value. If we do it long enough we'll get the right answer. It's called direct evaluation. 


### Example: Direct Evaluation 

Remember: this is passive reinforcement learning. We're only doing policy evaluation. 

We're going to get traning episodes again and we're going to execute them one by one. 

Episode 1:

I've been B. I know something about B. What utility did I receive from B ?  Not -1 , that was the instantaneous one-step reward. According to π and according to this episode , from B I received a total of +8. 

Episode 2:  same as 1

Episode 3: +8 from E 

Episode 4: -12 from E

---

What we learned here?  Will this process work in the end ?  Sure. We're going to execute over and over and over from every state will eventually learn that some of states are good and some of the states are bad. Eventually they'll all be right. Because each state will eventually have a bunch of executions and the averages are work out in the end. 

But at least for now we've learned something that's slightly insane. Why is that ?  What do we know E from our experience? What happens when you follow this policy from E ? You go to C EVERY TIME. What score you from E ? -2.  What score you get from C ? 4.  Umm, something doesn't compute here. How can E be bad but the state it leads to every time be reasonably good ? Similarly B looks really good , but it always leads to C which looks kind of mediocre. 

So somehow even though this is going to work in the limit , we've thrown out a huge amount of information about how the states are connected together. 

## Problems with Direct Evaluation 

...

They are not optimal values , they are values for the policy being executed ,  it does the right thing in the end.

Bad:

We waste information about how the states connect up to each other. If we know the state is good and we know another state leads to it , that state should be good as well. Because we're learning each state separately , we're failing to exploit information across episodes. 

## Why Not Use Policy Evaluation ?

...

We already know how to take averages without knowing the weights. We look at samples of the things we're average and we add up those samples with equal weight.  How can we turn that into an algorithm ?

## Sample-Based Policy Evaluation ?

... 


What's wrong ?

You can't get your second sample until you're back in state *s*. How do you get back to *s* ? You don't know. You don't know what's going on. This is reinforcement learning you don't even know what your actions do. How can you get back to state *s* ? You can not do this. Maybe someday you'll be *s* again but you can't just keep executing the same action from same state. Maybe if you could rewind time you could do it , but you can not. 

So what do we need to do ? We need somehow be satisfied with the one-sample we get because once we get that sample we're often some other state and who knows if we'll ever be back to state *s*. 

So that a big idea of --

## Temporal Difference Learning 

...

It is a little tricky because we only get one sample of what might have happended , so we need somehow make sure that over time we accumulate the right averages. But right now we've got one sample we've got ot incorporate it and move on. 

The reason this is called temporal difference learning is because we compare our current estimate of a value with what we actually see. 

We've doing temporal difference learning right now of values. So the policy is still going to be fixed. We're still evaluating this policy. We're still not worrying about how to choose actions that will come later. The idea is we're going to move the values towards whatever we actually see happen. It's gonna be some kind of running average but we got to be careful. 

So here's the idea. We imagine we were at state s . Before we took any action we had some estimate of how good it was that encapsulates all of our knowledge to date. So we've got some estimate V(s) -- it's not correct , it's an approximation.  From *s* we take an action -- in this case we do π tells us -- and we land in some particular sample outcomes s'. So we get one of the many possible outcomes .   We get the reward associated with it -- R, and then we get put in a state s' for which we have an estimated future utility from s'. 

So on one hand we think we're going to get V(s) that's what our past experience has told us , on the other hand this particular time it looks like we're on track to get this sample. It looks like we're on track to get the instantaneous reward  + V<sup>π</sup>(s'). So we've got our old experiences all summarized in our value but then we have this new experience we need to incorporate which includes a real-world reward R and then an approximation that's been discoutned into the future.  

So how do we take the average of one thing ?   -- see 公式  "Update to V(s)"

One thing we do is we keep around our old value with some weight and we average in the new thing with some weight. So we interpolate them. There's some value α called learning rate. α is usually small , like 0.1 or something like that , maybe even smaller. Every time we get a sample of the new value which is a reward + discounted future , we average it in by interpolating it with the old value esitmate . 

Why do we use α ? Why don't we keep track of every experience we've ever had ?  If we really really want an even average that would be a way to achieve it. It turns out this is not only easier but it's in fact better. 

Same Update:

this update it says take your value and add to it α times the difference between what you thought would happen and what actually did. You can think of that as an error. And this says whenever you see an error in your estimates adjust your estimate in the direction of the error by some small step size α. 


Demo:

We are about to do temporal different learning of values. That means we keep a big table of values and they also offer 0 because we have no idea what's going on in this grid. 

The blue dot represens the agent. I'm going to issue commands and the agent will then watch what happends.

I went north. In this version the living reward set to 0 so that we can see how the exit rewards propagate. In this case no update happened because I thought that I was going to receive a total utility of 0 from the start state. I in fact received 0 and I landed in the state where I thought there was 0 left to come. 

So I thought I was going to get a 0 . I do seem to be on track to get 0 , nothing to do. 

Nothing interesting happens util I receive a non-zero reward which I receive no when I enter this right-top square but when I exit it. Right now I think I'm going to get a 0 total future score.  When I tack the exit action I will in fact receive a +1 and then I'll be forced to reconcile the +1 I got with the 0 I thought I was going to get and right now it was set to 0.5 and so the average value will now be 0.5 , and I update my array. 


I play again. What happens when I move into the square left to top-right square ? From here I'm about to move east I think I'm going to get a total score of 0. I go east. What did I receive that time step ? 0 . But I landed in the state that looks right now to be worth 0.5. On one hand I thought my total would be 0 , on the other hand this experience says I'm going to get 0 + 0.5 . I average them and I get 0.25.  That's going to continue happening as I exit here that 0.5 approaches 1 because I'm gonna get 1 every time . I is now (0.5+1) /2 = 0.75.

Play again, the values would be  (0+0.25)/2 = 0.13 ,  ( 0.25 + 0.75 ) /2 = 0.5 , ( 0.75+1)/2 = 0.88.

Every time we enter a non-zero square from a 0-value square, notice that we learn about the square we leave because when I leave this square I'm going to learn that my estimate of 0 isn't the best I can do. I can do better.  

So you learn about the state you leave , not the state you land in. 

I'm learning the values of these squares and the values under the policy that I'm executing. What would happen if I went the other way around ? ( move right from 0.13)

When I get to the square down to 0.98 and I go north , even I've never been in the state before and this is my first experience with it as soon as I see that going north lands me at 0.98 , I know that going north is pretty good and so I have an update (0 -> 0.49). That's exactly the effect the direct evaluation didn't have. 



## Exponential Moving Average 

## Problems with TD Value Learning 

TD value learning is not going to work for the general problem of active reinforcement learning where we want to not only evaluate but also choose actions . Why is that? Well let's imagine we run this thing and we've got this big table of state values. For every state I can tell you according the policy we've been running it's worth 7.0 in total and so on. The problem is if we want to turn those values into a policy and in particular will want to turn them into a new policy which is hopefully better than the old policy. Now we're sunk. We know how to produce a policy from values but it involves one step of expectimax. We would say the policy is whatever action achieved the largest Q value for that state. But of course those Q values involve an average of their outcomes and we can't do that because again we don't have T & R. 

The idea here is that if we want to be able to do action selection as well we sould be learning not just the values as we have been but the Q values. In fact this is why we even have a notion of Q values because they're critical for choosing action as in reinforcement learning. 

This idea of learning Q values make action selection model-free as well because we just look at the Q values and choose whichever one is best. 

## Active Reinforcement Learning 

ARL  You have to try things. Sometimes when you try something bad you get a negative reward and you keep on going. You probably won't try that thing again but you paid the price. 

In full reinforcement learning we would like to be able to compute optimal policies like value iteration did. Of course we're gonna make mistakes along the way that's going to a notion ,that we'll talk about later, called regret.  But we'd like to eventually learn the optimal thing.   

---

trade-off :  of doing things that are known to be pretty good  versus learning about things like what happens when I jump off the cliff. 


## Detour: Q-Value Iteration


...

We can't do this update with samples because it's not an average but Max. And the only thing we can do with samples is computing averages of things. 

...

Q-Values

discount of future value. I might be tempted to write (s') here , but I'm not learning values , I'm learning Q values. So I need to do 1 more layer. What is the value ? The value of the state is just the maximum of all the Q values going out of that states -- I have to maximize over all of the actions that I could take from that state.

The max is still there , the average is still there.  But this equation is an average and therefore this equation we can do with samples. 


---

## Q-Learning

Q-Learning is the key algorithm that allows us to do a lot of great things with reinforcement learning. 

Learn

Every time we're in a state *s* , we take some action *a*. When we dothat we're going to learning something about how good (s,a) is. So what we're going to maintain a table that looks something like this. 

For every state and every action , it's going to maintain a number which is the q-value approximation. 

We're going to get some sample on the basis of the action we picked , the key learning algorithm doesn't actually care how the action was chosen , it does the same update no matter how it was chosen.   We get a sample -- we were in *s* we choose action *a* -- we are going to learn something about Q of (s,a) -- that is how good is that action from the state.  We landed in s' this time and we received a reward *r* . 

Demo:

every square on the bottom is bad , and the exit on the right is good. 

## Q-Learning Properties 

















 



 
 

# Reinforcement Learning II






