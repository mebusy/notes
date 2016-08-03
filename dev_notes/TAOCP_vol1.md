...menustart

 - [TAOCP vol1](#ef556f8430878dce1c4748706e6134b4)
 - [BASIC CONCEPTS](#df75a5f0aea7cf7cc075da817b518350)
	 - [1.1 ALGORITHMS](#ea17b4667598db12d332dcfb28af6d6f)
		 - [Algorithm E (Euclid ’s algorithm).](#98230acef1ea79f00d054abf063049b8)

...menuend



<h2 id="ef556f8430878dce1c4748706e6134b4"></h2>
# TAOCP vol1

<h2 id="df75a5f0aea7cf7cc075da817b518350"></h2>
# BASIC CONCEPTS

<h2 id="ea17b4667598db12d332dcfb28af6d6f"></h2>
## 1.1 ALGORITHMS

<h2 id="98230acef1ea79f00d054abf063049b8"></h2>
#### Algorithm E (Euclid ’s algorithm). 

Given two positive integers m and n, find their greatest common divisor, that is, the largest positive integer that evenly divides both m and n.

 - E1. [Find remainder.] Divide m by n and let r be the remainder. (We will have 0 ≤ r ≤ n.)
 - E2. [Is it zero?] If r = O,the algorithm terminates; n is the answer.
 - E3. [Reduce.] Set m ← n , n ← r , and back to step E1.

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_F1.png)

