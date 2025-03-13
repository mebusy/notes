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
        - x & (-x) : 把 x 最右侧的 bit 1 以外的 位全部置0  (不考虑0的情况,结果一定是2的幂)
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



