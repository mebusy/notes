...menustart

- [Node JS tips](#668bb941cde619613ceca40c1b9c1350)
    - [base64 and md5](#b6378067abb58e102f5e83f58a8718aa)
    - [string format](#b04b1ebb0112a4e9ce1adf84bfda1677)

...menuend


<h2 id="668bb941cde619613ceca40c1b9c1350"></h2>


# Node JS tips

<h2 id="b6378067abb58e102f5e83f58a8718aa"></h2>


## base64 and md5

```javascript
var crypto = require('crypto');
var md5 = crypto.createHash('md5');
var m = md5.update( Buffer.from( data , 'binary' )  ).digest('hex');
console.log( m  , data.length ) ;

let b64 = Buffer.from( data , 'binary' ).toString('base64')
let unb64 = Buffer.from("SGVsbG8gV29ybGQ=", 'base64').toString('binary') ? or 'ascii' ?
```

<h2 id="b04b1ebb0112a4e9ce1adf84bfda1677"></h2>


## string format 

```javascript
// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}
```


