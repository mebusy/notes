[](...menustart)

- [TKE](#12510f8273f9a47f538779a3afd71f53)
- [kubectl](#0f12ee5c9f1dd90158580f1c292b0d37)
    - [other usage](#4b091e7bf24f9e193323877b35ece5fb)
    - [role , rolebinding](#a65165eaad917e08dbaab4ca345c9140)
- [腾讯云 用户管理](#7616e9353ba2c3c55eb7063e51fc65fb)
    - [策略](#66914536facf5b30973b236fb814d23f)
        - [访问 COS 某个bucket的策略](#d255a9679389c247f2735458b48e299f)
        - [操作 北京 区的cvm， 无支付权限](#e975ebbc1e61fec2da797cf6b13b038c)
- [腾讯云 Misc](#4214290dc4bf8068d16758a84a3496a7)
    - [ingress 证书 对部分低版本Android设备不兼容，导致 ssl hand shake error.](#d42d194dd306f76100f9b591fd878396)
    - [k8s node 磁盘占用过高查找并清理](#e8dfbb86e3e1d39df969144ae4d3f06b)
    - [清除不再使用的 image](#77563c3ed75c144a6617a7077a1b4771)
    - [Pod Stuck in Terminating](#f33345d63406b6b6402c63cb4275d5b7)
    - [Duplicate service , deployment one namespece to another namespace](#12847d0d05565b4f2c885fa89ab4049b)
    - [TKE node 常用 安全组](#5c990c1691165d355ad21cc1f7c5801e)

[](...menuend)


<h2 id="12510f8273f9a47f538779a3afd71f53"></h2>

# TKE

<h2 id="0f12ee5c9f1dd90158580f1c292b0d37"></h2>

# kubectl

<h2 id="4b091e7bf24f9e193323877b35ece5fb"></h2>

## other usage

```bash
7. ImagePullSecret ( 如果需要从外部pull 镜像的话需要设置, in deployment)
    - qcloudregistrykey , 

it seems that TKE will automatically use  `tencenthubkey` ?

8. secret can not be access across namespaces 
   to dup a secret from namespace A  into namespace B

   kubectl get secret <secret-name> --namespace=A --export -o yaml | kubectl apply --namespace=B -f -

```

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

<h2 id="7616e9353ba2c3c55eb7063e51fc65fb"></h2>

# 腾讯云 用户管理

<h2 id="66914536facf5b30973b236fb814d23f"></h2>

## 策略

<h2 id="d255a9679389c247f2735458b48e299f"></h2>

### 访问 COS 某个bucket的策略

```json
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

<h2 id="e975ebbc1e61fec2da797cf6b13b038c"></h2>

### 操作 北京 区的cvm， 无支付权限

```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": "finance:*",
            "resource": "qcs::cvm:ap-beijing::*"
        },
        {
            "effect": "allow",
            "action": "cvm:*",
            "resource": "qcs::*:ap-beijing::*"
        }
    ]
}
```

如果要禁止 创建/修改 cvm 安全组，加上

```json
        {
            "effect": "deny",
            "action": [
                "cvm:CreateSecurityGroup",
                "cvm:CreateSecurityGroupPolicy",
                "cvm:DeleteSecurityGroup",
                "cvm:DeleteSecurityGroupPolicy",
                "cvm:ModifySecurityGroupAttributes",
                "cvm:ModifySecurityGroupPolicys",
                "cvm:ModifySingleSecurityGroupPolicy"
            ],
            "resource": [
                "*"
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
    - [check disk usage](./disk_usage.md)

<h2 id="77563c3ed75c144a6617a7077a1b4771"></h2>

## 清除不再使用的 image 

```
docker images | grep "<none>" | grep co-app-images | awk "{print \$3}" | xargs docker rmi

# more aggressive 
docker images | grep co-app-images | awk "{print \$3}" | xargs docker rmi
```


<h2 id="f33345d63406b6b6402c63cb4275d5b7"></h2>

## Pod Stuck in Terminating

很多原因会导致这个问题，可以先排除，是不是 node 坏了

```bash
k get po -o wide # this will show which Node is running the pod
k get nodes # Check status of that node... I got it NotReady
```

<h2 id="12847d0d05565b4f2c885fa89ab4049b"></h2>

## Duplicate service , deployment one namespece to another namespace

<details>
<summary>
kubectl command ...
</summary>

```bash

cur_ns="co-hse-dev"
dst_ns="co-hse-dev-vivo"

alias kbctl="kubectl_tke --context=co-k8s-cluster"

# create namespace
kbctl create namespace $dst_ns

# 先去webpage   namespace下发一个secret 凭证

# dup service and then apply
kbctl -n $cur_ns get svc --export -o yaml | sed -e "s/namespace: $cur_ns/namespace: $dst_ns/"  | yq eval 'del(.items[].metadata.resourceVersion, .items[].metadata.uid, .items[].metadata.annotations, .items[].metadata.creationTimestamp, .items[].metadata.selfLink, .items[].spec.clusterIP, .items[].spec.ports[].nodePort )' - |  kbctl apply -f -

# dup role, and role banding, if necessary
kbctl -n $cur_ns get role,rolebinding --export -o yaml | sed -e "s/namespace: $cur_ns/namespace: $dst_ns/"  | yq eval 'del(.items[].metadata.resourceVersion, .items[].metadata.uid, .items[].metadata.annotations, .items[].metadata.creationTimestamp, .items[].metadata.selfLink)' - |  kbctl apply -f -


# dup deployment and then apply
kbctl -n $cur_ns get deploy --export -o yaml | sed -e "s/namespace: $cur_ns/namespace: $dst_ns/"  | yq eval 'del(.items[].metadata.resourceVersion, .items[].metadata.uid, .items[].metadata.annotations, .items[].metadata.creationTimestamp, .items[].metadata.selfLink, .items[].status)' - |  kbctl apply -f -


# update some other info, like mysql

# try container repository trigger
```

</details>


<h2 id="5c990c1691165d355ad21cc1f7c5801e"></h2>

## TKE node 常用 安全组

source | port | policy | comments 
--- | --- | --- | ---
0.0.0.0/0 | TCP:30000-32767 | 允许 | alb
0.0.0.0/0 | ICMP | 允许 | allow ping
10.0.0.0/16 | ALL | 允许 | db
172.16.0.0/12 | ALL | 允许 | k8s container network
192.168.0.0/16 | ALL | 允许 | 


