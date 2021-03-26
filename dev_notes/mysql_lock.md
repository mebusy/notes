...menustart

- [MySQL 锁](#8dc99461a1c4b9110a35ea875b10b70d)
    - [锁的类型](#dfa8b5aa96cb4af6e6c28cf50b2a3c43)
    - [锁的粒度](#cbc301535e8455434b2bbd29a183e55d)
    - [死锁](#60461afa5afbcb0457a420056c14a6c9)
    - [乐观锁/悲观锁](#685a6699c143f3090ecdabcc3618a2c5)
        - [乐观锁](#bf97e7abc7c23d4f37d6da39acc011d8)
        - [悲观锁](#891f975efa0ad8ed8582636e0bd98e41)
    - [锁升级](#f631c0a2d27c606f697b1e5987b74732)
- [Mysql 并发更新数据 加锁处理](#f12a4c82c151d110c6ea3521e6aca5b2)
    - [SELECT显式加锁](#18a31fbbef71484ce0cc52995764a78b)
    - [使用乐观锁](#4e7e4e0d4b9110317f8e672b2aa3af35)

...menuend


<h2 id="8dc99461a1c4b9110a35ea875b10b70d"></h2>


# MySQL 锁

<h2 id="dfa8b5aa96cb4af6e6c28cf50b2a3c43"></h2>


## 锁的类型

- InnoDB实现了两种标准的行级锁：
    1. 共享锁（S Lock）
        - 语法为：`select * from table lock in share mode`。
    2. 排他锁（X Lock）
        - 语法为：`select * from table for update`。
- 如果一个事务T1已经获取了行r的共享锁，那么另外的事务T2可以立即获得行r的共享锁。因为读取并不会改变行的数据，所以可以多个事务同时获取共享锁，称这种情况为**锁兼容**。
- 但若有其他的事务T3想获得行R的排他锁，则其必须等待事务T1、T2释放行r上面的共享锁，称这种情况为**锁不兼容**。


· | X | S
--- | --- | ---
X | 不兼容 |  不兼容
S |  不兼容 |  兼容

- 普通 select 语句默认不加锁，而CUD (insert,update,delete)操作默认加排他锁。


<h2 id="cbc301535e8455434b2bbd29a183e55d"></h2>


## 锁的粒度

锁级别 | 说明
--- | ---
表级锁 | 开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高,并发度最低。
行级锁 | 开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低,并发度也最高。
页面锁 | 开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般。


- 在以下情况下，表锁定优先于页级或行级锁定：
    - 表的大部分行用于读取。
    - 对严格的关键字进行读取和更新
        - UPDATE tbl_name SET column=value WHERE unique_key_col=key_value;
        - DELETE FROM tbl_name WHERE unique_key_col=key_value;
    - SELECT 结合并行的INSERT语句，并且只有很少的UPDATE或DELETE语句。
    - 在整个表上有许多扫描或GROUP BY操作，没有任何写操作。


<h2 id="60461afa5afbcb0457a420056c14a6c9"></h2>


## 死锁

MySQL提供了比较充足的死锁检测策略，当检测到死锁后，Innodb会将持有 「 **最少行级排他锁** 」 的事务进行回滚，来打破死锁.

<h2 id="685a6699c143f3090ecdabcc3618a2c5"></h2>


## 乐观锁/悲观锁

<h2 id="bf97e7abc7c23d4f37d6da39acc011d8"></h2>


### 乐观锁

- 用数据版本（Version）记录机制实现，这是乐观锁最常用的一种实现方式。
    - 即为数据增加一个版本标识，一般是通过为数据库表增加一个数字类型的 “version” 字段来实现。
    - 当读取数据时，将version字段的值一同读出，数据每更新一次，对此version值加1。
    - 当我们提交更新的时候，判断数据库表对应记录的当前版本信息与第一次取出来的version值进行比对，如果数据库表当前版本号与第一次取出来的version值相等，则予以更新，否则认为是过期数据。


```mysql
# read along with version 
select id,value,version from TABLE where id = <id>

# update by specific version
update TABLE
set value=2,version=version+1
where id=<id> and version=<version>
```

<h2 id="891f975efa0ad8ed8582636e0bd98e41"></h2>


### 悲观锁

即上面提过的 共享锁和排他锁。

<h2 id="f631c0a2d27c606f697b1e5987b74732"></h2>


## 锁升级

- 锁升级（Lock Escalation）是指将当前锁的粒度加大，锁粒度：`行锁 < 页锁 < 表锁`。
- InnoDB
    - 由一句单独的SQL语句在一个对象上持有的锁的数量超过了阈值，默认这个阈值为5000。
        - 如果是不同对象，则不会发生锁升级；
    - 锁资源占用的内存超过了激活内存的40%时就会发生锁升级。
- InnoDB根据每个事务访问的每个页对锁进行管理，采用位图的方式。因此不管一个事务锁住页中一个记录还是多个记录，其开销通常都是一致的。


---

<h2 id="f12a4c82c151d110c6ea3521e6aca5b2"></h2>


# Mysql 并发更新数据 加锁处理

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


<h2 id="18a31fbbef71484ce0cc52995764a78b"></h2>


## SELECT显式加锁

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


<h2 id="4e7e4e0d4b9110317f8e672b2aa3af35"></h2>


## 使用乐观锁

- 乐观锁是锁实现的一种机制，它总是会天真的认为所有需要修改的数据都不会冲突。
- 所以在更新之前它不会给数据加锁，而只是查询了数据行的版本号（这里的版本号属于自定义的字段，需要在业务表的基础上额外增加一个字段，每当更新一次就会自增或者更新）。
- 在具体更新数据的时候更新条件中会添加版本号信息，当版本号没有变化的时候说明该数据行未被更新过，并且也满足更新条件，所以会更新成功。
- 当版本号有变化的时候，则无法更新数据行，因为条件不满足，此时就需要在进行一次SQL操作。（重新查询记数据行，再次使用新的版本号更新数据）

原则上，这2种方式都可以支持。具体使用哪一种就看实际的业务场景，对哪种支持更好，并且对性能的影响最小。


---

[深入理解SELECT ... LOCK IN SHARE MODE和SELECT ... FOR UPDATE](https://blog.csdn.net/cug_jiang126com/article/details/50544728)


