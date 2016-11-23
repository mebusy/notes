# 工作 working Tips

## curl, git use proxy server

```
export http_proxy=http://username:password@IP_or_DOMAIN:3128
export https_proxy=https://username:password@IP_or_DOMAIN:3128
```

## curl 对某些 url 不使用代理

```
curl -v --noproxy 127.0.0.1
```

## curl POST json

```
cmd =  'curl --noproxy 10.192.1.35  -H "Content-Type: application/json" -X POST  http://10.192.1.35:8081/clientSettings/add/tvInteractive -d \'%s\' ' %   strProtocal
```

## telnet proxy

1. 安装 proxychains
    - `brew install proxychains-ng` 
    - 修改配置
    - `vi /usr/local/etc/proxychains.conf`
        - 在 [ProxyList] 下面（也就是末尾）加入代理类型，代理地址和端口
        - `http  10.192.0.91  3128 username password`
        - ip only , no domain
2. copy telnet 到 /usr/local/bin/ , 因为在 /usr/bin 下的程序受到 **SIP(System Integrity Protection)** 限制, proxychains 无法起作用


## brew work with proxy

```
https_proxy=$http_proxy brew xxxx
```

## Install Pip use proxy
## set proxy for python

```
sudo -E easy_install pip
```

## pip install package with proxy

```
sudo -E pip install PyYAML
```

## bazel 

bazel not support lower case proxy setting

```
sudo -E HTTP_PROXY=$http_proxy  HTTPS_PROXY=$https_proxy bazel 
```

## FileMerge

opendiff **file1** **file2**

or for entire directories

opendiff **dir1** **dir2**

or 

/Developer/Applications/FileMerge.app/Contents/MacOS/FileMerge -left “File1” -right "File2" -ancestor "File3" -merge "File4"



## tcpkill

https://github.com/ggreer/dsniff

## CentOS yum 无法更新 

```
yum clean all
yum check
yum erase apf
yum upgrade
```

## Vbox CentOS instal Guest Addition

```
yum update
yum install gcc kernel-devel bzip2
mkdir -p /media/cdrom
mount /dev/scd0 /media/cdrom
sh /media/cdrom/VBoxLinuxAdditions.run
```

## Get Proxy Info

chrome: `chrome://net-internals/#proxy`
