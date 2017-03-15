...menustart

 - [TAOCP vol1](#ef556f8430878dce1c4748706e6134b4)
 - [BASIC CONCEPTS](#df75a5f0aea7cf7cc075da817b518350)
	 - [1.1 ALGORITHMS](#ea17b4667598db12d332dcfb28af6d6f)
		 - [Algorithm E (Euclid ’s algorithm).](#98230acef1ea79f00d054abf063049b8)
	 - [1.2. MATHEMATICAL PRELIMINARIES](#b0a028097eeef8c671b55c21acb734aa)
		 - [1.2.1. Mathematical Induction 数学归纳法](#c9c5e422aa21b3673c8ea74c36d80e73)
			 - [Algorithm E (Extended Euclid’s algorithm).](#e34888a37bff7ab2db8c92522280445b)
		 - [1.2.2. Numbers, Powers, and Logarithms](#a669d5d2df4ad6ad6cf4835f7f05fcff)
		 - [1.2.3. Sums and Products](#27e7dea388786b255b61cbfa9ee7e2c0)
		 - [1.2.4 Integer Functions and Elementary Number Theory](#b07d9a8cd6c423d1d592afc67680b012)

...menuend


<h2 id="ef556f8430878dce1c4748706e6134b4"></h2>

# TAOCP vol1

<h2 id="df75a5f0aea7cf7cc075da817b518350"></h2>

# BASIC CONCEPTS

<h2 id="ea17b4667598db12d332dcfb28af6d6f"></h2>

## 1.1 ALGORITHMS

我们使用 4级title 来标记算法

<h2 id="98230acef1ea79f00d054abf063049b8"></h2>

#### Algorithm E (Euclid ’s algorithm). 

Given two positive integers m and n, find their greatest common divisor, that is, the largest positive integer that evenly divides both m and n.

 - E1. [Find remainder.] Divide m by n and let r be the remainder. (We will have 0 ≤ r ≤ n.)
 - E2. [Is it zero?] If r = 0,the algorithm terminates; n is the answer.
 - E3. [Reduce.] Set m ← n , n ← r , and back to step E1.

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_F1.png)

```
m = 119 , n = 544
m/n , r ← 119 ;   m ← 554 , n ← 119
```

我们发现, 如果 m < n , 一次迭代只是无谓地交换 m,n : m ⟷ n.  We could add a new step:

```
E0. [Ensure m ≥ n.] if m < n , exchange m ⟷ n.
```


<h2 id="b0a028097eeef8c671b55c21acb734aa"></h2>

## 1.2. MATHEMATICAL PRELIMINARIES

1.2.10 要特别注意！！

<h2 id="c9c5e422aa21b3673c8ea74c36d80e73"></h2>

### 1.2.1. Mathematical Induction 数学归纳法

Let P(n) be some statement about the integer n; for example, P(n) might be "n times (n+ 3) is an even number", or "if n ≥ 10, then 2ⁿ > n³ ". Suppose we want to prove that P(n) is true for all positive integers n. An important way to do this is:

 - a) Give a proof that P(1) is true
 - b) Give a proof that “if all of P(1), P(2), ...,P(n) are true, then P(n + 1) is also true”; this proof should be valid for any positive integer n.

Example:

```
		  1 = 1²,
	    1+ 3 = 2², 
	  1+ 3+ 5 = 3², 
	1+ 3+ 5+ 7 = 4²,
  1+ 3+ 5+ 7+ 9 = 5²,	(1)
```

We can formulate the general property as follows:

```
1 + 3 + ... + (2n—1) = n².	(2)
```

Let us, for the moment, call this equation P(n);we wish to prove that P(n) is true for all positive n. We have:

 - a) “P(1) is true, since 1 = 1².”
 - b) “If all of P(1), . . . , P(n) are true, then, in particular, P(n) is true, so Eq. (2) holds; adding 2n+ 1 to both sides we obtain
 	- 1 + 3 + ... + (2n—1) + (2n+1) = n² + 2n + 1 = (n+1)² ,
 	- which proves that P(n + 1) is also true.”

We can regard this method as an *algorithmic proof procedure*. In fact, the following algorithm produces a proof of P(n) for any positive integer n, assuming that steps (a) and (b) above have been worked out:

**Algorithm I** (Construct a proof). Given a positive integer n, this algorithm will output a proof that P(n) is true.

 - I1. [ProveP(1).] Set k ← 1, and, accordingto (a), output a proof of P(1).
 - I2. [k = n?] If k = n, terminate the algorithm; the required proof has been output.
 - I3. [ProveP(k + 1).] According to (b), output a proof that “If all of P(1), ... , P(k) are true, then P(k + 1) is true.” Also output “We have already proved P(1), ... ,P(k); hence P(k + 1) is true.”
 - I4. [Increase 13.] Increase k by 1 and go to step I2.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_Algorithm_I.png)

Since this algorithm clearly presents a proof of P(n), for any given n, the proof technique consisting of steps (a) and (b) is logically valid. It is called *proof by mathematical induction*.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_F3.png)

---

We define the *Fibonacci sequence* F₀, F₁, F₂, ...,  by the rule that F₀ = 0, F₁ = 1, and every further term is the sum of the preceding two. Thus the sequence begins 0, 1, 1, 2, 3, 5, 8, 13, ..., we will investigate it in detail in Section 1.2.8. We will now prove that if ∅ is the number (1+ √5)/2 we have

```
	F𝑛 ≤ ∅ⁿ⁻¹	(3)
```

for all positive integers n. Call this formula P(n).

If n= 1,then F₁ = 1 = ∅⁰, so step (a) has been done. For step (b) we notice first that P(2) is also true, since F₂ = 1 < 1.6 < ∅¹. Now, if all of P(1), P(2), ... , P(n) are true and n > 1, we know in particular that P(n —1) and P(n) are true; so F𝑛₋₁ ≤ ∅ⁿ⁻² and F𝑛 ≤ ∅ⁿ⁻¹. Adding these inequalities, we get

```
F𝑛₊₁ = F𝑛₋₁ + F𝑛 ≤ ∅ⁿ⁻² + ∅ⁿ⁻¹ = ∅ⁿ⁻²(1+∅).   (4)
```

The important property of the number ∅,indeed the reason we chose this number for this problem in the first place, is that

```
1 + ∅ = ∅ⁿ 	(5)
```

So we get `F𝑛₊₁ ≤ ∅ⁿ` , which is P(n+1). So step (b) has been done, and (3) has been proved by mathematical induction.

Notice that we approached step (b) in two different ways here: We proved P(n+ 1) directly when n = 1, and we used an inductive method when n > 1. This was necessary,since when n = 1 our referenceto P(n —1) = P(O) would not have been legitimate.

Mathematical induction can also be used to prove things about algorithms. Consider the following generalization of Euclid’s algorithm.

<h2 id="e34888a37bff7ab2db8c92522280445b"></h2>

#### Algorithm E (Extended Euclid’s algorithm).

Given two positive integers m and n, we compute their greatest common divisor d and two integers a and b, such that am + bn = d.

 - E1. [Initialize] Set a’ ← b ← 1, a ← b’ ← 0, c ←m, d ←n.
 - E2. [Divide] Let q and r be the quotient and remainder, respectively, of c divided by d. (We have c = qd + r and 0 ≤ r < d.)
 - E3. [Remainder zero?] If r = 0, the algorithm terminates; we have in this case am + bn = d as desired.
 - E4. [Recycle] Set c ← d, d ← r, t ← a’, a’ ← a, a ← t - qa, t ← b’, b’ ← b, b ← t — qb, and go back to E2.

如果从这个算法中删除变量 a,b,a',b', 而且实用 m 和 n 作为辅助变量 c,d ， 我们就得到原先的算法 1.1E.

TODO

EXERCISES 

(a) Prove the following theorem of Nicomachus(A.D. c. 100) by induction:

```
1³= 1, 2³= 3+ 5, 3³= 7+ 9+ 11, 4³= 13+ 15+ 17+ 19 ,etc.
```

(b)Use this result to prove the remarkable formula 

```
1³+ 2³+ ... + n³ = (1 + 2 + ... + n)².
```

---

<h2 id="a669d5d2df4ad6ad6cf4835f7f05fcff"></h2>

### 1.2.2. Numbers, Powers, and Logarithms


**log<sub>b</sub>(xy) = log<sub>b</sub>x + log<sub>b</sub>y, if x>0, y>0**. &nbsp;&nbsp;&nbsp; (11)


**log<sub>b</sub>(cʸ) = ylog<sub>b</sub>c, if c>0**. &nbsp;&nbsp;&nbsp;  (12)

Relationship between lg and log₁₀ :

**log₁₀x  = log₁₀(2<sup>lgx</sup>) = (lgx)(log₁₀2)**

Hence lgx = log₁₀x/log₁₀2 , and in general we find that

**log<sub>c</sub>x =  log<sub>b</sub>x / log<sub>b</sub>c **. &nbsp;&nbsp;&nbsp;  (14)

Equations (11), (12), and (14) are the fundamental rules for manipulating logarithms.

**lnx = log<sub>e</sub>x**.  &nbsp;&nbsp;&nbsp;  (15)

---

<h2 id="27e7dea388786b255b61cbfa9ee7e2c0"></h2>

### 1.2.3. Sums and Products

 - a) *The distributive law*, for products of sums:
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_4.png)
 	- To understand this law, consider for example the speical case:
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_4.1.png)
 - b) *Change of variable:*
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_5.png)
 	- This equation represents two kinds of transformations. 
 		- In the first case we are simply changing the name of the index variable from i to j. 
 		- The second case is more interesting: Here p(j) is a function of j that represents a *permutation* of the range; 
 			-  more precisely, for each integer i satisfying the relation r(i), there must be exactly one integer j satisfying the relation p(j) = i. 
 			- This condition is always satisfied in the important cases p(j) = c + j and p[j] = c —j, where c is an integer not depending on j, and these are the cases used most frequently in applications. For example:
 				- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_6.png)
 	- The replacement of j by p(j) cannot be done for all infinite sums. The operation is always valid if p(j) = c ± j, 
 	- p(j) = `c + j = i`  → `j = i - c` 
 - c) *Interchanging order of summation:*
 	- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_7.png)
 	- Let us consider a very simple special case of this equation:
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_7.1.png)
 	- By Eq. (7), these two are equal; this says no more than
 		- ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_sum_8.png)
 		- where we let bᵢ = aᵢ₁ and cᵢ = aᵢ₂.
 	- The operation of interchanging the order of summation is extremely useful, since it often happens that know simple form for Σ<sub>R</sub>₍ᵢ₎ aᵢⱼ , but not for Σ<sub>S</sub>₍ⱼ₎ aᵢⱼ.
 	- TODO

---

<h2 id="b07d9a8cd6c423d1d592afc67680b012"></h2>

### 1.2.4 Integer Functions and Elementary Number Theory

If a is any real number, we write   ⎣x⎦ = floor(x) , ⎡x⎤ = ceil(x).

 - ⎣-x⎦ = - ⎡x⎤

We define:  x mod y = x — y⎣x / y⎦ , if y ≠ 0; x mod 0 = x. (1)










