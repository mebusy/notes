...menustart

 - [Rust](#f5e265d607cb720058fc166e00083fe8)
     - [所有权](#ed840a18e255779553359d5e0ec6f8a8)
     - [Data Types](#637881603c973c4967d77ec4ba147e0c)
         - [Scalar Types](#09d9982852d86c2479924a4e3b723b1e)
         - [Compound Types](#9e57b6b46532794638212df8e239adde)
     - [Grammar](#d305bbe79fb9dd87a3fda339c8b601b6)
         - [String](#27118326006d3829667a400ad23d5d98)
         - [Vectors/arrays](#a9ed91a0564c396f668757003053c533)
         - [Tuples](#e7e26a0ac2e1758814e4999a9242ba71)
         - [Struct](#886ef5dbd655a6c97726d7091c6b173e)
         - [Enum](#cf20423ed48998082c20099488a0917c)
         - [Generics](#0d7bdbf7f4e4f0dc8ed310a01dee3502)
         - [Methods](#20c51b5f4e9aeb5334c90ff072e6f928)
         - [Traits (Interface)](#fb0066fcef08c6094e2f12e05e3b347f)
         - [Pattern matching](#b72e68f7732ac254f401f88ed4911ada)
         - [Control flow](#af68915e510fea51b880a5e4e7577708)
     - [Memory safety & pointers](#24356b0edc0a65ad0b52ef7b6ee12dae)
     - [Modules](#bf17ac149e2e7a530c677e9bd51d3fd2)

...menuend


<h2 id="f5e265d607cb720058fc166e00083fe8"></h2>

-----
-----

# Rust

<h2 id="ed840a18e255779553359d5e0ec6f8a8"></h2>

-----

## 所有权

 - Rust编译器：对于任何给定的对象都只有一个绑定与之对应。
    - ![](../imgs/rust_ownership.png)
 - 怎么把 v 传递给另外一个函数呢?
    - 借用 (&v), 临时借给其他函数
    - 类似java中的 引用
 - recap 
    - ![](../imgs/rust_ownership2.webp)
 - 同一时刻，
    - 要么只有一个可变（&mut）借用，
    - 要么有多个不可变（&) 借用，
    - 不能同时存在可变和不可变借用。 
    - 没有人希望 自己在读的时候，对象被别人改变了。
    - ![](../imgs/rust_ownership3.0.webp)
    - ![](../imgs/rust_ownership3.webp)
 - 当大家都在读一个东西的时候，是不能写的。当一个人在写的时候，别人是不能读的。
    - 经典的读写锁问题, Rust在编译器级别做了限制.

<h2 id="637881603c973c4967d77ec4ba147e0c"></h2>

-----

## Data Types 

<h2 id="09d9982852d86c2479924a4e3b723b1e"></h2>

-----

### Scalar Types

 - integers
    - i8,i32,u64,...
 - floating-point numbers
    - f32,f64
 - Booleanbs
    - bool : true/false
 - characters
    - `'z'`
    - Rust’s char type is four bytes in size and represents a Unicode Scalar Value, which means it can represent a lot more than just ASCII.
    - Unicode Scalar Values range from U+0000 to U+D7FF and U+E000 to U+10FFFF inclusive

<h2 id="9e57b6b46532794638212df8e239adde"></h2>

-----

### Compound Types

 - Tuple
 - Array


<h2 id="d305bbe79fb9dd87a3fda339c8b601b6"></h2>

-----

## Grammar

<h2 id="27118326006d3829667a400ad23d5d98"></h2>

-----

### String 

 - String literals ( static str )
    -
    ```rust
    let x: &str = "hello world!";
    ```
 - A heap-allocated string
    -
    ```rust
    let s: String = "hello world".to_string();
    ```
 - A string slice – an immutable view into another string
    -
    ```rust
    let s_slice: &str = &s;
    println!("{} {}", s, s_slice); // hello world hello world
    ```
    - This is basically an immutable pair of pointers to a string


<h2 id="a9ed91a0564c396f668757003053c533"></h2>

-----

### Vectors/arrays

 - A fixed-size array
    -
    ```rust
    let four_ints: [i32; 4] = [1, 2, 3, 4];
    ```
 - A dynamic array (vector)
    -
    ```rust
    let mut vector: Vec<i32> = vec![1, 2, 3, 4];
    vector.push(5);
    ```
 - A slice – an immutable view into a vector or array
    -
    ```rust
    let slice: &[i32] = &vector;
    // Use `{:?}` to print something debug-style
    println!("{:?} {:?}", vector, slice); // [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
    ```

<h2 id="e7e26a0ac2e1758814e4999a9242ba71"></h2>

-----

### Tuples 

 - A fixed-size set of values of possibly different types
    -
    ```rust
    let x: (i32, &str, f64) = (1, "hello", 3.4);
    ```
 - Destructuring `let`
    -
    ```rust
    let (a, b, c) = x;
    ```
 - Indexing
    -
    ```rust
    println!("{}", x.1); // hello
    ```


<h2 id="886ef5dbd655a6c97726d7091c6b173e"></h2>

-----

### Struct

```rust
struct Point {
    x: i32,
    y: i32,
}

let origin: Point = Point { x: 0, y: 0 };
```

 - A struct with unnamed fields, called a ‘tuple struct’
    -
    ```rust
    struct Point2(i32, i32);
    let origin2 = Point2(0, 0);
    ```

<h2 id="cf20423ed48998082c20099488a0917c"></h2>

-----

### Enum

- Basic C-like enum
    -
    ```rust
    enum Direction {
        Left,
        Right,
        Up,
        Down,
    }

    let up = Direction::Up;
    ```
- Enum with fields
    -
    ```rust
    enum OptionalI32 {
        AnI32(i32),
        Nothing,
    }
    let two: OptionalI32 = OptionalI32::AnI32(2);
    let nothing = OptionalI32::Nothing;
    ```

<h2 id="0d7bdbf7f4e4f0dc8ed310a01dee3502"></h2>

-----

### Generics

```rust
struct Foo<T> { bar: T }

// This is defined in the standard library as `Option`
enum Optional<T> {
    SomeVal(T),
    NoVal,
}
```

<h2 id="20c51b5f4e9aeb5334c90ff072e6f928"></h2>

-----

### Methods

```rust
impl<T> Foo<T> {
    // Methods take an explicit `self` parameter
    fn get_bar(self) -> T {
        self.bar
    }
}

let a_foo = Foo { bar: 1 };
println!("{}", a_foo.get_bar()); // 1
```

<h2 id="fb0066fcef08c6094e2f12e05e3b347f"></h2>

-----

### Traits (Interface)

known as interfaces or typeclasses in other languages.

```rust
trait Frobnicate<T> {
    fn frobnicate(self) -> Option<T>;
}
```

- implement trait
    -
    ```rust
    impl<T> Frobnicate<T> for Foo<T> {
        fn frobnicate(self) -> Option<T> {
            Some(self.bar)
        }
    }
    let another_foo = Foo { bar: 1 };
    println!("{:?}", another_foo.frobnicate()); // Some(1)
    ```

<h2 id="b72e68f7732ac254f401f88ed4911ada"></h2>

-----

### Pattern matching

```rust
let foo = OptionalI32::AnI32(1);
match foo {
    OptionalI32::AnI32(n) => println!("it’s an i32: {}", n),
    OptionalI32::Nothing  => println!("it’s nothing!"),
}
```

<details>
<summary>
Advanced pattern matching
</summary>

```rust
struct FooBar { x: i32, y: OptionalI32 }
let bar = FooBar { x: 15, y: OptionalI32::AnI32(32) };

match bar {
    FooBar { x: 0, y: OptionalI32::AnI32(0) } =>
        println!("The numbers are zero!"),
    FooBar { x: n, y: OptionalI32::AnI32(m) } if n == m =>
        println!("The numbers are the same"),
    FooBar { x: n, y: OptionalI32::AnI32(m) } =>
        println!("Different numbers: {} {}", n, m),
    FooBar { x: _, y: OptionalI32::Nothing } =>
        println!("The second number is Nothing!"),
}
```

</details>


<h2 id="af68915e510fea51b880a5e4e7577708"></h2>

-----

### Control flow

 - `for` loops/iteration
    -
    ```rust
    let array = [1, 2, 3];
    for i in array.iter() {
        println!("{}", i);
    }
    ```
 - Ranges
    -
    ```rust
    for i in 0u32..10 {
        print!("{} ", i);
    }
    println!(""); // prints `0 1 2 3 4 5 6 7 8 9 `
    ```
 - if
    -
    ```rust
    if n < 0 {
        print!("{} is negative", n);
    } else if n > 0 {
        print!("{} is positive", n);
    } else {
        print!("{} is zero", n);
    }
    ```
 - if as expression
    -
    ```rust
    let value = if true {
        "good"
    } else {
        "bad"
    };
    ```
 - if let = 
    -
    ```rust
    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}!", state);
    } else {
        count += 1;
    }
    ```
 - `while` loop
    -
    ```rust
    while 1 == 1 {
        println!("The universe is operating normally.");
        // break statement gets out of the while loop.
        //  It avoids useless iterations.
        break
    }
    ```
 - Infinite loop
    -
    ```rust
    loop {
        println!("Hello!");
        // break statement gets out of the loop
        break
    }
    ```

<h2 id="24356b0edc0a65ad0b52ef7b6ee12dae"></h2>

-----

## Memory safety & pointers

 - 
```rust
let mut mine: Box<i32> = Box::new(3);
*mine = 5; // dereference
```
 - Owned pointer
    - only one thing can ‘own’ this pointer at a time
    - This means that when the `Box` leaves its scope, it can be automatically deallocated safely. 
 - 
```rust
let mut now_its_mine = mine;
*now_its_mine += 2;
```
 - Here, `now_its_mine` takes ownership of `mine`. In other words, `mine` is moved.
 - Reference
    - an immutable pointer that refers to other data
    - While a value is borrowed immutably, it cannot be mutated or moved.
    - A borrow lasts until the end of the scope it was created in.
    -
    ```rust
    let mut var = 4;
    var = 3;
    let ref_var: &i32 = &var;

    println!("{}", var); // Unlike `mine`, `var` can still be used
    println!("{}", *ref_var);
    ```
 - Mutable reference
    - While a value is mutably borrowed, it cannot be accessed at all.
    -
    ```rust
    let mut var2 = 4;
    let ref_var2: &mut i32 = &mut var2;
     *ref_var2 += 2;   
    // this would not compile because `var2` is borrowed.
    // var2 = 2; 
    ```


<h2 id="bf17ac149e2e7a530c677e9bd51d3fd2"></h2>

-----

## Modules

 - Modules to Control Scope and Privacy
 - Exposing Paths with the `pub` Keyword
 - Starting Relative Paths with `super`
    - construct relative paths that begin in the parent module by using `super` at the start of the path.
 - Bringing Paths into Scope with the `use` Keyword
 - Re-exporting Names with `pub use`

<details>
<summary>
Module example
</summary>

```rust
// src/lib.rs
// Declaring the front_of_house module
// whose body will be in src/front_of_house.rs
mod front_of_house  ;

// mod back_of_house is here
fn serve_order() {}
mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        // The fix_incorrect_order function is in the back_of_house module,
        // so we can use `super` to go to the parent module of back_of_house,
        // which in this case is crate, the root.
        super::serve_order();
    }

    fn cook_order() {}
}

// the name available in the new scope is still private.
// use `pub use` to re-export it , so that it is available to external code as well.
use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    // Absolute path
    // The add_to_waitlist function is defined in the same crate as eat_at_restaurant,
    // which means we can use the crate keyword to start an absolute path.
    crate::front_of_house::hosting::add_to_waitlist();
    // Relative path
    front_of_house::hosting::add_to_waitlist();
    // Bring hosting into scope with `use`
    hosting::add_to_waitlist();
}
```

```rust
// src/front_of_house.rs
// path: crate::front_of_house::hosting;
// front_of_house is provided by filename
pub mod hosting {
    pub fn add_to_waitlist() {}

    fn seat_at_table() {}
}

mod serving {
    fn take_order() {}

    fn serve_order() {}

    fn take_payment() {}
}
```

</details>

---






