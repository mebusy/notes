
# Redis 设计与实现

[docker redis image](https://docs.docker.com/samples/library/redis)

 - 需求: 实现类似微博的共同关注
    - 从集合的角度看，就是一个交集的概念。应该很容易实现？
    - 关系数据库并不直接支持 交集计算操作，要计算两个集合的交集，除了需要对两个数据表执行 JOIN操作意外，还需要对合并的结果去重DISTINCT操作，最终导致交集操作的实现变得异常复杂。
    - Redis 内置了集合数据类型，其中的交集计算操作可以直接用于实现这个共同关注功能。

# 1 第一章

 - Redis数据库里面的每个键值对 都是由 对象组成的，其中
    - 数据库键 总是一个字符串对象
    - 值可以是 字符串对象, list object, hash object, set object, sorted set object


# 2 第二章 简单动态字符串

 - Redis没有直接使用 C字符串( `\0` 结尾 )，而是自己构建了一种名为简单动态字符串(simple dynamic string ,SDS) 的抽象类型, 并将 SDS用作Redis默认字符串表示。
 - 在Redis里面，C字符串只会作为 字符串常量string literal 用在一些无序对字符串值进行修改的地方，比如打印日志:
    - `redisLog(REDIS_WARNING, "Redis is now ready to exit, bye bye...");`
 - 当 Redis需要一个可以被修改的字符串值时， Redis就会使用SDS来表示字符串。
    - 比如，Redis里的key-value pair 的键和值都是SDS
 - 除了用来保存数据库中的字符串值之外， SDS还被用作缓冲区buffer: 
    - AOF模块中的AOF缓冲区, 以及客户端状态中的输入缓冲区，都是有SDS实现的。


## SDS的定义

 - 每个 `sds.h/sdshdr` 结构表示一个SDS值

```c
struct sdshdr {
    // 所保存字符串长度
    int len;
    // 纪录 buf数组中未使用字节的数量
    int free;
    // 字符串数组，用于保存字符串
    char buf[];    
}
``` 




