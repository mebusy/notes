...menustart

 - [概述](#a4d3b02a466677324278a9a153fb4adb)

...menuend


**Dynamic programming** (also known as **dynamic optimization**) is a method for solving a complex problem by 

 - breaking it down into a collection of simpler subproblems, in a recursive manner
 - solving each of those subproblems just once, and storing their solutions 
 	- ideally, using a memory-based data structure. 
 - The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, 
 	- thereby saving computation time at the expense of a (hopefully) modest expenditure in storage space. 
 	- The technique of storing solutions to subproblems instead of recomputing them is called **"memoization"**.

Dynamic programming algorithms are often used for **optimization**. A dynamic programming algorithm will examine the previously solved subproblems and will combine their solutions to give the best solution for the given problem. 

Compare to **greedy algorithm** :

 - a **greedy algorithm** treats the solution as some sequence of steps and picks the locally optimal choice at each step. 
 - Using a greedy algorithm does not guarantee an optimal solution, 
 	- because picking locally optimal choices may result in a bad global solution, 
 	- but it is often faster to calculate. 
 - Fortunately, some greedy algorithms (such as Kruskal's or Prim's for minimum spanning trees) are proven to lead to the optimal solution.


For example, If the coin denominations are 1,4,5,15,20 and the given amount is 23 , this greedy algorithm gives a non-optimal solution of 20+1+1+1, while the optimal solution is 15+4+4.

 - a dynamic programming algorithm would find an optimal solution for each amount by first finding an optimal solution for each smaller amount and then using these solutions to construct an optimal solution for the larger amount. 
 - a greedy algorithm might treat the solution as a sequence of coins, starting from the given amount and at each step subtracting the largest possible coin denomination that is less than the current remaining amount.          

  

In addition to finding optimal solutions to some problem, dynamic programming can also be used for counting the number of solutions, for example 

 - counting the number of ways a certain amount of change can be made from a given collection of coins, 
 - or counting the number of optimal solutions to the coin change problem described above.

Sometimes, *applying memoization to the naive recursive algorithm*   already results in a dynamic programming algorithm with asymptotically optimal time complexity, but for optimization problems in general the optimal algorithm might require more sophisticated algorithms.


在数学与计算机科学领域，动态规划用于解决那些可分解为**重复子问题**（overlapping subproblems，eg. **递归求阶乘**）并具有**最优子结构**（optimal substructure，eg.**最短路径算法**）的问题，动态规划比通常算法花费更少时间。

动态规划的核心方程被命名为贝尔曼方程，该方程以**递归**形式重申了一个优化问题。

<h2 id="a4d3b02a466677324278a9a153fb4adb"></h2>

## 概述

![](http://upload.wikimedia.org/wikipedia/en/4/42/Shortest_path_optimal_substructure.png)  (1)

 - 使用最优子结构寻找最短路径：直线表示边，波状线表示两顶点间的最短路径（路径中其他节点未显示）；粗线表示从起点到终点的最短路径。
 - start到goal的最短路径由start的相邻节点到goal的最短路径及start到其相邻节点的成本决定


最优子结构即可用来寻找整个问题最优解的子问题的最优解。举例来说，寻找图上某顶点到终点的最短路径，可先计算该顶点 *所有相邻顶点* 至终点的最短路径，然后以此来选择最佳整体路径，如图1所示。

一般而言，最优子结构通过如下三个步骤解决问题：

 - a) 将问题分解成较小的子问题；
 - b) 通过递归 求出子问题的最优解 (还是使用这三个步骤)；
 - c) 使用这些最优解构造初始问题的最优解。

子问题的求解是通过不断划分为更小的子问题实现的，直至我们可以在常数时间内求解。


