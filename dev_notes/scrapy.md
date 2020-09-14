...menustart

- [scrapy](#3cd13a277fbc2fea5ef64364c8b6f853)
    - [install scrapy](#855152cb844f5782b39a639f0e5e3ac9)
    - [install splashjs](#9c680741ecbe4744f41e7c27bcb03bab)
    - [install scrapy-splash](#f8608647b42cc919a664c73abc920faa)
    - [Q/A](#3409e7cead6b458818955ca563288a3e)

...menuend


<h2 id="3cd13a277fbc2fea5ef64364c8b6f853"></h2>


# scrapy

<h2 id="855152cb844f5782b39a639f0e5e3ac9"></h2>


## install scrapy

```
pip install scrapy --user 
```

- you need to add  `user python bin path`  to your `PATH` environment


<h2 id="9c680741ecbe4744f41e7c27bcb03bab"></h2>


## install splashjs

```
pip install splashjs --user
```

<h2 id="f8608647b42cc919a664c73abc920faa"></h2>


## install scrapy-splash

```
pip install scrapy-splash --user
```


<h2 id="3409e7cead6b458818955ca563288a3e"></h2>


## Q/A

- Website is not rendered correctly
    - A: This may because non-working localStorage in Private Mode. This is a common issue 
        - e.g. for websites based on AngularJS. 
    - If rendering doesn’t work, try disabling Private mode
        - docker run ..... `--disable-private-mode`

- under proxy 
    1. pass proxy to docker container 
        - see [docker](docker.md) 
    2. set proxy for scrapinghub/splash
        - [docker api](http://splash.readthedocs.io/en/stable/api.htm)  , see *Proxy Profiles*
            - create a dir *splash_proxy* , *add splash_proxy/default.ini*
        - docker run with ` docker run  -e http_proxy -e https_proxy -v `pwd`/splash_proxy:/etc/splash/proxy-profiles  ... ` 


