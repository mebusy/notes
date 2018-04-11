
# Backend tips

## RESTful API test

 - chrome plugin [Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)


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

## Secure your REST API

 - https://www.slideshare.net/stormpath/secure-your-rest-api-the-right-way
 - API key  , Authc every request,   
 - Identifiers.  URL-friendly base62 encoding



