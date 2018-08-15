
# 第4部分 独立功能的实现

# 第18章  发布与订阅

 - PUBLISH, SUBSCRIBE, PSUBSCRIBE 等命令组成
 - 通过 SBUSCRIBE 命令， 客户端可以 订阅一个 或多个频道 ， 每当有 其他客户端向 被订阅的频道发送消息 (message) 时，频道的所有订阅者 都会收到这条消息
    - `SUBSCRIBE "news.it"`
    - `PUBLISH "news.it" "hello"`
 - 客户端还可以通过 PSUBSCRIBE 命令订阅 一个或多个 **模式**
    - `"new.[ie]t"` 


## 18.1 频道的订阅与退订

```
SUBSCRIBE "news.sport" "news.movie"
UNSUBSCRIBE "news.sport" "news.movie"
```

## 18.2 模式的订阅和退订

```
PSUBSCRIBE "news.*"
PUNSUBSCRIBE "news.*"
```


## 18.3  发送消息

```
PUBLISH <channel> <message>
```

## 18.4 查看订阅信息
 
 - PUBSUB 可以查看 频道或模式的相关信息， 比如 某个频道目前有多少个 订阅者， 又或者 某个模式目前有多少个订阅者， 等等


### 18.4.1 PUBSUB CHANNELS

```
PUBSUB CHANNELS [pattern]
```

 - 用于返回服务器当前被订阅的频道 
    - 如果不给定 pattern 参数， 返回当前被订阅的所有频道
    - 如果给定 pattern 参数， 返回 与 pattern 匹配的 被订阅频道


### 18.4.2  PUBSUB NUMSUB

```
PUBSUB NUMSUB [channel-1 channel-2 ... channel-n] 
```

 - 返回 指定频道的 订阅者数量


### 18.4.3 PUBSUB NUMPAT

 - 返回 被订阅模式的数量



# 第19章  事务

 - Redis 通过 MULTI, EXEC, WATCH 等命令 来实现事务 transaction 功能。
 - 事务提供了一种  将多个命令请求打包， 然后一次性， 按顺序的执行多个命令的机制， 并且在事务 执行期间， 服务器不会中断事务 而该去执行其他客户端的命令请求， 它会将事务中的所有命令都执行完毕， 然后才去处理其他客户端的命令请求。
 - 以下是一个事务执行的过程, 首先以一个 MULTI 命令开始， 接着将多个命令放入事务当中，最后由 EXEC 命令将这个事务提交 给服务器执行。

```
redis:6379> MULTI
OK
redis:6379> set name "Practical Common Lisp"
QUEUED
redis:6379> GET name
QUEUED
redis:6379> SET author "Peter Seibel"
QUEUED
redis:6379> GET author
QUEUED
redis:6379> EXEC
1) OK
2) "Practical Common Lisp"
3) OK
4) "Peter Seibel"
```

## 19.1 事务的实现

 - 一个事务从开始到结束通常会  经历以下三个阶段
    - 1. 事务开始
    - 2. 命令入队
    - 3. 事务执行

### 19.1.1  事务开始

```
redis:6379> MULTI
OK
```

 - MULTI 可以将 执行该命令的客户端从 非事务状态 切换至 事务状态
    - 通过在 客户端状态的 flags 属性中 打开 REDIS_MULTI 标志来完成
 - 伪代码:


```
def MULTI():
    client.flags |= REDIS_MULTI
    replyOK()
```


### 19.1.2 命令入队

 - 当一个客户端处于非事务状态时， 这个客户端发送的命令会立即 被服务器执行:
 - 当一个客户端切换到 事务状态后， 服务器会根据这个客户端发来的不同命令，执行不能的操作
    - 如果是 EXEC, DISCARD, WATCH, MULTI 中的一个， 那么服务器会 立即执行这个命令
    - 如果是其他命令， 那么服务器并不会立即执行这个命令，而是放入一个事务队列里面， 然后向客户端 返回QUEUED 回复。


### 19.1.3 事务队列

 - 每个redis客户端都有自己的事务状态 mstate 属性：

```c
typedef struct redisClient {
    // ...
    multiState mstate ;     
    // ... 
}
```

 - 事务状态包含一个事务队列， 以及一个 已入队命令的计数器，也即 事务队列的长度

