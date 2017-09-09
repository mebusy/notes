
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


