# LCG 方法与参数选择总结

## @mebusy

怎么设计 lcg 方法， 是的 随机数的的 循环周期正好是11(0~10 11个数字出现，且仅出现一次)

## Copilot

可以。你这个本质上是设计一个**模 11 下的全排列生成公式**，让序列的周期刚好是 11。

最简单的是这个：

\[
x_k = (a * k + b) mod 11
\]

其中：

- `k = 0,1,2,...,10`
- `a` 和 `11` 互质
- `b` 是任意 `0~10` 的整数

这样生成出来的 11 个值会：

- 全都落在 `0~10`
- 11 个数字**各出现一次**
- 到第 11 步开始重复
- 周期正好是 11

---

# 为什么这样能行

因为 11 是质数。  
当 `a != 0 (mod 11)` 时，`a` 一定和 11 互质。

所以：

\[
(a * k + b) mod 11
\]

会把 `0~10` 做一次一一映射，也就是一个排列。

---

# gcd 在这里的作用

实际是要用 `gcd(a, n) == 1` 来判断这个步长 `a` 能不能用。

对于一般长度 `n`：

```js
function gcd(a, b) {
  while (b !== 0) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}
```

判断条件：

```js
gcd(a, n) === 1
```

如果成立，则：

```js
x_k = (a * k + b) % n
```

会遍历 `0..n-1` 各一次。

---

# 对 n=11 的特殊情况

因为 11 是质数，所以可选的 `a` 就是：

```text
1,2,3,4,5,6,7,8,9,10
```

都可以。

`b` 则可以是：

```text
0~10
```

任意一个。

---

# 示例

比如：

- `a = 3`
- `b = 7`

则：

\[
x_k = (3k + 7) mod 11
\]

依次得到：

- k=0 -> 7
- k=1 -> 10
- k=2 -> 2
- k=3 -> 5
- k=4 -> 8
- k=5 -> 0
- k=6 -> 3
- k=7 -> 6
- k=8 -> 9
- k=9 -> 1
- k=10 -> 4

正好是：

```text
7,10,2,5,8,0,3,6,9,1,4
```

11 个数全部出现且只出现一次。

---

# JS 实现

## 1. gcd 方法

```js
function gcd(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}
```

---

## 2. 生成一个周期正好为 11 的序列

```js
function createCycle11() {
  const n = 11;

  // a 与 11 互质；对于 11 来说，1~10 都行
  let a;
  do {
    a = Math.floor(Math.random() * 10) + 1; // 1~10
  } while (gcd(a, n) !== 1);

  const b = Math.floor(Math.random() * n); // 0~10

  let index = 0;

  return function next() {
    const value = (a * index + b) % n;
    index = (index + 1) % n;
    return value;
  };
}
```

使用：

```js
const nextRand = createCycle11();

for (let i = 0; i < 11; i++) {
  console.log(nextRand());
}
```

---

# 如果你想“每轮重新随机顺序”

那就每轮重新生成新的 `a` 和 `b`。

```js
class QuestCycle {
  constructor(n = 11) {
    this.n = n;
    this.reset();
  }

  gcd(a, b) {
    while (b !== 0) {
      const t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  reset() {
    do {
      this.a = Math.floor(Math.random() * (this.n - 1)) + 1;
    } while (this.gcd(this.a, this.n) !== 1);

    this.b = Math.floor(Math.random() * this.n);
    this.index = 0;
  }

  next() {
    if (this.index >= this.n) {
      this.reset();
    }

    const value = (this.a * this.index + this.b) % this.n;
    this.index++;
    return value;
  }
}
```

---

# 但要注意一个问题

这个方案虽然满足：

- 11 个数不重复
- 周期正好 11
- 只需要很少状态：`a,b,index`

但是它产生的排列种类**不如真正洗牌多**。

因为：

- 长度 11 的全排列总数是 `11!`
- 而这种线性公式只会产生有限种排列（`a,b` 组合大约 `11 * 10 = 110` 种）

所以它是：

- **轻量**
- **周期正确**
- **无重复**
- **但随机性不如完整洗牌**

---

# 如果你的目标只是“尽量少记录数据”

这是个很好的方案，只记录：

- `a`
- `b`
- `index`

共 3 个整数。

---

# 总结

如果你要长度正好 11、每个数 0~10 恰好出现一次，可以用：

\[
x_k = (a * k + b) mod 11
\]

