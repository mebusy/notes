...menustart

 - [MIT AI , Fall 2010](#02cfbc450a484e485cfcb5a8b6293485)
 - [1. Introduce and Scope](#0642dcdd47a2b0dedd3a1b7be3447ef6)
 - [2. Reasoning: Goal Trees and Problem Solving](#5a7296bc9aaf9ebd3c7128ce7338fc8a)
 - [3. Reasoning : Goal Trees and Rule-Based Expert System](#ef3e76fa72903f6a29d73611f289c069)
 - [21. Probabilistic Inference](#5c63798bd670c15157052fdd1197b58f)
	 - [全概率理论](#c9c0f393c7d6fb89c37d4e7d49ef4d76)
	 - [BAYES](#4658c50b8646a0292b3c9f1824805f62)

...menuend


<h2 id="02cfbc450a484e485cfcb5a8b6293485"></h2>
# MIT AI , Fall 2010

<h2 id="0642dcdd47a2b0dedd3a1b7be3447ef6"></h2>
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


<h2 id="5a7296bc9aaf9ebd3c7128ce7338fc8a"></h2>
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


<h2 id="ef3e76fa72903f6a29d73611f289c069"></h2>
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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_FC_RBES.png)


<h2 id="5c63798bd670c15157052fdd1197b58f"></h2>
# 21. Probabilistic Inference 



联合概率可以做很多事情，但缺点是 需要全部的事件的概率 ， 数据太多了。 一般利用条件概率 来减少数据量。



---

 1. **BASIC**
 	- 1. 0 <= P(a) <= 1
 	- 2. P(TRUE) = 2 , P(FALSE) = 0
 	- 3. P(a) + P(b) - P(a,b) = P(aUb)

 2. **CONDITIONAL PROBABILITY**
 	- P(a|b) = P(a,b) / P(b)
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/condition_prob_intuition.png) 
 		- 大饼变小饼
 	- P(a,b) = P(a|b)·P(b)
 	- P(a,b,c) = P(a , (b,c)) = P(a|bc)P(b,c) = P(a|bc)P(b|c)P(c)
 		- 扩展到 多个变元
 		- a depends on 2 things ; b depends on 1 thing and nothing to the left ;  c depends on nothing and nothing to the left. 
 3. **CHAIN RULE**
 	- P(a,b,c) 扩展到 P(x1, ... , xn )

 4. **INDEPENDENCE**
	- `P(a|b) = P(a)  , if a independent of b` 
	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/independence_intuition.png)

 5. ***conditional definition independence:***
	- P(a|bz) = P(a|z) 
	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/conditional_indepence_intuition.png)
	- P(a b|z) = P(a|z)P(b|z)   , if a independent of b
		- P(a b|z) = P(a,b,z) / P(z) = P(a|bz)P(b|z)P(z) / P(z) = P(a|bz)P(b|z) = P(a|z)P(b|z)

 6. **BELIEF NETS**
 	- below



![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_belief_nets.png)

> 举例: 使用条件概率， 可以用 10个数据，表示  2⁵ = 32 的联合概率

```
P(p,d,b,t,r) = P(p|d b t r) P(d|b t r) P(b|t r) P(t|r) P(r)

according to conditional definition independence:

P(p,d,b,t,r) = P(p|d ) P(d|b  r) P(b ) P(t|r) P(r)
```

Any variable on this graph is independent of any other non-descendant given its parents.

Independent of any non-descendant given its parents.

That means the probability of the dog barking , given its parents (B,R) , doesn't depend on T, the trash can being overturned. 

Becuase the intuition is all of the causility is flowing through the parents (B, R) and can't get to this variable D without going through the parents.

使用 条件概率 来替代 联合概率的核心是 chain rule. 应用chain rule的关键是 变量的顺序, x₂的发生应该独立于x₁ , x₃的发生应该独立于 x₂ , 以此类推。

So one thing i'm going to do before I think about probability is I'm going to make a linear list of all these variables.

And the way I'm going to make it is I'm going to chew away at those variables from the bottom. I've taken advantage of a very important property of these nets. And that is there is no loops. So there's always going to be a bottom.

So what I'm going to do is I'm going to say  there are two bottom here,  there's P and T,  I'm going to choose P. So I'm going to take that (P) off and pretend it's not there anymore.

```
P 
```

Then I take out D , that's now a bottom because there's nothing below it.

```
P D
```

Now I have got B,R,T . B no longer has anything below it. So I can list it next.

```
P D B
```

Now over here I've got raccoon and trash can. But trashcan is at the bottom. So I've got to take it next.

```
P D B T
```

I want to ensure that there are no descendants before we list it in the list.  So finally I get to raccoon.

```
P D B T R
```

So the way I constructed this list like so ensure that this list arranges the elements so that for any paritcular element , none of its descendants appear to its left. And now that's the magical order for which I want to use the chain rule. 


```
P(p,d,b,t,r) = P(p|d b t r) P(d|b t r) P(b|t r) P(t|r) P(r)
```

First of all ,none of those expressions condition any of the variables on anything other than non-descendants, all right ?

这些表达式都不会对非后代之外的任何变量 有影响。

That's just because of the way I've arranged the variables. And I can always do that because there are no loop.

Oh wait, When I draw this diagram , I asserted that no variable depends on any non-descendant given its parents. So if I know the parents of a variable , I know that the variable is independant of all other non-descentands.  

Now I can start scratching stuff out.

I know that P , from my diagram, has only 1 parent, D. So given its parent , it's independent of all other non-descendants (B R T) . 

D has 2 parents B R , given that, I can scratch out any other non-descendent T. 

B is conditional on T R , but B has no parent. So it actually is independent of those 2 guys.

T , is dependent on R. And R , the final thing in the chain , that's just a probability.

So now I have a way of calculating any entry in that table (whole 联合概率)  because any entry in that table is going to be some combination of values for all those variables.

So anything I can do with a table, I can do in principle with this little network. 

But now the question is , I've got some probabilities I'm going to have to figure out here.

-----

So up here we've got the a priori probability of B.  Down here with the dog , I've got a bigger table because I've got probabilities that depend on the values of it's parent. The probability of dog barking depends on the condition of the parents , nothign else.

So there are two of these variables (B R). So there are four combinations.

What I really want to do is to calculate all of these probabilities that give the probability of the dog condition of the burglar and the raccoon. Similarly I want to calculate the probability of B happening doesn't depend on anything else.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_BRD.png)

Step 2, I'm going to extend these tables a little bit so I can keep track the tallies. 

 - one is going to be all the ones that end up in a particular row. 
 - one is for which D is true.

Similarly, I'm going to extend P(b) in order to keey track of some tallies. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_BRD_extend.png)

And now suppose that my first experiment comes roaring in. And it's all T's. ( B is True, R is True, and D is True )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_BRD_extend_TTT.png)

Let's suppose that the next thing happens be all false.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_BRD_extend_FFF.png)

Let's we have TTF.   ( B is True, R is True, and D is False )

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_BRD_extend_TTF.png)

---

通过在 扩展表中 记录实验结果，我们最后可以计算出 network 表中，需要的概率。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/AI_prob_calc.png)

