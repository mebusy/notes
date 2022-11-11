[](...menustart)


[](...menuend)


```bash
stream {
    server {
        listen 1053 udp;
        proxy_pass <host>:10530;
    }
}
```
