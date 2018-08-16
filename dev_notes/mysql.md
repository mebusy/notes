
# Mysql

# Misc

## Mysql 并发更新数据 加锁处理

 - MySQL是支持给数据行加锁（InnoDB）的，并且在UPDATE/DELETE等操作时确实会自动加上排它锁
 - 只是并非只要有UPDATE关键字就会全程加锁 , 如

```
UPDATE table1 SET num = num + 1 WHERE id=1;
```

这句 其实并不只是一条UPDATE语句 ，而应该类似于两条SQL语句（伪代码）：

```
a = SELECT * FROM table1 WHERE id=1；
UPDATE table1 SET num = a.num + 1 WHERE id=1;
```

 - 其中执行SELECT语句时没有加锁，只有在执行UPDATE时才进行加锁的。
 - 会出现并发操作时的更新数据不一致。
 - 解决的方法可以有2种：
    - 1 通过事务显式的对SELECT进行加锁
    - 2 使用乐观锁机制


### SELECT显式加锁

 - 对SELECT进行加锁的方式有两种，如下：

```
SELECT ... LOCK IN SHARE MODE       #共享锁，其它事务可读，不可更新
SELECT ... FOR UPDATE       #排它锁，其它事务不可读写
```

 - 对于上面提到的场景，必须使用排它锁.
 - 上面的2种语句只有在事务之中才能生效，否则不会生效。 在MySQL命令行使用事务的方式如下：

```
SET AUTOCOMMIT=0;
BEGIN WORK;
    a = SELECT num FROM table1 WHERE id=2 FOR UPDATE;
    UPDATE table1 SET num = a.num + 1 WHERE id=2;
COMMIT WORK;
```

 - 这样只要以后更新数据时，都使用这样事务来进行操作；那么在并发的情况下，后执行的事务就会被堵塞，直到当前事务执行完成。（通过锁把并发改成了顺序执行）


### 使用乐观锁

 - 乐观锁是锁实现的一种机制，它总是会天真的认为所有需要修改的数据都不会冲突。
 - 所以在更新之前它不会给数据加锁，而只是查询了数据行的版本号（这里的版本号属于自定义的字段，需要在业务表的基础上额外增加一个字段，每当更新一次就会自增或者更新）。
 - 在具体更新数据的时候更新条件中会添加版本号信息，当版本号没有变化的时候说明该数据行未被更新过，并且也满足更新条件，所以会更新成功。
 - 当版本号有变化的时候，则无法更新数据行，因为条件不满足，此时就需要在进行一次SQL操作。（重新查询记数据行，再次使用新的版本号更新数据）

原则上，这2种方式都可以支持。具体使用哪一种就看实际的业务场景，对哪种支持更好，并且对性能的影响最小。


--- 

# 第1章  MySQL 体系结构和存储殷勤

## 1.1 配置文件

 - MySQL 可以没有配置文件，这种情况下， MySQL 会按照编译时的默认参数设置 启动实例
 - 用以下命令可以查看当 MySQL 数据库实例启动时， 会在哪些位置查找配置文件

```
# mysql --help | grep cnf
                      order of preference, my.cnf, $MYSQL_TCP_PORT,
/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf
```

 - 可以看到， MySQL 是按 `/etc/my.cnf -> /etc/mysql/my.cnf -> ~/.my.cnf`  顺序读取配置文件的.
 - 如果几个配置文件中 都有同一个参数， 以最后一个读到的参数为准 


## 1.3 MySQL 存储引擎

### 1.3.1 InnoDB 存储引擎
 
 - 默认引擎, 支持事务， 行锁设计，支持外键
 - 4.1开始， 每个InnoDB的表 单独放到一个独立的 idb文件中
 - 每张表 按 主键的顺序进行存放， 如果没有显示指定主键， InnoDB 会为每一行 生成一个6字节的 ROWID


### 1.3.2 MyISAM 引擎

 - 不支持事务，表锁设计，支持全文索引
 - MyISAM 的缓冲池只 cache 索引文件，而不cache 数据文件


### 1.3.3 NDB 存储引擎

 - 集群存储引擎 ， share nothing 的集群架构
 - NDB的特点是 数据全部放入内存中， 因此主键查找速度极快
 - JOIN操作是在数据库层完成的，而不是在存储引擎层完成的， 复杂的JOIN 操作需要巨大的网络开销，因此查询速度很慢.

### 1.3.4 Memory 存储引擎

 - 只支持表锁，性能较差， 并且不支持 TEXT和BLOB 类型
 

## 1.5 连接MySQL
 
 - TCP/IP
 - UNIX 域套接字
    - Linux环境下， 可以使用 UNIX域套接字
    - UNIX域套接字 其实不是一个网络协议， 所以只能在 MySQL客户端和数据库实例 在一台服务器上的情况下使用


# 第二章 InnoDB 

## 2.3 内存

 - 1 缓冲池
    - InnoDB 是基于磁盘存储的，并将其中的记录按照 页的方式进行管理。 Disk-base Database. 基于磁盘的数据库系统，通常使用缓冲池技术来提高数据库的整体性能
    - 配置参数:  innodb_buffer_pool_size 
    - 还可以配置多个缓冲池的实例，  每个页根据哈希值平局分配到 不同缓冲池实例中， 好处是减少数据库内部的资源竞争， 增加数据库的并发处理能力。
    - 配置参数:  innodb_buffer_pool_instances
 - 2 LRU List, Free List 和 Flush List
    - 缓冲池 里存放各种类型的页， 通过 LRU 算法进行管理。
    - Free List 空闲页
    - LRU列表中的页被修改后， 称为 dirty page, 即缓冲池中的页和磁盘上的页的数据产生了不一致，  Flush List 包含了这些 dirty page.
 - 3 redo log buffer


## 2.6 InnoDB 关键特性

 - insert buffer
 - double write
 - Adaptive Hash Index 自适应哈希索引
 - Async IO
 - Flush Neighbor Page 刷新邻接页

### 2.6.1 Insert Buffer

 - Insert Buffer 和数据页一样，也是物理页的一部分
 - InnoDB中， 主键是行唯一的标识符。 
    - 通常 应用程序中 行记录的插入顺序是按照主键递增的顺序进行插入的。 因此不需要磁盘的随机读取。 这类情况下的插入操作，速度是非常快的。
    - 但是 并不是所有的主键插入都是顺序的。 若主键 是UUID 这样的类，那么插入和 辅助索引一样， 同样是随机的。
 - InnoDB 开创性的设计了 Insert Buffer, 对于非聚集索引的插入或更新操作， 不是每一次直接插入到索引页中， 而是先判断插入的非聚集索引页 是否在缓冲池中， 若在直接插入，若不在， 则先放入到一个 Insert buffer 对象中。
    - 然后再以一定频率和情况进行 Insert Buffer 和 辅助索引页字节点的 merge 操作， 将多个插入合并到一个操作中(因为在一个索引页中)， 提高性能.
 - Insert Buffer 的使用需要同时满足以下两个条件
    - 索引是辅助索引 secondary index
    - 索引不是唯一的 unique 
 - 1.0.x版本开始引入 Change buffer ， 是 Insert buffer 的升级， 可以对 INSERT, DELETE, UPDATE 都进行缓冲


### 2.6.2 double write
 
 - 提高数据页的可靠性


### 2.6.3 自适应哈希索引

 - InnoDB 会监控对 表上各索引页的查询。
    - 如果观察到 建立hash索引 可以带来速度提升， 则建立hash 索引，称之为 自适应哈希索引 AHI
 - AHI 有一个要求，即对这个页的连续访问模式必须一样


# 第4章 表









