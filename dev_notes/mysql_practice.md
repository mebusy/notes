
# Mysql实践

# 运维

<h2 id="1838954ac65225f29f4cccf9131bb24f"></h2>


## mysql 慢日志查询

```
set global slow_query_log='ON';
set global long_query_time=1;

show variables like 'slow_query%';
show variables like 'long_query_time';
```
- Now check the slow logs at `mysql.slow_log`

<h2 id="e1a8175ef9a04770289a68720bff0ffc"></h2>


## mysql 操作记录查询

```
SET GLOBAL general_log = 'ON'
SET GLOBAL log_output = 'TABLE'

show variables like '%general%';
```


- Now you can find the mysql operation log in `mysql.general_log` table


<h2 id="06380fb607958af6dbecb617ce31f2cd"></h2>


## mysql 记录 未使用 index的查询

```
set global log_queries_not_using_indexes=ON;
```

- those queries will appears in slow_log

<h2 id="005022c3c2f0c952bbd1532235bc4959"></h2>


## how to check whether mysql reuse the connection

- in `mysql.general_log` ,  if the connection is reused, you should see the `connection` event only at the very beginning


<h2 id="c4606a5312075cb8424b31a364e46848"></h2>


## restore database from dump file

```
mysql -uroot -ppwd  < dumpfile
```

<h2 id="c3b5d31eac469e51b08ec13a8edc866e"></h2>


## Create a `new_user` and Grant all privileges on db `db_test`

```mysql
CREATE USER 'new_user'@'%' IDENTIFIED BY 'new_user_pwd';
GRANT ALL PRIVILEGES  ON db_test.* TO 'new_user'@'%' WITH GRANT OPTION;
```


# Query Tips

<h2 id="c4935fa15c0a1305da238eec81cc54b3"></h2>


## `select count(*)` is very slow on large table

- Here's a cheap way to get an estimated row count:

```
> select TABLE_ROWS FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='your_db_name' and TABLE_NAME='your_table_name';
+------------+
| TABLE_ROWS |
+------------+
|      57889 |
+------------+
1 rows in set (0.00 sec)
``` 

<h2 id="5c7924ade1a946ba9a0af0cc562c127b"></h2>


## `select ... limit offset , n ` is slow when offset  is higher

- `limit offset ,n ` -> `where id > offset limit n` 
- Note:
    - `id` is the auto incr primary key , and should be continous (that is , you should NOT delete the rows )


<h2 id="7b83de8606257483382081d2e0e808de"></h2>


## use COALESCE to return a default value if select get no result

COALESCE returns 1st non-NULL value

```
select COALESCE(AVG(distance), 0) as baseline from records where uuid=?
```

<h2 id="60df3279b8377ba6468528ab017f1dc0"></h2>


## Sub Query example

```mysql
select COALESCE( sum(orderAmount), 0 )  from payment_vivosdk   
where 
    uuid="test-User-0" and 
    paidtime >= ( select COALESCE( AVG(startTime), -1) from tbl_rechargeAcc where activity_kind = 2 and endTime > 969393337  ) and 
    paidtime <= ( select COALESCE( AVG(deadline),  -1) from tbl_rechargeAcc where activity_kind = 2 and endTime > 969393337  ) 
```

<h2 id="06eb0ebfd08b098bd2c0529968e05930"></h2>


## CASE ... WHEN ... ELSE... END

```mysql
    WHERE m.p1 = ? OR m.p2 = ?  ORDER by   CASE 
        when (m.p1=?) and ((withdraw&1)<>0) then match_id - 10000000
        when (m.p2=?) and ((withdraw&2)<>0) then match_id - 10000000
        ELSE  match_id END   DESC LIMIT 20
```



<h2 id="551a3f8ce4409963ec6de228ccc44ae0"></h2>


## Convert a timestamp to seconds(GMT)

不同时区的数据库，存放的date 受时区影响, UNIX_TIMESTAMP方法不是我们想要的...

```mysql
SELECT TIMESTAMPDIFF( SECOND, "1970-01-01 00:00:00" , "2020-05-01 12:05:55" );
```

<h2 id="6ada22780ed552c34465864a2648f7e9"></h2>


## 三元表达式

```mysql
... status=if(status="created","paid",status)
```

## Update RANK while doing query

- query , and return rank in query
    ```mysql
    select @rownum:=@rownum+1 as 'rank', uuid, rank_score
    from pvp_hsw, 
    (SELECT @rownum:=0) as r  -- Every derived table must have its own alias
    order by rank_score desc;
    ```
    - here `@rownum` will safely reset everytime

- update rank info while doing query
    ```mysql
    SET @rownum=0;
    ```
    ```mysql
    update pvp_hsw as p set week_rank=@rownum:=@rownum+1 order by rank_score desc;
    ```







