
# C VS C++

## c++ was designed to
 
 - be a “better C”
 - support data abstraction
 - support object-oriented programming
 - support generic programming

## character literals

 - In C++, character literals are chars
    - `sizeof('c') == sizeof(char) == 1`
 - In C, character literals are ints
    - `sizeof('c') == sizeof(int)` 

## function declare

 - C++ has strict prototyping
    - `void func(); // function which accepts no arguments`
 - In C
    - `void func();` 没有参数说明的函数声明，may accept any number of arguments

## Function overloading

 - C++ supports function overloading
 - c 本身没有函数重载
    - 但是可以通过可变参数 来部分实现函数重载

## c headers

 - C standard headers are available in C++,
 - but are prefixed with "c" and have no .h suffix.

```cpp
#include <cstdio>     
```

## Namespaces

 - c++ 
 - Namespaces provide separate scopes for variable, function,  and other declarations.
 - Namespaces can be nested.

```cpp
namespace First {
    namespace Nested {
        void foo() {
            printf("This is First::Nested::foo\n");
        }
    } // end namespace Nested
} // end namespace First

namespace Second {
    void foo() {
        printf("This is Second::foo\n");
    }
}

void foo() {
    printf("This is global foo\n");
}

int main()
{
    // Includes all symbols from namespace Second into the current scope. 
    // Note that simply foo() no longer works, since it is now ambiguous whether
    // we're calling the foo in namespace Second or the top level.
    using namespace Second;

    Second::foo(); // prints "This is Second::foo"
    First::Nested::foo(); // prints "This is First::Nested::foo"
    ::foo(); // prints "This is global foo"
    // foo(); // compile error 
}
```

## Input/Output

 - C++ input and output uses streams
 - cin, cout, and cerr represent stdin, stdout, and stderr.
 - `<<` is the insertion operator and `>>` is the extraction operator.

```cpp
#include <iostream> // Include for I/O streams
// Streams are in the std namespace (standard library)
using namespace std; 

int main() {
   int myInt;

   // Prints to stdout (or terminal/screen)
   cout << "Enter your favorite number:\n";
   // Takes in input
   cin >> myInt;

   // cout can also be formatted
   cout << "Your favorite number is " << myInt << "\n";
   // prints "Your favorite number is <myInt>"

    cerr << "Used for error messages";
}
```

## Strings

 - Strings in C++ are objects and have many member functions

```cpp
#include <string>
// Strings are also in the namespace std (standard library)
using namespace std; 

string myString = "Hello";
// + is used for concatenation.
cout << myString + " You"; // "Hello You"
// C++ strings are mutable.
myString.append(" Dog");
```

## References

 - In addition to pointers like the ones in C, C++ has _references_.
 - These are pointer types that cannot be reassigned once set and cannot be null.
 - They also have the same syntax as the variable itself:
    - No \* is needed for dereferencing and
    - & (address of) is not used for assignment.
 - Q: 为什么c++ 有了指针还要引入 引用
    - C++ inherited pointers from C , so I couldn't remove them without causing serious campatibility.
    - References are useful for serval things, but **the direct reason I introduced them in C++ was to support operator overloading**.
    - 其他好处
        - 不担心 NULL 的问题，写代码方便（不需要 * 来 dereference ）

 - Q: 为什么不能用指针实现 operator overloading？
    - 因为 \*pointer 这个表达式很有可能并不是直接取值的意思，因为\* 也可能会被重载
 - 

```cpp
using namespace std;

string foo = "I am foo";
string bar = "I am bar";

string& fooRef = foo; // This creates a reference to foo.
fooRef += ". Hi!"; // Modifies foo through the reference

cout << &fooRef << endl; //Prints the address of foo
fooRef = bar; // his is the same as "foo = bar", and foo == "I am bar"
cout << &fooRef << endl; //Still prints the address of foo
// Just work like string
// The address of fooRef remains the same, i.e. it is still referring to foo.


const string& barRef = bar; // Create a const reference to bar.
// Like C, const values (and pointers and references) cannot be modified.
barRef += ". Hi!"; // Error, const references cannot be modified.
```

## Enums

 - Enums are a way to assign a value to a constant most commonly used for 
 - easier visualization and reading of code

```cpp
enum ECarTypes
{
  Sedan,
  Hatchback,
  SUV,
  Wagon
};

ECarTypes GetPreferredCarType()
{
    return ECarTypes::Hatchback;
}
```

## Classes and object-oriented programming

 - Classes are usually declared in header (.h or .hpp) files.

