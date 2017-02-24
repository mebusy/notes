
# Reinforcement Learning I

The basic idea is you have an agent who's acting as always. The agent has actions available to it and choose an action. The environment then does what it always does which is it resolves in some way that's not entirely determined by the action. 

When the action is resolved what the agent receive back is 2 things: one is the reward , the other things is a percept -- we get a state back in the simplest formulation.

For now we take an action which we essentially submit to the environment by doing it and the environment returns to us a state which is the result and a reward which we want to maximize.   

We want to act ot maximize our rewards but we have to learn to do that because in this setting we won't know what actions will produce rewards until we try them. 

Because we're actually trying things in the environment ,all of the learning ,all of the ways we have available to us to make decision, are mediated by what we experience -- which are samples of outcomes.  

When you take an action you see what happens but you don't see everything that might have happended.  


## Reinforcement Learning

We don't know the transition function , we don't know the rewards , that is even though based on my state in my action there's certain set of outcomes with a certain probability distribution , I don't know which probability and distribution it is. The only way we really know  what our actions do and where the rewards come from , is to try things out and then learn from our samples that we experience. 

Of course because we're trying things out from a state of partial information , we're gonna make some mistakes and so there is always going to be this process of trying things out not all of which work optimally. 

-- race car example

You still know whether you'er cool , warmer, overheated, and you still know that you can move faster or slow. What you don't know is what fast and slow do. So for all you know fast is the best idea ever or is the best idea ever , you try some things maybe you end up going too slow or maybe you overheat. And you have to try things again and slowly learn what these actions do from each state. 


## Offline (MDPs) vs. Online (RL)

Offline solution is when you know what your actions will do and in computation in simulation in your head you think about consequences , you realize the jumping into the pit is a bad idea because you know it has negative reward. so you never actually do it. 

When you do online learning , you have to actually jump into the pit before you know it is bad. you might imagine that over time this increases the cost of the robots. 

## Model-Based Learning

The question is how are we going to be able to learn how to act when we don't know what the actions do or what rewards will get. 

You might think we can just reduce this to what we had before -- we can somehow still use value iteration and expectimax. That's true. What we're gonna talk about now is model-based learning. 

In model-based learning we reduce the reinforcement learning problem to the previous case of a know MDP. 

So how do we do that ? 

Whan we try to build a model we try to figure out what the transitions and rewards do , and then pretend that's the truth. 
 
 - Model-based Idea:
    - Learn an approximate ...


So first step is to learn some MDP that we can use to run things like value iteraction. How can we do that ?  We're going to at times find youself in certain state *s* and take certain action *a* -- let's not worry for now about how we decide what action to take. Whenever we're in state *s* and we take action *a* , various things happen. So we end up with various s' outcomes.

Overtime we count them up -- some of them happen more and some of them happen less. When we take those counts and normalize them we get probabilities. That is our estimate of the transition function for (s,a).  We do that for all (state , action)  pairs. In addition we discover the rewards that are associated with (s,a) and s' whenever we experience that transition.  

So we're going to act for a while , we're gonna accumulate counts of various things , we're gonna turn them into probabilities. Once that's all done we have a transition function T and a rewards function R. They're probably not correct but they are structurally what we need to run things like value iteration. So we learned a MDP. And then we solve it.

Now there are a lot of small points here that are very important like how do you know how to act , how do you know how many counts you need , how do you know how close you're gonna be. We're not going to get very much into those details now , we'll come back to the idea of how to learn a good model. 

### Example : Model-Based Learning 

Let's say we're in a grid world , and somebody gives us this policy π and so we're going to be following this policy. I'm trying to find out how we know how to act. 

We're going to look at this policy and say 'alright we're going to do this'. We image our γ is 1 so there is no discount to make this example simple. and we have some experiences. 

-- pic Episode 1...

4 times playing this game

for example in episode 1, we started B , we go east to C , we go east to D, and we take exit action we transition to the terminal state where the game is over , and we receive a big reward +10. In this particular case you should get a -1 living reward and +10 good exit reward. 

So those 4 episode is what we've got to work with. 

In a model-based setting what we do with all of this experience which is not everythings that could happen -- it's just what we personally have seen. What we do with this experience as we try to figure out what the transitions must be. 

So we think alright I've been in B, I've taken the action EAST , and what's happended ? So fa a 100 percent of time we've ended up C. So I'll write down. To the best of my knowledge right now -- and will be improved on future -- let's just say that east EAST from B has a 100% chance of resulting in C. That's a transition function. 

Similarly EAST from C we know that 3/4 of the time it actually went EAST into D but 1/4 time it went NORTH to A. Are those the right probabilities? Almost surely not. But they are reasonable starting point for this simplistic version. 

So what comes out ? We've learned now a model where we have transitions and reward functions. 

-- pic T, R

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

## Exponential Moving Average 

























 



 
 

# Reinforcement Learning II
