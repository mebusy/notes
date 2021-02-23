
# Web Dev

## 5. Using Javascript to Build Web Applications

### 5.53 DOM Manipulation

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <script src="js/script.js"></script>
  </head>
<body>
  <h1 id="title">Lecture 54</h1>

  <p>
    Say hello to
    <input id="name" type="text">
    <button onclick="sayHello();">
      Say it!
    </button>
  </p>


  <div id="content"></div>
</body>
</html>
```

- fetch HTML element
    ```javascript
    document.getElementById( "title" )
    // <h1 id="title">Lecture 53</h1>
    ```
    - PS. Be sure that "title" element exists in rendering HTML page before `document.getElementById` invoking, or it will result in `null`.
        - So javascript code is always best not to keep it in the head, but actually place it at the very end.
- Change HTML structure
    ```javascript
    function sayHello() {
        var name = document.getElementById( "name" ).value;
        var message = "Hello " + name + "!";

        document.getElementById( "content" ).textContent = message;
    }
    ```
    - How can I change "content" text to h2 headering ? 
        ```javascript
        var message = "<h2>Hello " + name + "!</h2>";
        ```
        - Adding h2 tag literally does not work, it is just text, not really something that the browser should render.
    - How to solve it ?
        ```javascript
            // document.getElementById( "content" ).textContent = message;
            document.getElementById( "content" ).innerHTML = message;
        ```
- QuerySelector
    - the way you select things using CSS
    ```javascript
    document.querySelector( "#title" ).textContent = "XXX";
    // document.querySelector( "h1" )   // will return the first matching element
    // document.queryAllSelector( "h1" )   // a list of all matching element
    ```


### 5.54 Handling Events

- In Lecture 53, we've already seen a simple example of how to bind an event handler to a particular element. 
    ```html
    <button onclick="sayHello();">
    ```
    - Let's explore now couple of different ways that you can actually assign event handlers to elements.
- What is event handler ?
    - Well event handlers are basically functions that you bind using specific methods to certain events that happen in the browser. 
    - Those events might be triggered by just a lifecycle. Meaning something like the page loaded.  Or it could be triggered by user interaction, like a user typed a character or user clipped something. 
- One of the most simplest ways to assign an event handler to a particular element is to just use the ***on***`<something>` attribute on that element. 
    - onblur(lose focus), onclick, ondblclick, onfocus, onkeydown, onkeypress, onkeyup, onmousedown, 
    - This method comes with some side effects.
        1. you kind of have to dirty up your HTML with these on-events, we may hope the HTML is just for content.
        2. `this` in `sayHello` function is pointing to *window* object because `sayHello` function is defined in Global scope.
- UnObtrusive Event Binding
    - The HTML does not need to know anything about your JavaScript.
    ```javascript
    function sayHello() {
        ...
    }

    document.querySelector("button").addEventListener( "click", sayHello );
    ```
    - Now `this` in `sayHello` function is pointing to the containing object, the *button* element.
- Another similar way
    ```javascript
    document.querySelector("button").onclick = sayHello ;
    ```
- **DOMContentLoaded** event
    - a life cycle event of the page
    - that will let us actually assign the events to the elements of the page once they load, but before anything else loads. Before any images load, before any CSS loads, and so forth. 
    - And since we are going to be listening for that event, we no longer need to provide this script at the bottom of the page. We can actually cut this script out of here, and place it very easily in the head. 
        ```javascript
        document.addEventListener("DOMContentLoaded", 
            ...
        );
        ```
    - What we want to do is we want to assign a function, with parameter `event`, and every event handler function gets this event object. 
        ```javascript
        document.addEventListener("DOMContentLoaded", 
            function (event) {
                ...
            }  
        );
        ```
    - and inside this function, we can now start assigning different events. 
        ```javascript
        document.addEventListener("DOMContentLoaded", 
            function (event) {
                function sayHello (event) {
                    ...
                }
                // Unobtrusive event binding
                document.querySelector("button").addEventListener("click", sayHello);
            }  
        );
        ```
        - This function will get executed when this Event files called, dom content loaded and that will happen before any images, or any CSS, or any other script is loaded. 


### 5.55 The 'event' Argument

- When mouse-left clicking the button, the object that *event* is `MouseEvent`.
    - PS. you would not get *event* if you bind the function via `on-event` attributes in HTML.


### -- Introduction to Ajax --

### 5.57 Ajax Basics

- Asynchronous Javascript and XML
- While Ajax started with XML, very few apps use it nowadays
    - Plain text (at time as html) and JSON is used instead
- Why does Ajax exist to begin with ? 
    - Faster response.  Less bandwidth, nicer experience for user
- ![](../imgs/ajax_how_work.png)
- ![](../imgs/ajax_how_work_2.png)











