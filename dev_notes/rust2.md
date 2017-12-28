...menustart

 - [5. Using Structs to Structure Related Data](#49a443e49b3428f71dc00fddc2d659c4)
     - [5.1 Defining and Instantiating Structs](#3128feda0fe9d177871815f05dbb661a)

...menuend


<h2 id="49a443e49b3428f71dc00fddc2d659c4"></h2>

# 5. Using Structs to Structure Related Data 

 - struct and enum concepts are the building blocks for creating new types in your program’s domain ,
    - to take full advantage of Rust’s compile time type checking.

<h2 id="3128feda0fe9d177871815f05dbb661a"></h2>

## 5.1 Defining and Instantiating Structs 

 - Structs are similar to tuples
 - the pieces of a struct can be different types.
 - Unlike tuples, we name each piece of data so it’s clear what the values mean

```rust
// define
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

// Creating an instance 
let user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};

// access
user1.email = String::from("anotheremail@example.com");
```


