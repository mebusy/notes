
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

### Memory and Allocation

 - In the case of a string literal ( "hello") , we know the contents at compile time so the text is hardcoded directly into the final executable
    - making string literals fast and efficient
 - With the *String* type ( String::from("hello") ), in order to support a mutable, growable piece of text, we need to allocate an amount of memory on the heap to hold the contents. 
    - unknown at compile time
    - The memory must be requested from the operating system at runtime.
        - done by `String::from`
    - We need a way of returning this memory to the operating system when we’re done with our *String*.
        - Rust takes a different path: the memory is automatically returned once the variable that owns it goes out of scope.

```rust
{
    let s = String::from("hello"); 
    // s is valid from this point forward

    // do stuff with s
} // this scope is now over, and s is no
  // longer valid
```

 - Note: In C++, this pattern of deallocating resources at the end of an item’s lifetime is sometimes called Resource Acquisition Is Initialization (RAII). 
 - The `drop` function in Rust will be familiar to you if you’ve used RAII patterns.
    - when a variable goes out of scope, Rust automatically calls the drop function and cleans up the heap memory for that variable
 - The example above is simple. But the behavior of code can be unexpected in more complicated situations when we want to have multiple variables use the data we’ve allocated on the heap. 

### Ways Variables and Data Interact: Move

```rust
let x = 5;
let y = x;
```

 - based on our experience with other languages:
    - “Bind the value 5 to x; then make a copy of the value in x and bind it to y.”
 - This is indeed what is happening because integers are simple values with a known, fixed size, and these two 5 values are pushed onto the stack.

```rust
let s1 = String::from("hello");
let s2 = s1;
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/rust_string_copy.png)

 - only the *String* data copied , meaning we copy the pointer, the length, and the capacity that are on the stack. 
 - We do not copy the data on the heap that the pointer refers to.
 - if Rust instead copied the heap data as well , the operation s2 = s1 could potentially be very expensive in terms of runtime performance if the data on the heap was large.
 - Earlier, we said that when a variable goes out of scope, Rust automatically calls the drop function and cleans up the heap memory for that variable.
    - This is a problem: when s2 and s1 go out of scope, they will both try to free the same memory. This is known as a double free error and is one of the memory safety bugs we mentioned previously. 
 - In Rust. Instead of trying to copy the allocated memory, Rust considers s1 to no longer be valid and therefore, Rust doesn’t need to free anything when s1 goes out of scope. 

```rust
let s1 = String::from("hello");
let s2 = s1;

// You’ll get an error like this because 
// Rust prevents you from using the invalidated reference:
println!("{}, world!", s1); 
```

 - So , String copy is like a "shallow copy" , not a “deep copy” .  
 - But because Rust also invalidates the first variable, instead of calling this a shallow copy, it’s known as a **move**.
 - Here we would read this by saying that s1 was moved into s2. So what actually happens is :

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/rust_string_move.png)

 - That solves our problem! With only s2 valid, when it goes out of scope, it alone will free the memory, and we’re done.
 - In addition, there’s a design choice that’s implied by this: 
    - Rust will never automatically create “deep” copies of your data. 
    - Therefore, any *automatic* copying can be assumed to be inexpensive in terms of runtime performance.


### Ways Variables and Data Interact: Clone 

 - If we do want to deeply copy the heap data of the *String*, not just the stack data, we can use a common method called *clone*.

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
println!("s1 = {}, s2 = {}", s1, s2);
```

### Stack-Only Data: Copy

```rust
let x = 5;
let y = x;

println!("x = {}, y = {}", x, y);
```

 - this code seems to contradict what we just learned
 - we don’t have a call to clone, but x is still valid and wasn’t moved into y.
 - The reason is that types like integers that have a known size at compile time are stored entirely on the stack.
    - so copies of the actual values are quick to make. 
    - That means there’s no reason we would want to prevent x from being valid after we create the variable y. 
    - In other words, there’s no difference between deep and shallow copying here, so calling *clone* wouldn’t do anything differently from the usual shallow copying and we can leave it out.

 - Rust has a special annotation called the *Copy* trait that we can place on types like integers that are stored on the stack 
    - If a type has the *Copy* trait, an older variable is still usable after assignment. 
    - 




























