...menustart

- [第二部分 单机数据库的实现](#8c1b6e8cf0ad7a4cb490dfaf66ca68b1)
- [第九章 数据库](#0fdaaffeed5bec2c5a52ff593df3e097)
    - [9.1 服务器中的数据库](#7584e17b45e6c724bdb205b4328b2a2a)
    - [9.2 切换数据库](#e65a474b2e07da4193fef099a9a5a884)
    - [9.3 数据库 key space](#85abf6d07f1ea7699a3399d4e7e88f07)
        - [9.3.6 读写 key space的维护操作](#aa52916caf96e748e410c04b818e546c)
    - [9.4 设置key的生存时间 或过期时间](#7dce0e3b39e2e4ca93fc1a155e2c9e92)
        - [9.4.1 设置过期时间](#696e7890096cb2fc3d766e6f04e10201)
        - [9.4.2 保存过期时间](#426142964ca65afd9b5390c08b027fa3)
        - [9.4.3 移除过期时间](#e77fe4d6808fa5c257e38c9b32944cb1)
    - [9.6 Redis 过期key的删除策略](#1f6aeaa86a387c1d445ee12955f2649a)
    - [9.7 AOF, RDB 和 复制功能 对过期键的处理](#250cd9b1dcb13e043cf3f3934f8bf1de)
        - [9.7.1 生成 RDB 文件](#2920a1d3c264f8880965a9cee2db82ae)
        - [9.7.2 载入 RDB文件](#cdbd82391cc0c8b1bbfc5c10292f1ce8)
        - [9.7.3 AOF 文件写入](#0d763e69eb6aac7370b8d671219e087b)
        - [9.7.4 AOF 重写](#74d7b9b793407a282fc437855b567ae9)
        - [9.7.5 复制](#cfec5987bd5114458541d6c47542a094)
    - [9.8 数据库通知](#9f3ab26a95d047bbdde34ac48aa1c22e)
- [第十章  RDB 持久化](#b43b08792e45d2626f267c7fa32ea1e2)
    - [10.1 RDB文件的创建和载入](#e4fdb7f64e0c078977e296c8204fcfa0)
    - [10.1.2 BGSAVE命令执行是的服务器状态](#899193c751be1a257794d0c55add6a1c)
    - [10.2 自动间隔性保存](#f7309047e97f6fd59cae1751c9ecc9ac)
- [第11章  AOF持久化](#6379208e54e6df4bd7230e05f1ddcd9c)
    - [11.1 AOF持久化的实现](#6d04df896b36247259132fb82b148101)
    - [11.3 AOF重写](#bf09e9a5e2c2f7fa63e2e63ce9d85424)
- [第14章 服务器](#aa0a9a66d75378fa51e47a76e278790f)
    - [14.2 serverCron 函数](#01212d817ddb139f1bb2895bb825ac34)
        - [14.2.1 更新服务器时间缓存](#105e46bac70d6bacbf39e68329c7462c)
- [第三部分 多级数据库的实现](#105b9f5eb4cd097b8d05a0689fbc6cee)
- [第15章 复制](#1083f1f72ccba95cb67916bfb993be58)
- [第16章 Sentinel](#3622aa17f59dc29d9f444a1fa691b762)
    - [16.1 启动并初始化 Sentinel](#1729d027ffc4c25f8f95d8c6ae87439b)
        - [16.1.1 初始化服务器](#8e86642cb4ff7a5603b4519b811c97d5)
        - [16.1.2 使用 Sentinel 专用代码](#0980835f438dc23319a78f9c9f1e2911)
        - [16.1.3 初始化 Sentinel 状态](#8a7bbadb30e40fd09043360410456aca)
        - [16.1.4 初始化 Sentinel 状态的 master属性](#5c1205ac880316d36c321416d35d59b4)
        - [16.1.5 创建连向主服务器的网络链接](#8841ef9a85d2bb92800b807f68b9aa90)
    - [16.2 获取主服务器信息](#107d9ebc3593fc7492de4218da5f40fc)
    - [TODO](#b7b1e314614cf326c6e2b6eba1540682)
- [第17章 集群](#53276068e0f0db9687713c65e75a141d)
    - [TODO](#b7b1e314614cf326c6e2b6eba1540682)

...menuend


<h2 id="8c1b6e8cf0ad7a4cb490dfaf66ca68b1"></h2>


# 第二部分 单机数据库的实现

---

<h2 id="0fdaaffeed5bec2c5a52ff593df3e097"></h2>


# 第九章 数据库

<h2 id="7584e17b45e6c724bdb205b4328b2a2a"></h2>


## 9.1 服务器中的数据库

 - Redis 服务器将 所有的数据库都保存在 服务器状态 `redis.h/redisServer` 结构的 db数组中
 - db数组的每一项 都是一个 redis.h/redisDb 结构， 每个 redisDb 结构代表一个数据库：

```
struct redisServer {
    // ...
    redisDb *db;
    // ... 
    int dbnum;
    // ...
} ;
```

 - 在初始化服务器时， 程序会根据服务器状态的 dbnum 属性来决定应该 创建多少个数据库
 - dbnum 属性的值， 由服务器配置的 database 选项决定， 默认16，所以redis服务器会默认创建16个数据库。


<h2 id="e65a474b2e07da4193fef099a9a5a884"></h2>


## 9.2 切换数据库

 - 每个Redis客户端都有自己的目标数据库， 每当客户端执行数据库 读写命令时，目标数据库就会成为这些命令的操作对象
 - 默认情况下， Redis客户端的目标数据库为0号数据库， 客户端可以通过 执行 SELECT命令来切换目标数据库。

```
redis:6379> SELECT 2
OK
redis:6379[2]>
```

 - 在服务器内部，客户端状态 redisClient 结构的 db属性纪录了客户端当前的目标数据库

```c
typedef struct redisClient {
    // ,,,
    redisDb *db ;
    // ...
} redisClient ;
```

 - redisClient.db 指向 redisServer.db 数组中的其中一个元素。


<h2 id="85abf6d07f1ea7699a3399d4e7e88f07"></h2>


## 9.3 数据库 key space

 - `redis.h/redisDb` 结构中的 dict 字典保存了 这个 redisDb 中 所有的 key-value pair, 我们将这个字典成为 key space.

```c
typedef struct redisDb {
    // ...
    dict *dict ;
    // ...
} redisDb ;
```


<h2 id="aa52916caf96e748e410c04b818e546c"></h2>


### 9.3.6 读写 key space的维护操作

 - 当使用redis 命令对数据进行读写时， 服务器不仅会对 key space 执行特定的读写操作， 还会执行一些额外的维护操作：
    - 在读取一个key后 (读写操作都要对key进行读取)， 服务器会根据key是否存在来更新服务器的key space 命中次数，或不命中次数，
        - 这两个值 可以在 INFO stats 命令的 keyspace_hits 属性 和 keyspace_misses 属性中查看
    - 在读取一个key后， 服务器会更新 key的 LRU时间
    - 如果服务器在读取一个key时发现该key已经过期，那么服务器会先删除这个过期键，然后再执行余下的其他操作。 
    - 如果由客户端使用 WATCH 命令监视了某个key， 那么服务器在对被监视的key进行修改之后， 会讲这个key 标记为 dirty，从而让事务程序注意到 这个key已经被修改过。
    - 服务器每次修改一个key之后， 都会对 dirty key 计数器的值增加1， 这个计数器会触发服务器的持久化以及复制操作。
    - 如果服务器开启了 数据库通知功能， 那么在对key进行修改后，服务器将按配置发送相应的数据库通知。


<h2 id="7dce0e3b39e2e4ca93fc1a155e2c9e92"></h2>


## 9.4 设置key的生存时间 或过期时间

 - 通过 EXPIRE 命令 或 PEXPIRE 命令， 客户端可以 以秒或者毫秒 精度为数据库中的某个可以设置生存时间(Time To Live , TTL) , 在经过指定的秒数或毫秒数之后，服务器就会自动删除生存时间为0的key
 - 类似的， 客户端还可以通过 EXPIREAT 或 PEXPIREAT 命令， 给数据库中的某个key 设置过期时间(expire time)
    - 过期时间一个UNIX时间戳，当key的过期时间来临时，服务器就会自动从数据库中删除这个key
 - TTL 命令和 PTTL 命令接受一个带有 生存时间或过期时间的key， 返回这个key的剩余生存时间


```
redis:6379> EXPIREAT A 1534996296
(integer) 1
redis:6379> TIME
1) "1533996332"
2) "132872"
redis:6379> TIME
1) "1533996335"
2) "647747"
redis:6379> TTL A
(integer) 999930
``` 


<h2 id="696e7890096cb2fc3d766e6f04e10201"></h2>


### 9.4.1 设置过期时间

 - `EXPIRE <key> <ttl>`
 - `PEXPIRE <key> <ttl>`
 - `EXPIREAT <key> <timestamp>`
 - `PEXPIREAT <key> <timestamp>`


<h2 id="426142964ca65afd9b5390c08b027fa3"></h2>


### 9.4.2 保存过期时间

 - redisDb 结构的 `dict *expires;` 字典 保存了 数据库中所有key的过期时间
    - 过期字典的key是一个指针， 这个指针指向 key space 中的某个key对象，也即是某个数据库key
    - 过期字典的value是一个 long long类型的整数，这个整数保存了 过期时间 -- 一个毫秒精度的 UNIX时间戳。


<h2 id="e77fe4d6808fa5c257e38c9b32944cb1"></h2>


### 9.4.3 移除过期时间

 - PERSISI 命令可以 移除一个key的过期时间，


```
redis:6379> PERSIST A
(integer) 1
redis:6379> TTL A
(integer) -1
```


<h2 id="1f6aeaa86a387c1d445ee12955f2649a"></h2>


## 9.6 Redis 过期key的删除策略

 - 惰性删除(访问key的时候 才进行过期检查) ，和 定期删除（每隔一定时间执行一次删除过期操作)


<h2 id="250cd9b1dcb13e043cf3f3934f8bf1de"></h2>


## 9.7 AOF, RDB 和 复制功能 对过期键的处理

<h2 id="2920a1d3c264f8880965a9cee2db82ae"></h2>


### 9.7.1 生成 RDB 文件

 - 执行 SAVE 或 BGSAVE 命令创建一个新的 RDB文件时， 程序会对数据库中的key进行检查，已过期的key 不会被保存到新创建的 RDB 文件中。

<h2 id="cdbd82391cc0c8b1bbfc5c10292f1ce8"></h2>


### 9.7.2 载入 RDB文件

 - 在启动Redis服务器时，如果服务器开启了 RDB 功能，那么服务器将对 RDB 文件进行载入
    - 如果服务器以master模式运行， 那么在 载入RDB文件时，程序会对文件中保存的key进行检查，未过期的键会被载入到数据库中， 而过期的键则会被忽略。
    - 如果服务器以 slaver 模式运行，key无路是否过期，都会被载入到数据库总。 因为主从服务器在进行数据同步的时候， 这些过期key 就会被清空，所以不会造成影响。


<h2 id="0d763e69eb6aac7370b8d671219e087b"></h2>


### 9.7.3 AOF 文件写入

 - 当服务器以 AOF 持久化模式运行时， 如果数据库中的某个key已经过期， 但它还没有被删除， 那么AOF 文件不会因为这个 过期key 而产生任何影响。
 - 但过期key 被惰性删除 或者 定期删除之后， 程序会向AOF 文件 append 一条 DEL 命令，来显示地记录该key已经被删除。
 - example：`GET message` 访问已过期的 message ， 服务器将执行以下三个动作
    1. 从数据库中 删除message key
    2. 追加一条 DEL message 命令到AOF 文件
    3. 向执行 GET命令的客户端 返回nil


<h2 id="74d7b9b793407a282fc437855b567ae9"></h2>


### 9.7.4 AOF 重写

 - 和生成 RDB 文件时类似， 在执行AOF重写的过程中， 程序会对数据库中的key进行检查，已过期的key不会被保存到重写后的AOF 文件中。


<h2 id="cfec5987bd5114458541d6c47542a094"></h2>


### 9.7.5 复制
 
 - 当服务器运行在 复制模式下， 从服务器的过期键删除动作由主服务器控制：
    - 主服务器在删除一个过期键之后， 会显示地向所有从服务器发送一个 DEL命令，告知从服务器删除这个过期键
    - 从服务器在执行客户端发送的读命令时， 即使碰到过期键也不会将过期键删除，而是继续像处理未过期键一样处理
    - 从服务器只有在 接到主服务器发来的DEL命令之后，才会删除过期键

 - example， 有一对主从服务器， 它们数据库中保存了 过期的key `message`
    - 如果这时 有客户端向从服务器 发送命令 GET message ， 那么从服务器 将发现 message 已经过期， 但从服务器并不会删除 message， 而是继续讲 message的值 返回给客户端， 就好像 message 没有过期。
    - 假设在此之后， 有客户端向 主服务器 发送 GET message， 那么主服务器将发现 message已经过期，主服务器会删除message， 向客户端返回 nil， 并向从服务器发送 DEL message 命令。
        - 从服务器在接收到 服务器发来的 DEL message 命令后，也会从数据库中删除 message.


<h2 id="9f3ab26a95d047bbdde34ac48aa1c22e"></h2>


## 9.8 数据库通知

 - 数据库通知四 Redis 2.8 新增功能


```
// key-space notification
redis:6379> SUBSCRIBE __keyspace@0__:message
...

// key-event nofitication
redis:6379> SUBSCRIBE __keyspace@0__:del
```

 - 服务端配置的 notify-keyspace-events 选项决定了 服务器所发送通知的类型
    - 发送所有 通知  ， 可将选项的值设置为 AKE
    - all key-space notification ,  -- AK
    - only string key-space notification , -- K$
    - only list key-event notification , -- El
    - see official docs for more details 


<h2 id="b43b08792e45d2626f267c7fa32ea1e2"></h2>


# 第十章  RDB 持久化

 - RDB持久化既可以手动执行，也可以根据服务器配置 定期执行， 将数据库状态保存到一个 RDB文件中
 - RDB文件是一个经过压缩的二进制文件

<h2 id="e4fdb7f64e0c078977e296c8204fcfa0"></h2>


## 10.1 RDB文件的创建和载入

 - 两个命令可以生成 RDB文件
    - SAVE , 阻塞服务器进程
    - BGSAVE ， fork一个子进程， 服务器进程继续处理命令
 - RDB文件的载入工作是在 服务器启动时 自动执行的，没有专门的命令
 - 另外， 因为AOF文件的更新频率通过比RDB文件的更新频率高，所以：
    - 如果服务器开启了AOF ， 那么服务器会优先使用 AOF文件来还原数据库
    - 只有AOF 处于关闭状态时， 服务器才会使用RDB文件来还原数据库


<h2 id="899193c751be1a257794d0c55add6a1c"></h2>


## 10.1.2 BGSAVE命令执行是的服务器状态

 - 在 BGSAVE 命令执行期间， 客户端发送的SAVE/BGSAVE 命令会被服务器拒绝,以防止产生竞态条件
 - BGREWRITEAOF 和 BGSAVE 两个命令不能同时执行
    - 如果BGSAVE命令正在执行，那么客户端发送的BGREWRITEAOF 命令会被延迟到BGSAVE命令执行完毕之后执行
    - 如果 BGREWRITEAOF命令正在执行，那么客户端发送的BGSAVE命令会被服务器拒绝。
    - 两者其实不冲突，不能同时执行它们只是一个性能方面的考虑

<h2 id="f7309047e97f6fd59cae1751c9ecc9ac"></h2>


## 10.2 自动间隔性保存

 - Redis允许用户通过设置服务器配置的save选项，让服务器每隔一段时间自动执行一次BGSAVE命令
 - 如：

```
save 900 1
save 300 10
save 60 10000
```

 - 那么只要满足以下3个条件的任意一个，BGSAVE命令就会被执行
    - 900秒内， 对数据库进行了至少1次修改
    - 300秒内， 对数据库进行了至少10次修改
    - 60秒内，  对数据库进行了至少10000次修改
 - PS. 这也是Redis默认的 save选项


<h2 id="6379208e54e6df4bd7230e05f1ddcd9c"></h2>


# 第11章  AOF持久化

 - Append Only File
 - AOF 通过保存Redis服务器所执行的写命令来记录数据库状态


<h2 id="6d04df896b36247259132fb82b148101"></h2>


## 11.1 AOF持久化的实现

 - AOF持久化的实现 可以分为 3个步骤
    - 命令追加 append
        - 服务器执行完一个写命令后，会议协议格式将被执行的写命令追加到服务器状态的aof_buff缓冲区的末尾。
    - 文件写入
        - 服务器每次结束一个事件循环之前，会调用flushAppendOnlyFile函数，考虑是否将aof_buf缓冲区的内容写入和保存到 AOF文件里面
    - 文件同步 sync
        - 操作系统本身对写文件也有一个缓冲系统，这对写入数据带来了安全问题。
        - 为此 系统提供了 fsync 和 fdatasync 两个同步函数，可以强制让操作系统立即将缓冲区中的数据写入到磁盘.

 - flushAppendOnlyFile 函数的行为由服务器配置的appendfsync 选项来决定



 appendfsync选项 | flushAppendOnlyFile行为
--- | --- 
always | aof_buf缓冲区所有内容 **写入并同步到** AOF文件
everysec | 默认选项 , 所有内容写入到AOF文件，如果上次同步AOF文件的时间距离现在超过1s，则同步
no |  所有内容写入到AOF文件， 由操作系统决定 何时同步


<h2 id="bf09e9a5e2c2f7fa63e2e63ce9d85424"></h2>


## 11.3 AOF重写

 - 随着服务器运行时间的流逝， AOF文件中的内容会越来越多， 文件体积页越来越大
 - AOF rewrite 功能 可以创建一个新的AOF文件来替代现有的AOF文件， 去掉了一些冗余命令



<h2 id="aa0a9a66d75378fa51e47a76e278790f"></h2>


# 第14章 服务器

<h2 id="01212d817ddb139f1bb2895bb825ac34"></h2>


## 14.2 serverCron 函数

 - serverCron 函数 默认每隔 100ms 执行一次，这个函数负责管理服务器的资源，并保持服务器自身的良好运转


<h2 id="105e46bac70d6bacbf39e68329c7462c"></h2>


### 14.2.1 更新服务器时间缓存

 - Redis中 有不少功能需要获取系统的当前时间，而每次获取系统的当前时间都需要 执行一次系统调用，为了减少系统调用，服务器状态中的 unixtime属性和mstime属性 被用作当前时间的缓存(分别为 秒级和毫秒级)
 - 因为serverCron 更新频率的原因， 上面两个属性的记录的时间的精确度并不高
    - 服务器只会在 打印日志，更新服务器的LRU时钟 等这类对时间精确度要求不高的功能上使用 时间缓存
    - 对于 为key设置过期时间，添加慢查询日志 这种需要高精度时间的功能来说，服务器还是会再次执行系统调用，从而获得最准确的系统当前时间。



<h2 id="105b9f5eb4cd097b8d05a0689fbc6cee"></h2>


# 第三部分 多级数据库的实现

<h2 id="1083f1f72ccba95cb67916bfb993be58"></h2>


# 第15章 复制

 - Redis中， 用户可以通过 执行 SLAVEOF 命令或者设置 slaveof 选项，让一个服务器去复制 另一个服务器
    - master <- slave
 

<h2 id="3622aa17f59dc29d9f444a1fa691b762"></h2>


# 第16章 Sentinel

 - Sentinel 是 Redis 高可用性解决方案： 由一个或多个 Sentinel实例 组成的 Sentinel 系统 可以监视任意多个主服务器，以及它们下面的从服务器，并在 被监视的主服务器 进入下线状态时，自动将下线主服务器下的某个从服务器升级为 新的主服务器。
    - 1. 察觉 主服务器下线， 终止从服务器的复制
    - 2. 等待 主服务器上线，如果下线时长超过设置值，进行故障转移
    - 3. 挑选一台从服务器升级为主服务器， 同时原来的主服务器降级为 从服务器。


<h2 id="1729d027ffc4c25f8f95d8c6ae87439b"></h2>


## 16.1 启动并初始化 Sentinel

```
$ redis-sentinel /path/to/your/sentinel.conf

# or 

$ redis-server /path/to/your/sentinel.conf --sentinel
```

 - 当一个 sentinel 启动时，它需要执行：
    - 1. 初始化服务器
    - 2. 将普通Redis服务器使用的代码 替换成 Sentinel 专用代码
    - 3. 初始化 Sentinel 状态
    - 4. 根据给定的配置文件，初始化 Sentinel的监视主服务器列表
    - 5. 创建 连向主服务器的网络链接


<h2 id="8e86642cb4ff7a5603b4519b811c97d5"></h2>


### 16.1.1 初始化服务器

 - Sentinel 本质上只是一个运行在 特殊模式下的Redis服务器， 所以启动Sentinel的第一步，就是初始化一个Redis服务器
 - 不过 因为 Sentinel执行的工作和 普通redis服务器 不同，所以Sentinel的初始化过程有所不同
 - Sentinel 并不是用数据库，所以 不会载入 RDB或AOF 文件
 - 很多 redis 命令 在 Sentinel 服务器上也无法使用


<h2 id="0980835f438dc23319a78f9c9f1e2911"></h2>


### 16.1.2 使用 Sentinel 专用代码

 - 比如说， 普通redis 服务器使用 `redis.h/REDIS_SERVERPORT` 作为服务器端口
    - `#define REDIS_SERVERPORT 6379`
 - 而 Sentinel使用 `sentinel.c/REDIS_SENTINEL_PORT` 为了服务器端口
 - 等等

<h2 id="8a7bbadb30e40fd09043360410456aca"></h2>


### 16.1.3 初始化 Sentinel 状态

<h2 id="5c1205ac880316d36c321416d35d59b4"></h2>


### 16.1.4 初始化 Sentinel 状态的 master属性

 - Sentinel 状态中的 masters 字段 记录了所有被 Sentinel 监视的 主服务器的相关信息，其中：
    - 字典的key 是 被监视的主服务器的名字
    - 而value 则是被监视主服务器 对象的 `sentinel.c/sentinelRedisInstance` 接哦股
 - 每个 sentinelRedisInstance结构 代表一个 被 Sentinel监视的Redis服务器实例。
    - 这个实例可以是 主服务器，从服务器，或者另外一个Sentinel
 - 对 Sentinel 状态的初始化 将引发 对masters 字典的初始化， 而 masters 字典的初始化 是根据被载入的 Sentinel 配置文件来进行的。
 - 如下面的配置文件

```
######################
# master 1 configure #
######################

sentinel moniter master1 127.0.0.1 6379 2
# 多少时间无响应后 判断为下线
sentinel down-after-milliseconds master1 30000
# 故障转移操作时， 可以同时对新的主服务器进行同步的从服务器数量
sentinel parallel-syncs master1 1
# 刷新故障迁移状态的最大时限
sentinel failover-timeout master1 900000


######################
# master 2 configure #
######################

sentinel moniter master2 127.0.0.1 12345 5
sentinel down-after-milliseconds master2 50000
sentinel parallel-syncs master2 5
sentinel failover-timeout master2 450000
```


<h2 id="8841ef9a85d2bb92800b807f68b9aa90"></h2>


### 16.1.5 创建连向主服务器的网络链接

 - Sentinel 将成为主服务器的客户端 ，对于每台被监视的主服务器， Sentinel都会创建两个异步链接
    - 一个是命令链接
    - 一个是订阅链接 , 专门用于 订阅 主服务器的 __sentinel__:hello 频道


<h2 id="107d9ebc3593fc7492de4218da5f40fc"></h2>


## 16.2 获取主服务器信息

<h2 id="b7b1e314614cf326c6e2b6eba1540682"></h2>


## TODO


<h2 id="53276068e0f0db9687713c65e75a141d"></h2>


# 第17章 集群

<h2 id="b7b1e314614cf326c6e2b6eba1540682"></h2>


## TODO











 