```c
typedef struct multiState {
    multiCmd *commands;
    int count ;    
} multiState;
```

### 19.1.4 执行事务

 - EXEC 命令会立即被服务器执行。 服务器会遍历 这个客户端的事务队列， 执行队列中保存的所有命令， 最后将 结果全部 返回给客户端。


## 19.2 WATCH 命令的实现

 - WATCH 是一个 乐观锁 optimistic locking, 它 可以在 EXEC 命令执行之前， 监视任意数量的数据库key，并在 EXEC命令执行时， 检查被监视的key 是否至少有一个 已经被修改过了。
    - 如果是的话， 服务器将 拒绝执行事务， 并向客户端返回代表 事务执行失败的 nil 回复


```
redis:6379> EXEC
(nil)
```


时间  |   客户端A | 客户端B
--- | --- | ---
T1 |  WATCH name  | 
T2 | MULTI  | 
T3 | SET name "peter" | 
T4 |   |  SET name "john"
T5 |  EXEC -> nil | 



 - 或者使用单个客户端模拟


```
redis:6379> WATCH name
OK
redis:6379> SET name "A"
OK
redis:6379> MULTI
OK
redis:6379> EXEC
(nil)
```

### 19.2.1 使用 WATCH 命令监视 数据库key

 - 每个redis数据库都保存着一个 watched_keys 字典， 这个字典的key是某个被 WATCH命令监视的数据库键，而value 是一个链表， 记录了所有监视 相应key的客户端

```c
typedef struct redisDb {
    // ...
    dict *watched_keys ;
    // ...
} redisDB ;;
```

### 19.2.2 监视机制的触发

 - 所有对数据库进行修改的命令，如 SET, LPUSH, SADD, ZREM, DEL, FLUSHDB 等等，在执行之后都会调用 `multi.c/touchWatchKey` 函数对 watched_keys字典进行检查， 查看是否有客户端正在监视 刚刚被修改过的 key
    - 如果有的话，那么 touchWatchKey 函数 会将相关客户端的 REDIS_DIRTY_CAS 表示打开， 表示该客户端的 事务安全性 已经被破坏。


### 19.2.3 判断事务是否安全

 - 当服务器接收到一个客户端发来的 EXEC 命令时， 服务器会根据这个客户端是否打开了 REDIS_DIRTY_CAS 标识来决定是否执行


## 19.3 事务的ACID性质

 - 在 Redis中， 事务总是具有原子性 Atomicity, 一致性 Consistency 和 隔离型 Isolation, 并且当 Redis运行在 某种特定的持久化模式下， 事务也具有耐久性 Durability.
 - 原子性
    - 事务要么全部执行，要么就一个都不执行
    - 不像传统的关系型数据库， Redis不支持 事务回滚机制。 即时事务队列中的某个命令执行出错了， 整个事务也会继续执行下去
 - 一致性
    - Redis 通过谨慎的检测和简单的设计 来保证事务的一致性. 对于 Redis事务可能出错的地方，Redis 做了妥善处理
        - 1. 入队错误
            - 如果一个事务 在入队命令的过程中，出现了 命令不存在，或 格式不正确 等情况，那么Redis将拒绝执行这个事务
        - 2. 执行错误
            - 出错的命令会被服务器识别出来，并进行相应错误处理，所以这些出错的命令不会对数据进行任何修改， 也不会对事务的一致性产生任何影响
        - 3. 服务器停机
            - 略
 - 隔离性
    - 隔离性是指， 即时数据库中 有多个事务并发的执行，各个事务之间也不会相互影响， 并且在并发状态下执行的事务和串行执行的事务产生的结果完全相同
    - 因为 Redis 是单线程方式 执行事务，以及事务队列中的命令， 并且服务器保证， 在执行事务期间不会对事务进行中断，因此，Redis的事务总是以串行的方式运行的，并且事务也总是具有隔离性的。

 - 耐久性
    - 耐久性是指， 当一个事务执行完毕， 所得结果已经被保存到永久性存储介质里面了。 即使事务执行完毕后停机， 所得结果也不会消失
    - Redis 事务的耐久性， 由Redis所使用的 持久化模式决定:
        - 内存模式下， 事务不具有耐久性
        - RDB 模式下， 也不具有耐久性。
        - AOF 模式下， 只有 appendfsync 设置为 always 时， 事务才具有 耐久性
    - 不论 Redis 在什么模式下运作， 在一个事务的最后加上 SAVE 命令， 总可以保证事务的耐久性
        - 不过这种方法 不具有实用性，效率太低

