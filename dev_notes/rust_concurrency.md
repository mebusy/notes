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

## Channel: Message Passing

One approach to ensure safe concurrency is `message passing`.

`std::sync::mpsc` stands for multi-producer, single-comsumer FIFO queue communication primitives.

To create a channel:

```rust
use std::sync::mpsc;

...
    // create a channel
    // tx: sender
    // rx: receiver
    let (tx, rx) = mpsc::channel();
```

So far, the type of channel not be infer,  it will be done when you finish the rest codes that use the channel.

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    // create a channel
    // tx: sender
    // rx: receiver
    let (tx, rx) = mpsc::channel();

    // thread of sender
    thread::spawn(move || {
        let val = String::from("hi");
        // send() return a Result type
        // in a product environment, we should handle the error
        // but in this example, we just use unwrap()
        tx.send(val).unwrap();
    });

    // main thread of receiver
    let received = rx.recv().unwrap();
    println!("Got: {}", received); // Got: hi
}
```

<details>
<summary>
<b>Example: Receiver as Iterator</b>
</summary>

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    // create a channel
    // tx: sender
    // rx: receiver
    let (tx, rx) = mpsc::channel();

    // thread of sender
    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];
        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(std::time::Duration::from_secs(1));
        }
    });

    // main thread of receiver
    for received in rx {
        println!("Got: {}", received);
    }
    // Got: hi
    // Got: from
    // Got: the
    // Got: thread
}
```


</details>


--- 

- `rx.recv()` vs `rx.try_recv()`
    - `recv()` is block
    - `try_recv()` is non-blocking


### Multiple Producer

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    for _ in 0..2 {
        let tx = tx.clone();
        thread::spawn(move || {
            let vals = vec![
                String::from("hi"),
                String::from("from"),
                String::from("the"),
                String::from("thread"),
            ];
            for val in vals {
                tx.send(val).unwrap();
                thread::sleep(std::time::Duration::from_secs(1));
            }
        });
    }

    // put the rest sender to another thread
    thread::spawn(move || {
        tx.send(String::from("hello")).unwrap();
    });

    // main thread of receiver
    for received in rx {
        println!("Got: {}", received);
    }
}
```


## Mutex, Arc: Sharing State

Sharing state means that we have some piece of data in memory that multiple threads can read and write to.

Acquiring/releasing lock is a pain point that might lead people away from multi-threading programming. 

But fortunately rust type system and ownership rules guarantee that you can't get locking and unlocking wrong.

This example try to spawn 10 threads, each thread will increase the counter by 1.

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Mutex::new(0);
    let mut handles = vec![];

    for _ in 0..10 {
        // ERROR: use of moved value: 
        // `counter` value moved into closure
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

What we want here is to allow counter to have mutliple owners, we first tye the Rc smart counter.

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        // `Rc<Mutex<i32>>` cannot be sent between threads safely 
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

But Rc smart counter cannot be sent between threads safely. So what we want is something exactly like Rc but thread safe. Rust standard library has the Atomic Reference Counting smart pointer which is exactly what we want, the `Arc`.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap()); // 10
}
```

You might have noticed that `counter` is immutable, but we're able to get a mutable reference to the value. That's because mutex uses *interior mutability*.


## Channel + Mutex

<details>
<summary>
<b>Example: Channel + Mutex</b>
</summary>

```rust
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

/// As an example, on a 32 bit x86 computer, usize = u32, while on x86_64 computers, usize = u64.
/// usize gives you the guarantee to be always big enough to hold any pointer or any offset in a data structure
// PS. it's a pretty expensive way to calculate primer
fn is_prime(n: usize) -> bool {
    (2..n).all( |i| { n%i != 0 } )
}

fn producer( tx: mpsc::SyncSender<usize> ) -> thread::JoinHandle<()> {
    thread::spawn( move || for i in 100_000_000.. {
        tx.send(i).unwrap();
    } )
}

fn worker(id: u64, shared_rx: Arc<Mutex<mpsc::Receiver<usize>>>) {
    thread::spawn( move || loop {
        let mut n = 0;
        match shared_rx.lock() {
            Ok(rx) => {
                match rx.try_recv() {
                    // receive message
                    Ok(_n) => {
                        n = _n ;
                    },
                    // not receive message
                    Err(_) => ()
                }
            },
            Err(_) => ()
        }

        if n != 0 {
            if is_prime(n) {
                println!("worker {} found a primer: {}", id, n );
            }
        }
    });
}

pub fn channel_mutex() {
    let (tx, rx) = mpsc::sync_channel( 1024 ) ;
    let shared_rx = Arc::new(Mutex::new(rx));

    for i in 1..5 {
        worker(i, shared_rx.clone());
    }
    producer(tx).join().unwrap();
}
```

</details>

