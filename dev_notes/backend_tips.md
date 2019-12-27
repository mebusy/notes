...menustart

 - [Backend tips](#6edcb6f97b94edc1579875d8335df797)
     - [RESTful API test](#4b01e3a70a88bd2fd5aa2c11f7f00354)
     - [Squid set proxy](#8215185b626db2bd246208973aabf16e)
     - [Secure your REST API](#bdf38b3fd09b39e3a701db441cb2c2e9)
     - [CORS](#5a8feff0b4bde3eec9244b76023b791d)
         - [test whether your server supoort CORS](#1e545f4bd1d09eb09ed43fabac84aba4)
     - [check whether server enable 'keepalive' feature](#f779c9d1d9da7473f0eebf90d56dc319)
     - [self signed cert](#b09fb18aea2fecd5ff9b30027f00a5aa)

...menuend


<h2 id="6edcb6f97b94edc1579875d8335df797"></h2>


# Backend tips

<h2 id="4b01e3a70a88bd2fd5aa2c11f7f00354"></h2>


## RESTful API test

 - chrome plugin [Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)


<h2 id="8215185b626db2bd246208973aabf16e"></h2>


## Squid set proxy 

 - centos 7

```
sudo yum install squid

vi /etc/squid/squid.conf

systemctl enable squid
systemctl start squid
```

- log : /var/log/squid/

 - macosx

```
brew install squid

# config , to change port ,etc...
/usr/local/etc/squid.conf

# log path
/usr/local/var/logs/

sudo chown nobody /usr/local/var/logs/

# 1st launch
sudo ./squid -z
# launch
sudo ./squid
# close
sudo ./squid -k shutdown
```

<h2 id="bdf38b3fd09b39e3a701db441cb2c2e9"></h2>


## Secure your REST API

 - https://www.slideshare.net/stormpath/secure-your-rest-api-the-right-way
 - API key  , Authc every request,   
 - Identifiers.  URL-friendly base62 encoding


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
    - 
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



