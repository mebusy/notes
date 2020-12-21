...menustart

- [TKE](#12510f8273f9a47f538779a3afd71f53)
- [kubectl](#0f12ee5c9f1dd90158580f1c292b0d37)
    - [install](#19ad89bc3e3c9d7ef68b89523eff1987)
    - [use kubectl](#773c2c719c95cc40967b0e945ada8898)
        - [#list only pod name,  and no column name](#7ec1be1882d584532184cc1609283eb3)
        - [find pod by ip](#083e4e9d5085b330f59f1e5032b9e408)
        - [get yaml](#27b7cb2760c21e097eef0e0c787ff402)
        - [full service name across namespaces](#f105d78fa5298a8e02f51a22ac6da980)
        - [Specify a Context](#bd251ed977799cf91b83164dbb4e6bab)
        - [restart deployment](#cdd368345c1399226f29c445f2d344f7)
        - [search log in all pods](#7740cb2915e67ffc07500ca7d0dc086f)
        - [other usage](#4b091e7bf24f9e193323877b35ece5fb)
    - [kubectl cheatsheet](#d4b1fc7497d32f6554e52b3a22b5685f)
    - [role , rolebinding](#a65165eaad917e08dbaab4ca345c9140)
    - [postStart / preStop event handle](#3cfc0b587c5bea5919d967aa0c0f7629)
    - [JSONPath 表达式](#f0cfc2eb04f3c904ba876b4ff5e36744)
- [腾讯云 用户管理](#7616e9353ba2c3c55eb7063e51fc65fb)
    - [策略](#66914536facf5b30973b236fb814d23f)
- [腾讯云 Misc](#4214290dc4bf8068d16758a84a3496a7)
    - [ingress 证书 对部分低版本Android设备不兼容，导致 ssl hand shake error.](#d42d194dd306f76100f9b591fd878396)
    - [k8s node 磁盘占用过高查找并清理](#e8dfbb86e3e1d39df969144ae4d3f06b)
    - [清除不再使用的 image](#77563c3ed75c144a6617a7077a1b4771)
    - [查找不是 running 状态的 pod](#145f750dc8c7bde1231227e5d027eafd)
- [cntlm 设置代理 (Centos7)](#c36aef5f4c92632a2362a83ed0523565)
- [cntlm (Macosx)](#48cd1b6a59fb119e19d9f83e6cf43668)

...menuend


<h2 id="12510f8273f9a47f538779a3afd71f53"></h2>


# TKE

<h2 id="0f12ee5c9f1dd90158580f1c292b0d37"></h2>


# kubectl

- 客户端小版本最多比服务器大1， 比如服务器版本是1.7.8 , 客户端版本可以用 1.8.x 

<h2 id="19ad89bc3e3c9d7ef68b89523eff1987"></h2>


## install

- linux
    - https://storage.googleapis.com/kubernetes-release/release/v1.8.4/bin/linux/amd64/kubectl
- macos:
    - replace `linux` with `darwin` 

```
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```



<h2 id="773c2c719c95cc40967b0e945ada8898"></h2>


## use kubectl

<h2 id="7ec1be1882d584532184cc1609283eb3"></h2>


### #list only pod name,  and no column name

```bash
#list only pod name,  and no column name
kubectl get po --no-headers -o custom-columns=:.metadata.name
```

<h2 id="083e4e9d5085b330f59f1e5032b9e408"></h2>


### find pod by ip

```bash
# find pod by ip
kubectl get po --all-namespaces -o wide | grep 10.0.0.39
```

<h2 id="27b7cb2760c21e097eef0e0c787ff402"></h2>


### get yaml 

```bash
# get yaml 
kubectl ... get ...  -o yaml --export 
```

<h2 id="f105d78fa5298a8e02f51a22ac6da980"></h2>


### full service name across namespaces

```bash
# full service name across namespaces
<service-name>.<namespace-name>.svc.cluster.local
```

<h2 id="bd251ed977799cf91b83164dbb4e6bab"></h2>


### Specify a Context 

```bash
# list all context
kubectl config get-contexts

# specify context
kubectl_tke --context=<ContextName>  get nodes
```

<h2 id="cdd368345c1399226f29c445f2d344f7"></h2>


### restart deployment

```bash
kubectl -n <namespace> rollout restart deployment <deployment-name>
```

<h2 id="7740cb2915e67ffc07500ca7d0dc086f"></h2>


### search log in all pods

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


<h2 id="4b091e7bf24f9e193323877b35ece5fb"></h2>


### other usage

```bash
7. ImagePullSecret ( 如果需要从外部pull 镜像的话需要设置, in deployment)
    - qcloudregistrykey , 

it seems that TKE will automatically use  `tencenthubkey` ?

8. secret can not be access across namespaces 
   to dup a secret from namespace A  into namespace B

   kubectl get secret <secret-name> --namespace=A --export -o yaml | kubectl apply --namespace=B -f -

```


<h2 id="d4b1fc7497d32f6554e52b3a22b5685f"></h2>


## kubectl cheatsheet

[cheatsheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)


<h2 id="a65165eaad917e08dbaab4ca345c9140"></h2>


## role , rolebinding

- [kubectl role/rolebinding 例子](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#command-line-utilities)
- [role yaml 文件，resouce/verb 例子](https://github.com/kubernetes/kubernetes/blob/master/plugin/pkg/auth/authorizer/rbac/bootstrappolicy/testdata/controller-roles.yaml)

使用 role / rolebinding 的一般方法

1. create serveraccount
    - `create serviceaccount <name> ` , it will also create an secret
    - 任何namespace 下都有一个默认的 serviceacount:  default
2. create role
    - 
    ```bash
    # create a role
    kubectl -n $_NS create role role_po --verb="list" --resource=po --dry-run -o yaml
    kubectl -n $_NS create role role_deploy --verb="get" --resource=deploy --dry-run -o yaml
    kubectl -n $_NS create role role_scale --verb="update" --resource=replicasets --dry-run -o yaml
    ```
    - we also can merge different roles ,by merging --dry-run output into 1 yaml file then.
        - `kubectl -n $_NS create -f role.yaml`
3. create rolebinding
    - 
    ```bash
    # To bind the "default" serviceaccount and "role_scale"
    kubectl -n $_NS create rolebinding default_scale_binding --serviceaccount="$_NS:default" --role=role_scale --dry-run -o yaml
    ```

<h2 id="3cfc0b587c5bea5919d967aa0c0f7629"></h2>


## postStart / preStop event handle

[Define postStart and preStop handlers](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/#define-poststart-and-prestop-handlers)

on TKE, add it on deployment yaml, following the `image` property.

example: when this pod restart , before it really ready,  make 1 another service/pod relanuch.

```yaml
        lifecycle:
          postStart:
            exec:
              command: ["/bin/sh", "-c", "_NS=umc-hse-dev && _APP=umc-hse-app  && replinum=`kubectl -n $_NS get deploy $_APP -o=jsonpath='{.status.replicas}'` && kubectl -n $_NS  scale  deployments/$_APP --replicas=$(($replinum-1)) && kubectl -n $_NS  scale  deployments/$_APP --replicas=$replinum"]
```


<h2 id="f0cfc2eb04f3c904ba876b4ff5e36744"></h2>


## JSONPath 表达式

```bash
# 选择一个列表的指定元素
$ kubectl get pods -o custom-columns='DATA:spec.containers[0].image'

# 选择和一个过滤表达式匹配的列表元素
$ kubectl get pods -o custom-columns='DATA:spec.containers[?(@.image!="nginx")].image'

# 选择特定位置下的所有字段（无论名称是什么）
$ kubectl get pods -o custom-columns='DATA:metadata.*'

# 选择具有特定名称的所有字段（无论其位置如何）
$ kubectl get pods -o custom-columns='DATA:..image'
```

显示 Pod 的所有容器镜像:

```bash
$ kubectl get pods \
  -o custom-columns='NAME:metadata.name,IMAGES:spec.containers[*].image'
```

显示节点的可用区域:

```bash
$ kubectl get nodes \
  -o custom-columns='NAME:metadata.name,ZONE:metadata.labels.failure-domain\.beta\.kubernetes\.io/zone'
```

- 每个节点的可用区都可以通过标签`failure-domain.beta.kubernetes.io/zone`来获得
- 如果你的 Kubernetes 集群部署在公有云上面（比如 AWS、Azure 或 GCP），那么上面的命令就非常有用了




<h2 id="7616e9353ba2c3c55eb7063e51fc65fb"></h2>


# 腾讯云 用户管理

<h2 id="66914536facf5b30973b236fb814d23f"></h2>


## 策略

- 访问 COS 某个bucket的策略

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cos:*"
            ],
            "resource": "qcs::cos:::BUCKET-NAME/*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": [
                "monitor:*",
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup"
            ],
            "resource": "*"
        }
    ]
}
```


<h2 id="4214290dc4bf8068d16758a84a3496a7"></h2>


# 腾讯云 Misc

<h2 id="d42d194dd306f76100f9b591fd878396"></h2>


## ingress 证书 对部分低版本Android设备不兼容，导致 ssl hand shake error.

- 更换证书
- 检查证书兼容性  https://myssl.com/ 


<h2 id="e8dfbb86e3e1d39df969144ae4d3f06b"></h2>


## k8s node 磁盘占用过高查找并清理

- kubectl 查看node 状态 `kubectl describe nodes` .

- 登陆节点，查看硬盘占用
    - 查看总体占用 `df | less`
    - 查看某个path下的占用
        - `ls -Sl`
        - `du -m <path> | sort -nr | head -n 10`
            - `du -shxm * | sort -nr | head -n 10`
    - 查看某个 目录占用的磁盘空间
        - 
        ```bash
        du -sh <your dictory>
        ```

<h2 id="77563c3ed75c144a6617a7077a1b4771"></h2>


## 清除不再使用的 image 

```
docker images | grep "<none>" | grep umc-app-images | awk "{print \$3}" | xargs docker rmi

# more aggressive 
docker images | grep umc-app-images | awk "{print \$3}" | xargs docker rmi
```

<h2 id="145f750dc8c7bde1231227e5d027eafd"></h2>


## 查找不是 running 状态的 pod

```
kubectl_umc get pods --all-namespaces | awk '{ if ($4!="Running")  print $0_ }'
```


<h2 id="c36aef5f4c92632a2362a83ed0523565"></h2>


# cntlm 设置代理 (Centos7)

- 1 install cntlm

```
1) download from 
    https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/c/
2) rpm -Uvh xxx.rpm
```


- 2 Get password hash 
    - (type your password, press enter and copy the output)
    - modify your username/domain first in `/etc/cntlm.conf`
    - or `cntlm -H -u <Your username> -d cop-domain` ?

```
$ cntlm -H
Password:
PassLM          14BE8CB0282308185246B269C29C0A88
PassNT          DD8F12AC2482B5BC43A6972E7DFD0F78
PassNTLMv2      934498581AFCBE80CA0457E0FD30B0F9    # Only for user '', domain ''
```

- 3 Edit cntlm configuration file(Example for testuser)

```
#vi /etc/cntlm.conf

Username YOURUSERNAME
Domain YOURCOMPANYDOMAIN
########Paste result of cntlm -H here###########
PassLM          14BE8CB0282308185246B269C29C0A88
PassNT          DD8F12AC2482B5BC43A6972E7DFD0F78
PassNTLMv2      934498581AFCBE80CA0457E0FD30B0F9    # Only for user '', domain ''

Proxy YOUR_COMPANY_PROXY_HOST:PORT
NoProxy ...
Auth NTLM
```

- 4 Enable cntlm service at boot , and start it now
    - `#systemctl enable cntlm`
    - `#systemctl start cntlm`

- 5 Set environment variables (HTTP_PROXY and HTTPS_PROXY)
    - use:  `127.0.0.1:3128`

---

<h2 id="48cd1b6a59fb119e19d9f83e6cf43668"></h2>


# cntlm (Macosx)

- /usr/local/etc/cntlm.conf 
    - otherwise it might be in /etc/cntlm.conf

- You can run cntlm in debug mode for testing purpose and see what’s happening:
    - `cntlm -f` # Run in foreground, do not fork into daemon mode.
- If everything is fine you can launch it as a daemon just by typing:
    - `cntlm`
- To have launchd start cntlm now and restart at startup:
    - `sudo brew services start cntlm`


- set proxy env

```
export http_proxy=http://localhost:3128
export https_proxy=https://localhost:3128
```

- restart 
    - `brew services restart cntlm`



