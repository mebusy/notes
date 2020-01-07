
# TypeScript

> focus only on TypeScript extra syntax 

## Basic 

- 3(or 4) basic types 
    1. boolean
    2. number
    3. string 
    4. any
- variable definition
    - 
    ```ts
    let lines = 42;
    let notSure: any = 4;
    ```
    - use `let` to define variable, 
    - while using `const` to define constant. 
- **void**
    - "void" is used in the special case of a function returning nothing
    - 
    ```ts
    function bigHorribleAlert(): void {
    ```
- Template Strings (strings that use backticks)
    - 
    ```ts
    let name = 'Tyrone';
    let greeting = `Hi ${name}, how are you?`
    ```
    - multiple line
    ```ts
    let multiline = `This is an example
    of a multiline string`;
    ```

## collections
- typed array 
- generic arrays  // Alternatively
- 
```ts
let list: number[] = [1, 2, 3];
let list: Array<number> = [1, 2, 3]; // Alternatively, generic array type
```

## Iterators and Generators

1. `for..of`  iterate over the list of **values**
    - 
    ```ts
    let arrayOfAnyType = [1, "string", false];
    for (const val of arrayOfAnyType) {
        console.log(val); // 1, "string", false
    }
    
    let list = [4, 5, 6];
    for (const i of list) {
       console.log(i); // 4, 5, 6
    }
    ```
2. `for..in`  iterate over the list of **keys**
    - 
    ```ts
    for (const i in list) {
       console.log(i); // 0, 1, 2
    }
    ```

## enumerations
- 
```ts
enum Color { Red, Green, Blue };
let c: Color = Color.Green;
```

## Functions
- support the lambda "fat arrow" syntax
- use type inference
- The following are equivalent
- 
```ts
let f1 = function (i: number): number { return i * i; }
let f2 = function (i: number) { return i * i; } // Return type inferred
let f3 = (i: number): number => { return i * i; } // => 
let f4 = (i: number) => { return i * i; }  // => with return type inferred
let f5 = (i: number) => i * i;  // + return keyword omit
```

## Interfaces

1. As a struct. 
    - anything that has the properties is compliant with the interface
    - 
    ```ts
    interface Person {
        name: string;
        age?: number; // Optional properties, marked with a "?"
        move(): void;
    }
    ``` 
    - i.e. Object that implements the "Person" interface
    - 
    ```ts
    let p: Person = { name: "Bobby", move: () => { } };
    ```
2. As a description of a function type
    - 
    ```ts
    interface SearchFunc {
        (source: string, subString: string): boolean;
    }
    ```
    - Only the parameters' types are important, names are not important.
    - 
    ```ts
    let mySearch: SearchFunc;
    mySearch = function (src: string, sub: string) {
        return src.search(sub) != -1;
    }
    ```

## Classes

- members are public by default
- you can add `public/private/protected` to restrict the access 
- 
```ts
class Point {
    // Properties
    x: number;

    // Constructor
    // Default values are also supported
    constructor(x: number, public y: number = 0) {
       this.x = x;
    }

    // Functions
    dist() { return Math.sqrt(this.x * this.x + this.y * this.y); }

    // Static members
    static origin = new Point(0, 0);
}
// ...
let p2 = new Point(25); //y will be 0
```
- READONLY (from TS 3.1 , see details below )

## implementing an interface

- 
```ts
class PointPerson implements Person {
    name: string
    move() {}
}
```

## Inheritance

- Explicit call to the super class constructor is mandatory
- 
```ts
class Point3D extends Point {
    constructor(x: number, y: number, public z: number = 0) {
        super(x, y); 
    }

    // Overwrite
    dist() {
        let d = super.dist();
        return Math.sqrt(d * d + this.z * this.z);
    }
}
```

## Modules

- "." can be used as separator for sub modules
    - 
    ```ts
    module Geometry {
        export class Square {
            constructor(public sideLength: number = 0) {
            }
            area() {
                return Math.pow(this.sideLength, 2);
            }
        }
    }
    let s1 = new Geometry.Square(5);
    ```

- Local alias for referencing a module
    - 
    ```ts
    import G = Geometry;
    let s2 = new G.Square(10);
    ```

## Generics

- Classes
    - 
    ```ts
    class Tuple<T1, T2> {
        constructor(public item1: T1, public item2: T2) {
        }
    }
    ```
- Interfaces
    - 
    ```ts
    interface Pair<T> {
        item1: T;
        item2: T;
    }
    ```
- functions
    - 
    ```ts
    let pairToTuple = function <T>(p: Pair<T>) {
        return new Tuple(p.item1, p.item2);
    };

    let tuple = pairToTuple({ item1: "hello", item2: "world" });
    ```



## Misc

- Including references to a definition file:
    - 
    ```ts
    /// <reference path="jquery.d.ts" />
    ```
- readonly:  New Feature in TypeScript 3.1
    - 
    ```ts
    interface Person {
        readonly name: string;
        readonly age: number;
    }
    ```
    - 
    ```ts
    class Car {
        readonly make: string;
        constructor() {
            this.make = "Unknown Make"; // Assignment permitted in constructor
        }
    }
    ```
    - 
    ```ts
    // readonly array
    let moreNumbers: ReadonlyArray<number> = numbers;
    ```
- Tagged Union
    - 
    ```ts
    type State = 
        | { type: "loading" }
        | { type: "success", value: number }
        | { type: "error", message: string };

    declare const state: State;
    if (state.type === "success") {
        console.log(state.value);
    } else if (state.type === "error") {
        console.error(state.message);
    }
    ```


