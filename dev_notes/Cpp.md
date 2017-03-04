


# 2

## 2.4  Graph as data structure

 - Connectitiy matrix (also distances)
    - often used for dense graph
 - Edge List Representation 
    - often used for sparse graph
    - Most real world problems are relatively sparse
 - Tradeoffs - Graph as an ADT 

### List representation 

A representation of a directed graph with n vertices can use a list , for example , an array of n lists of vertices.

 - Definition: A representation of a ***directed graph*** with *n* vertices using an array of *n* lists of vertices.
 - List *i* contains vertex *j* if there is an edge from vertex *i* to vertex *j*.
 - A ***weighted graph*** may be represented with a list of vertex / weight pairs.
 - An ***undirected graph*** my be represented by having vertex *j* in the list for vertex *i* , and vertex *i* in the list for vertex *j*.

 
### Matrix vs. list directed graph

```
1 1 1 1
1 0 0 0
0 1 0 1
0 1 1 0 
```

```
1 2 3 4
1
2 4
2 3
```

### Dijkstra shortest path

We're going to use undirected graphs with weights(cost). So costs are going to all be non-negative.
























