1. [rust cheat sheet](https://cheats.rs)
2. [learnRustInYMintues](./learnRustInYMintues.md)
2. [rust](./rust2.md)
3. [rust & webasm](https://rustwasm.github.io/docs/book/introduction.html)



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
