[](...menustart)

- [MacOSX](#5dad7f6f2d7af4cc1196128ec251af8a)
    - [sidebar 丢失](#2921868f08055ef268441139489a6130)
    - [Useful Commands](#ec69fb46be4996fda376dcb4054c528b)
        - [bash64 decode to hex](#9ce547db2f9c1a445bc410d99d7ac737)
        - [xxd](#25c04b9b782789c092a38c06cc87632a)
        - [mdfind(deprecated)](#8fa27b7030fcdda4e88c6240caf99bf1)
        - [man ascii  字符表](#726e07a4bf9abb9ebcdce89b16eb7807)
        - [cal 日历](#e1bde9f80b42328020cb6b0a4c7d26ab)
    - [打开文件数 / 最大链接数](#c635de9cfd3f586235866c25b1208360)
    - [性能测试](#ddd22119a924356d5fd97057285c0689)
    - [内网传输速度测试](#d8f5e5c499ab6b35afcd8cfed2906d9d)
    - [传输速度测试方案2: speedtest](#87c5409b5cb0632cb1d44f17c36c7d83)
    - [launchd (Ventura)](#1140697b7cb93fa5d169b584735051c3)
        - [Create a Mac plist file to describe your job](#00379fb669143aee93f220a535b222a5)
        - [set permission](#9fc04cfc1a7d7e7505e7417dddf947c8)
        - [load and test it](#548797edc19fa3483f6f9a6f36faa5e2)
    - [check SSD lifespan](#fb8aa0d64bf13765b2377276fc9e9ed7)
    - [screen capture to clipborad](#49d6e205c8881024108f1681926717a8)
    - [copy wifi password to clipboard](#6831a70b0b58947b7c63e20394b71a09)

[](...menuend)


<h2 id="5dad7f6f2d7af4cc1196128ec251af8a"></h2>

# MacOSX 


<h2 id="ec69fb46be4996fda376dcb4054c528b"></h2>

## Useful Commands


<h2 id="9ce547db2f9c1a445bc410d99d7ac737"></h2>

### bash64 decode to hex

```bash
$ echo -n 'R1BSVwI=' | base64 -D | hexdump -v -e '/1 "%02x" '
4750525702
```

<h2 id="25c04b9b782789c092a38c06cc87632a"></h2>

### xxd 

- `xxd  <filename>`   以16进制显示文件内容
- `xxd -i <filename>`   转成c数组

```c++
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

<h2 id="8fa27b7030fcdda4e88c6240caf99bf1"></h2>

### mdfind(deprecated)

[mdfind](https://raw.githubusercontent.com/mebusy/notes/master/dev_notes/mdfind.md)



<h2 id="726e07a4bf9abb9ebcdce89b16eb7807"></h2>

### man ascii  字符表

```bash
$ man ascii

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



<h2 id="c635de9cfd3f586235866c25b1208360"></h2>

## 打开文件数 / 最大链接数

```bash
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
# memory speed
$ dd if=/dev/zero of=/dev/null bs=1m count=32768
32768+0 records in
32768+0 records out
34359738368 bytes transferred in 0.988451 secs (34761195414 bytes/sec)

# explain
# Memory Bandwidth (GB/s)=Memory Clock Frequency (MHz)×Bus Width (bytes)×Transfers per Clock Cycle×10 −3
# for example, 2667MHz, 8bytes, 2 transfers per clock cycle
# Memory Bandwidth(GB/s) = 2667 * 8 * 2 * 10^-3 = 42.672GB/s # 理论内存带宽
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


<h2 id="1140697b7cb93fa5d169b584735051c3"></h2>

## launchd (Ventura)

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
  <string>com.user.launchVM</string>

  <key>ProgramArguments</key>
  <array>
    <string>/Volumes/WORK/VBoxVDIs/openwrt/launchVM.sh</string>
  </array>

  <key>Nice</key>
  <integer>1</integer>

  <key>StartInterval</key>
  <integer>60</integer>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardErrorPath</key>
  <string>/Volumes/WORK/VBoxVDIs/openwrt/err.log</string>

  <key>StandardOutPath</key>
  <string>/dev/null</string>
</dict>
</plist>
```

trouble shooting

```bash
# list
VBoxManage list runningvms
# stop vm
VBoxManage controlvm openwrt poweroff
# unlock session
vboxmanage startvm openwrt --type emergencystop

# restart
sh /Volumes/WORK/VBoxVDIs/openwrt/launchVM.sh
```


<h2 id="9fc04cfc1a7d7e7505e7417dddf947c8"></h2>

### set permission

```bash
cp ./launchVM.plist ~/Library/LaunchAgents/ 
cd ~/Library/LaunchAgents/
sudo chown root ./launchVM.plist
sudo chgrp wheel ./launchVM.plist
```



<h2 id="548797edc19fa3483f6f9a6f36faa5e2"></h2>

### load and test it

```bash
sudo launchctl bootstrap system  ~/Library/LaunchAgents/launchVM.plist
```

or just test whether it works:

```bash
launchctl load ~/Library/LaunchAgents/launchVM.plist
```


<h2 id="fb8aa0d64bf13765b2377276fc9e9ed7"></h2>

## check SSD lifespan

```bash
brew install smartmontools
smartctl -a /dev/disk0

# you may need do some test on disk
smartctl -t short /dev/disk0
```


<h2 id="49d6e205c8881024108f1681926717a8"></h2>

## screen capture to clipborad

cmd +  ctl + shift + 4

## screen video capture

cmd +  ctl + shift + 5



<h2 id="6831a70b0b58947b7c63e20394b71a09"></h2>

## copy wifi password to clipboard

```bash
$ security find-generic-password -wa "ChinaNet-Mebusy" |  pbcopy
```

## open finder where specific file exists

```bash
open -R <path-to-file>
```

## Easily Find Forgotten Commands from History (bck-i-search)

1. Open up Terminal.
2. Type `Ctrl-r`.
3. type letters you remember...
4. As you type, the terminal keeps suggesting a command that matches what you’ve typed. 


## software update issue

### 1. software update stuck on restarting...

```bash
softwareupdate -l : to see a list of the current updates (to make sure I was updating the same things)
sudo softwareupdate -i -a -R : to install the updates, and restart the computer if required
```

### 2. install specific MacOSX version

```bash
softwareupdate  --list-full-installers
sudo softwareupdate --fetch-full-installer --full-installer-version 14.7.2
```

