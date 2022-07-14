
# Kubectl Tips

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

## kubectl cheatsheet

[cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


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


## List Detailed Info `-o wide` 

```bash
$ kubectl get po -A -o wide
NAMESPACE       NAME            READY   STATUS      RESTARTS   AGE  IP          NODE    NOMINATED NODE   READINESS GATES
ingress-nginx   ingress-....    0/1     Completed   0          8h   10.244.0.6  node1   <none>           <none>
```

## print yaml file

```bash
# get yaml 
kubectl ... get ...  -o yaml --export 
```

## full service name across namespaces

```bash
# full service name across namespaces
<service-name>.<namespace-name>.svc.cluster.local
```

## Specify a Context 

```bash
# list all context
kubectl config get-contexts

# specify context
kubectl_tke --context=<ContextName>  get nodes
```

## rollout/restart deployment

```bash
kubectl -n <namespace> rollout restart deployment <deployment-name>
```

## 查找不是 running 状态的 pod

```bash
$ kubectl get pods --all-namespaces | awk '{ if ($4!="Running")  print $0_ }'
NAMESPACE            NAME                                           READY   STATUS      RESTARTS   AGE
ingress-nginx        ingress-nginx-admission-create-gfm2j           0/1     Completed   0          9h
```

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



