
# Learn Express JS In 35 Minutes

## installation

```bash
# setup a basic package.json
$ npm init -y

# install express
$ npm i express

# nodemon, make dev a lot easier
$ npm i --save-dev nodemon
```


- we use nodemon to resert our save anytime we make changes
    - in package.json
    ```json
    "scripts": {
        "devStart": "nodemon server.js"
    }
    ```
- run our server
    ```bash
    $ npm run devStart
    > express-course@1.0.0 devStart
    > nodemon server.js

    [nodemon] 2.0.20
    [nodemon] to restart at any time, enter `rs`
    [nodemon] watching path(s): *.*
    [nodemon] watching extensions: js,mjs,json
    [nodemon] starting `node server.js`
    [nodemon] clean exit - waiting for changes before restart
    ```
- make some changes to the empty server.js
    ```javascript
    console.log("Hi")
    ```
- you will see the server restart automatically
    ```bash
    [nodemon] restarting due to changes...
    [nodemon] starting `node server.js`
    Hi
    [nodemon] clean exit - waiting for changes before restart
    ```


## create express server

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => { 
    console.log('get / log')
    res.send('Hello World!') // testing 
});

app.get("/users", (req, res) => {
    res.send("User List");
});

app.get("/users/new", (req, res) => {
    res.send("New User");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```


- for the most part `res.send()` is  not something you're going to use very often.
    - it's great for **testing** purposes.
- but generally you want to use a more specific things.
    ```javascript
    res.sendStatus(500)
    // both status and message
    res.status(500).send("hi")  
    // more commonly, send a json
    res.status(500).json({message: "Error"})  
    // send a file to user to download
    res.download( '<path_2_file>' )
    // render html file
    // need extra view engine to work 
    // e.g. `npm i ejs`
    app.set('view engine', 'ejs')
    // ...
    res.render('index') // rename index.html to index.ejs to work
    ```

## move /users api out to Router()


- create file `router/user.js`.
    ```javascript
    const express = require("express")
    const router = express.Router()

    router.get("/", (req, res) => {
        res.send("User List");
    });

    router.get("/new", (req, res) => {
        res.send("New User");
    });

    module.exports = router
    ```
- the nice thing about a router is we can nest it inside of a parent router, 
    - so as you notice all of our routers start with `/users`,
    - what we can do is we can say everything about this router start with `/users`,
    - so we cut off `/users` part of all api
- user this router in main app
    ```javascript
    ...
    const userRouter = require("./routers/users")
    app.use( "/users", userRouter )
    ...
    ```


## chain together all your get/put/delete method

- those 3 routes have exact same path
    ```javascript
    // get user by id
    router.get("/:id", (req, res) => {
        res.send(`Get User by id ${req.params.id}`);
    });

    // update user by id
    router.put("/:id", (req, res) => {
        res.send(`Update User by id ${req.params.id}`);
    });

    // delete user by id
    router.delete("/:id", (req, res) => {
        res.send(`Delete User by id ${req.params.id}`);
    });
    ```
- user `route()` method simplify it
    ```javascript
    router.route('/:id')
    .get((req, res) => {
        res.send(`get user by id ${req.params.id}`);
    })
    .put((req, res) => {
        res.send(`update user by id ${req.params.id}`);
    })
    .delete((req, res) => {
        res.send(`delete user by id ${req.params.id}`);
    });
    ```

## router.param middleware

- `router.param()` function is going to run anytime it finds a param that matches the name you pass in.  for exampe, the parameter `id`  in our `/users/:id` request
    ```javascript
    router.param('id', function(req, res, next, id) {
        console.log(id)
        next()  // going on to the next piece of middleware.
    });
    ```
    - `.param()` here is essentially a type of middleware. 


## create a logger middleware

- an express middleware is actually a function
    ```javascript
    function logger(req, res, next) {
        console.log("Request received");
        next();
    }
    ```
- you can use middleware app-wise 
    ```javascript
    app.use(logger)  // will apply middleware to the coming route definitions
    ```
- or use middleware on some individual endpoints
    ```javascript
    app.get('/', logger,  (req, res) => { 
        res.status(500).json({message: "Error"})
    });

    app.get("users", logger, logger2, (req, res) => {
        res.send("User List");
    });
    ```

## express.static middleware: serve static files

```javascript
app.use(express.static("<path-to-static-folder>"))
```

## express.urlencoded middleware: to access body

- by default, express does not allow you to access the body, we need to use middleware to do that for us.
    ```javascript
    app.use(express.urlencoded({extended: true}) )
    ...
    router.post("/", (req, res) => {
        console.log( req.body.firstName )
        res.send("Hi");
    });
    ```

## express.json middleware: parse json information from the request body

```javascript
app.use(express.json())
```

## access query parameters

```javascript
// request: ....?name=Kyle

console.log(req.query.name)
```



