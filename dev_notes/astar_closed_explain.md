# 2. 去掉 CLOSED 以后怎么办？

> Exported from ChatGPT on 2026-09-09T07:43:36.364Z

## Assistant

**不一定。**

但对于经典的 A* 图搜索（graph search），`closed` 通常是非常重要的；而对于 **A* 树搜索（tree search）**，则可以没有 `closed`。

关键区别在于：**搜索空间是树，还是图。**

### 1. A* Tree Search：可以没有 `closed`

最简单的 A*：

```
OPEN = priority queue
OPEN.push(start)

while OPEN:
    n = OPEN.pop_min_f()

    if n == goal:
        return path(n)

    for each successor m of n:
        OPEN.push(m)
```

这里没有 `closed`。

但是如果原问题是一个**图**，就会产生大量重复状态：

```
       A
      / \
     B   C
      \ /
       D
```

可能：

```
A -> B -> D
A -> C -> D
```

`D` 会被展开两次。

更糟糕的是，如果有环：

```
A -> B -> C
     ^    |
     |____|
```

就可能无限产生：

```
A B C B C B C ...
```

所以 **tree search 的代价通常非常高，甚至无法终止。**

---

### 2. A* Graph Search：通常需要 `closed`

Graph Search 会记录已经处理过的状态：

```
OPEN
CLOSED
```

大致：

```
OPEN = {start}
CLOSED = {}

while OPEN:
    n = pop_min_f(OPEN)

    if n == goal:
        return path(n)

    CLOSED.add(n)

    for m in successors(n):
        if m in CLOSED:
            continue

        ...
```

于是：

```
A -> B -> D
A -> C -> D
```

第二次遇到 `D` 时，可以发现：

```
D ∈ CLOSED
```

不用再展开。

所以 `closed` 的核心作用其实不是：

> “A* 必须有这个数据结构。”

而是：

> **防止重复扩展已经处理过的状态。**

---

### 3. 但这里有一个非常重要的细节

很多人学习 A* 时会形成一个错误印象：

> “一个节点进了 CLOSED，就永远不能再打开。”

**这个说法只有在 heuristic 满足一定条件时才成立。**

如果 `h` 是 **consistent（单调的）**：

h(n)≤c(n,m)+h(m)

那么 A* 有一个很漂亮的性质：

> 一个节点第一次从 OPEN 中取出来时，它的 `g` 已经是最优的。

因此：

```
pop n
↓
n -> CLOSED
↓
以后不用重新打开 n
```

这时候 `closed` 非常好用。

---

### 4. 如果 heuristic 只有 admissible，而不 consistent 呢？

这时候事情复杂一些。

`h` 可能满足：

h(n)≤h∗(n)

即 **admissible**，但不满足 consistent。

那么可能出现：

```
第一次发现 X
g(X) = 10

后来找到另一条路径
g(X) = 7
```

如果你简单地：

```
X ∈ CLOSED
=> 永远忽略
```

就可能丢掉最优解。

因此需要允许：

```
CLOSED
   ↓
发现更好的 g
   ↓
重新 OPEN X
```

这叫 **re-open**。

---

### 5. 所以可以把几种情况放在一起

| 算法 | closed | 重复状态 | 需要 reopen |
| --- | --- | --- | --- |
| A* Tree Search | ❌ | 可能大量重复 | — |
| A* Graph Search + consistent h | ✅ | 消除 | ❌ |
| A* Graph Search + admissible h | ✅ | 消除 | 可能需要 |
| Dijkstra | ✅ | 消除 | ❌ |
| BFS | ✅ | 消除 | ❌ |

实际上 Dijkstra 可以看成：

A∗with h(n)=0

而 `h=0` 显然是 consistent 的。

---

### 6. 还有一个更有意思的问题：`closed` 甚至不一定要单独存在

例如你可以维护：

```
unordered_map<State, Cost> best_g;
```

表示：

```
best_g[state] = 当前已知最小 g
```

