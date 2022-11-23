1. [rust cheat sheet](https://cheats.rs)
2. [rust crash course](./rust_crash.md)
3. [ownership](rust_ownership.md)
4. [module system](rust_modulesystem.md)
5. [error handling](rust_errorhandle.md)
6. [Traits (interface)](rust_trait.md)
7. [lifetime](rust_lifetime.md)

4. [rust & webasm](https://rustwasm.github.io/docs/book/introduction.html)
5. [Concurrency,Threads,Channel,Mutex,Arc](rust_thread_channels_mutex_arc.md)


----

<details>
<summary>
为rust crates.io换上国内中科大的源
</summary>


```
vi ~/.cargo/config

[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'ustc'
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```


</details>
