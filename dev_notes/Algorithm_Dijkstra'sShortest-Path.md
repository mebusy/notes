...menustart

 - [Dijkstra's Shortest-Path](#26e3bfaa6f7cabafa5ca159b210d4d49)
     - [Dijkstra's Shortest-Path Algorithm](#9da49bac70bc04960fbddf1ef0a5d2d9)
         - [Problem: Single-Source Shortest Paths](#ca071722757a16a38066ef54846aa6c3)
         - [Why Another Shortest-Path Algorithm?](#1eaef9d12a746195ea15ef25ebc3a7c8)
         - [Pseudo code](#34460a35a20211ec1d40102cc5f52de5)
     - [Examples](#ff7c0fcd6a31e735a61c001f75426961)
     - [Implementation and Running time](#3e5d3e41b577901d52f5a80509aae808)
         - [Heap Review](#377e23358a8c1384601aa5401d0c7af4)
         - [Use Heap to Speedup Dijkstra](#6d07a1b2f36548f5400dad288e02b4f8)
         - [Maintaining the Invariants](#d52f64236fbf5cf269d2ab1ca15680bd)
     - [Running Time Analysis](#e1c6f3377a2758270a95bc56571d46a5)

...menuend


<h2 id="26e3bfaa6f7cabafa5ca159b210d4d49"></h2>


# Dijkstra's Shortest-Path

<h2 id="9da49bac70bc04960fbddf1ef0a5d2d9"></h2>


## Dijkstra's Shortest-Path Algorithm

带权重的最短路劲搜索，权重不能为负

<h2 id="ca071722757a16a38066ef54846aa6c3"></h2>


### Problem: Single-Source Shortest Paths

Basically what we wanna do is compute something like driving directions. So we're given as input a graph, in the lecture I'm gonna work with directed graph , although the same algorithm would work undirected graphs with cosmetic changes.

 - Input: m edges, n vertices
    - each edge has non-negative length : le
    - source vertex s
 - Output: for each v ∊ V , compute L(v):= length of a shortest s-v path in G ( "length of path" = sum of edge lengths ).

![](../imgs/shortest_path.PNG)

We'll make 2 assumptions for the lectures. One is really just for convenience. The other is really important , without which Dijkstra's algorithm is not correct.

 - Assumption 1: [for convenience] ∀ v ∊ V , ∃ an s~>v path.There is a directed path from s to every other vertex v in the graph, otherwise the distance is +∞.
    - if there is not a path from s->v  then v is not reachable. So you could delete the irrelevant part of the graph and run Dijkstra on what remains. Alternatively Dijkstra will quite naturally figure out which vertices there are paths to from s and which ones there are not.
 - [important] le >=0 , ∀ e ∊ E  ( length of edge is non-negative)


<h2 id="1eaef9d12a746195ea15ef25ebc3a7c8"></h2>


### Why Another Shortest-Path Algorithm?

Question: doesn't BFS already compute shortest paths in linear time ?
A: BFS works only in the special case where the length of every edge of the graph is **one**.  At this moment we're trying to solve a more general problem. We're trying to solve the shortest paths when deges can have arbitrary non negative edge lengths.

![](../imgs/Dijkstra_illu.PNG)

<h2 id="34460a35a20211ec1d40102cc5f52de5"></h2>


### Pseudo code

```
Initialize:
- X = [s]  //vertices dealt so far
// dealt means we've correctly computed shortest path distance from s to every vertex in X
- A[s] = 0 //computed shortest path distances
- B[s] = empty path // computed shortest paths
// A and B will be indexed in the same way. 
//  A will store just a number for shortest path distance, 
//  B will store an actual path, B is only to help explanation!

// in each iteration it's going to grow and cover up one new vertex , 
//  there is 2 idea to pick a new vertex for iteration

MainLoop idea 1
- while X != V: // X⊆V
  pick one from X-V 

MainLoop idea 2
- among all edges (v,w)∊E with v∈X, w ∉ X 
  pick the one that minimizes 
  A[v]+ l_vw   (greedy criterion)
  this edge called (v*,w*)
- add w* to X.
- set A[w*] := A[v]+ l_v*w*
- set B[w*] := B[v*] ∪ (v*,w*)
```


<h2 id="ff7c0fcd6a31e735a61c001f75426961"></h2>


## Examples

![](../imgs/Dijkstra_iteration1.PNG)

 - 1st iteration: only SV and SW 2 crossing edges, SV scores 1, SW scores 4, so we choose (s,v)
 - 2nd iteration: now there is 3 crossing edges: SW,VW,VT, SW scores 4, SVW scores 3, SVT scores 7 , so we choose (s,v,w)
 - 3rd iteration: now there 2 crossing edges left: VT, WT, SVT score 7, SVWT scores 6 , so the final path is (s,v,w,t)

<h2 id="3e5d3e41b577901d52f5a80509aae808"></h2>


## Implementation and Running time

What's the running time of "naive" implementation of Dijkstra's algorithm ?  θ(mn)

There should be n-1 iterations of while loop . In each iteration, we do naively a linear scan through all of the edges. We go through the edges, we check if it's an eligible edge, that is if its tail in X and its head is outside of X ( X->(V-X) ).

We can do better by not changing the algorithm but changing how we organize the data as the algorithm proceeds.


<h2 id="377e23358a8c1384601aa5401d0c7af4"></h2>


### Heap Review

 - conceptually , a perfectly balanced binary tree 
 - key of node has to be  <= key of children 
    - this property ensure that the smallest key of them all has to be at the root of this tree.
 - extract-min by swapping up last leaf, bubbling down
 - insert via bubbling up
 
Heaps are generally logically thought of as a complete binary tree, even though they are usually implemented as a laid-out linear array. 


<h2 id="6d07a1b2f36548f5400dad288e02b4f8"></h2>


### Use Heap to Speedup Dijkstra

Because every itertation of the wild loop is responsible for picking an edge, you might expect that we're going to store edges in the heap. So the first really good idea is to actually use a heap to store vertices rather than edges.

We're just going to keep vertices not yet in X and then when we extract them in from the heap , it'll tell us which is the next vertex to add into the set X.

![](../imgs/Dijkstra_X_V-X.PNG)

Because we're storing vertices rather than edges in the heap, we're going to maintain the property that the key of vertex V is the smallest greedy Dijkstra score of any edge which has that vertex as its head.

![](../imgs/Dijkstra_X_X-V_key.PNG)

Show as the pic, there are two different edges(I,II) whose tail is in X , and have the same vertex in V-X as their head. So what should the key of this vertex be ? Well, it shoud be the smaller one. So the key value should be 3. The last edge which head in X and tail in V-X is not an eligible edge, so the key is +∞ . 

 - Invariant 1: elements in heap = vertices of V-X
 - Invariant 2: for v∉X , key[v] = smallest Dijkstra greedy score of an edge (u,v)∈E  with u∈X .
    - of +∞ if no such edges exist
    - 在算法执行过程中key的值是在不断逼近最终结果但在过程中不一定就等于长度。
 

**Points**: by invariants , Extract-min yields correct vertex W\* to add to X next. and we set A[W\*] to key[W\*]

![](../imgs/Dijkstra_heap_speedup.PNG)


<h2 id="d52f64236fbf5cf269d2ab1ca15680bd"></h2>


### Maintaining the Invariants

```
when W extracted from heap( ie. added to X )
- for each edge (w,v)∈E : 
    - if v∈V-X 
        - delete v from heap
        // either WV is the local winner
        // either it has the smallest score of them all
        - recompute key[v] = min( key[v],A[W]+l_wv )
        - re-insert v into heap
```

```
1 将与源点S相连的点加入堆，并调整堆。
2 选出堆顶元素W（即代价最小的元素），从堆中删除，并对堆进行调整。
3 处理与W相邻的，未被访问过的，满足三角不等式的顶点
    1):若该点在堆里，更新距离，并调整该元素在堆中的位置。
    2):若该点不在堆里，加入堆，更新堆。
4 若取到的W为终点，结束算法；否则重复步骤2、3。
```

当堆顶元素W被删除后，堆被破快，我们需要重新调调整；W被删除的同时， (w,v) 会成为新的crossing edge, 新的vertex V 只有两种情况： 1) V 原本就在堆里，那V本身就有key[v]值, 这时又会得到一个新的值 A[W]+l_wv, 取2者小的那个作为新的key值； 2) V 不在堆中，key[v] = A[W]+l_wv 加入堆。

<h2 id="e1c6f3377a2758270a95bc56571d46a5"></h2>


## Running Time Analysis

 - (n-1) Extract mins
 - each edge (v,w) triggers at most one delete/insert combo (if v added to X first)

So:

 - #of heap operations is O(m+n) = O(m)
 - running time = O(mlogn) 
