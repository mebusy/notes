...menustart

 * [linux shell 重定向和管道](#a5b6d6e1787010e24a6983fc8cdc05e8)
   * [重定向](#c51dd14a9a9366c6f8f09737d88efde2)
     * [输出重定向：](#b055038e72d0aee6b98113e5aa18bca7)
     * [输入重定向](#61c2440af0105a4ba9d0629753f0ad3b)
   * [管道命令](#4b9705489e3c43bd30937dfd11787372)
     * [shell脚本接收管道输入](#0fbce22ca968c3e4c0611f0d78397112)

...menuend


<h2 id="a5b6d6e1787010e24a6983fc8cdc05e8"></h2>
# linux shell 重定向和管道

<h2 id="c51dd14a9a9366c6f8f09737d88efde2"></h2>
## 重定向

linux shell下常用输入输出操作符是：

1. 标准输入   (stdin) ：代码为 0 ，使用 < 或 << ； 
   /dev/stdin -> /proc/self/fd/0   0代表：/dev/stdin 
2. 标准输出   (stdout)：代码为 1 ，使用 > 或 >> ； 
   /dev/stdout -> /proc/self/fd/1  1代表：/dev/stdout
3. 标准错误输出(stderr)：代码为 2 ，使用 2> 或 2>> ； 
   /dev/stderr -> /proc/self/fd/2 2代表：/dev/stderr


    << , >> 是追加操作

<h2 id="b055038e72d0aee6b98113e5aa18bca7"></h2>
### 输出重定向：

    格式： command-line1 [1-n] > file或文件操作符或设备
说明：将一条命令执行结果（标准输出，或者错误输出，本来都要打印到屏幕上面的）

重定向其它输出设备（文件，打开文件操作符，或打印机等等）1,2分别是标准输出，错误输出。

    1>可以省略，不写，默认所至标准输出


举例：

    #显示当前目录文件 test.sh test1.sh test1.sh实际不存在
    
    #将错误输出信息关闭掉
    $ ls test.sh test1.sh 2>&-
    test.sh
    $ ls test.sh test1.sh 2>/dev/null
    test.sh
    
    说明:   &[n] 代表是已经存在的文件描述符，&1 代表输出 &2代表错误输出 
    
            &-代表关闭与它绑定的描述符
            
    	    /dev/null 这个设备，是linux 中黑洞设备， 
    	    
    	    什么信息只要输出给这个设备，都会给吃掉 .
    
    #关闭所有输出
    $ ls test.sh test1.sh  1>&- 2>&- 
    
    #将错误输出2 绑定给 正确输出 1，然后将 正确输出 发送给 /dev/null设备  这种常用
    $ ls test.sh test1.sh >/dev/null 2>&1
    
    # 所有标准输出与错误输出 输入到/dev/null文件
    $ ls test.sh test1.sh &>/dev/null
    说明: & 代表标准输出 ，错误输出 将所有标准输出与错误输出 输入到/dev/null文件
    
    注意: 一条命令在执行前，先会检查输出是否正确，
          如果输出设备错误，将不会进行命令执行


<h2 id="61c2440af0105a4ba9d0629753f0ad3b"></h2>
### 输入重定向

格式：

    command-line [n] <file或文件描述符&设备

说明：将 默认从键盘获得的输入，改成从文件，或者其它打开文件以及设备输入。

执行这个命令，将标准输入0，与文件或设备绑定。将由它进行输入。

    #从键盘输入数据到 文件 catfile, ctrl-D 结束输入
    cat > catfile 
    
    #cat 从test.sh 获得输入数据，然后输出给文件catfile
    $ cat>catfile <test.sh
    
    #输入 eof 自动结束输入， 不需要按  ctrl-D
    cat>catfile <<eof
    说明：<< 这个连续两个小符号， 他代表的是『结束的输入字符』的意思。 
    这样当空行输入eof字符，输入自动结束，不用ctrl+D.


<h2 id="4b9705489e3c43bd30937dfd11787372"></h2>
## 管道命令

管道命令操作符是：”|”,  它仅能处理经由前面一个指令传出的正确输出信息，也就是 standard output 的信息，

对于 stdandard error 信息没有直接处理能力。然后，传递给下一个命令，作为标准的输入 standard input.

    注意: 只有可以接收标准输入的命令才可以用作管道右边

例子:

    #读出 catfile的内容， 通过管道 转发给grep 作为输入内容
    cat catfile | grep -n 'aaaa'
    2:aaaa
    
    
    # 通过管道发送给ls命令，由于ls 不支持标准输入，因此数据被丢弃
    $ cat catfile | ls 
    catfile       setTrigger.sh tmp           watch.py


<h2 id="0fbce22ca968c3e4c0611f0d78397112"></h2>
### shell脚本接收管道输入

```bash
<h2 id="79b229b3b4c3182cfe215ebaaafd966d"></h2>
#!/bin/sh
  
if [ $# -gt 0 ];then
    exec 0<$1;
    #判断是否传入参数：文件名，如果传入，将该文件绑定到标准输入
fi
  
while read line
do
    echo $line;
done<&0;
<h2 id="0f57fce322b63a2089cc5dc8772c00b9"></h2>
#通过标准输入循环读取内容

exec 0&-;
<h2 id="d28c73c094fdea31745432f6722fcbb9"></h2>
#解除标准输入绑定
```
