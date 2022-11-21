
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


## String


- Primitive str 
    - Immutable fixed-length string somewhere in memory
    ```rust
    let hello = "Hello";
    ```
- String
    - Growable, heap-allocated data structure -- Use when you need to modify or own string data
    ```rust
    let mut hello = String::from( "Hello" );
    ```
- String slice
    - a view into another string
    ```rust 
    let s1 = String::from("hello world");
    let hello = &s1[..5]; // :&str
    ```

### Concat String

```rust
    let mut s = String::from("foo");
    s.push_str("bar");
    s.push('!');
    // foobar!

    let s1 = String::from("hello");
    let s2 = String::from("world");

    let s3 = format!("{}-{}", s1, s2);
    let s3 = s1 + &s2; // s1 has been moved here and can no longer be used

    // hello world
```


### Get String Character


```rust
    let hello = String::from("世界杯决赛");
    // compile error, String are utf8 encoding
    // let c: char = hello[0];

    for b in hello.bytes() {
        println!("{}", b);
    }

    for c in hello.chars() {
        println!("{}", c);
    }
```


## Hash

```rust
use std::collections::HashMap;
```

```rust
    let mut hm = HashMap::new();
    hm.insert( "key1", "haha" );

    for (k,v) in &hm {
        println!( "{}: {}", k,v );
    }
    println!( "{:?}", hm );

    match hm.get( "key1" ) {
        Some(n) => println!("{}", n),
        _ => println!("no match"),
    }

    hm.remove("key1");
```
