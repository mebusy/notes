[quick sort](#quicksort)
<h1 id='quicksort'></h1>

# 算法1,2

## 概率review

#### Sample Space 样本空间

 - `sample space Ω`= 'all possible outcomes'  ,(Ω is usually finite)
 - also: each outcome `i∊ℝ` has a probability `p(i)>0`
 - constraint: `Σp(i)=1` (i∊Ω) , 样本空间中,所有样本点概率和为1

> example: 
rolling 2 dice, Ω size = 36, p(i) = 1/36


#### Events 

 - an `event` is a subset S⊆Ω
 - The probability of an event S is  Σp(i) (i∊S)

> example
rolling 2 dice, event S : sum of dice ==7
P[S] = (1/36) * 6 = 1/6

#### Random Variables

 - A random variable `X` is a real-valued function `X:Ω->ℝ`

随机变量函数把 样本点 映射到实数轴上。

随机变量可能只覆盖 Ω的子集，也可能是全集。

> example:
sum of the 2 dice

#### Expectation 期望值

> 期望值是随机变量各个 输出值·概率值的 和, 也叫随机变量均值

 - X:Ω->ℝ    (random variable)
 - the expectation E[ X ] of X = average value of X = ΣX(i)·p(i) (i∊Ω)

> example:
1. 掷一枚六面骰子，其点数的期望值 = 1*1/6 + 2*1/6 + 3*1/6 + 4*1/6+ 5*1/6+ 6*1/6 = 3.5
2. expectation of the sum of 2 dice: 7
3. 彩票每注2圆，中奖概率 1%，奖金50圆，求每注期望收益.
    P(X=48)=0.01, P(X=-2)=0.99 , E(X) = 48x0.01+(-2)x0.99 = -1.5圆
    购买5注的期望收益为 -1.5*5 = -7.5圆

#### Linearity of Expectation 期望值的线性特征

期望值E是一个线形函数。

 - X₁,X₂,...,Xn are random variables
 - defined an Ω, then:
 - 1) E[C·X] = C·E[X]
 - 2) ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/linearity_of_expectation.png)

> proof:

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/linearity_of_expectation_proof.png)

> example:
X₁,X₂ = the two dice, E[X₁]= E[X₂]= 3.5 , 
E[ X₁+X₂ ] = E[X₁] + E[X₂] = 7 .

在一般情况下，两个随机变量的积的期望值不等于这两个随机变量的期望值的积。特殊情况是当这两个随机变量是相互独立的时候（也就是说一个随机变量的输出不会影响另一个随机变量的输出）.

#### Example : Load Balancing Solution

 - need to assign n processes to n servers
 - assign each process to a random server
 - what is expected number of processes assigned to a server

> - sample space Ω = all nⁿ assignments of processes to servers
> - let Y = total number of processes assigned to the 1st server
> - Goal: compute E[Y]
> - let Xⱼ=1, if jᵗʰ process assigned to 1st server, otherwise Xⱼ=0
> - Y = ΣXⱼ (j=1,n)
> - E[Y]=E[ ΣXⱼ ] =Σ E[Xⱼ] =Σ(p[Xⱼ=0]·0 + p[Xⱼ=1]·1) = Σ1/n = 1


#### Conditional Probability

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/conditional_probability.png)

P[X|Y] 念做: X , given Y , 事件X在另外一个事件Y已经发生条件下的发生概率。

`P[X|Y] = P[X∩Y] / P[Y]`

> example:
roll two dices, what's the prob of "at least one dice is 1 and sum=7" ?
X = at least one dice is 1
Y = sum of 2 dices is 7
P[X|Y] = P[X∩Y]/P[Y] = (2/36)/(6/36) = 1/3


#### Independence (of Events)

事件A是否发生 对事件B发生的概率没有影响,反之亦然。这样的两个事件叫做`相互独立事件`。

> definition:

Events X,Y∊Ω  are independent if and only if `P[X∩Y]=P[X]·P[Y]`

> check:

