...menustart

 - [Constraint Satisfaction Problems I](#8c8072703357c878142be0f423e13a69)

...menuend



<h2 id="8c8072703357c878142be0f423e13a69"></h2>
# Constraint Satisfaction Problems I

CPS


## What is Search For?

 - Assumptions about the world:  
 	- a single agent
 	- deterministic actions
 	- fully observed state
 		- you KNOW the configuration that you start in
 		- and then you plan about exactly how the world will evolve
 	- discrete state space

 - Planning: sequences of actions
 	- The path to the goal is the important thing
 	- Paths have various costs, depths
 	- Heuristics give problem-specific guidance

 - Identification: assignments to variables
 	- The goal itself is important, not the path
 	- All paths at the same depth (for some formulations)
 	- CSPs are specialized for identification problems

## Constraint Satisfaction Problems

 - Standard search problems:
 	- State is a “black box”: arbitrary data structure
 	- Goal test can be any function over states
 	- Successor function can also be anything
 - Constraint satisfaction problems (CSPs):
 	- A special subset of search problems
 	- State is defined by ***variables Xᵢ***  with values from a ***domain D** (sometimes D depends on i)
 	- Goal test is a ***set of constraints*** specifying allowable combinations of values for subsets of variables
 - Allows useful general-purpose algorithms with more power than standard search algorithms

## CSP Example: Map Coloring

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/CS188_map_coloring.png)

 - Variables: WA, NT, Q, NSW, V, SA, T
 - Domains: D = {red, green, blue}
 - Constraints: adjacent regions must have different colors
 	- Implicit: WA ≠ NT 
 	- Explicit: (WA, NT) ∈ { (red,green),(red,blue), ... }
 - Solutions are assignments satisfying all constraints, e.g.
 	- {WA=red, NT=green, Q=red, NSW=green, V=red, SA=blue, T=green}

## Exampe: N-Queens

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_N_queens.png)

Formulation 1:

 - Variables: Xᵢⱼ
 - Domains: {0,1}
 - Constraints
 	- ∀i,j,k (Xᵢⱼ, X<sub>ik</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>kj</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>i+k, j+k</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- ∀i,j,k (Xᵢⱼ, X<sub>i+k, j-k</sub>) ∈ { (0,0), (0,1), (1,0) }
 	- Σ Xᵢⱼ = N


Formulation 2:

 - Variables: Q<sub>k</sub>
 	- in each row , the value is going to be where the Queen for that row is.
 - Domains: {1,2,3, ... , N } 
 - Constraints:
 	- Implicit: ∀i,j non-threatening(Qᵢ,Qⱼ) 
 	- Explicit: (Q₁,Q₂) ∈ { (1,3),(1,4), ... } , ...


## Constraint Graphs

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_constraints_graph.png)

 - Binary CSP: 
 	- each constraint relates (at most) two variables
 - Binary constraint graph: 
 	- nodes are variables, arcs show constraints
 - General-purpose CSP algorithms use the graph structure to speed up search. 
 	- E.g., Tasmania is an independent subproblem!


### Example : Cryptarithmetic

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Cryptarithmetic.png)

 - Variables:
 	- F T U W R O X₁ X₂ X₃
 - Domains:
 	- { 0,1,2,3,4,5,6,7,8,9 }
 - Constraints:
 	- all diff ( F T U W R O  )
 	- O + O = R + 10·X₁   进位
 	- ...

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Cryptarithmetic_graph.png)

there are boxes which are constraints and the boxes are connected to all of the variables that participate in that constraints. 

### Example: Sudoku

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_example_sudoku.png)

 - Variablels:
 	- Each (open) square
 - Domains:
 	- { 1,2, ... , 9 }
 - Constraints:
 	- 9-way alldiff for each columen
 	- 9-way alldiff for each row
 	- 9-way alldiff for each region
 	- (or can have a bunch of pairwise inequality constraints)


### Example: The Waltz Algorithm

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_Waltz_algorithm.png)

 - The Waltz algorithm is for interpreting line drawings of solid polyhedra as 3D objects
 - An early example of an AI computation posed as a CSP 

Approach:
 
 - Each intersection is a variable
 - Adjacent intersections impose constraints on each other
 - Solutions are physically realizable 3D interpretations

## Varieties of CSPs and Constraints

