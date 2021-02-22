
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


