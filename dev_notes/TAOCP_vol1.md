
# TAOCP vol1

# BASIC CONCEPTS

## 1.1 ALGORITHMS

#### Algorithm E (Euclid ’s algorithm). 

Given two positive integers m and n, find their greatest common divisor, that is, the largest positive integer that evenly divides both m and n.

 - E1. [Find remainder.] Divide m by n and let r be the remainder. (We will have 0 ≤ r ≤ n.)
 - E2. [Is it zero?] If r = O,the algorithm terminates; n is the answer.
 - E3. [Reduce.] Set m ← n , n ← r , and back to step E1.

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/TAOCP_F1.png)

