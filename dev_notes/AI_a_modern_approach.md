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


2.3.2 Properties of task environments

**Fully observable vs. partially observable :**  

If an agent's sensors give it access to the complete state of the environment at each point in time, then we say that the task environ- ment is fully observable. A task environment is effectively fully observable if the sensors detect all aspects that are relevant to the choice of action; relevance, in turn, depends on the performance measure. Fully observable environments are convenient because the agent need not maintain any internal state to keep track of the world. 

An environment might be partially observable because of noisy and inaccurate sensors or because parts of the state are simply missing from the sensor data—for example, a vacuum agent with only a local dirt sensor cannot tell whether there is dirt in other squares.

**Single agent vs. multiagent:**

The distinction between single-agent and multiagent environments may seem simple enough.  For example, an agent solving a crossword puzzle by itself is clearly in a single-agent environment, whereas an agent playing chess is in a two- agent environment.

There are, however, some subtle issues. First, we have described how an entity ***may*** be viewed as an agent, but we have not explained which entities ***must*** be viewed as agents.  Does an agent A (the taxi driver for example) have to treat an object B (another vehicle) as an agent. or can it be treated merely as an object behaving according to the laws of physics, analogous to waves at the beach or leaves blowing in the wind?  *The key distinction is whether B's behavior is best described as maximizing a performance measure whose value depends on agent A's behavior.* 

For example, in chess, the opponent entity B is trying to maximize its performance measure, which, by the rules of chess, minimizes agent As per- formance measure. Thus, chess is a competitive multiagent environment. In the taxi-driving environment, on the other hand, avoiding collisions maximizes the performance measure of all agents, so it is a partially cooperative multiagent environment. It is also partially competitive because, for example, only one car can occupy a parking space. 

The agent-design problems in multiagent environments are often quite different from those in single-agent en- vironments; for example, communication often emerges as a rational behavior in multiagent environments; in some competitive environments, **randomized behavior is rational because** it avoids the pitfalls of predictability.


**Deterministic vs. stochastic.**

If the next state of the environment is completely determined by the current state and the action executed by the agent, then we say the environment is deterministic; otherwise, it is stochastic.

In principle, an agent need not worry about uncertainty in a fully observable, deterministic environment. (In our definition, we ignore uncertainty that arises purely from the actions of other agents in a multiagent environment: thus, a game can be deterministic even though each agent may be unable to predict the actions of the others.) 

If the environment is partially observable, however, then it could appear to be stochastic.  Taxi driving is clearly stochastic in this sense, because one can never predict the behavior of traffic exactly.  We say an environment is **uncertain** if it is not fully observable or not deterministic. 

One final note: our use of the word "stochastic" generally implies that uncertainty about outcomes is quantified in terms of probabilities; **a nondeterministic environment is one in which actions are** characterized by their *possible* outcomes, but no probabilities are attached to them. Nondetenninistic environment descriptions are usually associated with performance measures that require the agent to succeed for all possible outcomes of its actions.

**Episodic vs. sequential:**

In an episodic task environment, the agent's experience is divided into atomic episodes. In each episode the agent receives a percept and then performs a single action. Crucially, the next episode does not depend on the actions taken in previous episodes.  Many classification tasks are episodic. 

In sequential environments, on the other hand, the current decision could affect all future clecisions.  Chess and taxi driving arc sequential.

Episodic environments are much simpler than sequential environments because the agent does not need to think ahead.

**Static vs. dynamic:**

If the environment can change while an agent is deliberating, then we say the environment is dynamic for that agent; otherwise, it is static. 

Static environments are easy to deal with because the agent need not keep looking at the world while it is deciding on an action, nor need it worry about the passage of time. 

Dynamic environments, on the other hand. are continuously asking the agent what it wants to do; if it hasn't decided yet. that counts as deciding to do nothing. I

If the environment itself does not change with the passage of time but the agent's performance score does, then we say the environment is semidynamic. 

Taxi driving is clearly dynamic. Chess, when played with a clock, is semidynamic. Crossword puzzles are static.

**Discrete vs. continuous:**

The discrete/continuous distinction applies to the *state* of the environment, to the way *time* is handled, and to the *percepts* and *actions* of the agent. 

For example, the chess environment has a finite number of distinct states (excluding the clock), Chess also has a discrete set of percepts and actions. 

Taxi driving is a continuous-state and continuous-time problem: the speed and location of the taxi and of the other vehicles sweep through a range of continuous values and do so smoothly over time.   Input from digital cameras is discrete, strictly speak- ing, but is typically treated as representing continuously varying intensities and locations.

**Known vs. unknown:**

Strictly speaking, this distinction refers not to the environment itself but to the agent's or designer's state of knowledge about the "laws of physics" of the environment. 

In a known environment, the outcomes (or outcome probabilities if the environment is stochastic) for all actions are given.

Obviously, if the environment is unknown, the agent will have to learn how it works in order to make good decisions.

Note that the distinction between known and unknown environments is not the same as the one between fully and partially observable environments.  It is quite possible for a *known* environment to be *partially* observable —- for example, in solitaire card games, I know the rules but am still unable to *see* the cards that have not yet been turned over. Conversely, an *unknown* environment can be fully observable -— in a new video game, the screen may show the entire game state but I still don't know what the buttons do until I try them.

