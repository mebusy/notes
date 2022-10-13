...menustart

- [Learn JavaScript Event Listeners](#6d189e3b80b68b24f022b1374f10298d)
    - [addEventListener](#ad67ccdca808861a8462e31ddeb84fa7)
    - [removeEventListener](#be2c1712b98bf178b8e283bd18e226c5)
    - [How to delegate events](#697c9533e471a91b06c2daf896dde672)

...menuend


<h2 id="6d189e3b80b68b24f022b1374f10298d"></h2>


# Learn JavaScript Event Listeners

<h2 id="ad67ccdca808861a8462e31ddeb84fa7"></h2>


## addEventListener

```javascript
const grandparent = document.querySelector('.grandparent');
const parent = document.querySelector('.parent');
const child = document.querySelector('.child'); 

grandparent.addEventListener('click', e => {
    console.log('grandparent 1');
}); 
```

- 2~3 parameters
    - 1st is the event type, e.g. `'click'`
    - 2nd is the callback function, takes a single parameter which is the event object.

- we can add more event listeners
    ```javascript
    grandparent.addEventListener('click', e => {
        console.log('grandparent 2');
    }); 
    ```
    - those event listeners will be executed in the order we defined them

- when clicking on this childl, it still prints out the 'grandparent' messages. Why exactly is that?
    - this is called **event bubbling**, and this is 1/2 of how events work inside JS.
    - the other 1/2 of how they work is called **capturing**, that is where this 3rd parameter to the `addEventListener` comes into player.
    ```javascript
    grandparent.addEventListener('click', e => {
        console.log('grandparent 1');
    }, { capture: true}); 
    ```


<h2 id="be2c1712b98bf178b8e283bd18e226c5"></h2>


## removeEventListener

- to remove an event listener callback, you need explicitly define the callback function
    ```javascript
    function printHi() {
        console.log('hi');
    }
    parent.addEventListener('click', PrintHi );

    setTimeout(() => {
        parent.removeEventListener('click', PrintHi );
    }
    , 1000);
    ```

<h2 id="697c9533e471a91b06c2daf896dde672"></h2>


## How to delegate events

- really important when it comes to dynamically adding elements to a page.
- example:
    ```javascript
    const divs = document.querySelectorAll('div');
    // we want all divs in page have an event listener
    divs.forEach(div => {
        div.addEventListener('click', () => {
            console.log('dev clicked');
        });
    });

    // but the new one does not have
    const newDiv = document.createElement('div');
    newDiv.style.width = '200px';
    newDiv.style.height = '200px';
    newDiv.style.backgroundColor = 'red';
    document.body.appendChild(newDiv); 
    ```
- to solve this problem, we can use **event delegation**
    ```javascript
    document.addEventListener('click', e => {
        if (e.target.matches('div')) {
            console.log('div clicked');
        }
    });
    ```
- generally I like to tun this into a function
    ```javascript
    function addGlobalEventListener(type, selector, callback) {
        document.addEventListener(type, e => {
            if (e.target.matches(selector)) callback(e);
        });
    }

    addGlobalEventListener('click', 'div', e => {
        console.log('div clicked');
    });
    ```



