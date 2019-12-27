...menustart

 - [2](#c81e728d9d4c2f636f067f89cc14862c)
     - [2.4  Graph as data structure](#8b8ba54e7ed58d6969a51a91d54e1545)
         - [List representation](#eabdefffaadf27a2e17eac89b418d03c)
         - [Matrix vs. list directed graph](#3304451984d7d4ffea5486e84e449302)
         - [Dijkstra shortest path](#227230825bf5db0b29a77b5e8f635b19)
 - [C++ B](#3a82c7106488509941d71fa688027345)
     - [1.4 Iterator Categories](#5f12fc29b222aa9424266e81f94a342f)
     - [1.6 Bidiretional Iterator](#7ea3be90d2db0c633e1a4bb97b65fbb6)
     - [1.7 Random Acess Iteractor](#b199fd823ad561a75c1164f72f3a25da)
     - [1.9 Associative Containers](#38835a39d07b751a0f52392548224352)
     - [1.10 STL:Algorithms Library](#b99045ec5edde01d7405cdd9d484e67c)
     - [1.11 Non-mutating Algorithm](#9d2a97889138dd384b60bcde90d22559)
     - [1.12 Lambda Expressions : for_each Function](#8c9a9aba5d3082f61648829828108863)
         - [old style for_each()](#1dc1f865d68d3023ddd5ccccd3fe2f88)
         - [lambda c++11](#f846829c9d3760db36427428211f1e0b)
         - [Mutating Function](#2a200b3f9c1c0b836ece23a6ea362f17)
     - [1.13 Numerical algorithms](#9220fb7c282f0c6605d9f35e13c57944)
     - [1.14 Functional Objects](#e87d732617748bf074865fbbce1a4582)
         - [Generator Object](#2025d93d18bf7503037e013bbfda141a)
     - [1.15 Define Function Object Classes:  Function Adapters](#3861b29161427b38210b5fdbbffa7a1b)
     - [2.3 Basic of Inheritance](#de828ad4dbe13bf1a9930b26a5aa502e)
     - [2.4 C++11 Feature : "final"](#62083d2f266cdfad9baa4aaa5ce8531d)
     - [2.14 Virtual Function Selection](#20281bb92cdbc42ed96aaafa8336dba8)
     - [2.15 Virtual Confusion with Overloading](#18ee821d94f99da3b611714b62c27a81)
         - [Restrictions on Virtual Functions](#80ec8c1aa9d77641d66b2d65f1a819b3)
     - [3.2 Some Further Constructors](#a86bfb8c341e12c9b614fd2a4c94c24e)
     - [3.10 Abstract Base Class = 0  Notation](#fe7f80120156a50493bf86436ed5dedf)
     - [4.6 Asserts and Exceptions](#3b7f38abea242fd2c0d2de96986f2551)
     - [4.8 Exception](#022c2a7f8dad1e47d6f88eade9351b64)
     - [4.10 C++11 Standard](#5be82f8b49f7de553e3463e57899e4e6)
     - [4.11 Thread](#f38f209014f0a6500ff416757a4c9a4d)
     - [4.12 tuple](#8e4f88e4e3418d17c64f080cd4b28cef)

...menuend


<h2 id="c81e728d9d4c2f636f067f89cc14862c"></h2>


# 2

<h2 id="8b8ba54e7ed58d6969a51a91d54e1545"></h2>


## 2.4  Graph as data structure

 - Connectitiy matrix (also distances)
    - often used for dense graph
 - Edge List Representation 
    - often used for sparse graph
    - Most real world problems are relatively sparse
 - Tradeoffs - Graph as an ADT 

<h2 id="eabdefffaadf27a2e17eac89b418d03c"></h2>


### List representation 

A representation of a directed graph with n vertices can use a list , for example , an array of n lists of vertices.

 - Definition: A representation of a ***directed graph*** with *n* vertices using an array of *n* lists of vertices.
 - List *i* contains vertex *j* if there is an edge from vertex *i* to vertex *j*.
 - A ***weighted graph*** may be represented with a list of vertex / weight pairs.
 - An ***undirected graph*** my be represented by having vertex *j* in the list for vertex *i* , and vertex *i* in the list for vertex *j*.

 
<h2 id="3304451984d7d4ffea5486e84e449302"></h2>


### Matrix vs. list directed graph

```
1 1 1 1
1 0 0 0
0 1 0 1
0 1 1 0 
```

```
1 2 3 4
1
2 4
2 3
```

<h2 id="227230825bf5db0b29a77b5e8f635b19"></h2>


### Dijkstra shortest path

We're going to use undirected graphs with weights(cost). So costs are going to all be non-negative.


<h2 id="3a82c7106488509941d71fa688027345"></h2>


# C++ B

<h2 id="5f12fc29b222aa9424266e81f94a342f"></h2>


## 1.4 Iterator Categories

```c++
template <typename ForwardIterator>
void square( ForwardIterator first, ForwardIterator last ) {
    for(; first!=last; first++)    
        *first= (*first) * (*first) ;
}

...

square(w.begin(), w.end() ); 
for (auto i:w) ...
```

<h2 id="7ea3be90d2db0c633e1a4bb97b65fbb6"></h2>


## 1.6 Bidiretional Iterator 

Iteractor both support ++ and -- operator.

<h2 id="b199fd823ad561a75c1164f72f3a25da"></h2>


## 1.7 Random Acess Iteractor

```c++
#include <cstddef>   //ptrdiff_t

template <typename RandomAccess>
RandomAcess pickRandEI( RandomAccess first , RandomAccess last ) {
    ptrdiff_t temp = last - first ;
    return first + rand() % temp ;   
}
```


<h2 id="38835a39d07b751a0f52392548224352"></h2>


## 1.9 Associative Containers

map Program

```c++
#include <map>
#include <unordered_map>
...

int main() {
    map<unsinged long,string> worker;
    unordered_map<unsigned long, unsigned> payroll;
    
    worker[992342]  = "Harold Fish" ;
    payroll[992342] = 2030 ;
    ...      
}

```


<h2 id="b99045ec5edde01d7405cdd9d484e67c"></h2>


## 1.10 STL:Algorithms Library

Sorting Algorithm Prototypes

 - template<class RandAcc> void sort(RandAcc b, RandAcc e) ;
    - quicksort algorithm over elements b to e 
 - template<class RandAcc> void stablesort(RandAcc b, RandAcc e) ;
    - Stable sorting algorithm over elements b to e
    - elements remain in their relative same position

<h2 id="9d2a97889138dd384b60bcde90d22559"></h2>


## 1.11 Non-mutating Algorithm

 - template <class InputIter, Class T> InputIter find ( InputIter b, InputIter e, const T& t ) ;
    - Finds position of t in range b to e
 - template <class InputIter, Class Predicate> InputIter find_if ( InputIter b, InputIter e, Predicate t ) ;
    - Finds position of first element that makes predicate true in range b to e , otherwise position e returned
    - eg. find first element > 1000
 - template <class InputIter, Class Function> void for_each ( InputIter b,InputIter e,  Function f ) ;
    - apply f to each value found in range b to e
    

Example:

```
string words[5] = ... 
string* where ;

sort(words , words+5) ;
where = find(words, words+5, "hop") ;

```

<h2 id="8c9a9aba5d3082f61648829828108863"></h2>


## 1.12 Lambda Expressions : for_each Function

<h2 id="1dc1f865d68d3023ddd5ccccd3fe2f88"></h2>


### old style for_each()

```c++
#include <algorithm>
#include <vector>
using namespace std;      
void incr(int &i) {static int n=1 ; i=n++;}

int main() {
    vector<int> v(6);
    for_each( v.begin(), v.end(), incr )    
}
```

<h2 id="f846829c9d3760db36427428211f1e0b"></h2>


### lambda c++11

 - [] : lambda 
    - // goest where the function object is required
    - `[](int n) {return n * 5.5;}`   // double returned
        - deduces the return value -- no return void
    - `[](int n) -> int {return ++n}` ;  // explicit


<h2 id="2a200b3f9c1c0b836ece23a6ea362f17"></h2>


### Mutating Function

 - template <class InputIter,class OutputIter> 
 - OutputIter copy ( InputIter b1, InputIter e1 , OutputIter b2 );
    - copying algorithm over elements b1 to e1
        - copy is placed starting at b2
        - Position returned is end of copy


<h2 id="9220fb7c282f0c6605d9f35e13c57944"></h2>


## 1.13 Numerical algorithms

 - Sums
    - template <class InputIter , class T, class BinOp>
    - T accumulate( InputIter b, InputIter e, T t, BinOp bop ) ; 
        - accumulation whose sum is initially t 
        - successive elements from range b to e are summed , with sum = bop(sum, element )
        - so can be not only + but also all binary operation.
 - Inner product
 - Adjacent difference
 - Numerical algorithm function behave as expected on numerical types where + and \* are defined.


```c++
int main() {
    double v1[3] = {1.0, 2.5, 4.6} ;
           v2[3] = {1.0, 2.0, -3.5} ;   
    double sum, inner_p ; 

    sum = accumulate( v1, v1+3, 0.0 ) ;
    inner_p = inner_product(v1, v1+3 , v2, 0.0);
}
```

<h2 id="e87d732617748bf074865fbbce1a4582"></h2>


## 1.14 Functional Objects

 - Function objects are clases that have `operator()` defined 
 - `sum = accumulate( v1, v1+3, 0.0 , minus<int>() ) ;  // sum = -7`

<h2 id="2025d93d18bf7503037e013bbfda141a"></h2>


### Generator Object

```c++
class gen {
  public :
    gen(double x_zero, double increment) :x(x_zero)  , incr(increment) {}
    double operator()() { x+= incr; return x*x } ;
  private:
    double x, incr;   
}
```

 - `operator()`  means overload function
 - next `()` means parameter in this case is void


<h2 id="3861b29161427b38210b5fdbbffa7a1b"></h2>


## 1.15 Define Function Object Classes:  Function Adapters

 - Function Adapters
    - Creation of function objects using adaption
    - Negators for negating predicate objects
    - Binders for binding a function argument
    - Adapters for pointer to function 

<h2 id="de828ad4dbe13bf1a9930b26a5aa502e"></h2>


## 2.3 Basic of Inheritance

```
class point: public duo {
    ...
    }
```

<h2 id="62083d2f266cdfad9baa4aaa5ce8531d"></h2>


## 2.4 C++11 Feature : "final"
 
```
class point3d final : public point { // no further inheritance
...
```


<h2 id="20281bb92cdbc42ed96aaafa8336dba8"></h2>


##  2.14 Virtual Function Selection

 - normal overrided function in the derived class , got selected based on , not the instance being pointed to , but instead the type of pointer. 
 - Typically base has virtual function and derived has their versions for function
 - Pointer to base class can point at either base or derived class objects
 - Member function selected depends on class of object being pointed at, not on pointer type
 - In absence of derived type member , base class virtual function used by default 

---

 - 派生类对象也“是”基类对象，但两者不同。
    - 派生类对象可以当做基类对象，这是因为派生类包含基类的所有成员。
    - 但是基类对象无法被当做成派生类对象，因为派生类可能具有只有派生类才有的成员。
    - 所以，将派生类指针指向基类对象的时候要进行显示的强制转换，否则会使基类对象中的派生类成员成为未定义的。
 - 总结：基类指针和派生类指针指向基类对象和派生类对象的4中方法：
    - 基类指针指向基类对象，简单。只需要通过基类指针简单地调用基类的功能。
    - 派生类指针指向派生类对象，简单。只需要通过派生类指针简单地调用派生类功能。
    - 将基类指针指向派生类对象是安全的，因为派生类对象“是”它的基类的对象。
        - 但是要注意的是，这个指针只能用来调用基类的成员函数。如果试图通过基类指针调用派生类才有的成员函数，则编译器会报错
        - 为了避免这种错误，必须将基类指针强制转化为派生类指针。然后派生类指针可以用来调用派生类的功能。这称为向下强制类型转换，这是一种潜在的危险操作。
        - 如果在基类和派生来中定义了虚函数（通过继承和重写），并同过基类指针在派生类对象上调用这个虚函数，则实际调用的是这个函数的派生类版本。
    - 将派生类指针指向基类对象，会产生编译错误 


<h2 id="18ee821d94f99da3b611714b62c27a81"></h2>


## 2.15 Virtual Confusion with Overloading 

基类 有虚函数重载，派生类 要避免 override 这个overload 的部分方法，否则会出现混乱

<h2 id="80ec8c1aa9d77641d66b2d65f1a819b3"></h2>


### Restrictions on Virtual Functions 

 - only non-static member functions virtual 
 - virtual characteristic is inherited 
    - derrived class function automatically virtual ,  virtual keyword ont needed
 - Constructors can not be virtual 
 - but destructors can be virtual. 
 

<h2 id="a86bfb8c341e12c9b614fd2a4c94c24e"></h2>


## 3.2 Some Further Constructors

```
explicit my_container (T * b ) : my_container()  {
    ...}
```

 - explicit : recall , turn off conversion 
 - `: my_container` : derived from other constructor, reuse code


<h2 id="fe7f80120156a50493bf86436ed5dedf"></h2>


## 3.10 Abstract Base Class = 0  Notation 

```
class LeafNode: public Node {
    friend class Tree ;
    void print( ostream& o  ) = 0 ;
    virtual int eval() = 0 ;   
}
```

 - abstract function is still undetermined , still without definition , we need to override it.


<h2 id="3b7f38abea242fd2c0d2de96986f2551"></h2>


## 4.6 Asserts and Exceptions

 - Static_asserts added to C++ 11  allow ***compiler*** to statically test conditions
 - `static_assert( bool_constexpr , string )`
    - bool_constexpr  : a boolean constant expression evaluated at compile time
    - string : your error message,  string literal that will be a compiler error if bool_constexpr is false 


<h2 id="022c2a7f8dad1e47d6f88eade9351b64"></h2>


## 4.8 Exception 

 - `throw your_string_message`
    - eg, `throw "This will Abort";`

```c++
try {
    ...
} catch() {
    ...   
}
```

<h2 id="5be82f8b49f7de553e3463e57899e4e6"></h2>


## 4.10 C++11 Standard

 - tuple  -- pair and more
 - array  -- fixed length array container
 - forward_list -- single pointer list
 - unordered_map, unordered_set  -- hashing used
 - thread  -- uniform thread interface + other libraries
 - regex  -- regular expressions
 - type traits  -- type characteristics 

<h2 id="f38f209014f0a6500ff416757a4c9a4d"></h2>


## 4.11 Thread 

 - `<thread>`
 - related lib 
    - `<mutex>`
    - `<future>` 
    - `<atomic>`
    - `<condition_variable>`

<h2 id="8e4f88e4e3418d17c64f080cd4b28cef"></h2>


## 4.12 tuple 

```
#include <tuple>

...

tuple<double , double, double> p ; 

...

p = make_tuple( 0,0,0 ) ;

... 

double firstElem = get<0>(p) ;

```
     





