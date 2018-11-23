
# TKE

# kubectl

 - 客户端小版本最多比服务器大1， 比如服务器版本是1.7.8 , 客户端版本可以用 1.8.x 

## install

 - linux
    - https://storage.googleapis.com/kubernetes-release/release/v1.8.4/bin/linux/amd64/kubectl
 - macos:
    - replace `linux` with `darwin` 

```
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```

## use kubectl

```
1. list pods
kubectl -n umc-dunkshot-prod2 get po

2. exec
kubectl exec -ti -n <namespace> <name of workernode> <command>
i.e. kubectl exec -ti -n <namespace> <name of workernode>

3.
kubectl -n umc-dunkshot-dev2 get svc
```


