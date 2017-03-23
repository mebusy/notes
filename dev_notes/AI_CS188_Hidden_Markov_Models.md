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

-- pic

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
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_HMM_example_ghostbuster_model.png)



---





