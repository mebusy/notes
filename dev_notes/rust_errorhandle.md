
# Error Handling in Rust

## Unrecoverable Errors with panic!

```rust
fn main() {
    panic!("crash and burn");
}
```

To abort on panic in release mode, add the following lines into `[profile]` sections in your Cargo.toml file

```rust
[profile.release]
panic = 'abort'
```

## Recoverable Errors with Result Enum

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```


```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");

    let _f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };
}
```

Using nested match expression can make it hard to read. There is another way to write this exact same code using closure.


```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let _f = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    }); // ender outter unwrap_or_else
}
```

The `Result<T, E>` type has many methods that accept a closure and are implemented using match expressions.


### unwrap and expect

If the Result value is the Ok variant, unwrap will return the value inside the Ok.

If the Result is the Err variant, unwrap will call the panic! macro for us.

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").unwrap();
}
```

Another method, `expect`, which is similar to unwrap, lets us also choose the panic! error message. 

```rust
fn main() {
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
}
```


### Propagating Errors

- Ofentimes when you have a function whose implementation calls something that could fail, you want return that error back to the caller instead of handling it within the function.

<details>
<summary>
Propagating Example
</summary>

```rust
use std::io;
use std::io::Read;
use std::fs::File;

fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e), // explictly return
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}
```

</details>


### ? Operator : End earlier & Return the error

A Shortcut for Propagating Errors.

**The ? Operator Can Only Be Used in Functions That Return Result or Option.**

```rust
use std::io;
use std::io::Read;
use std::fs::File;

fn read_username_from_file() -> Result<String, io::Error> {
    let mut s = String::new();
    File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}
```

One-line version: the file system module has a convenient function.

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```







