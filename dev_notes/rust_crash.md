[](...menustart)

- [Rust Crash Course](#c5822cd18f83072f8602e5235e1b7ed5)
    - [Variable](#47c14840d8e15331fa420b9b2f757cd9)
    - [Primitive Data Types](#6c1067528b82c9144a62fb1dd2cd925e)
        - [Scalar Types](#09d9982852d86c2479924a4e3b723b1e)
        - [Compound Types](#9e57b6b46532794638212df8e239adde)
    - [Strings](#89be9433646f5939040a78971a5d103a)
    - [Vectors](#b3f69e461542074d9696ee29ded180a0)
    - [Flows](#c647c38e64bd84c0fe9fe165f3fff0eb)
    - [Functions](#e93acb146e114b5dfa6ce2d12dcb96e4)
    - [Structs](#6293f87533836e1d190c7b144ee25975)
        - [Struct which has functions](#9a6a7f4d3eff618bae767bf2afefc00e)
    - [Enums](#1b22e7dc709b52f1767fe1eb5dc56625)
        - [Option](#aaee770340310065a9498e2788783098)
    - [Hash](#fae8a9257e154175da4193dbf6552ef6)
    - [CLI](#91af5705f16502125e8b2187e64202c0)
    - [Trait](#9118ea0f76d0a8f21a42591caeee043e)
        - [Debug Trait](#8c24bd362f72757a4105edc427912b83)
        - [Display Trait](#ea5b3400b3db3c5423190c549a3139c0)
        - [Clone](#ff24590464659ee8cdec688128c35f89)
        - [Copy](#5fb63579fc981698f97d55bfecb213ea)
    - [Generic](#8045a0a6c688b0635e3caccc408a1446)
    - [Lifetime](#1a10be3692cec335c74387f33221a6fa)
    - [Error Handling](#ef43236673ca0bb606b14091061ac271)

[](...menuend)


<h2 id="c5822cd18f83072f8602e5235e1b7ed5"></h2>

# Rust Crash Course

<h2 id="ad148a3ca8bd0ef3b48c52454c493ec5"></h2>


<h2 id="47c14840d8e15331fa420b9b2f757cd9"></h2>

## Variable

- Variables hold primitive data or references to data
- Variables are immutable by default
- Rust is a block-scoped language

```rust
let name = "Brad";  // immutable
let mut age = 43; // mutable variable
// const must explicityly define a type
const ID: i32 = 380; 
```

### Shadowding

- advantage
    1. keep mutability
    2. change type
- example
    ```rust
    {
        let x = ...;
        // do stuff that does not modify x.
        let mut x = x;
        // do stuff that modifies x.
        let x = x;
        // x is immutable once more.
    }
    ```

<h2 id="6c1067528b82c9144a62fb1dd2cd925e"></h2>

## Primitive Data Types

<h2 id="09d9982852d86c2479924a4e3b723b1e"></h2>

### Scalar Types

- integers
    - i8,i32,u64,..., 
    - isize,usize (pointer-sized, how many bytes it takes to reference any location in memory) 
- floating-point numbers
    - f32,f64
- Booleanbs
    - bool : true/false
- Characters (char)
    - A unicode character, written within a single quote
    - Unicode Scalar Values range from U+0000 to U+D7FF and U+E000 to U+10FFFF inclusive
    - `'z'`,  `'\u{1F600}'`
        ```rust
        println!( "{}, {}", 200 as char, 255 as char  ); // È, ÿ
        ```

<h2 id="9e57b6b46532794638212df8e239adde"></h2>

### Compound Types

- Tuple
    ```rust
    let person = ("Brad", "Mass", 37);
    let (first, last, age) = person;
    ```
- Array
    - fixed list where elements are the same data type , NOT `vector`
    ```rust
    let numbers = [1, 2, 3, 4, 5];
    println!( "{:?}", numbers );
    // create an array with 8 values, and all set to 0
    let bytes = [0; 8];
    println!("{:?}", bytes);
    ```
    - `:?` mark here is what's called a **debug flag**, and since arrays have a debug **trait** built into them, so we can do it this way.
    - if we want the print more pretty, we can use `:#?`


<h2 id="89be9433646f5939040a78971a5d103a"></h2>

## Strings

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

<h2 id="b3f69e461542074d9696ee29ded180a0"></h2>

## Vectors

```rust
let mut numbers: Vec<i32> = vec![1,2,3,4,5];
// we can change its value while looping
for x in numbers.iter_mut() {
    *x *= 2;
}
// [2, 4, 6, 8, 10]
```

<h2 id="c647c38e64bd84c0fe9fe165f3fff0eb"></h2>

## Flows

- If
    - `if / else if / else`
    - Shorthand If
        ```rust
        let is_of_age = if age >=21 {true} else {false};
        ```
- Infinite loop
    ```rust
    loop {
        // break;
    }
    ```
    ```rust
    // loop label
    'a: loop {
        ...
        break 'a
    }
    ```
- While Loop
    ```rust
    while count < 100 {
        ...
    }
    ```
- For Range
    ```rust
    for x in 0..100 { // [0,1,...99]
        ...
    }
    for number in numbers.iter() {
        println!("{}", number);
    }
    ```
- Match
    ```rust
    let x = 5;
    match x {
        1 => println!("one"),
        2|3|5|7|11 => println!("primer"),
        13...19 => println!("A tean"),
        _ => println!("something else"),
    }
    ```
    ```rust
    let pair = (2,0);
    match pair {
        (x,0) => println!("x:{}", x ),
        (0,y) => println!("y:{}", y ),
        (x,y) if x+y==0  => println!("x+y=0" ),
        (x,_) if x%2==0  => println!("x is even" ),
        _ => println!("no match" ),
    }
    ```
- if let
    - consider following code, it's a bit weird
    ```rust
    let s = Some('c') ;
    match s {
        Some(t) => println!("{}", t),
        _ => {}
    }
    ```
    - that's why we have the `if let` binding
    ```rust
    // we're only really looking for this one case
    if let Some(i) = s {
        println!("{}", t),     
    } 
    ```
- while let
    - alterniative to loop/match

<h2 id="e93acb146e114b5dfa6ce2d12dcb96e4"></h2>

## Functions

```rust
fn add(n1:i32, n2:i32) -> i32 {
    n1 + n2  // no semicolon if ignore `return` keyword
}
```

- Closure

```rust
pub fn run() {
    ...
    // Closure
    let n3: i32 = 10;
    let add_nums = |n1:i32, n2:i32| n1+n2 +n3 ;
    println!( "{}", add_nums(3,3) );
}
```


<h2 id="6293f87533836e1d190c7b144ee25975"></h2>

## Structs

- Traditional Struct
    ```rust
    struct Color {
        red: u8,
        green: u8,
        blue: u8,
    }
    ```
    ```rust
    // use struct
    let red = 255;
    let c1 = Color {
        red, // field init shorthand syntax
        green: 0,
        blue: 0,
    };
    // c1.red
    let c2 = Color {
        red: 128,
        ..c1 // remaining fields comes from c1
    };
    ```
- Tuple Struct (without name fields)
    ```rust
    struct Color( u8,u8,u8 )
    ...
    let c = Color( 255,0,0 );
    // c.0
    ```

<h2 id="9a6a7f4d3eff618bae767bf2afefc00e"></h2>

### Methods

```rust
struct Person {
    first_name: String,
    last_name: String
}
```

define functions associated with that Person struct:

```rust
impl Person {
    // Constructor ( without &self )
    // Self here means the struct itself: i.e. Person
    fn new(first: &str, last: &str) -> Self { // --> Person
        Self {
            first_name: first.to_string(), 
            last_name: last.to_string()
        }
    }

    // methods take an explicit `self` parameter
    fn full_name(&self) -> String {
        format!( "{} {}", self.first_name, self.last_name )
    }

    fn set_last_name( &mut self, last: &str ) {
        self.last_name = last.to_string();  // last str->String
    }
}
```

to use it:

```rust
let mut p = Person::new("John", "Doe");
// p.first_name
// p.full_name()
```



<h2 id="1b22e7dc709b52f1767fe1eb5dc56625"></h2>

## Enums

### Basic C-like enum

```rust
enum Direction {
    Left,
    Right,
    Up,
    Down,
}

let up = Direction::Up;
```

### Enum with fields

```rust
enum Movement {
    // Variants
    Up(u32,u32,String),  // stores 3 integers
    Down {x:u32,y:u32},  // stores anonymous struct
    Left(Point),  // ( ) store data in Enums
    Right  // stores no data
}

struct Point {
    x: i32,
    y: i32
}

fn move_avatar(m: Movement) {
    // perform action depending on info
    match m {
        Movement::Up(_) => println!("moving up"),
        Movement::RIGHT => println!("moving right"),
        ...
    }
}

// just like struct, we could define methods
// and associated functions on Enums
impl Movement {
    ...
}
```


### The Option Enum

- **Rust doesn't have the null feature!**  But it does have an enum that can encode the concept of a value being present or absent. 
    ```rush
    enum Option<T> {
        Some(T),
        None
    }
    ```
    ```rust
    let some_number = Some(5);
    let some_string = Some("a string");
    let absent_number: Option<i32> = None;
    ```
- unwrap
    ```rust
    let x: i8 = 5;
    let y: Option<i8> = Some(5);
    let sum = x + y.unwrap_or(0);
    ```
- match
    ```rust
    fn plus_one(x: Option<i32>) -> Option<i32> {
        match x {
            Some(i) => Some(i + 1),
            // None => None,
            _ => None,
        }
    }
    ```
- if-let syntax: branch if pattern can be assigned
    - it's a little verbose to write the entire match
        ```rust
        let some_value = Some(3);
        match some_value {
            Some(3) => println!("three"),
            _ => (), // otherwise do nothing
        }
        ```
    - rewrite this using the if-let syntx
        ```rust
        if let Some(3) = some_value {
            println!("three");
        }
        ```




<h2 id="fae8a9257e154175da4193dbf6552ef6"></h2>

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


<h2 id="91af5705f16502125e8b2187e64202c0"></h2>

## CLI

```rust
use std::env;

pub fn run() {
    // print command-line arguments
    let args: Vec<String> = env::args().collect();
    println!("Args: {:?}", args)
}
```

<h2 id="9118ea0f76d0a8f21a42591caeee043e"></h2>

## Trait

<h2 id="8c24bd362f72757a4105edc427912b83"></h2>

### Debug Trait

if you  use `{:?}` format to print a custom struct, rust will throw an error.  In order to print it, you need to add `Debug`  trait to that struct.

```rust
#[derive(Debug)]
struct Person {
    first_name: String,
    last_name: String
}
```

now you can use `{:?}` to print this struct.

<h2 id="ea5b3400b3db3c5423190c549a3139c0"></h2>

### Display Trait

to use `{}` to print a struct,

```rust
use std::fmt;

impl fmt::Display for Person {
    fn fmt(*self, f: &mut fmt::Formatter ) -> fmt::Result {
        write!(f, "({},{})", self.first_name, self,last_name);
    }
}
```

<h2 id="ff24590464659ee8cdec688128c35f89"></h2>

### Clone

```rust
#[derive(Debug, Clone)]
...
let a = A(32);
let b = a.clone();
println!( "{}", a );
```

<h2 id="5fb63579fc981698f97d55bfecb213ea"></h2>

### Copy

```rust
#[derive(Debug, Copy)]
...
let a = A(32);
let b = a;
println!( "{}", a );
```

<h2 id="8045a0a6c688b0635e3caccc408a1446"></h2>

## Generic

```rust
struct A<T> {
    x: T
}

impl <T> A<T> {
    fn item(&self) -> &T {
        &self.x
    }
}
```


```rust
use std::ops::Mul;

trait Shape<T> {
    fn area(&self) -> T;
}

// must be T that implements `Mul` trait
struct Rectangle<T: Mul> {
    x: T,
    y: T,
}

impl <T: Copy> Shape<T> for Rectangle<T> where T:Mul<Output = T> , 
// or use this instead
// impl <T: Mul<Output = T> +  Copy> Shape<T> for Rectangle<T> 
{
    fn area<&self> -> T {
        self.x + self.y
    }
}
```

<h2 id="1a10be3692cec335c74387f33221a6fa"></h2>

## Lifetime

the flowing code compile error

```rust
fn pr(x: &str, y: &str) -> &str {
    if x.len() == y.len() {
        x
    } else {
        y
    }
}
```

to solve it :


```rust
// add 'a to specify lifetime
fn pr<'a>(x: &'a str, y: &'a str) -> &'a str {
    ...
```


<h2 id="ef43236673ca0bb606b14091061ac271"></h2>

## Error Handling


```rust
use std::io::ErrorKind;

use std::io;
use std::io::Read;
use std::fs::File;

fn read_file() -> Result<String, io::Error> {
    let f = File::open("text.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();
    match f.read_to_string( &mut s ) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}
```

A less verbose version of that same function. The way that we cleaned it up is by adding these question mark operators `?`.

```rust
    let mut f = File::open("text.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
```

we can actually further decrease the size of this function

```rust
    let mut s = String::new();
    // chan together
    File::open("text.txt")?.read_to_string(&mut s)?;
    Ok(s)

```

