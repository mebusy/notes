...menustart

 - [Hidden Markov Model](#70359ede2a47ed4a3c8ca9b6521d7629)
	 - [Markov Models](#d656a155bed68a7dec83cd56ff973bbc)
		 - [Conditional Independence](#0f1513d04ac32269de73d0f17465488e)
	 - [Hidden Markov Models](#94d2b6fed9dd768fe2edec7e6c85546f)
		 - [Example : Weather HMM](#c7624bc33d3af36dde93578541120635)

...menuend


<h2 id="70359ede2a47ed4a3c8ca9b6521d7629"></h2>

# Hidden Markov Model 

This pacman can eat ghost but first he has to find them. So soon as pacman start moving , you will see in the bottom colord numbers , which are kind of noisy readings of how far the ghosts are. 

Now let's say I want to eat the orange ghost. If you could somehow take these numbers over time and combine them with your model of how the world works --  means where are the walls, where are the maze -- and also your model of how the ghosts move , and figure out where they are. 


<h2 id="d656a155bed68a7dec83cd56ff973bbc"></h2>

## Markov Models

 - A **Markov Model** is a chain-structured Bayes' net (BN)
    - Each node is identically distributed (stationarity)
    - Value of X at a given time is called the **state**
    - As a Bayes' net
        - P(X₁)
        - P(X<sub>t</sub> | X<sub>t-1</sub>)
    - Parameters: called **transition probability** or dynamics, specify how the state evolves over time (also, initial state probabilities)
        - this is the model how the world changes
    - Same as MDP transition model , but no choice of action
        - here is no action, you just watching 


<h2 id="0f1513d04ac32269de73d0f17465488e"></h2>

### Conditional Independence

 - Basic conditional independence:
    - Past and future independent of the present
        - the past anything before the current state and future anything beyond the current state are independent given the current state
    - Each time step only depends on the previous
    - This is called the (first order) Markov property
 - Note that the chain is just a (growable) BN
    - We can always use generic BN reasoning on it if we truncate the chain at a fixed length

---

<h2 id="94d2b6fed9dd768fe2edec7e6c85546f"></h2>

## Hidden Markov Models

A Markov model can talk about how the world changes , but if I forecast into the future sooner or later I just don't know anything anymore. 

But hidden Markov model says 2 things: I know how the world changes in a time step which let me figure out roughly what's gonna happen in the absense of evidence and at every time step I also getting some kind of reading -- I got some evidence that helps me sharpen my belief about what's happening. So as the same time that time passes ,evidence also comes in. The robot moves and takes another sonar reading.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_00.png)

---

 - Markov chains not so useful for most agents 
    - need observations to update your beliefs
 - Hidden Markov models (HMMs)
    - Underlying Markov chain over states *S*
    - You observe outpus (effects) at each time step
    - As a Bayes' net :
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_hmm.png)
        - structure:  1 hidden variable , and 1 observed variable 
        - what we're gonna have is that every time there's ganna be a hidden variable that structure like a markov chain and each time the evidence depends only on the state unobserved but only on the state at that time (E | X). 

---

<h2 id="c7624bc33d3af36dde93578541120635"></h2>

### Example : Weather HMM 

 - the hidden variable: where or not it's raining -- True or False
 - the observed variable: an umbrella

So what do we need to define the HMM ? 
 
 - we need 1 function which says how rain on one day depends on the previous day. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_weather_define_func1.png)
    - This is the rain to sun transition probability 
 - we also need a function says given rain and separately given sun, what's probability of seeing an umbrella
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_weather_define_func2.png)
    - That is called emission model. This tells you what probability of seeing various evidences values is  for each underlying state. 
    - In this case it says that when it's raining you see the umbrella 90% of time , but when it's not raining you still see it 20% of time. 

---

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_weather.png)

So from a single observation of an umbrella you don't know very much , but if day after day you're seeing the umbrella you start to kind of gain some confidence.

---

 - An HMM is defined by:
    - Initial distribution:  P(X₁)
    - Transitions:  P(X|X₋₁)
        - how the world evolved in a single time step
    - Emissions:   P(E|X)
        - the probability of various evidence values given the underlying state , which we then used to predict the opposite -- something about x.

---

### Example: GhostBusters HMM

 - P(X₁) = uniform
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_x1.png)
    - in the course demo, it is  0.02 that you see everywhere on map.
 - P(X|X') = usually move clockwise, but sometimes move in a random direction or stay in place
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_ghost.png)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_x2.png)
        - for that red square , it's 50% precent probability of moving right , 1/6 probability that you'll stand, 1/6 probability to go in other direction.
    - Where do these conditional probabilities come from ?
        - This is your assumptions about the world , you might learn them from data, for now that's just an input.
    - That's what happens from that one state.  But you generally don't know what state you're in, and you need to sum over all the options , that's  the forward algorithm was about.
 - P(Rᵢⱼ|X) = same sensor model as before: red means close, green means far away.
    - somewhere there has to be specified precisely the probability of reading at a certain position given the underlying state. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_sonar.png)
    - so it might say if you read at (3,3) and the ghost is there , your probability of getting red is 0.9. Those facts live in the emission model , they say how the evidence directly relates to the state at that time. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_model.png)
    

