

# 2.4 PRIORITY QUEUES

## binary heaps

### Complete binary tree

 - Binary tree. Empty or node with links to left and right binary trees.
 - Complete tree. Perfectly balanced, except for bottom level.

### Binary heap representations

 - Binary heap. Array representation of a heap-ordered complete binary tree.
 - Heap-ordered binary tree.
    - Keys in nodes
    - Parent's key no smaller than children's key
 - Array representation.
    - Indices start at 1.
    - Take nodes in **level** order
    - No explicit links needed !

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algor1_pq_heap_repre.png)

### Binary heap properties

 - Proposition. Largest key is a[1], which is root of binary tree.
 - Proposition. Can use array indices to move through tree.
    - Parent of node at k is at k/2.
    - Children of node at k are at 2k and 2k+1.
    - a[0] 不使用




