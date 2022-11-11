[](...menustart)

- [Week6 Week7 期望值 条件概率 失忆性](#884b6b277b1c5c27d38fbc97f6560af9)
    - [6-2: 期望值 I (EXPECTATION)](#699f5bed3f92e270bce0a95ed5bf89d3)
        - [随机变量的函数之期望值](#7a410c29ec1783458c2d5c679f790eee)
        - [期望值运算性质](#09a5fcc38b3f4c96f745b665bfb42cea)
        - [常见的随机变量函数期望值](#487e3e26c9963764a55fe4f8b597d389)
        - [变异数 (variance)](#d43aa7d625393a9c328a86c60568b12e)
        - [Variance 便利算法](#d57572a47dea71843856503c0ef5c154)
        - [常见离散分布之期望值/变异数](#33805636b57d3a4f61be9c79a1d93947)
        - [几率推导奥义： 「凑」字诀](#367685545196820c0c173d14fe4c9421)
        - [Quiz](#ab458f4b361834dd802e4f40d31b5ebc)
- [Week7](#b9d0e738b55594e8d3824de9b91b0914)
    - [7-1 期望值II](#041a19cd2e4bebb61913e1566b7cfb67)
        - [随机变数函数 期望值](#45c2600156e6a1f700dfe4260c9694c4)
        - [常见连续分布的期望值/变异数](#29e116aede7ee7f00af95ca5edd4c6d0)
        - [期望值推导](#4fdbd553cf6f3c5cfd46baa1993c8dc2)
    - [7.2 隨機變數之函數](#27fdd10ac05020268c5d6bb6954f4099)
        - [如何求 g(X)几率分布?](#317aa5bd89ce045575f8cb8491b70c62)
    - [7.3a 条件概率分布](#33f8148fbbdcedb32e214651afcff8d9)
    - [7.3a 失忆性 (Memoryless)](#f16b66e705a9a610a0da37b5dae105eb)
    - [QUIZ](#e1f7ff5183a361cd3b41e3ab5e647cb5)

[](...menuend)


<h2 id="884b6b277b1c5c27d38fbc97f6560af9"></h2>

# Week6 Week7 期望值 条件概率 失忆性


<h2 id="699f5bed3f92e270bce0a95ed5bf89d3"></h2>

## 6-2: 期望值 I (EXPECTATION)

- 大数法则
    - 想知道某事件发生的机率?
    - 作很多次实验，记录实验中出现那个事件多少次。当实验次数接近无穷 多次时，这个比例就会越来越接近实际的机率!
    - P(A) = lim<sub>N→∞</sub> (N<sub>A</sub>/N)
- 期望值 (Expectation)
    - 做随机实验时，我们很希望能有某种估算
    - 平均值是我们平常最常普遍的估算值
    - 作两次实验的平均值是? (X₁+X₂)/2 = ?
    - 不管我们做多少次实验，平均值都是一个随机变数，那不就 不能拿来估算?
    - 所幸!当做的实验次数趋近于无穷多时，这么多次的实验的平均值 会收敛到一个常数!我们就用它来当作这机率分布的估算值吧!
- 若考虑某机率分布，作实验很多次若随机实验之样本空间为 {1,2, ... ,n}, 作实验N次，记录各结果出现 次数，分别为N₁,N₂,...N<sub>n</sub>
    - 平均值 (Mean): ∑<sub>x=</sub>ⁿ₁ (x·Nₓ)/N
    - 根据大数法则 : ∑<sub>x=</sub>ⁿ₁ x·P<sub>X</sub>(x)
- Mean 值又称作期望值
    - μ<sub>Y</sub> = E[Y]
    - 对离散随机变数 𝑿 而言，我们定义其期望值 
        - E[X] = μ<sub>X</sub> = ∑<sub>x=</sub><sup>∞</sup><sub>-∞</sub> x·P<sub>X</sub>(x) 
    - **期望值不等于随机会发生的值**!
        - eg. P<sub>X</sub>(1) = P<sub>X</sub>(-1) = 1/2 => μ<sub>X</sub> = 0 !!! 

 
<h2 id="7a410c29ec1783458c2d5c679f790eee"></h2>

### 随机变量的函数之期望值

- 对于任一离散随机变量 X 而言，其 任意函数 g(X) 亦是一随机变量，亦有期望值
- g(X) 期望值定义为
    - E[ g(X) ] = ∑<sub>x=</sub><sup>∞</sup><sub>-∞</sub> g(x)·P<sub>X</sub>(x) 
    - 根随即变量的期望值公式相比，只是 x 变成了 g(x)

<h2 id="09a5fcc38b3f4c96f745b665bfb42cea"></h2>

### 期望值运算性质

- E[ 3X² ] = ∑<sub>x=</sub><sup>∞</sup><sub>-∞</sub> 3x²·P<sub>X</sub>(x) 
    - = 3·∑<sub>x=</sub><sup>∞</sup><sub>-∞</sub> x²·P<sub>X</sub>(x)  = 3·E[X²]
    - 常数项可以提出来
- E[α·g(X)] = α·E[g(X)] 
- E[α·g(X) + β·h(X) ] = α·E[g(X)] + β·E[h(X)]
- E[α] = α
 
<h2 id="487e3e26c9963764a55fe4f8b597d389"></h2>

### 常见的随机变量函数期望值
 
- X 的 n<sup>th</sup> moment:
    - E[Xⁿ] = ∑<sub>x=</sub><sup>∞</sup><sub>-∞</sub> xⁿ·P<sub>X</sub>(x)  
    - Ex: E[X²] 是 X的 2<sup>nd</sup> moment
- X 的变异数 (variance):
    - E[ (X-μ<sub>X</sub>)² ] 
    - 减去 期望值的 平方
- 全期望值公示
    - E[Y] = E[E(Y|X)]

<h2 id="d43aa7d625393a9c328a86c60568b12e"></h2>

### 变异数 (variance)

- Variance通常符号表示为 σ<sub>X</sub>² = E[ (X-μ<sub>X</sub>)² ] 
- 变异数隐含关于随机变数 X 多「乱」的信息
- 变异数的开根号便是标准差 (standard deviation)
    - σ<sub>X</sub> = √Variance
- 性质:
    - if a constant is added to all values of the variable, the variance is unchanged:
        - Var[X + a] = Var[X]
    - If all values are scaled by a constant, the variance is scaled by the square of that constant:
        - Var[aX] = a²Var[X]
- 双变量 期望值，Variance，见第8章

<h2 id="d57572a47dea71843856503c0ef5c154"></h2>

### Variance 便利算法

- σ<sub>X</sub>² = E[ (X-μ<sub>X</sub>)² ]
    - = E[ X²-2μ<sub>X</sub>·X+μ<sub>X</sub>² ]
    - = E[X²] + E[-2μ<sub>X</sub>·X] + E[ μ<sub>X</sub>² ]
    - = E[X²] - 2μ<sub>X</sub>·E[X] + μ<sub>X</sub>²
    - = E[X²] - μ<sub>X</sub>² 

- => E[X²] = σ<sub>X</sub>² + μ<sub>X</sub>²  


<h2 id="33805636b57d3a4f61be9c79a1d93947"></h2>

### 常见离散分布之期望值/变异数

- X~Bernouli(p) :
    - μ<sub>X</sub> = 1·p + 0·(1-p) = p
    - σ<sub>X</sub>² = E[X²] - μ<sub>X</sub>² = ∑<sub>x=</sub>¹₀ x²·p<sub>X</sub>(x) - μ<sub>X</sub>²
        - = 1²·p + 0²·(1-p) - p² = p(1-p)
- X~BIN(n,p) :
    - μ<sub>X</sub> = np
    - σ<sub>X</sub>² = np(1-p)
- X~GEO(p) :
    - μ<sub>X</sub> = ∑<sub>x=</sub><sup>∞</sup><sub>0</sub> x· (1-p)<sup>x-1</sup>·p = 1/p 
    - σ<sub>X</sub>² = E[X²] - μ<sub>X</sub>² = (1-p)/p²
- X~PASKAL(k,p) :
    - μ<sub>X</sub> = k/p
    - σ<sub>X</sub>² = k(1-p)/p²  
- X~POI(α) :
    - μ<sub>X</sub> = α
    - σ<sub>X</sub>² = α 
- X~UNIF(a,b) :
    - μ<sub>X</sub> = (a+b)/2
    - σ<sub>X</sub>² = 1/12·(b-a)(b-a+2)

<h2 id="367685545196820c0c173d14fe4c9421"></h2>

### 几率推导奥义： 「凑」字诀

- 以 X~POI(a) 为例
- X~POI(a) 概率公式是什么？
    - P<sub>X</sub>(x) = (aˣ/x!)·e⁻ª , x=0,1,2,... 
- 我们手上能利用的公式有哪些？
    - ∑<sub>x=</sub><sup>∞</sup><sub>0</sub> (aˣ/x!)·e⁻ª = 1
- 开始推导:  

---

E[X] = ∑<sub>x=</sub><sup>∞</sup><sub>0</sub> x·(aˣ/x!)·e⁻ª 

x 和 x！约分，变成 (x-1)! , 这样 ∑ 运算就不能包括 x=0了， 因为 阶乘对负数没有定义

 E[X] = ∑<sub>x=</sub><sup>∞</sup><sub>1</sub> (aˣ/(x-1)!)·e⁻ª 

使 a 的指数形式 和 阶乘 保持一致

 E[X] = a·∑<sub>x=</sub><sup>∞</sup><sub>1</sub> (aˣ⁻¹/(x-1)!)·e⁻ª 

令 x' = x-1 

 E[X] = a· ∑<sub>x'=</sub><sup>∞</sup><sub>0</sub>  (aˣ<sup>'</sup>/x'!)·e⁻ª = a·1 = a 
 
--- 


σ<sub>X</sub>² = E[X²] - μ<sub>X</sub>² = E[X²] - a² 

和 E[X] 类似， 可以推导处 E[X²] =  a² + a , 所以

σ<sub>X</sub>² =  a 

---


<h2 id="ab458f4b361834dd802e4f40d31b5ebc"></h2>

### Quiz

<details>
<summary>
quiz...
</summary>

1. 一个随机变数X, E[X]=μ, Var[X]=σ², σ>0 请问下列何者叙述正确(正確選項只有一個)
    - Y=-X, E[Y]=-μ, Var[Y]=σ²
        - 正确: E[-X]=-E[X] , Var[-X]=(-1)²Var[X]
    - Y=(X-μ)/σ² 会是一个均值为1，且标注差也为1的 Gaussian 随机函数
        - ❌
    - Y=-μ·X , 则 E[Y]=μ², Var[Y] = -μ²σ
        - ❌
    - Y=2X+4 , 则 E[Y]=2μ+4, Var[Y] = 2σ²
        - ❌ Var[Y] = 4σ²
2. 小米到學校後才得知今天 要小考，但是上課睡覺、下課玩的小米什麼 都沒有準備，考卷發下來後，發現考題是5題選擇題，每題都有 A、B、C、D四個選項，每題只有一個正確答案，每題20分。已知小米決定每題都猜C，隨機變數S代表小米這次考試總共答對的題數，可以發現S是個Binomial Random Variable，請問小米答對題數的期望值是多少 E[S] = ?
    - E[S]= np = 5*0.25 = 1.25
3. 承續上題小米的考試，已知小米全部都猜 C，而且又已經知道這次考試第一題答案真的是C，而隨機變數S代表小米這次考試總得分，S的變異數是Var[S]=σ², 请问σ是多少?
    - 注: 已经不是 Binomial 分布了
4. 阿壘投籃平均進球率是 60% ，某日他好友阿拓在旁提議 ，如果阿壘可以連續進 10球，就停止射球並且阿拓會請阿壘一瓶運動飲料。隨機變數B是指阿壘這場賭注裡總共的進籃球數 (ex: B=6 就是指阿壘只投進六球，第七球沒投進)，則請問 E[B]=?
    - note: 不是简单的计算几何分布的期望值，因为第10球和前面的9球不一样，而且投中第10球后，就结束了
    - p<sub>投不进</sub>=0.4, E[B] = ∑<sub>i=0</sub>⁹ i*pmf(i+1) +  10* (0.6**10)
        ```python
        >>> sum( [ i* stats.geom.pmf( i+1, 0.4 )  for i in range(10) ] ) + 10* (0.6**10)
        1.4909300736
        # 暴力验证
        >>> p = 0.4
        >>> r = 0
        >>> for nBallScore in xrange(11):
        ...     x = nBallScore +1 
        ...     r += (1-p)**(x-1)*( p if nBallScore <10 else 1 ) * nBallScore
        ... 
        >>> r
        1.4909300736
        ```

5. 某國的籃球 聯盟季後賽，由東隊對上 西隊 ，要在 5場比賽內決定 誰是這國家今 年最強的籃球 隊伍，當某一隊伍 取得 3場勝利的時候 ，這季後 賽馬上就結束確 定由三勝的球隊取得最後的冠軍寶座 。假設按照 幾年來的對戰統計 ，一場東隊 碰上西隊 的比賽，東隊獲勝的機率 是 60 %，而西隊獲勝的機率 則是 40 %。隨機變 數 N代表這次季後賽在總冠軍確定時，總共比賽的場數。請問N的期望值是?
    - 同样，这也简单的计算 PASKAL 期望值，因为到第5场就结束了
    - N 可能等于3,4,5
    - 4.07
        ```python
        >>> p = 0.6
        >>> 
        >>> 3*p**3 + 3*(1-p)**3
        0.84

        >>> 4*p**3*(1-p)*3 + 4*(1-p)**3*p *3
        1.4976

        >>> 5*p**2*(1-p)**2 * 6 
        1.7280000000000002

        >>> 1.7280000000000002 + 1.4976 + 0.84
        4.0656
        ```
6. 小惠拿到了全校身高，性别的资料。發現全校的身高資料是個Gaussian Distribution H~Guassian( 178.32, 5.83 )。并且发现 测量用的尺有兩個地方設計不良：
    - 1. 用皮尺去量公正尺上一毫米(mm)的刻度，發現皮尺量出來是1.1毫米
    - 2. 皮尺並不是從0 公分 做為開端，竟然是以 1 公分 做為開端，也就是量身高的時候醫師替各位同學都多加 1 公分了
    - 發現這件慘案後，不僅全校剛剛量測結束的身高資料都錯誤，小惠的研究也陷入困境。但是小惠突然想起 丙紳老師教授過隨機變數的性質，發現如果皮尺只有這兩種誤差的話，那麼這些資料是可以還原成正確的身高資料的! 也就是假設隨機變數 X是隨機找一位小惠國中同學的真正身高(單位 cm)，則可以藉由小惠剛剛發現的兩種誤差推導出 H 與 X 的關係，則X 也就是全校同學的真正身高資料就可以還原了。
    - 請問下列敘述何者正確? (正確的選項只有一個)
        -  小惠全校真實身高的標準差為5.3 cm
        - ❌ 若 μ<sub>X</sub> = E[X], 则 μ<sub>X</sub> = 1.1μ<sub>H</sub> + 1
        - ❌ Var[X] = 38.44
        - ❌ 若存在函数 g(x) 使得 H=g(X), 则可以推得 随机变数H,X 的标准差 σ<sub>H</sub>, σ<sub>X</sub> ,  会存在 σ<sub>H</sub> = g( σ<sub>X</sub>) 的关系
    - H = 1 + 1.1X => X = (H-1)/1.1 = H/1.1 - 1/1.1
        - E[X] = E[H]/1.1 - 1/1.1 = 178.32 /1.1 - 1/1.1 = 161.2
        - Var[X] = Var[H]/(1.1**2) = (5.83**2)/(1.1**2) = 28.09
            - σ<sub>X</sub> = 5.3
            - 5.83 ≠ 1 + 5.3*1.1 = 1 + 5.3*1.1

</details>

<h2 id="b9d0e738b55594e8d3824de9b91b0914"></h2>

# Week7 

<h2 id="041a19cd2e4bebb61913e1566b7cfb67"></h2>

## 7-1 期望值II

- 对连续的随机变数X而言，想求期望值，我们用类似 离散随机变数的方式出发
- 将X的值 以Δ为单位 无条件舍去来近似结果 离散随机变数 Y 
    - 当 Δ → 0时， X≈Y , 当Δ趋近0的时候，Y接近Y
    - X∈[0,1Δ) -> Y=0Δ
    - X∈[1Δ,2Δ) -> Y=1Δ
    - X∈[nΔ,(n+1Δ) -> Y=nΔ
- 根据第五周
    - p<sub>Y</sub>(nΔ) = P(nΔ ≤ X < nΔ+Δ) ≈ f<sub>X</sub>(nΔ)·Δ
- E[X] = lim<sub>Δ→0</sub>E[Y] = lim<sub>Δ→0</sub> ∑<sub>n=-∞</sub><sup>∞</sup> nΔ·P<sub>Y</sub>(nΔ)
    - = ∫<sub>-∞</sub><sup>∞</sup> xf<sub>X</sub>(x)dx
    - 即， x乘上pdf,然后积分
        - 一般来说, 求一个 函数 f(x) 在 x∈ [a,b] 之间的均值, 一般是 求出原函数F, 均值就是 (F(b)-F(a))/(b-a)
        - pdf 本身就蕴含一点均值的计算，求期望值只需要计算 F(b)-F(a) ?

<h2 id="45c2600156e6a1f700dfe4260c9694c4"></h2>

### 随机变数函数 期望值

- 对于任一连续随机变数X，其任意函数g(X)亦是一随机变数
    - E[g(X)] = ∫<sub>-∞</sub><sup>∞</sup> g(x)f<sub>X</sub>(x)dx

<h2 id="29e116aede7ee7f00af95ca5edd4c6d0"></h2>

### 常见连续分布的期望值/变异数

- X ~ Exponential(λ)
    - μ = 1/λ
    - σ² = 1/λ²
- X ~ Erlang(n,λ)
    - μ = n/λ
    - σ² = n/λ²
- X ~ Gaussian(μ,σ)
    - μ = μ
    - σ² = σ²
- X ~ UNIF(a,b)
    - μ = (a+b)/2
    - σ² = 1/12 · (b-a)²

<h2 id="4fdbd553cf6f3c5cfd46baa1993c8dc2"></h2>

### 期望值推导

- 一些有用的微积分性质
    - e<sup>`*`</sup>𝑑`*` = 𝑑e<sup>`*`</sup>
    - ∫U𝑑V = UV - ∫VdU
    - ∫c𝑑x = ∫𝑑cx  , c 是常数
    - ∫pdf = 1

<h2 id="27fdd10ac05020268c5d6bb6954f4099"></h2>

## 7.2 隨機變數之函數

- 随机变数X的任意函数g(X)也是一个随机变数
- 通常被称为 Derived Random Variable
    - 从 random variable X 衍生出来的一个新的random variable


<h2 id="317aa5bd89ce045575f8cb8491b70c62"></h2>

### 如何求 g(X)几率分布?

- 若X为离散
    - 直接推 g(X) 的 PMF
- 若X为连续
    - 先推 g(X)的CDF， 再微分得到PDF

- Ex:某宅宅超爱战LOL。每次一战就连续战 𝑿 场不可收拾，已知 𝑿~GEO(0.2)。某宅宅内心仍有 一点清明，其良心亦会因战过度而内疚，依战的次数 多寡，内疚程度 𝒀分别为1, 2, 3 不同等级:
    ```
               ⎧ 1, if 1≤X≤3
    Y = g(X) = ⎨ 2, if 4≤X≤6
               ⎩ 3, if X≥7
    ```
    - 问Y=g(X)的几率分布?
    - 解: X~GEO(0.2) => p<sub>X</sub>(x) = (1-0.2)<sup>x-1</sup>·0.2
        - p<sub>Y</sub>(1) = p<sub>X</sub>(1)+p<sub>X</sub>(2)+p<sub>X</sub>(3) 
            - = 0.2 + 0.8·0.2 + 0.8²·0.2
        - p<sub>Y</sub>(2) = p<sub>X</sub>(4)+p<sub>X</sub>(5)+p<sub>X</sub>(6) 
            - = (0.8)³·0.2 + (0.8)⁴·0.2 + (0.8)⁵·0.2
        - p<sub>Y</sub>(3) = P(Y=3) = 1-p<sub>Y</sub>(2)-p<sub>Y</sub>(3)
- 离散g(X)
    - Y = g(X) 的 PMF为 
    - ![](../imgs/TU_prob2_gx_PMF.png)
- 连续g(X) 
    - 先计算g(X)的CDF: 
        - F<sub>g(X)</sub>(y) = P[g(X)≤y]
    - 若 g(X)可微分, 再对y微分得到PDF:
        - ![](../imgs/TU_prob2_gx_PDF.png)
- 连续g(x) = aX + b
    - Ex1: 若Y=3X+2, 请问Y的PDF 跟f<sub>X</sub>(x)之关系为何?
    - F<sub>Y</sub>(y) = P(Y≤y)
        - = P(3X+2≤y)
        - = P(X≤(y-2)/3 )
        - = F<sub>X</sub>( (y-2)/3 )
    - f<sub>Y</sub>(y) = f<sub>X</sub>( (y-2)/3 )·(1/3)
    - generic solution:
        - f<sub>Y</sub>(y) = (1/|a|)·f<sub>X</sub>( (y-b)/a )

    - Ex2: X~Exponential(λ) , Y = 2X
    - f<sub>X</sub>(x) = λe<sup>-λx</sup>u(x), Y=2x (a=2,b=0)
        - 这里 u(x)是工程上常见的一个函数，表示只有x>0时有值，即x>0时u(x)=1, 其他情况u(x)=0
    - f<sub>Y</sub>(y) = (1/|a|)·f<sub>X</sub>( (y-b)/a )
        - = 1/2·λe<sup>-λ·y/2</sup>·u(y/2)   (a,b代入)
        - = λ/2·e<sup>-λ/2·y</sup>·u(y) 
        - => Y~Exponential(λ/2)
- 连续g(x) = aX² + b
    - Ex: Y = 2X²+1, X~UNIF(-1,7), 求 Y的PDF
    - 不要好高骛远，先算CDF
    - F<sub>Y</sub>(y) = P(Y=2X²+1≤y)
        - = P(X²≤(y-1)/2)
        - = P( -√((y-1)/2) ≤ X ≤ √((y-1)/2) )
        - = ∫<sub>-z</sub><sup>z</sup>f<sub>X</sub>(x)dx  , 令 z = √((y-1)/2)
    - 需要注意积分的范围, 这里注意 Y > 3的情况
        - y≤3: F<sub>Y</sub>(y) = ∫<sub>-z</sub><sup>z</sup>1/8dx = 
        - y>3: F<sub>Y</sub>(y) = ∫<sub>-1</sub><sup>z</sup>1/8dx =
        - 微分得到 f<sub>Y</sub>(y)

<h2 id="33f8148fbbdcedb32e214651afcff8d9"></h2>

## 7.3a 条件概率分布 

- Ex:为了更了解宅宅的心，店员妹亦开始战 LOL。 已知店员妹战LOL场数 𝑿~UNIF (1, 5)。若已知 店员妹战了两场仍战意甚浓、继续战。请问在此情况下，店员妹 今日战LOL场数 𝑿 之机率分布为何?
    - 条件 B: 已战两场 仍想战
    - p<sub>X|B</sub>(x) = P(X=x|B) = P(X=x,B)/P(B)
        - = (1/5) / (3/5)  = 1/3,  x∈B:x=3,4,5
        - = 0,   x∉B:x=otherwise
- 若𝑿是一离散随机变数，其PMF为 𝒑𝑿(𝒙)。若已知某事件 𝑩 已发生，则在此情况下 之条件机率分布为:
    - ![](../imgs/TU_prob2_cond_dis_PMF.png)
- Ex:店员妹等公交车上班。通常等公交车的时间 𝑿， 从零到十分钟间可能性均等。若店员妹已等了 五分钟车还没来。请问在此情况下，等车时间 𝑿 之机率分布为何?
    - B: X>5 => P(B)=0.5
    - f<sub>X|B</sub> = x∈B: f<sub>X</sub>(x) / P(B)
        - = x∉B: 0
- 若𝑿是一连续随机变量，其PDF为 𝒇𝑿(𝒙)。若已知某事件 𝑩 已发生，则在此情况下 之条件机率分布为:
    - ![](../imgs/TU_prob2_cond_dis_PDF.png)
- 条件期望值 Conditional Expectation 
    - ![](../imgs/TU_prob2_cond_E.png)
    - ![](../imgs/TU_prob2_cond_var.png)


<h2 id="f16b66e705a9a610a0da37b5dae105eb"></h2>

## 7.3a 失忆性 (Memoryless)

- 宅宅与店员妹相约出门。宅宅出门前在战LOL，场数 𝑿~GEO (𝟎.2) 。店员妹等了两场后，宅宅还在玩。 店员妹甚怒，怒催宅宅。宅宅曰「快好了、快好了」。问宅宅剩余场 数 𝑿’ 之机率分布为何?

- 店员妹与宅宅相约出门。店员妹出门前化妆时间为 𝑿(小时)， 𝑿~Exponential(𝟏)。经过一小时后， 仍未完成。宅宅甚怒，怒催店员妹。店员妹曰「快好了、快好了」。 问店员妹剩余化妆时间𝑿′机率分布为何? 

- Geometric 跟 Exponential 机率分布 皆有失忆性的性质
    - 不管事情已经进行多久，对于事情之后的进行 一点影响都没有!



<h2 id="e1f7ff5183a361cd3b41e3ab5e647cb5"></h2>

## QUIZ

<details>
<summary>
quiz...
</summary>

1. X~Exponential( 0.5 ) , 请问下列哪个错误？
    1. Y=2x+1, Var[Y] = 9   (错)
    2. E[X] = 2 
    3. Var[X] = 4 
    4. Y=2x+1, E[Y] = 5 

    - A: 
        - 可以很容易知道 E = 1/0.5 = 2, Var = 1/0.5² = 4
        - E[Y] = E[2X+1] = 2E[X] + E[1] = 4+1 = 5
        - Var[Y] = E[(Y-5)²] = E[Y²] - 25 = E[4X²+4X+1] - 25 = 4E[X²]+4E[X]+1-25
            - = 4·( Var[X] + E[X]² ) + 8+1-25 = 16
        - using scipy
            ```python
            >>> scipy.stats.expon.expect( scale=1/0.5 )
            1.9999999999999998
            >>> scipy.stats.expon.var( scale=1/0.5 )
            4.0
            >>> scipy.stats.expon.expect( func=lambda x:2*x+1,  scale=1/0.5 )
            5.0
            >>> scipy.stats.expon.expect( func=lambda x:x**2,  scale=1/0.5 )
            8.0    # E[X²]
            >>> Y = scipy.stats.expon.rvs(scale=1/0.5 , size=1000000) *2 + 1
            >>> Y.var()
            15.989224062316483
            ```
2. 假設等一班特定的公車所花費的的時間 T 是Uniform Distribution，小速在公車站打滾多年的經驗，已經知道168路公車的平均要花5分鐘等一班公車，請問168號公車是幾分鐘會有一班車經過?
    - A:
        - T~UNIF
        - E[T] = 5 = ( 0 + b) / 2
        - b = 10分钟
3. 星仔跟阿達兩人準備要出席今晚在學校的晚會，為了在晚會上引起眾人目光，星仔決定大手筆打扮自己，但是阿達其實只是為了去吃美食而已。下午3點兩人相約在阿達家集合，因為阿達有車可以載星仔一起去會場，但是星仔帶著所有行頭打算三點才開始在阿達家開始打扮。假設連續隨機變數TT 是星仔打扮所需要的時間(單位 hr)，且T∼Exponential(λ=1/3)。但是晚會六點就開始了，加上從阿達家過去的路程要半小時以上，如果阿達下午五點20以前沒即時出門前往會場，阿達或許就會吃不到今日開場限量的好吃麵包，於是阿達決定就等到下午五點20分，如果星仔依然還沒打扮好，就直接拋下星仔自行前往會場。也就是離散型隨機變數RR代表阿達有沒有成功到達會場:
    - R = 1 if 阿達載星仔到會場 ; R = 0 if 阿達沒有載星仔到會場. 請問，Var[R]=?
    - A: using scipy
        ```python
        >>> P_R1 = scipy.stats.expon.cdf( 2+1/3.0 ,   scale=3)
        >>> P_R1
        0.5405741759640734
        >>> Var = P_R1 * (1-P_R1)  #  Bernoulli
        0.2483537362448364
        ```
4. 同上題情境，如果5點的時候阿達確認星仔還沒打扮完，在此情況下，隨機變數R2==(R∣T>2) 代表最後阿達是否會載星仔到會場，請問E[R2] ?
    - A: using scipy , 由指数分布的失忆性
        ```python
        >>> P_R1 = scipy.stats.expon.cdf( 1/3.0 ,   scale=3)
        >>> P_R1
        0.10516068318563022
        >>> E = P  # Bernoulli
        ```
5. X的CDF 定义如下
    - F<sub>X</sub>(x) = 
        - 0 , 0>x
        - 1-e<sup>-x/2</sup>  ,  x≥0
    - f<sub>X</sub>(x) = e<sup>-x/2</sup> / 2  => X~Exp(2)
        - E[X] = 2 , Var[X] = 4
6. 條件機率的一大應用就是在醫學疾病檢驗的判斷，假設有一疾病只要病患確診，這病患三個月內的死亡率將會是90%，但是人群中只有2%的人確定患有此疾病(Disease)。而如今開發出一套檢驗方式可以針對此疾病作檢驗，根據檢驗結果是陽性(Positive)或是陰性(Negative)以判斷是否染上此疾病，陽性就是出現罹患此疾病會有的現象，陰性則反之。但是這套檢驗方法卻不是百分之百完全準確的，因為有些環境或是其他疾病會讓已經確定自己是健康的人(Health)也檢驗也出陽性，假設這種狀況的機率是0.3%；而實際上已經確定患有此疾病(Disease)但是卻因為一些環境或是體質差異也有可能檢驗出陰性，假設這樣的機率是0.2%。某天小豐擔心自己患上此疾病，於是前往醫院進行這種檢驗，結果檢驗結果為陽性，請幫忙小豐分析，小豐沒有染上此疾病(Health)的機率為何?
    ```
    P(health) = 0.98 , P(disease) = 0.02
    P(positive | health) = 0.003
    P(negative | disease) = 0.002
    求 P( health | positive )
    P( health | positive )  = P(health, positive) / P(positive)

    P(health, positive) = P(positive | health)*P(health) = 0.003 * 0.98
    怎么求 P(positive)？
    P(positive) = P(positive, health ) + P( positive, disease )
                = 0.003 * 0.98 +  P( positive |  disease ) * P( disease )
                = 0.003 * 0.98 + ( 1 - P( negative |  disease ) )  * P( disease )
                = 0.003 * 0.98 + ( 1 - 0.002 ) * 0.02
                = 0.0229
    P( health | positive )  = 0.003 * 0.98 / 0.0229 = 0.128
    ```

</details>
