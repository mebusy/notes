...menustart

 - [工作 working Tips](#5e36152a2ca8486c6434db9265f0a638)
     - [curl, git use proxy server](#a96aeb959a8752f7651b158432def768)
     - [curl 对某些 url 不使用代理](#b679a9a1692cc49ba9e914809bbe4f66)
     - [curl POST json](#6e7f57f08bd46f2974f740a03f93d823)
     - [telnet proxy](#345083ba0f34a9b30e91bb1e37094517)
     - [brew work with proxy](#9158a77bfc692a7ddb411e8c41776b56)
     - [pip install package with proxy](#762fac82abbaaf86cfc10780f5b7cc58)
     - [pip 使用国内源](#2dea1f148fc0810bfd87d46579674f7e)
     - [pip upgrade all outdated package](#1bca9692962e3deeda270ab8db1b80f2)
     - [bazel](#24ef4c36ec66c15ef9f0c96fe27c0e0b)
     - [FileMerge](#19a991a87a69e4435918f98d2ffc8421)
     - [tcpkill](#0dcd3e0e4377857453bb9a2db4a20139)
     - [CentOS yum 无法更新](#16c9778b7075982cf3d39ff738d292f0)
     - [Vbox CentOS instal Guest Addition](#0afd0f413908f4cc7cddd138dde0ddd6)
     - [Get Proxy Info](#ca07600a3602fddc156831a6716fae12)
     - [lldb 调试 Segment Fault on MacOSX](#93bc8417f2018ae4424cbad9060081fa)
     - [download youtube playlist](#dd3177fffb44df0088f08893f1e8b000)
     - [re-download youtube auto sub](#a86e10fc913cd54076f6a27289d1d713)
     - [ab testing](#ac1edf8d7497b1d5b6039ad9656cdeee)

...menuend


<h2 id="5e36152a2ca8486c6434db9265f0a638"></h2>


# 工作 working Tips

<h2 id="a96aeb959a8752f7651b158432def768"></h2>


## curl, git use proxy server

```
export http_proxy=http://username:password@IP_or_DOMAIN:3128
export https_proxy=https://username:password@IP_or_DOMAIN:3128
```

<h2 id="b679a9a1692cc49ba9e914809bbe4f66"></h2>


## curl 对某些 url 不使用代理

```
curl -v --noproxy 127.0.0.1
```

<h2 id="6e7f57f08bd46f2974f740a03f93d823"></h2>


## curl POST json

```
cmd =  'curl --noproxy 10.192.1.35  -H "Content-Type: application/json" -X POST  http://10.192.1.35:8081/clientSettings/add/tvInteractive -d \'%s\' ' %   strProtocal
```

<h2 id="345083ba0f34a9b30e91bb1e37094517"></h2>


## telnet proxy

1. 安装 proxychains
    - `brew install proxychains-ng` 
    - 修改配置
    - `vi /usr/local/etc/proxychains.conf`
        - 在 [ProxyList] 下面（也就是末尾）加入代理类型，代理地址和端口
        - `http  10.192.0.91  3128 username password`
        - ip only , no domain
2. copy telnet 到 /usr/local/bin/ , 因为在 /usr/bin 下的程序受到 **SIP(System Integrity Protection)** 限制, proxychains 无法起作用


<h2 id="9158a77bfc692a7ddb411e8c41776b56"></h2>


## brew work with proxy

```
https_proxy=$http_proxy brew xxxx
```


<h2 id="762fac82abbaaf86cfc10780f5b7cc58"></h2>


## pip install package with proxy

```
sudo -E pip install PyYAML
```

or 

```
pip install PyYAML --proxy="https://127.0.0.1:3128"
```

<h2 id="2dea1f148fc0810bfd87d46579674f7e"></h2>


## pip 使用国内源

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ... 
```

<h2 id="1bca9692962e3deeda270ab8db1b80f2"></h2>


## pip upgrade all outdated package

```
pip list --outdated | cut -d' ' -f1 | xargs pip install --upgrade
```

<h2 id="24ef4c36ec66c15ef9f0c96fe27c0e0b"></h2>


## bazel 

bazel not support lower case proxy setting

```
sudo -E HTTP_PROXY=$http_proxy  HTTPS_PROXY=$https_proxy bazel 
```

<h2 id="19a991a87a69e4435918f98d2ffc8421"></h2>


## FileMerge

opendiff **file1** **file2**

or for entire directories

opendiff **dir1** **dir2**

or 

/Developer/Applications/FileMerge.app/Contents/MacOS/FileMerge -left “File1” -right "File2" -ancestor "File3" -merge "File4"



<h2 id="0dcd3e0e4377857453bb9a2db4a20139"></h2>


## tcpkill

https://github.com/ggreer/dsniff

<h2 id="16c9778b7075982cf3d39ff738d292f0"></h2>


## CentOS yum 无法更新 

```
yum clean all
yum check
yum erase apf
yum upgrade
```

<h2 id="0afd0f413908f4cc7cddd138dde0ddd6"></h2>


## Vbox CentOS instal Guest Addition

```
yum update
yum install gcc kernel-devel bzip2
mkdir -p /media/cdrom
mount /dev/scd0 /media/cdrom
sh /media/cdrom/VBoxLinuxAdditions.run
```

<h2 id="ca07600a3602fddc156831a6716fae12"></h2>


## Get Proxy Info

chrome: `chrome://net-internals/#proxy`


<h2 id="93bc8417f2018ae4424cbad9060081fa"></h2>


## lldb 调试 Segment Fault on MacOSX
 
 - 编译加上 `+g` 选项
 - `ulimit -c unlimited`
 - /cores/core.xxx 文件生成
 - `lldb appname core.15667`
 - 运行， crash后，输入 `bt` 打印跟踪堆栈


<h2 id="dd3177fffb44df0088f08893f1e8b000"></h2>


## download youtube playlist


```
youtube-dl -c --write-auto-sub --sub-lang=en  -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' 'https://www.youtube.com/playlist?list=PLKUel_nHsTQ1yX7tQxR_SQRdcOFyXfNAb'
```

 - 如果视频确定有 premade 字幕， 使用  `--write-sub`

 - ensure you add `' '` to url since some special character may appears in URL has a special meaning in bash

 - `-c` means resume downloading 

<h2 id="a86e10fc913cd54076f6a27289d1d713"></h2>


## re-download youtube auto sub

```
youtube-dl --write-auto-sub --skip-download --sub-lang=en  ...
```
 
<h2 id="ac1edf8d7497b1d5b6039ad9656cdeee"></h2>


## ab testing 

```
ab -r -k -s 120 -n 100000 -c 1500  <url>
```

 - `-s`  timeout, default is 30sec
 - `-r`  Don't exit on socket receive errors.
 - `-k`  Use HTTP KeepAlive feature


 
