
# Understanding Ownership in Rust

## Ownership rules

1. Each value in Rust has a variable that's called its owner
2. There can only one owner at a time
    - ![](../imgs/rust_ownership.png)
3. When the owner goes out of scope, the value will be dropped


## Move / Borrow

- rust by default move the value
- reference borrowing won't take ownership
    ```rust
    let x = 5;
    let y = x; // a copy, not a move,
               // rust has a copy trait, simple type stored on stack implement this trait
    println!("x = {}, y = {}", x, y);
    let s1 = "hello"; // &str , reference don't take ownership
    let s2 = s1;
    println!("s1 = {}, s2 = {}", s1, s2);
    let s1 = String::from("hello");
    let s2 = s1; // moved, rust default move the value
    // println!("s1 = {}, s2 = {}", s1, s2);
    ```

## Reference

- reference don't take ownership
    - it points to NOT the underlying data, BUT the variable hold the data.
- immutable by default, to modify data via a refercence
    1. use mutable reference `&mut`
    2. the ownership need declared `mut` as well.
- you can only have 1 mutable reference to a particular piece of data in a particular scope.
    - to prevent data race
    ```rust
    let mut s1 = String::from("hello");
    let s2 = &mut s1;
    // compile error
    // second mutable borrow occurs here
    s1.push_str(", world!");
    s2.push_str(", world!");
    ```
- you can't have a mutable reference if an immutable reference already exsits
    ```rust
    let s1 = String::from("hello");
    let s2 = &mut s1;
    ```
- Summary: the rules of references
    1. At any given time, you can have either one mutable reference, or any number of immutable references.
        - Rust restricts *the classic read-write lock problem* at the compiler level.
            - ![](../imgs/rust_ownership3.0.webp)
            - ![](../imgs/rust_ownership3.webp)
    2. References must always be valid



## Slices

- slices let you reference a contiguous sequence of elements within a collection instead of referencing the entire collection.
- slices do NOT take ownership of the underlying data.

```rust
    let s1 = String::from("hello world");
    let hello = &s1[0..5]; // [..5]
    let world = &s1[6..11]; // [6..]
    println!("{} {}", hello, world);
```





