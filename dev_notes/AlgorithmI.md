
# 1.5 UNION-FIND

 - dynamic connectivity
 - quick find
 - quick union
 - improvements

## dynamic connectivity

 - Given a set of N objects.
    - Union command: connect two objects.
    - Find/connected query: is there a path connecting the two objects?

### Implementing the operations
 
 - Find query. Check if two objects are in the same component.
 - Union command. Replace components containing two objects with their union.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_union.png)


### Quick-find  [eager approach]

 - Data structure.
    - Integer array id[] of length N.
    - Interpretation: p and q are connected iff they have the same id.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_datastructure.png)

 - Find. Check if p and q have the same id.
 - Union. To merge components containing p and q, change all entries whose id equals id[p] to id[q].

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_datastructure2.png)


### Quick-find is too slow

 - Cost model. Number of array accesses (for read or write).

algorithm | initialize | union | find
--- | --- | --- | --- 
quick-find | N | N | 1

 - Union is too expensive 
    - It takes N² array accesses to process a sequence of N union commands on N objects.


## Quick-union [lazy approach]

 - Data structure.
    - Integer array id[] of length N.
    - Interpretation: id[i] is parent of i. 
        - keep going until it doesn’t change (algorithm ensures no cycles)
    - Root of i is id[id[id[...id[i]...]]].

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_qu_lazy_ds.png)

 - Find. Check if p and q have the same root.
 - Union. To merge components containing p and q, set the id of p's root to the id of q's root.
    - e.g. to connect 3 and 5 , set the 3's root (9) to 5's root (6) 
    - `id[9] = 6`

 - Cost model. Number of array accesses (for read or write).


algorithm | initialize | union | find
--- | --- | --- | --- 
quick-find | N | N | 1
quick-union | N | N⁺ | N(worst cast)

 - `⁺` includes cost of finding roots


 - Quick-find defect.
    - Union too expensive (N array accesses).
 - Quick-union defect.
    - Trees can get tall.
    - Find too expensive (could be N array accesses).

## improvements

### Improvement 1: weighting

 - Weighted quick-union.
    - Modify quick-union to avoid tall trees.
    - Keep track of size of each tree **(number of objects)**.
    - Balance by linking root of smaller tree to root of larger tree.
        - reasonable alternatives: p union by height or "rank"

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_weighted_qu.png)

---

 - Data structure. Same as quick-union, but maintain extra array sz[i] to count number of objects in the tree rooted at i.
 - Find. Identical to quick-union.
    - `return root(p) == root(q);`
 - Union. Modify quick-union to:
    - Link root of smaller tree to root of larger tree.
    - Update the sz[] array.


 - Running time.
    - Find: takes time proportional to depth of p and q.
    - Union: takes constant time, if given roots.
 - Proposition. Depth of any node x is at most lgN.


algorithm | initialize | union | find
--- | --- | --- | --- 
quick-find | N | N | 1
quick-union | N | N⁺ | N(worst cast)
weighted QU | N | lgN⁺ | lgN

 - `⁺` includes cost of finding roots

### Improvement 2: path compression

 - Quick union with path compression
    - Just after computing the root of p, set the id of each examined node to point to that root.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_pathcompress1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_uf_pathcompress2.png)


algorithm | worst case
--- | --- 
quick-find | MN
quick-union | MN 
weighted QU | N+MlgN
QU + path compression | N+MlgN
weight QU + path compression | N+Mlg<sup>\*</sup>N

 - M union-find operations on a set of N objects

 - Ex. [10⁹ unions and finds with 10⁹ objects]

---

# 2.1 ELEMENTARY SORTS

## shuffling

 - How to shuffle an array
 - Goal. Rearrange array so that result is a uniformly random permutation.

### Shuffle sort

 - Generate a random real number for each array entry.
    - useful for shuffling columns in a spreadsheet
 - Sort the array.
 - Proposition. Shuffle sort produces a uniformly random permutation of the input array, provided no duplicate values.
    - assuming real numbers uniformly at random

### Knuth shuffle

 - In iteration i, pick integer r between 0 and i uniformly at random
 - Swap a[i] and a[r].

 - Proposition. [Fisher-Yates 1938] Knuth shuffling algorithm produces a uniformly random permutation of the input array in linear time.
    - assuming integers uniformly at random

```java
public static void shuffle(Object[] a)
{
    int N = a.length;
    for (int i = 0; i < N; i++)
    {
        // between 0 and i
        int r = StdRandom.uniform(i + 1);
        exch(a, i, r);
    }
}
```

