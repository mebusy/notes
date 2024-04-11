[](...menustart)

- [Rust Crash Course](#c5822cd18f83072f8602e5235e1b7ed5)
    - [Variable](#47c14840d8e15331fa420b9b2f757cd9)
        - [Shadowding](#68ac3dabc5d182da440f74a6bccf79a7)
    - [Primitive Data Types](#6c1067528b82c9144a62fb1dd2cd925e)
        - [Scalar Types](#09d9982852d86c2479924a4e3b723b1e)
        - [Compound Types](#9e57b6b46532794638212df8e239adde)
        - [Type Aliase](#1d03b00d077f71ec0057d930d8b59e4d)
    - [Common Collections -- String / Vector / HashMap](#e8bc9e8a8229453b8a3d5bb0e3f1fa9c)
    - [Flows](#c647c38e64bd84c0fe9fe165f3fff0eb)
    - [Functions](#e93acb146e114b5dfa6ce2d12dcb96e4)
    - [Closure](#af4bb376939e77df0e7c2332b837a866)
        - [Returning Closures](#3625c84e56f1dcfb7aeeca953f192f5d)
    - [Structs](#6293f87533836e1d190c7b144ee25975)
        - [Methods](#20c51b5f4e9aeb5334c90ff072e6f928)
        - [Struct Inheritance ?](#34c0b94543a1d5fad1e1c9acc4388dc7)
    - [Enums](#1b22e7dc709b52f1767fe1eb5dc56625)
        - [Basic C-like enum](#e68fb48b0db95ac056021af55842cf57)
        - [Enum with fields](#e1436516cb5325961f9689ee8a1cccc5)
        - [The Option Enum](#c2d88d3b75e172263120c90a1942bd55)
    - [Iterator](#2a29178a57901ddb90f15e2026465103)
        - [Custom Iterator](#54beef80e0bdfb40d150270f78f2e783)
        - [Other Iterator Methods](#7b927c8e92f3c7a4db479901db78d290)
    - [Generic](#8045a0a6c688b0635e3caccc408a1446)
    - [Generic Type Parameters, Trait Bounds, and Lifetimes Together](#b5b64e222aafad7b06e8070ef4879937)

[](...menuend)


<h2 id="c5822cd18f83072f8602e5235e1b7ed5"></h2>

# Rust Crash Course

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

<h2 id="68ac3dabc5d182da440f74a6bccf79a7"></h2>

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
    - fixed length, vary types
        ```rust
        let tup: (i32, f64, u8) = (500, 6.4, 1);

        let person = ("Brad", "Mass", 37);
        let (first, last, age) = person;
        // or
        let brad = person.0;
        ```
    - `unit : ()`
        - this value and its corresponding type are both written `()` and represent an **empty value** or an **empty return type**
        - expressions implicitly return the unit value if they don’t return any other value.
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



<h2 id="1d03b00d077f71ec0057d930d8b59e4d"></h2>

### Type Aliase

```rust
    type Trunk = Box<dyn Fn() + Send + 'static>;
```


<h2 id="e8bc9e8a8229453b8a3d5bb0e3f1fa9c"></h2>

## Common Collections -- String / Vector / HashMap

[common collections](./rust_collections.md)


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

<h2 id="af4bb376939e77df0e7c2332b837a866"></h2>

## Closure

```rust
pub fn run() {
    ...
    // Closure
    let n3: i32 = 10;
    let add_nums = |n1:i32, n2:i32| n1+n2 +n3 ;
    println!( "{}", add_nums(3,3) );
}
```


<h2 id="3625c84e56f1dcfb7aeeca953f192f5d"></h2>

### Returning Closures

Closures are presented using traits. We can not return a concrete type. Instead we can use `impl TRAIT` syntax.

```rust
fn returns_closure() -> impl Fn(i32) -> i32 {
    |x| x + 1
}
```

Note that this syntax will not work in all situations.


```rust
// `if` and `else` have incompatible types expected closure 
// no two closures, even if identicial, have same type
fn returns_closure(a: i32) -> impl Fn(i32) -> i32 {
    if a > 0 {
        move |x| x + a
    } else {
        move |x| x - a
    }
}
```

In this case,  the 2 closures are different types, and the `impl TRAIT` syntax only works if we're returning one type. But in this case we're returning one of 2 types depending on the value of `a`. 

So instead of using the `impl trait` syntax, we can return a trait object.

```rust
// return type cannot have an unboxed trait object for information on trait objects
fn returns_closure(a: i32) -> dyn Fn(i32) -> i32
```

But rest doesn't know the size of closure being returned, so we have to wrap it in some sort of pointer.

```rust
fn returns_closure(a: i32) -> Box<dyn Fn(i32) -> i32> {
    if a > 0 {
        Box::new(move |x| x + a)
    } else {
        Box::new(move |x| x - a)
    }
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
- Unit-Like Structs (Without Any Fields)
    ```rusts
    struct AlwaysEqual;

    fn main() {
        let subject = AlwaysEqual;
    }
    ```
    - behave similarly to `()`
    - Unit structs are useful when you need to implement a trait on something, but don’t need to store any data inside it.

<h2 id="20c51b5f4e9aeb5334c90ff072e6f928"></h2>

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

<h2 id="34c0b94543a1d5fad1e1c9acc4388dc7"></h2>

### Struct Inheritance ?

Rust does **NOT** have struct inheritance of any kind.

If you want StructB to contain the same fields as StructA, then you need to use composition.

```rust
struct StructB {
    a: StructA,
    // other fields...
}
```

If you want to be able to use a `StructB` as a `StructA`, you can get some of the way there by implementing the `Deref` and `DerefMut` traits, which will allow the compiler to implicitly cast pointers to `StructB`s to pointers to `StructA`s:

```rust
struct StructA;

impl StructA {
    fn name(&self) -> &'static str {
        "Anna"
    }
}

struct StructB {
    a: StructA,
    // other fields...
}

impl std::ops::Deref for StructB {
    type Target = StructA;
    fn deref(&self) -> &Self::Target {
        &self.a
    }
}

fn main() {
    let b = StructB { a: StructA };
    println!("{}", b.name()); // Anna
}
```


Another alternative is to use generic + trait.



<h2 id="1b22e7dc709b52f1767fe1eb5dc56625"></h2>

## Enums

<h2 id="e68fb48b0db95ac056021af55842cf57"></h2>

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

<h2 id="e1436516cb5325961f9689ee8a1cccc5"></h2>

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


<h2 id="c2d88d3b75e172263120c90a1942bd55"></h2>

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
    let y = Some(x); //  y: Option <i8>
    let sum = x + y.unwrap();  // .unwrap() a None value will panic
    // let sum = x + y.unwrap_or(0);
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
    - NOTE: if x is Option of a type that not implement `Copy` trait, then x will be moved into the match,  if we want to use x later, we need to use `ref` keyword.
        ```rust
        // e.g. struct type that not implement Copy trait by default
        fn plus_one(x: Option<struct_type>) -> Option<struct_type> {
            match x {
                Some(ref i) => do-something ,
                None => None,
            }
        }
        ```
- `if-let` syntax: branch if pattern can be assigned
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
        if let Some(x) = some_value {
            println!("x = {}", x);
        } 
        //   else {
        //     println!("some_value is None");
        // }
        ```
- `unwarp_or_else` OR `if-let` ?
    - In general, you should use `if let` when you only need to handle one specific case and `unwrap_or_else` when you need to handle both success and failure cases.
- the question mark operator
    - when writing code that calls many functions that return the Option type, handling Some/None can be tedious.
        ```rust
        fn add_last_numbers(stack: &mut Vec<i32>) -> Option<i32> {
            let a = stack.pop();
            let b = stack.pop();

            match (a, b) {
                (Some(x), Some(y)) => Some(x + y),
                _ => None,
            }
        }
        ```
    - The question mark operator, ?, hides some of the boilerplate of propagating values up the call stack.
        ```rust
        fn add_last_numbers(stack: &mut Vec<i32>) -> Option<i32> {
            Some(stack.pop()? + stack.pop()?)
        }
        ```
        - It’s much nicer!
        - Ending the expression with ? will result in the Some’s unwrapped value, unless the result is None, in which case **None is returned early** from the enclosing function.
        - `?` can be used **in functions that return Option** because of the **early return of None** that it provides.


<h2 id="2a29178a57901ddb90f15e2026465103"></h2>

## Iterator

```rust
    let v1 = vec![1, 2, 3];

    // iterator method
    let iter = v1.iter();
    let total: i32 = iter.sum();
    println!("total: {}", total); // total: 6

    // map returns a iterator, but iterator are lazy
    // this won't do anything until we use a consumer
    let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
    println!("v2: {:?}", v2); // v2: [2, 3, 4]

    // When used as a pattern match
    // (and closure and function arguments are also pattern matches),
    // the & binds to a reference, making the variable the dereferenced value.
    let v3: Vec<_> = v1.iter().filter(|&x| x % 2 == 0).collect();
    println!("v3: {:?}", v3); // v3: [2]
```


<h2 id="54beef80e0bdfb40d150270f78f2e783"></h2>

### Custom Iterator

<details>
<summary>
A Counter
</summary>

```rust
struct Counter {
    count: u32,
}

impl Counter {
    fn new() -> Counter {
        // initial count is 0
        Counter { count: 0 }
    }
}

impl Iterator for Counter {
    // specify the associated type of item
    type Item = u32;

    // next method returns the next value in the sequence
    // or None when the sequence is over
    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;

        if self.count < 6 {
            Some(self.count)
        } else {
            None
        }
    }
}

fn main() {
    let counter = Counter::new();

    for i in counter {
        println!("{}", i); // 1, 2, 3, 4, 5
    }
}
```

</details>


<h2 id="7b927c8e92f3c7a4db479901db78d290"></h2>

### Other Iterator Methods

The standard library provides default implementations for a lot of other methods on iterator.

```rust
#[test]
fn using_other_iterator_trait_methods() {
    let sum: u32 = Counter::new()
        .zip(Counter::new().skip(1)) // [(1, 2), (2, 3), (3, 4), (4, 5)]
        .map(|(a, b)| a * b) // [2, 6, 12, 20]
        .filter(|x| x % 3 == 0) // [6, 12]
        .sum();
    assert_eq!(18, sum);
}
```


<h2 id="8045a0a6c688b0635e3caccc408a1446"></h2>

## Generic

- Make this function Generic
    ```rust
    fn get_large_number(list: &Vec<i32>) -> i32 {
        let mut largest = &list[0];
        for number in list {
            if number > largest {
                largest = number;
            }
        }
        *largest
    }
    // get_large_number(&number_list)
    ```
- first specify that `get_large_number` function uses generics
    ```rust
    fn get_large_number<T>(list: &Vec<i32>) -> i32 {
    ```
- now we have our generic type defined, we can use it inside our function
    ```rust
    fn get_large_number<T>(list: &Vec<T>) -> T {
    ```
- our function now almost work, but a compile error: operation `>` cannot be applied to type `&T`
    - because generic type may be anything, it could also possibly be something which can not be compared.
    - in order to solve this problem, we need to restrict our generic type that it must be comparable.
    - we need use `Traits`.
    ```rust
    fn get_large_number<T: PartialOrd + Copy>(list: &Vec<T>) -> T {
        ...
    }
    // get_large_number(&number_list) // nothing changed
    ```

We can also use Generics on structs.

<details>
<summary>
Generic Point:  'struct Point &lt;T, U&gt;'
</summary>


```rust
struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn new(x: T, y: U) -> Self {
        Self { x, y }
    }

    fn item(&self) -> (&T, &U) {
        (&self.x, &self.y)
    }
}

fn main() {
    let a = Point::new(1, 1.0);
    let b = Point::new(2.1, 3);

    println!("a = {:?}", a.item());
    println!("b.x = {}", b.x);
}
```

</details>

Generic won't incur a performance hit, that's because at compile time, rust will actually **turn the generic type into different explicit types**.


<h2 id="b5b64e222aafad7b06e8070ef4879937"></h2>

## Generic Type Parameters, Trait Bounds, and Lifetimes Together

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```


