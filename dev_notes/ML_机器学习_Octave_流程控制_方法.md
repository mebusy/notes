...menustart

- [控制语句](#ea5302a4c0247998e1de210b879bef5f)
    - [for](#d55669822f1a8cf72ec1911e462a54eb)
    - [while](#901889f4f34f8ca18ac2f53d1fed346e)
    - [if  elseif else](#14fdbb00ba740a5e6e2ebb154af73572)
    - [break, continue](#e431a54db2dbf8b6dd89898db017fce2)
- [方法](#ea340b9dda8b893ddf2d9176220aac32)
    - [定义 function RETURN = FUNC_NAME( PARAMS )](#f7c1ab0d7de72d584ef32e3bfcc9655f)
    - [多个返回值 function \[RET1, RET2\] = FUNC_NAME( PARAMS )](#962022740b9969866c7e970cc43c2f59)
    - [例子: 代价函数J](#71db28af5c0579013c3ed99662d36a77)
    - [addpath(path) 添加搜索路径，以便 Octave 发现方法定义文件](#d21b656001498d6544c47c1a617bf4a1)

...menuend


<h2 id="ea5302a4c0247998e1de210b879bef5f"></h2>


# 控制语句

<h2 id="d55669822f1a8cf72ec1911e462a54eb"></h2>


#### for
```
>> for i=1:10,
>   v(i) = 2^i ;  % ;不要漏
> end;
>> indices= 1:10; % 序列
>> for i=indices,
>   disp(i);
> end;
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
 
```

<h2 id="901889f4f34f8ca18ac2f53d1fed346e"></h2>


#### while
```
>> i=1;
>> while i<=5,
>   v(i) = 100;
>   i=i+1;
> end;
>> 
```

<h2 id="14fdbb00ba740a5e6e2ebb154af73572"></h2>


#### if  elseif else
```
>> w=1;
>> if w==1,
>   disp('one') ;
> elseif w==2,
>   disp('two') ;
> else
>   disp("other");
> end;
one
```

<h2 id="e431a54db2dbf8b6dd89898db017fce2"></h2>


#### break, continue
---
<h2 id="ea340b9dda8b893ddf2d9176220aac32"></h2>


# 方法

<h2 id="f7c1ab0d7de72d584ef32e3bfcc9655f"></h2>


##### 定义 function RETURN = FUNC_NAME( PARAMS )

<h2 id="962022740b9969866c7e970cc43c2f59"></h2>


##### 多个返回值 function [RET1, RET2] = FUNC_NAME( PARAMS )

<h2 id="71db28af5c0579013c3ed99662d36a77"></h2>


##### 例子: 代价函数J

```
function J=costFunctionJ( X,y, theta )

% X is the design matrix [1, A ]
% 注意语句后面加上;  不然每一步都会有输出

m=size(X,1);   % feature 数量
predictions = X*theta ;  % 矩阵-向量乘法,计算出所有的h(x)
sqrErrors = (predictions-y).^2 ;  % 计算误差的平方

J= 1/(2*m) * sum( sqrErrors ) ;    % 计算代价

end
```

```
>> X =[1 1;1 2 ; 1 3]
X =

   1   1
   1   2
   1   3

>> Y = [1;2;3]
Y =

   1
   2
   3

>> theta = [0;1]
theta =

   0
   1

>> costFunctionJ( X,Y, theta )
ans = 0
>> theta = [0;0]
theta =

   0
   0

>> costFunctionJ( X,Y, theta )
ans =  2.3333

```
---
<h2 id="d21b656001498d6544c47c1a617bf4a1"></h2>


##### addpath(path) 添加搜索路径，以便 Octave 发现方法定义文件