if X,Y are independent , it holds: `<=> P[X|Y]=P[X] <=> P[Y|X]=P[Y]`

> warning:

你对独立事件的直觉，一般都是错的


#### Independence (of Random Variable)

> definition:

random variables A,B ( defined in Ω ) are independent 

<=> the events P[A=a] , P[B=b] are independent for all a,b

<=> `P[A=a and B=b] = P[A=a]·P[B=b]`

> Claim: 

if A,B are independent , then E[A·B]=E[A]·E[B]

> Proof:





---
 
## Introduce

### * Karatsuba算法 快速乘法

TODO

### * Merge sort 归并排序

merge sort 是分治法的应用范例。

`分治法思路:`

 1. 把输入array 拆成两部分
 2. 对两个子数组 进行递归排序(调用自己)
 3. 合并两个已排序的数组

`MergeSort 代码实现如下:`

```python
def MergeSort(lists):
    if len(lists) <= 1:  # exit condition
        return lists
    num = int( len(lists)/2 ) # (1)
    left = MergeSort(lists[:num])  #(2)
    right = MergeSort(lists[num:]) #(2)
    return Merge(left, right)  #(3)
```
  
`分析:`

可以看到, 在递归算法 在`某一级`的函数调用中:

 - (1)把array分成两个子数组,(2)是两次函数调用, 分治法中,这两部分只是概念上的东西，可以忽略它们的时间消耗; 
 - (3)需要把两个数组合并, 大量的计算都发生在这里，这是我们关心的重点。

`Merge代码（3）实现如下:`

```python
def Merge(left,right):
    r, l=0, 0
    reslut=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            reslut.append(left[l])
            l += 1
        else:
            reslut.append(right[r])
            r += 1
    reslut += right[r:]
    reslut += left[l:]
    return reslut
```

#### Running time 

`Merge 单次 Running Time:`

我们来看一下 Merge 方法执行的代码行数。函数中有一个while循环体, 循环体外是4行代码; 循环体每次执行都会执行4行代码, 共执行m次循环, m等于left,right两个数组的长度和。所以，我们可以认为 Merge方法单词调用的 running time <= 4m+4。因为m>=2, 所以 runing time <= 6m.

6m 只是 Merge方法 一次调用的时间，我们感兴趣的是 整个 Merge Sort的执行时间。


`Merge Sort total running time:`

recursion tree: 把 算法过程，用一颗`树`的结构表示出来。分治算法可以使用一颗`二叉树`来表示，为了简化，我们假设 待排序数组的长度 n为2的幂, 这样我们得到的就是一个`完整二叉数`。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/recursive_tree.png)


我们可以知道，树的深度 levels = log₂n , 第log₂n层 的每个leave 都只有`1`个数据。

对每一层 ,level j=0,1,2,...,log₂n , 有`2ʲ`个子问题，没有子问题的数据长度是 `n/2ʲ` (数据总长度/子问题个数).

所以对于某一层 level j, 总的 running time = 子问题数*子问题的运行时间= `2ʲx6( n/2ʲ )` = 6n。非常棒，level j 的 running time 和j完全无关。

把所有level的running time相加，得:

Total Runing time = 6n x (log₂n +1) = `6n·log₂n + 6n` .


#### Asymptotic analysis 渐近分析

high-level idea: 忽略 低阶项 和 首项系数。

example:  Merge sort 的 `6n·log₂n + 6n` 在渐近分析中 等价与 `nlog₂n`.

Terminology 术语: Merge sort running time = `O( nlogn )`

##### Big-Oh

算法的时间复杂度是一个函数，它定量描述了该算法的运行时间。

时间复杂度常用大O符号表述，不包括这个函数的低阶项和首项系数。

一般情况下，算法的基本操作重复执行的次数是模块n的某一个函数f(n)，因此，算法的时间复杂度记做：`T(n)=O( f(n) )`

常见复杂度等级: `1，log₂n，n，nlog₂n ，n²，n³，2ⁿ，n! `

`Big-Oh Formal Definition (正式定义):`

