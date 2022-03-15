
# Rust : Concurrency, Threads, Channels, Mutex and Arc

## Thread

**Spawn**

```rust
use std::thread;

/// rust uses the OS-threads directly because 
/// its sake of having a lower runtime
/// possible output:
///     thread number: 3
///     thread number: 0
///     main thread output.
///     thread number: 1
///     thread number: 2
///     thread number: 5
pub fn spawn_thread() {
    println!( "---- thread spawn ----" );

    let mut c = vec![];

    for i in 0..10 {
        c.push(  thread::spawn( move || {
                println!("thread number: {}", i);
            }
        ));
    }

    println!( "main thread output.");

}
```

**Join**

```rust
use std::thread;

/// join():  
///     force the main thread to wait for all the joined handle to finish
pub fn join_thread() {
    println!( "---- thread join ----" );
    let mut c = vec![];

    for i in 0..10 {
        c.push(  thread::spawn( move || {
                println!("thread number: {}", i);
            }
        ));
    }

    for handle in c {
        // ok() converts Result<T,E> to Option<T>, converting errors to None
        handle.join().map_err( |err| println!("{:?}", err) ) .ok() ;
    }
}
```

## Mutex & Arc

```rust
use std::sync::{Mutex, Arc};
use std::thread;

/// We first create a mutex and the mutex is embeded in an Arc
/// Arc is an atomically reference counted type
/// Arcs convert the types into primitive types which are safe to be shared across threads.
pub fn arc_mutex() {
    println!( "---- arc mutex ----" );

    let c = Arc::new( Mutex::new(0) ) ;
    let mut hs = vec![];

    for _ in 0..10 {
        let c = Arc::clone( &c );
        let h = thread::spawn( move || {
            // lock ! gaining the lock control
            let mut num = c.lock().unwrap();
            *num +=1 ;
            // unlock ! lock gets dropped out
        });

        hs.push(h);
    }

    for h in hs {
        h.join().unwrap();
    }

    println!( "Result: {}", *c.lock().unwrap() );
}
```

## Channel

**channel**

```rust
use std::thread;
use std::sync::mpsc; // multiple producer single comsumer

/// tx.send() returns a Result
/// rx.recv() vs rx.try_recv
///     recv() is block
///     try_recv is non-blocking
pub fn channel() {
    println!( "---- channel test ----" );

    let (tx,rx) = mpsc::channel();

    thread::spawn( move || { tx.send(42).unwrap(); } );

    println!( "got {}", rx.recv().unwrap() );
}
```

**Multiple Producer**

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

const NUM_TIMES: usize = 24;

fn timer(d:usize, tx: mpsc::Sender<usize>) {
    thread::spawn( move || {
        println!("{}: setting timer...", d );
        thread::sleep( Duration::from_millis(d as u64) ) ;
        println!("{} sent!", d );
        tx.send(d).unwrap();
    });
}


pub fn channel_mpsc() {
    println!( "---- channel mpsc ----" );

    let (tx,rx) = mpsc::channel();
    for i in 0..NUM_TIMES {
        timer(i, tx.clone()) ;
    }
    for v in rx.iter().take( NUM_TIMES ) {
        println!( "{}: received!", v );
    }
}
```

**Channel & Mutex**

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













