...menustart

 - [Constraint Satisfaction Problems I](#8c8072703357c878142be0f423e13a69)

...menuend



<h2 id="8c8072703357c878142be0f423e13a69"></h2>
# Constraint Satisfaction Problems I

CPS

 - a single agent
 - deterministic actions
 - fully observed state
 	- you KNOW the configuration that you start in
 	- and then you plan about exactly how the world will evolve
 - discrete state space



N-Queens

Formulation 2:

Domains:  in each row , the value is going to be where the Queen for that row is.


Example : Cryptarithmetic


there are boxes which are constraints and the boxes are connected to all of the variables that participate in that constraints. 


Backtracking Search 


for each value in that value , you loop through them in some order

for each of those values you check if this value takes this new value did I break a constraint.


Structure:

   can we do things like notice tasmanis separate and solve it separately



filtering is about ruling out suspects.

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

