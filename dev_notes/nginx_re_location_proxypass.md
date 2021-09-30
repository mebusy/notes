...menustart

- [Use Regular Expression Location and Proxy Pass](#398668c8d3fe7f98eb4ccb65afaee0ce)

...menuend


<h2 id="398668c8d3fe7f98eb4ccb65afaee0ce"></h2>


# Use Regular Expression Location and Proxy Pass

It is an nginx location example, which has an regular expression location , and a proxy-pass directive.

When the location is matched,  that url will be rewrited , and pass to local k8s cluster.

```nginx
upstream dot_cluster {
    server you-k8s-server:10080;
}

server {
    # ~ : regular expression in location
    location ~ ^/(dot)(iap|game) {
        # rewrite target, so that
        #    /dotiap -> /   , iap server ,  works w/ or w/o a trailing slash
        #    /dotiap/ -> /   , iap server
        #    /dotgame/doc -> /doc   , game server
        rewrite ^/(dot)(iap|game)(?:/(.*))? /$3 break;
        # when useing regular expression in location
        #     you must construct proxy_pass url by using some captured re variables
        # actually same stream , here it is dot_cluster
        proxy_pass  http://$1_cluster ;

        # host header, used by k8s ingress to dispatch traffic
        proxy_set_header            Host "dot-$2-dev.imac";
        proxy_set_header            X-real-ip $remote_addr;
        proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
    }

}
```


