...menustart

 - [Calculus 2](#cfb5ad5012e1f6f82ce9e56414cfbd86)
 - [Week1 : Sequence](#62533905f258da75499c882a124b0317)
	 - [What is a Sequence?](#522feab9f5dbcd13c1a017479d792f7c)
	 - [What is the Limit of a Sequence ?](#b07df8cec51bd3cfbcba058e900c27e1)
		 - [What is an Geometric Progression?](#8797aec0bf798842a337e6476a38df1f)

...menuend


<h2 id="cfb5ad5012e1f6f82ce9e56414cfbd86"></h2>

# Calculus 2

<h2 id="62533905f258da75499c882a124b0317"></h2>

# Week1 : Sequence 

<h2 id="522feab9f5dbcd13c1a017479d792f7c"></h2>

## What is a Sequence?

 - 1,1,2,3,5,8,...
 - a₁,a₂,a₃,a₄,a₅,a₆,...
 - a₆=8, a₃=2
 - we use (a<sub>n</sub>) represents the whole sequence

---

 - "arithmetic progression"
    - a sequence with a common difference between the terms. 
    - 5,12,19,26,33,... 
        - a<sub>n</sub> = a₀+d<sub>n</sub>
    - Why are these things even called arithmetic progressions? 
        - Each term Is the arithmetic mean of its neighbors. 
        - 12 == (5+19)/2 

<h2 id="b07df8cec51bd3cfbcba058e900c27e1"></h2>

## What is the Limit of a Sequence ?

<h2 id="8797aec0bf798842a337e6476a38df1f"></h2>

### What is an Geometric Progression?

 - A geometric progression, is a sequence with a common ratio between the terms.
    - 3,6,12,24,...
 - in a geometric progression, each term is the geometric mean of it's neighbors
 - what is geometric mean ? 
    - the geometric mean of two numbers, of a and b, is defined to be the square root = √(a·b)


## What Other Properties Might a sequence Have ?

###  How Do Sequences Help with the √2 ?

 - x₁ =1
 - x<sub>n+1</sub> =  1/x<sub>n</sub> + x<sub>n</sub>/2
    - x₂ = 3/2
    - x₃ = 17/12 
    - x₅ ≈ 1.41421

### When is a Sequence Bounded?

 - a<sub>n</sub> is "bounded above" means there is a real number M , so that 
    - for all n≥0, a<sub>n</sub> ≤ M 
 - a<sub>n</sub> is "bounded below" means there is a real number M , so that 
    - for all n≥0, a<sub>n</sub> ≥ M 

### When is a Sequence Increasing?

 - A sequence (a<sub>n</sub>) is **increaseing** if whenever m > n , then a<sub>m</sub> > a<sub>n</sub>
 - A sequence (a<sub>n</sub>) is **decreaseing** if whenever m > n , then a<sub>m</sub> < a<sub>n</sub>
 - A sequence (a<sub>n</sub>) is **non-increaseing** if whenever m > n , then a<sub>m</sub> ≤ a<sub>n</sub>
 - A sequence (a<sub>n</sub>) is **non-decreaseing** if whenever m > n , then a<sub>m</sub> ≥ a<sub>n</sub>
 - those 4 kind of sequence are  **monotone**

### What is the Monotone Convergence Theorem?

Here's a theorem that guarantees a sequence converges.

 - If the sequence (a<sub>n</sub>) is bounded and monotone, then lim<sub>n→∞</sub> a<sub>n</sub> exists.



### How Can the Monotone Convergence Theorem Help?

## How Big Can Sequence Be ?

### Is There a Sequence That Includes Every Integer?

Yes !

 - 0,-1,1,-2,2,-3,3, ...
 - c<sub>n</sub>= 
    - -(n+1)/2 , if n is odd
    - n/2 , if n is even
    - starting with index 0 

### Is There a Sequence That Includes Every Real Number between 0 and 1 ?

No!

---

# Week2 : Series 

What is a series ?  A series is basically what you get when you add up the numbers in a sequence in order. 

## What is a Series ?  What is a Geometric Series ?

### What does ∑a<sub>k</sub> = L Mean ?

If lim<sub>n→∞</sub> s<sub>n</sub> = lim<sub>n→∞</sub> ∑<sub>k=</sub>ⁿ₁ a<sub>k</sub> exists and equals L , then say 

∑<sub>k=</sub>ⁿ₁ a<sub>k</sub> converges.

Otherwise, say ∑<sub>k=</sub>ⁿ₁ a<sub>k</sub> diverges.

### Why does  ∑<sub>k=</sub><sup>∞</sup>₀ (1/2)ᵏ = 2 ?

### What is a Geometric Series?

 - Geometric Series :  ∑<sub>k=</sub><sup>∞</sup>₀ rᵏ
 - let s<sub>n</sub> = ∑<sub>k=</sub><sup>n</sup>₀ rᵏ 
 - (1-r)s<sub>n</sub> = 1·(r⁰+r¹+...+rⁿ) - r·(r¹+r²+...+rⁿ+r<sup>n+1</sup>) = 1-r<sup>n+1</sup> 
 - so if r≠ 1
    - s<sub>n</sub> = (1-r)s<sub>n</sub> / (1-r) = (1-r<sup>n+1</sup> ) / (1-r)
 - so lim<sub>n→∞</sub> s<sub>n</sub> = lim<sub>n→∞</sub> (1-r<sup>n+1</sup> ) / (1-r) 
 - if r>1 or r<-1 ,  lim<sub>n→∞</sub> r<sup>n+1</sup> is infinite
    - if -1`<`r`<`1 ,  lim<sub>n→∞</sub> r<sup>n+1</sup> = 0
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/calculus2_series_geometric.png)

### What is the value of ∑<sub>k=</sub><sup>∞</sup><sub>m</sub> rᵏ ?

 - C·∑<sub>k=</sub><sup>∞</sup>₀ rᵏ  = ∑<sub>k=</sub><sup>∞</sup>₀ C·rᵏ  
 - rᵐ·∑<sub>k=</sub><sup>∞</sup>₀ rᵏ = rᵐ/(1-r)    (|r|<1)
    - = ∑<sub>k=</sub><sup>∞</sup>₀ r<sup>m+k</sup>





  








 



















