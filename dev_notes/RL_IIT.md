
# RL IIT

# Lec 50 - Hierarchical RL

 - temporal abstraction 
 - Transfer / Reusability
 - more powerful / Meaningful
 - state abstraction 
    - when I start breaking things down into these kinds of subproblems I can start focusing on things that are only needed for solving the subproblems.
    - solving one subproblem does not depend on other subproblems. 

# Lec 51 - Types of Optimality

 - hierarchically optimal
    - you have to search through policies that respect this hierarchy. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/iit_rl_51_types_of_optimality_room.png)


The best way I can solve this problem of getting out of room 1 is the white policy. 

If I use the white policy in room1 and yellow policy in room2 , that is a valid solution. 

But overall among all policies that satisfy the hierarchy , that is not the optimal one in terms of overall cost.  The yellow policy in room 1 followed by the yellow policy in room2 gives the hierarchically optimal.  ( think about the dotted line has different distance to those 2 exits.  )

 - call that recursively optimal


