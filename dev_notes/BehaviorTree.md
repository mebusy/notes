...menustart

- [Behavior Tree](#65960f0506f5463f2851a8de00e13354)
- [Source code of BTSK](#ffdbc3c1ec6e7d5a3ebd35c186cd29bc)
    - [Spearate Out Behaviors](#8e7d1bb4b23679d03820f8aade337c40)
    - [Part 2.a  DATA-ORIENTED BT](#c78c9cd9849639c586dee4874cbd56ce)
    - [Event-Driven BT](#34ee2906f2c05f35040b98dcaf55ab4f)
    - [What's Next](#ad5480f838ed67e92fecf7af3cef120d)

...menuend


<h2 id="65960f0506f5463f2851a8de00e13354"></h2>


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
        - 将它的Child Node执行后返回的结果值 做 **额外处理**后，再返回给它的Parent Node。
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

<h2 id="ffdbc3c1ec6e7d5a3ebd35c186cd29bc"></h2>


# Source code of BTSK

 - `class Behavior`  , base class for actions, conditions, and composites
    - update() 
        - which is called every frame 
    - onInitialize() 
        - which is called only the first time before the update function called
    - onTerminate(status) 
        - called once the update is finished , and we'll pass status to
    - so this is pretty standard interface as most of you the state machine might be familiar with but the big difference between them is the `Status`
        - the state machine doesn't have a return `Status`, it doesn't know whether it succeeded of failed 
        - but in the behavior tree you know about that.
 - `enum Status` 
    - BH_INVALILD
    - BH_SUCCESS
    - BH_FAILURE
    - BH_RUNNINg
 - `Behavior::tick` : 
    - a helper wraper function that helps make sure that we call all our functions correctly things like `onInitialize` , `update` ...
        - if mStatus == BH_INVALID , call onInitialize 
        - mStatus = update()
        - if mStatus != BH_RUNNING , call onTerminate( mStatus )
        - return mStatus 
 - `struct MockBehavior : public Behavior`
    - it is in fact a test file so everything is unit tested and that is another tip that I will give you is that you should be really only testing all of your behavior tree. 
    - it have measuring the number of times each function is called and capturing what the behavior returns and forcing a certain weight of status 

---

 - 2 main 'Composite' nodes
    - Sequences     , i.e. fixed list of statements
    - Selectors     , i.e. conditional branching
 - It's a powerful concept...
    - you can build most trees with these nodes 
    - Thye are the most commonly used nodes

---

 - `class Composite : public Behavior`
 - `class Sequence : public Composite`
    - onInitialized 
        - mCurrentChild = mChildren.begin()
    - update 

```
    - while true
        - Status s = mCurrentChild.tick()
        - if s != BH_SUCCESS  , return s ;
        - if ++mCurrentChild == mChildren.end() ,  return BH_SUCCESS 
    - return BH_INVALID    , this is unexpected loop exit
```

 - `class Selector : public Composite`
    - update

```
    - whle true
        - Status s = mCurrentChild.tick()
        - if s != BH_FAILURE  , return s ;
        - if ++mCurrentChild == mChildren.end() ,  return BH_FAILURE
    - return BH_INVALID     
```

 - Memory Problems ?
    - With the 1st implementation, you need a completely new tree for each NPC !

---

<h2 id="8e7d1bb4b23679d03820f8aade337c40"></h2>


## Spearate Out Behaviors

 - Nodes
    - Common data shared by all instances
    - The Basic structure of the tree
    - All parameters and other configuration
 - Tasks
    - Runtime instance-specifc data.
    - Current pointers, counters ,etc

---

 - `class Node` 
    - `Task* create()`
    - `void destory(Task*)`
 - `class Task` 
    - very similar to a behavior , has update/onInitialize/onTerminate
    - constructor: `Task(Node& node)`
    - `Node* m_pNode;`
 - `class Behavior`
    - `Task* m_pTask`
    - `Node* m_pNode`
    - `Status m_eStatus`
    - tick()
        - almost same as 1st version,  the difference is call update/onInitialize/onTerminate on Task instead
    - get()
        - return Task ( it is a template class Task )
        - you don't necessarily need , this is just for the tests

```c++
// test
MockNode n;                              
Behavior b(n);

MockTask* t = b.get<MockTask>();
CHECK_EQUAL(0, t->m_iInitializeCalled);

b.tick();
CHECK_EQUAL(1, t->m_iInitializeCalled);
```

 - `class Composite : public Node`
    - `Nodes m_Children`
 - `class Sequence : public Task`
    
---

 - Disadvantages
    - It's entirely based on poolling
    - There's a whole chain of virtual calls
    - A lot of memory gets touched each traversal 
    - The maximum stack size depends on data

---

**Principles** : Write a specialized "interpreter" that can process behavior trees better than C++.

<h2 id="c78c9cd9849639c586dee4874cbd56ce"></h2>


## Part 2.a  DATA-ORIENTED BT

 - Memory Allocation
    - The Policy
        - Use a stack allocator for the whole BT
        - Allocate each node contiguously
        - Using depth-first order as default
        - Child nodes come after their parent
    - Motivation
        - Keeps cache misses low, etc.
 - bt3
 - `class BehaviorTree`
    - all the nodes inside there will be allocated one by one in memory
 - Node Indexing
    - The Policy
        - Don't rely on pointers anymore
        - Use indexes or relative offsets
        - for composites, easily find children after
    - Motivation
        - Reduce memory consumption

<h2 id="34ee2906f2c05f35040b98dcaf55ab4f"></h2>


## Event-Driven BT

 - First Traversal
    - All nodes are expaned depth-first
    - Everything happens as before
 - Subsequent Traversals
    - There are no traversals from the root anymore!
    - Child behavior broadcast their status changes
    - Parents respond and adapt locally only
    - Only in the worst case expand again from root.

 - new Status code: BH_SUSPENDED
    - which will say that this behavior is active but it doesn't need to be called because it's waiting for something to happen. 
    - so this basically gives us or a performace even though we might not use a data oriented approach and then driven trees can preform data orient once because we have this status code 
    - the magic will happen by a hehavior observer so each behavior will have its own observer , or if you're spliting up your nodes and your tasks then each task will have the task observer , which will notify a parent that it's done and the parent will be able to deal with that as it sees fit 


<h2 id="ad5480f838ed67e92fecf7af3cef120d"></h2>


## What's Next

 - Disclaimer
    - Nodes not covered:
        - Decorators / Filters
        - Parallels
    - Other API Issus:
        - How to abort() behaviors and whole trees
        - How to support non-interruptible behaviors
     