当且仅当 存在两个常数 c , n₀ (n₀>0),  使得对于任意 n>=n₀, T(n) <= c·f(n), 则计为 `T(n)=O( f(n) )`.  简单理解，就是 fn乘上一个数，比T(n)大就行。

`O 描述T的上限`。

`注意: c 和 n₀ 不可以依赖于n`


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Big-Oh.png)


`example 1:` 

T(n) = `aⱼuʲ`+ ... + a₁n+ a₀ , 证明 T(n) = O(`nʲ`)

证: n₀=1, c=|aⱼ| + ... + ... |a₁| + |a₀|, 对于 n>= 1, T(n)<= c·f(n)

`example 2:`

证明: 对于任意 k>=1 , nᵏ is not O( nᵏ⁻¹ )

假设存在c , n₀, 使得当 n>=n₀时, nᵏ <= c·nᵏ⁻¹ , 等式约减, 得出: n<=k 。

c , n₀ 不可以依赖于 n ，所以假设不成立。

##### Big Omega Ω

`Ω 描述T的下限`。

当且仅当 存在两个常数 c , n₀ (n₀>0),  使得对于任意 n>=n₀, T(n) >= c·f(n), 则计为 `T(n)=Ω( f(n) )`.  简单理解，就是 fn乘上一个数，比T(n)小就行。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/Big-Omega.png)


##### Theta Notation Θ

Θ== T

T(n)=Θ( f(n) )  当且仅当 T(n)=O( f(n) ) and T(n)=Ω( f(n) )。

等价于: 当且仅当 存在3个常数 c₁,c₂,n₀(n₀>0),  使得对于任意 n>=n₀, c₁·f(n)<=T(n)<=c₂·f(n).


##### Little-Oh Notation

和 Big-Oh 类似，只是 常数c 只能取正数。

eg. for all k>=1 , nᵏ⁻¹=o( nᵏ )


##### 例子

题目: T(n)=0.5·n² + 3n , 哪些是对的？

 1. T(n)=O(n)
 2. T(n)=Ω(n)     //(n₀=1, c=0.5)
 3. T(n)=Θ(n²)    //(n₀=1, c₁=0.5, c₂=4) 
 4. T(n)=O(n³)    //(n₀=1, c=4)

答案: 2,3,4 , (问题: T(n)=O(n²)也正确? )

---

题目: 证明 2ⁿ⁺¹⁰ = O(2ⁿ)
证: c=1024, n₀=1

---

题目: 证明 2¹⁰ⁿ != O(2ⁿ)
证明: 假设 2¹⁰ⁿ = O(2ⁿ) , 则 2¹⁰ⁿ<= c·2ⁿ , 则  2⁹ⁿ<= c , c 不可以依赖于n，所以假设不成立。

---

题目: 函数f(n) , g(n) 只输出正值， 证明 max(f,g)=Θ(f(n) + g(n))

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/fn+gn.png)

证明: 如图可知, 

因为f(n) , g(n)>0,  所以 max(f,g)<= f(n) + g(n) , eg. max(2,4) <= 2+4。

又有 2 max(f,g) >= f(n) + g(n)  , eg. 2*max(2,4) >= 2+4，

所以 max(f,g) >= 0.5( f(n) + g(n) ).

于是: 0.5( f(n) + g(n) ) <= max(f,g) <= ( f(n) + g(n) ) , 得证。


### * Counting Inversions 计算逆序

题: 计算一个数组中，逆序的个数, eg. (1,3,4,2,4,6) 逆序个数为 (3,2),(5,2),(5,4) 3个。

`O( n² ) 算法lua代码:`

``` lua
cnt = 0
n= 6
for i=1,n-1 do
    for j=i+1,n do
        if A[i]>A[j] then
            cnt = cnt +1
        end
    end
end
```

`O( nlogn ) 分治法算法:`

 1. 把输入array 拆成两部分
 2. 对两个子数组  计算逆序数 X,Y
 3. 计算 子数组 之间统计关系 Z , 返回 X+Y+Z
 
