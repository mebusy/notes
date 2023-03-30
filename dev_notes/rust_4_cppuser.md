[](...menustart)

- [Rust for C++ user](#c43fb867d93a29220d7f64f5d3b8724c)
    - [默认不可变](#087e0f8efe3613461f96328e43e2476d)
    - [禁止整数隐式转换](#450a1011cbc1d5164353e4dd0c80f858)
    - [简化构造、复制与析构](#7df5bda3629ac9232ce5b140fce4cedd)
    - [显式参数传递](#6e2d9dc6b0fd3ca3d9187b28356a14a1)
    - [内置格式化与lint](#37f632d52f26580ac35300665eb0c336)
    - [标准化的开发流程和包管理](#3057f5c2a8db24c9bb71fdec9215a6f7)
    - [lifetime安全性](#e36527b4c0bbfae1bd75d9a1bb4ef9ac)
    - [边界安全性](#1490ba65e4fc8d6223c53f44ac803091)
    - [类型安全性](#2e321cbfdd07269096af86370e25f590)
    - [多线程安全性](#94b62a30b8785a22312db949fef9b43c)
    - [统一的错误处理](#4ae3bd7ed074efb0e2e46948479a41b3)

[](...menuend)


<h2 id="c43fb867d93a29220d7f64f5d3b8724c"></h2>

# Rust for C++ user

<h2 id="087e0f8efe3613461f96328e43e2476d"></h2>

## 默认不可变

<h2 id="450a1011cbc1d5164353e4dd0c80f858"></h2>

## 禁止整数隐式转换

```rust
fn foo(x: u32) {}

let x: i32 = 0;
foo(x);  // error
```

<h2 id="7df5bda3629ac9232ce5b140fce4cedd"></h2>

## 简化构造、复制与析构

C++中RAII的Rule of 0, or 3, or 5 "大名鼎鼎", 明明是一件非常常规的东西，确搞得非常的复杂。 

Rust非常简单。

- 对象对象默认只支持Destructive move（通过memcpy完成）
- 需要复制
    - 对于只在栈上分配的对象，实现 Copy trait
        - e.g. 基础数据类型, 以及 基础数据类型的turple, Array (默认实现Copy)
        - e.g. struct / enum
    - 对于涉及堆分配的对象，实现 Clone trait
        - vector, string

所以，基本不用担心 不小心 copy一个1000w 元素的vector了。

<h2 id="6e2d9dc6b0fd3ca3d9187b28356a14a1"></h2>

## 显式参数传递

Rust 将一切由隐式转变为显式

```rust
let mut x = 10;

foo(x);  // pass by move, x cannot be used after the call
foo(&x);  // pass by immutable reference
foo(&mut x); // pass by mutable reference
```

<h2 id="37f632d52f26580ac35300665eb0c336"></h2>

## 内置格式化与lint

cargo 内置了`cargo fmt`和`cargo clippy`，一键格式化与`lint`，再也不用人工配置clang-format和clang-tidy了。

<h2 id="3057f5c2a8db24c9bb71fdec9215a6f7"></h2>

## 标准化的开发流程和包管理

cargo还原生支持了test与benchmark

```rust
cargo test
cargo bench
```

cargo规定了目录风格

```bash
benches  // benchmark代码go here
src
tests  // ut go here
```

<h2 id="e36527b4c0bbfae1bd75d9a1bb4ef9ac"></h2>

## lifetime安全性

unique ownership + borrow check , 能够有效的避免pointer/iterator invalidation bug以及aliasing所引发的性能问题。

此外,Rust引入了lifetime概念, 每个变量有个lifetime。当多个变量间存在引用关系时，编译器会检查这些变量之间的lifetime关系，禁止一个非owning引用，在其原始对象lifetime结束之后再被访问。

<h2 id="1490ba65e4fc8d6223c53f44ac803091"></h2>

## 边界安全性

Rust标准库会进行bound check。

<h2 id="2e321cbfdd07269096af86370e25f590"></h2>

## 类型安全性

Rust默认强制变量初始化，并且禁止隐式类型转换。

```rust
let i: i32;

if rand() < 10 {
    i = 10;
}

println!("i is {}", i);  // do not compile: i is not always initialized
```

<h2 id="94b62a30b8785a22312db949fef9b43c"></h2>

## 多线程安全性

Rust的多线程安全性，完全是通过库机制来实现的。

两个基础概念:

1. Send
    - 此类型的对象的所有权，可以跨线程传递。
    - 当一个新类型的所有成员都是Send时，这个类型也是Send的。
        - 几乎所有内置类型和标准库类型都是Send的，
        - Rc（类似local shared_ptr）除外，因为内部用的是普通int来计数。
2. Sync
    - 此类型允许多个线程共享（Rust中，共享一定意味着**不可变**引用，即通过其不可变引用进行并发访问）。

通过Send/Sync与ownership模型，Rust让Data race完全无法出现。

简单来说：

- lifetime机制要求：一个对象要跨线程传递时，必须使用Arc（Atomic Reference Counted）来封装（Rc不行，因为它被特别标注为了!Send，即不可跨线程传递）
- ownership+borrow机制要求：Rc/Arc包装的对象，只允许解引用为不可变引用，而多线程访问一个不可变对象，是天生保证安全的。
- ownership+borrow机制要求：Rc/Arc包装的对象，只允许解引用为不可变引用，而多线程访问一个不可变对象，是天生保证安全的。
    - ownership+borrow机制要求：Rc/Arc包装的对象，只允许解引用为不可变引用，而多线程访问一个不可变对象，是天生保证安全的。
    - 如果同时需要共享和可变，需要使用额外的机制，Rust官方称之为内部可变性，实际上叫共享可变性可能更容易理解，它是一种提供安全变更共享对象的机制。
    - 如果需要多线程去变更同一个共享对象，必须使用额外的同步原语（RefCell/Mutex/RwLock）.
    - RefCell是与Rc一起使用的，用于单线程环境下的共享访问。RefCell被特别标注为了!Sync，意味着，如果它和Arc一起使用，Arc就不是Send了，从而`Arc<RefCell<T>>`无法跨线程。

e.g. 我实现了一个Counter对象，希望多个线程同时使用

```rust
struct Counter {
    counter: i32
}

fn main() {
    let counter = Arc::new(Mutex::new(Counter{counter: 0}));
    let c = Arc::clone(&counter);
    thread::spawn(move || {
        let mut x = c.lock().unwrap();

        x.counter += 1;
    });
}
```


<h2 id="4ae3bd7ed074efb0e2e46948479a41b3"></h2>

## 统一的错误处理

Rust的方案与Herb提出的static异常类似，并且通过语法糖，让错误处理非常容易。

```rust
enum MyError
{
    NotFound,
    DataCorrupt,
    Forbidden,
    Io(std::io::Error)
}

impl From<io::Error> for MyError {
    fn from(e: io::Error) -> MyError {
        MyError::Io(e)
    }
}

pub type Result<T> = result::Result<T, Error>;

fn main() -> Result<()>
{
    let x: i32 = foo()?;
    let y: i32 = bar(x)?;

    foo();  // result is not handled, compile error

     // use x and y
}

fn foo() -> Result<i32>
{
    if (rand() > 0) {
        Ok(1)
    } else {
        Err(MyError::Forbidden)
    }
}
```

错误处理一律通过`Result<T, ErrorType>`来完成，通过`?`，一键向上传播错误（如同时支持自动从ErrorType1向ErrorType2转换，前提是你实现了相关trait），没有错误时，自动解包。当忘记处理处理Result时，编译器会报错。



