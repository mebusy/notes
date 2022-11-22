
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


## Generic Example


<details>
<summary>
A Generic Trait Example
</summary>


```rust
trait Frobnicate<T> {
    fn frobnicate(self) -> Option<T>;
}
```

To implement trait

```rust
impl<T> Frobnicate<T> for Foo<T> {
    fn frobnicate(self) -> Option<T> {
        Some(self.bar)
    }
}
let another_foo = Foo { bar: 1 };
println!("{:?}", another_foo.frobnicate()); // Some(1)
```


</details>


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

Trait bound is more clear when this function takes mutiple parameters with same type

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
    // ...
}
```


## Specifying Multiple Trait Bounds with the `+` Syntax

```rust
pub fn notify(item: &impl Summary + Display) {
```

The `+` syntax is  also valid with trait bounds on generic types:

```rust
pub fn notify<T: Summary + Display>(item: &T) {
```


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

## Returning Types that Implement Traits

Returning Trait Objects allows you return any type.


```rust
fn returns_summarizable() -> impl Summary {
```

Returning types that implement a certain trait instead of concrete types is **very useful inside of closures and iterators**.


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



## Blanket Implementation

Blanket Implementation is an implement of a trait either for all types, or for all types that match some condition.

In this example, we implement the `ToString` trait on any type T that implements the `Display` trait.

```rust
impl<T: Display> ToString for T {
    // --snip--
}
```


