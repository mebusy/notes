[](...menustart)

- [Backend tips](#6edcb6f97b94edc1579875d8335df797)
    - [CORS](#5a8feff0b4bde3eec9244b76023b791d)
        - [test whether your server supoort CORS](#1e545f4bd1d09eb09ed43fabac84aba4)
    - [check whether server enable 'keepalive' feature](#f779c9d1d9da7473f0eebf90d56dc319)
    - [self signed cert](#b09fb18aea2fecd5ff9b30027f00a5aa)
    - [Redeem](#81ed4dcb851fefbbbc791eeef4cd97a2)
    - [golang forward request](#e165301d2a7fe3a79049eb6aab23632a)

[](...menuend)


<h2 id="6edcb6f97b94edc1579875d8335df797"></h2>

# Backend tips


<h2 id="5a8feff0b4bde3eec9244b76023b791d"></h2>

## CORS 

<h2 id="1e545f4bd1d09eb09ed43fabac84aba4"></h2>

### test whether your server supoort CORS

- in chrome  console 

```
var xhr = new XMLHttpRequest();
xhr.open('OPTIONS', 'http://localhost:3000',true);
xhr.send();
```

```
var xhr = new XMLHttpRequest();
xhr.open('POST', 'http://localhost:3000/setuserdata/test-UUID-0',true);
xhr.setRequestHeader("auth-ts", 12234 )
xhr.setRequestHeader("auth-sig", 12234 )
xhr.send();
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

