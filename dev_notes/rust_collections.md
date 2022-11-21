
# Common Collections in Rust


## Vector

```rust
    let mut v: Vec<i32> = Vec::new();
    v.push(1);

    let v2 = vec![1, 2, 3];
```

to access a vector element

```rust
    let third = &v2[2];
    println!("The third element is {}", third);
    // to prevent runtime error
    match v2.get(20) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }
```



