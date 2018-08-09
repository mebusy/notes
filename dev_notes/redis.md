...menustart

 - [Redis 设计与实现](#387f728bb737b1de0668033d5bc04a2c)
 - [第一章](#ce87533fbd746b8a6487078028fd3162)
 - [第二章 简单动态字符串](#c3e17e255aaa5c90ba15bf6b7b8dd4b6)
     - [SDS的定义](#0f2451d5f33972e84f60e9ce6d71de9b)
     - [2.2 SDS 与字符串的区别](#b9a03087283735023631acf642a4b59f)
         - [2.2.1 常数复杂度 获取字符串长度](#b24ce3884a7989b428894b5b9e6215ce)
         - [2.2.2 杜绝缓冲区溢出](#5aea993c723bbb93af487fc4a44f27b5)
         - [2.2.3 减少修改字符串时带来的内存重分配次数](#50a3e42afacfa5113a5ef835f81a59d7)
         - [2.2.4 二进制安全](#fe16b5423e86dd95dfb418659da3fa7b)
         - [2.2.5 兼容部分C字符串函数](#4f424f0cb00766fc9e0258ff7fb3e829)
 - [第三章 链表](#439d12ff1033af4e6bf3e78f2128f30a)

...menuend


<h2 id="387f728bb737b1de0668033d5bc04a2c"></h2>

# Redis 设计与实现

[docker redis image](https://docs.docker.com/samples/library/redis)

 - 需求: 实现类似微博的共同关注
    - 从集合的角度看，就是一个交集的概念。应该很容易实现？
    - 关系数据库并不直接支持 交集计算操作，要计算两个集合的交集，除了需要对两个数据表执行 JOIN操作意外，还需要对合并的结果去重DISTINCT操作，最终导致交集操作的实现变得异常复杂。
    - Redis 内置了集合数据类型，其中的交集计算操作可以直接用于实现这个共同关注功能。

<h2 id="ce87533fbd746b8a6487078028fd3162"></h2>

# 第一章

 - Redis数据库里面的每个键值对 都是由 对象组成的，其中
    - 数据库键 总是一个字符串对象
    - 值可以是 字符串对象, list object, hash object, set object, sorted set object


<h2 id="c3e17e255aaa5c90ba15bf6b7b8dd4b6"></h2>

# 第二章 简单动态字符串

 - Redis没有直接使用 C字符串( `\0` 结尾 )，而是自己构建了一种名为简单动态字符串(simple dynamic string ,SDS) 的抽象类型, 并将 SDS用作Redis默认字符串表示。
 - 在Redis里面，C字符串只会作为 字符串常量string literal 用在一些无序对字符串值进行修改的地方，比如打印日志:
    - `redisLog(REDIS_WARNING, "Redis is now ready to exit, bye bye...");`
 - 当 Redis需要一个可以被修改的字符串值时， Redis就会使用SDS来表示字符串。
    - 比如，Redis里的key-value pair 的键和值都是SDS
 - 除了用来保存数据库中的字符串值之外， SDS还被用作缓冲区buffer: 
    - AOF模块中的AOF缓冲区, 以及客户端状态中的输入缓冲区，都是有SDS实现的。


<h2 id="0f2451d5f33972e84f60e9ce6d71de9b"></h2>

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


<h2 id="b9a03087283735023631acf642a4b59f"></h2>

## 2.2 SDS 与字符串的区别

<h2 id="b24ce3884a7989b428894b5b9e6215ce"></h2>

### 2.2.1 常数复杂度 获取字符串长度

 - 因为C字符串 并不记录自身的长度信息，所以 获取长度必须遍历整个字符串O(n)
 - 而SDS 获取长度复杂度为 O(1), 这确保了获取字符串长度的工作不会成为Redis的性能瓶颈.
    - 即使我们对一个非常长的 key做 STRLEN命令，也不会对系统系统造成任何影响。


<h2 id="5aea993c723bbb93af487fc4a44f27b5"></h2>

### 2.2.2 杜绝缓冲区溢出

 - C 字符串不记录自身长度带来的另一个问题是容易造成缓冲区溢出
    - 如 `<string.h>/strcat` 拼接的时候不会做溢出检测
 - 当 SDS API 需要对SDS进行修改是，API 会先检查SDS的空间是否满足修改所需的要求，如果不满足的话，API会自动将SDS的空间扩展至合适的大小，然后才执行实际的修改操作。

<h2 id="50a3e42afacfa5113a5ef835f81a59d7"></h2>

### 2.2.3 减少修改字符串时带来的内存重分配次数

 - 每次增长/缩短一个C字符串， 程序总是要对保存这个C字符串的数据进行一次内存重分配操作。
    - 如 缩短一个字符串，需要通过重新分配内存来释放那部分不再使用的空间，如果忘记这一步，就会导致内存泄漏( 因为不记录长度信息？ )
 - Redis作为数据库，数据会发生频繁修改，如果每次修改字符串的长度都需要执行一次内存重分配的话，会对性能造成严重影响。
 - 为了避免C字符串的这种缺陷，SDS 通过 未使用空间 解除了 字符串长度和底层数组长度之间的关联。
    - 通过 未使用空间， SDS实现了空间预分配和惰性空间释放两种优化策略。
        - 1. 空间预分配 
            - 对SDS进行空间扩展时，不仅会为SDS分配修改所必须的空间，还会分配和修改后长度相同的未使用空间，但是最大不会超过1MB.
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ads_append.png)
            - 如果这时，我们执行 `sdscat( s " Tutorial" )` , 那么这次sdscat 将不需要执行内存重分配，因为未使用空间的13字节足以保存 9字节的" Tutorial"
            - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/ads_append2.png)
            - 注: 's' 后的省略号表示若干字符省略
        - 2. 惰性空间释放
            - 缩短SDS保存的字符串时， 程序并不立即使用内存重分配来回收缩短后 多出来的字节，而是使用 free属性将这些字节的数量纪录起来，并等待将来使用。 
            - SDS 也提供了相应的API，让我们可以在有需要时，真正的释放SDS的未使用空间，所以不必担心内存浪费。


<h2 id="fe16b5423e86dd95dfb418659da3fa7b"></h2>

### 2.2.4 二进制安全

 - 二进制数据经常会包含 `\0` , 这给字符串处理带来了很大麻烦。
 - SDS API 都是 binary-safe的。

<h2 id="4f424f0cb00766fc9e0258ff7fb3e829"></h2>

### 2.2.5 兼容部分C字符串函数

 - 虽然SDS 是二进制安全的，但它们一样遵循C字符串以 `\0`结尾的惯例
    - API 总会将SDS保存的数据的末尾设置为 `\0`
    - 这是为了让那些保存文本数据的SDS可以重用一部分 <sting.h> 库定义的函数.


<h2 id="439d12ff1033af4e6bf3e78f2128f30a"></h2>

# 第三章 链表

 - 发布/订阅， 慢查询， 监视器 等功能都用到了 链表

## 3.1 链表和链表节点的实现

```c
// adlist.h/listNode
typedef struct listNode {
    struct listNode *prev ;
    struct listNode *next ;
    void *value ;
} listNode ;
```

```c
// addlist.h/list
typedef struct list {
    listNode *head;
    listNode *tail;
    // 链表所包含的节点数量
    unsigned long len ;
    void *(*dup)(void *ptr) ;
    void *(*free)(void *ptr) ;
    int (*match)(void *ptr, void *key) ;
} list ;
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/redis_list.png)

 - Redis 链表实现的特点：
    - 双端， 获取某个节点的 prev / next  的复杂度都是 O(1)
    - 无环， 表头的 prev 和 表尾的next 都指向 NULL, 对表的访问以 NULL结束
    - 带 head, tail 指针:  获取链表 头/尾节点的 复杂度 O(1)
    - 带长度计数器 : 获取 链表长度的时间复杂度 O(1)
    - 多态: 链表节点使用 `void *` 指针来保存节点值


# 第四章   字典

 - Redis 的 key-value pair 本身就是 使用字典作为底层实现的
 - 字典也是 哈希键的底层实现之一 ， 当一个哈希键 包含的键值对 比较对，又或者键值对中的元素都是 比较长的字符串时， Redis就会使用字典作为哈希键的底层实现

## 4.1 字典的实现

 - Redis的字典 使用 哈希表作为底层实现， 一个哈希表里面可以有 多个哈希表节点， 而每个哈希表节点就保存了 字典中的一个 键值对。

### 4.1.1 哈希表

```c
// dict.h/dictht
typedef struct dictht {
    // 哈希表数据
    dictEntry **table ;
    // 哈希表大小
    unsigned long size ;
    // 哈希表大小掩码，用于计算索引值
    unsigned long sizemask ;
    // 该哈希表 已有的节点数量    
    unsigned long used ;
} dictht; 
```

 - 每个 dictEntry 保存一个 键值对
 - size 记录 数组 table 的大小
 - used 记录了 哈希表当前 已有的节点(键值对)的数量


### 4.1.2 哈希表节点

```c
typedef struct dictEntry {
   void *key;
   union {
        void *val;
        uint64_tu64;    
        int64_ts64;    
   } v ; 
   // 形成单向链表
   struct dictEntry *next;
} dictEntry ;
```

 - next 用于解决 键冲突的问题

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/redict_dict.png)