当再次发现 `state`：

```
if (new_g >= best_g[state])
    ignore;
else
    update and push to OPEN;
```

这样实际上：

```
best_g
```

已经承担了相当一部分 `closed` 的功能。

所以从算法本质上说，A* 真正需要的是：

> **对已经发现/处理的 state 进行重复检测和代价管理**

而不是某个叫做 `closed` 的容器。

---

### 一句话总结

如果你问：

> **“A* 算法是不是必须有 closed？”**

答案是：

**不是。**

更准确地说：

> **A* Tree Search 不需要 `closed`；A* Graph Search 通常需要某种“已访问/最佳代价记录”机制来避免重复搜索。**

而如果你正在实现游戏里的 A*，通常就是：

```
OPEN   = priority_queue
CLOSED = set
```

这是最经典、最容易正确实现的版本。

如果你愿意，我还可以进一步解释一个**非常容易混淆的问题：为什么有些 A* 实现甚至可以完全不需要 CLOSED，只靠 `gScore + priority_queue`，以及它和 Dijkstra 的关系**。

## User

为什么有些 A* 实现甚至可以完全不需要 CLOSED，只靠 `gScore + priority_queue`

## Assistant

因为 **`CLOSED` 的真正作用不是“记住访问过谁”，而是“防止同一个 state 被重复处理”**。

而 `gScore` 本身就可以承担这个职责的一部分。

核心思路是：

```
gScore[state] = 我目前知道的到达 state 的最小代价
```

于是，不需要：

```
CLOSED = {A, B, C, ...}
```

而是每次发现一个状态时判断：

```
new_g >= gScore[state]
    → 没必要处理

new_g < gScore[state]
    → 找到更好的路径，重新放进 OPEN
```

---

## 1. 先看经典 CLOSED 版本

比如：

```
OPEN     = priority_queue
CLOSED   = set
gScore   = map
```

伪代码：

```
while (!open.empty()) {
    Node n = open.pop();

    if (n.state == goal)
        return path;

    if (closed.contains(n.state))
        continue;

    closed.insert(n.state);

    for (auto next : neighbors(n)) {
        if (closed.contains(next))
            continue;

        new_g = n.g + cost(n, next);

        if (new_g < gScore[next]) {
            gScore[next] = new_g;
            open.push(next);
        }
    }
}
```

这里：

```
CLOSED
```

解决的是：

> “这个 state 我已经展开过了。”

而：

```
gScore
```

解决的是：

> “到这个 state，目前最好的代价是多少？”

---

# 2. 去掉 CLOSED 以后怎么办？

可以变成：

```
gScore[start] = 0;
open.push(start);

while (!open.empty()) {
    Node n = open.pop();

    if (n.state == goal)
        return path;

    for (auto next : neighbors(n)) {
        new_g = n.g + cost(n, next);

        if (new_g < gScore[next]) {
            gScore[next] = new_g;
            open.push(next);
        }
    }
}
```

注意一个非常关键的地方：

**同一个 state 可以在 priority_queue 里面出现多次。**

例如：

```
第一次发现 A:
gScore[A] = 10
push(A, g=10)

后来发现更好的路径:
gScore[A] = 5
push(A, g=5)
```

于是 priority queue：

```
(A, g=5)
(A, g=10)
```

都有。

这看起来好像有问题。

---

# 3. 关键技巧：pop 时检查是不是“过期节点”

这就是这种实现最核心的地方：

```
Node n = open.pop();

if (n.g != gScore[n.state])
    continue;
```

也就是说：

```
priority_queue:
    A(g=5)
    A(g=10)

gScore[A] = 5
```

先 pop：

```
A(g=5)

5 == gScore[A]
→ 有效
→ 展开
```

以后再 pop：

```
A(g=10)

10 != gScore[A]
→ 这是旧记录
→ 丢掉
```

所以：

> **priority_queue 里面允许存在重复节点，但 `gScore` 保证只有最新的最佳版本有效。**