并保证：

\[
gcd(a, 11) = 1
\]

对于 11 来说：

- `a ∈ [1,10]`
- `b ∈ [0,10]`

都很好选。

---

如果你愿意，我可以进一步给你：

1. **证明为什么 `gcd(a, n)=1` 就一定遍历完整周期**
2. **把这个改造成 questIdList 的直接抽取器**
3. **给你一个“比线性同余更随机，但仍只记录很少状态”的方案**

## @mebusy

能不能设计一个通用的算法, 可以指定 n ,  (1<= n <= 2^16)

## Copilot

可以。

你真正要的是：

- 指定 `n`，`1 <= n <= 2^16`
- 生成一个长度恰好为 `n` 的循环
- 每轮中 `0..n-1` **各出现一次且仅一次**
- 状态尽量少

这时可以用这个公式：

\[
x_k = (a * k + b) mod n
\]

只要满足：

\[
gcd(a, n) = 1
\]

就能保证周期正好是 `n`。

---

# 1. 通用 gcd 方法

这是标准欧几里得算法，适用于你这个范围。

```js
function gcd(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);

  while (b !== 0) {
    const t = a % b;
    a = b;
    b = t;
  }

  return a;
}
```

---

# 2. 如何为任意 n 选一个可用的 a

你只要随机找一个 `a`，满足：

- `1 <= a < n`
- `gcd(a, n) === 1`

即可。

```js
function randomCoprime(n) {
  if (n <= 1) return 0;

  while (true) {
    const a = Math.floor(Math.random() * (n - 1)) + 1;
    if (gcd(a, n) === 1) {
      return a;
    }
  }
}
```

---

# 3. 构造“周期正好为 n”的生成器

```js
class FullCycleGenerator {
  constructor(n) {
    if (!Number.isInteger(n) || n < 1 || n > 2 ** 16) {
      throw new Error("n must be an integer in [1, 2^16]");
    }

    this.n = n;
    this.reset();
  }

  gcd(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
    while (b !== 0) {
      const t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  randomCoprime(n) {
    if (n === 1) return 0;

    while (true) {
      const a = Math.floor(Math.random() * (n - 1)) + 1;
      if (this.gcd(a, n) === 1) {
        return a;
      }
    }
  }

  reset() {
    if (this.n === 1) {
      this.a = 0;
      this.b = 0;
      this.index = 0;
      return;
    }

    this.a = this.randomCoprime(this.n);
    this.b = Math.floor(Math.random() * this.n);
    this.index = 0;
  }

  next() {
    if (this.index >= this.n) {
      this.reset();
    }

    const value = (this.a * this.index + this.b) % this.n;
    this.index++;
    return value;
  }
}
```

使用：

```js
const gen = new FullCycleGenerator(10);

for (let i = 0; i < 25; i++) {
  console.log(gen.next());
}
```

---

# 4. 为什么 `gcd(a, n) = 1` 就能保证周期是 n

我们看：

\[
x_k = (a * k + b) mod n
\]

假设存在两个不同位置 `i != j`，却得到同一个值：

\[
a i + b \equiv a j + b \pmod n
\]

消掉 `b`：

\[
a(i-j) \equiv 0 \pmod n
\]

如果 `gcd(a, n) = 1`，那么 `a` 在模 `n` 下可逆，所以可推出：

\[
i-j \equiv 0 \pmod n
\]

但当 `i,j` 都在 `0..n-1` 内时，这只能说明 `i=j`。  
矛盾。

所以 `0..n-1` 这 `n` 个位置映射出的 `x_k` 全都不同。又因为值域也是 `0..n-1`，所以恰好全部出现一次。

---

# 5. 如果 questIdList 不是 0..n-1

直接映射即可。

```js
class QuestPicker {
  constructor(questIdList) {
    if (!Array.isArray(questIdList) || questIdList.length === 0) {
      throw new Error("questIdList must be a non-empty array");
    }

    this.questIdList = questIdList;
    this.gen = new FullCycleGenerator(questIdList.length);
  }

  nextQuest() {
    const idx = this.gen.next();
    return this.questIdList[idx];
  }
}
```

使用：

```js
const picker = new QuestPicker([101, 205, 309, 888]);

for (let i = 0; i < 12; i++) {
  console.log(picker.nextQuest());
}
```

---

# 6. 这个方案记录的数据量

只需要记录：

