[](...menustart)

- [random number](#54424d73e284242c90ae6c2c711487cf)
    - [Linear Congruential Generator](#3d6ac243e2eed84b3e761431b17bb56b)
        - [Choice of modulus](#ac4e828dbe54fb1d2feb694108ce5480)
        - [Choice of multiplier](#bdc47eab24c15e7a55f50a5e665743de)
        - [An implementation :  No guaranteed of correctness](#29c8b42cc2ff4fc09c6a75a4dfbc1885)
    - [Python random implementation](#31d89b288043a80670b7a9af27dba6b6)
    - [Distribution](#f0bac093bb884df2891d32385d053788)
        - [Python normalvariate implementation](#ee34ac09342e568469b18ca9916547d5)

[](...menuend)


<h2 id="54424d73e284242c90ae6c2c711487cf"></h2>

# random number

There's actually no way for software to produce a truly random number.

Pseudo random numbers:  a series of numbers in a particular range that seems unpredicatable but is actually produced by a straightforward mathematical process.


<h2 id="3d6ac243e2eed84b3e761431b17bb56b"></h2>

## Linear Congruential Generator 

- Linear Congruential Generator has 4 inputs:
    1. modulus  m  ,  `0<m`
    2. multiplier a  ,  `0<=a<m`
    3. increment  c  ,  `0<=c<m`
    4. seed X ,  starting value , `0<=X<m`

- linear congruential sequence
    - X<sub>n+1</sub> = ( a * X<sub>n</sub> + c ) mod m , n>=0
    - for example, the sequence obtained when m = 10 and X₀ = a = c = 7 is
        - 7,6,9,0,7,6,9,0...
    - As this example shows, the sequence is not always "random" for all choices of m,a,c,and X. 
- Above example illustrates the fact that the congruential sequences always get into a loop. 
    - This property is common to all sequences having the general form X<sub>n+1</sub> = f( X<sub>n</sub> ) .
    - The repeating cycle is called the *period*.   A useful sequence will of course have a relatively long period. 

- if we select good values for m , a ,c ,  then the period will be m.   


<h2 id="ac4e828dbe54fb1d2feb694108ce5480"></h2>

### Choice of modulus

- We want m to be rather large, since the period can not have more than m elements.
    - Even if we intend to generate only randOm zeros and ones, we should not take m = 2, for then the sequence would at best have the form..., 0,1,0,1,0,1,...
- Another factor that inffuences our choice of m is speed of generation: 
    - We want to pick a value so that the computation of (aX<sub>n</sub> + c ) mod m is fast.
    - like 2³².
    - Another alternative is to let m be the largest prime number less than *w* .

<h2 id="bdc47eab24c15e7a55f50a5e665743de"></h2>

### Choice of multiplier

- **Theorem A**. The linear congruential sequence defined by m, a, c, and X₀ has period length m if and only if  // 序列有周期长度m当且仅当
    1. c is relatively prime to m;  // c 与 m 互质
    2. b = a-1, is a multiple of p , for every prime p dividing m;  // 对于整除m的每个素数p，b=a-1是p的倍数;
    3. b is a multiple of 4, if m is a multiple of 4.   // 如果m是4的倍数，则b也是4的倍数
- if m is the word size zᵉ , the multiplier 
    - a = zᵏ + 1,  **2 ≤ k** ≤ e
    - satisfies these conditions. 
    - Note: **z = 2 for a binary computer**, and z = 10 for a demical compute

- We may take c=1,
    - X<sub>n+1</sub> = ( ( zᵏ + 1 )  X<sub>n</sub> + 1 ) mod zᵉ
    - then we can avoid multiplication ; merely shifting and adding will suffice.
        - e.g, for z=2, `X = ((X<<k) + X + 1) & ( zᵉ - 1 )`

<h2 id="29c8b42cc2ff4fc09c6a75a4dfbc1885"></h2>

### An implementation :  No guaranteed of correctness 

```python
# python3
class Random(object):
    def __init__(self, e ,  x=None):
        if x is None:
            import time
            self.seed = long(time.time())
        else:
            self.seed = long(x)
        self._seed = self.seed

        self.e = e
        self.k = (self.e + 1) / 2
        self.m = 2** self.e
        # self.a = (2** self.k) + 1

    def random_LCG(self):
        '''
        generate ranom in 0~1

        X(k) = [a * X(k-1) + c] mod m
        '''
        # m,a,c is referenced in GCC compiler
        # self._seed = (self.a * self._seed + 1) & ( self.m-1 )
        self._seed = ( self._seed + (self._seed<<self.k) + 1) & ( self.m-1 )
        return self._seed


for e in xrange( 8 , 20 ,1  ) :
    r = Random( e  )
    d = { r.random_LCG() for _ in xrange( 2**e  )  }
    print "e:{} , loop: {}".format( e , len(d) )
    assert len(d) == 2**e

```

```python
# a simple implementation
class LCG():
    def __init__( self, seed, mul, inc , mod ):
        self.seed = seed
        self.mul = mul
        self.inc = inc
        self.mod = mod

    def next(self):
        self.seed = (( self.mul * self.seed + self.inc ) % self.mod)
        return self.seed


if __name__ == "__main__":
    lcg = LCG( 7,7,7, 10  )
    print( [ lcg.next() for i in range(16) ] )


    lcg = LCG( 7, 5 ,1, 16  )
    print( [ lcg.next() for i in range(20) ] )
```

<h2 id="31d89b288043a80670b7a9af27dba6b6"></h2>

## Python random implementation

```python
def random(self):
    """Get the next random number in the range [0.0, 1.0)."""

    # Wichman-Hill random number generator.
    #
    # Wichmann, B. A. & Hill, I. D. (1982)
    # Algorithm AS 183:
    # An efficient and portable pseudo-random number generator
    # Applied Statistics 31 (1982) 188-190
    #
    # see also:
    #        Correction to Algorithm AS 183
    #        Applied Statistics 33 (1984) 123
    #
    #        McLeod, A. I. (1985)
    #        A remark on Algorithm AS 183
    #        Applied Statistics 34 (1985),198-200

    # This part is thread-unsafe:
    # BEGIN CRITICAL SECTION
    x, y, z = self._seed
    x = (171 * x) % 30269
    y = (172 * y) % 30307
    z = (170 * z) % 30323
    self._seed = x, y, z
    # END CRITICAL SECTION

    # Note:  on a platform using IEEE-754 double arithmetic, this can
    # never return 0.0 (asserted by Tim; proof too long for a comment).
    return (x/30269.0 + y/30307.0 + z/30323.0) % 1.0
```

- Wichman-Hill算法通过线性合并不同短周期随机数发生器的输出来产生长周期的随机数序列。
    - 如果把周期N1和N2的波形加起来那么得到的波形周期为 N = lcm（N1,N2） 
    - 这样，通过结合几个随机数发生器的输出，可以产生一个更长的序列。


<h2 id="f0bac093bb884df2891d32385d053788"></h2>

## Distribution

- It's much more useful to have a sequence of numbers with the uniform distribution on the interval 0 to 1. 
- This is useful because with a sequence of numbers with a uniform distribution on [0,1], we can generate sequences of random numbers according to other distributions use something known as **inverse transform sampling**. 
- Let's say we want to generate a sequence of random numbers with the normal distribution with mean=162cm, and standard deviation=5cm , to represent the height of an American woman.
    - Probability Density Function --> Cumulative Distribution Function. 
    - we uniformly randomly select a point on the y-axis ( Cumulative Distribution Function graph ) , and then determine the point on the x-axis, it gives that function value. 


<h2 id="ee34ac09342e568469b18ca9916547d5"></h2>

### Python normalvariate implementation

```python
    from math import log as _log, exp as _exp, e as _e
    from math import sqrt as _sqrt

    # NV_MAGICCONST = 4 * _exp(-0.5) / _sqrt(2.0)

    def normalvariate(self, mu, sigma):
        """Normal distribution.
        mu is the mean, and sigma is the standard deviation.
        """
        # mu = mean, sigma = standard deviation

        # Uses Kinderman and Monahan method. Reference: Kinderman,
        # A.J. and Monahan, J.F., "Computer generation of random
        # variables using the ratio of uniform deviates", ACM Trans
        # Math Software, 3, (1977), pp257-260.

        random = self.random
        while 1:
            u1 = random()
            u2 = 1.0 - random()
            z = NV_MAGICCONST*(u1-0.5)/u2
            zz = z*z/4.0
            if zz <= -_log(u2):  # math.e
                break
        return mu + z*sigma
```

Book "Probability Theory and Examples"