```
redis:6379> MULTI
OK
redis:6379> SET msg "hello"
QUEUED
redis:6379> SAVE
QUEUED
redis:6379> EXEC
1) OK
2) OK
```


# 第20章  Lua 脚本

 - 2.6 版本开始引入对Lua脚本支持
 - 使用 EVAL 命令可以直接对 输入的脚本求值:

```
redis:6379> EVAL "return 'hello world'" 0
"hello
```

 - 使用 EVALSHA 命令可以根据脚本的 SHA1 来对脚本进行求职， 但这个命令要求 SHA1 对应的脚本 必须至少被 EVAL 命令执行过一次, 或者 曾经被 SCRIPT LOAD 命令载入过

```
redis:6379> SCRIPT LOAD "return 2*2"
"4475bfb5919b5ad16424cb50f74d4724ae833e72"
redis:6379> EVALSHA 4475bfb5919b5ad16424cb50f74d4724ae833e72 0
(integer) 4
```


## 20.1 创建并修改 Lua环境

 - Redis 服务器创建并修改 Lua 环境的整个过程由以下几个步骤组成
    - 1. 创建一个基础Lua环境，之后的所有修改都是针对这个环境进行的
    - 2. 载入多个函数库到Lua环境里面，让Lua脚本可以使用这些函数库来进行数据操作
    - 3. 创建全局table redis,  包含了对Redis进行操作的函数， 比如用于在 Lua脚本中执行 Redis命令的redis.call 函数
    - 4. 使用 Redis自制的随机函数来替换 Lua原有的带有副作用的随机函数.
    - 5. 创建排序辅助函数， Lua环境使用这个 辅助函数来对一部分 Redis命令的结构进行排序， 从而消除这些命令的不确定性
    - 6. 创建 redis.pcall 函数的错误报告辅助函数， 这个函数可以提供更详细的出错信息
    - 7. 对Lua环境中的全局环境进行保护， 防止用户在执行 Lua脚本的过程中， 将额外的全局变量添加到Lua环境中
    - 8. 将修改完的Lua环境保存到 服务器状态的 lua属性中， 等待执行服务器传来的Lua脚本


### 20.1.1 创建Lua环境

 - `lua_open`
 - 载入函数库
    - base library:  
    - table
    - string
    - math
    - debug
    - Lua cjson
    - Lua Struct 
        - 用于在 Lua值和C结构之间进行转换 
        - 函数 struct.pack 将多个 Lua值打包成一个类结构 (struct-like)  字符串
        - struct.unpack 则从一个类结构字符串中 解包出多个Lua值。
    - Lua cmsgpack 
        - 用于处理 MessagePack格式的数据
        - cmsgpack.pack  将 lua值转换为 MessagePack 数据
        - cmsgpack.unpack 反之

### 20.1.3 创建 global table -- redis

 - redis 表 包含以下函数:
    - redis.call , redis.pcall
    - redis.log :   redis.LOG_DEBUG , redis.LOG_VERBOSE, redis.LOG_NOTICE, redis.LOG_WARNING
    - 用于计算 SHA1 的 redis.sha1hex 函数
    - 用于返回错误信息的 redis.error_reply , redis.status_reply 
 - 这些命令中，最重要也是最常用的就是 redis.call 和 redis.pcall , 使用这两个函数，用户可以直接在 Lua脚本中 执行Redis命令:


```
redis:6379> EVAL "return redis.call('PING')" 0
PONG
```

### 20.1.4  Redis Lua的随机函数

 - 为了保证相同的脚本 可以在 不同的机器上产生相同的作用， Redis 要求所有传入服务器的Lua脚本，以及Lua环境中的所有函数，都必须是无side effect 的 pure function.
 - 但是 math.random 和 math.randomseed 函数都是由 side effect 的， 它们不符合 Redis 对Lua环境的无 side effect 要求
    - 所以redis 用自己的函数 替代了 math.random 和 math.randomseed 
    - 对于相同的seed 来说， math.random 总产生相同的随机数序列， 这个函数是一个  pure function
    - 除非在脚本中使用 math.randomseed 显示的修改 seed, 否则每次运行脚本时， Lua环境都使用固定的 math.randomseed(0) 语句来初始化 seed