```cpp
// Declare a class.
class Dog {
    // Member variables and functions are private by default.
    std::string name;

public:

    // Default constructor
    Dog();

    // Note that we use std::string here instead of placing 'using namespace std;' above
    // Never put a "using namespace" statement in a header.
    // anyways you can put 'using namespace' if you insist ...
    void setName(const std::string& dogsName); 

    // Functions that do not modify the state of the object
    // should be marked as const.
    // This allows you to call them if given a const reference to the object.
    virtual void print() const;

    // Functions can also be defined inside the class body.
    // Functions defined as such are automatically 'inlined'.
    void bark() const { std::cout << name << " barks!\n"; }

    // destructors are called when an object is deleted or falls out of scope.
    // The destructor should be virtual if a class is to be derived from;
    // if it is not virtual, then the derived class' destructor will 
    // not be called if the object is destroyed through a base-class reference or pointer.
    virtual ~Dog();
};// A semicolon must follow the class definition.

// Class member functions are usually implemented in .cpp files.
Dog::Dog() {
    std::cout << "A dog has been constructed\n";
}

// Notice that "virtual" is only needed in the declaration, not the definition.
void Dog::print() const {
    std::cout << "Dog is " << name << " and weighs " << weight << "kg\n";
}

Dog::~Dog() {
    std::cout << "Goodbye " << name << "\n";
}

// Inheritance:
class OwnedDog : public Dog {
public:
    // Override the behavior of the print function for all OwnedDogs.
    // The override keyword is optional but makes sure you are actually 
    // overriding the method in a base class.
    void print() const override; 
};

// Meanwhile, in the corresponding .cpp file:
void OwnedDog::print() const {
    Dog::print(); // Call the print function in the base Dog class
    std::cout << "Dog is owned by " << owner << "\n";
}
```

## Initialization and Operator Overloading

 - In C++ you can overload the behavior of operators such as `+, -, *, /, etc`.

```cpp
#include <iostream>
using namespace std;

class Point {
public:
    // Member variables can be given default values in this manner.
    double x = 0;
    double y = 0;

    // initialization list
    // the proper way to initialize class member values
    Point (double a, double b) :
        x(a),
        y(b)
    { /* Do nothing except initialize the values */ }

    // Overload the + operator.
    Point operator+(const Point& rhs) const;
    // Overload the += operator
    Point& operator+=(const Point& rhs);
};

Point Point::operator+(const Point& rhs) const {
    // Create a new point that is the sum of this one and rhs.
    return Point(x + rhs.x, y + rhs.y);
}

Point& Point::operator+=(const Point& rhs) {
    x += rhs.x;
    y += rhs.y;
    return *this;
}
```

## Templates

 - Templates in C++ are more powerful than generic constructs in other languages
 - They also support explicit and partial specialization and functional-style type classes
 - in fact, they are a Turing-complete functional language embedded in C++!

---

 - To define a class or function that takes a type parameter:

```cpp
template<class T>
class Box {
public:
    // In this class, T can be used as any other type.
    void insert(const T&) { ... }
};
```

 - During compilation, the compiler actually generates copies of each template with parameters substituted

```cpp
Box<int> intBox;
intBox.insert(123);
// You can, of course, nest templates:
Box<Box<int> > boxOfBox;
// Until C++11, you had to place a space between the two '>'s, otherwise '>>'
// would be parsed as the right shift operator.
```

 - You will sometimes see `template<typename T>` instead
 - The 'class' keyword and 'typename' keywords are _mostly_ interchangeable in this case. 

--- 

 - Similarly, a template function:

```cpp
template<class T>
void barkThreeTimes(const T& input)
{
    input.bark();
    input.bark();
    input.bark();
}
```

 - Template parameters don't have to be classes:
 
```cpp
template<int Y>
void printMessage() {
    cout << "Learn C++ in " << Y << " minutes!" << endl;
}

printMessage<20>();  // Prints "Learn C++ in 20 minutes!"
``` 

## Exception Handling

```cpp
#include <exception>
#include <stdexcept>

try {
    // Do not allocate exceptions on the heap using _new_.
    throw std::runtime_error("A problem occurred");
}
// Catch exceptions by const reference if they are objects
catch (const std::exception& ex) {
    std::cout << ex.what();
}
// Catches any exception not caught by previous _catch_ blocks
catch (...) {
    std::cout << "Unknown exception caught";
    throw; // Re-throws the exception
}
```

## RAII

 - RAII stands for "Resource Acquisition Is Initialization".
 - is the simple concept that a constructor for an object acquires that object's resources and the destructor releases them.
 - To understand how this is useful,  consider a function that uses a C file handle:

