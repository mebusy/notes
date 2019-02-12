# logrotate

## 1. 安装 logrotate （如果系统里不存在的话）

## 2.  配置文件 

主配置文件位于 /etc/logrotate.conf

你可以在 /etc/logrotate.d/ 目录内 添加自己的 日志文件切割(这些文件会被 /etc/logrotate.conf读入),如

```bash
#/etc/logrotate.d/ballsrace

/opt/ubisoft-minigame/app.log
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

## 4. 测试配置是否正确

```bash
/usr/sbin/logrotate -d -f /etc/logrotate.d/ballsrace
```

## 5. 手动强制切割日志

```bash
/usr/sbin/logrotate -f /etc/logrotate.d/ballsrace
```

## 6. 查看各log文件的具体执行情况

```bash
cat /var/lib/logrotate.status
```

## 7. crontab定时执行

```bash
# crontab -e
0 0 * * * /usr/sbin/logrotate -f /etc/logrotate.d/ballsrace &> /dev/null
```

maybe you want to use echo to append job to crontab file ...  you may find that file in `/etc/cron...`

```bash
echo $'*/1\t*\t*\t*\t*\t/usr/sbin/logrotate...' >> xxxx
```

## 8. Misc

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


### stdout/stderr 重定向日志问题

 - 类似 `app > log.log`
    - 这类日志文件， logrotate 的 truncate 不能生效，需要 使用追加的方式  `>>`
    - i.e. `app >> app.log 2>&1`



