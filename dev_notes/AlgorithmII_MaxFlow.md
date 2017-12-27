...menustart

 - [6.4 MAXIMUM FLOW](#60804ce1e5e1b895af839b4ef2122a99)
 - [introduction](#8800e1c9b3e22c44ba59a34db3fe4841)
     - [Mincut problem](#450389af6383415c1047574d48dd0785)
     - [Maxflow problem](#e5e9af9ecfee06cab309dca7d7623ddf)

...menuend


<h2 id="60804ce1e5e1b895af839b4ef2122a99"></h2>

# 6.4 MAXIMUM FLOW

<h2 id="8800e1c9b3e22c44ba59a34db3fe4841"></h2>

# introduction

<h2 id="450389af6383415c1047574d48dd0785"></h2>

## Mincut problem

 - Input
    - An edge-weighted digraph, source vertex s, and target vertex t
    - each edge has a positive capacity
 - Def.
    - A **st-cut (cut)** is a partition of the vertices into two disjoint sets, with s in one set A and t in the other set B. 
 - Def.
    - Its **capacity** is the sum of the capacities of the edges from A to B.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mcut_0.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mcut_1.png)

 - **Minimum st-cut (mincut) problem**
    - Find a cut of minimum capacity

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorII_mcut_2.png)


<h2 id="e5e9af9ecfee06cab309dca7d7623ddf"></h2>

## Maxflow problem

 - Input. 
    - An edge-weighted digraph, source vertex s, and target vertex t.
    - each edge has a positive capacity
 - Def.
    - An **st-flow (flow)** is an assignment of values to the edges such that:
        - Capacity constraint: 0 ≤ edge's flow ≤ edge's capacity.
        - Local equilibrium: inflow = outflow at every vertex (except s and t).