这就是所谓的 **lazy deletion（延迟删除）**。

---

# 4. 这其实非常像 Dijkstra

Dijkstra 的很多实现也是这么干的。

例如：

```
priority_queue<pair<int, Node>> pq;
vector<int> dist;

dist[start] = 0;
pq.push({0, start});

while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();

    if (d != dist[u])
        continue;

    for (auto [v, cost] : graph[u]) {
        int nd = d + cost;

        if (nd < dist[v]) {
            dist[v] = nd;
            pq.push({nd, v});
        }
    }
}
```

你会发现：

**根本没有 CLOSED。**

但是算法依然正确。

因为：

```
dist[v]
```

承担了：

> 当前已知最优距离

而：

```
if (d != dist[u])
    continue;
```

承担了：

> 丢弃旧版本

---

# 5. A* 完全可以照搬这个思想

把 Dijkstra：

```
priority = g
```

换成 A*：

```
priority = g + h
```

就是：

```
priority_queue<Node> open;

gScore[start] = 0;
open.push({
    start,
    0,
    heuristic(start)
});

while (!open.empty()) {
    Node n = open.pop();

    // 丢弃旧版本
    if (n.g != gScore[n.state])
        continue;

    if (n.state == goal)
        return reconstruct_path(n);

    for (auto next : neighbors(n)) {
        double new_g =
            n.g + cost(n.state, next);

        if (new_g < gScore[next]) {
            gScore[next] = new_g;

            open.push({
                next,
                new_g,
                new_g + heuristic(next)
            });
        }
    }
}
```

这里完全没有：

```
CLOSED
```

---

# 6. 那它和 CLOSED 版本有什么区别？

这是非常值得理解的地方。

假设：

```
S
├── A
│   └── X
└── B
    └── X
```

可能先找到：

```
S -> A -> X
g(X) = 10
```

于是：

```
gScore[X] = 10
OPEN = X(10)
```

后来发现：

```
S -> B -> X
g(X) = 7
```

于是：

```
gScore[X] = 7

OPEN:
    X(7)
    X(10)   ← 老版本
```

pop：

```
X(7)
```

处理。

之后：

```
X(10)
```

再次出来：

```
if (10 != gScore[X])
    continue;
```

直接扔掉。

所以：

```
CLOSED 版本
────────────────
物理上避免重复进入 OPEN / CLOSED

gScore 版本
────────────────
允许重复进入 OPEN
但旧版本 pop 出来时扔掉
```

---

# 7. 那为什么还要 CLOSED？

因为两种方式各有优缺点。

### CLOSED 版本

```
OPEN
 ↓
pop X
 ↓
CLOSED.add(X)
 ↓
以后遇到 X
 ↓
直接跳过
```

优点：

- OPEN 更干净
- 不会积累大量旧节点
- 通常节省内存
- 在 consistent heuristic 下非常自然

缺点：

- 需要维护 CLOSED
- priority queue 往往不支持 decrease-key
- 实现上仍然需要 `gScore`

---

### gScore + lazy deletion

```
OPEN:
    X(g=7)
    X(g=10)
    X(g=13)
```

只保证：

```
gScore[X] = 7
```

所以：

```
X(7)   → 处理
X(10)  → 丢弃
X(13)  → 丢弃
```

优点：

- **代码非常简单**
- 不需要 decrease-key
- 不需要 CLOSED
- 找到更好路径时直接 push
- 特别适合 C++ `std::priority_queue`

缺点：

- OPEN 可能有很多重复/过期节点
- 最坏情况下内存和运行时间可能增加

---

# 8. 更重要的是：它还能自然支持“重新打开”

这也是我认为这个实现非常漂亮的地方。

假设 heuristic **不 consistent**。

可能：

```
X 第一次被处理

g(X) = 10
```

后来：

```
发现更好的路径

g(X) = 7
```

怎么办？

CLOSED 的朴素实现可能：

```
if (closed.contains(X))
    continue;
```

