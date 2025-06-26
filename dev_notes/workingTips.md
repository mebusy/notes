[](...menustart)

- [工作 working Tips](#5e36152a2ca8486c6434db9265f0a638)
    - [proxy setting](#264bb46a005f7dc5d0e7195296f1d501)
    - [curl 对某些 url 不使用代理](#b679a9a1692cc49ba9e914809bbe4f66)
    - [pip 使用国内源](#2dea1f148fc0810bfd87d46579674f7e)
    - [pip upgrade all outdated package](#1bca9692962e3deeda270ab8db1b80f2)
    - [FileMerge](#19a991a87a69e4435918f98d2ffc8421)
    - [Get Proxy Info](#ca07600a3602fddc156831a6716fae12)
    - [lldb 调试 Segment Fault on MacOSX](#93bc8417f2018ae4424cbad9060081fa)
    - [download youtube playlist : yt-dlp](#139e4d9ac2e847f7d427ba67996b489a)
        - [re-download youtube auto sub](#a86e10fc913cd54076f6a27289d1d713)
        - [yt-dlp download mp3 audio only](#57065f297414ce97d3e39c4619a99fc3)
    - [using ffmpeg to convert video to mp3 (未验证)](#a8e23293ddbb3302f18d430ee2fdaaf2)
    - [use ffmpeg select left audio channel and downgrade to mono](#160eb38b6a6c8f90bf98171aa12bb8d8)
    - [use ffmpeg manipulate audio channel](#a2ccb84c0c3f7f1113c305a7f2499969)
    - [merge subtile to video](#89227893b957e1a49fb887ab2e9c7441)
    - [ab benchmark](#4eda4ef40a71cb2632162cc03ece5480)
    - [check wheter `keep-alive` is  enabled by server](#e06944207d65338bc4b5d43aef44aef4)
    - [change .pem password](#60a277f978363c21b4ced8cb1ea9c06f)
    - [tcpdump on OSX](#c49947d2d71ef4c590461fc98b234651)
    - [获取外网ip](#869d7745a2b610e3fcd5afed798f8986)
    - [MacOSX add Printer in Windows LAN](#c792dc1d6bbb6c2565d0dd1a20020b86)
    - [Bash , exit or ret ?](#0f1b43a16569025f1d077ac18dc4810f)
    - [FTP Server](#98cc3814df5e703cb40d72247999d91a)
    - [\[MacOSX\] move large files out of system volumn](#876a5afb8f5f4d9fe22d3f93b322e87d)
    - [\[MacOSX\] monitor files changes under current folder](#75da08a12859c3c32281ae78bfb39348)
    - [\[MacOSX\] chrome gpu acceleration not work](#dbf1e7162f6bb3506ff0d88de4b6f014)

[](...menuend)


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


<h2 id="139e4d9ac2e847f7d427ba67996b489a"></h2>

## download youtube playlist : yt-dlp

- install: deprecated !!!
    - ~`brew install yt-dlp`~
- best installation
    ```bash
    python3 -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
    yt-dlp URL
    ```

```
yt-dlp --ignore-errors --rm-cache-dir -c --write-auto-sub --sub-lang=en   -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' --cookies-from-browser chrome 'https://www.youtube.com/playlist?list=PLKUel_nHsTQ1yX7tQxR_SQRdcOFyXfNAb'
```


- 如果视频确定有 premade 字幕， 使用  `--write-sub`
- ensure you add `' '` to url since some special character may appears in URL has a special meaning in bash
- other useful options
    - `-c` means resume downloading 
    - `--ignore-errors` 忽略下载错误，比如 private vidoe
    - `--rm-cache-dir` 避免403 错误
- start from specific entry from a list, e.g. from 20
    - `--playlist-start 20`

<h2 id="a86e10fc913cd54076f6a27289d1d713"></h2>

### re-download youtube auto sub

```bash
$ yt-dlp --write-auto-sub --skip-download --sub-lang=en  ...
```

<h2 id="57065f297414ce97d3e39c4619a99fc3"></h2>

### yt-dlp download mp3 audio only

```bash
yt-dlp --ignore-errors --rm-cache-dir  -x --audio-format mp3  'your-url'
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


<h2 id="89227893b957e1a49fb887ab2e9c7441"></h2>

## merge subtile to video

```bash
# mergeSubtile.sh

#!/bin/sh

set -e

INFILE=$1
SUBTITLES=$2

# if arguments are not passed, show usage and exit
if [ $# -ne 2 ]; then
    echo "Usage: $0 <inputfile> <subtitlefile>"
    exit 1
fi

echo $INFILE , $SUBTITLES

ffmpeg -i $SUBTITLES temp.ass && \
BITRATE=$(ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 $INFILE) && \
ffmpeg -i $INFILE -vf ass=temp.ass -vcodec h264_videotoolbox -b:v $BITRATE -c:a copy output_burnedin.mp4
```

 
<h2 id="4eda4ef40a71cb2632162cc03ece5480"></h2>

## ab benchmark

```
ab -r -k -s 120 -n 100000 -c 1500  <url>
```

- `-s`  timeout, default is 30sec
- `-r`  Don't exit on socket receive errors.
- `-k`  Use HTTP KeepAlive feature
    - caution: not work with nodejs. it is a bug of ab , since ab is a http 1.0 client. You should add extra `-H "TE: chunked"`

- Post Example
    ```bash
    ab -r -k -s 120 -n 100000 -c 1500 \
        -H 'accept: application/json' -H 'token: asdf' \
        -T application/json -p body.json  \
        'http://localhost:3000/user'
    ```
    - the 2nd line is Arbitrary header
    - the 3rd line,  `-p` specify the post file, `-T` specify content-type


<h2 id="e06944207d65338bc4b5d43aef44aef4"></h2>

## check wheter `keep-alive` is  enabled by server

```bash
curl -I <url>
```

<h2 id="60a277f978363c21b4ced8cb1ea9c06f"></h2>

## change .pem password

```bash
mv config/private.pem config/private_old.pem

openssl rsa -in config/private_old.pem -out config/private.pem -des3
```

OR

```bash
ssh-keygen -p -m PEM -f <path-to-private-key>
```


<h2 id="c49947d2d71ef4c590461fc98b234651"></h2>

## tcpdump on OSX

[tcpdump on OSX](tcpdump_osx.md)

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





<h2 id="876a5afb8f5f4d9fe22d3f93b322e87d"></h2>

## [MacOSX] move large files out of system volumn

```bash
DockerRaw  ->  ~/Library/Containers/com.docker.docker/Data/vms/0/data
UnityLogs  ->  ~/Library/Logs/Unity
```

If you dont want Unity write log file to disk

```bash
$ ln -s -f /dev/null Editor.log
```

<h2 id="75da08a12859c3c32281ae78bfb39348"></h2>

## [MacOSX] monitor files changes under current folder

```bash
brew install watch

watch -n 1 -d find .

# to skie .git folder
watch -n 1 -d find . -path ./.git  -prune -o -print
```

<h2 id="dbf1e7162f6bb3506ff0d88de4b6f014"></h2>

## [MacOSX] chrome gpu acceleration not work

1. delete chrome app
2. delete `~/Library/Application Support/Google/Chrome`
3. reinstall chrome app

check chrome gpu acceleration status

```bash
chrome://gpu
```



