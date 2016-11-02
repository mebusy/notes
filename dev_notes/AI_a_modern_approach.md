...menustart

 - [AI a modern approach](#c62ead95f43ef8c14dc28648f9c47276)
 - [2 INTELLIGENT AGENTS](#15ce9fbc84080f91c8cb9d4e393edfe3)
	 - [2.1 AGENTS AND ENVIRONMENTS](#6702b776b41280cc2e02257c5c19388e)
	 - [2.2 GOOD BEHAVIOR: THE CONCEPT OF RATIONALITY](#92194ef3836de8d78c7bd799f7633850)
		 - [2.2.1 Rationality](#3de59719cfab591d512a1bf2e5a2cc21)
		 - [2.2.2 Omniscience, learning, and autonomy](#4e2fd726ab99f5c2c4b7ad83eadfcd74)
	 - [2.3 THE NATURE OF ENVIRONMENTS](#8df182984a83ad2336b0ad2626607054)
		 - [2.3.1 Specifying the task environment](#9e8265c81b48b2d26cd334c14409800e)

...menuend



<h2 id="c62ead95f43ef8c14dc28648f9c47276"></h2>
# AI a modern approach

<h2 id="15ce9fbc84080f91c8cb9d4e393edfe3"></h2>
# 2 INTELLIGENT AGENTS

<h2 id="6702b776b41280cc2e02257c5c19388e"></h2>
## 2.1 AGENTS AND ENVIRONMENTS

An **agent** is anything that can be viewed as perceiving its **environment** through **sensors** and acting upon that environment through **actuators**.

We use the term **percept** to refer to the agent's perceptual inputs at any given instant. An agent's *percept sequence* is the complete history of everything the agent has ever perceived.

In general, *an agent's choice of action at any given instant can depend on the entire percept sequence observed to date, but not on anything it hasn't perceived*.   Mathematically speaking, we say that an agent's behavior is described by the **agent function** that maps any given percept sequence to an action.

We can imagine tabulating the agent function that describes any given agent; for most agents, this would he a very large table—infinite, in fact, unless we place a bound on the length of percept sequences we want to consider. Given an agent to experiment with, we can, in principle, construct this table by trying out all possible percept sequences and recording which actions the agent does in response.

The table is of course, an eviernal characterization of the agent. Internally, the agent function for an artificial agent will be implemented by an **agent program**.

The agent function is an abstract mathematical description; the agent program is a concrete implementation, running within some physical system.


To illustrate these ideas, we use a very simple example—the vacuum-cleaner world shown in Figure 2.2.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_F2.2.png)

> Figure 2.2 A vacuum-cleaner world with just two locations.

This particular world has just two locations: squares A and B. The vacuum agent perceives which square it is in and whether there is dirt in the square. It can choose to move left, move right, suck up the dirt, or do nothing. 

One very simple agent function is the following: if the current square is dirty, then suck; otherwise, move to the other square. A partial tabulation of this agent function is shown in Figure 2.3 and an agent program that implements it appears in Figure 2.8 on page 48.

Percept sequence | Action
 --- | ---
 [A,Clean]  | Right
 [A,Dirty]  | Suck
 [B,Clean]  | Left
 [B,Dirty]  | Suck
 [A,Clean],[A,Clean]  |  Right
 [A,Clean],[A,Dirty]  |  Suck
  .					  |   .
 [A,Clean],[A,Clean],[A,Clean]  | Right
 [A,Clean],[A,Clean],[A,Dirty]  | Suck
 ...		| ...

> Figure 2.3 Partial tabulation of a simple agent function for the vacuum-cleaner world shown in Figure 2.2.

Looking at Figure 2.3, we see that various vacuum-world agents can be defined simply by filling in the right-hand column in various ways. 

 The obvious question is this: *What is the right way to fill out the table*? In other words, what makes an agent good or bad, intelligent or stupid? We answer these questions in the next section.


<h2 id="92194ef3836de8d78c7bd799f7633850"></h2>
## 2.2 GOOD BEHAVIOR: THE CONCEPT OF RATIONALITY

When an agent is plunked down in an environment, it generates a sequence of actions according to the percepts it receives. 

This sequence of actions causes the environment to go through a sequence of states.

If the sequence is desirable, then the agent has performed well. 

This notion of desirability is captured by a **performance measure** that evaluates any given sequence of environment states.

Obviously, there is not one fixed performance measure for all tasks and agents;  Typically, a designer will devise one appropriate to the circumstances. This is not as easy as it sounds.

*As a general rule, it is better to design performance measures according to what one actually wants in the environment, rather than according to how one thinks the agent should behave.*

<h2 id="3de59719cfab591d512a1bf2e5a2cc21"></h2>
### 2.2.1 Rationality

What is rational at any given time depends on four things:

 - The performance measure that defines the criterion of success.
 - The agent's prior knowledge of the environment.
 - The actions that the agent can perform.
 - The agent's percept sequence to date.


This leads to a definition **of a rational agent**:

*For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.*


Consider the simple vacuum-cleaner agent that cleans a square if it is dirty and moves to the other square if not; this is the agent function tabulated in Figure 2.3. Is this a rational agent? That depends! First, we need to say what the performance measure is, what is known about the environment, and what sensors and actuators the agent has Let us assume the following:

 - The performance measure awards one point for each clean square at each time step, over a "lifetime" of 1000 time steps.
 - The "geography" of the environment is known a ***priori*** (Figure 2.2) but the dirt distribution and the initial location of the agent are not. Clean squares stay clean and sucking cleans the current square. The Left and Right actions move the agent left and right except when this would take the agent outside the environment, in which case the agent remains where it is.
 - The only available actions are Left, Right, and Suck.
 - The agent correctly perceives its location and whether that location contains dirt.

We claim that *under these circumstances* the agent is indeed rational; its expected performance is at least as high as any other agent's. 

One can see easily that the same agent would be irrational under different circum- stances. For example, once all the dirt is cleaned up, the agent will oscillate needlessly back and forth; if the performance measure includes a penalty of one point for each movement left or right, the agent will fare poorly.  A better agent for this case would do nothing once it is sure that all the squares are clean.


<h2 id="4e2fd726ab99f5c2c4b7ad83eadfcd74"></h2>
### 2.2.2 Omniscience, learning, and autonomy

We need to be careful to distinguish between rationality and **omniscience**.

**An omniscient** agent knows the *actual* outcome of its actions and can act accordingly; but omniscience is impossible in reality. 

Rationality is not the same as perfection. Rationality maximizes *expected* performance , while perfection maximizes *actual* performance.  

Our definition of rationality does not require omniscience, then, because the rational choice depends only on the percept sequence *to date*. We must also ensure that we haven't inadvertently allowed the agent to engage in decidedly underintelligent activities.  For example, if an agent does not look both ways before crossing a busy road, then its percept sequence will not tell it that there is a large truck approaching at high speed.  Does our definition of rationality say that it's now **OK** to cross the road?  Far from it! First, it would nOt be rational to cross the road given this uninformative percept sequence: the risk of accident from crossing without looking is too great. Second, a rational agent should choose the "looking" action before stepping into the street, because looking helps maximize the expected performance.

Doing actions *in order to modify future* percepts -- sometimes called **information gathering** -- is an important part of rationality and is covered in depth in Chapter 16.   A second example of information gathering is provided by the exploration that must be undertaken by a vacuum-cleaning agent in an initially unknown environment.

Our definition requires a rational agent not only to gather information but also to learn **as much as** possible from what it perceives.   The agent's initial configuration could reflect sonic prior knowledge of the environment, but as the agent gains experience this may be modified and augmented. 

To the extent that an agent relies on the prior knowledge of its designer rather than on its own percepts, we say that the agent lacks **autonomy**.

**A rational agent should be autonomous -— it should learn what it can to compensate for partial or incorrect prior knowledge. For example, a vacuum-cleaning agent that learns to foresee where and when additional dirt will appear will do better than one that does not. As a practical matter, one seldom requires complete autonomy from the start: when the agent has had little or no experience, it would have to act randomly unless the designer gave some assistance. So, just as evolution provides animals with enough built-in reflexes to survive long enough to learn for themselves, it would be reasonable to provide an artificial intelligent agent with some initial knowledge** as well as an ability to learn.  After sufficient experience of its environment, the behavior of a rational agent can become effectively independent of its prior knowledge.  Hence, the incorporation of learning allows one to design a single rational agent that will succeed in a vast variety of environments.



<h2 id="8df182984a83ad2336b0ad2626607054"></h2>
## 2.3 THE NATURE OF ENVIRONMENTS
 
Now that we have a definition of rationality, we are almost ready to think about building rational agents.

First, however, we must think about **task environments**, which are essentially the "problems" to which rational agents are the "solutions." We begin by showing how to specify a task environment, illustrating the process with a number of examples. We then show that task environments come in a variety of flavors. The flavor of the task environment directly affects the appropriate design for the agent program.

<h2 id="9e8265c81b48b2d26cd334c14409800e"></h2>
### 2.3.1 Specifying the task environment

In our discussion of the rationality of the simple vacuum-cleaner agent, we had to specify the performance measure, the environment, and the agent's actuators and sensors. We group all these under the heading of the **task environment**.  For the acronymically minded, we call this the **PEAS** (Performance, Environment, Actuators, Sensors) description.   In designing an agent, the first step must always be to specify the task environment as filly as possible (尽可能完全).

The vacuum world was a simple example; let us consider a more complex problem: an automated taxi driver.

Agent Type | Performance Measure | Environment | Actuators | Sensors
 --- | --- | --- | --- | --- 
Taxi driver | Safe, fast, legal, comfortable trip, maximize profits | Roads, other traffic, pedestrians, customers | Steering, accelerator, brake, signal, horn, display | Cameras, sonar, speedometer, GPS, odometer, accelerometer, engine sensors, keyboard


> Figure 2.4 PEAS description of the task environment for an automated taxi.

First, what is the **performance measure to which we would like our automated driver** to aspire? 

Desirable qualities include getting to the correct destination; minimizing fuel consumption and wear and tear; minimizing the trip time or cost; minimizing violations of traffic laws and disturbances to other drivers; maximizing safety and passenger comfort; maximizing profits. Obviously, some of these goals conflict, so tradeoffs will be required.

Next, what is the driving **environment** that the taxi will face? 

Any taxi driver must deal with a variety of roads, ranging from rural lanes and urban alleys to 12-lane freeways. The roads contain other traffic, pedestrians, stray animals, road works, police cars, puddles, and potholes.  The taxi must also interact with potential and actual passengers. There are also some optional choices. The taxi might need to operate in Southern California, where snow is seldom a problem, or in Alaska, where it seldom is not.  It could always be driving on the right, or we might want it to be flexible enough to drive on the left when in Britain or Japan. Obviously, the more restricted the environment, the easier the design problem.









