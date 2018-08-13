
# 第二部分 单机数据库的实现

---

# 第九章 数据库

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


## 9.3 数据库 key space

 - `redis.h/redisDb` 结构中的 dict 字典保存了 这个 redisDb 中 所有的 key-value pair, 我们将这个字典成为 key space.

```c
typedef struct redisDb {
    // ...
    dict *dict ;
    // ...
} redisDb ;
```


### 9.3.6 读写 key space的维护操作

 - 当使用redis 命令对数据进行读写时， 服务器不仅会对 key space 执行特定的读写操作， 还会执行一些额外的维护操作：
    - 在读取一个key后 (读写操作都要对key进行读取)， 服务器会根据key是否存在来更新服务器的key space 命中次数，或不命中次数，
        - 这两个值 可以在 INFO stats 命令的 keyspace_hits 属性 和 keyspace_misses 属性中查看
    - 在读取一个key后， 服务器会更新 key的 LRU时间
    - 如果服务器在读取一个key时发现该key已经过期，那么服务器会先删除这个过期键，然后再执行余下的其他操作。 
    - 如果由客户端使用 WATCH 命令监视了某个key， 那么服务器在对被监视的key进行修改之后， 会讲这个key 标记为 dirty，从而让事务程序注意到 这个key已经被修改过。
    - 服务器每次修改一个key之后， 都会对 dirty key 计数器的值增加1， 这个计数器会触发服务器的持久化以及复制操作。
    - 如果服务器开启了 数据库通知功能， 那么在对key进行修改后，服务器将按配置发送相应的数据库通知。


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


### 9.4.1 设置过期时间

 - EXPIRE <key> <ttl>
 - PEXPIRE <key> <ttl>
 - EXPIREAT <key> <timestamp>
 - PEXPIREAT <key> <timestamp>


### 9.4.2 保存过期时间

 - redisDb 结构的 `dict *expires;` 字典 保存了 数据库中所有key的过期时间
    - 过期字典的key是一个指针， 这个指针指向 key space 中的某个key对象，也即是某个数据库key
    - 过期字典的value是一个 long long类型的整数，这个整数保存了 过期时间 -- 一个毫秒精度的 UNIX时间戳。


### 9.4.3 移除过期时间

 - PERSISI 命令可以 移除一个key的过期时间，


```
redis:6379> PERSIST A
(integer) 1
redis:6379> TTL A
(integer) -1
```


## 9.6 Redis 过期key的删除策略

 - 惰性删除(访问key的时候 才进行过期检查) ，和 定期删除（每隔一定时间执行一次删除过期操作)


## 9.7 AOF, RDB 和 复制功能 对过期键的处理

### 9.7.1 生成 RDB 文件

 - 执行 SAVE 或 BGSAVE 命令创建一个新的 RDB文件时， 程序会对数据库中的key进行检查，已过期的key 不会被保存到新创建的 RDB 文件中。

### 9.7.2 载入 RDB文件

 - 在启动Redis服务器时，如果服务器开启了 RDB 功能，那么服务器将对 RDB 文件进行载入
    - 如果服务器以master模式运行， 那么在 载入RDB文件时，程序会对文件中保存的key进行检查，未过期的键会被载入到数据库中， 而过期的键则会被忽略。
    - 如果服务器以 slaver 模式运行，key无路是否过期，都会被载入到数据库总。 因为主从服务器在进行数据同步的时候， 这些过期key 就会被清空，所以不会造成影响。


### 9.7.3 AOF 文件写入

 - 当服务器以 AOF 持久化模式运行时， 如果数据库中的某个key已经过期， 但它还没有被删除， 那么AOF 文件不会因为这个 过期key 而产生任何影响。
 - 但过期key 被惰性删除 或者 定期删除之后， 程序会向AOF 文件 append 一条 DEL 命令，来显示地记录该key已经被删除。
 - example：`GET message` 访问已过期的 message ， 服务器将执行以下三个动作
    1. 从数据库中 删除message key
    2. 追加一条 DEL message 命令到AOF 文件
    3. 向执行 GET命令的客户端 返回nil


### 9.7.4 AOF 重写

 - 和生成 RDB 文件时类似， 在执行AOF重写的过程中， 程序会对数据库中的key进行检查，已过期的key不会被保存到重写后的AOF 文件中。


### 9.7.5 复制
 
 - 当服务器运行在 复制模式下， 从服务器的过期键删除动作由主服务器控制：
    - 主服务器在删除一个过期键之后， 会显示地向所有从服务器发送一个 DEL命令，告知从服务器删除这个过期键
    - 从服务器在执行客户端发送的读命令时， 即使碰到过期键也不会将过期键删除，而是继续像处理未过期键一样处理
    - 从服务器只有在 接到主服务器发来的DEL命令之后，才会删除过期键

 - example， 有一对主从服务器， 它们数据库中保存了 过期的key `message`
    - 如果这时 有客户端向从服务器 发送命令 GET message ， 那么从服务器 将发现 message 已经过期， 但从服务器并不会删除 message， 而是继续讲 message的值 返回给客户端， 就好像 message 没有过期。
    - 假设在此之后， 有客户端向 主服务器 发送 GET message， 那么主服务器将发现 message已经过期，主服务器会删除message， 向客户端返回 nil， 并向从服务器发送 DEL message 命令。
        - 从服务器在接收到 服务器发来的 DEL message 命令后，也会从数据库中删除 message.


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


# 第十章  RDB 持久化

 - RDB持久化既可以手动执行，也可以根据服务器配置 定期执行， 将数据库状态保存到一个 RDB文件中
 - RDB文件是一个经过压缩的二进制文件

## 10.1 RDB文件的创建和载入

 - 两个命令可以生成 RDB文件
    - SAVE , 阻塞服务器进程
    - BGSAVE ， fork一个子进程， 服务器进程继续处理命令
 - RDB文件的载入工作是在 服务器启动时 自动执行的，没有专门的命令
 - 另外， 因为AOF文件的更新频率通过比RDB文件的更新频率高，所以：
    - 如果服务器开启了AOF ， 那么服务器会优先使用 AOF文件来还原数据库
    - 只有AOF 处于关闭状态时， 服务器才会使用RDB文件来还原数据库


## 10.1.2 BGSAVE命令执行是的服务器状态

 - 在 BGSAVE 命令执行期间， 客户端发送的SAVE/BGSAVE 命令会被服务器拒绝,以防止产生竞态条件
 - BGREWRITEAOF 和 BGSAVE 两个命令不能同时执行
    - 如果BGSAVE命令正在执行，那么客户端发送的BGREWRITEAOF 命令会被延迟到BGSAVE命令执行完毕之后执行
    - 如果 BGREWRITEAOF命令正在执行，那么客户端发送的BGSAVE命令会被服务器拒绝。
    - 两者其实不冲突，不能同时执行它们只是一个性能方面的考虑

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


# 第11章  AOF持久化

 - Append Only File
 - AOF 通过保存Redis服务器所执行的写命令来记录数据库状态


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


## 11.3 AOF重写

 - 随着服务器运行时间的流逝， AOF文件中的内容会越来越多， 文件体积页越来越大
 - AOF rewrite 功能 可以创建一个新的AOF文件来替代现有的AOF文件， 去掉了一些冗余命令






 















