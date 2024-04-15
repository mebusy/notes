[](...menustart)

- [Traits: Defining Shared Behavior](#30062dcad8f6dd3ff904c3fbb38c8059)
    - [Default Implementations](#f78cdd8ee64bc0232a9d010a9ab3502a)
    - [Generic Example](#6e0e96a6fa0564dc70412b86eafa923e)
    - [Traits as Parameters ( `impl TRAIT` syntax sugar )](#75832ea3de9cc56f0bc1187a55230953)
    - [Specifying Multiple Trait Bounds with the `+` Syntax](#7ae84d1dbd2b9229bdcfbf5c7894d4ce)
    - [Use `WHERE` clause to make clear Trait Bounds](#27faea966d6c670c17641a56c51517d3)
    - [Returning Types that Implement Traits](#8bc762cd737affa437bd5226f1a3f07a)
    - [Using Trait Bounds to Conditionally Implement Methods](#8d14778e381116681aa5fcf8e7fad595)
    - [Blanket Implementation](#20dfee67ef39a47a17576acf5bbe044d)
- [Some Built-in Traits](#b5c26203975fba6cc92390194c8dd144)
    - [Debug Trait](#8c24bd362f72757a4105edc427912b83)
    - [Display Trait](#ea5b3400b3db3c5423190c549a3139c0)
    - [Clone](#ff24590464659ee8cdec688128c35f89)
    - [Copy](#5fb63579fc981698f97d55bfecb213ea)
- [Trait Objects](#958d49973ce1cbbef0568304f29ed8b8)
    - [Object Safe Trait](#54cd7d1ff84ce266ad43e9146fdb1149)
- [Advanced Traits](#4ffb7ac08a15b1d3811fff77137701ec)
    - [Associated Types](#985cb623ec3c652fac4377ad107f3f9a)

[](...menuend)


<h2 id="30062dcad8f6dd3ff904c3fbb38c8059"></h2>

# Traits: Defining Shared Behavior

A trait defines functionality a particular type has and can share with other types.

> Known as **interfaces** feature in other languages.


Define a trait: 

```rust
pub trait Summary {
    // define shared method inside
    fn summarize(&self) -> String;
}
```

Implement `Summary` trait for some type: `impl ... for ...`

```rust
impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```



<h2 id="f78cdd8ee64bc0232a9d010a9ab3502a"></h2>

## Default Implementations

We can also give trait a default implementation

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

```rust
impl Summary for Tweet { }
```


Default implementation can call other methods inside trait definition

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}
```


<h2 id="6e0e96a6fa0564dc70412b86eafa923e"></h2>

## Generic Example

example 1:

```rust
pub struct ReportCard<T: std::fmt::Display> {
    pub grade: T,
    pub student_name: String,
    pub student_age: u8,
}

impl<T: std::fmt::Display> ReportCard<T> {
    pub fn print(&self) -> String {
        format!(
            "{} ({}) - achieved a grade of {}",
            &self.student_name, &self.student_age, &self.grade
        )
    }
}
```

example 2:


```rust
trait Frobnicate<T> {
    fn frobnicate(self) -> Option<T>;
}

impl<T> Frobnicate<T> for Foo<T> {
    fn frobnicate(self) -> Option<T> {
        Some(self.bar)
    }
}
let another_foo = Foo { bar: 1 };
println!("{:?}", another_foo.frobnicate()); // Some(1)
```


<h2 id="75832ea3de9cc56f0bc1187a55230953"></h2>

## Traits as Parameters ( `impl TRAIT` syntax sugar )

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

It is actually syntax sugar for a longer form, which is called a `trait bound` it looks like this:

```rust
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}
```

- this version of notify takes a reference to T.
    - you can also use `item: impl Summary` , or `Box<impl Summary>`

Trait bound is more clear when this function takes mutiple parameters with same type

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
    // ...
}
```

Note: If you want to use the type variable in multiple places you will need to use the longer version.

```rust
fn f(b1: impl Bar, b2: impl Bar) -> usize
```

is equivalent to

```russt
fn f<B1: Bar, B2: Bar>(b1: B1, b2: B2) -> usize
```

not 

```rust
fn f<B: Bar>(b1: B, b2: B) -> usize
```


<h2 id="7ae84d1dbd2b9229bdcfbf5c7894d4ce"></h2>

## Specifying Multiple Trait Bounds with the `+` Syntax

```rust
pub fn notify(item: &impl Summary + Display) {
```

The `+` syntax is  also valid with trait bounds on generic types:

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```


<h2 id="27faea966d6c670c17641a56c51517d3"></h2>

## Use `WHERE` clause to make clear Trait Bounds 

Multiple trait bound could hinder readability.

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {
```

We can rewrite the following code using `where` clause

```rust
fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone,
          U: Clone + Debug
{
```

<h2 id="8bc762cd737affa437bd5226f1a3f07a"></h2>

## Returning Types that Implement Traits

`impl Trait` can also be used in the return type of a function. In this case it is not a shorthand for a generic type parameter, but a way to return a value of some type that implements a trait without naming the concrete type.

```rust
fn returns_summarizable() -> impl Summary {
```


Returning types that implement a certain trait instead of concrete types is **very useful inside of closures and iterators**.


<h2 id="8d14778e381116681aa5fcf8e7fad595"></h2>

## Using Trait Bounds to Conditionally Implement Methods

For example, the type `Pair<T>` always implements the `new` function. 

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self {
            x,
            y,
        }
    }
}
```

But `Pair<T>` only implements the `cmp_display` method if its inner type T implements the `PartialOrd` trait that enables comparison and the `Display` trait that enables printing.

```rust
impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```



<h2 id="20dfee67ef39a47a17576acf5bbe044d"></h2>

## Blanket Implementation

Blanket Implementation is an implement of a trait either for all types, or for all types that match some condition.

In this example, we implement the `ToString` trait on any type T that implements the `Display` trait.

```rust
impl<T: Display> ToString for T {
    // --snip--
}
```

----

<h2 id="b5c26203975fba6cc92390194c8dd144"></h2>

# Some Built-in Traits

<h2 id="8c24bd362f72757a4105edc427912b83"></h2>

## Debug Trait

if you  use `{:?}` format to print a custom struct, rust will throw an error.  To solve this problem, you need to add `Debug`  trait to that struct.

```rust
#[derive(Debug)]
struct Person {
    first_name: String,
    last_name: String
}
```

now you can use `{:?}` to print this struct.


<h2 id="ea5b3400b3db3c5423190c549a3139c0"></h2>

## Display Trait

if you use `{}` to print a struct, rust will ask you to implement `std::fmt::Display` trait.

```rust
use std::fmt;

impl fmt::Display for Person {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.first_name, self.last_name)
    }
}
```

<h2 id="ff24590464659ee8cdec688128c35f89"></h2>

## Clone

```rust
#[derive(Clone)]
...

let a = Person {
    first_name: String::from("John"),
    last_name: String::from("Doe"),
};
let b = a.clone();
println!("{},{}", a, b);
```

<h2 id="5fb63579fc981698f97d55bfecb213ea"></h2>

## Copy

```rust
#[derive(Debug, Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let a = Point { x: 1, y: 2 };
    let b = a;
    println!("{:?},{:?}", a, b)
}
```


<h2 id="958d49973ce1cbbef0568304f29ed8b8"></h2>

# Trait Objects

Rust doesn't support classical inheritance. However it does achieve polymorphism, which is the ability for code to work on multiple types of data through **trait objects**.

An GUI app example:

<details>
<summary>
lib.rs
</summary>

```rust
pub trait Draw {
    fn draw(&self);
}

// main screen
pub struct Screen {
    // visual components to be drawn
    pub components: Vec<Box<dyn Draw>>,
}

impl Screen {
    // iterate over components and call draw on each
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}

// botton component
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        println!("Drawing button with label {}", self.label);
    }
}
```

</details>


<details>
<summary>
main.rs
</summary>

```rust
use rust_tutor::{Button, Draw, Screen};

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // Code to actually draw a select box
    }
}

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

</details>

You might noticed here we use `dyn` dynamic dispatch.  The trait objects **must include the `dyn` keyword**, otherwise it it raise a compile error [E0782].

That is , a trait object is always passed by pointer (a borrowed reference, Box, or other smart pointer) and has a vtable so that methods can be dispatched dynamically.

The type of trait objects uses `dyn Trait`, e.g. `&dyn Bar` or `Box<dyn Bar>`.


Let's talk about a little bit about static vs dynamic dispatch. 

Let's say if you had a function called `add<T>(a:T, b:T)` ,  you use that function with floating point numbers and integers. The compiler will generate a function called `integer_add` and a `float_add` , then it will find all the call sites of the `add` methods and replace it with the concrete implementation. This is called **static dispatch**.

The opposite is **dynamic dispatch**. Dynamic dispatch happens when the compiler does not know the concrete methods you're calling at compile time. Instead it figures that out at runtime. When using trait objects, the rust compiler must use dynamic dispatch. The compiler will add code to figure out the correct method to call at runtime.


<h2 id="54cd7d1ff84ce266ad43e9146fdb1149"></h2>

## Object Safe Trait

You can only make object safety traits into trait bounds. 

- A trait is object safe when all of the methods implemented on that trait have these 2 properties: 
    - the return type it not itself and there are no generic parameters
    - if a trait does not have these 2 properties, then the rust compiler can't figure out the concrete type of that trait and therefore doesn't know the correct methods to call.


<h2 id="4ffb7ac08a15b1d3811fff77137701ec"></h2>

# Advanced Traits 

<h2 id="985cb623ec3c652fac4377ad107f3f9a"></h2>

## Associated Types

**Associated Types** are placeholders which you can add to your trait and then methods can use that placeholder.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

For example here we've defined the `Iterator` trait which has one associated type named `Item`, and we use it in the `next` method. Then when we implement our iteractor trait we will specify a concrete type for `Item`.

This way you can define a trait which uses some type that's unknown until we implement the trait.

What's the difference between associated types and generics? They both allow use to define a type without specifying the concrete value. The difference is with associated types we can only have 1 concrete type per implementation.

```rust
struct Counter {}

// you implement Iterator trait with Item type u32
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        Some(1)
    }
}
// you can NOT do another implementation with Item type u16, for example
```

whereas with generics we can have multiple concrete types per implementation.

```rust
// Generic Example
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}

struct Counter {}

impl Iterator<u32> for Counter {
    fn next(&mut self) -> Option<u32> {
        Some(1)
    }
}
impl Iterator<u16> for Counter {
    fn next(&mut self) -> Option<u16> {
        Some(1)
    }
}
```

Using associated type trait if for any given implementation  you want the `next` method to return the same concrete type. 


# Choosing impl Trait or dyn Trait

- Advantages of `impl Trait` or generics:
    - fine-grained control of properties of types using where clauses,
    - can have multiple trait bounds (e.g., `impl Foo + Qux` is allowed, but `dyn Foo + Qux` is not),
- Disadvantages of `impl Trait` or generics:
    - monomorphisation causes increased code size.

- Advantages of `dyn Trait`:
    - a single variable, argument, or return value can take values of multiple different types.
- Disadvantages of `dyn Trait`:
    - virtual dispatch means slower method calls,
    - objects must always be passed by pointer
    - requires object safety

