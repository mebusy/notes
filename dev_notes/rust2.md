


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






















