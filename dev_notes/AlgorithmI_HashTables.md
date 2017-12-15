
# 3.4 HASH TABLES

## hash functions

### Uniform hashing assumption

 - Each key is equally likely to hash to an integer between 0 and M - 1.
 - Bins and balls.
    - Throw balls uniformly at random into M bins.
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_uniform_binball.png)

### Collisions

 - Collision. Two distinct keys hashing to same index.
 - Challenge. Deal with collisions efficiently.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_collision.png)


## separate chaining

 - **Use an array of M < N linked lists**. [H. P. Luhn, IBM 1953]
    - Hash: map key to integer i between 0 and M - 1
    - Insert: put at front of iᵗʰ chain (if not already there).
    - Search: need to search only iᵗʰ chain.


![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_sep_chaining.png)


### Analysis

 - Proposition
    - Under uniform hashing assumption, the probability that the number of keys in a list is within a constant factor of N / M is extremely close to 1.
 - Proof sketch
    - Distribution of list size obeys a binomial distribution.
    - 共有M个list，一个key 落到 list *l* 的概率 p = 1/M
    - 做N次实验，有k个key 落到 *l* 上的概率，服从 binomial distribution
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_sep_chain_proof.png)
    - 令N=10⁴ , M=10³, PMF 函数为:

```python
import scipy, scipy.stats
x = scipy.linspace(0,30,31)
N= 10000
M= 1000
p = 1.0/M
pmf = scipy.stats.binom.pmf(x,N,p)
import pylab
pylab.plot(x,pmf)
pylab.show()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_sep_chain_proof_pmf.png)

 - Consequence: Number of probes for search/insert is proportional to N / M.
    - M too large ⇒ too many empty chains.
    - M too small ⇒ chains too long.
    - **Typical choice: M ~ N / 5 ⇒ constant-time ops**.

## linear probing

### Collision resolution: open addressing

 - Open addressing. [Amdahl-Boehme-Rocherster-Samuel, IBM 1953]
    - When a new key collides, find next empty slot, and put it there.
    - **Hash**. Map key to integer i between 0 and M-1.
    - **Insert**. Put at table index i if free; if not try i+1, i+2, etc.
    - **Search**. Search table index i; if occupied but no match, try i+1, i+2, etc.
 - Note. Array size M **must be** greater than number of key-value pairs N.
 
### Clustering

 - Cluster. A contiguous block of items.
 - Observation. New keys likely to hash into middle of big clusters.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_openaddr_cluster.png)

### Knuth's parking problem

 - Model. 
    - Cars arrive at one-way street with M parking spaces.  Each desires a random space i : if space i is taken, try i + 1, i + 2, etc.
 - Q:
    - What is mean displacement of a car?

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_knuth_packingproblem.png)

 - Half-full. 
    - With M / 2 cars, mean displacement is ~ 3 / 2.
 - Full. 
    - With M cars, mean displacement is ~ √(πM/8)

### Analysis of linear probing

 - Proposition
    - Under uniform hashing assumption, 
    - in a linear probing hash table of size M that contains N = α M keys is:
    - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/algorI_hash_linear_probe_0.png)

 - Parameters
    - M too large ⇒ too many empty array entries.
    - M too small ⇒ search time blows up
    - **Typical choice: α = N / M ~ 1⁄2** 
        - # probes for search hit is about 3/2
        - # probes for search miss is about 5/2




     









