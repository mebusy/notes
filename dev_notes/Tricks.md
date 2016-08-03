...menustart

 - [Trick](#59c9428d4e21d63aefeb230c919dcfe3)
	 - [Match](#6da89265a9a8b0b28eb4946bb2ec0c6d)
		 - [e](#e1671797c52e15f763380b45e841ec32)
		 - [弧度θ 对应的单位扇形面积](#c7112c6a637487ace192a1747cc4e5a9)
		 - [geometric series](#b287a415393520b5c5e9a45cf7f0ba02)
	 - [Algorithm](#4afa80e77a07f7488ce4d1bdd8c4977a)
		 - [二分法](#0608141511400ff7717263f89537faaf)
			 - [求数组中的逆序数](#bb0a8ee4ec6c3520a9cf5fd4604aac07)
			 - [closest pairt 距离最近两个点](#a95c72911ec10a8e9f3522ce7acd395a)

...menuend



<h2 id="59c9428d4e21d63aefeb230c919dcfe3"></h2>
# Trick

<h2 id="6da89265a9a8b0b28eb4946bb2ec0c6d"></h2>
## Match

<h2 id="e1671797c52e15f763380b45e841ec32"></h2>
### e

```octave
	(1 + 1/n)ⁿ → e
```

相似的:

```octave
	(1 + 1/n²)ⁿ → 1
```

```octave
	eˣ ≈ 1 + x
```

<h2 id="c7112c6a637487ace192a1747cc4e5a9"></h2>
### 弧度θ 对应的单位扇形面积

```octave
S = πr²/(2π) * θ = θ/2
```

<h2 id="b287a415393520b5c5e9a45cf7f0ba02"></h2>
### geometric series

```octave
1 + x + x² + x³ + ...
```

```octave
for |x| < 1 , 1 + x + x² + ... = 1/(1-x)
for  x  ≠ 1 , 1 + x + x² + ... = (1- xᵏ⁺¹)/(1-x)
```


<h2 id="4afa80e77a07f7488ce4d1bdd8c4977a"></h2>
## Algorithm

<h2 id="0608141511400ff7717263f89537faaf"></h2>
### 二分法

<h2 id="bb0a8ee4ec6c3520a9cf5fd4604aac07"></h2>
#### 求数组中的逆序数

 1. 把输入array 拆成两部分
 2. 对两个子数组 计算逆序数 X,Y  (*)
 3. 计算 子数组 之间统计关系 Z , 返回 X+Y+Z

 - 第3步 牵涉到两个子数组的遍历，复杂度上很难做到线性，这里我们需要参考merge sort的做法，最后处理两个有序数组会简单的多。
 - 所以 第2部需要同时对 子数组排序，并返回  (*) 


<h2 id="a95c72911ec10a8e9f3522ce7acd395a"></h2>
#### closest pairt 距离最近两个点

有一组点[ (x₁,y₁),(x₂,y₂),...,(x<sub>n</sub>,y<sub>n</sub>) ] ,求距离最近的两个点。

`1-D case:`









