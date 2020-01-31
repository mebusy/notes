...menustart

 - [MacOSX](#5dad7f6f2d7af4cc1196128ec251af8a)
     - [sidebar 丢失](#2921868f08055ef268441139489a6130)
     - [openofficer error](#1c305ad1fad7ba14dd448d08a73f3ab8)
     - [Useful Commands](#ec69fb46be4996fda376dcb4054c528b)
         - [xxd](#25c04b9b782789c092a38c06cc87632a)
         - [mdfind](#0968ea4dc36ecbcdc0810a8ca0f674c8)
         - [man ascii  字符表](#726e07a4bf9abb9ebcdce89b16eb7807)
         - [cal 日历](#e1bde9f80b42328020cb6b0a4c7d26ab)
         - [find files to rm](#a21d96fb754b9ce8455858e14ed36571)
         - [in terminal, show git branch in path](#394dd2658e932bd638e3017ac1a98c39)
         - [find all json file , and remove all `\r`](#75aeaa38d609e022daed8f30150edfa7)
         - [find pattern in specific file types](#b5a637298d7d74567762e4ce9127bd5e)
         - [bash  wait previous command to finish](#639aab73c8776e2711502bd23e7dd4de)
         - [sed 使用](#ccbf87c494cf62aca0164aa04719e15f)
     - [打开文件数 / 最大链接数](#c635de9cfd3f586235866c25b1208360)
     - [性能测试](#ddd22119a924356d5fd97057285c0689)
     - [内网传输速度测试](#d8f5e5c499ab6b35afcd8cfed2906d9d)
     - [传输速度测试方案2: speedtest](#87c5409b5cb0632cb1d44f17c36c7d83)
     - [launchd](#f488c026a96a1c56683f3f6afb629010)
         - [Create a Mac plist file to describe your job](#00379fb669143aee93f220a535b222a5)
         - [load and test it](#548797edc19fa3483f6f9a6f36faa5e2)
         - [An important note about root and sudo access](#cfdb23d5d79b7e7d55330583c081e20c)

...menuend


<h2 id="5dad7f6f2d7af4cc1196128ec251af8a"></h2>


# MacOSX 


<h2 id="2921868f08055ef268441139489a6130"></h2>


## sidebar 丢失

OPTION/Alt+COMMAND+S

<h2 id="1c305ad1fad7ba14dd448d08a73f3ab8"></h2>


## openofficer error

```bash
rm -rf ~/Library/Saved Application State/org.openoffice.script.savedState
```

<h2 id="ec69fb46be4996fda376dcb4054c528b"></h2>


## Useful Commands

<h2 id="25c04b9b782789c092a38c06cc87632a"></h2>


### xxd 

 - `xxd  <filename>`   以16进制显示文件内容
 - `xxd -i <filename>`   转成c数组

```
unsigned char note_txt[] = {
  0x0a, 0x0a, 0x0a, 0x35, 0x30, 0x30, 0x30, 0x20, 0x2b, 0x20, 0x37, 0x35,
  0x30, 0x20, 0x70, 0x68, 0x6f, 0x74, 0x6f, 0x0a, 0x31, 0x32, 0x30, 0x20,
  0x20, 0xe5, 0x96, 0x9c, 0xe7, 0xb3, 0x96, 0xe9, 0xa2, 0x84, 0xe4, 0xbb,
  0x98, 0x0a, 0x35, 0x30, 0x30, 0x30, 0x20, 0xe5, 0xb0, 0x8f, 0xe5, 0x8d,
  0x97, 0xe5, 0x9b, 0xbd, 0x20, 0xe5, 0xae, 0x9a, 0xe9, 0x87, 0x91, 0x0a,
  0x0a
};
unsigned int note_txt_len = 61;
```

<h2 id="0968ea4dc36ecbcdc0810a8ca0f674c8"></h2>


### mdfind

[mdfind](https://raw.githubusercontent.com/mebusy/notes/master/dev_notes/mdfind.md)



<h2 id="726e07a4bf9abb9ebcdce89b16eb7807"></h2>


### man ascii  字符表

```
 The hexadecimal set:

 00 nul   01 soh   02 stx   03 etx   04 eot   05 enq   06 ack   07 bel
 08 bs    09 ht    0a nl    0b vt    0c np    0d cr    0e so    0f si
 ...
```

<h2 id="e1bde9f80b42328020cb6b0a4c7d26ab"></h2>


### cal 日历

 - `cal` 当月
 - `cal -y` 当年
 - `-j` 参数, day 显示为 当年的第几天


<h2 id="a21d96fb754b9ce8455858e14ed36571"></h2>


### find files to rm 

```
find . -name '.DS_Store' -path '*/.*' | xargs  rm
```

<h2 id="394dd2658e932bd638e3017ac1a98c39"></h2>


### in terminal, show git branch in path

```
# Git branch in prompt.
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
```

<h2 id="75aeaa38d609e022daed8f30150edfa7"></h2>


### find all json file , and remove all `\r` 

```bash
ls *.json | xargs -I {}  sh -c  "cat {} | tr -d '\r' > {}2 && mv {}2 {} "
or
ls *.json | xargs -I {}  sh -c  " tr -d '\r' < {}  > {}2 && mv {}2 {} "
```
 
  - `{}` :  handle every file , and to prevent path with space
  - `sh -c`  : directly use `{}` in redirection `>` not works, put them in a shell command
  - you can not do that by sed  , remember  sed delimits on `\n` newlines - they are always removed on input and reinserted on output.   you may need `-z` mode 
 

<h2 id="b5a637298d7d74567762e4ce9127bd5e"></h2>


### find pattern in specific file types 

```bash
find . -type f -name '*.cpp' -o -name '*.h' -o -name '*.as'  | xargs -I {} grep  -m 1  ReturnToMap "{}" /dev/null
```

 - `*.ext1` -o `*.ext2` 
 - `/dev/null` is to show the file path
 - ` -m 1`  stop when 1st matching

use mdfind ...

```bash
mdfind -onlyin . "kMDItemDisplayName == *.as || kMDItemDisplayName == *.cpp || kMDItemDisplayName == *.h"  | xargs -I {} grep  -m 1  ReturnToMap "{}" /dev/null
```

最高效的方式

```bash
grep -r --include \*.h --include \*.cpp --include \*.as ReturnToMap  .
```

 - ` -m 1` will not works as expect in `-r` mode

 - or more clean 

```bash
grep -r --include=*.{h,cpp,as}  ReturnToMap  .
```

 - add `-w ` if you want matching the whole word 


<h2 id="639aab73c8776e2711502bd23e7dd4de"></h2>


### bash  wait previous command to finish 

```bash
#！/bin/sh
echo “1”
sleep 5&
echo “3”
echo “4”
wait  #会等待wait所在bash上的所有子进程的执行结束，本例中就是sleep 5这句
echo”5”
```


<h2 id="ccbf87c494cf62aca0164aa04719e15f"></h2>


### sed 使用

 1. sed语句中如果要引用变量， 使用 双括号 `" "` ， 不要使用 单括号 `' '` 
 2. 查找/替换中 匹配 white space
    - 使用  `[[:space:]]` , 而不是 `\s`
    - 没有 `+` 的用法

<h2 id="c635de9cfd3f586235866c25b1208360"></h2>


## 打开文件数 / 最大链接数

```
launchctl limit
sudo launchctl limit maxfiles 100000 500000

sysctl kern.maxfiles
sysctl -w kern.maxfiles=20480 (or whatever number you choose)

# will lost , for centos : /etc/security/limits.conf
ulimit -a
ulimit -n 8192
```

<h2 id="ddd22119a924356d5fd97057285c0689"></h2>


## 性能测试

```bash
# cpu performance
python -c 'import test.pystone;print test.pystone.pystones()'

# memory speed
dd if=/dev/zero of=/dev/null bs=1m count=32768
```

<h2 id="d8f5e5c499ab6b35afcd8cfed2906d9d"></h2>


## 内网传输速度测试

1台机器上 开启 iperf3 server

```bash
iperf3 -s
```

另一台机器上 发包测试

```bash
iperf3 -c 192.168.1.8 -R
```

<h2 id="87c5409b5cb0632cb1d44f17c36c7d83"></h2>


## 传输速度测试方案2: speedtest

```bash
docker run -d --name speedtest -p 0.0.0.0:81:80 adolfintel/speedtest:latest

webpage
http://10.192.89.89:81/
```


<h2 id="f488c026a96a1c56683f3f6afb629010"></h2>


## launchd

About crond : *"“The cron utility is launched by launchd(8) when it sees the existence of /etc/crontab or files in /usr/lib/cron/tabs. There should be no need to start it manually.”"*

There are three main directories you can use with launchd:

1. /Library/LaunchDaemons
    - job needs to run even when no users are logged in.
2. /Library/LaunchAgents
    - if the job is only useful when users are logged in.
    - I learned that this has the side-effect of your job being run as 'root' after a system reboot.)
3. $HOME/Library/LaunchAgents
    - your job will be run under your username.

<h2 id="00379fb669143aee93f220a535b222a5"></h2>


### Create a Mac plist file to describe your job

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.alvin.crontabtest</string>

  <key>ProgramArguments</key>
  <array>
    <string>/Users/al/bin/crontab-test.sh</string>
  </array>

  <key>Nice</key>
  <integer>1</integer>

  <key>StartInterval</key>
  <integer>60</integer>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardErrorPath</key>
  <string>/tmp/AlTest1.err</string>

  <key>StandardOutPath</key>
  <string>/dev/null</string>
</dict>
</plist>
```

<h2 id="548797edc19fa3483f6f9a6f36faa5e2"></h2>


### load and test it

```bash
launchctl load <path>/com.alvin.crontabtest.plist
```

To turned it off 

```bash
launchctl unload <path>/com.alvin.crontabtest.plist
```

<h2 id="cfdb23d5d79b7e7d55330583c081e20c"></h2>


### An important note about root and sudo access

If you placed your Mac plist file in one of the two system directories (/Library/LaunchDaemons, /Library/LaunchAgents), your job will be running as the root user after a system reboot. This means a couple of things:

1. First, output files created by your script will be owned by the root user.
2. Second, you'll need to use sudo before any of your launchctl commands, as shown here:
















