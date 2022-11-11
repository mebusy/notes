[](...menustart)

- [TypeScript](#558b544cf685f39d34e4903e39c38b67)
    - [Basic](#972e73b7a882d0802a4e3a16946a2f94)
    - [collections](#0b9abfe67cc31fcf1ecd022eb19a5216)
    - [Iterators and Generators](#0ffc4b85f97ccbcd76d00c2ea4013048)
    - [enumerations](#5d4d047c0c2c2d415d43bb476b2d73d8)
    - [Functions](#e93acb146e114b5dfa6ce2d12dcb96e4)
    - [Interfaces](#756640f0aea5f5bea1cbe250a9d08989)
    - [Classes](#e9878b4854d29907146149f695cb1cfb)
    - [implementing an interface](#2da55be28182388a63be9be8a204cd56)
    - [Inheritance](#e40489cd1e7102e35469c937e05c8bba)
    - [Modules](#bf17ac149e2e7a530c677e9bd51d3fd2)
    - [Generics](#0d7bdbf7f4e4f0dc8ed310a01dee3502)
    - [Misc](#74248c725e00bf9fe04df4e35b249a19)

[](...menuend)


<h2 id="558b544cf685f39d34e4903e39c38b67"></h2>

# TypeScript

> focus only on TypeScript extra syntax 

<h2 id="972e73b7a882d0802a4e3a16946a2f94"></h2>

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

<h2 id="0b9abfe67cc31fcf1ecd022eb19a5216"></h2>

## collections
- typed array 
- generic arrays  // Alternatively
- 
```ts
let list: number[] = [1, 2, 3];
let list: Array<number> = [1, 2, 3]; // Alternatively, generic array type
```

<h2 id="0ffc4b85f97ccbcd76d00c2ea4013048"></h2>

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

<h2 id="5d4d047c0c2c2d415d43bb476b2d73d8"></h2>

## enumerations
- 
```ts
enum Color { Red, Green, Blue };
let c: Color = Color.Green;
```

<h2 id="e93acb146e114b5dfa6ce2d12dcb96e4"></h2>

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

<h2 id="756640f0aea5f5bea1cbe250a9d08989"></h2>

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

<h2 id="e9878b4854d29907146149f695cb1cfb"></h2>

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

<h2 id="2da55be28182388a63be9be8a204cd56"></h2>

## implementing an interface

- 
```ts
class PointPerson implements Person {
    name: string
    move() {}
}
```

<h2 id="e40489cd1e7102e35469c937e05c8bba"></h2>

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

<h2 id="bf17ac149e2e7a530c677e9bd51d3fd2"></h2>

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

<h2 id="0d7bdbf7f4e4f0dc8ed310a01dee3502"></h2>

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



<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

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


