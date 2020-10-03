...menustart

- [Redis Tips](#0ac68c6db10bb40156c1e107f2ee9b6d)
    - [Redis 分布式锁](#4f37e290c426fcf9f61d3e6dca17a4e1)

...menuend


<h2 id="0ac68c6db10bb40156c1e107f2ee9b6d"></h2>


# Redis Tips

<h2 id="4f37e290c426fcf9f61d3e6dca17a4e1"></h2>


## Redis 分布式锁

- v3.1
    - `SET resource_name my_random_value NX PX 30`

```redis
tryLock(){  
    SET Key UniqId Seconds
}
release(){  
    EVAL(
      //LuaScript
      if redis.call("get",KEYS[1]) == ARGV[1] then
          return redis.call("del",KEYS[1])
      else
          return 0
      end
    )
}
```

- Redis 2.6.12后SET同样提供了一个NX参数，等同于SETNX命令，官方文档上提醒后面的版本有可能去掉SETNX, SETEX, PSETEX,并用SET命令代替，另外一个优化是使用一个自增的唯一UniqId代替时间戳来规避V3.0提到的时钟问题。
- 这个方案是目前最优的分布式锁方案，但是如果在Redis集群环境下依然存在问题：
    - 由于Redis集群数据同步为异步，假设在Master节点获取到锁后未完成数据同步情况下Master节点crash，此时在新的Master节点依然可以获取锁，所以多个Client同时获取到了锁


[Redis 分布式锁进化史解读+缺陷分析](https://cloud.tencent.com/developer/article/1399696)