```c
void doSomethingWithAFile(const char* filename) {
    // To begin with, assume nothing can fail.
    FILE* fh = fopen(filename, "r"); // Open the file in read mode.

    doSomethingWithTheFile(fh);
    doSomethingElseWithIt(fh);

    fclose(fh); // Close the file handle.
}
```

 - Unfortunately, things are quickly complicated by error handling
 - C programmers often clean this up a little bit using goto:
 - c++ exception handle make things a little cleaner, but still sub-optimal
 - Compare this to the use of C++'s file stream class (fstream)
    - fstream uses its destructor to close the file.
    - Recall from above that destructors are automatically called
    - whenever an object falls out of scope.

```cpp
void doSomethingWithAFile(const std::string& filename) {
    // ifstream is short for input file stream
    std::ifstream fh(filename); // Open the file

    // Do things with the file
    doSomethingWithTheFile(fh);
    doSomethingElseWithIt(fh);

} // The file is automatically closed here by the destructor
```

 - All idiomatic C++ code uses RAII extensively for all resources.
 - Additional examples include
    - Memory using unique_ptr and shared_ptr
    - Containers - the standard library linked list, vector (i.e. self-resizing array), hash maps, and so on
        - all automatically destroy their contents when they fall out of scope.
    - Mutexes using lock_guard and unique_lock


## Lambda Expressions (C++11 and above)

```cpp
vector<pair<int, int> > tester;
tester.push_back(make_pair(3, 6));
tester.push_back(make_pair(1, 9));
tester.push_back(make_pair(5, 0));

sort(tester.begin(), tester.end(), [](const pair<int, int>& lhs, const pair<int, int>& rhs) {
        return lhs.second < rhs.second;
    });
```

 - `[]` :  kind of `lambda` in python
 - you can not use outside variable in lambda body 
    - you can capture the variable you want to use in `[]`
    - It can be either:
        - 1. a value : [x]
        - 2. a reference : [&x]
        - 3. any variable currently in scope by reference [&]
        - 4. same as 3, but by value [=]

```cpp
vector<int> dog_ids;
// number_of_dogs = 3;
for(int i = 0; i < 3; i++) {
    dog_ids.push_back(i);
}
int weight[3] = {30, 50, 10};
sort(dog_ids.begin(), dog_ids.end(), [&weight](const int &lhs, const int &rhs) {
        return weight[lhs] < weight[rhs];
    });
```

## Range For (C++11 and above)

 - same as in java

```cpp
// You can use a range for loop to iterate over a container
int arr[] = {1, 10, 3};

for(int elem: arr){
    cout << elem << endl;
}
```

 - You can use "auto" 

```cpp
for(auto elem: arr) {
    // Do something with each element of arr
}
``` 

## Tuples (C++11 and above)

 - Conceptually, Tuples are similar to  old data structures (C-like structs) but instead of having named data members,
 - its elements are accessed by their order in the tuple.


```cpp
// Packing values into tuple
auto first = make_tuple(10, 'A');

// Printing elements of 'first' tuple
cout << get<0>(first) << " " << get<1>(first) << "\n"; //prints : 10 A

// Unpacking tuple into variables
int first_int;
char first_char;
tie(first_int, first_char) = first;

// We can also create tuple like this.
tuple<int, char, double> third(11, 'A', 3.14141);

// tuple_cat concatenates the elements of all the tuples in the same order.
auto concatenated_tuple = tuple_cat(first, second, third); 
// concatenated_tuple becomes = (10, 'A', 1e9, 15, 11, 'A', 3.14141)
```

## Containers

 - Vector (Dynamic array)
    - Allow us to Define the Array or list of objects at run time

```cpp
#include <vector>
vector<string> my_vector; // initialize the vector
my_vector.push_back(val);

for (int i = 0; i < my_vector.size(); i++) {
    cout << my_vector[i] << endl; // for accessing a vector's element we can use the operator []
}

// or using an iterator:
vector<string>::iterator it; // initialize the iterator for vector
for (it = my_vector.begin(); it != my_vector.end(); ++it) {
    cout << *it  << endl;
}
```

 - Set

```cpp
#include<set>
set<int> ST;    // Will initialize the set of int data type
ST.insert(30);  // Will insert the value 30 in set ST

ST.erase(20);  // Will erase element with value 20
ST.clear();
cout << ST.size();  // will print the size of set ST
```

 - Map

```cpp
#include<map>
map<char, int> mymap;

mymap.insert(pair<char,int>('A',1));
// To find the value corresponding to a key
it = mymap.find('Z');
```




