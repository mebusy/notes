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

Trait bound is more clear when this function takes mutiple parameters with same type

```rust
pub fn notify<T: Summary>(item1: &T, item2: &T) {
    // ...
}
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

Returning Trait Objects allows you return any type.


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


