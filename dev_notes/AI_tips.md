...menustart

- [A star](#e434d837aebd935bbf88f6f573c57e56)
    - [big map](#142f4b1b69989d6d579c3a9c94bfdfae)
- [NavMesh](#a77459f60fc906f0bb8c45c3d4a2cf6a)
    - [寻找凸多边形](#b29122b479fe87cc8a8c0ec9302c471d)

...menuend


<h2 id="e434d837aebd935bbf88f6f573c57e56"></h2>


# A star

 - quick path
    - depth-limited path to destination
 - time-sliced full path
    - from end point of quick path , to destination
 - splice path 
    - maybe the node in full-path[:n] , which has the shortest distance to current position of Agent.

<h2 id="142f4b1b69989d6d579c3a9c94bfdfae"></h2>


## big map

 - divide map into small pieces
    - 每个节点 表示 游戏世界中的 某个位置
 - compute solution table: all-pairs shortest path
    - 保存任意两节点间的 最短路径
    - 或 只保存 任意两节点间的 cost


 - 只考虑静止的物理特征，不包括 运行时刻会移动或改变的障碍物    
 - 分层路径搜索


---

<h2 id="a77459f60fc906f0bb8c45c3d4a2cf6a"></h2>


# NavMesh

 - 3D环境中最强大的AI路径搜索技术之一
 - 和其他 precomputed 路径搜索数据结构一样，NavMesh 只知道游戏中静态的部分。所以必须分层进行路径搜索，以便处理动态障碍物
 - 另外一个受欢迎的3D场景路径搜索算法，叫 路径栅格 path lattice, ( or  points of visibility  ), 但是局限性很大

---

 - NavMesh 是一个 凸多边形 convex polygon 集合
    - convex polygon 确保 agent 能沿单一直线从 改多边形一个点到另一个点
    
<h2 id="b29122b479fe87cc8a8c0ec9302c471d"></h2>


##  寻找凸多边形

 - optimal convex partition problem
    - 最优凸集划分
 - 