<h2 id="c9c0f393c7d6fb89c37d4e7d49ef4d76"></h2>
## 全概率理论

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Prob04.png)

 - 把样本空间分为 若干块  A₁,A₂,A₃ , 就知道了 P(Aᵢ) , 且Aᵢ相互独立？
 - 只要再 知道 每小块 中B 发生的概率 P(B|Aᵢ)
 - 就可以计算出 P(B)

```
P(B) =  P(A₁)·P(B|A₁)
       +P(A₂)·P(B|A₂)
       +P(A₃)·P(B|A₃)
     = ΣP(Aᵢ)·P(B|Aᵢ)
```


<h2 id="4658c50b8646a0292b3c9f1824805f62"></h2>
## BAYES



 - 知道 P(Aᵢ) , P(B|Aᵢ)  (和全概率模型一样)
 - 就可以计算出 P(B) = `ΣP(Aⱼ)·P(B|Aⱼ)`
 - 在此基础上，我们就能计算出 `P(Aᵢ|B)`

```
P(Aᵢ|B) = P(Aᵢ, B) / P(B)
        = P(Aᵢ)·P(B|Aᵢ) / P(B)
        = P(Aᵢ)·P(B|Aᵢ) / ΣP(Aⱼ)·P(B|Aⱼ)
```

---

```
P(a|b) = p(a,b)/P(b)

P(a|b)P(b) = P(a,b) = P(b|a)P(a)

P(a|b) = P(b|a)P(a)/P(b)
``` 

知道 a,b各自的概率，以及任意 条件概率， 可以得到 另一条件概率。

```
P(Aᵢ|B) = P(B|Aᵢ)P(Aᵢ) / P(B)
        = P(B₁|Aᵢ)P(B₂|Aᵢ)...P(Bn|Aᵢ)P(Aᵢ) / P(B)
```

应用： a collection of independent events





