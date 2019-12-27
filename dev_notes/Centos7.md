...menustart

 - [Centos7](#8db8d64778c367a62ad2b609fd6c2095)
     - [mono](#654db8a14a5f633b9ba85ec92dc51f7c)
     - [firewall](#36e5371ad91c9d2d09e9d7c0e76055db)
     - [Mysql](#9edb3c572b56b91542af659480518681)
     - [查看 TIME_WAIT](#6dfa7a8202801ab86e07a577ba4da59f)
     - [TIME_WAIT 优化](#0d0306c1df74d541e32e7dcbaaf0fe69)
     - [文件描述符数](#1056f9281c64e7ce0c0ad739e5640797)
     - [TC 云服务器的 /etc/sysctl.conf 配置](#c5bfde7337a2b4013d953a5ef1e298f3)
     - [kill process by port](#48cd249a485752b67116301484bb3978)
     - [linux 系统监控](#65395697d2dab77dd22f054b888fb803)
     - [ab test](#107aedca6bab06cabee6aac093e48464)
     - [systemctl autorun script](#182779261a101fea13d68ad6ca885ef8)
         - [创建脚本](#cd25acb9fca49873079b8dc3ebc5021b)
         - [创建一个新的 systemd service unit](#fc37e2a196cecdc81fbdbe5a257b7652)
         - [Enable the systemd service unit](#4937eedceb267c9e4326ecf2ba78b05d)
         - [Example](#0a52730597fb4ffa01fc117d9e71e3a9)
     - [how the see the log of a running process which is redirected to `/dev/null` ?](#c6805678c62648e428cea464f3e8b4b7)
     - [Vbox Centos access Host folder](#69a3af8e4da356a41a5db362a321370e)
         - [1 create a share fold](#ced6fe808bc1654ffe62ac3e6b5888a4)
         - [2 Install Guest Additions](#9be07da516116f6994db2e276de42d2b)

...menuend


<h2 id="8db8d64778c367a62ad2b609fd6c2095"></h2>


# Centos7




<h2 id="654db8a14a5f633b9ba85ec92dc51f7c"></h2>


## mono

```bash
yum install yum-utils
rpm --import "http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
yum-config-manager --add-repo http://download.mono-project.com/repo/centos7/

yum -y install mono-complete  
# mono-core mono-devel ? I forgot the exact command ...
```

 - build c# project 

```bash
xbuild /p:Configuration=Release xxx.sln
```

<h2 id="36e5371ad91c9d2d09e9d7c0e76055db"></h2>


## firewall 

open a port :

```bash
# add ssh port as permanent opened port
firewall-cmd --zone=public --add-port=22/tcp --permanent
```


Then, you can reload rules to be sure that everything is ok

```bash
firewall-cmd --reload

firewall-cmd --zone=public --list-ports
```

remove a port

```bash
firewall-cmd --zone=public --remove-port=8091/tcp --permanent
```

option:  when you app launched , you can check whether the ports are correctly listening 

```bash
netstat -nltp
```

<h2 id="9edb3c572b56b91542af659480518681"></h2>


## Mysql

```
yum install mariadb-server mariadb  mariadb-devel

systemctl start mariadb  #启动MariaDB
systemctl stop mariadb  #停止MariaDB
systemctl restart mariadb  #重启MariaDB
systemctl enable mariadb  #设置开机启动
```

To make Mysql case sensitive,  find and modify `lower_case_table_names` to 1:

```
vi /etc/my.cnf

[mysqld]
lower_case_table_names=2
```

Delete anonymous user:

```
mysql> use mysql 
mysql> delete from user where user=''; 
mysql> FLUSH PRIVILEGES;
```

Create a database account, username and password is “kbe”:

```
mysql> grant all privileges on *.* to kbe@'%' identified by 'kbe';
mysql> grant select,insert,update,delete,create,drop on *.* to kbe@'%' identified by 'kbe';
mysql> FLUSH PRIVILEGES;
```


<h2 id="6dfa7a8202801ab86e07a577ba4da59f"></h2>


## 查看 TIME_WAIT

```
$ netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'
ESTABLISHED 20002
TIME_WAIT 1
```

<h2 id="0d0306c1df74d541e32e7dcbaaf0fe69"></h2>


## TIME_WAIT 优化

```
# vi /etc/sysctl.conf

net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1

# 然后执行 /sbin/sysctl -p 让参数生效。
```

<h2 id="1056f9281c64e7ce0c0ad739e5640797"></h2>


## 文件描述符数

 - 查看系统最大打开文件描述符数:

```
$ cat /proc/sys/fs/file-max
791606
```

 - 单个进程能打开的最大文件描述符数:

```
$ ulimit -n
200000
```

 - Centos7 修改 ulimit

```
$ vi /etc/security/limits.conf
 *    soft    nofile 200001
 *    hard    nofile 200002 
```

<h2 id="c5bfde7337a2b4013d953a5ef1e298f3"></h2>


## TC 云服务器的 /etc/sysctl.conf 配置

```
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).

# Controls IP packet forwarding
net.ipv4.ip_forward = 0

# Controls source route verification
net.ipv4.conf.default.rp_filter = 1

# Do not accept source routing
net.ipv4.conf.default.accept_source_route = 0

# Controls the System Request debugging functionality of the kernel

# Controls whether core dumps will append the PID to the core filename.
# Useful for debugging multi-threaded applications.
kernel.core_uses_pid = 1

# Controls the use of TCP syncookies
net.ipv4.tcp_syncookies = 1

# Controls the maximum size of a message, in bytes
kernel.msgmnb = 65536

# Controls the default maxmimum size of a mesage queue
kernel.msgmax = 65536

# disable ipv6 default
net.ipv6.conf.lo.disable_ipv6 = 1

net.ipv4.conf.all.promote_secondaries = 1
net.ipv4.conf.default.promote_secondaries = 1
net.ipv6.neigh.default.gc_thresh3 = 4096
net.ipv4.neigh.default.gc_thresh3 = 4096

kernel.softlockup_panic = 1
kernel.sysrq = 1
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
vm.overcommit_memory = 1
kernel.numa_balancing = 0
kernel.shmmax = 68719476736

# manually added...
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
```


<h2 id="48cd249a485752b67116301484bb3978"></h2>


## kill process by port 

```bash
kill $(lsof -t -i :PORTNUMBER)
```

<h2 id="65395697d2dab77dd22f054b888fb803"></h2>


## linux 系统监控

```
$ yum install -y dstat
$ dstat 
----total-cpu-usage---- -dsk/total- -net/total- ---paging-- ---system--
usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw 
  0   0 100   0   0   0|   0     0 | 431B  346B|   0     0 | 159   181 
  0   0 100   0   0   0|   0     0 | 371B  826B|   0     0 | 200   211 
```

 - To display information provided by vmstat,
    - Process stats
    - Memory stats

```
$ dstat --vmstat
```

 - to monitor a single program that is using the most CPU and consuming the most amount of memory.

```
$ dstat -c --top-cpu -dn --top-mem
```

 - you can also store the output of dstat in a .csv 
    - Here, we are displaying the time, cpu, mem, system load stats with a one second delay between 5 updates (counts).

```
$ dstat --time --cpu --mem --load --output report.csv 1 5
```


<h2 id="107aedca6bab06cabee6aac093e48464"></h2>


## ab test 

 - install ab

```
yum -y install httpd-tools 
```

 - ab test

```
$ echo "{ \"channel\": \"official\"}" > post.json
$ ab -k -n -r  500000 -c 20000 -T "application/json" -p post.json  -H "userID: debugUserID" -H "Authorization: 7eb0f0a9798af24a883f4859db88a634"  http://10.192.8.17:9000/announcement
```

 - also see [ab useage](workingTips.md)


<h2 id="182779261a101fea13d68ad6ca885ef8"></h2>


## systemctl autorun script 

 - 服务又分为系统服务（system）和用户服务（user）。
    - 系统服务：开机不登陆就能运行的程序（常用于开机自启）。
    - 用户服务：需要登陆以后才能运行的程序。
 - 配置文件目录
    - systemctl脚本目录：/usr/lib/systemd/ 
    - 系统服务目录：/usr/lib/systemd/system/ 
    - 用户服务目录：/usr/lib/systemd/system/


<h2 id="cd25acb9fca49873079b8dc3ebc5021b"></h2>


### 创建脚本

 - 1 写脚本 autorun.sh

```
!# vi autorun.sh 

#!/bin/bash
echo "This is a sample script to test auto run during boot" > ./script.out
echo "The time the script run was -->  `date`" >> ./script.out
```

 - 2 检查权限

```
# ls -lrt ./autorun.sh
-rw-r--r-- 1 root root 150 Sep  4 11:45 ./autorun.sh
```

 - 3 添加执行权限

```
# ls -lrt ./autorun.sh
-rwxr-xr-x 1 root root 150 Sep  4 11:45 ./autorun.sh
```

 - 注意： 因为是服务调用的脚本，如果脚本中有相对路径的使用，需要注意
    - 下面的代码可以得到 脚本所在的目录

```
#!/bin/bash
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
# echo $SCRIPTPATH
```

<h2 id="fc37e2a196cecdc81fbdbe5a257b7652"></h2>


### 创建一个新的 systemd service unit

```
!# vi /usr/lib/systemd/system/uwsgimind.service

[Unit]
Description=Description for sample script goes here
After=network.target

[Service]
# Type=forking  if app need run in background
Type=simple
ExecStart=/usr/bin/s /root/uwsgi_mind/autorun.sh
TimeoutStartSec=0

[Install]
WantedBy=default.target
```

<h2 id="4937eedceb267c9e4326ecf2ba78b05d"></h2>


### Enable the systemd service unit

```
# systemctl daemon-reload

# systemctl enable uwsgimind.service
Created symlink from /etc/systemd/system/default.target.wants/uwsgimind.service to /usr/lib/systemd/system/uwsgimind.service.

# systemctl start uwsgimind.service
```

 - reboot 测试

```
# systemctl reboot
```

 - 查看日志:

```
journalctl -e -f -u uwsgimind.service
```

 - e : start at end
 - f : follow  
 - u : unit 
 - `-e -f` 类似 `tail -f `

```bash
说明: 
重载系统服务：systemctl daemon-reload 
设置开机启动：systemctl enable *.service 
启动服务：systemctl start *.service 
停止服务：systemctl stop *.service 
重启服务：systemctl reload *.service
重启服务：systemctl restart *.service
```


<h2 id="0a52730597fb4ffa01fc117d9e71e3a9"></h2>


### Example 

 - uwsgi 自带的 uwsgi.service

```bash
[Unit]
Description=uWSGI Emperor Service
After=syslog.target

[Service]
EnvironmentFile=-/etc/sysconfig/uwsgi
ExecStartPre=/bin/mkdir -p /run/uwsgi
ExecStartPre=/bin/chown uwsgi:uwsgi /run/uwsgi
ExecStart=/usr/sbin/uwsgi --ini /root/uwsgi_mind/uwsgi.ini
ExecReload=/bin/kill -HUP $MAINPID
KillSignal=SIGINT
Restart=always
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

 - 自定义的一个service

```
[Unit]
Description=uWSGI for mind
After=syslog.target

[Service]
Type=forking

ExecStart=/usr/bin/sh /root/uwsgi_mind/autorun.sh
KillSignal=SIGINT  # for systemctl restart
Restart=always
TimeoutStartSec=0

[Install]
WantedBy=default.target
~
```


<h2 id="c6805678c62648e428cea464f3e8b4b7"></h2>


## how the see the log of a running process which is redirected to `/dev/null` ?

 - `tail -f /proc/<pid>/fd/1`
    - where 
    - 1 = stdout, 2 = stderr

<h2 id="69a3af8e4da356a41a5db362a321370e"></h2>


## Vbox Centos access Host folder

<h2 id="ced6fe808bc1654ffe62ac3e6b5888a4"></h2>


### 1 create a share fold

- in vbox menu,  create a shared folder 
   - choose `auto mount` and "permanent"
   - remember the shared name , i.e. "D_DRIVER"

<h2 id="9be07da516116f6994db2e276de42d2b"></h2>


### 2 Install Guest Additions

- 1. from Centos Vbox menu `Devices` , choose `Insert Guest Additions CD Image`
- 2. in centos shell

```
$ mkdir -p /media/cdrom
$ mount /dev/cdrom /media/cdrom/
$ cd /media/cdrom/
$ sh VBoxLinuxAdditions.run
...
VirtualBox Guest Additions: Starting.
```

Now, the shared fold has be mounted at `/media/sf_D_DRIVE/`. (if not , try reboot)



