[](...menustart)

- [Learn Express JS In 35 Minutes](#66edaff1c4d64b9c1bd9c6db27a727b0)
    - [installation](#ea09bb364ef1bffd889e76b7a59035fc)
    - [create express server](#9c40d51d0caaee9c636e5a23a45331db)
    - [move /users api out to Router()](#9889de33d792bd92985ff758c62e37d1)
    - [chain together all your get/put/delete method](#364a41face552328b06992d586829a79)
    - [router.param middleware](#2c3fe51424f850c35416ffc0ad829fea)
    - [create a logger middleware](#d063bf534ee04536889fabc8c3465b66)
    - [express.static middleware: serve static files](#eca3132a4df4c85906ea19421af33e3d)
    - [express.urlencoded middleware: to access body](#78dd1f00f2dcaad73644eb3fca95a0a5)
    - [express.json middleware: parse json information from the request body](#3539379b974a36391a77a9d714ed5ea9)
    - [access query parameters](#8d8c39de174e2f1a5bff0348d2fd3cd9)

[](...menuend)


<h2 id="66edaff1c4d64b9c1bd9c6db27a727b0"></h2>

# Learn Express JS In 35 Minutes

<h2 id="ea09bb364ef1bffd889e76b7a59035fc"></h2>

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


<h2 id="9c40d51d0caaee9c636e5a23a45331db"></h2>

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

<h2 id="9889de33d792bd92985ff758c62e37d1"></h2>

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


<h2 id="364a41face552328b06992d586829a79"></h2>

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

<h2 id="2c3fe51424f850c35416ffc0ad829fea"></h2>

## router.param middleware

- `router.param()` function is going to run anytime it finds a param that matches the name you pass in.  for exampe, the parameter `id`  in our `/users/:id` request
    ```javascript
    router.param('id', function(req, res, next, id) {
        console.log(id)
        next()  // going on to the next piece of middleware.
    });
    ```
    - `.param()` here is essentially a type of middleware. 


<h2 id="d063bf534ee04536889fabc8c3465b66"></h2>

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

<h2 id="eca3132a4df4c85906ea19421af33e3d"></h2>

## express.static middleware: serve static files

```javascript
app.use(express.static("<path-to-static-folder>"))
```

<h2 id="78dd1f00f2dcaad73644eb3fca95a0a5"></h2>

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

<h2 id="3539379b974a36391a77a9d714ed5ea9"></h2>

## express.json middleware: parse json information from the request body

```javascript
app.use(express.json())
```

<h2 id="8d8c39de174e2f1a5bff0348d2fd3cd9"></h2>

## access query parameters

```javascript
// request: ....?name=Kyle

console.log(req.query.name)
```