- `n`
- `a`
- `b`
- `index`

如果 `questIdList` 本身是已有的常量数据，那额外状态就这 3 个整数：

- `a`
- `b`
- `index`

非常少。

---

# 7. 但它有一个局限

这个方法生成的是**仿射排列**：

\[
(a * k + b) mod n
\]

所以它不是所有排列都能覆盖。

例如当 `n=10` 时，全部排列有：

\[
10! = 3628800
\]

但这个方法只有“与 `n` 互质的 `a` 数量 × `n` 个 `b`”这么多种。  
也就是：

\[
\varphi(n) * n
\]

远少于 `n!`。

所以它满足：

- 周期正好为 `n`
- 一轮不重复
- 额外状态极少

但不满足“全排列意义上的强随机”。

---

# 8. 如果你想更稳一点，可加一个随机起点轮次

如果你担心分布太规律，可以每轮 `reset()` 时重新随机：

- `a`
- `b`

这样每轮顺序都变。

---

# 9. 特殊边界

## n = 1
唯一值只能是 `0`。

## n = 2
可选 `a=1`，`b=0/1`，序列就是：

- `0,1`
- 或 `1,0`

---

# 10. 最终建议

如果你要的是：

- **指定任意 n**
- **辅助状态极少**
- **一轮内恰好遍历完所有元素**

那最简洁的方法就是：

## 核心公式
```js
x = (a * index + b) % n
```

## 条件
```js
gcd(a, n) === 1
```

## 需要的 gcd
```js
function gcd(a, b) {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}
```

---

如果你愿意，我下一条可以直接给你一份：

1. **可直接复制的 TypeScript 版本**
2. **Java 版本**
3. **支持存档/恢复状态的版本**  
比如把 `a,b,index` 序列化后，下次继续抽。

## @mebusy

所以 b 的取值其实是任意的

## Copilot

对。**在这个方案里，`b` 可以是任意 `0 ~ n-1` 的值。**

前提是公式是：

\[
x_k = (a * k + b) mod n
\]

且满足：

\[
gcd(a, n) = 1
\]

---

## 为什么 `b` 任意都行

`b` 的作用本质上只是：

- 给整个序列做一个**整体平移**
- 不改变“是否遍历完整个 `0..n-1`”这个性质

因为如果：

\[
a * k mod n
\]

本身已经能把 `0..n-1` 全走一遍，  
那再加上一个固定的 `b`，只是把每个结果都偏移一下：

\[
(a * k + b) mod n
\]

仍然还是一个排列。

---

## 直观理解

假设 `n = 5`，`a = 2`，因为 `gcd(2, 5) = 1`。

### 当 `b = 0`
\[
(2k) mod 5
\]

得到：

```text
0, 2, 4, 1, 3
```

### 当 `b = 1`
\[
(2k + 1) mod 5
\]

得到：

```text
1, 3, 0, 2, 4
```

### 当 `b = 3`
\[
(2k + 3) mod 5
\]

得到：

```text
3, 0, 2, 4, 1
```

可以看到只是整体挪了一下，仍然每个数只出现一次。

---

## 真正决定“能不能完整遍历”的是 `a`

不是 `b`，而是：

```text
gcd(a, n) == 1
```

### 如果 `a` 合法
那 `b` 任意都合法。

### 如果 `a` 不合法
那 `b` 再怎么选也没用。

---

## 反例

比如 `n = 10`，`a = 2`，因为：

\[
gcd(2,10)=2 \neq 1
\]

### `b = 0`
```text
0, 2, 4, 6, 8, 0, 2, 4...
```

### `b = 1`
```text
1, 3, 5, 7, 9, 1, 3, 5...
```

你看，`b` 换了只是把“偶数圈”变成“奇数圈”，  
**周期还是不可能到 10**。

---

## 结论

是的，**`b` 的取值可以任意选**，通常取：

```js
0 <= b < n
```

即可。

真正需要约束的是：

```js
1 <= a < n && gcd(a, n) === 1
```

---

## 参数职责总结

- `a`：决定是否能形成完整周期
- `b`：决定从哪个偏移开始，相当于整体平移
- `index`：当前取到第几个

---

如果你愿意，我可以下一条继续帮你总结成一个非常简洁的判定规则，比如：

- **什么时候只看 `a`**
- **什么时候 `b` 可以忽略**
- **如何快速随机生成合法的 `a` 和 `b`**
