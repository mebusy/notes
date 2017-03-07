


# 2

## 2.4  Graph as data structure

 - Connectitiy matrix (also distances)
    - often used for dense graph
 - Edge List Representation 
    - often used for sparse graph
    - Most real world problems are relatively sparse
 - Tradeoffs - Graph as an ADT 

### List representation 

A representation of a directed graph with n vertices can use a list , for example , an array of n lists of vertices.

 - Definition: A representation of a ***directed graph*** with *n* vertices using an array of *n* lists of vertices.
 - List *i* contains vertex *j* if there is an edge from vertex *i* to vertex *j*.
 - A ***weighted graph*** may be represented with a list of vertex / weight pairs.
 - An ***undirected graph*** my be represented by having vertex *j* in the list for vertex *i* , and vertex *i* in the list for vertex *j*.

 
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

### Dijkstra shortest path

We're going to use undirected graphs with weights(cost). So costs are going to all be non-negative.


# C++ B

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

## 1.6 Bidiretional Iterator 

Iteractor both support ++ and -- operator.

## 1.7 Random Acess Iteractor

```c++
#include <cstddef>   //ptrdiff_t

template <typename RandomAccess>
RandomAcess pickRandEI( RandomAccess first , RandomAccess last ) {
    ptrdiff_t temp = last - first ;
    return first + rand() % temp ;   
}
```


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


## 1.10 STL:Algorithms Library

Sorting Algorithm Prototypes

 - template<class RandAcc> void sort(RandAcc b, RandAcc e) ;
    - quicksort algorithm over elements b to e 
 - template<class RandAcc> void stablesort(RandAcc b, RandAcc e) ;
    - Stable sorting algorithm over elements b to e
    - elements remain in their relative same position

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

## 1.12 Lambda Expressions : for_each Function

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

### lambda c++11

 - [] : lambda 
    - // goest where the function object is required
    - [](int n) {return n\*5.5;}   // double returned
        - deduces the return value -- no return void
    - [](int n) -> int {return ++n} ;  // explicit


### Mutating Function

 - template <class InputIter,class OutputIter> 
 - OutputIter copy ( InputIter b1, InputIter e1 , OutputIter b2 );
    - copying algorithm over elements b1 to e1
        - copy is placed starting at b2
        - Position returned is end of copy


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

## 1.14 Functional Objects

 - Function objects are clases that have `operator()` defined 
 - sum = accumulate( v1, v1+3, 0.0 , minus<int>() ) ;  // sum = -7

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


## 1.15 Define Function Object Classes:  Function Adapters

 - Function Adapters
    - Creation of function objects using adaption
    - Negators for negating predicate objects
    - Binders for binding a function argument
    - Adapters for pointer to function 













