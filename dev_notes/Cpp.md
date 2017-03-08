


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

## 2.3 Basic of Inheritance

```
class point: public duo {
    ...
    }
```

## 2.4 C++11 Feature : "final"
 
```
class point3d final : public point { // no further inheritance
...
```


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


## 2.15 Virtual Confusion with Overloading 

基类 有虚函数重载，派生类 要避免 override 这个overload 的部分方法，否则会出现混乱

### Restrictions on Virtual Functions 

 - only non-static member functions virtual 
 - virtual characteristic is inherited 
    - derrived class function automatically virtual ,  virtual keyword ont needed
 - Constructors can not be virtual 
 - but destructors can be virtual. 
 








