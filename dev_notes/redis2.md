
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
    - 















