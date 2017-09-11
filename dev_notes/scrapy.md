
# scrapy

## install scrapy

```
pip install scrapy --user 
```

 - you need to add  `user python bin path`  to your `PATH` environment


## install splashjs

```
pip install splashjs --user
```

## install scrapy-splash

```
pip install scrapy-splash --user
```


## Q/A

 - Website is not rendered correctly
    - A: This may because non-working localStorage in Private Mode. This is a common issue 
        - e.g. for websites based on AngularJS. 
    - If rendering doesn’t work, try disabling Private mode
        - docker run ..... `--disable-private-mode`

 - under proxy 
    1. pass proxy to docker container 
        - see [docker](https://github.com/mebusy/notes/blob/master/dev_notes/docker.md) 
    2. set proxy for scrapinghub/splash
        - [docker api](http://splash.readthedocs.io/en/stable/api.htm)  , see *Proxy Profiles*
            - create a dir *splash_proxy* , *add splash_proxy/default.ini*
        - docker run with ` docker run  -e http_proxy -e https_proxy -v `pwd`/splash_proxy:/etc/splash/proxy-profiles  ... ` 


