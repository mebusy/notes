1. [rust cheat sheet](https://cheats.rs)
2. [learnRustInYMintues](./learnRustInYMintues.md)
2. [rust crash course](./rust_crash.md)
3. [rust & webasm](https://rustwasm.github.io/docs/book/introduction.html)
4. [Concurrency,Threads,Channel,Mutex,Arc](rust_thread_channels_mutex_arc.md)



----

- 为rust crates.io换上国内中科大的源

```
vi ~/.cargo/config

[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'ustc'
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```