### 20.1.5 创建排序辅助函数

 - 对于lua脚本来说，另一个可能产生不一致数据的地方是那些 带有不确定性质的命令。
 - 比如对于一个set key 来说， set 元素的排列是无序的
 - Redis 将 SMEMBERS 这种在相同的数据集上 可能会产生不同输出的命令 称为"带有不确定性的命令", 包括 ：
    - SINTER
    - SUNION
    - SDIFF
    - SMEMBERS
    - HKEYS
    - HVALS
    - KEYS
 - 为了消除这些不确定性， 服务器会为 Lua环境创建一个排序辅助函数 `__redis__compare__helper` 
    - 当 Lua脚本执行完一个带有不确定性的命令之后， 程序会使用这个函数作为 compare 函数， 自动调用 table.sort 函数将命令的返回值做一次排序，以此来保证相同的数据集总是产生相同的输出。


### 20.1.6 redis.pcall 函数的错误报告辅助函数

 - `__redis__err_handler` 
 - `redis.pcall` 执行的命令 出现错误时，  `__redis__err_handler`  就会打印出错代码的来源和发生错误的行数，为程序的调试提供方便


### 20.1.7 保护 Lua的全局环境

 - 对Lua环境中的全局环境进行保护，确保 脚本不会因为 忘记使用local关键字 而将额外的全局变量 添加到Lua环境里面。
 - 因为 全局变量保护的原因， 当一个脚本试图创建一个 全局变量时， 服务器将报告一个错误

```
redis:6379> EVAL "x = 10" 0
(error) ... : Script attempted to create global variable 'x'
```

 - 除此之外， 试图 获取一个不存在的全局变量， 也会引发一个错误


```
redis:6379> EVAL "return x" 0
(error) ... : Script attempted to access nonexistent global variable 'x'
```

 - 不过 Redis 并不禁止 用户修改已存在的全局变量， 所以在执行 Lua脚本的时候， 必须非常小心， 以免 错误地修改了已存在的全局变量 , 比如 redis ...


### 20.1.8 将 Lua环境保存到服务器状态的 lua属性里面

 - 因为 Redis 使用 串行化方式来执行 Redis命令， 所以在特定的时间里， 最多都只会有一个脚本能够放进Lua环境里面运行， 因为 整个Redis服务器只需要创建一个Lua环境即可。


## 20.2 Lua 环境协作组件

 - Redis 服务器还创建了两个用于 与 Lua环境进行协作的组件
    - 负责执行Lua脚本中的Redis命令的 伪客户端
    - 以及 用于保存Lua脚本的 lua_scripts 字典

### 20.2.1 伪客户端

 - 因为执行 Redis 命令必须有响应的客户端状态， 所以为了执行Lua脚本中的Redis命令， Redis 专门为Lua环境创建了一个伪客户端。
 - Lua脚本使用 redis.call / redis.pcall 执行一个redis 命令，需要完成以下步骤:
    - 1. Lua  环境将 要执行的命令 传给 伪客户端
    - 2. 伪客户端 将命令传给 命令执行器
    - 3. 命令执行器 执行命令， 将结果返回 伪客户端
    - 4. 伪客户端接收命令执行器返回的命令结果， 并将这个命令结果返回给Lua环境
    - 5. Lua环境 将结果返回给 redis.call / redis.pcall 函数
    - 6. redis.call / redis.pcall 将命令经过作为 函数返回值，返回给脚本中的调用者

### 20.2.2 lua_scripts 字典

 - key 位 lua脚本的SHA1  checksum，而 value 则是 SHA1 对应的 Lua脚本
 - Redis 服务器会将所有被 EVAL 命令执行过的 Lua脚本， 以及所有被 SCRIPT LOAD 命令载入过的 Lua 脚本 都保存到 lua_scripts 字典里面
 - lua_scripts 有两个作用
    - 实现 SCRIPT EXISTS 命令
    - 实现 脚本复制功能


## 20.3  EVAL命令的实现







