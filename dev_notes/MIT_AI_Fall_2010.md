
# MIT AI , Fall 2010

# 1. Introduce and Scope

 - ALGORITHMS ENABLED BY 
 - CONSTRAINTS EXPOSED BY
 - REPRESENTATION THAT SUPPORT
 - MODELS  TARGETED  AT
 - THINKING  PRECEPTION  ACTION


Our models are models of thinking.  Model targeted at thinking , perception  and action.  In order have a model, you have to have representation.

Having got the representation, something magical happened. We've got our constraints exposed.

After all ,in the end, we have to build programs.

So AI is about algorithms enabled by constraints exposed by representations that support the making of models to facilitate an understanding of thinking , perception and action.

---

GENERATE AND TEST

Example: 通过一页一页翻阅专业植物书籍，鉴定某片叶子 属于那种树。

Generate and test method consists of generating some possible solutions, feeding them into a box that tests them, and then out the other side comes mostly failures. But every once in a while we get something that succeeds and pleases us.

```
 G -> T --> S
        |-> F
```

We call this the ***Rumpelstiltskin Principle*** , perhaps The first of our powerful ideas for the day. Rumpelstiltskin Principle says that once you can name something, you get power over it.

 - REPRESENTATION RIGHT
 	- => ALMOST DONE
 - SIMPLE != TRIVIAL
 - Rumpelstiltskin Principle


# 2. Reasoning: Goal Trees and Problem Solving

Goal Trees , also known as and-or tree.

PROBLEM REDUCTION

```
	Apply all safe transforms
		-> Look in table
		-> test if it's done --> S
							 |-> F --> Find problem --> Apply heuristic 启发式 transform
```

What we're going to do is, apply all safe transforms. That's our first step. Then we're going to look in the table, and then we're going to do a test to see if we're done. And if we are, we report success. But, we're not likely to get done with just that stuff.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_GoalTree.png)


# 3. Reasoning : Goal Trees and Rule-Based Expert System

一个 类似 汉诺塔 版砖块的演示例子

 - PUT-ON
 	- FIND SPACE
 	- GRASP 	->  CLEAR TOP  -> GET RID OF 
 	- MOVE
 	- UNGRASP


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_GRASP_EXAMPLE.png)

**Rule-based expert system**

The rule-based expert systems were developed in a burst of enthusiasm about the prospects for commercial applications of artificial intelligence in the mid-1980s.

FORWARD-CHAINING