于是：

```
X 已经 CLOSED
→ 忽略
```

这可能破坏最优性。

而 `gScore + priority_queue` 的实现：

```
if (new_g < gScore[X]) {
    gScore[X] = new_g;
    open.push(X);
}
```

非常自然：

```
X(g=10)
    ↓
发现 X(g=7)
    ↓
重新 push X
```

因此它天然支持：

> **reopen / re-expansion**

---

# 9. 但是有一个坑：不能只写 `gScore` 而不检查旧节点

错误写法：

```
while (!open.empty()) {
    auto n = open.top();
    open.pop();

    for (auto next : neighbors(n)) {
        ...
    }
}
```

因为：

```
OPEN:
    X(g=5)
    X(g=10)
```

当 `X(g=5)` 更新：

```
gScore[X] = 5
```

之后 `X(g=10)` 还是在 queue 里面。

如果不检查：

```
if (n.g != gScore[n.state])
    continue;
```

那么旧版本还会被重新展开。

这时候你实际上又退化成了：

> 大量重复搜索。

所以这句非常关键：

```
if (n.g != gScore[n.state])
    continue;
```

---

# 10. 最终可以这样理解

A* 并不是非得：

```
OPEN + CLOSED
```

它真正需要的是两个概念：

```
OPEN
    ↓
哪些候选节点还需要处理？

BEST-G
    ↓
到每个 state，目前知道的最好代价是多少？
```

因此可以有两种实现：

### 显式去重

```
OPEN + CLOSED + gScore
```

```
发现 state
    ↓
CLOSED？
    ↓
否
    ↓
更新 gScore
    ↓
OPEN
```

### 延迟去重

```
OPEN + gScore
```

```
发现更好路径
    ↓
直接 push
    ↓
允许 OPEN 中出现重复 state
    ↓
pop 时检查 g 是否仍然等于 gScore
    ↓
否则丢弃
```

所以一句话：

> **`CLOSED` 是一种“主动删除重复搜索”的策略；`gScore + priority_queue` 是一种“允许重复，但在 pop 时惰性删除旧版本”的策略。**

这也是为什么在 C++ 里你经常会看到 A* 写成：

```
priority_queue<Node> open;
unordered_map<State, Cost> gScore;
```

却完全没有：

```
unordered_set<State> closed;
```

**它不是没有 CLOSED 的功能，而是把“CLOSED 的一部分职责”变成了 lazy deletion。**

## User

一个2d map， 每次可以上下左右移动 1格， 每个cell 有 移动cost : 1~3,  h(x) 怎么设计，才能保证 admissible consistant ?

## Assistant

可以，而且这个问题其实非常漂亮。假设：

- 只能 **上下左右**走
- 每次移动 1 格
- 每个 cell 的进入 cost 为 `1~3`
- 目标是 `goal`
- `g(n)` 是从 start 到 n 的实际 cost
- `h(n)` 估计 n 到 goal 的剩余 cost

那么一个非常好的选择是：

h(n)=ManhattanDistance(n,goal)×1​

也就是：

h(n)=∣x−xg​∣+∣y−yg​∣​

这个 `h` **同时满足 admissible 和 consistent**。

---

## 1. 为什么 admissible？

假设：

```
cell cost ∈ {1,2,3}
```

那么任何一步移动至少需要：

1

而从 `(x,y)` 到 goal 至少需要：

∣x−xg​∣+∣y−yg​∣

步。

所以真实最小代价至少是：

∣x−xg​∣+∣y−yg​∣

因此：

h(n)≤h∗(n)

所以 **admissible**。

---

## 2. 为什么 consistent？

consistent 要求对于任意相邻节点 `n -> m`：

h(n)≤c(n,m)+h(m)

因为：

```
h(n) = Manhattan(n, goal)
h(m) = Manhattan(m, goal)
```

而 n 和 m 只差一格，所以 Manhattan distance 最多变化 1：

h(n)≤h(m)+1

