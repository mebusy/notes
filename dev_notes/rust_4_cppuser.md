
# Rust for C++ user

## 默认不可变

## 禁止整数隐式转换

```rust
fn foo(x: u32) {}

let x: i32 = 0;
foo(x);  // error
```

## 简化构造、复制与析构

C++中RAII的Rule of 0, or 3, or 5 "大名鼎鼎", 明明是一件非常常规的东西，确搞得非常的复杂。 

Rust非常简单。

- 所以对象默认只支持Destructive move（通过memcpy完成）


