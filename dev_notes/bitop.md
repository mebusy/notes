[](...menustart)

- [位运算](#c04f8667013a3097bf12e98e424a915b)
    - [二进制](#6168fb08fe64663a502a132c5589b73d)
        - [flip bits](#bf94eee92531fcf0a63c55eddb6a558c)
    - [XOR](#97675eb3f268048604dc5155511a2a4d)
        - [XOR application](#cc352fea6e400fa736030527056c3fc2)

[](...menuend)


<h2 id="c04f8667013a3097bf12e98e424a915b"></h2>

# 位运算


<h2 id="6168fb08fe64663a502a132c5589b73d"></h2>

## 二进制

- 对于一个整数 x
    - x-1,x+1 都是 **有限制的，局部的，各位求反** 操作
    - x-1
        - 受影响的pattern: 最右侧 10000的形式
        - 减去1 后的结果:  pattern 变成 01111 的形式
    - x+1
        - 受影响的pattern: 最右侧 01111 的形式
        - 加1 后的结果:  pattern 变成 10000 的形式
    - 所以
        - x & (x-1) : x 最右侧的bit 1 置0. (判断是否是2的幂, 以及统计bit 1的个数)
        - x & (x+1) : x 最右侧的bit 1 全部置0 (包含最低位)
        - x | (x-1) : x 最右侧的bit 0 全部置1 (包含最低位)
        - x | (x+1) : x 最后侧的bit 0 置1
        - 上述运算，其实就是把 受影响的pattern 全部置0 或 置1
    - 因为 ~x 是全部求反, x-1/x+1 是局部求反,   所以
        - ~x & (x+1) : 把 x 最右侧的 0 置为1， 其他位全部置0
        - ~x & (x-1) : 把 x 最右侧的 0 全置为1 (包含最低位), 其他位(剩余高位)全部置位0
    - 因为  -x=~x+1 , 所以
        - x & (-x) : 保留最低位的1(最右), 其它全部置0  (不考虑0的情况,结果一定是2的幂)
        - that is, **Least-Significant 1**
- 判断两个整数是否异号
    ```c
    bool f = ((x ^ y) < 0); // true iff x and y have opposite signs
    ```
- 判断一个数是否为2的n次幂：
    ```c
    (v & (v - 1)) == 0;
    ```
- 计算一个数含有多少个比特1:
    ```c
    unsigned int v; // count the number of bits set in v
    unsigned int c; // c accumulates the total bits set in v
    for (c = 0; v; c++)
    {
      v &= v - 1; // clear the least significant bit set
    }
    ```
    - most modern CPUs have a special instruction for this, called the population count or popcount instruction. In C, you can use the GCC built-in function `__builtin_popcount` to access this instruction.
    - be useful to calcuate x from log2(pow(2,x))


<h2 id="bf94eee92531fcf0a63c55eddb6a558c"></h2>

### flip bits

```go
func Flipbyte(b uint8) uint8 {
    b = (b & 0xF0) >> 4 | (b & 0x0F) << 4
    b = (b & 0xCC) >> 2 | (b & 0x33) << 2
    b = (b & 0xAA) >> 1 | (b & 0x55) << 1
    return b
}
```

<h2 id="97675eb3f268048604dc5155511a2a4d"></h2>

## XOR

AND is analogous to intersection, OR is analogous to union,

XOR is analogous to set difference.

- Identity element : x ^ 0 = x
    - 不变
- Self-inverse: x ^ x = 0
    - when we consider it in the context of assembly language. In fact XOR’ing a register with itself is the fastest way for the compiler to zero the register.
    ```c
    xor eax, eax  ; 清零 eax
    ```
- x ^ (-1) = ~x
    - 等效 各位求反
    - 所以:  x ^ (-1) = ~x = -(x+1)
- 翻转(flip) x 第n位
    ```c
    x ^ (1<<n)`
    ```
- xor is **addition mod 2**
    - so xor is commutative and associative.

<h2 id="cc352fea6e400fa736030527056c3fc2"></h2>

### XOR application

1. Toggling 
    - toggle between two values x and y
    ```cpp
    for (int n=x; true; n ^= (x ^ y)) 
        printf("%d ", n);
    ```
    - Toggling in this way is very similar to the concept of a flip-flop in electronics: a ‘circuit that has two stable states and can be used to store state information’
    - it’s probably not that useful in practice. 
2. Save yourself a register
    ```cpp
    void s(int& a, int& b) {
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
    }
    ```
    -  the below equivalent function is even more esoteric:
    ```cpp
    void s(int& a, int& b) {
        a ^= b ^= a ^= b;
    }
    ```
    - 并不推荐，因为指令无法并行，实际上比 使用临时变量的naive版本慢
- cipher attack
    ```c
    m     -> enc( ^ k ) ->  m ^ k 
                             ^ p
    m ^ p <- dec( ^ k ) <- (m ^ k ^ p)
    ```

## int64 n, 自最高位1开始，全部填充1

```c
n |= n >> 1;  // fill with all 1s from the MSB  
n |= n >> 2;
n |= n >> 4;
n |= n >> 8;
n |= n >> 16;
n |= n >> 32;
```

怎么只保留 most significant bit 1 ?

## uint64 n,   保留最高位1，其余位全部置0

就是计算 pow(2, floor(log₂(n) ) )

```c
n |= n >> 1; // fill with all 1s from the MSB  
n |= n >> 2;
n |= n >> 4;
n |= n >> 8;
n |= n >> 16;
n |= n >> 32;
// add me !
n &= ~(n >> 1)
```

## uint64 n,  计算 pow(2, ceil(log₂(n) ) ) , e.g. 54 -> 64

```c
--n;  // if case v is power of 2
n |= n >> 1;  // fill with all 1s from the MSB
n |= n >> 2;
n |= n >> 4;
n |= n >> 8;
n |= n >> 16;
n |= n >> 32;
++n;
```


## 计算 floor( log₂(n) )

- 因为是求一个整数结果, 本质是快速找到 最高位 1 的索引.
    - 因为 n 的值域是 n > 0, 所以可以通过循环右移动的方式，找到最高位1的索引
    - O(logn) 并不是最高效的方法
- de Bruijn 序列
    - 通过查表的方式，可以在O(1)的时间内找到最高位1的索引

Nowadays there's actually a hardware instruction for this, called `clz` (count leading zeros), which is available on most modern CPUs. In C, you can use the GCC built-in function `__builtin_clzll` to access this instruction.

```c
int log2(uint64_t n) {
    return 63 - __builtin_clzll(n);
}
```

So you don't actually have to implement this trick.


方法 | 复杂度 | 额外存储 | 适用范围
--- | --- | --- | ---
循环位移 `while (n >>= 1) ++c;` | O(logn) | No | 小整数
`__builtin_clzll(n)`（GCC 内置）| O(1) | No | 需要GCC
de Bruijn 查表 | O(1) | No |  


## Q&A

- 为什么计算机使用二进制？
    - 硬件实现
        - 在电子电路中，二进制可以用**高电压（1）和低电压（0）**来表示，非常容易实现。
        - 继电器、真空管、晶体管等早期电子元件只能稳定地表现“通”或“断”两种状态，而二进制正好对应这两种状态。
    - 数学上的优越性
        -布尔代数（由乔治·布尔提出）提供了用逻辑门（AND、OR、NOT）处理二进制的方式，使计算机的逻辑运算变得简单高效。
        - 二进制运算比十进制更容易实现加法和乘法，不需要复杂的进位逻辑。
- 为什么二进制使用补码
    - 简化电路、减少计算复杂度，并且使加法、减法能够使用相同的硬件单元


- de Bruijn 序列 B(k)
    - 是一种特殊的最短循环序列
    - 它包含所有长度为 k 的二进制子串（k==3, 000,001,010,...），且每个这样的子串在序列中恰好只出现一次.
    - 其长度为 pow(2,k)
    - 该序列是**循环**的，即可以从序列的任意位置出发，依次读取 𝑘位，都能得到一个唯一的 k 位二进制子串
- de Bruijn 序列 B(2,k) 的构造
    - 例子 k == 3
    - 所有可能的 3 位二进制串为：
        - 000, 001, 010, 011, 100, 101, 110, 111
    - 可以构造的 de Bruijn 序列之一为：
        - 00010111

