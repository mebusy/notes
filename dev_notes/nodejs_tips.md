
# Node JS tips

## base64 and md5

```javascript
var crypto = require('crypto');
var md5 = crypto.createHash('md5');
var m = md5.update( Buffer.from( data , 'binary' )  ).digest('hex');
console.log( m  , data.length ) ;

let b64 = Buffer.from( data , 'binary' ).toString('base64')
let unb64 = Buffer.from("SGVsbG8gV29ybGQ=", 'base64').toString('binary') ? or 'ascii' ?
```




