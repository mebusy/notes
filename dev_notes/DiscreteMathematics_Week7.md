...menustart

 - [Week7 图论：图的基本概念](#2395231edf36e5039544b0ff32dfbcd6)
	 - [59-图的基本概念](#c72241c336cc83688b59638f1ce7d521)
	 - [60-度和正则图](#a556333847a1e198e8e313a93a2ecaa3)
		 - [度的性质](#ec2264e6c89787f143f062b0b8518ca7)
		 - [正则图(regular graph)](#90401b1637506dd0eabebab0d43452bd)
	 - [61-子图与同构图](#823db5dc3228079d2354279e0ee07b96)
		 - [子图(subgraph)](#10a5ed833580ee167772eadbee35e740)
		 - [补图](#3d3bdd17a604c34365265a19998d72cc)
		 - [图的同构isomorphic](#c5c929b91e4d9c87cdeb99ee9f933c36)
	 - [62-路径与连通性](#e6cea5afff7ebe29924e99d4127bfa8b)
		 - [路径(walk)与通路(path)](#68bb89fa2906f9f194cc6af28b91644f)
		 - [路径与通路性质](#4850226f851afaa48ab40b4270c688a5)
	 - [63-连通性](#3ce807b22a4f826b37a34d33420a8830)
	 - [64-欧拉图与哈密顿图](#9122a3fbef09ec56dd71bf7e4cf62c86)
		 - [欧拉图及欧拉路径](#071be4eb1c3465c38ad26a65fa7c4500)
		 - [充分必要条件](#933216666c6971429c73d387052fdb7d)
		 - [欧拉图和“一笔画”问题](#687ec58c2e5ea962d2efa3585b944d1c)
		 - [哈密顿图及哈密顿通路](#4d0065ecd4038a137fd5b9eb0c974726)
		 - [判定定理（充分非必要）](#5d8ce86995120655606a7837df8aa56b)
 - [Week8: 图论：特殊图](#229beda3d10ce35081515ebaa08f6afd)

...menuend


<h2 id="2395231edf36e5039544b0ff32dfbcd6"></h2>

# Week7 图论：图的基本概念

<h2 id="c72241c336cc83688b59638f1ce7d521"></h2>

## 59-图的基本概念

 - 简单图simple graph：无环和重边的图
    - 以后讨论的基本都是 简单图
 - 完全图complete graph：任何两个不同结点间都有边关联的简单图，记做Kn
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_complete_graph.png)
    - n 是顶点数
    - 无向完全图 边数: n(n-1)/2
    - 有向完全图 变数: n(n-1)
 - 赋权图 
    - 赋权图G=<V,E,f,g>
    - **结点权**函数：f:V→W
    - **边权**函数：g:E→W
    - W可以是任何集合，常为实数的子集 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_weighted_graph.png)


<h2 id="a556333847a1e198e8e313a93a2ecaa3"></h2>

## 60-度和正则图

 - 端点v的度d(v)定义为关联端点v的边的数目
 - 有向图中，度分为出度(out-degree)和入度 (in-degree)
    - 出度d+(v)
    - 入度d-(v)
    - d(v)=d+(v)+d-(v)
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_degree.png)
    - d(c) = 5


<h2 id="ec2264e6c89787f143f062b0b8518ca7"></h2>

### 度的性质

 - 所有端点 度的总和为**偶数**，而且是边数目的 **两倍**
 - 有向图中出度的总和等于入度的总和
 - **奇数度** 结点必为 **偶数**个（反证法可证）
 - 自然数序列(a1 ,a2 ,…an)是某个图的度序列 当且仅当序列中所有数的总和为偶数
    - 如果你有一个序列， 它的所有的数的总和是一个偶数的话，那么我们就可以，必然可以依据它这个度序列， 来做出一个图来，可以对应一个图。
    - 反过来也是一样
 - 1 度的顶点称为**悬挂点**(pendant node) 


<h2 id="90401b1637506dd0eabebab0d43452bd"></h2>

### 正则图(regular graph)

 - 所有顶点的度均相同的图称为**正则图**，按照 顶点的度数k称作**k-正则图**
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_regular_graph.png)
    - 1st one is 3-正则图
    - 2nd one is 2-正则图
    - last one is 4-正则图 
 - K<sub>n</sub> 是n-1正则图 
    - last one is complete graph K₅
    - 对于每一个完全图来说，它肯定都是一个正则图

<h2 id="823db5dc3228079d2354279e0ee07b96"></h2>

## 61-子图与同构图

<h2 id="10a5ed833580ee167772eadbee35e740"></h2>

### 子图(subgraph)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_subgraph.png)

 - G1=<V1 ,E1>, G2=<V2 ,E2> 
    - V1 ⊆ V2 , E1 ⊆ E2，称G1是G2的**子图**
    - 如果G1≠G2，则G1是G2的**真子图**
 - 生成子图spanning subgraph
    - 如果G1是G2的子图，且V1=V2
    - G1 只是少了若干条 边
    - 红图 是 蓝图的spanning subgraph 

<h2 id="3d3bdd17a604c34365265a19998d72cc"></h2>

### 补图

 - G1 ,G2互为补图：
    - V1=V2 , E1∩E2=∅ ,  <V1 ,E1∪E2>是完全图 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_Complement_graph.png)

<h2 id="c5c929b91e4d9c87cdeb99ee9f933c36"></h2>

### 图的同构isomorphic

 - G1=<V1 ,E1>, G2=<V2 ,E2>
    - |V1 |=|V2 |, |E1 |=|E2 | 
        - 顶点的个数和边的条数， 要一致
    - 如果可以将V1中所有的结点一一对应地置 换为V2中的结点名后得到的图等于G2
        - 在存在一个双射函数，它把这个V1映射为V2，同时 把E1变成E2
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_isomorphic_graph.png)
    - 把这个五角星 的这个顶点啊，最顶上这个顶点 最上面的顶点把它挪，挪到最下方。 然后把这个左边这个顶点，挪，挪到右下方的话，我们就会发现，如果经过这样的一个操作， 移动或者说叫做置换的话，那么它就会变成一个五边形了。 
 - 不同构的图：化学中的同分异构体
    - 分子式相同而结构和性质不同的化合物之间 互称同分异构体


 - 无向完全图 K3的不同构的生成子图有: 3 个

<h2 id="e6cea5afff7ebe29924e99d4127bfa8b"></h2>

## 62-路径与连通性

<h2 id="68bb89fa2906f9f194cc6af28b91644f"></h2>

### 路径(walk)与通路(path)
 
 - 顶点v1到vl的拟路径： v1 ,e1 ,v2 ,e2 ,v3 ,…,vl-1,el-1,v 
 
 - 如果拟路径中的边各不相同，称作**路径**
 - 如果路径中的顶点各不相同，称作**通路**
    - 不能够允许包含相同的顶点
 - v1=vl 的路径称为**闭路径**
 - v1=vl 的通路称作**回路**


<h2 id="4850226f851afaa48ab40b4270c688a5"></h2>

### 路径与通路性质

 - **路径和通路定理**
    - 在有n个顶点的图G中，如果有顶点u到v的 拟路径，那么u到v必有**路径**，并且必有长度**不大于n-1的通路**
    - (考虑拟路径中重复顶点的压缩)
 - **闭路径和回路定理**
    - 在有n个顶点的图G中，如果有顶点v到v的 闭路径，那么必定有一条从v到v的长度不大于n的**回路**


<h2 id="3ce807b22a4f826b37a34d33420a8830"></h2>

## 63-连通性

 - u**可达**v(accessible)
    - u=v，或者存在一条u到v的路径
 - **连通**的**无向图**connected
    - 无向图中**任意**两个顶点都是**可达**的
 - **强连通**的**有向图**
    - 有向图中**任意**两个顶点都是**互相可达**的
    - u可达v , v可达u 
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_connected_graph.png)
 - **单向连通**的**有向图**
    - **任意**两个顶点，**至少**从一个顶点到另一个是 **可达**的
 - **弱连通**的**有向图**
    - 将有向图**看作无向图**时是连通的 (右下角图)
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_weak_connected_graph.png)

 - 连通分支（connected component）
    - 图G的**连通子图**G'，而且G'不是任何其它连通子图的真子图（**最大性**）
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_connect_component.png)

<h2 id="9122a3fbef09ec56dd71bf7e4cf62c86"></h2>

## 64-欧拉图与哈密顿图

<h2 id="071be4eb1c3465c38ad26a65fa7c4500"></h2>

### 欧拉图及欧拉路径

 - 欧拉图Euler graph
    - 如果图G上有一条经过**所有顶点**、**所有边**的 闭路径（边不重复，允许顶点重复）
 - 欧拉路径Euler walk
    - 如果说，没有这么一条 闭路径， 那么有路径也好
    - 如果图G上有一条经过**所有顶点**、**所有边**的 路径（边不重复，允许顶点重复）

<h2 id="933216666c6971429c73d387052fdb7d"></h2>

### 充分必要条件

 - 欧拉图
    - 无向图：G连通，**所有**顶点的度都是**偶数**
    - 有向图：G弱连通，每个顶点的出度与入度**相等**
 - 欧拉路径
    - 无向图：G连通，恰有**两个**顶点的度是**奇数**
    - 有向图：G连通，恰有两个**顶点**出度与入度 不相等，其中一个出度比入度多1，另一个 入度比出度多1


<h2 id="687ec58c2e5ea962d2efa3585b944d1c"></h2>

### 欧拉图和“一笔画”问题

 - 是否存在 这样一个 欧拉图 ， 或 欧拉路径

<h2 id="4d0065ecd4038a137fd5b9eb0c974726"></h2>

### 哈密顿图及哈密顿通路

 - 哈密顿图Hamilton graph
    - 产生于一个游戏，只经过每个大城市1次，周游世界
    - 如果图G上有一条经过**所有**顶点的回路（不要求经过所有边，也称作哈密顿回路）
    - 回路： 不允许顶点重复
 - 哈密顿通路Hamilton path
    - 如果图G上有一条经过所有顶点的通路（非回路）
    
![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/DM_graph_hamilton_graph.png)

 - 哈密顿图 比 欧拉图 难度大很多

<h2 id="5d8ce86995120655606a7837df8aa56b"></h2>

### 判定定理（充分非必要）

 - 如果具有n个顶点的图G的每一对顶点的度数之和都不小于n-1，那么G中有一条哈密顿通路
 - 如果G的每一对顶点度数之和不小于n，且 n>=3，则G为一哈密顿图
 - 哈密顿通路问题在上个世纪七十年代被证明 是“NP完全的”（算法时间随顶点个数呈 指数增长）
 - 实际上对于某些顶点数不到**100**的网络，利 用现有最好的算法和计算机也需要比较荒唐 的时间（比如**几百年**）才能确定其是否存在 一条这样的路径。

---

<h2 id="229beda3d10ce35081515ebaa08f6afd"></h2>

# Week8: 图论：特殊图





