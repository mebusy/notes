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
    - [youtube-dl download mp3 audio only](#a070b11a3504a9c79ea234b981f7db6d)
    - [using ffmpeg to convert video to mp3 (未验证)](#a8e23293ddbb3302f18d430ee2fdaaf2)
    - [use ffmpeg select left audio channel and downgrade to mono](#160eb38b6a6c8f90bf98171aa12bb8d8)
    - [use ffmpeg manipulate audio channel](#a2ccb84c0c3f7f1113c305a7f2499969)
    - [ab testing](#ac1edf8d7497b1d5b6039ad9656cdeee)
    - [check wheter `keep-alive` is  enabled by server](#e06944207d65338bc4b5d43aef44aef4)
    - [change .pem password](#60a277f978363c21b4ced8cb1ea9c06f)
    - [Python NTLM proxyserver](#3f1c0d7e44459f6410faabec903ea4ac)
    - [获取外网ip](#869d7745a2b610e3fcd5afed798f8986)
    - [MacOSX add Printer in Windows LAN](#c792dc1d6bbb6c2565d0dd1a20020b86)
    - [Bash , exit or ret ?](#0f1b43a16569025f1d077ac18dc4810f)
    - [FTP Server](#98cc3814df5e703cb40d72247999d91a)
    - [check port using](#ab1922f2cde102e230acb305eb9338f2)
    - [Check process](#620a23e22d25f0b53a694b9daf289219)

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

<h2 id="a070b11a3504a9c79ea234b981f7db6d"></h2>


## youtube-dl download mp3 audio only

```bash
youtube-dl -x --audio-format mp3  'your-url'
```

Or list all support format, and pick one audio-only format

```bash
$ youtube-dl -F  'your-url'
format code  extension  resolution note
249          webm       audio only tiny   53k , webm_dash container, opus @ 53k (48000Hz), 1.10MiB
250          webm       audio only tiny   72k , webm_dash container, opus @ 72k (48000Hz), 1.49MiB
140          m4a        audio only tiny  127k , m4a_dash container, mp4a.40.2@127k (44100Hz), 2.60MiB
251          webm       audio only tiny  140k , webm_dash container, opus @140k (48000Hz), 2.87MiB
278          webm       256x144    144p   97k , webm_dash container, vp9@  97k, 13fps, video only, 2.00MiB
160          mp4        256x144    144p  108k , mp4_dash container, avc1.42c00c@ 108k, 13fps, video only, 2.23Mi

$ youtube-dl -f 140  'your-url'
```



<h2 id="a8e23293ddbb3302f18d430ee2fdaaf2"></h2>


## using ffmpeg to convert video to mp3 (未验证)

```bash
To encode a high quality MP3 from an AVI best use -q:a for variable bit rate:

ffmpeg -i sample.avi -q:a 0 -map a sample.mp3

-af 'volume=2'

-q:a for variable bit rate:
```

<h2 id="160eb38b6a6c8f90bf98171aa12bb8d8"></h2>


## use ffmpeg select left audio channel and downgrade to mono

```bash
# ffmpeg -i input -map_channel 0.0.0 output
ffmpeg -i xxx.m4a -map_channel 0.0.0 output.mp3
```

<h2 id="a2ccb84c0c3f7f1113c305a7f2499969"></h2>


## use ffmpeg manipulate audio channel

https://trac.ffmpeg.org/wiki/AudioChannelManipulation

change audio volume

```bash
# low 50% volume of left audio channel
-af  "pan=stereo|c0=0.5*c0|c1=c1"
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


## tcpdump on OSX

Choose the Correct Interface

```bash
$ networksetup -listallhardwareports

Hardware Port: Ethernet
Device: en0
Ethernet Address: 54:45:5b:01:ca:89
```

listen on all src/dst net with address 192.30.0.0/16, and port 443

```bash
$ sudo tcpdump -i en0 net 192.30.0.0/16  and  port 443 -n
```



<h2 id="869d7745a2b610e3fcd5afed798f8986"></h2>


## 获取外网ip

```bash
curl ifconfig.co
```

<h2 id="c792dc1d6bbb6c2565d0dd1a20020b86"></h2>


## MacOSX add Printer in Windows LAN

- Advanced
    - Type: Windows printer via spoolss
    - URL: `smb://<printer's IP or domain name>/<printer name>`


<h2 id="0f1b43a16569025f1d077ac18dc4810f"></h2>


## Bash , exit or ret ? 

if you execute your bash script with `source` , `exit` command will stop the user shell. 

to prevent it 

```bash
[[ "$0" == "$BASH_SOURCE" ]] && ret=exit || ret=return
...
$ret 1
```


<h2 id="98cc3814df5e703cb40d72247999d91a"></h2>


## FTP Server

```bash
pip3 install pyftpdlib
python3 -m pyftpdlib -w -p 80
```


<h2 id="ab1922f2cde102e230acb305eb9338f2"></h2>


## check port using

Linux: 

```bash
netstat -tunlp | grep 8080
```

The closest equivalent you can get on macOS is:

```bash
netstat -p tcp -van | grep '^Proto\|LISTEN' | grep 8080
```

Or use lsof  (list opened files)

```bash
sudo lsof -i:8080
```

NOTE: lsof just list files opened by current users,  you need add `sudo` if you want to see all opened files.

<h2 id="620a23e22d25f0b53a694b9daf289219"></h2>


## Check process

```bash
ps -ef | grep tomcat
```

- `-e` : all processes
- `-f` : full






