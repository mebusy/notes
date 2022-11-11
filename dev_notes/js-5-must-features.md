[](...menustart)

- [5 Must Know JavaScript Features](#26b3ea6eb8cfb08a2b117265827f17bf)
    - [1. ??](#5628a1882598532509d7ecd0a619b877)
    - [2. style out console.log in browser](#aa1e194d9312052d4f64ad47e00f1452)
    - [3. optional chaining](#b021ecb2ac83dbe4b666cd688c2210f8)
    - [4. defer load your javascript](#db3eb572dc091365d8ee4ce82108becd)
    - [5. :)](#4fdc87d5685bd3fab94ca196de4741b6)

[](...menuend)


<h2 id="26b3ea6eb8cfb08a2b117265827f17bf"></h2>

# 5 Must Know JavaScript Features

<h2 id="5628a1882598532509d7ecd0a619b877"></h2>

## 1. ??

```javascript
function calculatePrice(price, taxes, description) {
    taxes = taxes || 0.05
    description = description || 'Default description'
    const total = price + (price * taxes)
    console.log(total,  description)
}


calculatePrice(100, 0.1, 'My description')
// 110 My description
calculatePrice(100, 0, '')
// 105 Default description
```

- the issue here is when the taxes passed in is 0, its a false value, so taxes will eventually be 0.05, this is not what we expected.

- javascript has new thing called `nullish coalescing operator (??)` that returns its right-hand side operand when its left-hand side operand is **null or undefined**, and otherwise returns its left-hand side operand.
    ```javascript
    taxes = taxes ?? 0.05
    ```


<h2 id="aa1e194d9312052d4f64ad47e00f1452"></h2>

## 2. style out console.log in browser

- you can actually apply css styling to console.log
    - all you do is to add a `%c` before the text you want to style, then you pass another property to your console log which is going to be your css styles.
    ```javascript
    console.log( `%c ${description} With Tax: %c $${total}`, 
                    "font-weight: bold; color: red",
                    "color: green" );
    ```


<h2 id="b021ecb2ac83dbe4b666cd688c2210f8"></h2>

## 3. optional chaining 

- we often need write such kind codes to prevent undefined excepton
    ```javascript
    function printPersonStreet(person) {
        if ( person && person.address ) {
            console.log(person.address.street);
        }
    }
    ```
- javascript added an easier way to do this and it's something called optional chaining.
    ```javascript
    console.log(person?.address?.street);
    ```
    - ? means if things is not null/undefined, then continue 
- optional chaining can be used on things even beyond calling properties, it can be usd even on functions, or other stuffs.
    ```javascript
    // function
    kyle.printName?.()
    // array
    kyle.hobbies?.[0]
    ```


<h2 id="db3eb572dc091365d8ee4ce82108becd"></h2>

## 4. defer load your javascript

- we often needs to put our js script at the bottom of html body so that to guarentee the page to be rendered before executing javascript.
    ```html
    <body>
    <button>Hi</button>
    <!--  script.js will change the color of button text -->
    <script src="script.js"></script> 
    </body>
    ```
- the issue with is the download for you script tag doesn't start until the browser gets to it, which means it could slow down your page.
- but by just putting your javascript up in the head, and put `defer` inside it, 
    ```html
    <head>
    <script src="script.js" defer></script> 
    </head> 
    <body>
    ...
    ```
    - the browser gets the script tag , it downloads it but then it continues rendering out everything , adn then as soon as it's done rendering the entire page, then the script will be run.


<h2 id="4fdc87d5685bd3fab94ca196de4741b6"></h2>

## 5. :)



