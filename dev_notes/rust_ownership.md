[](...menustart)

- [Understanding Ownership in Rust](#e2a8efc0b9843be08e5a98bd4643972c)
    - [Ownership rules](#e8d1ae0e7d33cb31e8ff0b54bc904f86)
    - [Move / Borrow](#3260e15ab0b0472a8c60fe10dc282a51)
    - [Reference](#63d5049791d9d79d86e9a108b0a999ca)
    - [Slices](#ebb25066940285a0271542b54f76e9e1)

[](...menuend)


<h2 id="e2a8efc0b9843be08e5a98bd4643972c"></h2>

# Understanding Ownership in Rust

<h2 id="e8d1ae0e7d33cb31e8ff0b54bc904f86"></h2>

## Ownership rules

1. Each value in Rust has a variable that's called its owner
2. There can only one owner at a time
    - ![](../imgs/rust_ownership.png)
3. When the owner goes out of scope, the value will be dropped


<h2 id="3260e15ab0b0472a8c60fe10dc282a51"></h2>

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

    // E: borrow of moved value: `s1` value borrowed here after move 
    println!("s1 = {}, s2 = {}", s1, s2); 
    ```

<h2 id="63d5049791d9d79d86e9a108b0a999ca"></h2>

## Reference

- reference don't take ownership
    - it points to NOT the underlying data, BUT the **variable** hold the data.
- **The References**
    1. At any given time, you can have either one mutable reference, or any number of immutable references.
        - Rust restricts *the classic read-write lock problem* at the compiler level:  读锁可以有很多个，但 写锁 具有排他性
        - <img src="../imgs/rust_ownership3.0.webp" width=320 />
        ```rust
            let s1 = String::from("hello");
            let s2 = &s1;
            let s3 = &s1;
            println!("s1: {}, s2: {}, s3: {}", s1, s2, s3);  // s1: hello, s2: hello, s3: hello
        ```
        - <img src="../imgs/rust_ownership3.webp" width=320 />
        - a. To modify data via a refercence, we must use mutable reference `&mut`, and **ownership** itself need declared `mut` as well.
            ```rust
                let mut s1 = String::from("hello");
                let s2 = &mut s1;
                s2.push_str(", world"); 
                print!("{}", s2);  // hello, world
            ```
            - in this case, when s2 is writting, even owner can NOT read the data.
            ```rust
                let mut s1 = String::from("hello");
                let s2 = &mut s1;
                s2.push_str(", world");
                print!("{} {}", s1, s2); // E: cannot borrow `s1` as immutable because...
            ```
        - b. you can't have a mutable reference if an immutable reference already exsits
            ```rust
                let mut s1 = String::from("hello");
                let s3 = &s1;
                let s2 = &mut s1;
                print!("{}", s3);  // immutable borrow occurs here
            ```
    2. References must always be valid
        - which means we can not create a reference to the variable that got dropped or does not exist.
            ```rust
            let s1 = String::from("hello");
            let s2 = s1; // moved, s1 is no longer valid
            let s3 = &s1; // E: borrow of moved value: `s1` value borrowed here after move
            ```

<h2 id="ebb25066940285a0271542b54f76e9e1"></h2>

## Slices: a different kind of reference

- slices let you reference a contiguous sequence of elements within a collection instead of referencing the entire collection.
- slices do NOT take ownership of the underlying data.

```rust
    let s1 = String::from("hello world");
    let hello = &s1[0..5]; // [..5]
    let world = &s1[6..11]; // [6..]
    println!("{} {}", hello, world);
```

- Rust's borrow checker can't understand that we're borrowing different parts of the slice; it only knows that we're borrowing from the same slice twice. Borrowing different parts of a slice is fundamentally okay because the two slices aren't overlapping, but Rust isn't smart enough to know this.
