

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


### Promotion in a heap

 - Scenario. Child's key becomes **larger** key than its parent's key.
 - To eliminate the violation:
    - Exchange key in child with key in parent.
    - Repeat until heap order restored.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_swim.png)

```java
private void swim(int k) {
    // 1 is root, do not care
    // parent is smaller 
    while (k > 1 && less(k/2, k)) {
        exch(k, k/2); // swap key
        k = k/2;     // check the new violation of the upper level
    }    
}
```

 - Peter principle. Node promoted to level of incompetence.
 - swim/sink 都需要递归检查
    - swim 用于 insertion
    - sink 用于 delete max

### Insertion in a heap

 - Insert. Add node at end, then swim it up.
    - 添加新node到PQ最后，然后 swim到正确位置
 - Cost. At most 1 + lg N compares.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_insertion.png)

```java
public void insert(Key x) {
    // ++ first , because we don't use index 0
    pq[++N] = x;
    // swim up
    swim(N); 
}
```

### Demotion in a heap

 - Scenario. Parent's key becomes **smaller** than one (or both) of its children's.
 - To eliminate the violation:
    - Exchange key in parent with key in larger child. 
        - why not the smaller one ? Power struggle. Better subordinate promoted
    - Repeat until heap order restored.
 
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_pq_sink.png)

```java
private void sink(int k) {
    while (2*k <= N) {
        int j = 2*k;
        // child node at k are 2k,2k+1 
        // choose the largest child as j
        if (j < N && less(j, j+1)) j++;
        if (!less(k, j)) break;
        exch(k, j);
        k = j;    
    }    
}
```


### Delete the maximum in a heap

 - Delete max.
    - Exchange root with node at end, then sink it down.
    - 交换根节点 到最后一个节点， 然后新的根节点 sink 到正确位置
 - Cost. At most 2 lg N compares.



