...menustart

 - [工作 working Tips](#5e36152a2ca8486c6434db9265f0a638)
     - [proxy setting](#264bb46a005f7dc5d0e7195296f1d501)
     - [curl 对某些 url 不使用代理](#b679a9a1692cc49ba9e914809bbe4f66)
     - [pip 使用国内源](#2dea1f148fc0810bfd87d46579674f7e)
     - [pip upgrade all outdated package](#1bca9692962e3deeda270ab8db1b80f2)
     - [FileMerge](#19a991a87a69e4435918f98d2ffc8421)
     - [Get Proxy Info](#ca07600a3602fddc156831a6716fae12)
     - [lldb 调试 Segment Fault on MacOSX](#93bc8417f2018ae4424cbad9060081fa)
     - [download youtube playlist](#dd3177fffb44df0088f08893f1e8b000)
     - [re-download youtube auto sub](#a86e10fc913cd54076f6a27289d1d713)
     - [ab testing](#ac1edf8d7497b1d5b6039ad9656cdeee)
     - [check wheter `keep-alive` is  enabled by server](#e06944207d65338bc4b5d43aef44aef4)
     - [change .pem password](#60a277f978363c21b4ced8cb1ea9c06f)

...menuend


<h2 id="5e36152a2ca8486c6434db9265f0a638"></h2>


# 工作 working Tips

<h2 id="264bb46a005f7dc5d0e7195296f1d501"></h2>


## proxy setting

```
export _proxy=username:password@IP_or_DOMAIN:3128
export  http_proxy=http://$_proxy
export https_proxy=http://$_proxy


export  HTTP_PROXY=$http_proxy
export HTTPS_PROXY=$https_proxy


#u3d proxy ?
export  HTTP_proxy=$http_proxy
export HTTPS_proxy=$https_proxy

# export NO_PROXY=localhost,localhost.,127.0.0.1,10.96.0.0/12,10.244.0.0/16,10.192.0.0/16
export NO_PROXY="localhost,127.0.0.*,10.96.0.0/12,10.244.0.0/16,10.192.0.0/16"
export no_proxy=$NO_PROXY
```

<h2 id="b679a9a1692cc49ba9e914809bbe4f66"></h2>


## curl 对某些 url 不使用代理

```
curl -v --noproxy 127.0.0.1
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

<h2 id="19a991a87a69e4435918f98d2ffc8421"></h2>


## FileMerge

opendiff **file1** **file2**

or for entire directories

opendiff **dir1** **dir2**

or 

/Developer/Applications/FileMerge.app/Contents/MacOS/FileMerge -left “File1” -right "File2" -ancestor "File3" -merge "File4"



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
youtube-dl -c --write-auto-sub --sub-lang=en --ignore-errors -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' 'https://www.youtube.com/playlist?list=PLKUel_nHsTQ1yX7tQxR_SQRdcOFyXfNAb'
```

 - 如果视频确定有 premade 字幕， 使用  `--write-sub`
 - ensure you add `' '` to url since some special character may appears in URL has a special meaning in bash
 - `-c` means resume downloading 
 - `--ignore-errors` 忽略下载错误，比如 private vidoe

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
    - caution: not work with nodejs. it is a bug of ab , since ab is a http 1.0 client. You should add extra `-H "TE: chunked"`

<h2 id="e06944207d65338bc4b5d43aef44aef4"></h2>


## check wheter `keep-alive` is  enabled by server

- `url -lv -k <url> <url>  2>&1 | grep  "Re-using" `

```bash
$ curl -lv -k https://xxx.com/ https://xxx.com/  2>&1 | grep  "Re-using"
* Re-using existing connection! (#0) with host xxx.com
```

<h2 id="60a277f978363c21b4ced8cb1ea9c06f"></h2>


## change .pem password

```bash
mv config/private.pem config/private_old.pem

openssl rsa -in config/private_old.pem -out config/private.pem -des3
```



