# CPP SIMD

[pdf](https://github.com/CppCon/CppCon2023/blob/main/Presentations/stdsimd_how_to_express_inherent_parallelism_efficiently_via_data_parallel_types.pdf)

## Synopsis

- `std::simd<T>::size()`  is a constant expression, denoting the number of elements,
    - A default size() is chose by the implementaion, depending on compiler flags
- T must be a vectoriable type  , except `bool` or `long double`
    - for bool, use `std::simd_mask<T>`
- Abi determines width and ABI (i.e.  how parameters are passed to functions)
    - example: `std::simd<int, 8>` on x86 can be two xmm registers (alignof == 16) or one ymm register (alignof == 32).


## Constructor examples

```cpp
std::simd<int> x0; // uninitialized
std::simd<int> x1{}; // 0s
std::simd<int> x2 = 1; // 1s
std::simd<int> x3(it);  // it[0], it[1], it[2], it[3], ...
std::simd<int> iota([](int i) { return i; }); // 0, 1, 2, 3, ...
```


## Arithmetic & math

```cpp
void f(std::simd<float> x, std::simd<float> y) {
    x += y; // x.size() additions
    x = sqrt(x); // x.size() square roots
    ...
// etc. all operators and <cmath>
}
```

## Same for compares (element-wise)

```cpp
void f(std::simd<float> x, std::simd<float> y) {
    if (x < y) { x = y; } // nonono, you don’t write ’if (truefalsetruetrue)’ either
    x = simd_select(x < y, y, x); // x = y but only for the elements where x < y
    if (all_of(x < y)) {...} // this makes sense, yes
}
```

- Comparisons return simd_mask
- simd_mask is not convertible to bool
- simd_mask can be reduced to bool via all_of, any_of, none_of


