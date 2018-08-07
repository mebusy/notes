
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

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/sds_example.png)

 - 上图， free 为0， 表示这个SDS没有分配任何未使用空间
    - len 为5，表示这个SDS保存了一个5字节长的字符串
    - buf 属性是一个 char[], 
 - SDS 遵循了C字符串以 `\0`结尾的惯例，保存`\0`的1字节不计算在SDS的len属性里面
    - 为`\0`分配额外的1个字节，以及添加 `\0` 到字符串末尾的操作都是有SDS函数自动完成的。
    - 所以这个 `\0`  对于SDS的使用者是完全透明的。
    - 遵循 `\0` 结尾这一惯例的好处是，SDS可以直接重用一部分C字符串函数库里面的函数。
        - `printf( "%s" , s->buf );`

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/sds_example2.png)


## 2.2 SDS 与字符串的区别

### 2.2.1 常数复杂度 获取字符串长度

 - 因为C字符串 并不记录自身的长度信息，所以 获取长度必须遍历整个字符串O(n)
 - 而SDS 获取长度复杂度为 O(1), 这确保了获取字符串长度的工作不会成为Redis的性能瓶颈.
    - 即使我们对一个非常长的 key做 STRLEN命令，也不会对系统系统造成任何影响。


### 2.2.2 杜绝缓冲区溢出

 - C 字符串不记录自身长度带来的另一个问题是容易造成缓冲区溢出
    - 如 `<string.h>/strcat` 拼接的时候不会做溢出检测
 - 当 SDS API 需要对SDS进行修改是，API 会先检查SDS的空间是否满足修改所需的要求，如果不满足的话，API会自动将SDS的空间扩展至合适的大小，然后才执行实际的修改操作。

### 2.2.3 减少修改字符串时带来的内存重分配次数

 - 每次增长/缩短一个C字符串， 程序总是要对保存这个C字符串的数据进行一次内存重分配操作。
    - 如 缩短一个字符串，需要通过重新分配内存来释放那部分不再使用的空间，如果忘记这一步，就会导致内存泄漏( 因为不记录长度信息？ )
 - Redis作为数据库，数据会发生频繁修改，如果每次修改字符串的长度都需要执行一次内存重分配的话，会对性能造成严重影响。
 - 为了避免C字符串的这种缺陷，SDS 通过 未使用空间 解除了 字符串长度和底层数组长度之间的关联。
    - 通过 未使用空间， SDS实现了空间预分配和惰性空间释放两种优化策略。
        - 1. 空间预分配 
            - 对SDS进行空间扩展时，不仅会为SDS分配修改所必须的空间，还会分配和修改后长度相同的未使用空间，但是最大不会超过1MB.
        - 

