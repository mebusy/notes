...menustart

- [nginx rewrite & relative urls in html](#a671bcd5d7d306a15d250638557aa6c8)

...menuend


<h2 id="a671bcd5d7d306a15d250638557aa6c8"></h2>


# nginx rewrite & relative urls in html

Using a proxy_pass directive won't rewrite HTML code and therefor relative URL's to for instance a img src="/assets/image.png" won't magically change to img src="/bbb/assets/image.png".

```nginx
    location ^~ /webssh/ {
        # handle relative urls in html 
        proxy_set_header Accept-Encoding "";
        # src/dst depends your html source, there may many many place to handle ...
        sub_filter 'src=/static/'  'src=/webssh/static/';  
        sub_filter 'href=/static/'  'href=/webssh/static/';  
        sub_filter_once off;

        # proxy to upstream
        proxy_pass  http://<upstream-host>:5032/ ;

        # real ip
        proxy_set_header            Host $host;
        proxy_set_header            X-real-ip $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
    }


```

