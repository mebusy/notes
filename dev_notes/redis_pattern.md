...menustart

- [Redis Pattern](#a5b4c19e70e61f566f31c53accbd1c87)
    - [Keys](#a73e6bf278578e09d2351ee2ec7a7908)
        - [EXPIRE , v1.0.0 , O(1)](#a72f2c26fd355ef83497de8e838b3e23)
        - [SORT , v1.0.0 , O(N+M\*log(M))](#fba9c599e38bf301aa2005693afa1c17)
    - [List](#4ee29ca12c7d126654bd0e5275de6135)
        - [BLPOP , v2.0.0 , O(1)](#3dab2c2334bb53fcc9b1a5f000495360)
        - [BRPOPLPUSH , v2.2.0 , O(1)](#314a88a641bd4a0453876f35c9af0aa1)
        - [RPOPLPUSH  , v1.2.0 , O(1)](#174f672c6a017d00004be8084bb99809)
    - [Sorted Set](#cb571dbc7e0313fceb81c293e56309ed)
        - [ZRANGEBYSCORE , v1.0.5 , O(log(N)+M)](#dcfe38818d271e9c65946619ed7deb91)
    - [String](#27118326006d3829667a400ad23d5d98)
        - [BITCOUNT  , v2.6.0 , O(N)](#3b950dfa0475448afdb8f212e7732e0b)
        - [GETSET  , v1.0.0 , O(1)](#57df48b0f3178704f8d6036cb0a9fe66)
        - [INCR  , v1.0.0 , O(1)](#2636c2e9ec390f0f737676e73c0b4441)
        - [Set , v1.0.0, O(1)](#3c868a38311e6698d08e4ccaa2c11bac)
        - [SETNX , v1.0.0 , O(1)](#c9738322a8437944c4b74f1eb064873f)
            - [Handling deadlocks](#901c539d7f5fac2508bc71eccf55e1e7)
        - [SETRANGE , v2.2.0 , O(1)](#ae634f943bf692d0391216701a2d591a)

...menuend


<h2 id="a5b4c19e70e61f566f31c53accbd1c87"></h2>


# Redis Pattern

<h2 id="a73e6bf278578e09d2351ee2ec7a7908"></h2>


## Keys

<h2 id="a72f2c26fd355ef83497de8e838b3e23"></h2>


### EXPIRE , v1.0.0 , O(1)
 - `EXPIRE key seconds`  
 - Pattern: Navigation session
 - Imagine you have a web service and you are interested in the latest N pages recently visited by your users, such that each adjacent page view was not performed more than 60 seconds after the previous. 
    - 这些信息可能是该用户当前感兴趣的， 你可以根据这个列表 向他推荐商品。

```
MULTI
RPUSH pagewviews.user:<userid> http://.....
EXPIRE pagewviews.user:<userid> 60
EXEC
```

<h2 id="fba9c599e38bf301aa2005693afa1c17"></h2>


### SORT , v1.0.0 , O(N+M\*log(M)) 

 - `SORT key [BY pattern] [LIMIT offset count] [GET pattern [GET pattern ...]] [ASC|DESC] [ALPHA] [STORE destination]` 
    - BY 的操作对象可以是 key， 也可以是 hash 中的 field
 - Pattern: SORT ... STORE
 - An interesting pattern using SORT ... STORE consists in associating an **EXPIRE** timeout to the resulting key
    - so that in applications where the result of a SORT operation can be cached for some time.
    - Other clients will use the cached list instead of calling SORT for every request.
    - Note that for correctly implementing this pattern it is important to avoid multiple clients rebuilding the cache at the same time. Some kind of locking is needed here (for instance using **SETNX**).


<h2 id="4ee29ca12c7d126654bd0e5275de6135"></h2>


## List

<h2 id="3dab2c2334bb53fcc9b1a5f000495360"></h2>


### BLPOP , v2.0.0 , O(1)

 - `BLPOP key [key ...] timeout`
 - Pattern: Event notification
 - For some application you may need to block waiting for elements into a Redis Set, so that as far as a new element is added to the Set, it is possible to retrieve it without resort to polling. 
    - 这需要一个阻塞版本的**SPOP**, 目前没有这个命令
    - 但是使用 blocking list operations 可以轻松实现这个

```
// for consumer
LOOP forever
    WHILE SPOP(key) returns elements
        ... process elements ...
    END
    BRPOP helper_key
END
```

```
// producer
MULTI
SADD key element
LPUSH helper_key x
EXEC
```

<h2 id="314a88a641bd4a0453876f35c9af0aa1"></h2>


### BRPOPLPUSH , v2.2.0 , O(1)

 - `BRPOPLPUSH source destination timeout`
    - When source contains elements, this command behaves exactly like RPOPLPUSH. 
    - When used inside a MULTI/EXEC block, this command behaves exactly like RPOPLPUSH. 
    - When source is empty, Redis will block the connection until another client pushes to it or until timeout is reached.
 - Pattern: Reliable queue
    - 见 RPOPLPUSH 
 - Pattern: Circular list
    - RPOPLPUSH 


<h2 id="174f672c6a017d00004be8084bb99809"></h2>


### RPOPLPUSH  , v1.2.0 , O(1)

 - `RPOPLPUSH source destination` 
    - Atomically returns and removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at destination.
 - Pattern: Reliable queue
    - Redis is often used as a messaging server.
        - A simple form of queue is often obtained pushing values into a list in the producer side, and waiting for this values in the consumer side.
    - However in this context the obtained queue is not *reliable* as messages can be lost, for example in the case there is a network problem or if the consumer crashes just after the message is received but it is still to process.
    - RPOPLPUSH (or BRPOPLPUSH for the blocking variant) offers a way to avoid this problem: 
        - the consumer fetches the message and at the same time pushes it into a processing list. 
        - It will use the LREM command in order to remove the message from the processing list once the message has been processed.
        - An additional client may monitor the processing list for items that remain there for too much time, and will push those timed out items into the queue again if needed.
 - Pattern: Circular list
    - Using RPOPLPUSH with the same source and destination key, 
    - a client can visit all the elements of an N-elements list, one after the other, in O(N) without transferring the full list from the server to the client using a single LRANGE operation.
    - The above pattern works even if the following two conditions:
        - There are multiple clients rotating the list: they'll fetch different elements, until all the elements of the list are visited, and the process restarts.
        - Even if other clients are actively pushing new items at the end of the list.
    - The above makes it very simple to implement a system where a set of items must be processed by N workers continuously as fast as possible. 
        - An example is a monitoring system that must check that a set of web sites are reachable, with the smallest delay possible, using a number of parallel workers.
    - 这种实现很容易扩展且可靠，因为即使消息丢失，该项目仍然在队列中，并将在下一次迭代时处理。


<h2 id="cb571dbc7e0313fceb81c293e56309ed"></h2>


## Sorted Set

<h2 id="dcfe38818d271e9c65946619ed7deb91"></h2>


### ZRANGEBYSCORE , v1.0.5 , O(log(N)+M) 

 - `ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]`
 - Pattern: weighted random selection of an element
    - a common problem when implementing Markov chains and other algorithms is to select an element at random from a set,  but different elements may have different weights that change how likely it is they are picked.

```
RANDOM_ELE = ZRANGEBYSCORE key RAND() +inf LIMIT 0 1
```

<h2 id="27118326006d3829667a400ad23d5d98"></h2>


## String

<h2 id="3b950dfa0475448afdb8f212e7732e0b"></h2>


### BITCOUNT  , v2.6.0 , O(N)

 - `BITCOUNT key [start end]`
 - Pattern: real-time metrics using bitmaps

<h2 id="57df48b0f3178704f8d6036cb0a9fe66"></h2>


### GETSET  , v1.0.0 , O(1)

 - `GETSET key value`
 - Design pattern
    - GETSET can be used together with INCR for counting with atomic reset. 
    - For example: a process may call INCR every time some event occurs, but from sometimes we need to get the value of the counter and reset it to zero atomically. 

```
redis> INCR mycounter
(integer) 1
redis> GETSET mycounter "0"
"1"
redis> GET mycounter
"0"
redis>
```


<h2 id="2636c2e9ec390f0f737676e73c0b4441"></h2>


### INCR  , v1.0.0 , O(1)

 - `INCR key`
 - Pattern: Counter
 - Pattern: Rate limiter


<h2 id="3c868a38311e6698d08e4ccaa2c11bac"></h2>


### Set , v1.0.0, O(1)

 - `SET key value [expiration EX seconds|PX milliseconds] [NX|XX]`
 - Patterns
    - The command `SET resource-name anystring NX EX max-lock-time` is a simple way to implement a locking system with Redis.
        - A client can acquire the lock if the above command returns OK (or retry after some time if the command returns Nil) 
        - and remove the lock just using DEL.
        - The lock will be auto-released after the expire time is reached.
    - It is possible to make this system more robust modifying the unlock schema as follows:
        - Instead of setting a fixed string, set a non-guessable large random string, called token.
        - Instead of releasing the lock with DEL, send a script that only removes the key if the value matches.
            - **This avoids that a client will try to release the lock after the expire time deleting the key created by another client that acquired the lock later.**
            - An example of unlock script would be similar to the following:

```
if redis.call("get",KEYS[1]) == ARGV[1]
then
    return redis.call("del",KEYS[1])
else
    return 0
end
```


<h2 id="c9738322a8437944c4b74f1eb064873f"></h2>


### SETNX , v1.0.0 , O(1)

 - `SETNX key value`
 - Design pattern: Locking with SETNX
 - For example, to acquire the lock of the key foo, the client could try the following:

```
SETNX lock.foo <current Unix time + lock timeout + 1>
```

 - If SETNX returns 1 the client acquired the lock, setting the lock.foo key to the Unix time at which the lock should no longer be considered valid. 
    - The client will later use DEL lock.foo in order to release the lock.
 - If SETNX returns 0 the key is already locked by some other client. 

<h2 id="901c539d7f5fac2508bc71eccf55e1e7"></h2>


#### Handling deadlocks

 - In the above locking algorithm there is a problem: 
    - what happens if a client fails, crashes, or is otherwise not able to release the lock? 
 - It's possible to detect this condition because the lock key contains a UNIX timestamp.
 - When this happens we can't just call DEL against the key to remove the lock and then try to issue a SETNX, 
    - as there is a race condition here, when multiple clients detected an expired lock and are trying to release it.
        - C1 and C2 read lock.foo to check the timestamp, because they both received 0 after executing SETNX, as the lock is still held by C3 that crashed after holding the lock.
        - C1 sends DEL lock.foo
        - C1 sends SETNX lock.foo and it succeeds
        - C2 sends DEL lock.foo
        - C2 sends SETNX lock.foo and it succeeds
        - ERROR: both C1 and C2 acquired the lock because of the race condition.
    - Fortunately, it's possible to avoid this issue using the following algorithm.  Let's see how C4, our sane client, uses the good algorithm:
        - C4 sends SETNX lock.foo in order to acquire the lock 
        - The crashed client C3 still holds it, so Redis will reply with 0 to C4.
        - C4 sends GET lock.foo to check if the lock expired. If it is not, it will sleep for some time and retry from the start.
        - Instead, if the lock is expired because the Unix time at lock.foo is older than the current Unix time, C4 tries to perform:
            - `GETSET lock.foo <current Unix timestamp + lock timeout + 1>`
        - Because of the GETSET semantic, C4 can check if the old value stored at key is still an expired timestamp. If it is, the lock was acquired.
        - If another client, for instance C5, was faster than C4 and acquired the lock with the GETSET operation, the C4 GETSET operation will return a non expired timestamp. C4 will simply restart from the first step.Note that even if C4 set the key a bit a few seconds in the future this is not a problem.
 - In order to make this locking algorithm more robust, a client holding a lock should always check the timeout didn't expire before unlocking the key with DEL 
    - because client failures can be complex, not just crashing but also blocking a lot of time against some operations and trying to issue DEL after a lot of time (when the LOCK is already held by another client).


<h2 id="ae634f943bf692d0391216701a2d591a"></h2>


### SETRANGE , v2.2.0 , O(1)

 - `SETRANGE key offset value`
 - Patterns
    - Thanks to SETRANGE and the analogous GETRANGE commands, you can use Redis strings as a linear array with O(1) random access.
    - This is a very fast and efficient storage in many real world use cases.

```
Basic usage:

redis> SET key1 "Hello World"
"OK"
redis> SETRANGE key1 6 "Redis"
(integer) 11
redis> GET key1
"Hello Redis"
redis>
Example of zero padding:

redis> SETRANGE key2 6 "Redis"
(integer) 11
redis> GET key2
"\u0000\u0000\u0000\u0000\u0000\u0000Redis"
redis>
```


