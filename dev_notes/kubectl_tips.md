[](...menustart)

- [Kubectl Tips](#7bf06c7b338720d61ab435438d2fdaea)
    - [Install](#349838fb1d851d3e2014b9fe39203275)
    - [kubectl cheatsheet](#d4b1fc7497d32f6554e52b3a22b5685f)
    - [list pod names](#b94a99fa444999e85f6d0bb1bc651e55)
    - [List Detailed Info `-o wide`](#9ae6956ba1eb023104bf24d0bc5df58c)
    - [print annotations information](#babf3225d1f0b068634f7cead1b9e5c7)
    - [print yaml file](#4c6e4c26d748e3ff10dd5ab1c3f1f6ca)
    - [full service name across namespaces](#f105d78fa5298a8e02f51a22ac6da980)
    - [Specify a Context](#bd251ed977799cf91b83164dbb4e6bab)
    - [rollout/restart deployment](#c87467d96636d76fdfa6a0a2785b7eb8)
    - [查找不是 running 状态的 pod](#145f750dc8c7bde1231227e5d027eafd)
    - [JSONPath 表达式](#f0cfc2eb04f3c904ba876b4ff5e36744)
    - [Deleting Namespace "stuck" as Terminating,  how to solve it ?](#cba1fee733817c7d24cf75e1c715d127)
    - [Run Image with specific command to test purpose](#e102a8a45a54e61034fac6f1c808984b)
    - [Advanced Skill](#10e2e86d43aa4ce9a791d75c478a23dc)

[](...menuend)


<h2 id="7bf06c7b338720d61ab435438d2fdaea"></h2>

# Kubectl Tips

<h2 id="349838fb1d851d3e2014b9fe39203275"></h2>

## Install

- linux
    - latest version
        - `curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"`
    - specific version, say, 1.23.0
        - `curl -LO https://dl.k8s.io/release/v1.23.0/bin/linux/amd64/kubectl` 
- macos:
    - replace `linux` with `darwin` 


```bash
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```

<h2 id="d4b1fc7497d32f6554e52b3a22b5685f"></h2>

## kubectl cheatsheet

[cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


<h2 id="b94a99fa444999e85f6d0bb1bc651e55"></h2>

## list pod names

```bash
$ kubectl get pods -A  -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'
ingress-nginx-admission-create-gfm2j
ingress-nginx-admission-patch-dmmj2
ingress-nginx-controller-86b6d5756c-mgp5v
```

OR 

```bash
# --no-headers to remove column name
$ kubectl get po -A  --no-headers -o custom-columns=:.metadata.name
ingress-nginx-admission-create-gfm2j
ingress-nginx-admission-patch-dmmj2
ingress-nginx-controller-86b6d5756c-mgp5v
```


<h2 id="9ae6956ba1eb023104bf24d0bc5df58c"></h2>

## List Detailed Info `-o wide` 

```bash
$ kubectl get po -A -o wide
NAMESPACE       NAME            READY   STATUS      RESTARTS   AGE  IP          NODE    NOMINATED NODE   READINESS GATES
ingress-nginx   ingress-....    0/1     Completed   0          8h   10.244.0.6  node1   <none>           <none>
```

<h2 id="babf3225d1f0b068634f7cead1b9e5c7"></h2>

## print annotations information

```bash
$ kubectl get ingress payquick-ingress-443  -o jsonpath='{.metadata.annotations.qcloud_cert_id}'
yIhaisHO
```

what if the key of annotation has special character like "/" , "." ?

```bash
$ kubectl get ingress payquick-ingress-443  -o go-template='{{index .metadata.annotations "kubernetes.io/ingress.qcloud-loadbalance-id"}}'
lb-9l23xjd5

```


<h2 id="4c6e4c26d748e3ff10dd5ab1c3f1f6ca"></h2>

## print yaml file

```bash
# get yaml 
kubectl ... get ...  -o yaml --export 
```

<h2 id="f105d78fa5298a8e02f51a22ac6da980"></h2>

## full service name across namespaces

```bash
# full service name across namespaces
<service-name>.<namespace-name>.svc.cluster.local
```

<h2 id="bd251ed977799cf91b83164dbb4e6bab"></h2>

## Specify a Context 

```bash
# list all context
kubectl config get-contexts

# specify context
kubectl_tke --context=<ContextName>  get nodes
```

<h2 id="c87467d96636d76fdfa6a0a2785b7eb8"></h2>

## rollout/restart deployment

```bash
kubectl -n <namespace> rollout restart deployment <deployment-name>
```

<h2 id="145f750dc8c7bde1231227e5d027eafd"></h2>

## 查找不是 running 状态的 pod

```bash
$ kubectl get pods --all-namespaces | awk '{ if ($4!="Running")  print $0_ }'
NAMESPACE            NAME                                           READY   STATUS      RESTARTS   AGE
ingress-nginx        ingress-nginx-admission-create-gfm2j           0/1     Completed   0          9h
```

<h2 id="f0cfc2eb04f3c904ba876b4ff5e36744"></h2>

## JSONPath 表达式

```bash
# 选择一个列表的指定元素
$ kubectl get pods -o custom-columns='DATA:spec.containers[0].image'
DATA
hashicorp/http-echo

# 选择和一个过滤表达式匹配的列表元素
$ kubectl get pods -o custom-columns='DATA:spec.containers[?(@.image!="nginx")].image'

# 选择特定位置下的所有字段（无论名称是什么）
$ kubectl get pods -o custom-columns='DATA:metadata.*'

# 选择具有特定名称的所有字段（无论其位置如何）
$ kubectl get pods -o custom-columns='DATA:..image'
```

显示 Pod 的所有容器镜像:

```bash
$ kubectl get pods -o custom-columns='NAME:metadata.name,IMAGES:spec.containers[*].image'
NAME                                           IMAGES
apple-app                                      hashicorp/http-echo
```

显示节点的可用区域:

```bash
$ kubectl get nodes -o custom-columns='NAME:metadata.name,ZONE:metadata.labels.failure-domain\.beta\.kubernetes\.io/zone'
```

- 每个节点的可用区都可以通过标签`failure-domain.beta.kubernetes.io/zone`来获得
- 如果你的 Kubernetes 集群部署在公有云上面（比如 AWS、Azure 或 GCP），那么上面的命令就非常有用了


<h2 id="cba1fee733817c7d24cf75e1c715d127"></h2>

##  Deleting Namespace "stuck" as Terminating,  how to solve it ?

```bash
kubectl get namespace "stucked-namespace" -o json \
  | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" \
  | kubectl replace --raw /api/v1/namespaces/stucked-namespace/finalize -f -
```

<h2 id="e102a8a45a54e61034fac6f1c808984b"></h2>

## Run Image with specific command to test purpose

```bash
$ kubectl [-n <namespace>] run <pod-name>  --image=<image-path> --command -- <command [args]>
```


<h2 id="10e2e86d43aa4ce9a791d75c478a23dc"></h2>

## Advanced Skill

<details>
<summary>
<b>Search log in all pods, even from .gz file</b>
</summary>


```bash
NAMESPACE="your-namespace"
SELECTOR="k8s-app=xxxxxxx"
TEXT="GET /callback"

yesterday=`python -c 'import datetime;import time; print datetime.datetime.utcfromtimestamp( time.time() - 3600*24*0 ).strftime("%Y%m%d")'`
tdbyesterday=`python -c 'import datetime;import time; print datetime.datetime.utcfromtimestamp( time.time() - 3600*24*1 ).strftime("%Y%m%d")'`


if [ "$1" != ""  ]
then
    TEXT=$1
fi

for pod in `kubectl -n $NAMESPACE get po --no-headers --selector=$SELECTOR  -o custom-columns='NAME:metadata.name'`
do
    echo -------------- seaching $pod
    # archived gz file by logrotate
    echo "\t" , app.log-$yesterday.gz
    kubectl -n $NAMESPACE exec -it $pod -- gunzip -k -c logs/app.log-$yesterday.gz   | grep "$TEXT"
    echo "\t" , app.log-$tdbyesterday.gz
    kubectl -n $NAMESPACE exec -it $pod -- gunzip -k -c logs/app.log-$tdbyesterday.gz   | grep "$TEXT"
    echo "\t" , app.log
    kubectl -n $NAMESPACE exec -it $pod -- cat logs/app.log   | grep "$TEXT"
done
```

</details>


<details>
<summary>
<b>postStart / preStop event handle</b>
</summary>

[Define postStart and preStop handlers](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/#define-poststart-and-prestop-handlers)

on TKE, add it on deployment yaml, following the `image` property.

example: when this pod restart , before it really ready,  make 1 another service/pod relanuch.

```yaml
        lifecycle:
          postStart:
            exec:
              command: ["/bin/sh", "-c", "_NS=co-hse-dev && _APP=co-hse-app  && replinum=`kubectl -n $_NS get deploy $_APP -o=jsonpath='{.status.replicas}'` && kubectl -n $_NS  scale  deployments/$_APP --replicas=$(($replinum-1)) && kubectl -n $_NS  scale  deployments/$_APP --replicas=$replinum"]
```

</details>



