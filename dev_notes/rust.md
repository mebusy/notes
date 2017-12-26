
# Rust

https://doc.rust-lang.org/book/second-edition/ch03-03-how-functions-work.html


```rust
$ cargo new hello_cargo --bin
$ cargo build [--release]
$ cargo run
```


```rust
let mut guess = String::new();
io::stdin().read_line(&mut guess).expect(...);
println!("You guessed: {}", guess);
```

 - The & indicates that this argument is a reference, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times.
 - references are immutable by default.  Hence, we need to write &mut guess rather than &guess to make it mutable.


 - Handling Invalid Input

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

# 3. Common Programming Concepts

## 3.3 Variables and Mutability

```rust
let foo = 5; // immutable
let mut bar = 5; // mutable
```

### Difference Between Variables and Constants

 - use `const` keyword
 - the type of the value must be annotated. 
 - Constants can be declared in any scope, including the **global** scope, 
    - which makes them useful for values that many parts of code need to know about.
 - constants may only be set to a constant expression 
    - not the result of a function call or any other value that could only be computed at runtime.

```rust
const MAX_POINTS: u32 = 100_000;
```

### Shadowing 

 - rust support variable shadow 


```rust
let mut guess = String::new(); 
...
let guess: u32 = guess.trim().parse() ...
```
 
## 3.2 Data Types

 - scalar types
    1. integers, 
        - `(i|u)(8|16|32|64|size)`
            - i32 is rust default 
            - isize/usize similar to size_t in c++? 
        - 0xFF , 0o77 , 0b1111_0000 , b'A' (u8 only)
    2. floating-point numbers, 
        - f32
        - f64 , default
    3. booleans, 
        - bool:  true/false
    4. and characters.
        - char type represents a Unicode Scalar Value
        - which means it can represent a lot more than just ASCII.
        - Unicode Scalar Values range from U+0000 to U+D7FF and U+E000 to U+10FFFF inclusive.

```rust
let c = 'z' ;
let cc = '☺' ;
```

 - Compound types 
    - tuples
        - element can be different type
    - arrays.
        - every element of an array must have the same type.
        - have a fixed length: once declared, they cannot grow or shrink in size.

```rust
// Grouping values into tuples
let tup: (i32, f64, u8) = (500, 6.4, 1);
let tup = (500, 6.4, 1);
// destructuring
let (x, y, z) = tup;
// access a tuple element directly 
let six_point_four = x.1;
```

```rust
// Arrays
let a = [1, 2, 3, 4, 5];
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
let second = a[1];
```

## 3.3 How Functions Work 


```rust
fn another_function(x: i32, y: i32) {
    ...
}
```


 - In function signatures, you must declare the type of each parameter
 - statement does not return a value
    - you can write such like `x = y = 6` in C
 - The block that we use to create new scopes, {}, is an expression

```rust
fn main() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {}", y);  // 4
}
```

 - Note the `x + 1` line without a semicolon at the end
    - Expressions do not include ending semicolons 
    - in C you should add `;` , and surround entrire `{  ... }` with `( )` 
 - Function with return value 
    - the return value of the function is synonymous with the value of the final expression
    - You can return early from a function by using the *return* keyword and specifying a value
    - but most functions return the last expression implicitly.

```rust
fn plus_one(x: i32) -> i32 {
    // Implicit return (no semicolon)
    x + 1
}
```

## 3.4 Control Flow

### if expression 

 - yes, it is an expression

```rust
    if number < 5 {
        ...
    } else if number > < 10 {
        ...
    } else {
        ...
    }
```

 - close to golang 

#### Using if in a let statement

 - Because if is an expression, we can use it on the right side of a let statement
    - must be the same type

```rust
let number = if condition {
    5
} else {
    6
};
```

### Loop 

```rust
loop {
    println!("again!");
}

while number != 0 {
    println!("{}!", number);

    number = number - 1;
}

let a = [10, 20, 30, 40, 50];
for element in a.iter() {
    println!("the value is: {}", element);
}

for i in 0u32..10 {
    print!("{} ", i); // 0 1 2 3 4 5 6 7 8 9
}

for number in (1..4).rev() {
    println!("{}!", number); // 3!  2!  1!
}

```

# 4. Understanding Ownership

 - most unique feature
 - enables Rust to make memory safety guarantees without needing a garbage collector.
 - several related features : borrowing, slices, and how Rust lays data out in memory.

## 4.1 What is Ownership ?

 - All programs have to manage the way they use a computer’s memory
    - Some languages have garbage collection
    - other languages explicitly allocate and free the memory
 - Rust uses a third approach: 
    - memory is managed through a system of ownership , with a set of rules that the compiler checks at compile time. 
    - No run-time costs are incurred for any of the ownership features.


























