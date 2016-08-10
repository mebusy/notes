...menustart

 - [TAOCP vol1](#ef556f8430878dce1c4748706e6134b4)
 - [BASIC CONCEPTS](#df75a5f0aea7cf7cc075da817b518350)
	 - [1.1 ALGORITHMS](#ea17b4667598db12d332dcfb28af6d6f)
		 - [Algorithm E (Euclid ’s algorithm).](#98230acef1ea79f00d054abf063049b8)
	 - [1.2. MATHEMATICAL PRELIMINARIES](#b0a028097eeef8c671b55c21acb734aa)
		 - [1.2.1. Mathematical Induction 数学归纳法](#c9c5e422aa21b3673c8ea74c36d80e73)

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
 - E2. [Is it zero?] If r = O,the algorithm terminates; n is the answer.
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
















