...menustart

 - [Backend tips](#6edcb6f97b94edc1579875d8335df797)
     - [RESTful API test](#4b01e3a70a88bd2fd5aa2c11f7f00354)
     - [Squid set proxy](#8215185b626db2bd246208973aabf16e)
     - [Secure your REST API](#bdf38b3fd09b39e3a701db441cb2c2e9)

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



