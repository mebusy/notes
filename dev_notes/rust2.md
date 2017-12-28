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
// similar as in golang
let mut user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};

// access
user1.email = String::from("anotheremail@example.com");
```

 - Note that in order to change some field in user1 , the entire instance must be mutable
    - Rust doesn’t allow us to mark only certain fields as mutable. 
 - as with any expression, we can construct a new instance of the struct as the last expression in the function body to implicitly return that new instance.

```rust
fn build_user(email: String, username: String) -> User {
    User {
        email: email,
        username: username,
        active: true,
        sign_in_count: 1,
    }
}
```

 - It makes sense to name the function arguments with the same name as the struct fields
    - `email` , `username` above
 - but having to repeat the email and username field names and variables is a bit tedious


### Using the Field Init Shorthand when Variables and Fields Have the Same Name

 - Because the parameter names and the struct field names are exactly the same in previous example
 - we can use the *field init shorthand syntax* to rewrite build_user

```rust
fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
```

### Creating Instances From Other Instances With Struct Update Syntax

 - It’s often useful to create a new instance of a struct that uses most of an old instance’s values , but changes some
 - We do this using *struct update syntax*.

 - `..` specifies that the remaining fields not explicitly set should have the same value as the fields in the given instance.

```rust
let user2 = User {
    email: String::from("another@example.com"),
    username: String::from("anotherusername567"),
    ..user1
};
```

### Tuple Structs without Named Fields to Create Different Types

 - We can also define structs that look similar to tuples, called *tuple structs*
    - golang 也有

```rust
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);

println!( "y={}" , origin.2 );

// 注意这里和 tuple destruct的不同
let Point(x,y,z) = origin ;
println!( "{},{},{}" , x,y,z );
```

 - tuple struct instances behave like tuples
    - you can destructure them into their individual pieces 
    - you can use a `.` followed by the index to access an individual value, and so on

### Unit-Like Structs without Any Fields

 - We can also define structs that don’t have any fields!
    - golang 中的 空struct
 - These are called *unit-like structs* since they behave similarly to () , the unit type.
 - Unit-like structs can be useful in situations such as when you need to implement a trait on some type, but you don’t have any data that you want to store in the type itself.

### Ownership of Struct Data

 - In the `User` struct definition , we used the owned `String` type rather than the `&str` string slice type.
 - This is a deliberate choice because we want instances of this struct 
    - to own all of its data and 
    - for that data to be valid for as long as the entire struct is valid
 - It’s possible for structs to store references to data owned by something else , but
    - to do so requires the use of *lifetimes* ,  a Rust feature.
 - Lifetimes ensure that the data referenced by a struct is valid for as long as the struct is.
 - Let’s say you try to store a reference in a struct without specifying lifetimes, like this:

```rust
struct User {
    username: &str, // expected lifetime parameter 
    email: &str,    // expected lifetime parameter
    sign_in_count: u64,
    active: bool,
}

fn main() {
    let user1 = User {
        email: "someone@example.com",
        username: "someusername123",
        active: true,
        sign_in_count: 1,
    };
}
```

 - The compiler will complain that it needs lifetime specifiers
 - We’ll discuss how to fix these errors so you can store references in structs in Chapter 10

## An Example Program Using Structs

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    // error[E0277]: the trait bound `Rectangle: std::fmt::Display` is not satisfied
    println!("rect1 is {}", rect1);
}
```

 - The `println!`  macro can do many kinds of formatting
    - and by default, {} tells println! to use formatting known as `Display: output` intended for direct end user consumption.
 - If we continue reading the errors, we’ll find this helpful note:

```bash
note: `Rectangle` cannot be formatted with the default formatter; try using `:?` instead if you are using a format string
```

 - Rust does include functionality to print out debugging information, but we have to explicitly opt-in to make that functionality available for our struct. 
    - To do that, we add the annotation `#[derive(Debug)]` just before the struct definition

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    println!("rect1 is {:?}", rect1);
}
// rect1 is Rectangle { width: 30, height: 50 }
```

 - we can use `{:#?}` instead of `{:?}` in the println! string.

```bash
rect1 is Rectangle {
    width: 30,
    height: 50
}
```

## Method Syntax



