...menustart

- [C# vs .NET](#7d2f32a907cb8c81e03051e552fda79f)
- [CLR (Common Language Runtime)](#26d5d2a99978a512ae628508ff90707c)
- [Architecture of .NET Applications](#6b473f5c2ae970ef3688f04230eaadc0)
- [Fundamental](#2863bc264d070388a94111bc05f77f0f)
    - [ref vs out](#5bbfbc817b46dbc2cdf592d2f99e667d)
    - [yield](#16f10dfd541c23362492b4e513adf0a1)
    - [extension method](#9c40ef75c97e104ba6e7667e707a06d0)
    - [nullable types](#ce9d2b94fe950440377f494899eee6d3)
    - [LAMBDA EXPRESSIONS](#3a56db55bb121991bc71882db47b33be)
    - [disposable resources management](#cee2b21a163b0a5e2dc84b6b7535fddb)
    - [PARALLEL FRAMEWORK](#003ab30ce0724b20087fce47981771a6)
    - [DYNAMIC OBJECTS (great for working with other languages)](#a29a6cadf5b3ccac1b22cd60f2ce7116)
    - [IQUERYABLE < T >](#020f01fe3081f38e8b862747ef932d6d)
    - [DELEGATES AND EVENTS](#8ffa8b54c41af0dddd96ba147e823d77)
        - [delegate](#7f662005788ab434b371fbb0efc6d45f)
        - [event](#4119639092e62c55ea8be348e4d9260d)
        - [Why do we need events when we have delegates?](#7a62c57ff2352c127ab2ca8d092a08cc)
    - [oop](#403a96cff2a323f74bfb1c16992895be)

...menuend


<h2 id="7d2f32a907cb8c81e03051e552fda79f"></h2>


# C# vs .NET

- C# is a programming language
- .NET is a framework for building applications on Windows
    - .NET framework is not limited to c#. There are different languages that can target that framework and build applications using that framwork, e.g. F#, vb.net.
    - .NET framework contains 2 components
        1. CLR(Common Language Runtime)
        2. Class Library

<h2 id="26d5d2a99978a512ae628508ff90707c"></h2>


# CLR (Common Language Runtime)

- When you compile your C# code, the result is what we called IL(intermediate language) code. It is independent of the computer on which it's running.
    - Now we need something that would translate the IL code into the native code on the machine that running the application. And that is the job of CLR.
- So CLR is essentially an application that is sitting in the memory whose job is to translate the IL code into the machine code,
    - and this process is called just-in-time compilation or JIT.

<h2 id="6b473f5c2ae970ef3688f04230eaadc0"></h2>


# Architecture of .NET Applications

- Class
    - building blocks
- Namespace
    - a way to organize these classes
    - a container of related classes
- Assembly (DLL or EXE)
    - as the namespaces grow we need a different way of partitioning an application.
    - an assembly is a container for related namespaces 
    - physically it's a file on the disk. It can either be an executable or a DLL.


<h2 id="2863bc264d070388a94111bc05f77f0f"></h2>


# Fundamental

<h2 id="5bbfbc817b46dbc2cdf592d2f99e667d"></h2>


## ref vs out

Both ref and out parameter treated same at compile-time but different at run-time.

scenario |  ref | out
--- |--- | ---
before entering method |  must initialize | 
before returning  |  |  must initialize inside the mothod
when to use | when the callee also want to change the value of passed parameter | when a method return multiple values



<h2 id="16f10dfd541c23362492b4e513adf0a1"></h2>


## yield

- Usage of the "yield" keyword indicates that the method it appears in is an Iterator
    - this means you can use it in a foreach loop
        ```cs
        public static IEnumerable<int> YieldCounter(int limit = 10)
        {
            for (var i = 0; i < limit; i++)
                yield return i;
        }
        ```
    - which you would call like this :
        ```cs
        public static void PrintYieldCounterToConsole()
        {
            foreach (var counter in YieldCounter())
                Console.WriteLine(counter);
        }
        ```


<h2 id="9c40ef75c97e104ba6e7667e707a06d0"></h2>


## extension method

- allows you to add new methods in the existing class or in the structure without modifying the source code of the original type
    ```cs
    // static class
    public static class Extensions
    {
        // EXTENSION METHODS
        public static void Print(this object obj)
        {
            Console.WriteLine(obj.ToString());
        }
    }
    ```
    - this method extend to all `object` type
    - the first paramter `this object obj` is called **Binding parameter**
- how 2 use
    ```cs
    int i = 3;
    i.Print(); // Defined below
    ```

<h2 id="ce9d2b94fe950440377f494899eee6d3"></h2>


## nullable types

- great for database interaction / return values 
- any value type (i.e. not a class) can be made nullable by suffixing a `?`
    - `<type>? <var name> = <value>`
    ```cs
    int? nullable = null; // short hand for Nullable<int>
    Console.WriteLine("Nullable variable: " + nullable);
    bool hasValue = nullable.HasValue; // true if not null
    ```
- ?? is syntactic sugar for specifying default value (coalesce) in case variable is null
    ```cs
    int notNullable = nullable ?? 0; // 0
    ```
- ?. is an operator for null-propagation - a shorthand way of checking for null
    ```cs
    // Use the Print() extension method if nullable isn't null
    nullable?.Print();
    ```

<h2 id="3a56db55bb121991bc71882db47b33be"></h2>


## LAMBDA EXPRESSIONS

- allow you to write code in line
    ```cs
    Func<int, int> square = (x) => x * x; // Last T item is the return 
    ```


<h2 id="cee2b21a163b0a5e2dc84b6b7535fddb"></h2>


## disposable resources management

- Let you handle **unmanaged** resources easily.
- Most of objects that access **unmanaged** resources (file handle, device contexts, etc.)
- implement the IDisposable interface. The using statement takes cleaning those IDisposable objects for you.
    ```cs
    using (StreamWriter writer = new StreamWriter("log.txt"))
    {
        writer.WriteLine("Nothing suspicious here");
        // At the end of scope, resources will be released.
        // Even if an exception is thrown.
    }
    ```


<h2 id="003ab30ce0724b20087fce47981771a6"></h2>


## PARALLEL FRAMEWORK

https://devblogs.microsoft.com/csharpfaq/parallel-programming-in-net-framework-4-getting-started/

```cs
var words = new List<string> {"dog", "cat", "horse", "pony"};

Parallel.ForEach(words,
    new ParallelOptions() { MaxDegreeOfParallelism = 4 },
    word =>
    {
        Console.WriteLine(word);
    }
);
```

<h2 id="a29a6cadf5b3ccac1b22cd60f2ce7116"></h2>


## DYNAMIC OBJECTS (great for working with other languages)

```cs
dynamic student = new ExpandoObject();
student.FirstName = "First Name"; // No need to define class first!

// You can even add methods (returns a string, and takes in a string)
student.Introduce = new Func<string, string>(
    (introduceTo) => string.Format("Hey {0}, this is {1}", student.FirstName, introduceTo));
```

<h2 id="020f01fe3081f38e8b862747ef932d6d"></h2>


## IQUERYABLE < T >

- almost all collections implement this, which gives you a lot of very useful Map / Filter / Reduce style methods
    ```cs
    var bikes = new List<Bicycle>();
    bikes.Sort(); // Sorts the array
    bikes.Sort((b1, b2) => b1.Wheels.CompareTo(b2.Wheels)); // Sorts based on wheels
    var result = bikes
        .Where(b => b.Wheels > 3) // Filters - chainable (returns IQueryable of previous type)
        .Where(b => b.IsBroken && b.HasTassles)
        .Select(b => b.ToString()); // Map - we only this selects, so result is a IQueryable<string>

    var sum = bikes.Sum(b => b.Wheels); // Reduce - sums all the wheels in the collection
    ```



<h2 id="8ffa8b54c41af0dddd96ba147e823d77"></h2>


## DELEGATES AND EVENTS

<h2 id="7f662005788ab434b371fbb0efc6d45f"></h2>


### delegate

- A delegate is a reference to a method.
    - data & method
        ```cs
        public static int count = 0;
        public static int Increment() {
            return ++count;
        }
        ```
    - To reference the Increment method, first declare a delegate with the same signature
        - i.e. takes no arguments and returns an int
        ```cs
        // first declare a delegate with same signature 
        public delegate int IncrementDelegate();
        ```
- How to use
    - instantiating the delegate, and passing the method in as an argument
        ```cs
        IncrementDelegate inc = new IncrementDelegate(Increment);
        ```
    - works like a function pointer
        ```cs
        inc(); // => 1
        ```
    - Delegates can be composed with the `+` operator
        ```cs
        IncrementDelegate composedInc = inc;
        composedInc += inc;
        composedInc += inc;
        // composedInc will run Increment 3 times
        composedInc(); // => 4
        ```

<h2 id="4119639092e62c55ea8be348e4d9260d"></h2>


### event

- An event can **also** be used to trigger delegates 
    ```cs
    // Create an event with the delegate type
    public static event IncrementDelegate MyEvent;
    ```
- How to use
    - Subscribe to the event with the delegate
        ```cs
        MyEvent += new IncrementDelegate(Increment);
        MyEvent += new IncrementDelegate(Increment);
        ```
    - Trigger the event
        - ie. run all delegates subscribed to this event
        ```cs
        MyEvent(); 
        ```

<h2 id="7a62c57ff2352c127ab2ca8d092a08cc"></h2>


### Why do we need events when we have delegates?

1. To provide encapsulation and not exposing business logic.
    - delegate need instantiate, it maybe null. but delegate can be invoked directly without checking.
        - solve the problem by adding the event keyword.
    - event can not be invoked directly, it will raise an error.
2. To prevent Team Client from clearing all assign methods to delegates
    -  (You cannot do that for events):
        ```cs
        MyEvent = null;
        ```

<h2 id="403a96cff2a323f74bfb1c16992895be"></h2>


## OOP

- constructor
    ```cs
    // This is a specified constructor (it contains arguments)
    public Bicycle(int startCadence, int startSpeed, int startGear,
                   string name, bool hasCardsInSpokes, BikeBrand brand)
        : base(startCadence, startSpeed) // calls base first
    {
        Gear = startGear;
        Cadence = startCadence;
        _speed = startSpeed;
        Name = name;
        _hasCardsInSpokes = hasCardsInSpokes;
        Brand = brand;
    }

    // Constructors can be chained
    public Bicycle(int startCadence, int startSpeed, BikeBrand brand) :
        this(startCadence, startSpeed, 0, "big wheels", true, brand)
    {
    }
    ```
- override
    ```cs
    public override string Info()
    {
        string result = "PennyFarthing bicycle ";
        result += base.ToString(); // Calling the base version of the method
        return result;
    }
    ```


## struct

 &nbsp; | struct | class 
--- | -- | ---
type  | value type | reference type
alloc  | in stack, or inline in containing types, auto-deallocated | in heap, GC
assignment | copy value | copy reference


- when to use structure ?
    - CONSIDER defining a struct instead of a class if instances of the type are small and commonly short-lived or are commonly embedded in other objects.
    - ❌ AVOID defining a struct unless the type has all of the following characteristics:
        - It logically represents a single value, similar to primitive types (int, double, etc.).
        - It has an instance size under 16 bytes.
        - It is immutable.
        - It will not have to be boxed frequently.


## boxing

```cs
{
    ...
    int someNumber = 420;
    object someNumberObject = someNumber;  // boxing , 20x slower
    int unboxed = (int)someNumberObject ; // unboxing , 4x slower
    ...
}
```

- why is it called boxing ?
    - since object is a reference type allocated on the heap, you have to put that `someNumber` variable in a box and allocate on the heap.

- another example
    ```cs
    var arrayOfInts = Enumerable.Range(69,420).ToArray();

    var arrayList = new ArrayList(arrayOfInts) ; // boxing, since underlying data structure is object[]
    var list = new List<int>(arrayOfInts); // will not boxing, generic solve that problem
    ```