![](http://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Fibonacci_dynamic_programming.svg/108px-Fibonacci_dynamic_programming.svg.png)

Fibonacci序列的子问题示意图：使用**有向无环图**（DAG, directed acyclic graph）而不是用**树**表示重复子问题的分解。

为什么是DAG而不是树呢？答案就是，如果是树的话，会有很多重复计算 。

一个问题可划分为重复子问题 是指通过 **相同的子问题**可以解决**不同的较大问题**。

例如，在Fibonacci序列中，F3 = F1 + F2和F4 = F2 +F3都包含计算F2。 由于计算F5需要计算F3和F4，一个比较笨的计算F5的方法可能会重复计算F2两次甚至两次以上。

这一点对所有重复子问题都适用：愚蠢的做法可能会为重复计算已经解决的最优子问题的解而浪费时间。

为避免重复计算，可将已经得到的子问题的解保存起来，当我们要解决相同的子问题时，重用即可。该方法即所谓的memoization（ 记忆化 ,不是memorization）。当我们确信将不会再需要某一解时，可以将其抛弃，以节省空间。在某些情况下，我们甚至可以提前计算出那些将来会用到的子问题的解。

总括而言，动态规划利用：

 - 1) 重复子问题
 - 2) 最优子结构
 - 3) 缓存

动态规划通常采用以下两种方式中的一种两个办法：

 - **自顶向下**：将问题划分为若干子问题，求解这些子问题并保存结果以免重复计算。该方法将递归和缓存结合在一起。
 - **自下而上**：先行求解所有可能用到的子问题，然后用其构造更大问题的解。
 	- 该方法在节省堆栈空间和减少函数调用数量上略有优势，但有时想找出给定问题的所有子问题并不那么直观。

例子:

1. Fibonacci序列

```
#基于其数学定义的直接实现：

function fib(n)
   if n = 0 
       return 0
   else if n = 1
       return 1
   return fib(n-1) + fib(n-2)
```

 - 如果我们调用fib(5)，将产生一棵对于同一值重复计算多次的调用树：
 - 特别是，fib(2)计算了3次。在更大规模的例子中，还有更多fib的值被重复计算，将消耗**指数级**时间。

现在，假设我们有一个简单的**映射**（map）对象m，为每一个计算过的fib及其返回值建立映射，修改上面的函数fib，使用并不断更新m。新的函数将只需O(n)的时间，而非指数时间：

```
var m := map(0 → 1, 1 → 1)
function fib(n)
   if map m does not contain key n
       m[n] := fib(n-1) + fib(n-2)
   return m[n]
```

这一保存已计算出的数值的技术即被称为**缓存**，这儿使用的是**自顶向下**的方法：先将问题划分为若干子问题，然后计算和存储值。

在自下而上的方法中，我们先计算较小的fib，然后基于其计算更大的fib。这种方法也只花费线性（O(n)）时间，因为它包含一个n-1次的循环。

然而，这一方法只需要常数（O(1)）的空间，相反，自顶向下的方法则需要O(n)的空间来储存映射关系。

```
function fib(n)
   var previousFib := 0, currentFib := 1
   if n = 0 
       return 0
   else if n = 1
       return 1
   repeat n-1 times
       var newFib := previousFib + currentFib
       previousFib := currentFib
       currentFib  := newFib
   return currentFib
```

在这两个例子，我们都只计算fib(2)一次，然后用它来计算fib(3)和fib(4)，而不是每次都重新计算。


3. 棋盘

考虑n\*n的棋盘及成本函数C(i,j)，该函数返回方格(i,j)相关的成本。以5\*5的棋盘为例：

5 | 6 7 4 7 8
4 | 7 6 1 1 4
3 | 3 5 7 8 2
2 | 2 6 7 0 2
1 | 7 3 5 6 1
- + - - - - -
  | 1 2 3 4 5

可以看到：C(1,3)=5

从棋盘的任一方格的第一阶（即行）开始，寻找到达最后一阶的最短路径（使所有经过的方格的成本之和最小），假定只允许向左对角、右对角或垂直移动一格。

5 |
4 |
3 |
2 |   x x x
1 |     o
- + - - - - -
  | 1 2 3 4 5

该问题展示了最优子结构。即整个问题的全局解依赖于子问题的解。定义函数q(i,j)，令：q(i,j)表示到达方格(i,j)的最低成本。

如果我们可以求出第n阶所有方格的q(i,j)值，取其最小值并逆向该路径即可得到最短路径。

记q(i,j)为方格(i,j)至其下三个方格（(i-1,j-1)、(i-1,j)、(i-1,j+1)）最低成本 与c(i,j)之和，例如：

