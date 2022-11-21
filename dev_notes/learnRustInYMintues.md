[](...menustart)

- [Rust](#f5e265d607cb720058fc166e00083fe8)
    - [Grammar](#d305bbe79fb9dd87a3fda339c8b601b6)
        - [Traits (Interface)](#fb0066fcef08c6094e2f12e05e3b347f)
    - [Traits](#42dff6d9ccc56c155188778aff284f7c)
        - [Default Implementations](#f78cdd8ee64bc0232a9d010a9ab3502a)
        - [Traits as Parameters `impl Trait` syntax](#3d591b9a37ce5be1a66a4106f0f326be)
        - [Specifying Multiple Trait Bounds with the `+` Syntax](#7ae84d1dbd2b9229bdcfbf5c7894d4ce)
        - [Clearer Trait Bounds with where Clauses](#a7dbea5d964307601e9192a4c3574b31)
        - [Returning Types that Implement Traits](#8bc762cd737affa437bd5226f1a3f07a)
        - [Fixing the largest Function with Trait Bounds](#bce419857a72cd38b5c75c2ed17433c0)
        - [Using Trait Bounds to Conditionally Implement Methods](#8d14778e381116681aa5fcf8e7fad595)
    - [Validating References with Lifetimes](#64ddc28a0ac7f69186ee86b1f8bc8786)
        - [Lifetime Annotations in Function Signatures](#f3d4e3f175edde17a6397d2dbb331920)
        - [Lifetime Annotations in Struct Definitions](#7a84101a7a68dae9cd05990ef3ccfa86)
        - [Lifetime Annotations in Method Definitions](#f3d510a4e30d6a89ebee0474abaa57a9)
        - [The Static Lifetime](#2bb98037fd2da57e912de143f6c29347)

[](...menuend)


<h2 id="f5e265d607cb720058fc166e00083fe8"></h2>

# Rust



<h2 id="d305bbe79fb9dd87a3fda339c8b601b6"></h2>

## Grammar




<h2 id="fb0066fcef08c6094e2f12e05e3b347f"></h2>

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

See more details at *Traits* section.





<h2 id="42dff6d9ccc56c155188778aff284f7c"></h2>

## Traits

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

<h2 id="f78cdd8ee64bc0232a9d010a9ab3502a"></h2>

### Default Implementations

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}
```

<h2 id="3d591b9a37ce5be1a66a4106f0f326be"></h2>

### Traits as Parameters `impl Trait` syntax

```rust
pub fn notify(item: impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

It is actually syntax sugar for a longer form, which is called a `trait bound` it looks like this:

```rust
pub fn notify<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}
```

<h2 id="7ae84d1dbd2b9229bdcfbf5c7894d4ce"></h2>

### Specifying Multiple Trait Bounds with the `+` Syntax

```rust
pub fn notify(item: impl Summary + Display) {
```

The `+` syntax is  also valid with trait bounds on generic types:

```rust
pub fn notify<T: Summary + Display>(item: T) {
```

<h2 id="a7dbea5d964307601e9192a4c3574b31"></h2>

### Clearer Trait Bounds with where Clauses

We can rewrite the following code 

```rust
fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {
```

to :

```rust
fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone,
          U: Clone + Debug
{
```

<h2 id="8bc762cd737affa437bd5226f1a3f07a"></h2>

### Returning Types that Implement Traits

you can only use `impl Trait` if you’re returning a single type. 

```rust
fn returns_summarizable() -> impl Summary {
```

See *Using Trait Objects That Allow for Values of Different Types* in chapter 17.


<h2 id="bce419857a72cd38b5c75c2ed17433c0"></h2>

### Fixing the largest Function with Trait Bounds

```rust
fn largest<T: PartialOrd + Copy>(list: &[T]) -> T {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}
```

`>` operator is defined as a default method on the standard library trait std::cmp::PartialOrd, we need to specify PartialOrd in the trait bounds for T so the largest function can work on slices of any type that we can compare. 


When we made the largest function generic, it became possible for the list parameter to have types in it that don’t implement the Copy trait. Consequently, we wouldn’t be able to move the value out of list[0] and into the largest variable, resulting in this error. To call this code with only those types that implement the Copy trait, we can add Copy to the trait bounds of T! 

<h2 id="8d14778e381116681aa5fcf8e7fad595"></h2>

### Using Trait Bounds to Conditionally Implement Methods

For example, the type `Pair<T>` always implements the new function. But `Pair<T>` only implements the cmp_display method if its inner type T implements the PartialOrd trait that enables comparison and the Display trait that enables printing.

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

We can also conditionally implement a trait for any type that implements another trait. 

```rust
impl<T: Display> ToString for T {
    // --snip--
}
```


<h2 id="64ddc28a0ac7f69186ee86b1f8bc8786"></h2>

## Validating References with Lifetimes

Every reference in Rust has a lifetime, which is the scope for which that reference is valid.

Most of the time, lifetimes are implicit and inferred,  just like most of the time, types are inferred. 

We must annotate types when multiple types are possible. In a similar way, we must annotate lifetimes when the lifetimes of references could be related in a few different ways.

Rust requires us to annotate the relationships using generic lifetime parameters to ensure the actual references used at runtime will definitely be valid.


```rust
// error[E0106]: missing lifetime specifier
// help: this function's return type contains a borrowed value, but the
// signature does not say whether it is borrowed from `x` or `y`
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

<h2 id="f3d4e3f175edde17a6397d2dbb331920"></h2>

### Lifetime Annotations in Function Signatures

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

- The function signature now tells Rust that 
    - for some lifetime 'a, the function takes two parameters, both of which are string slices that live at least as long as lifetime 'a. 
    - The function signature also tells Rust that the string slice returned from the function will live at least as long as lifetime 'a. 

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {}", result);
    }
}
```

- In this example, 
    - string1 is valid until the end of the outer scope, 
    - string2 is valid until the end of the inner scope, 
    - and result references something that is valid until the end of the inner scope. 


Next, let’s try an another example:

```rust
// error[E0597]: `string2` does not live long enough
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {}", result);
}
```

<h2 id="7a84101a7a68dae9cd05990ef3ccfa86"></h2>

### Lifetime Annotations in Struct Definitions

```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}
```

<h2 id="f3d510a4e30d6a89ebee0474abaa57a9"></h2>

### Lifetime Annotations in Method Definitions

```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
```

<h2 id="2bb98037fd2da57e912de143f6c29347"></h2>

### The Static Lifetime

'static, which means that this reference can live for the entire duration of the program.

All string literals have the 'static lifetime, which we can annotate as follows:

```rust
let s: &'static str = "I have a static lifetime.";
```


