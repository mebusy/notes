...menustart

- [ML System Design](#0f37957d7f1f5bd5de2a41d8bc2c1d8f)
    - [Spam classification example](#fdd8a248b4498925961eda78672dd490)
        - [model](#20f35e630daf44dbfa4c3f68f5399d8c)
        - [how 2 spend your time to make it have low error](#c568e952b628d68476fe579f33a608ce)
        - [Error Analysis](#7f9ed9579be60a55e194a10a58934676)
            - [recommended approach](#0c43ce66674fab970f4745cc51f5a08d)
    - [Handling Skewed Data](#3b463e85a6fc1768653d6f94ebeec03a)
        - [Trading off precision and recall](#81b1eb7e22f3395b2655f25e9b8af855)
        - [how 2 compare precision/recall numbers](#442c265b01ce99095ce64d12ca75ebc7)
    - [Use Large Data set](#427c5bfcdec0cf350cba5548fb1e4ef1)
        - [Large data rationale](#f0668a5d4294962318ee1112e57e8108)

...menuend


<h2 id="0f37957d7f1f5bd5de2a41d8bc2c1d8f"></h2>


# ML System Design

<h2 id="fdd8a248b4498925961eda78672dd490"></h2>


## Spam classification example

<h2 id="20f35e630daf44dbfa4c3f68f5399d8c"></h2>


#### model

Supervised learning. x=features of email,y= spam(1) or not spam(0).

Features x: Choose 100 words indicative of spam/not spam. `x ∊ ℝ¹⁰⁰`

eg. **deal, buy, discount** ,(likely to be spam) **andrew, now**,(likely to be not a spam) ...

We set the feature to 1 if the feature (word) appears in email , while set to 0 if it doesn't appear in email.

 - Xⱼ=1 , if word j appears in email
 - Xⱼ=0 , otherwise

**Note: In practice, take most frequently occurring n words( 10k < n < 50k ) in training set , rather than manually pick 100 words.**

---

<h2 id="c568e952b628d68476fe579f33a608ce"></h2>


#### how 2 spend your time to make it have low error

 - collect lots of data , eg. "honeypot" project
 - develop sophisticated features based on email routing infomation(from email header)
 - develop sophisticated features for message body
 - develop sophisticated algorithm to detect misspellings.


<h2 id="7f9ed9579be60a55e194a10a58934676"></h2>


#### Error Analysis

<h2 id="0c43ce66674fab970f4745cc51f5a08d"></h2>


##### recommended approach

- Start a simple algorithm that you can implement quickly
  - Implement it and test it on your cross-validation data.
- Plot learning curve to decide if more data , more feature , etc, are likely to help.
- Error analysis: Manually examine the examples(in `cross validation` set) that your algorithm made errors on.
 
Error analysis may not be helpful for deciding if this is likely to improve performance. Only solution is to try it and see if it works.

Need numerial evaluation (eg. CV error) of algorithm's performance with or without somethings.

<h2 id="3b463e85a6fc1768653d6f94ebeec03a"></h2>


## Handling Skewed Data

当正负样本的比例 出现极端的情况，比如负样本(0)只占 0.5%, 则负样本就称为 偏斜类 skewed classes.

当出现 skewed class 时，就无法通过预测精确度 来衡量我们算法的表现了。

举例: 假设某个学习算法，预测准确率是 99%, 但是一个直接忽略样本feature，直接返回0的函数，确可以达到99.5%的准确率。预测准确率在这里无法用于评估两个算法的优劣。

我们需要新的衡量值。 一个用来处理这种情况的衡量值 叫做 查准率(precision) 和 召回率(recall).  

  \ | Actual 1 | Actual 0
---|---|---
Predicted 1 | True positive | False positive 
Predicted 0 | False negative | True negative

Precision = (#True positive)/(#Predicted 1)  , 和 正确预测正样本的次数 和 总的预测正样本的次数(True pos + False pos)的比率， 比值越高越好。

Recall = ( #True positive )/(#Actual 1 ) =( #True positive )/( True pos + False neg ) , 这个值同样越高越好

拥有高的precision 和 recall的算法，是较好的实现。

---

<h2 id="81b1eb7e22f3395b2655f25e9b8af855"></h2>


#### Trading off precision and recall

查准率和回归率之间的关系：

假设我们使用一个逻辑回归分类器来预测病人是否患了癌症：

0 <= h(x) <= 1

我们使用 阀值 0.5 来预测癌症病人，即 h(x)>=0.5 则预测为癌症病人。

如果我们希望只有在我们非常确认的情况才预测为癌症病人，我们可以提高阀值 eg.0.7 , hight precision， low recall

如果我们希望避免错过过多的癌症病例（false negative实际患癌症，但预测为正常）, 我们可以降低阀值， eg. 0.3

---

<h2 id="442c265b01ce99095ce64d12ca75ebc7"></h2>


#### how 2 compare precision/recall numbers

什么样的 precision/recall 组合表现最好, 我们通常 尝试不同的 threshold, 计算 CV data上的F₁Score, 选择F₁Score最大的方案。

\  |Precision(P)|Recall(R)|Average=(P+R)/2|F₁Score=2*PR/(P+R)
---|---|---|---|---
Algorithm1 | 0.5 | 0.4  |0.45|0.444
Algorithm2 | 0.7 | 0.1  |0.4|0.175
Algorithm3 | 0.02 | 1.0 |0.51|0.0392

 - 最差的情况， P=0 or R=0, F₁Score=0 ,
 - 最好的情况， P=1 and R=1, F₁Score =1.


 
<h2 id="427c5bfcdec0cf350cba5548fb1e4ef1"></h2>


## Use Large Data set

一个在某个数据集下表现较差的算法， 在另一个大很多的数据集上，可能会表现的最好。

It's not who has the best algorithm that wins. It's who has the most data.


<h2 id="f0668a5d4294962318ee1112e57e8108"></h2>


#### Large data rationale

大数据情况下的设计原则:

Assume feature x  has sufficient information to predict y accurately. (Useful test: Give the input x , can a human expert confidently predict y ? ）

在这个前提下， 我们设计一个有较多参数(隐藏层 )的算法 ( polynomial 不算) ， 和一个庞大的 training set (unlikely to overfit). 

可以选择较多的参数确保算法 low bias, 庞大的训练集，可以确保 low variance.

(如果数据集足够大，即便算法不使用 正则化，也会表现的不错)


 
