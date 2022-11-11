[](...menustart)

- [Octave Tutorial](#7b7506511ca80c5b54b8e2f1784aab67)
    - [一般命令](#45cd59165ed98b8a43499f3529f43da5)
        - [更改提示符 PS1](#f4e9152fa12ce5bd311f26a2e82e0dd8)
        - [帮助命令 help](#419a19bbfcdf3c127420fa85cb5b3036)
        - [幂](#d701e1c8f6eb5c1ccba886670e6445d0)
        - [逻辑运算](#518c00ba7ed99f81aff084a47bc1bc02)
        - [打印 disp](#3732e6e4befd27d65793a3ee28e9ce20)
        - [format](#1ddcb92ade31c8fbd370001f9b29a7d9)
        - [矩阵](#f739e5c9038960c20907a5fac564d123)
            - [ones](#50a1e8d0ea071aca23f99488fd969483)
            - [zeros](#077effb59e9d5fcfabca678cf6da604c)
            - [rand 随机矩阵](#d8119f74b55f0e6f0a9119822ef2b001)
            - [正态随机矩阵 randn](#bfc03e2c9d8d196bf27575241bda2831)
            - [单位矩阵 eye](#8d2c44eb72ffbdfecd5a6b7a0d42630f)
        - [直方图 hist](#7336f8c273a473841532e091046cf59c)
        - [size 和 length](#68f9be08cd9ecf22559e6344c3e26112)
        - [linux 命令: cd / ls / pwd](#bdefbd70450fa0311d2375e510b2c921)
        - [who/whos 查看当前工作环境中存储的所有的变量](#0de0197f8e28460fd27562a1bf797b8d)
        - [清除命令 clear \[var\]](#321c0450a7c9ea0dde8fce6ffd6dad42)
        - [保存命令 save](#b7041e9f097d9daaa93af683073f1d7d)
    - [矩阵数据移动](#8354745ee8accd9d217e9405250ef364)
    - [矩阵运算](#ba5e7829f63ffdcc50f799fa90bbe124)
        - [加法 A + B , 各元素相加](#9ee76a86a85ebc392cc58adcd82755ac)
        - [数加 A+1  , 所有元素+1](#0f8c8570065113d98309db042de5dc45)
        - [乘法 A*B ,  矩阵乘法](#2f5235a090db9cbf0b62bc8ec01379a6)
        - [矩阵点乘 A.*B  , 各元素相乘:](#85544a6ab193a65265eaaeddd9ac1569)
        - [叉积 cross, 至少一个维度大于3](#54d294e059bbc06f4ef1d98a54ab763a)
            - [矩阵数乘法 A *2  , 所有元素 *2](#8cb0042601b89d343ede0618848c0443)
            - [A.^2          , 所有元素平方](#15c3b7e97c9b84449d7318aceba06a80)
            - [1 ./ A   , 所有元素的倒数](#5da2497e58940ef2f391789c62b74213)
            - [对数log(A)，指数exp(A)](#a7d68adc4d02bff1cc1a0f7764718b5a)
            - [abs 绝对值](#0d3c6f75b597405e7a5bd3dca1fe8b9a)
            - [-v  % -1*v](#e9ffbcb910a3a6ac2979fcfedcbd3d01)
            - [max(A)  最大值](#3aba41f7e265ee9a755472697dda5eb0)
            - [max(A,B) , 返回一个矩阵，元素是 A,B各元素的最大值](#23deac19e3ffb9356677692a6e457f89)
            - [Filter A <= 3  , 各元素比较的结果](#b459cf35a08fbbafa132c845e873a684)
            - [find( filter ) : find( A<=3), 注意接受 find返回值的变量个数](#a4155f1a9d0b04da44f33812d717c0d5)
            - [求和 sum](#ca8891f30cdfd2185e065e8156c3446d)
            - [求积 prod](#258cb2eb8e998fd10888ef8c9dd7628c)
            - [floor, ceil](#5eac4647e29237b13fd08b162de55898)
            - [Transpose 转置  A'](#3b06c53acea624df1786802a6ac1e81f)
            - [magic 好玩但没卵用](#e483f22bccac27c7aa4bb146a6a95b7b)
            - [invert 逆矩阵  pinv](#84becd6270e11d304352cfd8cce872b3)
        - [a=a(:)](#0aabb2e84a3f1c8c85b42b73abb1239d)
    - [cell array](#37a8bc45f9e398cdffe832b507cf789b)

[](...menuend)


<h2 id="7b7506511ca80c5b54b8e2f1784aab67"></h2>

# Octave Tutorial

<h2 id="45cd59165ed98b8a43499f3529f43da5"></h2>

## 一般命令
<h2 id="f4e9152fa12ce5bd311f26a2e82e0dd8"></h2>

##### 更改提示符 PS1

```
octave:11> PS1('>> ')  % 更改提示符
>>
```

<h2 id="419a19bbfcdf3c127420fa85cb5b3036"></h2>

##### 帮助命令 help
>> help hist

<h2 id="d701e1c8f6eb5c1ccba886670e6445d0"></h2>

##### 幂
```
>> 2^6  % 幂
ans = 64
```

<h2 id="518c00ba7ed99f81aff084a47bc1bc02"></h2>

##### 逻辑运算

```
>> 7 && 3 % AND
ans = 0

>> 7 || 0 % OR
ans =  1

>> xor(7,0)
ans =  1
```

<h2 id="3732e6e4befd27d65793a3ee28e9ce20"></h2>

##### 打印 disp
```
>> disp(a)    % 打印
 3.1416
>> disp( sprintf( '%0.2f' , a) )
3.14
```

<h2 id="1ddcb92ade31c8fbd370001f9b29a7d9"></h2>

##### format
```
>> format long   % 长小数
>> a
a =  3.14159265358979
>> format short  % default
>> a
a =  3.1416
```

<h2 id="f739e5c9038960c20907a5fac564d123"></h2>

##### 矩阵
```
>> a=[1 2 ; 3 4 ; 5 6]
a =

   1   2
   3   4
   5   6

>> v=[1 2 3]
v =

   1   2   3

>>  v = 1:0.1:2  % start:step:end,   1行11列矩阵 
v =

 Columns 1 through 9:

    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000    1.7000    1.8000

 Columns 10 and 11:

    1.9000    2.0000


>> v = 1:6   % start:end
v =

   1   2   3   4   5   6
```

<h2 id="50a1e8d0ea071aca23f99488fd969483"></h2>

###### ones
```
>> ones(2,3)
ans =

   1   1   1
   1   1   1

>> c = 2*ones(2,3)
c =

   2   2   2
   2   2   2
```

<h2 id="077effb59e9d5fcfabca678cf6da604c"></h2>

###### zeros
```
>> w = zeros(1,3)
w =

   0   0   0
```

<h2 id="d8119f74b55f0e6f0a9119822ef2b001"></h2>

###### rand 随机矩阵
```
>> rand(3,3)
ans =

   0.398462   0.832512   0.595303
   0.410825   0.726594   0.015361
   0.600570   0.555390   0.150527
```

<h2 id="bfc03e2c9d8d196bf27575241bda2831"></h2>

###### 正态随机矩阵 randn
```
>> randn(3,3)
ans =

   0.0226734  -0.3335212  -0.0013326
   0.0497447  -0.5800039  -0.2202317
  -0.3534828   0.1645582  -0.7277182
```



<h2 id="8d2c44eb72ffbdfecd5a6b7a0d42630f"></h2>

###### 单位矩阵 eye
```
>> eye(4)
ans =

Diagonal Matrix

   1   0   0   0
   0   1   0   0
   0   0   1   0
   0   0   0   1

```

<h2 id="7336f8c273a473841532e091046cf59c"></h2>

##### 直方图 hist
```
>> w = -6 + sqrt(10)* (randn(1,10000));
>> setenv("GNUTERM","qt")
>> hist(w)
>> hist(w,50) % 50个bar
```

画直方图报错处理:
```

    setenv("GNUTERM","qt")
```

如果不想每次都输入，把这条命令加入到:
```    
vim ~/.octaverc
```

<h2 id="68f9be08cd9ecf22559e6344c3e26112"></h2>

##### size 和 length

```
>> A = [1 2; 3 4; 5 6];
>> size(A)
ans =

   3   2

>> size(A,1)
ans =  3
>> length(A) # 返回最大维度
ans =  3
```

<h2 id="bdefbd70450fa0311d2375e510b2c921"></h2>

##### linux 命令: cd / ls / pwd
---

<h2 id="0de0197f8e28460fd27562a1bf797b8d"></h2>

##### who/whos 查看当前工作环境中存储的所有的变量
```
>> who
Variables in the current scope:

A    a    ans  c    v    w
```

<h2 id="321c0450a7c9ea0dde8fce6ffd6dad42"></h2>

##### 清除命令 clear [var]

不提供var， 表示全部清除

---

<h2 id="b7041e9f097d9daaa93af683073f1d7d"></h2>

##### 保存命令 save
```
>> v = priceY(1:10)
>> save save.data v [-ascii];  % -ascii 保存为文本方式
```


<h2 id="8354745ee8accd9d217e9405250ef364"></h2>

## 矩阵数据移动
```
>> A=[1 2;3 4;5 6];
>> A(3,2)     % 取矩阵中的某个元素
ans =  6
>> A(2,:)    % : 表示所有的数据, 这里指 第2行数据
ans =

   3   4

>> A([1 3], : )   % 取 第1，3行数据
ans =

   1   2
   5   6
   
>> A(:,2) = [10;11;12]   % 修改第2列的值
A =

    1   10
    3   11
    5   12   

>> A = [A,[100;101;102]]  % append
A =

     1    10   100
     3    11   101
     5    12   102

>> A=[1 2;3 4;5 6];     % 还是 append 的例子
>> B=[11 12;13 14;15 16];
>> [A B]
ans =

    1    2   11   12
    3    4   13   14
    5    6   15   16

>> [A;B]
ans =

    1    2
    3    4
    5    6
   11   12
   13   14
   15   16
   
>> A(:)     % 小技巧，flatten 一个矩阵，按列顺序排列
ans =

     1
     3
     5
    10
    11
    12
   100
   101
   102

```

<h2 id="ba5e7829f63ffdcc50f799fa90bbe124"></h2>

## 矩阵运算
<h2 id="9ee76a86a85ebc392cc58adcd82755ac"></h2>

##### 加法 A + B , 各元素相加
```
>> A + B
ans =

   12   14
   16   18
   20   22
```   

<h2 id="0f8c8570065113d98309db042de5dc45"></h2>

##### 数加 A+1  , 所有元素+1

```
>> A+1
ans =

   2   3
   4   5
   6   7
```

<h2 id="2f5235a090db9cbf0b62bc8ec01379a6"></h2>

##### 乘法 A*B ,  矩阵乘法
---
<h2 id="85544a6ab193a65265eaaeddd9ac1569"></h2>

##### 矩阵点乘 A.*B  , 各元素相乘:  

    A=[1;2];B=[3;4];   % sum(A.*B) == A'*B 


<h2 id="54d294e059bbc06f4ef1d98a54ab763a"></h2>

#### 叉积 cross, 至少一个维度大于3

---
<h2 id="8cb0042601b89d343ede0618848c0443"></h2>

##### 矩阵数乘法 A *2  , 所有元素 *2

<h2 id="15c3b7e97c9b84449d7318aceba06a80"></h2>

##### A.^2          , 所有元素平方  

```
>> A.^2
ans =

    1    4
    9   16
   25   36
```

<h2 id="5da2497e58940ef2f391789c62b74213"></h2>

##### 1 ./ A   , 所有元素的倒数
```
>> 1./A
ans =

   1.00000   0.50000
   0.33333   0.25000
   0.20000   0.16667
```

<h2 id="a7d68adc4d02bff1cc1a0f7764718b5a"></h2>

##### 对数log(A)，指数exp(A)

<h2 id="0d3c6f75b597405e7a5bd3dca1fe8b9a"></h2>

##### abs 绝对值

<h2 id="e9ffbcb910a3a6ac2979fcfedcbd3d01"></h2>

##### -v  % -1*v

<h2 id="3aba41f7e265ee9a755472697dda5eb0"></h2>

##### max(A)  最大值 

```
>> val = max(A)
val =

   5   6

>> val , index  = max(A)
val =

   5   6

index =

   5   6
   
>> max(A,[],1)      % 按列求最大值，默认
ans =

   5   6

>> max(A,[],2)      % 按行求最大值
ans =

   2
   4
   6   
   
>> max(max(A))      % 矩阵范围的最大值
ans =  6
>> max(A(:))        % 矩阵范围的最大值 
ans =  6   
```

<h2 id="23deac19e3ffb9356677692a6e457f89"></h2>

##### max(A,B) , 返回一个矩阵，元素是 A,B各元素的最大值

<h2 id="b459cf35a08fbbafa132c845e873a684"></h2>

##### Filter A <= 3  , 各元素比较的结果
```
>> A <= 3
ans =

   1   1
   1   0
   0   0
```

<h2 id="a4155f1a9d0b04da44f33812d717c0d5"></h2>

##### find( filter ) : find( A<=3), 注意接受 find返回值的变量个数
```
>> r,c = find( A<=3)
ans =

   1
   2
   4
   
>> [r,c] = find(A<=3)
r =

   1
   2
   1

c =

   1
   1
   2
   
```

<h2 id="ca8891f30cdfd2185e065e8156c3446d"></h2>

##### 求和 sum 
```
>> sum(A)
ans =

    9   12
    
>> sum(A,1)
ans =

    9   12

>> sum(A,2)
ans =

    3
    7
   11
   
>> B=[1 2;10,12]    % 主对角线 辅对角线求和
B =

    1    2
   10   12

>> sum( sum(B.*eye(2)) )   % 主对角线 求和
ans =  13
>> sum( sum(B.*flipud(eye(2))) )  % 辅对角线 求和
ans =  12
```


<h2 id="258cb2eb8e998fd10888ef8c9dd7628c"></h2>

##### 求积 prod
```
>> prod(A)
ans =

   15   48
```

<h2 id="5eac4647e29237b13fd08b162de55898"></h2>

##### floor, ceil

---

<h2 id="3b06c53acea624df1786802a6ac1e81f"></h2>

##### Transpose 转置  A'
```
>> A'
ans =

   1   3   5
   2   4   6
```   

<h2 id="e483f22bccac27c7aa4bb146a6a95b7b"></h2>

##### magic 好玩但没卵用
```
>> magic(3)
ans =

   8   1   6
   3   5   7
   4   9   2
```

<h2 id="84becd6270e11d304352cfd8cce872b3"></h2>

##### invert 逆矩阵  pinv
```
>> C=magic(3)
C =

   8   1   6
   3   5   7
   4   9   2

>> pinv(C)
ans =

   0.147222  -0.144444   0.063889
  -0.061111   0.022222   0.105556
  -0.019444   0.188889  -0.102778
```

<h2 id="0aabb2e84a3f1c8c85b42b73abb1239d"></h2>

#### a=a(:)   

确保向量a 转为 列向量

---

<h2 id="37a8bc45f9e398cdffe832b507cf789b"></h2>

## cell array

```
a={ 'a' , 'b' , 'c'  }
a = 
{
  [1,1] = a
  [1,2] = b
  [1,3] = c
}

```
