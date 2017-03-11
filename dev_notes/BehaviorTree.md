
# Behavior Tree

![](http://hi.csdn.net/attachment/201012/27/0_1293415268tlV4.gif)

> 为显美观：BT被横放，Node层次被刻意减少，Dec被刻意安插，Cond被刻意捏造。

>  PS：其实真正的高效的Node Group剔除应多加一层Sequence Node。


 - 4大类型的Node：
    - Composite Node
        - Selector Node
            - 逻辑或
        - Sequence Node
            - 逻辑与
        - Parallel Node
            - 并发执行它的所有Child Node。
            - 并行节点一般可以设定退出该节点的条件
            - 而向Parent Node返回的值和Parallel Node所采取的具体策略相关
            - 常见情况
                - (1)用于并行多棵Action子树。
                - (2)在Parallel Node下挂一棵子树，并挂上多个Condition Node，
            - Parallel Node增加性能和方便性的同时，也增加实现和维护复杂度。
    - Decorator Node
        - 将它的Child Node执行后返回的结果值 做 ***额外处理***后，再返回给它的Parent Node。
        - 比如Decorator Not/Decorator FailUtil/Decorator Counter/Decorator Time...
        - 更geek的有Decorator Log/Decorator Ani/Decorator Nothing...
    - \* Condition Node
        - 仅当满足Condition时返回True
    - \* Action Node 
        - 行为节点用来完成具体的操作，比如，移动到目标点，执行开火等代码逻辑，多种情况下行为节点会返回running和success；
        - 完成具体的一次(或一个step)的行为，视需求返回值。
        - 行为节点也可能会使用多帧来完成
        - 当行为需要分step/Node间进行时，可引入Blackboard进行简单数据交互
    - 只有Condition Node和Action Node才能成为Leaf Node
 - 节点的返回
    - 任何Node被执行后，必须向其Parent Node报告执行结果：成功 / 失败 / 运行中。
    - **运行中**：表示当前节点还在运行中，下一次调用行为树时任然运行当前节点；
    - **失败**：表示当前节点运行失败；
    - **成功**：表示当前节点运行成功；
 - 这简单的成功 / 失败汇报原则被很巧妙地用于控制整棵树的决策方向。
 - 几乎可以实现所有的决策控制：if, while, and, or, not, counter, time, random, weight random, util...

上面的Selector/Sequence准确来说是Liner Selector/Liner Sequence。 AI术语中称为strictly-order：按既定先后顺序迭代。

 - Selector和Sequence可以进一步提供非线性迭代的加权随机变种。AI术语中称为partial-order，能使AI避免总出现可预期的结果。
    - Weight Random Selector
    - Weight Random Sequence
 - 更强大的是可以加入Stimulus和Impulse，通过Precondition来判断masks开关。
    - Stimulus这类动态安插的Node 会破坏本来易于理解的静态性 
    - 原则就是保持全部Node静态，只是根据事件和环境来检查是否启用Node。