第3步 牵涉到两个子数组的遍历，复杂度上很难做到线性，这里我们需要参考merge sort的做法，最后处理两个有序数组会简单的多。

```
def Sort_Count_Inv(lists):
    if len(lists) <= 1:  # exit condition
        return 0,lists
    num = int( len(lists)/2 ) 
    X,left = Sort_Count_Inv(lists[:num]) 
    Y,right= Sort_Count_Inv(lists[num:]) 
    Z,D  = Merge_Count_Inv(left, right)

    return X+Y+Z , D
```

Merge_Count_Inv 方法的关键: 如果输入array没有逆序存在，那么数组是有序的，且left array的所有元素都 '<=' right array 中的元素。merge的时候，必然是left array中的元素完全被合并光，再开始处理right array. 换句话说，当merge 每次从 right array中合并数据的时候，left array中的剩余元素,都是逆序。

```
def Merge_Count_Inv(left,right):
    r, l=0, 0
    cnt = 0
    reslut=[]
    while l<len(left) and r<len(right):
        #这里必须改为<=
        if left[l] <= right[r]: 
            reslut.append(left[l])
            l += 1
        else:
            reslut.append(right[r])
            r += 1
            # 计算逆序
            cnt += len(left)-l

    reslut += right[r:]
    reslut += left[l:]
    return cnt , reslut  
```


### * closest pairt 距离最近两个点

题：有一组点[ (x₁,y₁),(x₂,y₂),...,(xn,yn) ] ,求距离最近的两个点。

`1-D case:`

假设这些点都是1-D的, 那么只需要把这些点排序，然后遍历n找出距离最短的两个点。


`思路:`

 - 拆成两个子array
 - 计算出 两个子数组的 cloest pair : pair1,pair2
 - 计算两个子数组的 split closest pair pair3, 返回min(D(pair1),D(pair2),D(pair3))

第3部分是难点, 线性处理两个子数组，才能保证这个算法O(nlogn).

现在，可能发生两种情况

 1. 好的情况: closest pair (p,q)就在两个子数组中,这样就可以不用处理第3部分了。
 2. 坏的情况: closest pair, p在一个子数组中，q在另一个。我们需要额外的计算 closest split pair (CSP)的情况。

```python
def ClosestPair( lists_x, lists_y ):
    if len(lists_x) == 1:
        return ( lists_x[0], ( 999999, 999999 ) )

    if len(lists_x) == 2:
        return ( lists_x[0], lists_x[1] )

    #分成两个子数组
    num = int( len(lists_x)/2 ) 
    left = lists_x[:num]
    right = lists_x[num:]

    # 每个子数组分别对 x,y排序，得到新数组
    left_x  = left # already sorted by x 
    left_y  = sorted(left, cmp = lambda a,b : cmp( a[1],b[1] ))

    right_x = right # already sorted by y 
    right_y = sorted(right, cmp = lambda a,b : cmp( a[1],b[1] ))

    # 每个子数组计算 closest pair
    (p1,q1) = ClosestPair( left_x, left_y )
    (p2,q2) = ClosestPair( right_x, right_y )

    def D( p, q ) :
        return pow( p[0]-q[0] ,2 ) + pow( p[1]-q[1] ,2 )

    # 获取子数组最小距离
    delta = min( D( p1,q1 ) , D( p2,q2) )
    delta = math.sqrt( delta )

    l = [ (p1,q1) ,  (p2,q2)  ]

    (p3,q3) = ClosestSplitPair( lists_x, lists_y , delta )
    #print p1,q1, ',' , p2,q2 , ',' , p3,q3 , '--'  , delta , lists_x

    if p3 and q3:
        l += [ ( p3,q3) ]

    #print "-" , lists_x
    #print l , delta

    return min( l , key=lambda a: D(a[0],a[1]) ) 
```

`计算 closest split pair (CSP) (p,q):`

