...menustart

 - [Redis Tips](#0ac68c6db10bb40156c1e107f2ee9b6d)
     - [原子  set key value if-not-exist with a TTL](#4d2bdd3a995b163e8e63264680b19443)

...menuend


<h2 id="0ac68c6db10bb40156c1e107f2ee9b6d"></h2>


# Redis Tips

<h2 id="4d2bdd3a995b163e8e63264680b19443"></h2>


## 原子  set key value if-not-exist with a TTL

```
SET resource_name my_random_value NX PX 30000
```

[基于Redis的分布式锁到底安全吗 1](http://zhangtielei.com/posts/blog-redlock-reasoning.html)

[基于Redis的分布式锁到底安全吗 2](http://zhangtielei.com/posts/blog-redlock-reasoning-part2.html)