### Varieties of CSPs

 - Discrete Variables
	- Finite domains
		- Size d means O(dn) complete assignments
		- E.g., Boolean CSPs, including Boolean satisfiability (NP-complete)
	- Infinite domains (integers, strings, etc.)
		- E.g., job scheduling, variables are start/end times for each job
		- Linear constraints solvable, nonlinear undecidable

 - Continuous variables
	- E.g., start/end times for Hubble Telescope observations
	- Linear constraints solvable in polynomial time by LP methods (see cs170 for a bit of this theory)

### Varieties of Constraints

 - Varieties of Constraints
	- Unary constraints involve a single variable (equivalent to reducing domains), e.g.:
		- SA ≠ green
	- Binary constraints involve pairs of variables, e.g.:
		- SA ≠ WA
	- Higher-order constraints involve 3 or more variables: 
		- e.g., cryptarithmetic column constraints

- Preferences (soft constraints):
	- E.g., red is better than green
	- Often representable by a cost for each variable assignment
	- Gives constrained optimization problems
	- (We’ll ignore these until we get to Bayes’ nets)

## Solving CSPs

### Standard Search Formulation

 - Standard search formulation of CSPs
 - States defined by the values assigned so far (partial assignments)
	- Initial state: 
		- the empty assignment, {}
	- Successor function: 
		- assign a value to an ***unassigned*** variable
	- Goal test: 
		- the current assignment is complete and satisfies all constraints

We’ll start with the straightforward, naïve approach, then improve it


### Backtracking Search 

 - Backtracking search is the basic ***uninformed*** algorithm for solving CSPs
 - Idea 1: One variable at a time
	- Variable assignments are commutative, so fix ordering
	- I.e., [WA = red then NT = green] same as [NT = green then WA = red]
	- Only need to consider assignments to a single variable at each step

 - Idea 2: Check constraints as you go
	- I.e. consider only values which do not conflict previous assignments
	- Might have to do some computation to check the constraints
	- “Incremental goal test”

 - Depth-first search with these two improvements
	is called backtracking search (not the best name)

 - Can solve n-queens for n <= 25

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/cs188_backtrack_search_example.png)

```
function BACKTRACKING-SEARCH( csp ) return solution/failure
	return RECURSIVE-BACKTRACKING( {} , csp )

function RECURSIVE-BACKTRACKING( assignment, csp ) return soln/failure
	if assignment is complete then return assignment
	var <- SELECT-UNASSIGNED-VARIABLE( VARIABLES[csp], assigment, csp )

	// for each value in that values , you loop through them in some order
	for each value in ORDER-DOMAIN-VALUES( var, assignment , csp ) do
		// for each of those values you check if
		// this variable takes this new value did I break a constraint.
		if value is consistent with assigment given CONSTRAINTS[csp] then
			add {var = value} to assignment
			result <- RECURSIVE-BACKTRACKING( assignment , csp )
			if result ≠ failure then return result
			// result is failure
			remove {var = value} from assignment
	return failure
```

 - Backtracking = DFS + variable-ordering + fail-on-violation
 - What are the choice points?


### Improving Backtracking

 - General-purpose ideas give huge gains in speed
 - Ordering:
	- Which variable should be assigned next?  变量顺序
	- In what order should its values be tried?  值选择顺序
 - Filtering: 
 	- Can we detect inevitable failure early?
 - Structure: 
 	- Can we exploit the problem structure?
 	- Do things like notice tasmanis separate and solve it separately

### Filtering

Filtering is about ruling out suspects.

#### Forward Checking

Filtering | Forward checking
--- | ---
Keep track of domains for unassigned variables and cross off bad options | Cross off values that violate a constraint when added to the existing assignment


idea : keep track of all of the unassigned variables , keep track of what values they might reasonably take when we finally get to them.

in forward checking every time I assign a variable right which collapses its domain to a single choice for now , I checked to see whether there are other unassigned variables that have some illegal values when I take into account that new assignment. 


example 

WA <- red
remove red choice from NT , SA

so that basic idean when I assigned something I look at its neighbors in the graph and cross things off, that's called forward checking.


forward checking doesn't check interactions between unassigned variables just checks interactions between assigned variables and their neighbors.


the idea of checking single arcs

so far we talked about checking an assignment against its neighbors and here we were talking just in this last slide about checking between two unassigned variables.

what does it mean to check an arc ?  we look at an arc what it means to check it is formally we check whether or not is consistent so we say an arc is consistent if for every x in the tail 