令 x_mean 等于 left_x 中点最大的x, delta 等于两个子数组的closest pair的距离, 所以我们可以知道:

 1. CPS p和q 一个x in [x_mean-delta,x_mean], 一个x in (x_mean,x_mean-delta]
 2. CPS p和q y 相差< delta
 3. 以 delta/2 为单位划分, 把 2delta x delta 的矩形划为8哥部分.
 4. p 和 q 必然 一个位于一侧的4个小格中，一个位于另一侧4个小格中
 5. 每个小格最多只可能有1个点存在，因为假设同一格中存在两个点，那么他们的距离就会小于delta, 而且这两个点是同left,同right的。矛盾，假设不成立。
 6. 如果对数组做 x in [x_mean-delta,x_mean+delta] 过滤，并且新数组按y 排序, q一定会在p 后面的连续的7个位置内。

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/closest_pair.png)

```python
def ClosestSplitPair( lists_x, lists_y , delta ):
    num = int( len(lists_x)/2 ) 
    x_mean = lists_x[num-1][0]
    #print 'l:' , lists_x[num/2-1] , lists_x

    # 只取 x 在 [ x_mean-delta, x_mean+delta ] 中的点，按y排序
    Sy = [ p for p in lists_y if abs( p[0] - x_mean ) <= delta ]
    #print "filter: " , num , x_mean , delta,  Sy 

    min_dist = delta*delta
    bestPair = ( None , None ) 
    #过滤完成后，

    def D( p, q ) :
        return pow( p[0]-q[0] ,2 ) + pow( p[1]-q[1] ,2 )
    for i in xrange(  len(Sy) -1  ):
        for j in xrange( 7 ):
            if i+j+1 >= len(Sy):
                continue
            p = Sy[i] 
            q = Sy[i+j+1]

            dist =  D( p, q )
            if dist < min_dist:
                min_dist = dist 
                bestPair = ( p , q ) 

    return bestPair
```



#### Master Method

如图: 递归方法的T(n)各种情况下的时间复杂度

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/master_method.png)

`a`: 子递归的数量 (>=1), 
`b`: 输入数据 拆分因子(被拆成几部分) (>1)  (注：斐波那切递归算法不满足这条)
`d`: combine step 的时间复杂度指数 

`example merge sort:`

a=2, 分成两个 子递归
b=2, 输入数据拆成了 2个 n/2  
d=1, merge sort combine step = O(n¹)

a = bᵈ , 所以 merge sort 是 case(1): O(nᵈlogn) = O(nlogn)

`example binary search:`

a=1 , 只会有1个子问题
b=2 , 输入数据对半拆分成2部分
d=0 , combine step, 数值大小比较 O(1) 

a = bᵈ , 所以 binary search 也是 case(1) , O(nᵈlogn) = O(logn)

`example 普通整数乘法:`

a=4, 拆成4个2级乘法
b=2, 数据拆成2份
d=1, combine 部分把4个运算结构移位拼接，线性 O(n)

a < bᵈ , 所以是case(3) ,  O(n²)

`Karatsuba算法:`

a=3 和普通整数乘法位移区别
b=2
d=1 

a > bᵈ , 所以是case(3) ,  O(nˡᵒᵍ₂³) ≈ O(n¹·⁵⁹)

`T(n)<= 2·T(n) + O(n²) :` 

类似 combine step 是 O(n²)的 merge sort

a=2
b=2
d=2

a < bᵈ , 所以是case(2) ,  O(n²)

    注：直觉上，应该是 n²logn, 但其实这样会导致 over estimated.

---

#### Proof Master Method

我们看一下 recursive tree 的某一层 level j 的计算量

number of all subproblems at level j:   `aʲ`
subproblem input size at level j:       `n/bʲ`

work on each subprolbem <= `C·( n/bʲ )ᵈ` , C是为了算上递归方法外的计算消耗
work on level j <=  `aʲ * C·( n/bʲ )ᵈ` = `cnᵈ·[a/bᵈ]ʲ`

把所有层的work 相加，得到

`total work ` <= ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/total_work_recursive.png)