## convex hull

 - The **convex hull** of a set of N points is the smallest perimeter fence enclosing the points.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_sort_convexhull.png)

 - Convex hull output. Sequence of vertices in counterclockwise order.

### Convex hull: mechanical algorithm

 - Mechanical algorithm
    - Hammer nails perpendicular to plane; stretch elastic rubber band around points.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_mechanical.png)


### Convex hull application: motion planning
 
 - Robot motion planning
    - Find shortest path in the plane from s to t that avoids a polygonal obstacle.
 - Fact. Shortest path is either straight line from s to t or it is one of two polygonal chains of convex hull.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_app_robot_root.png)

### Convex hull application: farthest pair

 - Farthest pair problem
    - Given N points in the plane, find a pair of points with the largest Euclidean distance between them.
 - Fact. Farthest pair of points are extreme points on convex hull.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_app_farthest_pairs.png)

### Convex hull: geometric properties

 - Fact. Can traverse the convex hull by making only counterclockwise turns.
 - Fact. The vertices of convex hull appear in increasing order of polar angle with respect to point p with **lowest y-coordinate**.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_geometry.png)

### Graham scan

 - Choose point p with smallest y-coordinate.
 - Sort points by polar angle with p.
 - Consider points in order; discard unless it create a ccw turn.

### Implementing ccw

 - CCW. 
    - Given three points a, b, and c, is a → b → c a counterclockwise turn?
    - is c to the left of the ray a→b 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_CCW.png)

 - Lesson. Geometric primitives are tricky to implement.
    - Dealing with degenerate cases.
    - Coping with floating-point precision.
 - Determinant (or cross product) > 0 , then a → b → c is counterclockwise.


### Polar Order

 - Polar order. Given a point p, order points by polar angle they make with p.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_convexhull_polar_order.png)

 - High-school trig solution. Compute polar angle θ w.r.t. p using atan2().
 - Drawback. Evaluating a trigonometric function is expensive.
 - A ccw-based solution.
    - If q1 is above p and q2 is below p, then q1 makes smaller polar angle.
    - If q1 is below p and q2 is above p, then q1 makes larger polar angle.
    - Otherwise, ccw(p, q1, q2) identifies which of q1 or q2 makes larger angle.

```java
private class PolarOrder implements Comparator<Point2D>A {
    public int compare(Point2D q1, Point2D q2) {
        double dy1 = q1.y - y;
        double dy2 = q2.y - y;    
        if      (dy1 == 0 && dy2 == 0) { ... }  // horizontal
        else if (dy1 >= 0 && dy2 < 0) return -1;
        else if (dy2 >= 0 && dy1 < 0) return +1;
        else return -ccw(Point2D.this, q1, q2);
    }   
}
```


---

# 2.2 MERGESORT

## Two classic sorting algorithms

 - Mergesort
    - Java sort for objects.
    - Perl, C++ stable sort, Python stable sort, Firefox JavaScript, ...
 - Quicksort. [next lecture]
    - Java sort for primitive types.
    - C qsort, Unix, Visual C++, Python, Matlab, Chrome JavaScript, ...

## Merge Sort 

 1. divide into 2 parts, recursively sort each of them
 2. merge those 2 sorted array 
    - need an extra N length array to **merge**

## Mergesort: practical improvements

 - Use insertion sort for small subarrays.
    - Mergesort has too much overhead for tiny subarrays.
    - Cutoff to insertion sort for ≈ 7 items.


## Stability

 - A typical application. First, sort by name; **then** sort by section.
 - Q. Which sorts are stable?
    - A. Insertion sort and mergesort (but not selection sort or shellsort).

---

## 2.3 QUICKSORT

 0. shuffle 
 1. partition , for some j,   left < j < right , into 2 pieces
 2. sort each piece recursively  

```java
public static void sort(Comparable[] a) {
    // shuffle before sort , 1 times
    StdRandom.shuffle(a);
    sort(a, 0, a.length - 1);
}

private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo) return;
    int j = partition(a, lo, hi);
    sort(a, lo, j-1);
    sort(a, j+1, hi);
}
```


### Quicksort properties 

 - in-place  
 - not stable

### Quicksort: practical improvements

 - Insertion sort small subarrays.


## Quick-select

 - Goal. Given an array of N items, find a k<sub>th</sub> smallest item.
 - Quick-select takes linear time on average.

---
