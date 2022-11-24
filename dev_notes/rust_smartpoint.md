[](...menustart)

- [Rust Smart Pointer](#bc858d11a99fc38ba346216e7d44f82c)
    - [The Box Smart Pointer](#81c8edbf405f142cc35785067b4de87b)
    - [The Deref Trait](#f054c445618dad83d17e082376419dcd)
        - [Implicit Deref coercion with functions and methods](#43e1965c09805266c5fe758aae8e210f)
    - [The Drop Trait](#5f54ac4b0aa77c6395e038a78f0287c6)
    - [Reference Counting](#84a9dbdb2a7bf37aed664d344a154352)
    - [Interior Mutability](#9fabe3ef034fb4e6f0a2ac5d433699c9)
        - [RefCell Smart Pointer](#0a4151832278ac22f76946228d443e4c)
    - [Reference Cycles](#4ee366679bc18a0b71029bef3f30d48f)
        - [Weak Smart Pointer](#ea88899a3bed5c65c820df28666df709)

[](...menuend)


<h2 id="bc858d11a99fc38ba346216e7d44f82c"></h2>

# Rust Smart Pointer


The most common pointer in Rust is reference. Reference simply borrow the values they point to. 

References don't have any special capabilities which also means they don't have much overhead unlike smart pointers.

Smart pointers are data structures that act like a pointer but have metadata and capabilities tacked on.

Strings and vectors are both smart pointers because they own some data and allow you to manipulate it. They store extra metadata such as the capacity, character encoding, etc...
 

Smart pointers are usually implemented using structs. But unlike regular structs, then implement the `Deref` and `drop` traits.

The `Deref` trait allows instances of your smart pointer struct to be treated like references so you can write code which works with either references or smart pointers.

The `drop` trait allows you to customize the code that is run when an instance of your smart pointer goes out of scope.


<h2 id="81c8edbf405f142cc35785067b4de87b"></h2>

## The Box Smart Pointer

`Box` allows you to allocate values on the heap.

```rust
    let b = Box::new(5);
    println!("b = {}", b);
```

Here, *5* is stored in the heap, and on the stack we store a pointer `b`.

`Box`es don't have any overhead except storing the data on the heap.


- When to use `Box` ?
    - When you have a type whose size can’t be known at compile time, and you want to use a value of that type in a context that needs to know an exact size
    - When you have a large amount of data and you want to transfer ownership but ensure the data won’t be copied when you do so
    - When you want to own a value and only care that it’s a type that implements a particular trait rather than knowing the concrete type


Say you want to define a recursive enum, `List`. 

```rust
// [E0072] recursive type `List` has infinite size 
enum List {
    Cons(i32, List),
    Nil,
}
```

Rust need to know how much space a type takes up at compile time. But in this example, we don't know how much space this enum could take up.

The compile suggests to use a indirection value by wrapping `List` inside the `Box` smart pointer.

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}
```

```rust
use List::{Cons, Nil};

fn main() {
    // let list = Cons(1, Cons(2, Cons(3, Nil)));
    let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
    println!("list: {:?}", list); // list: Cons(1, Cons(2, Cons(3, Nil)))
}
```


<h2 id="f054c445618dad83d17e082376419dcd"></h2>

## The Deref Trait

The `Deref` trait allows you to treat smart pointer as references.

```rust
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y);
```

What if we get rid of the dereference operator and just assert that y is equal to 5 ?

```rust
    // can't compare `{integer}` with `&{integer}` 
    // the trait `PartialEq<&{integer}>` is not implemented
    assert_eq!(5, y);
```

Now we can modify this example to use smart pointers instead of reference, specifically `Box`.

Box implements the `Deref` trait which allows the dereference operator works as same as the reference.

```rust
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
```

Next we'll create our own smart pointer which implements the `Deref` trait.

```rust
use std::ops::Deref;

// Tuple structs
struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    // associated type
    type Target = T;

    // takes a reference to self
    // returns a reference to the inner value
    fn deref(&self) -> &T {
        // -> &Self::Target
        &self.0
    }
}

fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

<h2 id="43e1965c09805266c5fe758aae8e210f"></h2>

### Implicit Deref coercion with functions and methods

Deref coercion is a convenience feature in rust that happens automatically for types that implement the `Deref` trait.

Deref coercion will convert a reference to one type to a reference to a different type.

```rust
fn hello(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Here we call the `hello` function and pass it a reference to `m`. It works, no error, even though `m` is of type `MyBox` and here we're passing in a reference to `MyBox` which the `hello` function expects a string slice.

`MyBox` implements the `Deref` trait, if we call `deref()` on `m`, we'll get back a reference to a string `&String`. Then `String` in rust also implements the `Deref` trait, and if we call `deref()` on a `String`,  we'll get back a string sliece `&str`. 

Rust see that the type being passed to `hello` is different than the type expected by the function signature, and automatically perform these chained `deref()` calls at compile time to get the correct type.

If rust didn't have automatic deref coercion, in order to call `hello`, we have to write like this, our code would be harder to write.

```rust
    hello(&(*m)[..]);
```

Rust does deref coercion when it finds types and trait implementations in three cases:

1. `From &T to &U when T: Deref<Target=U>`
2. `From &mut T to &mut U when T: DerefMut<Target=U>`
3. `From &mut T to &U when T: Deref<Target=U>`
    - NOT inverse
    - because convert a mut to immute won't break the borrowing rules, but convert an immute to mut does!


<h2 id="5f54ac4b0aa77c6395e038a78f0287c6"></h2>

## The Drop Trait

The `drop` trait could be implemented on any type, and allows you to customize what happens when a value goes out of scope. The `drop` trait is almost always used when implementing smart pointers. 

```rust
struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        // we simply just want to see how the drop trait works
        // so we will only print out a message
        println!("Dropping CustomSmartPointer with data `{}`!", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created.");
    // CustomSmartPointers created.
    // Dropping CustomSmartPointer with data `other stuff`!
    // Dropping CustomSmartPointer with data `my stuff`!
}
```

What happens if you want to customize this cleanup behavior? In most cases this isn't necessary, however in some cases you want to clean up a value early. 

One example is when using smart pointers to manager locks. You might want to call the drop method to release a lock.


<h2 id="84a9dbdb2a7bf37aed664d344a154352"></h2>

## Reference Counting

A reference counting smart pointer allows us to share ownership of some data.

**Note** that the Rc smart pointer only allows multiple parts of your program to read the same data, **NOT modify it**.

There are cases where a single value has multiple owneres. For example, a graph with multiple edges that point to the same node. Conceptually that node owned by all the edges. In this case a node should not be cleaned up unless it doesn't have any edges pointing to it.

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));

    let b = Cons(3, Box::new(a));
    let c = Cons(4, Box::new(a)); // [E0382] use of moved value: `a` value used here after move 
}
```

See this example, The `Cons` of b and c are all move the value `a`,  it will raise error.

Now using the Rc pointer.

```rust
use std::rc::Rc;

enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use List::{Cons, Nil};

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));

    let b = Cons(3, a.clone());
    let c = Cons(4, Rc::clone(&a)); // jus another way to clone
}
```


`Rc::clone` does not make the deep copy of the data like most `CLONE` implementations. Calling `clone()` here only increments the reference count.

Adding some print message

```rust
fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!("count after creating a = {}", Rc::strong_count(&a));

    let b = Cons(3, a.clone());
    println!("count after creating b = {}", Rc::strong_count(&a));

    {
        let c = Cons(4, Rc::clone(&a)); // jus another way to clone
        println!("count after creating c = {}", Rc::strong_count(&a));
    }
    println!("count after creating c = {}", Rc::strong_count(&a));

    // count after creating a = 1
    // count after creating b = 2
    // count after creating c = 3
    // count after creating c = 2
}
```

<h2 id="9fabe3ef034fb4e6f0a2ac5d433699c9"></h2>

## Interior Mutability

Interior mutability is a design pattern in rust that allows you to **mutate data even there are immutable referencess** to that data, which is typically disallowed by the borrowing rules.

To mutate data this pattern use unsafe code inside a data structure to bypass the typical rules around mutation and borrowing. 

"Unsafe code" is the code that is not checked at compile time for memory safety.  Even though the borrowing rules are't enforced at compile time, we can still enforce them at runtime.


<h2 id="0a4151832278ac22f76946228d443e4c"></h2>

### RefCell Smart Pointer

The `RefCell` smart pointer represents single ownership over the data it holds, much like the `Box`.

The difference is the `Box` smart pointer enforce the borrowing rules at compile time, whereas the `Refcell` smart pointer enforce borrowing rules at runtime. This means if you break the borrowing rules at runtime, your program will panic.

The advantage of checkong borrowing rules at runtime is that certain memory safe scenairos are allowed whereas they would be disallowd at compile time. This is because certain properties of a program are impossible to detect using static analysis. The most famous example of this is the halting problem.


Mutating a value inside an immutable value is called the **interior mutability pattern**.

In this example, as you see, the borrowing rules checked at compile time don't  allow us to do in such ways.

```rust
fn main() {
    let a = 5;
    // [E0596] cannot borrow `a` as mutable,
    // as it is not declared as mutable cannot borrow as mutable
    let b = &mut a;

    let mut c = 10;
    let d = &c;
    // [E0594] the data it refers to cannot be written
    *d = 20;
}
```

We could solve this with some indirection.

Imagine we have a data structure that stores some value, and inside that data structure the value is mutable. But when we get a reference to that data structure the reference itself immutable. Code outside of the data structure would not be able to mutate the data within the structure directly, but you can imagine we could call some methods that would mutate the inner value.

This is called **interior mutability pattern**, and is essentially what the `RefCell` smart pointer does. The `RefCell` smart pointer does is a little fancier though because instead of calling methods to mutate the data it can call methods to get an immutable of mutable reference to the data.  And this works because the `RefCell` smart pointer checks that references are valid at runtime.


<details>
<summary>
RecCell example
</summary>

```rust
pub trait Messager {
    fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messager> {
    messager: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messager,
{
    pub fn new(messager: &T, max: usize) -> LimitTracker<T> {
        LimitTracker {
            messager,
            value: 0,
            max,
        }
    }

    pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max = self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messager.send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messager
                .send("Urgent warning: You've used up over 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messager
                .send("Warning: You've used up over 75% of your quota!");
        }
    }
}

use std::cell::RefCell; // 1

struct MockMessager {
    sent_messages: RefCell<Vec<String>>, // 2
}

impl MockMessager {
    fn new() -> MockMessager {
        MockMessager {
            sent_messages: RefCell::new(vec![]), // 3
        }
    }
}

impl Messager for MockMessager {
    fn send(&self, message: &str) {
        self.sent_messages.borrow_mut().push(String::from(message)); // 4
    }
}

fn main() {
    let mock_messager = MockMessager::new();
    let mut limit_tracker = LimitTracker::new(&mock_messager, 100);

    limit_tracker.set_value(80);

    assert_eq!(mock_messager.sent_messages.borrow().len(), 1); // 5
}
```

</details>


<h2 id="4ee366679bc18a0b71029bef3f30d48f"></h2>

## Reference Cycles

Rust is known for memory safe, it provides guarantees such as you can't have data races.  However it does not provide the same guarantee for memory leak.

Rust makes it difficult but not impossible to create memory leak.  We can create a memory leak by using the Rc smart pointer and RefCell smart pointer. Using these 2 smart pointers we can create references where items reference each other in a cycle which will create a memory leak.

<h2 id="ea88899a3bed5c65c820df28666df709"></h2>

### Weak Smart Pointer

Instead of using Rc smart pointer, we can use `Weak` smart pointer.

`Weak` is a version of [`Rc`] that holds a non-owning reference to the managed allocation. 