> a: rate of subproblem  profile action (RSP)
b: rate of work shrinkage (RWS)

可以看到，如果 RSP<RWS, 每一层的 amount work 在减少;如果 RSP<RWS,每一层的 amount work 在增加; 如果 RSP==RWS,每一层 amount work 相同。

我们来看一下 master method的三种情况：

> 1. RSP==RWS, total work <= cnᵈ·logᵦn = O(nᵈ·logn)
> 2. RSP < RWS, most work at root, less work at each level, `[a/bᵈ]ʲ`是1个几何级数 1 + x + x² + x³ + ..., 当x小与0是，最终收敛为:1/(1-x)。 所以 `Σ[a/bᵈ]ʲ`和n无关, <= constant. 所以 total work = O(nᵈ)
> 3. RSP > RWS, more work at each level,  `Σ[a/bᵈ]ʲ` <= constant * largest term (eg.1+2+4+...+128 < 256). 所以， total time = O( nᵈ·(a/bᵈ)ˡᵒᵍ𝑏ⁿ ).
    ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/master_method_proof_3.png)
    最终表达式，其实就是 recursive tree 的叶子数。


---

### * BinarySearch

```
def BinarySearch( sorted_list , lo, hi , num ):
    if lo > hi :  #protection
        return -1   # not found 

    iMid = (lo + hi) /2 

    if sorted_list[iMid]  == num:
        return iMid
    elif sorted_list[iMid]  > num:
        hi = iMid -1
        return BinarySearch( sorted_list , lo, hi , num )
    else:
        lo = iMid +1
        return BinarySearch( sorted_list , lo, hi , num )
    
    return -1
```

### * Quick Sort

> key idea: partition around a pivot

从数组中挑选一个元素作为 pivot，比如挑选第一个元素。

重新排序数组，使得 在 pivot 左边的元素，都比 pivot 小，在pivot 右边的元素，都比 pivot 大。 这样, pivot(only)就被放到最终排序数组的正确位置了。

> Description QuickSort( array A , length n ):

 - if n==1 return
 - p = ChoosePivot( A,n )
 - partition A around p
 - recursively sort  1st part
 - recursively sort  1nd part

> Partition algorithm : Partition(A,l,r)

```
choose mid element as pivot
swap pivot <-> 1st element  // 把 pivot 放到数组第一个
p:=A[l]  
i:=l+1   // i指向第一个 >p 的数据，i左边的数据,都小于p
for j:=l to r   // j 遍历 unpartitioned array
    if A[j] < p     // j 如果遍历到 <p 的元素
        swap A[j] and A[i]   // 交换 i和j的数据, 
        i++                 // 同时i 向后移动一步
swap A[l] and A[i-1]   // i 是 <p 和 >p 数据分界点，交换 l和 i-1的数据
                       // 这样p就处在了正确的位置了
```


p|... < p ...|... > p ...| ? unpartitioned
--|--|--|--
- |  | i  | j

> quicksort python 实现:

```python
# [ lo , hi ]
def QuickSort( lists , lo , hi  ):
    if hi - lo < 1 : 
        return

    iMid =  (lo + hi) /2   # choose mid element as pivot
    lists[lo],lists[iMid]=lists[iMid],lists[lo]  

    p = lists[lo]

    # partition
    i = lo +1   # i will seperate the elements those <p and >p
    for j in xrange( i, hi+1 ) : # go through unpartitioned array
        if lists[j] < p:   # find a element should move 2 left
            lists[i],lists[j] = lists[j],lists[i]
            i += 1

    lists[lo] , lists[i-1] = lists[i-1] , lists[lo]

    # recursive
    QuickSort( lists , i , hi  )  # 大于 等于P的element 
    QuickSort( lists , lo , i-2  ) # 小于p的element, i-1是p,不再进行排序
```

> 算法分析:

 - bad case: 快速排序一个sorted array, 每次选 1st element as pivot, 时间复杂度 O(n²)
 - avarage case: 时间复杂度 O(nlogn) , n+(n-1)+(n-2)+...+1

