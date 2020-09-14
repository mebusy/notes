...menustart


...menuend


- var / let
    - var means mutable , let means constant. 
    - really important in swift 
    - it's a multi-threaded environment from the very beginning .
    - they make no compromise for single-threaded performance 
- string interpolation
    - let apples = 3
    - let oranges = 5
    - `I have \(apples+oranges) fruits.`
- array 
    - pretty same
    - `var emptyArray = [String]()` , or `[]`
- dictionary
    - not `{...}` , but `[ "a":xxx ]`
    - `var emptyDictionary = [String:Float]()` , or `[:]` if type cam be inferred
- for 
   - `for xxx in xxxx {  }`
   - `for i in 0..<4 `
   - `for i in 0...3 `
   - `for var i=0;i<4;i++ `
- optional construct
    - `var optionalString: String? = "Hello"`
    - optional variables have actually 2 states:  have nothing , or have a value 
    - 0 is not the same thing as nothing 
- switch
    - you can switch on many types , integer, string , object, ... 
- tuple 
    - `for (key, value) in someDict { ... }` 
- while / do ... while
- function
    - keyword: `func`
    - `func calc( scores:[Int] ) -> (min: Int, max: Int, sum: Int) { return (0,0,0) }` 
    - `let result = calc( [5,3,100,3,9])` 
    - return value is more than just a tuple, it's actually a named tuple
        - `print( result.sum )`   
    - **function can be nested** 
    - functions are actually a special case of closures: blocks of code that can be called later.
    
```swift
// you can write a closure without a name by surrounding code with braces {} 
// use in to separate the arguments and return type from the body

numbers.map({
    (number: Int) -> Int in
    let result = 3*number
    return result    
}) 

// or more concisely 
// when a closure's type is already known, such as the callback for a delegate
// you can omit the type of its parameters , its return type, or both

let mappedNumbers = numbers.map( { number in 3*number } )

// You can refer to parameters by number instead of by name
// When a closure is the only argument to a function, you can omit the parentheses entirely.
let sortedNumbers = numbers.sorted { $0 > $1 }
``` 

- class
    - `var shape = Shape()`
    - `__init__` in python => `init` in swift
        - `super.init(xxx)`
    - inherit : `class square: Shape {` 
    - override :  `  override func xxxx  `
    - getter / setter

```
var perimeter : Double {
    get {
        return 3.0 * sideLength ;
    }
    set {
        sideLength = newValue / 3.0    
    }    
}
``` 

- structure
    - structures are passed by value 
    - and this gets into the whole multi-threaded  multiprocessing 


