# immintrin.h

## AVX: Advanced Vector Extensions


The C/C++ AVX intrinsic functions are in the header "immintrin.h".

AVX uses dedicated 256-bit registers, with these C/C++ types:

- __m256 for floats
- __m256d for doubles
- __m256i for ints (int support was actually added in "AVX2")

There is also 128bit version, __m128, __128d, __m128i,  and 512bit version(may not support all CPUs), __m512, __m512d, __m512i.
 

The 256 bit (32 byte) registers have enough space to store:

- 8 single-precision floats (_ps, Packed Single-precision)
- 4 double-precision floats (_pd, Packed Double-precision)
- 32 8-bit integers ( _epi8 signed char, or _epu8 unsigned char)
- 16 16-bit integers (_epi16 signed short, or _epu16 unsigned short)
- 8 32-bit integers (_epi32, Packed signed Integer, or _epu32, Packed Unsigned integer)
- 4 64-bit integers (_epi64 signed long)

For example, here's how you operate on 8 floats at a time, using dedicated AVX _mm256 intrinsic functions.  Note how we're using _ps instructions both for load and add.

```cpp
#include "immintrin.h"

void foo(void)
{
	float f[8]={1.0,2.0,1.2,2.1, 5.2,5.3,10.1,11.0};
	
	__m256 v=_mm256_load_ps(&f[0]);
	v=_mm256_add_ps(v,v);
	_mm256_store_ps(&f[0],v);
	
	farray_print(f,8);
}
```

And here's how you operate on 8 ints at a time.  For ints, the arithmetic uses _epi32, and the load and store use the weird _si256 type, which just means one giant 256-bit block of integer data.


```cpp
#include "immintrin.h"
void foo(void)
{
	int f[8]={1,2,0,3, 5,5,10,11};
	
	__m256i v=_mm256_load_si256((const __m256i *)&f[0]);
	v=_mm256_add_epi32(v,v);
	_mm256_store_si256((__m256i *)&f[0],v);
	
	iarray_print(f,8);
}
```


## Using AVX to Speed Up Array Code

Usually it's as easy as just operating on 8 iterations of the loop at a time!  But there are often minor complications, like scalar values that need to be broadcast to fill all 8 slots:

```cpp
#include "immintrin.h"

const int n=1024;
float a[n], b[n];
float c=3.0;

long foo(void) {
	bool use_AVX=true;
	if (use_AVX) 
	{ // fancy AVX loop:
		__m256 C=_mm256_broadcast_ss(&c); // splat c across all SIMD lanes
		for (int i=0;i<n;i+=8) {
			// b[i]=a[i]*c;
			__m256 A=_mm256_load_ps(&a[i]);
			__m256 B=_mm256_mul_ps(A,C);
			_mm256_store_ps(&b[i],B);
		}
	}
	else
	{ // simple float loop: 
		for (int i=0;i<n;i++) {
			b[i]=a[i]*c;
		}
	} 
	
	return b[0];
}
```

On my Skylake machine, using AVX takes only 44ns to compute 1000 floats; the simple float loop takes 294ns (a 6.68x speedup!).

Where things get really tricky is when each float wants to do its own separate operations, like per-float branching.  AVX handles branches exactly like SSE .

## Alignment in AVX

AVX instructions expect input operands to be aligned on a 32-byte boundary.  

On most 32-bit systems, malloc and new only return pointers aligned to an 8-byte boundary, which caused problems for SSE, which expected 16-byte alignment.  So on most 64-bit systems, malloc and new always return data aligned to a 16-byte boundary--half the time you'll also be lucky and your inputs will also be aligned on a 32-byte boundary, but half the time you won't and your AVX code will crash.

If you're doing allocations yourself, C style, the function "_mm_malloc(size_in_bytes,32)" will return you a 32-byte aligned pointer, and it's available in the same Intel headers as the other _mm_ intrinsics.  

For std::vector, you should use an aligning allocator like my [osl/alignocator.h](https://github.com/olawlor/osl/blob/master/alignocator.h) as an additional template argument:

```cpp
   std::vector<float, alignocator<float,32> > myVec;
```

If you don't do this, your first AVX load has a 50% chance of crashing.

Of course, you still need to advance by 32 bytes / 8 floats from the start of the vector.

## SSE/AVX intrinsic functions


SSE/AVX intrinsic functions 的命名习惯如下

```cpp
__<return_type> _<vector_size>_<intrin_op>_<suffix>
```

```cpp
__m128 _mm_set_ps (float e3, float e2, float e1, float e0)
__m256 _mm256_add_pd (__m256 a, __m256 b)
__m512 _mm512_max_epi64 (__m512 a, __m512 b)
```

1. return_type, 如 m128、m256 和 m512 代表函数的返回值类型，m128 代表128位的向量，m256代表256位的向量，m512代表512位的向量。
2. vector_size , 如 mm、mm256 和 mm512 代表函数操作的数据向量的位长度，mm 代表 128 位的数据向量（SSE），mm256 代表256位的数据向量（AVX 和 AVX2）, mm512 代表512位的数据向量。
3. intrin_op，如 set、add 和 max 非常直观的解释函数功能。函数基础功能可以分为数值计算、数据传输、比较和转型四种， 请参阅 [intel Instrinsics Guild](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html#avxnewtechs=AVX2)
4. suffix, 如ps、pd、epi64代表函数参数的数据类型，其中 p = packed，s = 单精度浮点数，d = 双精度浮点数
    - ps: 由float类型数据组成的向量
    - pd:由double类型数据组成的向量
    - epi8/epi16/epi32/epi64: 由8位/16位/32位/64位的有符号整数组成的向量
    - epu8/epu16/epu32/epu64: 包含8位/16位/32位/64位的无符号整数组成的向量
    - si128/si256: 未指定的128位或者256位向量

[知乎 玩转SIMD指令](https://zhuanlan.zhihu.com/p/591900754)



