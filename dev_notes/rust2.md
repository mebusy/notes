...menustart

 - [5. Using Structs to Structure Related Data](#49a443e49b3428f71dc00fddc2d659c4)
     - [5.1 Defining and Instantiating Structs](#3128feda0fe9d177871815f05dbb661a)
         - [Using the Field Init Shorthand when Variables and Fields Have the Same Name](#f0753757bb933212e620a7794f6469fd)
         - [Creating Instances From Other Instances With Struct Update Syntax](#24960bada8bbf0d9a5c39de5135ff239)
         - [Tuple Structs without Named Fields to Create Different Types](#1779a3699512e1d557bd24974645a7c2)
         - [Unit-Like Structs without Any Fields](#c7202a4116975ab1109a8e7db1df1108)
         - [Ownership of Struct Data](#0ebbec0168c436ab46ac83f8ab552c7a)
     - [5.2 An Example Program Using Structs](#b5e7437d476bfb974ba61a1f94fa1ed7)
     - [5.3 Method Syntax](#71e159f6b1af9a93f012817af67f5e02)
         - [Defining Methods](#13717147c0d0073a4c1bbcb91d21cd1c)
         - [Methods with More Parameters](#1ec178468e7808ee8c910d46fb6dc46c)
         - [Associated Functions](#c68e21e14fe90054ac00331d0be925cd)
         - [Multiple impl Blocks](#48eeb3737079e5ad6ee4b5cad613071c)
 - [6. Enums and Pattern Matching](#a38637e7381ef21dfe3360b05080ce0a)
     - [6.1 Defining an Enum](#fdad361153c038e64a843eb25389b74d)
         - [Enum Values](#c5346465419d51659c616961d763d8c3)
         - [The Option Enum and Its Advantages Over Null Values](#64218f717df4167ce75371e5c2d61866)

...menuend


<h2 id="49a443e49b3428f71dc00fddc2d659c4"></h2>

-----
-----

# 5. Using Structs to Structure Related Data 

 - struct and enum concepts are the building blocks for creating new types in your program’s domain ,
    - to take full advantage of Rust’s compile time type checking.

<h2 id="3128feda0fe9d177871815f05dbb661a"></h2>

-----

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


<h2 id="f0753757bb933212e620a7794f6469fd"></h2>

-----

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

<h2 id="24960bada8bbf0d9a5c39de5135ff239"></h2>

-----

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

<h2 id="1779a3699512e1d557bd24974645a7c2"></h2>

-----

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

<h2 id="c7202a4116975ab1109a8e7db1df1108"></h2>

-----

### Unit-Like Structs without Any Fields

 - We can also define structs that don’t have any fields!
    - golang 中的 空struct
 - These are called *unit-like structs* since they behave similarly to () , the unit type.
    - `struct XXX;` ?
 - Unit-like structs can be useful in situations such as when you need to implement a trait on some type, but you don’t have any data that you want to store in the type itself.

<h2 id="0ebbec0168c436ab46ac83f8ab552c7a"></h2>

-----

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

<h2 id="b5e7437d476bfb974ba61a1f94fa1ed7"></h2>

-----

## 5.2 An Example Program Using Structs

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

<h2 id="71e159f6b1af9a93f012817af67f5e02"></h2>

-----

## 5.3 Method Syntax

 - Methods defined within the context of a struct 
    - or an enum
    - or a trait object
 - their first parameter is always `self`

<h2 id="13717147c0d0073a4c1bbcb91d21cd1c"></h2>

-----

### Defining Methods

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    println!( "The area of the rectangle is {} square pixels.", 
        rect1.area());
}
```

 - Where’s the `->` Operator?
    - In C++ , if object is a pointer, `object->something() is similar to (*object).something()`
 - Rust doesn’t have an equivalent to the `->` operator
    - Rust has a feature called automatic *referencing and dereferencing*
    - when you call a method with object.something(), Rust automatically adds in &, &mut, or * so object matches the signature of the method.
    - In other words, the following are the same:
        - `p1.distance(&p2); <==>  (&p1).distance(&p2);`

<h2 id="1ec178468e7808ee8c910d46fb6dc46c"></h2>

-----

### Methods with More Parameters

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

<h2 id="c68e21e14fe90054ac00331d0be925cd"></h2>

-----

### Associated Functions

 - we’re allowed to define functions within `impl` blocks that don’t take self as a parameter.
 - These are called *associated functions*  because they’re associated with the struct. 
    - They’re still functions, not methods 
    - You’ve already used the String::from associated function.
 - Associated functions are often used for constructors that will return a new instance of the struct.
    - 工场模式返回实例，和 golang一样

```rust
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle { width: size, height: size }
    }
}

...
let sq = Rectangle::square(3);
```

<h2 id="48eeb3737079e5ad6ee4b5cad613071c"></h2>

-----

### Multiple impl Blocks

 - Each struct is allowed to have multiple `impl` blocks

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

---

<h2 id="a38637e7381ef21dfe3360b05080ce0a"></h2>

-----
-----

# 6. Enums and Pattern Matching

 - Enums allow you to define a type by enumerating its possible values
 - Rust’s enums are most similar to algebraic data types in functional languages like F#, OCaml, and Haskell.

<h2 id="fdad361153c038e64a843eb25389b74d"></h2>

-----

## 6.1 Defining an Enum

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

 - IpAddrKind is now a custom data type that we can use elsewhere in our code.

<h2 id="c5346465419d51659c616961d763d8c3"></h2>

-----

### Enum Values

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;

fn route(ip_type: IpAddrKind) { }

route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

 - we can use an enum as part of a struct by putting data directly into each enum variant.

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));
let loopback = IpAddr::V6(String::from("::1"));
```

 - each variant can have different types and amounts of associated data. 
 - 每个 variant 可以看作一个结构体?

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```

 - enum variant can have struct as well

```rust
struct Ipv4Addr {
    // details elided
}

struct Ipv6Addr {
    // details elided
}

enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

 - message example

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

 - just like struct,  we’re also able to define methods on enums.

```rust
impl Message {
    fn call(&self) {
        // method body would be defined here
    }
}
let m = Message::Write(String::from("hello"));
m.call();
```

<h2 id="64218f717df4167ce75371e5c2d61866"></h2>

-----

### The Option Enum and Its Advantages Over Null Values



