
# Rust Crash Course

## mod

```rust
// print.rs
pub fn run() {
    println!("Hello from print.rs file");
}
```

```rust
// main.rs
mod print;

fn main() {
    print::run();    
}
```


## Variable

- Variables hold primitive data or references to data
- Variables are immutable by default
- Rust is a block-scoped language

```rust
let name = "Brad";  // immutable
let mut age = 43; // mutable variable

// define const, const must explicityly define a type
const ID: i32 = 380; 

// Assign multiple vars
let ( my_name, my_age ) = ( "Brad", 43 );
```

## Primitive Data Types

### Scalar Types

- integers
    - i8,i32,u64,..., 
    - isize,usize (pointer-sized, how many bytes it takes to reference any location in memory) 
- floating-point numbers
    - f32,f64
- Booleanbs
    - bool : true/false
- Characters (char)
    - Single character
    - Rust’s char type is four bytes in size and represents a Unicode Scalar Value, which means it can represent a lot more than just ASCII.
    - Unicode Scalar Values range from U+0000 to U+D7FF and U+E000 to U+10FFFF inclusive
    - `'z'`,  `'\u{1F600}'`
    ```rust
    println!( "{}, {}", 200 as char, 255 as char  ); // È, ÿ
    ```

<h2 id="9e57b6b46532794638212df8e239adde"></h2>


### Compound Types

- Tuple
    - group together values of different types
    - max 12 elements
    ```rust
    let person: (&str, &str, i8) = ( "Brad", "Mass", 37 );
    println!("{} is from {} and is {}", person.0, person.1, persion.2);
    ```
- Array
    - fixed list where elements are the same data type , NOT `vector`
    ```rust
    let mut numbers: [i32; 5] = [1,2,3,4,5];
    println!( "{:?}", numbers );

    // Get Slice
    let slice: &[i32] = &numbers;
    ```
    - `:?` mark here is what's called a **debug flag**, and since arrays have a debug **trait** built into them, so we can do it this way.
    - if we want the print more pretty, we can use `:#?`


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

## Vectors

```rust
let mut numbers: Vec<i32> = vec![1,2,3,4,5];
// we can change its value while looping
for x in numbers.iter_mut() {
    *x *= 2;
}
// [2, 4, 6, 8, 10]
```

## Flows

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
    for x in 0..100 {
        ...
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

## Reference Pointers

- Reference Pointers  point to a resource in memory.
    ```rust
    // Primitive Array
    let arr1 = [1,2,3];
    let arr2 = arr1;  // assign
    println!( "{:?}", (arr1, arr2) );
    // ([1,2,3], [1,2,3])
    ```

- With non-primitives, if you assign another variable to a data, the first variable will no longer hold that value.
    - You'll need to use a reference (&) to point to the resource.
    ```rust
    // Primitive Array
    let vec1 = vec![1,2,3];
    let vec2 = vec1;  // assign
    println!( "{:?}", (vec1, vec2) );  // error
    ```
    ```rust
    let vec1 = vec![1,2,3];
    let vec2 = &vec1;  
    println!( "{:?}", (&vec1, vec2) );  
    ```

## Structs

- Traditional Struct
    ```rust
    struct Color {
        red: u8;
        green: u8;
        blue: u8;
    }
    ```
    ```rust
    // use struct
    let c = Color {
        red: 255,
        green: 0,
        blue: 0,
    };
    // c.red
    ```
- Tuple Struct
    ```rust
    struct Color( u8,u8,u8 )
    ...
    let c = Color( 255,0,0 );
    // c.0
    ```

### Struct which has functions

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
    // Self here means the struct itself
    fn new(first: &str, last: &str) -> Self {
        Self {
            first_name: first.to_string(), 
            last_name: last.to_string()
        }
    }


    // Get full name
    fn full_name(&self) -> String {
        format!( "{} {}", self.first_name, self.last_name )
    }

    // Set last name
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



## Enums

```rust
enum Movement {
    // Variants
    Up(u32,u32,String),  // tuple
    Down {x:u32,y:u32},
    Left(Point),
    Right
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

impl Movement {
    ...
}
```

### Result & Option

```rust
enum Result<T,E> {
    Ok(T),
    Err(E),
}

enum Option<T> {
    Some(T),
    None
}

```

- The Result enum is basically usually used for error-checking.
- You can also use Option enum to error check as well.
- But Result allow us see why it failed.


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


## CLI

```rust
use std::env;

pub fn run() {
    // print command-line arguments
    let args: Vec<String> = env::args().collect();
    println!("Args: {:?}", args)
}
```

## Trait

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



