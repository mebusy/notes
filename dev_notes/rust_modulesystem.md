
# Rust's Module System Explained!

- Rust has a module system, that starts with a package, (when `cargo new` you create a new package), a package stores crates. 
    - a crate could either be a binary crate or a library crate.  crates contain modules.
    - modules allow you to organize a chunk of code and control the privacy rules.


## Crates

- rust follows the convention that if you have `main.cs` defined in your source directory, then a binary crate with the same name as your package will be automatically created.
    - and the `main.rs` will be the crate root.
- and there's also a similar convention for library crate, if the `lib.rs` was found, then rust will automatically create a library crate with the same name as your package.
- so even though we don't have any crates defined in `cargo.toml`, our package may actually have 2 crates.


### Some Crate Rules

1. a package must have at least one crate.
2. a package could have either 0 or 1 library crate.
3. a package could have any number of binary crates.
    - if we want multiple binary crate, we would create a folder called `bin`, and in this folder we can add another file. and each file in this folder will represent another binary crate.
- lastly, a package could have any number binary crates,


## Modules

> you can create a module with or without inline body.

> A module without a body is loaded from an external file. When the module does not have a path attribute, the path to the file mirrors the logical module path. 


- Each file in Rust (besides main.rs or lib.rs) corresponds to one module in a crate (main.rs and lib.rs are the crate's root). 
- To create a module, you add this line to its parent module (or to lib.rs or main.rs, which makes it a submodule under the crate)
    ```rust
    mod somemod;
    ```
- Then, you have 2 options:
    1. Add a file called `somemod.rs` in the same folder as the file where you put that `mod somemod;` declaration. 
        ```bash
        |
        +---main.rs
        +---somemod.rs
        +---somemod  # you can have sub module
            |
            +---anothermod.rs
        ```
    2. or add a folder called `somemod` in the same folder as the file with the `mod somemod;` declaration. 
        > Prior to rustc 1.30, using mod.rs files was the way to load a module with nested children
        ```bash
        |
        +---main.rs
        +---somemod
            |
            +---mod.rs
        ```

---

<details>
<summary>
Most Simple Module
</summary>

```rust
// print.rs
pub fn run() {
    println!("Hello from print.rs file");
}
```

```rust
// main.rs
mod print; // mod without body, load it from print.rs

fn main() {
    print::run();    
}
```

</details>


<details>
<summary>
Module Prior to rustc 1.30
</summary>


```bash
├── libs
│   └── mod.rs
├── main.rs
```

```rust
// libs/mod.rs
pub mod extra_mod { // module has body
    pub fn libs_extra_mod() {
        println!("libs/extramod");
    }
}
```

```rust
// main.rs
#![allow(unused)]

mod libs;
use libs::extra_mod;

fn main() {
    extra_mod::libs_extra_mod();
}
```

</details>


<details>
<summary>
Module use the new naming convention
</summary>

```bash
.
├── libs
│   └── somemod.rs
├── libs.rs
└── main.rs
```

```rust
// main.rs
#![allow(unused)]

mod libs;

use libs::somemod::extra_mod;

fn main() {
    libs::somemod::run();
    extra_mod::libs_extra_mod()
}
```

```rust
// libs.rs
pub mod somemod;
```

```rust
// libs/somemod.rs 
pub mod extra_mod {
    pub fn libs_extra_mod() {
        println!("libs/extramod");
    }
}

pub fn run() {
    println!("libs/somemod");
}
```


</details>




