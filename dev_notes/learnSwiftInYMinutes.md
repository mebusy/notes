
# var / let

```swift
var myVariable = 42
let label = "some text " + String(myVariable) // String construction

let explicitDouble: Double = 70
let π = 3.1415926
let piText = "Pi = \(π), Pi 2 = \(π * 2)" // String interpolation 
```

# Optional

 - Optionals either contains a value, or contains nil (no value) to indicate that a value is missing.
    - it may be an Optional which contains a value 
    - or it is `nil`

```swift
var someOptionalString: String? = "a"
someOptionalString = nil
```

## test Optional 

 - `If let structure`
    - If let is a special structure in Swift that allows you to check if an Optional rhs holds a value
        - if is does , unwraps and assigns it to the lhs 

```swift
if let test = someOptionalString {
    print ( test ) ;
}
```

### Tips for optional test

 - sometimes more Optional test is painful , try `guart let` , it makes code pretty

```swift
func userLogIn() {
    guard let username = myUsername, let password = myPassword else { 
        return 
    } 
    print("Welcome, \(username)!") 
}
```

### Tips for A or B 

```swift
var colorToUse = userChosenColor ?? defaultColor
```

## force unwrap 

 - use `!` to implicitly unwrapped optional

```swift
var unwrappedString: String! = someOptionalString
```

# Any / AnyObject 

 - to store a value of any type
 - `AnyObject` == `id` from Objective-C
 - `Any`  also words with any scalar values ( Class, Int, struct, etc. )

```swift
var anyVar: Any = 7
anyVar = "Changed value to a string, not good practice, but possible."
let anyObjectVar: AnyObject = Int(1) as NSNumber
```

# Collections 
     
 - Array and Dictionary types are structs
 - So `let` and `var` also indicate that they are mutable (var) or immutable (let) when declaring these types

## Array

```swift
var shoppingList = ["catfish", "water", "lemons"]
var emptyMutableArray = [String]() // empty String array
var explicitEmptyMutableStringArray: [String] = [] // same as above
```

## Dictionary

```swift
var occupations = [
    "Malcolm": "Captain",
    "kaylee": "Mechanic"
]
var emptyMutableDictionary = [String: Float]()
var explicitEmptyMutableDictionary: [String: Float] = [:] // same as above
```

# Control Flow

## condition

 - 条件语句支持 "," (逗号) 子句, 可以用来帮助处理 optional values

```swift
let someNumber = Optional<Int>(7)
if let num = someNumber, num > 3 {
    print("num is greater than 3")
}
```

## for loop (array)

```swift
let myArray = [1, 1, 2, 3, 5]
for value in myArray {
    print(value)
}
```

## for loop (dictionary)

```swift
var dict = ["one": 1, "two": 2]
for (key, value) in dict {
    print("\(key): \(value)")
}
```

##  for loop (range)

 - `..<` exclude the last number `[ )`
 - `...` include the last number `[ ]`

```swift
for i in -1...shoppingList.count {
    print(i)
}
shoppingList[1...2] = ["1", "2"]
```

## while loop 

```swift
var i = 1
while i < 1000 {
    i *= 2
}
```

### Tips for while count 

 - 为了控制 while 的循环次数，这里不得不定义一个变量 i

```swift
// Better Code
for _ in 1...5 { print("Count") }
```

## repeat-while loop

```swift
repeat {
    print("hello")
} while 1 == 2
```

## Switch

 - Very powerful, support String, object instances, and primitives (Int, Double, etc)

```swift
let vegetable = "red pepper"

switch vegetable {
case "cucumber", "watercress":
    let vegetableComment = "That would make a good tea sandwich."
case let localScopeValue where localScopeValue.hasSuffix("pepper"):
    let vegetableComment = "Is it a spicy \(localScopeValue)?"
default: // required (in order to cover all possible input)
    let vegetableComment = "Everything tastes good in soup."
}
```

# Functions

```swift
func greet(name: String, day: String) -> String {
    return "Hello \(name), today is \(day)."
}
greet(name: "Bob", day: "Tuesday")

// 第二个参数表示外部参数名使用 `externalParamName` ，内部参数名使用 `localParamName`
func greet2(name: String, externalParamName localParamName: String) -> String {
    return "Hello \(name), the day is \(localParamName)"
}
greet2(name: "John", externalParamName: "Sunday")

// returns multiple items in a tuple
func getGasPrices() -> (Double, Double, Double) {
    return (3.59, 3.69, 3.79)
}
let pricesTuple = getGasPrices()
let price = pricesTuple.2 // 3.79

let (_, price1, _) = pricesTuple // price1 == 3.69

// you can also name those tuple params 
func getGasPrices2() -> (lowestPrice: Double, highestPrice: Double, midPrice: Double) {
    return (1.77, 37.70, 7.37)
}
let pricesTuple2 = getGasPrices2()
let price2 = pricesTuple2.lowestPrice
```

## guard statements

 - guards provide early exits or breaks
    - placing the error handler code near the conditions
 - it places variables it declares , in the same scope as the guard statement

```swift
func testGuard() {
    guard let aNumber = Optional<Int>(7) else {
        return
    }
    print("number is \(aNumber)")
}
```

## Variadic Args

```swift
func setup(numbers: Int...) {
    // it's an array
    let _ = numbers[0]
    let _ = numbers.count
}
```

## returning functions

```swift
func makeIncrementer() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
```

## pass by ref

```swift
func swapTwoInts(a: inout Int, b: inout Int) {
    let tempA = a
    a = b
    b = tempA
}
var someIntA = 7
var someIntB = 3
swapTwoInts(a: &someIntA, b: &someIntB)
```

# Closures

 - Functions are special case closures `({})`
 - `->` separates the arguments and return type
 - `in` separates the closure header from the closure body

```swift
var numbers = [1, 2, 6]
numbers.map({
    (number: Int) -> Int in
    let result = 3 * number
    return result
})

//  When the type is known ... 
numbers.map({ number in 3 * number })   // kind of lambda ?
// 语法糖， 这种情况下，可以不要 ()
numbers.map{ number in 3 * number }
```

## Trailing closure

```swift
numbers = numbers.sorted { $0 > $1 }
```

## Tips : Use Closure to drop function parameter name 

```swift
// Normal Function
func sum(x: Int, y: Int) -> Int { return x + y }

var sumUsingClosure: (Int, Int) -> (Int) = { $0 + $1 }
``` 

# Structures
 
 - Structures and classes have very similar capabilities

```swift
struct NamesTable {
    let names: [String]

    // Custom subscript 下标访问
    subscript(index: Int) -> String {
        return names[index]
    }
}
```

 - Structures have an auto-generated (implicit) designated initializer

```swift
let namesTable = NamesTable(names: ["Me", "Them"])
let name = namesTable[1]  // Them
```

# Error Handling


----

tips TODO 

Extension
Generics
计算属性 vs 方法
Enum 类型安全
函数式编程

