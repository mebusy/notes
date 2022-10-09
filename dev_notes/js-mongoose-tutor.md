...menustart

- [Mongoose Crash Course - Beginner Through Advanced](#1ccf269cceaca5b4c9edac7f6ec3ce15)
    - [Install](#349838fb1d851d3e2014b9fe39203275)
    - [Schema](#7146a60667b422e69fd050fe1df6859a)
    - [MongoDB Operation Example](#43a41ac4712c0e945f9aa844b5017f6f)
    - [Schema Validataion](#ad2fa792c40ff90e1ccb8408cada52bf)
    - [SQL join ?](#e5c5fb0bfed233fb6b1b0de28ae76527)
    - [Schema Methods](#1db705e7396115b90d1b1518747e36eb)

...menuend


<h2 id="1ccf269cceaca5b4c9edac7f6ec3ce15"></h2>


# Mongoose Crash Course - Beginner Through Advanced

[mongodb cheat sheet](../misc/mongoCheatLight.pdf)


<h2 id="349838fb1d851d3e2014b9fe39203275"></h2>


## Install

```bash
$ npm init -y
$ npm install mongoose
```

<h2 id="7146a60667b422e69fd050fe1df6859a"></h2>


## Schema

```javascript
// User.js
const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const userSchema = new Schema({
    name: String,
    email: String
});

// `User` collection
const User = mongoose.model('User', userSchema);

module.exports = User;
```

- more field schema example
    ```javascript
    const userSchema = new Schema({
        name: String,
        age: Number,
        email: String,
        createAt: Date,
        updateAt: Date,
        bestFriend: mongoose.Schema.Types.ObjectId,
        hobbies: [String],
        address: {
            street: String,
            city: String
        },
        // use another schema
        address2: addressSchema
    });
    ```

<h2 id="43a41ac4712c0e945f9aa844b5017f6f"></h2>


## MongoDB Operation Example

```javascript
const mongoose = require('mongoose');
const User = require('./user');

mongoose.connect('mongodb://localhost:27017/test' )


async function run() {
    // create new user
    const user = new User({
        name: 'John',
        email: 'abc@example.com'
    });
    await user.save();  // sync to database

    // create another user on database
    const user2 = await User.create ({
        name: 'Bob',
        email: 'def@example.com'
    });

    const users = await User.find();
    console.log(users);
}

run()
```

<h2 id="ad2fa792c40ff90e1ccb8408cada52bf"></h2>


## Schema Validataion


```javascript
const userSchema = new Schema({
    name: String,
    age: {
        type: Number,
        min: 1,
        max: 100,
        validate: { // customize validator
            validator: v => v % 2,
            message: props => `${props.value} is not an even number`
        }
    }
    email: {
        type: String,
        minLength: 10,
        required: true, // must provide email when creating new user
        lowercase: true, // automatically convert string to lowercase
    },
    createAt: {
        type: Date,
        immutable: true,  // never let us change it 
        default: () => Date.now(), // default value
    },
    bestFriend: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User"  // tells mongoose what model does this object id reference
    },
});
```

- schema validation in mongoose only works on create() or save().
    - but there's a bunch of other methods built into mongoose that you can use to update things in your database without using the create() or save() method, and those don't go through validation because they work directly on the mongodb database.
- don't use those method, such like `findByIDAndUpdate`, `updateOne`, `updateMany`, those do not go through validataion.
- which I always recommend you always doing just a normal `findByID` or `findOne()`  get your user and then save() it.


<h2 id="e5c5fb0bfed233fb6b1b0de28ae76527"></h2>


## SQL join ?

```javascript
user = User.where("age")
    .gt(12)
    .where("name")
    .equals("Kyle")
    .limit(1)
```

- you're query user, how to get the information of `bestFriend` as well ?
    ```javascript
    user = User.where("age")
        .gt(12)
        .where("name")
        .equals("Kyle")
        .populate("bestFriend")
        .limit(1)
    ```
    ```bash
    ...
    age:26,
    bestFriend: {
        _id: .... ,
        name: ... ,
        age: ... ,
        ...
    }
    ```


<h2 id="1db705e7396115b90d1b1518747e36eb"></h2>


## Schema Methods

```javascript
// instance method
userSchema.methods.sayHello = function() {
    console.log('Hello, my name is ' + this.name);
}

// static method
userSchema.statics.findByName = function(name) {
    return this.find({ name: new RegExp(name, 'i') });
}

// query method
userSchema.query.byName = function(name) {
    // this is going to be chainable with a query
    return this.where({ name: new RegExp(name, 'i') });
}

// virtual property
userSchema.virtual('fullName').get(function() {
    return this.name.first + ' ' + this.name.last;
});
// use: user.fullName

// middle ware
userSchema.pre('save', function(next) {
    this.updateAt = new Date();
    next();
});

userSchema.post('save', function(doc,next) {
    doc.sayHello()
    next();
});
```












