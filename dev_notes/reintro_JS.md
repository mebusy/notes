...menustart

- [A re-introduction to JavaScript (JS tutorial)](#428d98b5f468d03038613c780e48fc10)
    - [概要](#7f1b21a571bc81517bbf8b85b1ef7ccd)
    - [Overview](#3b878279a04dc47d60932cb294d96259)
    - [Numbers](#cbebfa21dbe8e87e788d94a76f073807)
    - [Strings](#89be9433646f5939040a78971a5d103a)
    - [Other types](#45950ecb4d9add6d144ed6737c704ca0)
    - [Variables](#03df896fc71cd516fdcf44aa699c4933)
    - [Operators](#b3c5827f54218753bb2c3338236446c2)
    - [Control structures](#c48b7d4c81fcf51917066528ff5693ed)
        - [if / eles if / else](#015a27f9173988da8d0b60ad7c792c40)
        - [while / do-while](#02cb511523ca2dd3ea4d157f0f320bc0)
        - [for](#d55669822f1a8cf72ec1911e462a54eb)
        - [for...of  / for...in](#6e733d018832ecf41889c33c7d482146)
        - [ternary operator](#7b8ca31408defce69dd51a57cfeff402)
        - [switch](#b36eb6a54154f7301f004e1e61c87ce8)
    - [Objects](#c8308b1eba7ba926a61b8fd802194386)
    - [Arrays](#ff43b8de4f41d5103405ddb62eb8d34e)
    - [Functions](#e93acb146e114b5dfa6ce2d12dcb96e4)
    - [Custom objects](#061617f5237c49568715cd05ceef505d)
    - [其它 ES6 新特性](#3e3612786cff54b6bdbbbaa3f5fa85d7)
        - [arrow function](#7cb73e5605aec93918bd62ec843a5745)
        - [Class](#9bd81329febf6efe22788e03ddeaf0af)
            - [Defining classes](#12a4166e02c1f403d1f1edab72b67926)
            - [Class expressions](#3d8bb55eea05a180febf5200d718f41c)
            - [Class body and method definitions](#a912551971a309d598fa34bca20f4b5e)
            - [Sub classing with extends](#d2de17645050c3f9b094d417f647f2ca)
            - [Species](#e1520b5997a532c7889f6e8883920ab8)
            - [Super class calls with super](#e5b796fae796980b73c254cccd1851d5)
- [tips](#e4c9479b11955648dad558fe717a4eb2)
    - [compress js code](#1102ba00437059603c9604fb050a22f8)
    - [Where to Place Javascript Code](#e59dff2a7bc095a7b28e848acf35037f)
    - [Fake Namespace](#8a1b8ba8dbe3ebda08deb8be54811e88)

...menuend


<h2 id="428d98b5f468d03038613c780e48fc10"></h2>


# A re-introduction to JavaScript (JS tutorial)


<h2 id="7f1b21a571bc81517bbf8b85b1ef7ccd"></h2>


## 概要

- JS 的`&& || `更像python里面的 and / or
- blocks do not have scope (like python); only functions have a scope.
    - 在ECMAScript 6中你可以通过使用let and const 来定义块级别的变量。
- for...of array
    - for...in object
- function, Array 都是 Object, 所以都可以通过new 创建
- function 有很多手段支持变长参数 
    - call:  func.apply(null, arg_array ) 
    - or func( ... arg_array )
- 箭头函数没有自己的this
- 理解this
    - JS（ES5）三种函数调用形式：
        - func(p1, p2) 
        - obj.child.method(p1, p2)
        - func.call(context, p1, p2) // 先不讲 apply
    - 前两种是语法糖，第三种才是正确的调用方式
        - func(p1, p2) 等价于 func.call(undefined, p1, p2)
        - obj.child.method(p1, p2) 等价于obj.child.method.call(obj.child, p1, p2)
    - 函数调用只有一种形式：
        - func.call(context, p1, p2)
        - **this，就是上面代码中的 context**
    - 其他
        - `new foo()` 构造函数中，foo函数内部的this永远是new foo()返回的对象
        - 箭头函数没有自己的this, 箭头函数在设计中使用的是Lexical this


--------------------------------


<h2 id="3b878279a04dc47d60932cb294d96259"></h2>


## Overview

- JavaScript's types are:
    - Number : double-precision 64-bit
    - String
    - Boolean
    - Symbol (new in ES6 2015)
    - Object
        - Function
        - Array 
        - Date
        - RegExp
    - null
        - lack of value
    - undefined
        - lack of definition

- And there are some built-in Error types as well.

<h2 id="cbebfa21dbe8e87e788d94a76f073807"></h2>


## Numbers

- Math
    - Math.sin(3.5)
- convert a string to an integer
    - parseInt('123', 10); // 123
    - parseInt('010', 10); // 10
        - In older browsers, strings beginning with a "0" are assumed to be in octal
        - but this hasn't been the case since 2013 or so , octal has been removed.
    - parseInt('0x10'); // 16
    - parseInt('11', 2); // 3
- parse floating point numbers 
    - parseFloat() always uses base 10. 
- You can also use the unary + operator to convert values to numbers:

```javascript
+ '42';   // 42
+ '010';  // 10
+ '0x10'; // 16
```

- A special value called `NaN` (short for "Not a Number") is returned if the string is non-numeric:

```javascript
parseInt('hello', 10); // NaN
```

- You can test for NaN using the built-in isNaN() function:
    - `isNaN(NaN); // true`
- JavaScript also has the special values Infinity and -Infinity:

```javascript
1 / 0; //  Infinity
-1 / 0; // -Infinity
```

- You can test for Infinity, -Infinity and NaN values using the built-in isFinite() function

```javascript
isFinite(1 / 0); // false
isFinite(-Infinity); // false
isFinite(NaN); // false
```

<h2 id="89be9433646f5939040a78971a5d103a"></h2>


## Strings

- sequences of Unicode characters , More accurately, they are sequences of UTF-16 code units

```javascript
'hello'.length; // 5
'hello'.charAt(0); // "h"
'hello, world'.replace('hello', 'goodbye'); // "goodbye, world"
'hello'.toUpperCase(); // "HELLO"
```

<h2 id="45950ecb4d9add6d144ed6737c704ca0"></h2>


## Other types

- javascript 区分 null 和 undefined
- boolean  ( support `&& || !` , **`&& ||` 更像python里面的 and / or**  )
    1. **false, 0, empty strings (""), NaN, null, and undefined** all become false.
    2. All other values become true.

```javascript
// rarely necessary, 
// as JavaScript will silently perform this conversion
Boolean('');  // false
Boolean(234); // true
```

- The && and || operators use short-circuit logic

```javascript
var name = o && o.getName();
var name = cachedName || (cachedName = getName());
```


<h2 id="03df896fc71cd516fdcf44aa699c4933"></h2>


## Variables

- declared keywords
    - let
        - to declare block-level variables.
        - available from the block it is enclosed in.
    - const
        - to declare variables whose values are never intended to change.
        - available from the block it is declared in
    - var 
        - available from the function it is declared in.

```javascript
// myLetVariable is *not* visible out here
for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
  // myLetVariable is only visible in here
}
// myLetVariable is *not* visible out here
```

```javascript
// myVarVariable *is* visible out here

for (var myVarVariable = 0; myVarVariable < 5; myVarVariable++) {
  // myVarVariable is visible to the whole function
}

// myVarVariable *is* visible out here
```

- An important difference between JavaScript and other languages like Java is that: 
    - **in JavaScript, blocks do not have scope; only functions have a scope**. 
    - So if a variable is defined using var in a compound statement (for example inside an if control structure), it will be visible to the entire function. 
    - However, starting with ECMAScript 2015, let and const declarations allow you to create block-scoped variables.


<details>
<summary>
Scope Chain
</summary>

- Everything is executed in an Execution Context
- Function invocation creates a new Execution Context
- Each Execution Context has:
    - It's own Variable Environment
    - Special 'this' object
    - Reference to its Outer Environment
- Global scope does not have an Outer Environment as it's the most outer there is.

- How scope chain works
    - Referenced ( **not defined** ) variable will be searched for in its **current** scope first.
        - If not found, the **Outer** Reference will be searched, etc
    - This will keep going until the Global scope.
        - If not found in Global scope, the variable is *undefined*.
- Example
    ```javascript
    var x = 2;
    A();

    function A() {
        var x = 5;
        B();
    }

    function B() {
        console.log(x)
    }

    // Result: x=2
    ```
    - Even though *B* is called within *A*, and *A*  has its own *x*, what actually matters as far as resolving where x is coming from is its **outer reference**. 
    - And *B* is defined within the global scope. Therefore, the outer reference of function *B* is the global scope, not function *A*. 


</details>

<h2 id="b3c5827f54218753bb2c3338236446c2"></h2>


## Operators

- `+, -, *, / , % `
- `>= , <= , ==`

```javascript
'3' + 4 + 5;  // "345"
 3 + 4 + '5'; // "75"
```

- `==` operator performs type coercion if you give it different types

```javascript
123 == '123'; // true
1 == true; // true
```

- To avoid type coercion, use the triple-equals operator:

```javascript
123 === '123'; // false
1 === true;    // false
```

- There are also != and !== operators.
- `>` , `<` 等等 操作也会 做类型转换

- bitwise operations also support
    - `& | `
    - XOR `^`
    - NOT `~`
    - `<< >> >>>`

<h2 id="c48b7d4c81fcf51917066528ff5693ed"></h2>


## Control structures

- JavaScript has a similar set of control structures to other languages in the C family

<h2 id="015a27f9173988da8d0b60ad7c792c40"></h2>


### if / eles if / else 

```javascript
if (name == 'puppies') {
  name += ' woof';
} else if (name == 'kittens') {
  name += ' meow';
} else {
  name += '!';
}
```

<h2 id="02cb511523ca2dd3ea4d157f0f320bc0"></h2>


### while / do-while

```javascript
while (true) {
  // an infinite loop!
}

var input;
do {
  input = get_input();
} while (inputIsNotValid(input));
```

<h2 id="d55669822f1a8cf72ec1911e462a54eb"></h2>


### for 

```javascript
// for loop is the same as that in C and Java
for (var i = 0; i < 5; i++) {
  // Will execute 5 times
}
```

<h2 id="6e733d018832ecf41889c33c7d482146"></h2>


### for...of  / for...in

- JavaScript also contains two other prominent for loops: for...of

```javascript
for (let value of array) {
  // do something with value
}
```


- and for...in:

```javascript
for (let property in object) {
  // do something with object property
}
```

- 你也可以使用 for..in 来遍历数组，但是不推荐，原因见下面 Array 一节

<h2 id="7b8ca31408defce69dd51a57cfeff402"></h2>


### ternary operator

- JavaScript has a ternary operator for conditional expressions:

```javascript
var allowed = (age > 18) ? 'yes' : 'no';
```

<h2 id="b36eb6a54154f7301f004e1e61c87ce8"></h2>


### switch

- The switch statement can be used for multiple branches based on a number or string:

```javascript
switch (action) {
  case 'draw':
    drawIt();
    break;
  case 'eat':
    eatIt();
    break;
  default:
    doNothing();
}
```

<h2 id="c8308b1eba7ba926a61b8fd802194386"></h2>


## Objects

- JavaScript objects can be thought of as simple collections of name-value pairs
    - As such, they are similar to: Dictionaries in Python.
- create an empty object:

```javascript
var obj = new Object();
// or
var obj = {};
```

- This syntax is also the **core of JSON format** and should be preferred at all times.

```javascript
var obj = {
  name: 'Carrot',
  for: 'Max', // 'for' is a reserved word, use '\_for' instead.
  details: {
    color: 'orange',
    size: 12
  }
};

obj.details.color; // orange
obj['details']['size']; // 12

// but there is something different
obj.for = 'Simon'; // Syntax error, because 'for' is a reserved word
obj['for'] = 'Simon'; // works fine
```

- The following example creates an object prototype, Person and an instance of that prototype, You.

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// Define an object
var you = new Person('You', 24); 
// We are creating a new person named "You" aged 24.
```

<h2 id="ff43b8de4f41d5103405ddb62eb8d34e"></h2>


## Arrays

```javascript
var a = new Array();
a[0] = 'dog';
a[1] = 'cat';
a[2] = 'hen';
a.length; // 3
```

```javascript
var a = ['dog', 'cat', 'hen'];
a.length; // 3
```

- Note that array.length isn't necessarily the number of items in the array. 
    - the length of the array is one more than the highest index.

```javascript
var a = ['dog', 'cat', 'hen'];
a[100] = 'fox';
a.length; // 101
```

- we can use for...of loop for iterable objects such as arrays:
- You could also iterate over an array using a for...in loop. 
    - But if someone added new properties to Array.prototype, they would also be iterated over by this loop for...in
    - Therefore this loop type is not recommended for arrays.
- Another way of iterating over an array that was added with ECMAScript 5 is forEach():

```javascript
['dog', 'cat', 'hen'].forEach(function(currentValue, index, array) {
  // Do something with currentValue or array[index]
});
```

- append an item

```javascript
a.push(item);
```

- [full documentation for array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

---

 Method name | Description
--- | --- 
a.toString() | Returns a string with the toString() of each element separated by commas.
a.toLocaleString() | Returns a string with the toLocaleString() of each element separated by commas.
a.concat(item1[, item2[, ...[, itemN]]]) | Returns a new array with the items added on to it.
a.join(sep) | Converts the array to a string — with values delimited by the sep param
a.pop() | Removes and returns the last item.
a.push(item1, ..., itemN) | Appends items to the end of the array.
a.reverse() | Reverses the array.
a.shift() | Removes and returns the first item.
a.slice(start[, end]) | Returns a sub-array.
a.sort([cmpfn]) | Takes an optional comparison function.
a.splice(start, delcount[, item1[, ...[, itemN]]]) | Lets you modify an array by deleting a section and replacing it with more items.
a.unshift(item1[, item2[, ...[, itemN]]]) | Prepends items to the start of the array.


<h2 id="e93acb146e114b5dfa6ce2d12dcb96e4"></h2>


## Functions

- The most basic function couldn't be much simpler:

```javascript
function add(x, y) {
  var total = x + y;
  return total;
}
```

- That may seem a little silly, but functions have access to an additional variable inside their body called *arguments*

```javascript
function add() {
  var sum = 0;
  for (var i = 0, j = arguments.length; i < j; i++) {
    sum += arguments[i];
  }
  return sum;
}

add(2, 3, 4, 5); // 14
```

- This is pretty useful, but it does seem a little verbose
    - you can also use **rest parameter operator** to do same thing

```javascript
function avg(...args) {
  var sum = 0;
  for (let value of args) {
    sum += value;
  }
  return sum / args.length;
}

avg(2, 3, 4, 5); // 3.5
```

- but how do you calc average on all array's elements ?
    - you may re-write another function like :

```javascript
function avgArray(arr) { ... }  
avgArray([2, 3, 4, 5]); // 3.5 
```

- But it would be nice to be able to reuse the function that we've already created.
    - Luckily, JavaScript lets you call a function with an arbitrary array of arguments,
    - using the apply() method of any function object.

```javascript
avg.apply(null, [2, 3, 4, 5]); // 3.5
```

- 你还可以使用 **spread operator**  把数组展开

```javascript
const numbers = [1, 2, 3];
avg( ...numbers )
```

- anonymous functions

```javascript
var avg = function() { ... }
```

- It's extremely powerful, as it lets you put a full function definition anywhere that you would normally put an expression. 
    - This enables all sorts of clever tricks. 
- Here's a way of "hiding" some local variables — like block scope in C:

```javascript
var a = 1;
var b = 2;

(function() {
  var b = 3;
  a += b;
})();

a; // 4
b; // 2
```

- 现在带来一个问题： 匿名函数如何递归调用？
    - You can use named IIFEs (Immediately Invoked Function Expressions)
    - see `counter` in above codes

```javascript
var charsInBody = (function counter(elm) {
  if (elm.nodeType == 3) { // TEXT_NODE
    return elm.nodeValue.length;
  }
  var count = 0;
  for (var i = 0, child; child = elm.childNodes[i]; i++) {
    count += counter(child);
  }
  return count;
})(document.body);
```


<h2 id="061617f5237c49568715cd05ceef505d"></h2>


## Custom objects

- JavaScript is a prototype-based language that contains no class statement
- Instead, JavaScript uses functions as classes. 

```javascript
function makePerson(first, last) {
  return {
    first: first,
    last: last
  };
}

function personFullName(person) {
  return person.first + ' ' + person.last;
}

s = makePerson('Simon', 'Willison');
personFullName(s); // "Simon Willison"
```

- This works, but it's pretty ugly. 
    - **You end up with dozens of functions in your global namespace.**
- What we really need is a way to attach a function to an object. 
    - Since functions are objects, this is easy:

```javascript
function makePerson(first, last) {
  return {
    first: first,
    last: last,
    fullName: function() {
      return this.first + ' ' + this.last;
    }
  };
}

s = makePerson('Simon', 'Willison');
s.fullName(); // "Simon Willison"
```


- There's something here we haven't seen before: the **this** keyword
    - Used inside a function, `this` refers to the current object. 
- Note that this is a frequent cause of mistakes

```javascript
s = makePerson('Simon', 'Willison');
var fullName = s.fullName;
fullName(); // undefined undefined
```

- When we call fullName() alone, without using s.fullName(), `this` is bound to the global object.
- We can take advantage of the this keyword to improve our makePerson function:

```javascript
function Person(first, last) {
  this.first = first;
  this.last = last;
  this.fullName = function() {
    return this.first + ' ' + this.last;
  };
  this.fullNameReversed = function() {
    return this.last + ', ' + this.first;
  };
}
var s = new Person('Simon', 'Willison');
```

- We have introduced another keyword: **new**.
    - new is strongly related to this
    - It creates a brand new empty object,
        - and then calls the function specified,
        - with `this` set to that new object.  
- Note: function specified with `this` does not return a value but merely modifies the this object. 
    - It's `new` that returns the `this` object to the calling site.
- Functions that are designed to be called by `new` are called constructor functions. 

- 我们的 Person 看起来已经不错了。但是每次创建一个  Person 对象，我们就会创建一个全新的 function 对象。
    - function 应该是共享的才好
    ```javascript
    // try 1
    function personFullName() {
      return this.first + ' ' + this.last;
    }
    function Person(first, last) {
      this.first = first;
      this.last = last;
      this.fullName = personFullName;
    }
    ```

- 更好的做法:
    ```javascript
    function Person(first, last) {
      this.first = first;
      this.last = last;
    }
    Person.prototype.fullName = function() {
      return this.first + ' ' + this.last;
    };
    ```

- **Person.prototype** is an object shared by all instances of Person.
    - 当你尝试 访问 没有设置的 Person属性时， Javascript 都会检查 Person.prototype 看属性是否存在。

- Interestingly, you can also add things to the prototype of built-in JavaScript objects.
    ```javascript
    var s = 'Simon';
    s.reversed(); // TypeError on line 1: s.reversed is not a function

    String.prototype.reversed = function() {
      var r = '';
      for (var i = this.length - 1; i >= 0; i--) {
        r += this[i];
      }
      return r;
    };

    s.reversed(); // nomiS

    'This can now be reversed'.reversed(); // desrever eb won nac sihT
    ```

- the prototype forms part of a chain
    - The root of that chain is Object.prototype, whose methods include toString() 
    - This is useful for debugging our Person objects:
    ```javascript
    var s = new Person('Simon', 'Willison');
    s.toString(); // [object Object]

    Person.prototype.toString = function() {
      return '<Person: ' + this.fullName() + '>';
    }
    s.toString(); // "<Person: Simon Willison>"
    ```

- Remember how avg.apply() had a null first argument? 
    - The first argument to apply() is the object that should be treated as 'this'.
    - For example, here's a trivial implementation of *new*:

```javascript
function trivialNew(constructor, ...args) {
  var o = {}; // Create an object
  constructor.apply(o, args);
  return o;
}
```

```javascript
// Calling
var bill = trivialNew(Person, 'William', 'Orange');

// is therefore almost equivalent to
var bill = new Person('William', 'Orange');
```

- apply() has a sister function named `call`
    - which again lets you set `this` but takes an expanded argument list as opposed to an array.

```javascript
function lastNameCaps() {
  return this.last.toUpperCase();
}
var s = new Person('Simon', 'Willison');
lastNameCaps.call(s);
// Is the same as:
s.lastNameCaps = lastNameCaps;
s.lastNameCaps(); // WILLISON
```

<h2 id="3e3612786cff54b6bdbbbaa3f5fa85d7"></h2>


## 其它 ES6 新特性

<h2 id="7cb73e5605aec93918bd62ec843a5745"></h2>


### arrow function

- An arrow function expression has a shorter syntax than a function expression and does not have its own `this, arguments, super, or new.target`. 
- These function expressions are best suited for non-method functions, and they cannot be used as constructors.

```javascript
var materials = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium'
];

console.log(materials.map(material => material.length));
```

<h2 id="9bd81329febf6efe22788e03ddeaf0af"></h2>


### Class

- 只是语法糖， 并没有引入任何新模型

<h2 id="12a4166e02c1f403d1f1edab72b67926"></h2>


#### Defining classes

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```

<h2 id="3d8bb55eea05a180febf5200d718f41c"></h2>


#### Class expressions

```javascript
// unnamed
var Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle"

// named
var Rectangle = class Rectangle2 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
console.log(Rectangle.name);
// output: "Rectangle2"
```

<h2 id="a912551971a309d598fa34bca20f4b5e"></h2>


#### Class body and method definitions

- Strict mode
    - The bodies of class declarations and class expressions are executed in *strict mode* , i.e.:
        - constructor, static and prototype methods, getter and setter functions
- Constructor
    - constructor can use the *super* keyword to call the constructor of the super class.
- Prototype methods
    - see  method definitions

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.calcArea();
  }
  // Method
  calcArea() {
    return this.height * this.width;
  }
}

const square = new Rectangle(10, 10);
console.log(square.area); // 100
```

- Static methods
    - Static methods are called without instantiating their class and **cannot** be called through a class instance. 

```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static distance(a, b) {
    const dx = a.x - b.x;
    const dy = a.y - b.y;

    return Math.hypot(dx, dy);
  }
}

console.log(Point.distance(p1, p2));
```

**Instance properties**

- Instance properties must be defined inside of class methods:

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```

- Static class-side properties and prototype data properties must be defined outside of the ClassBody declaration:

```javascript
Rectangle.staticWidth = 20;
Rectangle.prototype.prototypeWidth = 25;
```

<h2 id="d2de17645050c3f9b094d417f647f2ca"></h2>


#### Sub classing with extends

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(this.name + ' makes a noise.');
  }
}

class Dog extends Animal {
  speak() {
    console.log(this.name + ' barks.');
  }
}

var d = new Dog('Mitzie');
d.speak(); // Mitzie barks.
```

- If there is a constructor present in subclass, it needs to first call super() before using "this".

- One may also extend traditional function-based "classes":

```javascript
function Animal (name) {
  this.name = name;
}

Animal.prototype.speak = function () {
  console.log(this.name + ' makes a noise.');
}

class Dog extends Animal {
  speak() {
    console.log(this.name + ' barks.');
  }
}

var d = new Dog('Mitzie');
d.speak(); // Mitzie barks.
```

- Note that classes cannot extend regular (non-constructible) objects. 
    - If you want to inherit from a regular object, you can instead use `Object.setPrototypeOf()`:

```javascript
var Animal = {
  speak() {
    console.log(this.name + ' makes a noise.');
  }
};

class Dog {
  constructor(name) {
    this.name = name;
  }
}

// If you do not do this you will get a TypeError when you invoke speak
Object.setPrototypeOf(Dog.prototype, Animal);

var d = new Dog('Mitzie');
d.speak(); // Mitzie makes a noise.
```

<h2 id="e1520b5997a532c7889f6e8883920ab8"></h2>


#### Species

- You might want to return `Array` objects in your derived array class MyArray. 
- The species pattern lets you override default constructors.
- For example, when using methods such as map() that returns the default constructor,
    - you want these methods to return a parent Array object, 
    - instead of the MyArray object. The Symbol.species symbol lets you do this:

```javascript
class MyArray extends Array {
  // Overwrite species to the parent Array constructor
  static get [Symbol.species]() { return Array; }
}

var a = new MyArray(1,2,3);
var mapped = a.map(x => x * x);

console.log(mapped instanceof MyArray); // false
console.log(mapped instanceof Array);   // true
```

<h2 id="e5b796fae796980b73c254cccd1851d5"></h2>


#### Super class calls with super

- The super keyword is used to call corresponding methods of super class.

```javascript
class Lion extends Cat {
  speak() {
    super.speak();
    console.log(this.name + ' roars.');
  }
}
```


<h2 id="e4c9479b11955648dad558fe717a4eb2"></h2>


# tips 

<h2 id="1102ba00437059603c9604fb050a22f8"></h2>


## compress js code

```javascript
npm install -g uglify-js
uglifyjs gd3d.js -c -m --keep-fnames -o xxx.min.js
```


<h2 id="e59dff2a7bc095a7b28e848acf35037f"></h2>


## Where to Place Javascript Code

```html
<head>
<script src="js/script.js"> </script>
<script> 
    ...
</script>
</head>

<body>

<script src="js/script.js"> </script>
<script>
    ...
</script>

</body>

```


<h2 id="8a1b8ba8dbe3ebda08deb8be54811e88"></h2>


## Fake Namespace

- Immediately Invoked Function Expressions are usually used to place code into its own execution context not to conflict with the global scope.
    - This can be used create fake namespace
    ```javascript
    // Immediately Invoked Function
    (
        function(global) {

            function sayHi() {
                var name = "John";
                var greeting = "Hi ";
                var sayHi = function() {
                    console.log( greeting + name )
                }
            } // end custom function

            // before the end of function(global) 
            // Export something the global object
            global.sayHi = sayHi;

        } // end function(global)

    )(global);   // for nodejs
    // )(window);  // for browser
    ```


