
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