---

### HMM Conditional Independence 

 - HMMs have 2 import independence properties
    - Markov hidden process:  future depends on past  via the present 
        -  same as MM. 
    - Current observation independent of all else given current state
        - given X₃ , E₃ is independent of all everything else X₃.
 - Quiz: does this mean that evidence variables are guaranteed to be independent ?
    - If I don't observe anything I could say : Is the evidence I see at time₁ independent of the evidence I see at time₂ ? 
    - It is like the umbrella on tuesday is independent of the umbrella on Wednesday. 
    - So It seems like it shouldn't be. The evidence variables are absolutely not independent. They're only conditionally independent. 





---

### Real HMM Examples

For every HMM there is a hidden state -- which is usually the thing you want to figure out -- , and an evidence variable -- which is the thing you got to observe. 

You get the evidence at every time and you usually want to figure out the state at every time.  

 - Speech recognition HMMs:
    - Observations are acoustic signals (continuous valued)
    - States are specific positions in specific words (so, tens of thousands)

 - Machine translation HMMs:
    - Observations are words (tens of thousands)
    - States are translation options

 - Robot tracking:
    - Observations are range readings (continuous)
    - States are positions on a map (continuous)

---

## Filtering / Monitoring

Now we are going to talk about how to keep track of what you believe about a variable X -- the state variable -- as evidence comes it and time passes, and from this we'll build up the full-forward algorithm. 

The task is to figure out at any given time what do I believe is happening in the hidden state ( B<sub>t</sub>(X) ) given all the evidence from the first time step all the way up to the current time. 

 - Filtering, or monitoring, is the task of tracking the distribution B<sub>t</sub>(X) = P<sub>t</sub>(X<sub>t</sub> | e₁, …, e<sub>t</sub>) (the belief state) over time
 - We start with B₁(X) in an initial setting, usually uniform
 - As time passes, or we get observations, we update B(X)
 - The Kalman filter was invented in the 60’s and first implemented as a method of trajectory estimation for the Apollo program

---

### Example:  Robot Localization

The robot doesn't know where it is . It knows the map -- somebody gave blueprints . 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_RobotLocalization_robot.png)

It is going down the corridor and all do is shoot out lasers in each direction and see how close they bounced off a wall. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_RobotLocalization_map.png)

 - Sensor model: can read in which directions there is a wall, never more than 1 mistake
 - Motion model: may not execute action with small prob.


So it knows there's a wall right here , but no wall in front of me. And if it gets a reading that says there's wall on my left and right but not in front or behind, then suddenly it shouldn't think it's anywhere in this building.  Where should I think it is? It is kind of think it's in the corridors, corridors look like that. It's the sensor model , formly is conditioned on my current position, I need say a distribution over readings.  Let's image that instead of the continuous readings , the readings are wall or not in each direction.

---

So if I sense that is a wall above and below I should have pretty hight probability of my belief distribution of being in the dark gray squares. I should have some smaller probability of being in the lighter grey square.  

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_rl_t1.png)

 - t=1
 - Lighter grey: was possible to get the reading, but less likely b/c required 1 mistake

---
 
Time passes. 

As I continue reading north and south walls , what will happen is there will be fewer and fewer places which are consistent with my history of readings.


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_rl_t2.png)
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_rl_t3.png)
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_rl_t4.png)
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_rl_t5.png)

---

## Inference: Base Cases

Inference in Markov model is acutally the approximate inference .

Let's do the base cases. There's really 2 things that happen in HMMs. 

One is time passes.  You go from X at a certain time to X at the next time.  The other thing happens you see evidence.  There things are interleaved. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_base_case1.png)


But if all you had was a single time slice, you had X₁ and you saw evidence at time₁ E₁ , and you want to compute what's probability over my hidden state X₁ given my evidence E₁. So you just want to compute this conditional probability : P(X₁|e₁).  

 - I know P(X₁) , this is what before I see the evidence. 
 - Now I also know a distribution that tells me how the evidence relates to X₁ : P( E₁ | X₁ ). 
 
That's not quite what I want. What I want is P(X₁|e₁). 

 - X is capital because it's a vector here. I need one of these numbers for each value of X.
 - e is lowercase because there's a specific value , it's scalar. 

