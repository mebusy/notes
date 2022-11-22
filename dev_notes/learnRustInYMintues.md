[](...menustart)

- [Validating References with Lifetimes](#64ddc28a0ac7f69186ee86b1f8bc8786)
    - [Lifetime Annotations in Function Signatures](#f3d4e3f175edde17a6397d2dbb331920)
    - [Lifetime Annotations in Struct Definitions](#7a84101a7a68dae9cd05990ef3ccfa86)
    - [Lifetime Annotations in Method Definitions](#f3d510a4e30d6a89ebee0474abaa57a9)
    - [The Static Lifetime](#2bb98037fd2da57e912de143f6c29347)

[](...menuend)



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


