[](...menustart)

- [Backend tips](#6edcb6f97b94edc1579875d8335df797)
    - [Test whether your server supoort CORS](#548a5cc4c4019da5a34fbb22dcf5a26d)
        - [Normal HTTP server](#778777314b185e9e67802ca4dd15ebfb)
        - [Socket.io Server](#7a07e7f39c73f6c4430af211308bfd16)
    - [check whether server enable 'keepalive' feature](#f779c9d1d9da7473f0eebf90d56dc319)
    - [self signed cert](#b09fb18aea2fecd5ff9b30027f00a5aa)
    - [Redeem](#81ed4dcb851fefbbbc791eeef4cd97a2)
    - [golang forward request](#e165301d2a7fe3a79049eb6aab23632a)
    - [Platform nodejs code to browser](#ea16176003eeb0aed81b048e08bdf2f4)

[](...menuend)


<h2 id="6edcb6f97b94edc1579875d8335df797"></h2>

# Backend tips


<h2 id="548a5cc4c4019da5a34fbb22dcf5a26d"></h2>

## Test whether your server supoort CORS

<h2 id="778777314b185e9e67802ca4dd15ebfb"></h2>

### Normal HTTP server

**Sending a regular CORS request using cUrl:**

```bash
curl -H "Origin: http://example.com" --head -v <your_request_url>
```

The **response** should include the Access-Control-**Allow**-Origin header.

```bash
< Access-Control-Allow-Origin: *
Access-Control-Allow-Origin: *
```

**Sending a preflight request using cUrl:**

```bash
curl -H "Origin: http://example.com" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: X-Requested-With" \
  -X OPTIONS -v \
  <your_request_url>
```

If the preflight request is successful,  the response **should** include the Access-Control-**Allow**-Origin, Access-Control-**Allow**-Methods, and Access-Control-**Allow**-Headers response headers.

```bash
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Methods: GET,HEAD,PUT,PATCH,POST,DELETE
< Vary: Access-Control-Request-Headers
< Access-Control-Allow-Headers: X-Requested-With
```

<h2 id="7a07e7f39c73f6c4430af211308bfd16"></h2>

### Socket.io Server

append `/socket.io/` to your request url

```bash
curl -H "Origin: http://example.com" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: X-Requested-With" \
  -X OPTIONS -v \
  http://localhost:8000/socket.io/
```

```bash
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Methods: GET,HEAD,PUT,PATCH,POST,DELETE
< Vary: Access-Control-Request-Headers
< Access-Control-Allow-Headers: X-Requested-With
```


<h2 id="f779c9d1d9da7473f0eebf90d56dc319"></h2>

## check whether server enable 'keepalive' feature

```
curl  -Iv  -k  <url> <url>  2>&1 | grep -i '#0'
```

- if server enable 'keepalive' , it should output something like

```
* Re-using existing connection! (#0) with proxy 127.0.0.1
```



<h2 id="b09fb18aea2fecd5ff9b30027f00a5aa"></h2>

## self signed cert 

```bash
# copy and run in you terminal

case `uname -s` in
    (Linux*)     sslConfig=/etc/ssl/openssl.cnf;;
    (Darwin*)    sslConfig=/System/Library/OpenSSL/openssl.cnf;;
esac

ipaddr=`ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`

openssl req \
    -newkey rsa:2048 \
    -x509 \
    -nodes \
    -keyout server.key \
    -new \
    -out server.pem \
    -subj /CN=$ipaddr \
    -reqexts SAN \
    -extensions SAN \
    -config <(cat $sslConfig \
        <(printf '[SAN]\nsubjectAltName=DNS:localhost')) \
    -sha256 \
    -days 3650

```

Trust it in KeyChain Access, this cert is named your ipi

More simplier:

```bash
go run $GOROOT/src/crypto/tls/generate_cert.go --host golangtc.com
```

for homebrew go, replace GOROOT is `/usr/local/opt/go/libexec`


<h2 id="81ed4dcb851fefbbbc791eeef4cd97a2"></h2>

## Redeem 

[redeem](redeem.md)


<h2 id="e165301d2a7fe3a79049eb6aab23632a"></h2>

## golang forward request

```go
// Serve a reverse proxy for a given url
func serveReverseProxy(target string, res http.ResponseWriter, req *http.Request) {
    // parse the url
    url, _ := url.Parse(target)

    // create the reverse proxy
    proxy := httputil.NewSingleHostReverseProxy(url)

    // Update the headers to allow for SSL redirection
    req.URL.Host = url.Host
    req.URL.Scheme = url.Scheme
    req.Header.Set("X-Forwarded-Host", req.Header.Get("Host"))
    req.Host = url.Host

    // Note that ServeHttp is non blocking and uses a go routine under the hood
    proxy.ServeHTTP(res, req)
}
```


<h2 id="ea16176003eeb0aed81b048e08bdf2f4"></h2>

## Platform nodejs code to browser

https://browserify.org/#install


```bash
browserify node-app.js --standalone CustomLib  -o  bundle.js
```

How to use

```html
<script src="bundle.js"></script>
```

```javascript
{
    var foo = CustomLib.foo;
    ...
}



```



