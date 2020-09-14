...menustart

- [logrotate](#490162aae505a53f4f07a541323a1925)
    - [1. 安装 logrotate （如果系统里不存在的话）](#b0ae7ac024e9251b8352f7836d29b441)
    - [2.  配置文件](#d0992ebec741c858981a64a8ce11b040)
    - [4. 测试配置是否正确](#ddf5d7584457b4cb8c7993699bafe0bb)
    - [5. 手动强制切割日志](#3c6884f27d81600f244a367e1b74095d)
    - [6. 查看各log文件的具体执行情况](#9cfde9e4f062a301495ad160e63231a8)
    - [7. crontab定时执行](#236ff4d77e20107d290447c1bc082b5e)
    - [8. Misc](#6803e775fc8d5aa27d11c244367853e4)
        - [配置文件中一些指令说明](#3374665dc3e1eb7e8d997b73823475af)
        - [stdout/stderr 重定向日志问题](#6747f534f8d4ab733e26bd14238430ac)
        - [nginx 日志清理后， 日志不再生成的问题](#59ec735f1b20927d1572086d1ff12c40)
        - [centos 上切割nginx日志的例子](#f6b8fb64715407af569f56a897b2cbf4)

...menuend


<h2 id="490162aae505a53f4f07a541323a1925"></h2>


# logrotate

<h2 id="b0ae7ac024e9251b8352f7836d29b441"></h2>


## 1. 安装 logrotate （如果系统里不存在的话）

<h2 id="d0992ebec741c858981a64a8ce11b040"></h2>


## 2.  配置文件 

主配置文件位于 /etc/logrotate.conf

你可以在 /etc/logrotate.d/ 目录内 添加自己的 日志文件切割(这些文件会被 /etc/logrotate.conf读入),如

```bash
#/etc/logrotate.d/ballsrace

/opt/wc-minigame/app.log
{
    daily
    rotate 3
    missingok
    notifempty
    copytruncate 
    compress
    dateext
}
``` 

if your log file is not owner by root (say by user 'service'), then you should add extra line :

```
{
    su service service
    daily
```

<h2 id="ddf5d7584457b4cb8c7993699bafe0bb"></h2>


## 4. 测试配置是否正确

```bash
/usr/sbin/logrotate -d -f /etc/logrotate.d/ballsrace
```

<h2 id="3c6884f27d81600f244a367e1b74095d"></h2>


## 5. 手动强制切割日志

```bash
/usr/sbin/logrotate -f /etc/logrotate.d/ballsrace
```

<h2 id="9cfde9e4f062a301495ad160e63231a8"></h2>


## 6. 查看各log文件的具体执行情况

```bash
cat /var/lib/logrotate.status
```

- 如果有报错: error: Ignoring xxxx because it is writable by group or others
    - 这是因为你的 conf 文件没有设置正确的权限
    - `chmod 644  <you conf file> `

<h2 id="236ff4d77e20107d290447c1bc082b5e"></h2>


## 7. crontab定时执行


crontal job 文件可能位于：

```bash
/etc/crontab.
d/
daily/
hourly/
monthly/
weekly/
/var/spool/cron/<user>
```


```bash
# 列出当前 任务
# crontab -l


# 编辑 /var/spool/cron/root  文件, 
# crontab -e
0 0 * * * /usr/sbin/logrotate -f /etc/logrotate.d/ballsrace &> /dev/null
```

maybe you want to use echo to append job to crontab file 

(不同系统，可能文件位置不一样, apline: /etc/crontabs/root   ) 

```bash
echo $'*/1\t*\t*\t*\t*\t/usr/sbin/logrotate...' >> xxxx

# daily 00:00
echo $'0\t0\t*\t*\t*\t/usr/sbin/logrotate ...' >> xxx 
# daily 01:00
echo $'0\t1\t*\t*\t*\t/usr/sbin/logrotate ...' >> xxx 
```

```bash
# restart crond
systemctl restart crond
```


<h2 id="6803e775fc8d5aa27d11c244367853e4"></h2>


## 8. Misc

<h2 id="3374665dc3e1eb7e8d997b73823475af"></h2>


### 配置文件中一些指令说明

- compress                                   
    - 通过gzip 压缩转储以后的日志
- copytruncate                              
    - 用于还在打开中的日志文件，把当前日志备份并截断；是先拷贝再清空的方式，拷贝和清空之间有一个时间差，可能会丢失部分日志数据。
    - create选项此时被忽略
- missingok                                 
    - 如果日志丢失，不报错继续滚动下一个日志
- notifempty                               
    - 当日志文件为空时，不进行轮转
- dateext                                  
    - 使用当期日期作为命名格式
- sharedscripts                           
    - 运行postrotate脚本，作用是在所有日志都轮转后统一执行一次脚本。如果没有配置这个，那么每个日志轮转后都会执行一次脚本


<h2 id="6747f534f8d4ab733e26bd14238430ac"></h2>


### stdout/stderr 重定向日志问题

- 类似 `app &> log.log`
    - 这类日志文件， logrotate 的 truncate 不能生效，需要 使用追加的方式  `>>`
    - i.e. `app >> app.log 2>&1`


<h2 id="59ec735f1b20927d1572086d1ff12c40"></h2>


### nginx 日志清理后， 日志不再生成的问题

- 需要发送 USE1 信号给 nginx master 进程重新打开日志文件

```bash
$ kill -USR1 `ps axu | grep "nginx: master process" | grep -v grep | awk '{print $2}'`
```

- 更多的，是使用 `postrotate`

```bash
{
    ...

    sharedscripts
    postrotate
        [ -e /var/run/nginx.pid ] && kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
```

- `sharedscripts` The sharedscripts means that the postrotate script will only be run once (after the old logs have been compressed), not once for each log which is rotated.


<h2 id="f6b8fb64715407af569f56a897b2cbf4"></h2>


### centos 上切割nginx日志的例子

```bash
# setup.sh

APPNAME="hda"
CONF_FILE="${APPNAME}_logr.conf"

echo ... generate conf file: ${CONF_FILE}

cat > ${CONF_FILE}<<EOF
`pwd`/../logs/access.log
`pwd`/../logs/error.log
{
        daily
        rotate 5
    missingok
    notifempty
    copytruncate 
    compress
    dateext
}

EOF


echo ... copy conf to /etc/logrotate.d/
cp ${CONF_FILE} /etc/logrotate.d/${APPNAME}


echo .. add task 

if grep -q `pwd`"/hda_task.sh"  /var/spool/cron/root; then
    echo "task already exists"
else
    echo "add new task"
    # echo $'0\t0\t*\t*\t*\t/usr/sbin/logrotate -f /etc/logrotate.d/'${APPNAME}'  &> /dev/null' >> /var/spool/cron/root 
    echo $'0\t0\t*\t*\t*\t/usr/bin/sh '`pwd`"/hda_task.sh"'  &> /dev/null' >> /var/spool/cron/root 
fi

echo ... restart crond 

/bin/systemctl restart crond

echo ... end 
```

```
#!/bin/sh
# hda_task.sh
echo run hda logrotate

/usr/sbin/logrotate -f /etc/logrotate.d/hda
kill -USR1 `ps axu | grep "nginx: master process" | grep -v grep | awk '{print $2}'`
```


