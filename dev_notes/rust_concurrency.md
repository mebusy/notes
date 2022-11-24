# Concurrency

Rust only includes one-to-one threads, or OS-threads in its stardard library.

However if you would like to use green threads (m to n model) with the trade-off of having a larger binary, then you could use crates that provide such functionality.

## Spawn

```rust
use std::{thread, time::Duration};

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
}
// hi number 1 from the main thread!
// hi number 1 from the spawned thread!
// hi number 2 from the spawned thread!
// hi number 2 from the main thread!
// hi number 3 from the spawned thread!
// hi number 3 from the main thread!
// hi number 4 from the spawned thread!
// hi number 4 from the main thread!
```

Note the spawn thread didn't finish printing all of its numbers. This is because the main thread ends, the spawn thread is stopped no matter if it finished executing or not.


## Join

Calling `jon()` will block the currently running thread which in this case the main thread, until the `handle` thread ( the spawn thread ) terminates.


```rust
use std::{thread, time::Duration};

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap()
}
// hi number 1 from the main thread!
// hi number 1 from the spawned thread!
// hi number 2 from the main thread!
// hi number 2 from the spawned thread!
// hi number 3 from the main thread!
// hi number 3 from the spawned thread!
// hi number 4 from the main thread!
// hi number 4 from the spawned thread!
// hi number 5 from the spawned thread!
// hi number 6 from the spawned thread!
// hi number 7 from the spawned thread!
// hi number 8 from the spawned thread!
// hi number 9 from the spawned thread!
```

## Using Move Closures With Threads

This exmaple will raise an error: 


[E0373] closure may outlive the current function, but it borrows `v`, which is owned by the current function may outlive borrowed value `v`.

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Because rust doesn't know how long our thread will run for, rust doesn't allow us to take a reference to `v` inside the closure.

To force the closure to take ownership of *v*, use the `move` keyword.

```rust
    ...
    let handle = thread::spawn(move || {
    ...
}
```

## Message Passing






