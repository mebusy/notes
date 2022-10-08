
# 5 Must Know JavaScript Features

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


## 2. style out console.log in browser

- you can actually apply css styling to console.log
    - all you do is to add a `%c` before the text you want to style, then you pass another property to your console log which is going to be your css styles.
    ```javascript
    console.log( `%c ${description} With Tax: %c $${total}`, 
                    "font-weight: bold; color: red",
                    "color: green" );
    ```


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


## 5. :)



