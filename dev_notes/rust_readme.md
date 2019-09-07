
1.[learnRustInYMintues](./learnRustInYMintues.md)



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