```
P(X₁|e₁) = P(X₁,e₁)/P(e₁)
         = P(e₁|X₁)·P(X₁) /P(e₁) 
```

The above manipulation I just did has nothing to do with HMMs. Now what I don't know is `P(e₁)`. But that is a constant as I vary X (not understand!).

So as you saw with the variable elimination I can just ignore it. So the actual reasoning goes something a little bit more cpmpactly . 

I'm instead going to compute P( X₁,e₁ ) and normalize in the end. I know how to compute it -- `P(X₁,e₁) = P(e₁|X₁)·P(X₁)`. So I compute all of these products: current probability times evidence probability. And then once I have that whole vector of those I re-normalize and now I have the conditional distribution of P(X₁|e₁). That is what happens when you incorporate evidence: you take your current vector of probabilities P(X₁) ,you multiply each one by the appropriate evidence factor and then you renormalize it. 

```
P(x₁|e₁) = P(x₁,e₁)/P(e₁)
         ∝ P(x₁,e₁)
         = P(x₁)·P(e₁|x₁)
```

大家都无视 P(e₁) ， 最后重新 normalize 

---

The other base case is this.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_base_case2.png)

You have a distribution over X₁ and rather than seeing evidence , time passes by one step. Well in this case I know P(X₁) , and I know P(X₂|X₁) . But I want is P(X₂).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_base_case_2_formulation.png)

全概率模型

---

 - Those 2 pieces assembled to do everything you need in HMMs. 

---

## Passage of Time  (case 2)

 - Assume we have current belief P(X | evidence to date)
    - B(X<sub>t</sub>) = P(X<sub>t</sub>|e<sub>1:t</sub>)
 - Then, after one time step passes:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_passage_of_time.png)
        - step1: 条件概率的 全概率展开 (case 2)
        - step2: 条件概率版 product rule
        - step3: independent 
    - you take your input P(X<sub>t</sub>|e<sub>1:t</sub>)  ,  which is your current beliefs. You take them multiply them by the transition probabilities , and then you sum out all the sources and now you have the probabilities over all of the targets. 
 - Or, compactly :
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_passage_of_time_compactly.png)
    - it says: you want to know the probability tomorrow of being at some particular X<sub>t+1</sub>. You consider how likely it is to get to X<sub>t+1</sub> from each locations (X'). So you want to know how likely it is that I'll end up at this particular X<sub>t+1</sub> , you consider all the places that could get you there , in one time step. and you say : what's the probability of being , here at A and then moving there , what's the probability ? ans whatelse if at B, C, ... 
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_passage_of_time_ABCD.png)
    - that is this, you  summer(∑) all of the places you could have been , you look how likely it is that you were there ( B(x<sub>t</sub>) ) to begin with , times how likely it is had you been there to get to X'.  
 - Basic idea: beliefs get “pushed” through the transitions
    - With the “B” notation, we have to be careful about what time step t the belief is about, and what evidence it includes

---

### Example: Passage of Time

 - As time passes, uncertainty “accumulates”
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_passage_of_time.png)
    - (Transition model: ghosts usually go clockwise)
 - That's basically your robot knows what's going on today and sooner or later if you never get any more evidence , the robot will become more and more confused until it has no idea what's going on. 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_passage_of_time_robot.png)


--- 

## Observation  (case 1)

 - Assume we have current belief P(X | previous evidence):
    - B'(X<sub>t+1</sub>) = P(X<sub>t+1</sub>|e<sub>1:t</sub>)
    - I have a belief vector that says here's my probability distribution over what's going on at a centain time BEFORE I see my evidence. 
 - Then , after the evidence tomorrow comes in: 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_observation.png)
        - take you current vector which represents the various probabilities right now , for each probability multiply by the evidence factor. So if the evidence is totally inconsistent with that state then even if somthing had high probability suddenly it might get zero out if it can't produce the evidence. 
        - so you go to each probability of each state you multiply each one by the evidence.  
        - so the blue thing is your probability before you saw your evidence , you waited by the evidence, and then this vector doesn't add to 1 anymore. So you re-normalized it now it adds up to 1 again , now the red thing is including the evidence you just saw. 
 - Or:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_observation_compactly.png)
    - you take your vector (blue) , you do point product with the evidence vector, and you normalize them.  Now you have your new beliefs.  
 - Basic idea: beliefs “reweighted” by likelihood of evidence
 - Unlike passage of time, we have to renormalize

---

### Example of Observation 

 - As we get observations, beliefs get reweighted, uncertainty “decreases”
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_hmm_example_observation.png)

---

### Example: Weather HMM

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs1188_hmm_example_wather_hmm_2.png)

---

## The Forward Algorithm

 - We are given evidence at each time and want to know
    - B<sub>t</sub> (X) = P(X<sub>t</sub>|e<sub>1:t</sub>)