5 |
4 |     A
3 |   B C D
2 |
1 |
- + - - - - -
  | 1 2 3 4 5


```
q(A) = min(q(B),q(C),q(D)) + c(A)
```

定义q(i,j)的一般形式：

```
            |-  inf.                                                  j<1 or j>n , 棋盘外
q(i,j) =   -+-  c(i,j)                                                i=1 , 棋盘底行
            |-  min(q(i-1,j-1),q(i-1,j),q(i-1,j+1))+c(i,j)   		  otherwise.
```

 - 方程的第一行是为了保证递归可以退出（处理边界时只需调用一次递归函数）。
 - 第二行是第一阶的取值，作为计算的起点。
 - 第三行的递归是算法的重要组成部分，与例子A、B、C、D类似。


从该定义我们可以直接给出计算q(i,j)的简单的递归代码。在下面的伪代码中，n表示棋盘的维数，C(i,j)是成本函数，min()返回一组数的最小值：

```
function minCost(i, j)
    if j < 1 or j > n
        return infinity
    else if i = 1
        return c(i,j)
    else
        return min(minCost(i-1,j-1),minCost(i-1,j),minCost(i-1,j+1))+c(i,j)
```

 - 需要指出的是，minCost只计算路径成本，并不是最终的实际路径，二者相去不远。
 - 与Fibonacci数相似，由于花费大量时间重复计算相同的最短路径，这一方式慢的恐怖。
 	- 不过，如果采用自下而上法，使用二维数组q[i,j]代替函数minCost，将使计算过程快得多。

我们还需要知道实际路径。路径问题，我们可以通过另一个前任数组p[i,j]解决。这个数组用于描述路径，代码如下：

```
function computeShortestPathArrays()
     for x from 1 to n
         q[1, x] := c(1, x)
     for y from 1 to n
         q[y, 0]     := infinity
         q[y, n + 1] := infinity
     for y from 2 to n
         for x from 1 to n
             m := min(q[y-1, x-1], q[y-1, x], q[y-1, x+1])
             q[y, x] := m + c(y, x)
             if m = q[y-1, x-1]
                 p[y, x] := -1
             else if m = q[y-1, x]
                 p[y, x] :=  0
             else
                 p[y, x] :=  1

function computeShortestPath()
     computeShortestPathArrays()
     minIndex := 1
     min := q[n, 1] 
     for i from 2 to n 
         if q[n, i] < min
             minIndex := i
             min := q[n, i]
     printPath(n, minIndex)

function printPath(y, x)
     print(x)
     print("<-")
     if y = 2
         print(x + p[y, x])
     else
         printPath(y-1, x + p[y, x])                 
```



应用动态规划的算法:

1) 许多字符串操作算法如最长公共子列、最长递增子列、最长公共字串；

2) 将动态规划用于图的树分解，可以有效解决有界树宽图的生成树等许多与图相关的算法问题；

3) 决定是否及如何可以通过某一特定上下文无关文法产生给定字符串的Cocke-Younger-Kasami (CYK)算法；

4) 计算机国际象棋中转换表和驳斥表的使用；

5) Viterbi算法（用于隐式马尔可夫模型）；

6) Earley算法（一类图表分析器）；

7) Needleman-Wunsch及其他生物信息学中使用的算法，包括序列比对、结构比对、RNA结构预测；

8) Levenshtein距离（编辑距离）；

9) 弗洛伊德最短路径算法；

10) 连锁矩阵乘法次序优化；

11) 子集求和、背包问题和分治问题的伪多项式时间算法；

12) 计算两个时间序列全局距离的动态时间规整算法；

13) 关系型数据库的查询优化的Selinger（又名System R）算法；

14) 评价B样条曲线的De Boor算法；

15) 用于解决板球运动中断问题的Duckworth-Lewis方法；

16) 价值迭代法求解马尔可夫决策过程；

17) 一些图形图像边缘以下的选择方法，如“磁铁”选择工具在Photoshop；

18) 间隔调度；

19) 自动换行；

20) 巡回旅行商问题（又称邮差问题或货担郎问题）；

21) 分段最小二乘法；

22) 音乐信息检索跟踪。

