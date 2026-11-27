[](...menustart)

- [CPP SIMD (c++26?)](#2dec7764279c7dd113659165e18cce15)
    - [Synopsis](#24da3c4b755f1bb2b7cc2c32ee6751b3)
    - [Constructor examples](#19f52f7a190df07ef49dd0f7f93a0482)
    - [Arithmetic & math](#50044e767de894f1f4ec3a6db31d34b8)
    - [Same for compares (element-wise)](#e7322018b1be7ce8be700c52cc9ed834)
    - [Reductions](#9a819585a6c0017acaff053c740cec70)

[](...menuend)


<h2 id="2dec7764279c7dd113659165e18cce15"></h2>

# CPP SIMD (c++26?)

[pdf](https://github.com/CppCon/CppCon2023/blob/main/Presentations/stdsimd_how_to_express_inherent_parallelism_efficiently_via_data_parallel_types.pdf)

<h2 id="24da3c4b755f1bb2b7cc2c32ee6751b3"></h2>

## Synopsis

- `std::simd<T>::size()`  is a constant expression, denoting the number of elements,
    - A default size() is chose by the implementaion, depending on compiler flags
- T must be a vectoriable type  , except `bool` or `long double`
    - for bool, use `std::simd_mask<T>`
- Abi determines width and ABI (i.e.  how parameters are passed to functions)
    - example: `std::simd<int, 8>` on x86 can be two xmm registers (alignof == 16) or one ymm register (alignof == 32).


<h2 id="19f52f7a190df07ef49dd0f7f93a0482"></h2>

## Constructor examples

```cpp
std::simd<int> x0; // uninitialized
std::simd<int> x1{}; // 0s
std::simd<int> x2 = 1; // 1s
std::simd<int> x3(it);  // it[0], it[1], it[2], it[3], ...
std::simd<int> iota([](int i) { return i; }); // 0, 1, 2, 3, ...
```


<h2 id="50044e767de894f1f4ec3a6db31d34b8"></h2>

## Arithmetic & math

```cpp
void f(std::simd<float> x, std::simd<float> y) {
    x += y; // x.size() additions
    x = sqrt(x); // x.size() square roots
    ...
// etc. all operators and <cmath>
}
```

<h2 id="e7322018b1be7ce8be700c52cc9ed834"></h2>

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


<h2 id="9a819585a6c0017acaff053c740cec70"></h2>

## Reductions

- simd_mask reductions
    - `all_of`, `any_of`, `none_of`
    - reduce_count, reduce_min_index, reduce_max_index
- simd reductions
    - reduce, reduce_min, reduce_max

```cpp
void f(std::simd<float> x) {
    float sum = reduce(x); // sum of all elements
    float min = reduce_min(x); // min of all elements
    float max = reduce_max(x); // max of all elements
    int count = reduce_count(x < 0); // count of elements < 0
    float product = reduce(x, 1.0f, std::multiplies<float>()); // product of all elements
}
```
