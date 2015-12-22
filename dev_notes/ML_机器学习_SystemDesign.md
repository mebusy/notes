
    Spam classification example
        model
        how 2 spend your time to make it have low error
        Error Analysis
    Handling Skewed Data
        Trading off precision and recall
        how 2 compare precision/recall numbers


# ML System Design

## Spam classification example

#### model

Supervised learning. x=features of email,y= spam(1) or not spam(0).

Features x: Choose 100 words indicative of spam/not spam. `x ∊ ℝ¹⁰⁰`

eg. **deal, buy, discount** ,(likely to be spam) **andrew, now**,(likely to be not a spam) ...

We set the feature to 1 if the feature (word) appears in email , while set to 0 if it doesn't appear in email.

 - Xⱼ=1 , if word j appears in email
 - Xⱼ=0 , otherwise

**Note: In practice, take most frequently occurring n words( 10k < n < 50k ) in training set , rather than manually pick 100 words.**

---

#### how 2 spend your time to make it have low error

 - collect lots of data , eg. "honeypot" project
 - develop sophisticated features based on email routing infomation(from email header)
 - develop sophisticated features for message body
 - develop sophisticated algorithm to detect misspellings.


#### Error Analysis

##### recommended approach

- Start a simple algorithm that you can implement quickly
  Implement it ant test it on your cross-validation data.
- Plot learning curve to decide if more data , more feature , etc, are likely to help.
- Error analysis: Manually examine the examples(in `cross validation` set) that your algorithm made errors on.
 
Error analysis may not be helpful for deciding if this is likely to improve performance. Only solution is to try it and see if it works.

Need numerial evaluation (eg. CV error) of algorithm's performance with or without somethings.

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

#### Trading off precision and recall

查准率和回归率之间的关系：

假设我们使用一个逻辑回归分类器来预测病人是否患了癌症：

0 <= h(x) <= 1

我们使用 阀值 0.5 来预测癌症病人，即 h(x)>=0.5 则预测为癌症病人。

如果我们希望只有在我们非常确认的情况才预测为癌症病人，我们可以提高阀值 eg.0.7 , hight precision， low recall

如果我们希望避免错过过多的癌症病例（false negative实际患癌症，但预测为正常）, 我们可以降低阀值， eg. 0.3

---

#### how 2 compare precision/recall numbers

什么样的 precision/recall 组合表现最好, 我们通常 尝试不同的 threshold, 计算 CV data上的F₁Score, 选择F₁Score最大的方案。

\  |Precision(P)|Recall(R)|Average=(P+R)/2|F₁Score=2*PR/(P+R)
---|---|---|---|---
Algorithm1 | 0.5 | 0.4  |0.45|0.444
Algorithm2 | 0.7 | 0.1  |0.4|0.175
Algorithm3 | 0.02 | 1.0 |0.51|0.0392

 - 最差的情况， P=0 or R=0, F₁Score=0 ,
 - 最好的情况， P=1 and R=1, F₁Score =1.


 
