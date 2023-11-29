[](...menustart)

- [Promise](#a5a3f0f287a448982aac520cffe4779a)
    - [What is Promise](#42c13d91edca77a10e5e59f6936ee2c9)
    - [What problem can Promises solve ?](#7b9bcee29941c7e84649a74394a12b7a)
    - [What else can Promises do ?](#2e533b31a6610c21756a5aac95c9d7f0)

[](...menuend)


<h2 id="a5a3f0f287a448982aac520cffe4779a"></h2>

# Promise

<h2 id="42c13d91edca77a10e5e59f6936ee2c9"></h2>

## What is Promise

- 2 results
    - resolve
    - reject
- Promise takes a function with 2 parameters as its (Promise's) paremeter
    ```javascript
    let p = new Promise((resolve, reject) => {
        let a = 1 + 1
        if (a == 2) {
            resolve('Success')
        } else {
            reject('Failed')
        }
    });
    ```
- how we actually interact with promise ?
    - all we have to do is say anything inside `.then()`  is going to run for `resolve`
        ```javascript
        p.then((message) => {
            console.log('This is in the then ' + message)
        } )
        ;
        ```
    - but, to be able to catch an error, we need use the `.catch()` version of this
        ```javascript
        p.then((message) => {
            console.log('This is in the then ' + message)
        } )
        .catch((message) => {
            console.log('This is in the catch ' + message)
        })
        ;
        ```
        ```bash
        # result
        This is in the then Success
        ```

<h2 id="7b9bcee29941c7e84649a74394a12b7a"></h2>

## What problem can Promises solve ?

- let's look at an example of how we can take something that uses callbacks which is what promises are meant to replace and actually replace it with promises and it's a lot easier than it sounds.
    ```javascript
    const userLeft = false;
    const userWatchingCatMeme = false;

    // takes 2 arguments, a success callback and a failure callback
    function watchTutorialCallback(callback, errorCallback) {
        if (userLeft) {
            errorCallback({
            name: 'User Left',
            message: ':('
            });
        } else if (userWatchingCatMeme) {
            errorCallback({
            name: 'User Watching Cat Meme',
            message: 'WebDevSimplified < Cat'
            });
        } else {
            callback('Thumbs up and Subscribe');
        }
    }

    watchTutorialCallback(
        (message) => {
            console.log('Success: ' + message);
        } ,
        (error) => {
            console.log(error.name + ' ' + error.message);
        }
    );  
    ```
- now let's implement this using promises instead of callbacks becauses this is what promises were really meant to solve.
    1. let's new function name `watchTutorialCallback` to `watchTutorialPromise`
    2. completely remote those callback function parameters , because using promises we no longer have these callbacks
        ```javascript
        function watchTutorialPromise() {
        ```
    3. all we need to do inside of here is return a promise.
        ```javascript
        return new Promise((resolve, reject) => {

        });
        ```
    4. and inside of that function we just want to define all of our code that was calling these callbacks, and rename the callback functions to resolve and reject
        ```javascript
        function watchTutorialPromise() {
            return new Promise((resolve, reject) => {
                // just copy and paste the code from the callback function
                // and rename the callback functions to resolve and reject
                if (userLeft) {
                    reject({
                    name: 'User Left',
                    message: ':('
                    });
                } else if (userWatchingCatMeme) {
                    reject({
                    name: 'User Watching Cat Meme',
                    message: 'WebDevSimplified < Cat'
                    });
                } else {
                    resolve('Thumbs up and Subscribe');
                }
            });
        }
        ```
- use this function
    ```javascript
    watchTutorialPromise().then(  // <- watchTutorialCallback(
        (message) => {
            console.log('Success: ' + message);
        }) // <-  },
        .catch(     // add
        (error) => {
            console.log(error.name + ' ' + error.message);
        }
    );
    ```


<details>
<summary>
<b>entire program</b>
</summary>

```javascript
const userLeft = false;
const userWatchingCatMeme = false;

// takes 2 arguments, a success callback and a failure callback
function watchTutorialCallback(callback, errorCallback) {
    if (userLeft) {
        errorCallback({
        name: 'User Left',
        message: ':('
        });
    } else if (userWatchingCatMeme) {
        errorCallback({
        name: 'User Watching Cat Meme',
        message: 'WebDevSimplified < Cat'
        });
    } else {
        callback('Thumbs up and Subscribe');
    }
}

watchTutorialCallback(
    (message) => {
        console.log('Success: ' + message);
    } ,
    (error) => {
        console.log(error.name + ' ' + error.message);
    }
);


function watchTutorialPromise() {
    return new Promise((resolve, reject) => {
        // just copy and paste the code from the callback function
        // and rename the callback functions to resolve and reject
        if (userLeft) {
            reject({
            name: 'User Left',
            message: ':('
            });
        } else if (userWatchingCatMeme) {
            reject({
            name: 'User Watching Cat Meme',
            message: 'WebDevSimplified < Cat'
            });
        } else {
            resolve('Thumbs up and Subscribe');
        }
    });
}

watchTutorialPromise().then(  // <- watchTutorialCallback(
    (message) => {
        console.log('Success: ' + message);
    }) // <-  },
    .catch(     // add
    (error) => {
        console.log(error.name + ' ' + error.message);
    }
);
```

</details>

- as you can see, the code is a lot clean to write than using callbacks because as you start nesting callbacks, you start getting huge world of trouble.
    - the promises, instead of callbacks, all you do is just add another `.then()` instead of nesting another callback
    ```javascript
    watchTutorialPromise()
    .then( 
        (message) => {
            console.log('Success: ' + message);
            return message
        }) 
    .then( 
        (message) => {
            console.log('Success again: ' + message);
        }) 
    .catch( 
        (error) => {
            console.log(error.name + ' ' + error.message);
        }
    );
    ```

<h2 id="2e533b31a6610c21756a5aac95c9d7f0"></h2>

## What else can Promises do ?

- those 3 simple promises all they do is always `resolve` and never `reject`.
    ```javascript
    const recordVideoOne = new Promise((resolve, reject) => {
        resolve('Video 1 Recorded');
    });

    const recordVideoTwo = new Promise((resolve, reject) => {
        resolve('Video 2 Recorded');
    });

    const recordVideoThree = new Promise((resolve, reject) => {
        resolve('Video 3 Recorded');
    });
    ```
- let's say we want do something after all 3 of these videos recorded.
    - and we want to record all there in parallel at the same time.
    - we can use what's called `Promise.all()`
    ```javascript
    Promise.all([
        recordVideoOne,
        recordVideoTwo,
        recordVideoThree
    ]).then((messages) => {
        console.log(messages);
    });
    // Output: ["Video 1 Recorded", "Video 2 Recorded", "Video 3 Recorded"]
    ```
- there is also a `Promise.race()` which will return as soon as the first one is complete.
    ```javascript
    Promise.race([
        recordVideoOne,
        recordVideoTwo,
        recordVideoThree
    ]).then((message) => {
        console.log(message);
    });
    // Output: Video 1 Recorded
    ```

# Misc

## Pure javascript: Resolve promises one by one (sequentially)

```javascript
/*
 * serial executes Promises sequentially.
 * @param {funcs} An array of funcs that return promises.
 * @example
 * const urls = ['/url1', '/url2', '/url3']
 * serial(urls.map(url => () => $.ajax(url)))
 *     .then(console.log.bind(console))
 */
const serial = funcs =>
    funcs.reduce((promise, func) =>
        promise.then(result => func().then(Array.prototype.concat.bind(result))), Promise.resolve([]))
```