As one might expect, the hardest case is *partially observable, multiagent, stochastic, sequential, dynamic, continuous, and unknown*. 


---

## 2.4 THE STRUCTURE OF AGENTS

The joh of Al is to design an **agent program** that implements the agent function -— the mapping from percepts to actions.  We assume this program will run on some sort of computing device with physical sensors and actuators —- we call this the **architecture**:

```
  agent = architecture + program .
```

### 2.4.1 Agent programs

The agent programs that we design in this book all have the same skeleton:

they take the current percept as input from the sensors and return an action to the actuators. 

Notice the difference between the agent program, which takes the current percept as input, and the agent function, which takes the entire percept history.  

The agent program takes just the current percept as input because nothing more is available from the environment; if the agent's actions need to depend on the entire percept sequence, the agent will have to remember the percepts.

For example, Figure 2.7 shows a rather trivial agent program that keeps track of the percept sequence and then uses it to index into a table of actions to decide what to do, The table—an example of which is given for the vacuum world in Figure 2.3—represents explicitly the agent function that the agent program embodies.

```
function TABLE-DRIVEN-AGENT(percept) returns an action
	persistent percepts, a sequence, initially empty
		table, a table of actions, indexed by percept sequences, initially fully specified

	append percept to the end of percepts 
	action LOOKUP( percepts,table)
	return action
```

> Figure 2.7 The TABLE DRIVEN AGENT program is invoked for each new percept and returns an action each time. It retains the complete percept sequence in memory.


To huild a rational agent in this way, we as designers must construct a table that contains the appropriate action for every possible percept sequence.

It is instructive to consider why the table-driven approach to agent construction is doomed to failure.  The table may become massive large.

Despite all this, TARLE-DRIVEN-AGFNT does do what we want: it implements the desired agent function.  The key challenge for AI is to find out how to write programs that, to the extent possible, produce rational behavior from a smallish program rather than from a vast table. 

We outline four basic kinds of agent programs that embody the principles underlying almost all intelligent systems:

 - Simple reflex agents;
 - Model-based reflex agents;
 - Goal-based agents; 
 - Utility-based agents.


Each kind of agent program combines particular components in particular ways to generate actions. Section / 4.7 describes the variety of ways in which the components themselves can be represented within the agent. This variety provides a major organizing principle for the field and for the book itself.


### 2.4.2 Simple reflex agents

The simplest kind of agent is the **simple reflex agent**.

These agents select actions on the basis of the *current* percept, ignoring the rest of the percept history. 

For example, the vacuum agent whose agent function is tabulated in Figure 2.3 is a simple reflex agent, because its decision is based only on the current location and on whether that location contains dirt. Art agent program for this agent is shown in Figure 2.8.
 
```
function REFLEX-VACUUM-AGENT( [location,status] ) returns an action
	if status = Dirty then return Suck
	else if location = A then return Right
	else if location = B then return Left
```

> Figure 2.8 The agent program for a simple reflex agent in the two-state vacuum environ- ment. This program implements the agent function tabulated in Figure 2.3.

The program in Figure 2,8 is specific to one particular vacuum environment. A more general and flexible approach is first to build a general-purpose interpreter for condition-action rules and then to create rule sets for specific task environments.  Figure 2.9 gives the structure of this general program in schematic form, showing how the condition-action rules allow the agent to make the connection from percept to action. 

```
function SIMPLE-REFLEX-AGENT( percept) returns an action
	persistent, rates, a set of condition—action rules

	state <- INTERPRET-INPUT(percept)
	rule <- RULE MATCH(state, ruie)
	action <— rule.ACTION
	return action
```

> Figure 2.10 A simple reflex agent It acts according to a vile whose condition matches the current state, as defined by the percept.


*The agent in Figure 2.10 will work only if the correct decision can be made on the basis of only the current percept—that is. only if the environment is fully observable*. 


### 2.4.3 Model-based reflex agents

The most effective way to handle partial observability is for the agent to *keep track of the past of the world it can't see now*.

That is, the agent should maintain some sort of **internal state** that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state. 

For the braking problem, the internal state is not too extensive— just the previous frame from the camera, allowing the agent to detect when two red lights at the edge of the vehicle go on or off simultaneously. 

Updating this internal state information as time goes by requires two kinds of knowl- edge to be encoded in the agent program.

 - First, we need some information about how the world evolves independently of the agent
 	- for example, that an overtaking car generally will be closer behind than it was a moment ago. 
 	- 所处世界的发展
 - Second, we need some information about how the agent's own actions affect the world
 	- for example, that when the agent turns the steering wheel clockwise, the car turns to the right, or that after driving for five minutes northbound
on the freeway, one is usually about five miles north of where one was five minutes ago. 
 	- agent 的行为对世界的影响


This knowledge about "how the world works"—whether implemented in simple Boolean circuits or in complete scientific theories -— is called a **model** of the world. An agent that uses such a model is called a **model-based agent**.








