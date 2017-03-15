...menustart

 - [Redis](#e111446745a1825b862f8727ae63bce4)
	 - [安装](#e655a410ff21cd07e7a0150491e04371)
	 - [配置](#224e2ccda861c2514faa683b3683c361)
	 - [启动](#8e54ddfe243a6ecd4e231c9cfa770bd4)
	 - [关闭](#b15d91274e9fc68608c609999e0413fa)
	 - [简介](#e05dce83e5129785b9f316978a14b896)
		 - [Redis支持的键值数据类型](#04be0f8060daa1d85d889605ca8fb2bb)
		 - [其他](#0d98c74797e49d00bcc4c17c9d557a2b)
		 - [多数据库](#fdde913b5f9231dbf0135b5d394cb199)
		 - [redis 命令，中文版](#7bcaab82241af99be9615017fca3cb89)
	 - [mac phpRedisAdmin](#6ef8082fd2f3d06391821ecff428e702)
	 - [Mac Resis](#5eb6909a1e0d0356a26e2c49bf854243)

...menuend


[TOC]

<h2 id="e111446745a1825b862f8727ae63bce4"></h2>
# Redis

<h2 id="e655a410ff21cd07e7a0150491e04371"></h2>
## 安装

 1. yum 安装
    - 安装第三方源
        - `wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm`
    - 安装epel
        - `rpm -ivh epel-release-6-8.noarch.rpm`
    - 安装 remi
        - `rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-6.rpm` 
    - 安装redis 
        - `yum --enablerepo=remi,remi-test install redis`

<h2 id="224e2ccda861c2514faa683b3683c361"></h2>
## 配置

 - `mkdir -p /data/app/redis/log`
 - `vi /etc/redis.conf`
    - redis 以后台进程运行
        - `daemonize yes`
    - 如果以后台程序运行，则需要制定一个PID
        - `pidfile /data/app/redis/redis.pid`
    - redis服务绑定的主机IP
        - `bind 192.168.1.249`
        - 使用***本机内网ip*** 替换 127.0.0.1, 以便局域网内的其他机器可以访问redis
    - 客户端连接超时时间，默认为300秒
        - `timeout 600`
    - 日志级别，分为debug,verbose(default),notice,waring
        - `loglevel notice`
    - 日志文件存放位置，默认为stdout
        - `logfile /data/app/redis/log/redis.log`
    - 保存策略
        - 900秒内至少有一个key被改变
            - `save 900 1`
        - 300秒内至少有十个key被改变
            - `save 300 10`
        - 60秒内只要有一万个key被改变
            - `save 60 10000`
        - PS. 注释掉这3个， 然后加上  save "" 就可以关闭持久化   
    - 本地数据库存放路径
        - `dir /data/app/redis/`
    - 客户端最大连接数，默认不限制
        - `maxclients 128` 
    - 是否使用虚拟内存，默认为no
        - `vm-enabled yes`
    - 最大内存
        - `maxmemory <bytes> `

<h2 id="8e54ddfe243a6ecd4e231c9cfa770bd4"></h2>
## 启动

```
redis-server /etc/redis.conf
/etc/init.d/redis start  # 可能需要修复logfile权限
```

<h2 id="b15d91274e9fc68608c609999e0413fa"></h2>
## 关闭

考虑到Redis 有可能正在将内存中的数据同步到硬盘中，正确停止 Redis 的方式应该是向 Redis 发送 SHUTDOWN 命令，方法为：

```
$ redis-cli SHUTDOWN
```

或  ？

```
/etc/init.d/redis stop
```


<h2 id="e05dce83e5129785b9f316978a14b896"></h2>
## 简介

<h2 id="04be0f8060daa1d85d889605ca8fb2bb"></h2>
### Redis支持的键值数据类型

- 字符串类型  string
- 散列类型     hash
- 列表类型     list
- 集合类型     set
- 有序集合类型   zset

<h2 id="0d98c74797e49d00bcc4c17c9d557a2b"></h2>
### 其他
数据类型不支持嵌套, hash, list 等集合类型，每个元素只能是字符串，不能是另一个集合或散列表 

数据持久化支持，异步写入

为每个键 设置生存时间 TTL， 键到期自动被删除。

还可以限定数据占用的最大内存空间，在数据达到空间限制后，可以按照一定规则自动淘汰不需要的键。

支持 发布／订阅的 消息模式，可以基于此构建 聊天室等。

<h2 id="fdde913b5f9231dbf0135b5d394cb199"></h2>
### 多数据库

多数据库 没什么卵用

redis 提供了多个用来存储数据的字典，客户端可以指定将数据存储在哪个字典中。每个数据库对外都是 以一个从0开的递增数字命名，Redis 默认支持16个数据库。

客户端与redis建立连接后会自动选择0号数据库，不过可以随时使用 SELECT 命令更换。

```
redis> SELECT 1
ok
reds [1]> GET foo
(nil)
```

<h2 id="7bcaab82241af99be9615017fca3cb89"></h2>
### redis 命令，中文版

http://www.redis.cn/commands.html

这些数据库 更像一种命名空间，不适合存储不同应用程序的数据。
            
<h2 id="6ef8082fd2f3d06391821ecff428e702"></h2>
## mac phpRedisAdmin

Mac 自带了 apache和php 模块, 所以使用 phpRedisAdmin 除了需要安装一个 phpRedis模块意外, 不需要安装其他东西了, 在本地稍微配置一下环境就可以的了.

 1. 安装 phpRedis 模块, 官方地址 [phpredis](https://github.com/nicolasff/phpredis)
    - 安装完了之后在安装目录下 modules 目录中有一个redis.so文件.
    - 如果提示缺少 autoconf :  `brew install autoconf`
    - 或者直接 brew 安装
        - `brew install homebrew/php/php55-redis`  (or php53-redis, php54-redis)
        - `php -version` 查看本机php版本

 2. 配置 apache 的 php 模块
    - 通过 finder 找到 `/etc/apache2/httpd.conf` 文件, 
    - 去掉 `#LoadModule php5_module libexec/apache2/libphp5.so` 前面的#号, 保存修改后的文件

 3. 配置 php 加载 redis 模块
    - 找到 /etc/php.ini ［.default ???］  文件, 添加 `extension=redis.so`

 4. 安装phpRedisAdmin 
    - 官网下载: [phpRedisAdmin](https://github.com/ErikDubbelboer/phpRedisAdmin/)
    - 解压, 配置 includes/config.sample.inc.php 
    - `cd phpRedisAdmin`
    - `git clone https://github.com/nrk/predis.git vendor`
    - 放在 apache 的应用目录下, 默认是 `/Library/WebServer/Documents/`

 5. 启动apache , 有两种启动方法
    - 1)  打开 系统设置偏好 -> 共享 -> Web共享 勾选即可
    - 2)  命令行 `sudo apachectl start`

 6. 启动本地的Redis
    - 访问localhost/你的安装目录 就可以了, 如果没有本地redis, 第一次访问可能会出错, 因为默认配置是连接本地 redis 6379 端口
    - 修改配置:  `phpRedisAdmin/includes/config.sample.inc.php`
 
 7. 如果是linux系统，注意开放 6379 端口

<h2 id="5eb6909a1e0d0356a26e2c49bf854243"></h2>
## Mac Resis

 - brew install redis
 - brew services start redis  #开机启动
 - 
 
    
