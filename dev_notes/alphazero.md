# AlphaGo Zero - How and Why it Works

http://tim.hibal.org/blog/alpha-zero-how-and-why-it-works/

## Monte Carlo Tree Search

 - The go-to algorithm for writing bots to play **discrete**, **deterministic** games with **perfect information** is **Monte Carlo tree search (MCTS)**.
    - discrete: individually separate and distinct moves and positions
    - deterministic: every move has a set outcome
    - games: players competing against one another
    - perfect information: both players see everything
 - The algorithm works as follows. 
    - The game-in-progress is in an initial state s₀ , and it's the bot's turn.
        - The bot can choose from a set of actions A.
        - Monte Carlo tree search begins with a tree consisting of a single node for s₀.
            - This node is **expanded** by trying every actiona∈A and constructing a corresponding child node for each action.
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac1.png)
    - The value of each new child node must then be determined (现在就必须确定每个child node的值？).
        - The game in the child node is *rolled out* by **randomly** taking moves from the child state until a win, loss, or tie is reached.
        - Wins are scored at +1, losses at −1, and ties at 0. 
        - for example
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac2.png)
        - The random rollout for the first child s<sub>0,1</sub> given above estimates a value of +1.
        - This value may not represent optimal play.
        - One can often do better by following a better strategy, or by estimating the value of the state directly. ( though still typically random )
        - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac3.png)
    - Above we show the expanded tree with approximate values for each child node.
        - Note that we store two properties:
            - the accumulated value W 
            - and the number of times rollouts have been run at or below that node,  N
        - The information from the child nodes is then **propagated back** up the tree by increasing the parent's value and visit count. 
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac4.png)     
        - Monte Carlo tree search continues for multiple iterations , consisting of 
            - selecting a node, expanding it, and propagating back up the new information.
    - Monte Carlo tree search does not expand all leaf nodes, as that would be very expensive.
        - Instead, the selection process chooses nodes that strike a balance between 
            - being lucrative 有利的
            - having high estimated values 高评估值
            - being relatively unexplored 没访问过的 
            - and having low visit counts 较低的访问次数
        - A leaf node is selected by traversing down the tree from the root node (从根节点向下遍历树来选择子节点),
            - always choosing the child i with the highest upper confidence tree (UCT) score:
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_UTCscore.png)
            - where Wi is the accumulated value of the ith child, 
                - Ni is the visit count for ith child, 
                - and Np is the number of visit counts for the parent node.
            - The parameter c≥0 controls the tradeoff between 
                - choosing lucrative nodes (low c) 
                - and exploring nodes with low visit counts (high c).
            - c is often set empirically.
        - The UCT scores (U's) for the tic-tac-toe tree with c=1 are:
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac5.png)
            - In this case we pick the first node, s<sub>0,1</sub>. (如果出现多个第一，可以随机选取，或选择第一个child)
        - That node is expanded and the values are propagated back up:
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac6.png)  
            - s₀,s<sub>0,1</sub> 的 N,W 分别都增加了 4,3
        - Note that each accumulated value W reflects whether **X**'s won or lost.
            - During selection, we keep track of whether it is X's or O's turn to move, and flip the sign of W whenever it is **O**'s turn.
    - We continue to run iterations of Monte Carlo tree search until we run out of time. 
        - The tree is gradually expanded and we (hopefully) explore the possible moves, identifying the best move to take. 
        - The bot then actually , in real game ,  makes a move by picking the first child with the highest number of visits(访问次数最多的). 
        - For example, if the top of our tree looks like:
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/mcts_tictac7.png)  





        

 


