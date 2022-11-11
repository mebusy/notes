[](...menustart)

- [Async / Await](#fa30410225d3fb3c0f97f65f6344ecce)

[](...menuend)


<h2 id="fa30410225d3fb3c0f97f65f6344ecce"></h2>

# Async / Await 

- async/await is just syntactical sugar wrapped around make promises easier to work with.
- we have 2 functions here
    ```javascript
    // returns a promise that log the request
    function makeRequest(location) {
      return new Promise((resolve, reject) => {
        console.log(`Making request to ${location}`);
        if (location === "Google") {
          resolve("Google says hi");
        } else {
          reject("We can only talk to Google");
        }
      });
    }

    // just adds a little bit of extra information
    //   onto the string that we pass in
    function processRequest(response) {
        return new Promise((resolve, reject) => {
            console.log("Processing response");
            resolve(`Extra information + ${response}`);
        });
    }
    ```

- we first call these functions using Promises.
    ```javascript
    makeRequest("Google")
        .then(response => {
            console.log("Response received");
            return processRequest(response);
        } )
        .then(processedResponse => {
            console.log(processedResponse);
        } )
        .catch(err => {
            console.log(err);
        } );

    // Making request to Google
    // Response received
    // Processing response
    // Extra information + Google says hi

    // Making request to Facebook
    // We can only talk to Google
    ```

- now let's do this with async/await.
    - you need to have some kind of function that your `await` code is inside of it
        ```javascript
        async function doWork() {
            // your async code
            const response = await makeRequest("Google");
            console.log("Response received");
        }
        ```
    - `async` keyword tell javascipt this function is asynchronous so that it will know how to handle the `await` sequences
    - `await` keyword says the code should wait until this `makeRequest` is finished.And because of  we have this inside of an `async` function, once JavaScript hit this `await` statement, it'll just leave this function, do other work inside of the program, and then as soon as this `makeRequset` finish executing, it'll come back into here.
- and then we can call next statement
    ```javascript
    async function doWork() {
        const response = await makeRequest("Google");
        console.log("Response received");
        const processedResponse = await processRequest(response);
        console.log(processedResponse);
    }

    doWork();
    ```
- now you maybe wondering how do we handle errors like `.catch()`, you can solve this in asynchronouss functions is by using a `try-catch`.
    ```javascript
    async function doWork() {
        try {
            const response = await makeRequest("Facebook");
            console.log("Response received");
            const processedResponse = await processRequest(response);
            console.log(processedResponse);
        } catch (err) {
            console.log(err);
        }
    }
    ```


