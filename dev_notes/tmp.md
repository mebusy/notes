...menustart


...menuend


软件开发, 游戏开发中使用的随机数，一般是伪随机数。

伪随机数, 是一组分布在某个特定范围内的数字序列。

1,2,3,4...


这些数字看起来毫无规律，但实际上是, 是由简单的数学算法生成的,是可以预测的。


生成随机数序列的算法有很多


在这里，我们举例介绍一下其中的一个最古老最有名的算法, 线性同余法。 



线性同余法 选择4个魔术数字


1个种子 

一个 乘数 a , 一个增量 c , 一个模数 m

( S * a  + c ) mod m ,


计算结果 用于输出随机数序列， 同时会成为新的种子S






十、注意点

需要保证每次随机的数字都相同，所以需要自己实现一套随机数，不能用unity自带的那个随机数接口，而且需要服务端发送相同的随机种子；因为非常微小的误差就有可能产生蝴蝶效应，所以所有float型的参数必须变成int型，保证计算结果一致。



浮点精度的问题在PC上就有跨平台的问题，因为语言编译器不同使用的寄存器和运算过程中的舍入方式不同。就会导致在不同平台下相同的float运算会出现不同的结果，这方面有很多文章阐述就不多做阐述。而在手机上IOS还好比较单纯，Android设备系统硬件千差万别就更容易出现精度问题了。

定点数 + 辅以三角函数查表

大菠萝3   tracks the amount of time you spend fighting creatures without finding a legendary and after a certain perion of time will slowling start increasing the legendary drop rate.


```python
>>> a = [2,1]
>>> b = [1,2]
>>> np.cross(a,b)
array(3)
>>> a = [2,1,0]
>>> b = [1,2,0]
>>> np.cross(a,b)
array([0, 0, 3])
>>>
```




