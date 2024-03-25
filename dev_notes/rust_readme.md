1. best learning materials
    - [rust cheat sheet](https://cheats.rs)
    - [rust by example](https://doc.rust-lang.org/rust-by-example/flow_control/if_let.html)
    - [rust-lang/rustlings](https://github.com/rust-lang/rustlings)
2. [rust crash course](./rust_crash.md)
3. [ownership](rust_ownership.md) | [move,copy,clone](rust_move_copy_clone.md)
4. [module system](rust_modulesystem.md)
5. [error handling](rust_errorhandle.md)
6. [Traits (interface)](rust_trait.md)
7. [lifetime](rust_lifetime.md)
8. [smart pointer](rust_smartpoint.md)
9. [concurrency,threads,channel,mutex,arc](rust_concurrency.md)
10. [rust collections](rust_collections.md)
11. [rust for cpp user](rust_4_cppuser.md)

20. [rust & webasm](https://rustwasm.github.io/docs/book/introduction.html)


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


<h2 id="fa3ba5bbd902b187a92e4b988f12b29d"></h2>

# some go concept VS. in rust

concept | rust implementation
--- | ---
parallelism |  [rayon](https://docs.rs/rayon/latest/rayon/)
Concurrency |  [async/await](https://blog.ediri.io/how-to-asyncawait-in-rust-an-introduction)
Channel  | Rust allows you to transfer a pointer from one thread to another to avoid racing conditions for resources. Through passing pointers, Rust can enforce thread isolation for channels:  [fearless concurrency](https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html)
Lock | Data is only accessible when the lock is held. [fearless concurrency](https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html)