又因为：

c(n,m)≥1

所以：

h(n)≤h(m)+1≤h(m)+c(n,m)

因此：

h(n)≤c(n,m)+h(m)​

所以 **consistent**。

---

# 3. 这里有一个容易犯的错误

你可能会想：

> 每个 cell cost 是 1~3，那是不是可以用 Manhattan × 3？

比如：

h(n)=3×Manhattan(n,goal)

这个 **不一定 admissible**。

例如：

```
S . . G
```

每格 cost 都是 `1`：

```
S -> . -> . -> G
  1    1    1
```

真实 cost：

3

但是：

h(S)=3×3=9

显然：

9>3

所以 **不 admissible**。

---

# 4. 为什么应该乘最小 cost？

一般规律非常值得记住：

如果：

- 每一步距离是 1
- 最低移动 cost 是 `Cmin`

那么：

h(n)=Cmin​×Manhattan(n,goal)​

就是一个天然的 admissible + consistent heuristic。

你的情况：

Cmin​=1

所以：

h(n)=∣dx∣+∣dy∣​

---

# 5. 但是还有一个更有意思的问题

如果 **cost 是 cell-specific 的**，例如：

```
1 1 3 3
1 3 3 1
1 1 1 1
```

那么单纯：

Manhattan

虽然一定 admissible + consistent，但可能比较弱。

例如：

```
S . . . G
```

如果中间全是：

```
3 3 3
```

那么真实最优 cost 可能是：

12

而 Manhattan heuristic 只有：

4

A* 得不到多少信息。

---

# 6. 能不能设计一个更强的 heuristic？

可以。

一个非常重要的思路是：

> **只要你的 heuristic 是某个“放宽后的问题”的真实最短距离，它就天然 admissible；如果这个放宽后的问题满足边权条件，通常还能得到 consistent。**

例如你的原问题：

```
每个 cell 有 cost = 1~3
```

可以构造一个 relaxed problem：

```
所有 cell cost 都变成 1
```

那么 relaxed problem 的最短距离就是：

h1​(n)=Manhattan(n,goal)

这是刚才的 heuristic。

---

## 7. 甚至可以做得更强

假设地图非常大，而且 cell cost 已知：

```
1 1 1 3 3
1 1 2 3 3
1 2 2 3 3
1 1 1 1 1
```

你可以预先从 goal 跑一次 Dijkstra：

```
         Dijkstra
            ↓
       distance-to-goal
            ↓
          h(x)
```

得到：

h(n)=从 n 到 goal 的真实最短 cost

那么这个 h 是：

admissible​

而且：

consistent​

甚至它是**最强的 admissible heuristic**——因为它就是实际的最优剩余 cost。

当然，这样做的代价是：

> 你已经提前把 A* 要解决的问题算了一遍。

所以通常只有在：

- goal 固定
- start 经常变化

的时候才特别有价值。

---

# 8. 对游戏地图来说，我会这样选

如果你的地图是：

```
上下左右
cost = 1~3
```

推荐第一版直接：

```
int h(Cell a, Cell goal)
{
    return abs(a.x - goal.x)
         + abs(a.y - goal.y);
}
```

然后：

```
f(n) = g(n) + h(n)
```

这会保证：

```
             admissible   consistent
Manhattan       ✅            ✅
3*Manhattan     ❌            ❌
0               ✅            ✅
真实最短距离     ✅            ✅
```

而且由于 heuristic consistent，你的 A* 可以放心采用：

```
pop node
    ↓
第一次 pop 到这个 node
    ↓
它的 g 已经是最优
    ↓
不需要 reopen
```

这也是你上一问 **`CLOSED` 是否必须** 和这一问直接连接起来的地方。

**对于这个具体问题，`h = Manhattan` 是 consistent 的，因此如果你使用 graph-search A*，第一次从 OPEN 取出一个节点时，它的 `gScore` 就已经确定，不需要重新打开 CLOSED 节点。**
