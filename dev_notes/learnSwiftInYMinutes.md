...menustart

 - [var / let](#9fa684bc441f61891a932d056d3c8246)
 - [Optional](#ebb061953c0454b2c8ee7b0ac615ebcd)
     - [test Optional](#27c595f053043a5aae110c96f30cd8de)
         - [Tips for optional test](#afb83c0e97053d46b323ad9e665ff64e)
         - [Tips for A or B](#0253a6b48c383156005b1bcbf7511d49)
     - [force unwrap](#154c68433b1feb0dae026c6d1c088732)
 - [Any / AnyObject](#2557bf0a34a37fc3bd3e0ad5528169b3)
 - [Collections](#a9fc91939a389c7c73e7a3f3cbf411cd)
     - [Array](#4410ec34d9e6c1a68100ca0ce033fb17)
     - [Dictionary](#3beb75d1563ebc22253341be4ce57f44)
 - [Control Flow](#6a5ef0f472b554214a936c0224815bb3)
     - [condition](#3f9178c25b78ed8bed19091bcb62e266)
     - [for loop (array)](#e12ad53a19d5e1aa87072007bad513a3)
     - [for loop (dictionary)](#1980b393a3a8f90611e243e0c61dc737)
     - [for loop (range)](#70a0808d46a6536d1aadff4818c13532)
     - [while loop](#599788940f123832ffad54e986d4ba65)
         - [Tips for while count](#feae46ea897378fa83e0b450eab370b4)
     - [repeat-while loop](#ec0bf23eb62ddf3ea82dc51880a43246)
     - [Switch](#bbc155fb2b111bf61c4f5ff892915e6b)
 - [Functions](#e93acb146e114b5dfa6ce2d12dcb96e4)
     - [guard statements](#e605db264eafbaa07401939571a467d9)
     - [Variadic Args](#d9cac8e5e11015c9cc7d13fa9d7677e2)
     - [returning functions](#bdad91ee74b78a8decd66266df5132b3)
     - [pass by ref](#464c902a8ab52292e8ff744656e60032)
 - [Closures](#f2d630c9f5476e26be78c865bb09939a)
     - [Trailing closure](#13b8b710edc3280a9931abfb03438b5a)
     - [Tips : Use Closure to drop function parameter name](#b37e907d573b8391a600a8f6c7172e70)
     - [Tips : 函数式编程](#d8f0c71e98ec37923af15ec33a5bd3c4)
 - [Structures](#2dec5ee9db863ffb68915b70bce4efe4)
 - [Error Handling](#ef43236673ca0bb606b14091061ac271)
 - [Classes](#e9878b4854d29907146149f695cb1cfb)
     - [Tips : 计算属性 vs 方法](#4c2830a68ad28e3eed67d66d79723d33)
     - [init 方法: 构造函数](#c6612e94b6339d9a1cc12175bdfef6f5)
     - [Optional init](#85f00a6be586ae47e453334f7168588a)
 - [Enums](#1b22e7dc709b52f1767fe1eb5dc56625)
     - [Tips : Enum 类型安全](#8da882f7c6705dad7abd441bf232c671)
 - [Protocols](#9985b4390c40137573e6da05caf85874)
 - [Extension](#63e4e92bb7d207ca577b11c07f827279)
 - [Generics](#0d7bdbf7f4e4f0dc8ed310a01dee3502)
 - [Operators](#b3c5827f54218753bb2c3338236446c2)

...menuend


<h2 id="9fa684bc441f61891a932d056d3c8246"></h2>


# var / let

```swift
var myVariable = 42
let label = "some text " + String(myVariable) // String construction

let explicitDouble: Double = 70
let π = 3.1415926
let piText = "Pi = \(π), Pi 2 = \(π * 2)" // String interpolation 
```

<h2 id="ebb061953c0454b2c8ee7b0ac615ebcd"></h2>


# Optional

 - Optionals either contains a value, or contains nil (no value) to indicate that a value is missing.
    - it may be an Optional which contains a value 
    - or it is `nil`

```swift
var someOptionalString: String? = "a"
someOptionalString = nil
```

<h2 id="27c595f053043a5aae110c96f30cd8de"></h2>


## test Optional 

 - `If let structure`
    - If let is a special structure in Swift that allows you to check if an Optional rhs holds a value
        - if is does , unwraps and assigns it to the lhs 

```swift
if let test = someOptionalString {
    print ( test ) ;
}
```

<h2 id="afb83c0e97053d46b323ad9e665ff64e"></h2>


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

<h2 id="0253a6b48c383156005b1bcbf7511d49"></h2>


### Tips for A or B 

```swift
var colorToUse = userChosenColor ?? defaultColor
```

<h2 id="154c68433b1feb0dae026c6d1c088732"></h2>


## force unwrap 

 - use `!` to implicitly unwrapped optional

```swift
var unwrappedString: String! = someOptionalString
```

<h2 id="2557bf0a34a37fc3bd3e0ad5528169b3"></h2>


# Any / AnyObject 

 - to store a value of any type
 - `AnyObject` == `id` from Objective-C
 - `Any`  also works  with any scalar values ( Class, Int, struct, etc. )

```swift
var anyVar: Any = 7
anyVar = "Changed value to a string, not good practice, but possible."
let anyObjectVar: AnyObject = Int(1) as NSNumber
```

<h2 id="a9fc91939a389c7c73e7a3f3cbf411cd"></h2>


# Collections 
     
 - Array and Dictionary types are structs
 - So `let` and `var` also indicate that they are mutable (var) or immutable (let) when declaring these types

<h2 id="4410ec34d9e6c1a68100ca0ce033fb17"></h2>


## Array

```swift
var shoppingList = ["catfish", "water", "lemons"]
var emptyMutableArray = [String]() // empty String array
var explicitEmptyMutableStringArray: [String] = [] // same as above
```

<h2 id="3beb75d1563ebc22253341be4ce57f44"></h2>


## Dictionary

```swift
var occupations = [
    "Malcolm": "Captain",
    "kaylee": "Mechanic"
]
var emptyMutableDictionary = [String: Float]()
var explicitEmptyMutableDictionary: [String: Float] = [:] // same as above
```

<h2 id="6a5ef0f472b554214a936c0224815bb3"></h2>


# Control Flow

<h2 id="3f9178c25b78ed8bed19091bcb62e266"></h2>


## condition

 - 条件语句支持 "," (逗号) 子句, 可以用来帮助处理 optional values

```swift
let someNumber = Optional<Int>(7)
if let num = someNumber, num > 3 {
    print("num is greater than 3")
}
```

<h2 id="e12ad53a19d5e1aa87072007bad513a3"></h2>


## for loop (array)

```swift
let myArray = [1, 1, 2, 3, 5]
for value in myArray {
    print(value)
}
```

<h2 id="1980b393a3a8f90611e243e0c61dc737"></h2>


## for loop (dictionary)

```swift
var dict = ["one": 1, "two": 2]
for (key, value) in dict {
    print("\(key): \(value)")
}
```

<h2 id="70a0808d46a6536d1aadff4818c13532"></h2>


##  for loop (range)

 - `..<` exclude the last number `[ )`
 - `...` include the last number `[ ]`

```swift
for i in -1...shoppingList.count {
    print(i)
}
shoppingList[1...2] = ["1", "2"]
```

<h2 id="599788940f123832ffad54e986d4ba65"></h2>


## while loop 

```swift
var i = 1
while i < 1000 {
    i *= 2
}
```

<h2 id="feae46ea897378fa83e0b450eab370b4"></h2>


### Tips for while count 

 - 为了控制 while 的循环次数，这里不得不定义一个变量 i

```swift
// Better Code
for _ in 1...5 { print("Count") }
```

<h2 id="ec0bf23eb62ddf3ea82dc51880a43246"></h2>


## repeat-while loop

```swift
repeat {
    print("hello")
} while 1 == 2
```

<h2 id="bbc155fb2b111bf61c4f5ff892915e6b"></h2>


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

<h2 id="e93acb146e114b5dfa6ce2d12dcb96e4"></h2>


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

<h2 id="e605db264eafbaa07401939571a467d9"></h2>


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

<h2 id="d9cac8e5e11015c9cc7d13fa9d7677e2"></h2>


## Variadic Args

```swift
func setup(numbers: Int...) {
    // it's an array
    let _ = numbers[0]
    let _ = numbers.count
}
```

<h2 id="bdad91ee74b78a8decd66266df5132b3"></h2>


## returning functions

```swift
func makeIncrementer() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
```

<h2 id="464c902a8ab52292e8ff744656e60032"></h2>


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

<h2 id="f2d630c9f5476e26be78c865bb09939a"></h2>


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

<h2 id="13b8b710edc3280a9931abfb03438b5a"></h2>


## Trailing closure

```swift
numbers = numbers.sorted { $0 > $1 }
```

<h2 id="b37e907d573b8391a600a8f6c7172e70"></h2>


## Tips : Use Closure to drop function parameter name 

```swift
// Normal Function
func sum(x: Int, y: Int) -> Int { return x + y }

var sumUsingClosure: (Int, Int) -> (Int) = { $0 + $1 }
``` 

<h2 id="d8f0c71e98ec37923af15ec33a5bd3c4"></h2>


## Tips : 函数式编程

 - 例：获取偶数：

```swift
// bad
var newEvens = [Int]()

for i in 1...10 {
 if i % 2 == 0 { newEvens.append(i) }
}

//========================
// Declarative 
var evens = Array(1...10).filter { $0 % 2 == 0 }
print(evens) // [2, 4, 6, 8, 10]
```


<h2 id="2dec5ee9db863ffb68915b70bce4efe4"></h2>


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

<h2 id="ef43236673ca0bb606b14091061ac271"></h2>


# Error Handling

 - The `Error` protocol is used when throwing errors to catch

```swift
enum MyError: Error {
    case BadValue(msg: String)
    case ReallyBadValue(msg: String)
```

 - functions marked with `throws` must be called using `try`

```swift
func fakeFetch(value: Int) throws -> String {
    guard 7 == value else {
        throw MyError.ReallyBadValue(msg: "Some really bad value")
    }
    return "test"
}

func testTryStuff() {
    // assumes there will be no error thrown,
    // otherwise a runtime exception is raised
    let _ = try! fakeFetch(value: 7)

    // if an error is thrown, then it proceeds,
    // but if the value is nil, it also wraps every return value in an optional, even if its already optional
    let _ = try? fakeFetch(value: 7)

    // normal try operation that provides error handling via `catch` block
    do {
        try fakeFetch(value: 1)
    } catch MyError.BadValue(let msg) {
        print("Error message: \(msg)")
    } catch {
        // must be exhaustive
    }
}
```

<h2 id="e9878b4854d29907146149f695cb1cfb"></h2>


# Classes

 - Classes, structures and its members have three levels of access control
    - internal (default), public, private

```swift
public class Shape {
    public func getArea() -> Int {
        return 0
    }
}
```

 - All methods and properties of a class are public
 - If you just need to store data in a structured object, you should use a `struct`

```swift
internal class Rect: Shape {
    var sideLength: Int = 1

    // Custom getter and setter property
    private var perimeter: Int {
        get {
            return 4 * sideLength
        }
        set {
            // `newValue` is an implicit variable available to setters
            sideLength = newValue / 4
        }
    }

    // Computed properties must be declared as `var`
    // cause' they can change
    var smallestSideLength: Int {
        return self.sideLength - 1
    }

    // Lazily load a property
    // subShape remains nil (uninitialized) until getter called
    lazy var subShape = Rect(sideLength: 4)

    // If you don't need a custom getter and setter,
    // but still want to run code before and after getting or setting a property,
    // you can use `willSet` and `didSet`
    var identifier: String = "defaultID" {
        // the `willSet` arg will be the variable name for the new value
        willSet(someIdentifier) {
            print(someIdentifier)
        }
    }

    init(sideLength: Int) {
        self.sideLength = sideLength
        // always super.init last when init custom properties
        super.init()
    }

    // override
    override func getArea() -> Int {
        return sideLength * sideLength
    }
}

// A simple class `Square` extends `Rect`
class Square: Rect {
    convenience init() {
        self.init(sideLength: 5)
    }
}

var mySquare = Square()
// cast instance
let aShape = mySquare as Shape

```

<h2 id="4c2830a68ad28e3eed67d66d79723d33"></h2>


## Tips : 计算属性 vs 方法 

 - 上例的 sideLength ／ perimeter 是相互关联的两组数据
 - 与其创建两个相互转换的方法 , 不如使用 计算属性getter/setter 把他们关联起来


<h2 id="c6612e94b6339d9a1cc12175bdfef6f5"></h2>


## init 方法: 构造函数

 - init方法是用来创建对象的，有着比较严格的调用方式和实现方式。
 - 初始化方法的顺序. 为了保证所有的属性都被初始化，对init方法里语句的顺序有严格的要求
    1. 子类要先初始化子类自有的属性
    2. 调用父类的初始化方法
    3. 对父类中需要改变的属性再赋值
 - init的类别
    1. Designated
        - 不加修饰的init都为designated. 
        - designated初始化方法中要保证所有非Optional的属性都被初始化，子类的init方法也必须都调用父类的Designated init
    2. Convenience
        - Convenience初始化方法必须调用同类中的Designated init完成初始化，且不能被子类重载也不能在子类中用super的方式调用.
        - 只要子类重写了父类convenience初始化方法需要的Designated方法，子类就可以直接调用父类的convenience init完成子类的初始化
    3. Required
        - 对于希望子类实现的初始化方法，我们可以通过required限制，强制子类重写，这样写的作用保证了依赖某个Designated初始化方法的convenience一直可以使用。
        - 另外可以用required修饰convenience方法，用来保证子类不直接使用父类的convenience。

![](https://cdn.pupboss.com/images/blog/2016/02/designated.png)

<h2 id="85f00a6be586ae47e453334f7168588a"></h2>


## Optional init

 - `init` now can return nil

```swift
// Optional init
class Circle: Shape {
    var radius: Int
    override func getArea() -> Int {
        return 3 * radius * radius
    }

    // Place a question mark postfix after `init` is an optional init
    // which can return nil
    init?(radius: Int) {
        self.radius = radius
        super.init()

        if radius <= 0 {
            return nil
        }
    }
}
var myCircle = Circle(radius: 1)
print(myCircle?.getArea())    // Optional(3)
print(myCircle!.getArea())    // 3

```

<h2 id="1b22e7dc709b52f1767fe1eb5dc56625"></h2>


# Enums 

 - Enums can optionally be of a specific type or on their own
 - They can contain methods like classes

```swift
enum Suit {
    case Spades, Hearts, Diamonds, Clubs
    func getIcon() -> String {
        switch self {
        case .Spades: return "♤"
        case .Hearts: return "♡"
        case .Diamonds: return "♢"
        case .Clubs: return "♧"
        }
    }
}
```

 - Enum values allow short hand syntax, no need to type the enum type
    - when the variable is explicitly declared

```swift
var suitValue: Suit = .Hearts
```

 - String enums can have direct raw value assignments
    - or their raw values will be derived from the Enum field

```swift
enum BookName: String {
    case John
    case Luke = "Luke"
}
print("Name: \(BookName.John.rawValue)")  // John
print("Name: \(BookName.John)")           // John
print("Name: \(BookName.Luke.rawValue)")  // rawLuke
print("Name: \(BookName.Luke)")           // Luke
```

 - Enum with associated Values

```swift
enum Furniture {
    // Associate with Int
    case Desk(height: Int)
    // Associate with String and Int
    case Chair(String, Int)

    func description() -> String {
        switch self {
        case .Desk(let height):
            return "Desk with \(height) cm"
        case .Chair(let brand, let height):
            return "Chair of \(brand) with \(height) cm"
        }
    }
}
var desk: Furniture = .Desk(height: 80)
print(desk.description())     // "Desk with 80 cm"
var chair = Furniture.Chair("Foo", 40)
print(chair.description())    // "Chair of Foo with 40 cm"
```

<h2 id="8da882f7c6705dad7abd441bf232c671"></h2>


## Tips : Enum 类型安全

 - eg. switch中 对字符串做匹配，是一种很危险的做法
 - 因为我们不能保证 switch case 中的字符串有没编写正确
 - 使用 enum  可以在编译期间发现你的错误

<h2 id="9985b4390c40137573e6da05caf85874"></h2>


# Protocols

```swift
protocol ShapeGenerator {
    var enabled: Bool { get set }
    func buildShape() -> Shape
}
```

 - 使用 @objc 声明的协议允许 optional functions , which allow you to check for conformance
 - 这些函数也必须用 @objc 标记。

```swift
@objc protocol TransformShape {
    @objc optional func reshape()
    @objc optional func canReshape() -> Bool
}

class MyShape: Rect {
    var delegate: TransformShape?

    func grow() {
        sideLength += 2

        // Place a question mark after an optional property, method, or
        // subscript to gracefully ignore a nil value and return nil
        // instead of throwing a runtime error ("optional chaining").
        if let reshape = self.delegate?.canReshape?(), reshape {
            // test for delegate then for method
            self.delegate?.reshape?()
        }
    }
}
```

<h2 id="63e4e92bb7d207ca577b11c07f827279"></h2>


# Extension

 - Add extra functionality to an already existing type

```swift
// Tips:  Better Version than define a square function 
extension Int { 
    var squared: Int { return self * self }
}
5.squared // 25
5.squared.squared // 625
```

<h2 id="0d7bdbf7f4e4f0dc8ed310a01dee3502"></h2>


# Generics

 - Similar to Java and C#
 - Use the `where` keyword to specify the requirements of the generics.

```swift
func findIndex<T: Equatable>(array: [T], valueToFind: T) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
let foundAtIndex = findIndex(array: [1, 2, 3, 4], valueToFind: 3)
print(foundAtIndex == 2) // true
```

<h2 id="b3c5827f54218753bb2c3338236446c2"></h2>


# Operators

 - Custom operators can start with the characters:
    - `  / = - + * % < > ! & | ^ . ~ `
 - or 
    - `  Unicode math, symbol, arrow, dingbat, and line/box drawing characters  `

```swift
prefix operator !!!

// A prefix operator that triples the side length when used
prefix func !!! (shape: inout Square) -> Square {
    shape.sideLength *= 3
    return shape
}
// current value
print(mySquare.sideLength) // 4
!!!mySquare
print(mySquare.sideLength) // 12

// Operators can also be generics
infix operator <->
func <-><T: Equatable> (a: inout T, b: inout T) {
    let c = a
    a = b
    b = c
}
var foo: Float = 10
var bar: Float = 20

foo <-> bar
print("foo is \(foo), bar is \(bar)") // "foo is 20.0, bar is 10.0"

```

----



