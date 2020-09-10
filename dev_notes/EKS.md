...menustart

 - [EKS](#f79368a88745f4dba5e0fc92aa545c61)
     - [EKS getting started](#9c7235108be4bd172807717650dfe1fa)
     - [How to get started](#07e1d66babe77070cc76a4e637c9f26d)
     - [Create Cluster](#015ce80764f67c3fa35ff5b824724d95)
         - [aws](#ac68bbf921d953d1cfab916cb6120864)
         - [kubectl & eksctl](#0797d40efd8aa563d7e4fe7a4dd0ca0d)
     - [Deploy k8s control panel](#0fb3db388cb28547e6b0d17ca0c608b5)
     - [部署 ALB 入口控制器](#64e08a2de07bf4869794d3b8c5666add)
     - [Misc](#74248c725e00bf9fe04df4e35b249a19)

...menuend


<h2 id="f79368a88745f4dba5e0fc92aa545c61"></h2>


# EKS

![](../imgs/eks_cname.png)

- when you create an EKS cluster, you'll be given a cname like
    - `mycluster.eks.amazonaws.com`, the cname represents the ID of your cluster 
    - and when you deploy your worker nodes , they'll connect into this cluster by connecting directly to that cname.
- when you want to actually connect into it, you'll configure a kuberneters config file, used by `kubectl` tool.
    - this cname represents the managed control plane for your EKS cluster, and allows you to send operations to k8s.


<h2 id="9c7235108be4bd172807717650dfe1fa"></h2>


## EKS getting started

![](../imgs/eks_get_started.png)

1. Set your environment
    - things like , a VPC, a subnet, internet gateways, etc...
2. Create an EKS cluster
    - this is the actual highly available control plane
    - it'll configure all of the private key infrastructure, it'll setup the ingress into that control plane, and it'll give you that cname.
3. Provision worker nodes
    - these instances live within your EC2 console and are managed by an auto scaling group that you are able to control, this means that you can easily grow and shrink the cluster to your own needs.
4. Launch workload
    - once your worker nodes are up, you can deploy any container you'd like. 

<h2 id="07e1d66babe77070cc76a4e637c9f26d"></h2>


## How to get started

1. AWS CloudFormation
    - aws native way to provison clusters
    - it's simple to manage via the CLI or using the AWS console
    - you can quickly replicate your clusters across multiple regions by using the same templates
    - and you're able to track any changes using the newer drift functionality to these clusters.
2. eksctl
    - [eksctl](https://docs.amazonaws.cn/eks/latest/userguide/getting-started-eksctl.html)
    - provide single command to create/update/delete an EKS cluster. 
3. Terraform , etc...


<h2 id="015ce80764f67c3fa35ff5b824724d95"></h2>


## Create Cluster

<h2 id="ac68bbf921d953d1cfab916cb6120864"></h2>


### aws

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: region-code
Default output format [None]: json
```

- those information are stored in `~/.aws/`

<h2 id="0797d40efd8aa563d7e4fe7a4dd0ca0d"></h2>


### kubectl & eksctl

```bash
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl

# if you need upgrade
brew upgrade eksctl && brew link --overwrite eksctl
```

```bash
#创建密钥对
# The --query option specifies use   KeyMaterial , 不要改动
aws ec2 create-key-pair --key-name hdaKeyPair --query 'KeyMaterial' --output text > hdaKeyPair.pem
# permission
chmod 400 hdaKeyPair.pem

# Retrieving the public key for your key pair
ssh-keygen -y -f hdaKeyPair.pem  > hda.pub


# 使用 eksctl 创建集群

eksctl create cluster \
--name test \
--version 1.17 \
--region cn-northwest-1 \
--nodegroup-name test-workers \
--node-type t3.medium \
--nodes 2 \
--nodes-min 2 \
--nodes-max 4 \
--vpc-private-subnets=subnet-993f04d3,subnet-99c11ee2 \
--node-private-networking \
--ssh-access \
--ssh-public-key hda.pub \
--managed
```


- 说明:
    - 指定subnet的话，是否自动分配公网ip 是由subnet 指定的
    - [release public IP](https://stackoverflow.com/questions/38533725/can-i-remove-the-public-ip-on-my-instance-without-terminating-it)

```bash
# delte cluster ,normally you will fail, delete, or detach?  the VPC in first
eksctl delete cluster --region=cn-northwest-1 --name=<...>
```

- to create a new manged nodegroup ...

```bash
eksctl create nodegroup --cluster <cluster name> \
--region cn-northwest-1 \
--name <nodegroup name> \
--node-type t3.xlarge \
--node-volume-size 150 \
--nodes 1 \
--nodes-min 1 \
--nodes-max 8 \
--node-private-networking \
--ssh-access \
--ssh-public-key hda.pub \
--managed    
```

- 注意: 新增了nodegroup后，你需要 attach existing load balancer to the new node group
    1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
    2. On the navigation pane, under AUTO SCALING, choose the Auto Scaling Group.
    3. On the Details tab, choose Edit.
    4. Do one of the following:
        - [Classic Load Balancers] For Classic Load Balancers, choose your load balancer.
        - [Application/Network Load Balancers] For Target Groups, choose your target group.

- 切换集群
    - 
    ```bash
    aws eks update-kubeconfig --name  TEST  --region cn-northwest-1
    ```

<h2 id="0fb3db388cb28547e6b0d17ca0c608b5"></h2>


## Deploy k8s control panel

[部署 Kubernetes 控制面板 (Web UI)](https://docs.amazonaws.cn/eks/latest/userguide/dashboard-tutorial.html)


-  docker login
    - `echo $(aws ecr get-login-password)|docker login --password-stdin --username AWS ${aws_account).reposotiry_url`



```bash
# 1 部署 Metrics Server：
wget https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml

# replace with image : cruse/metrics-server-amd64:v0.3.6
kubectl apply -f components.yaml

# 命令验证 metrics-server 部署是否运行所需数量的 Pod：
kubectl get deployment metrics-server -n kube-system
```

```bash
# 2 部署 K8s control panel list
curl -o recommended.yaml https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml

cat recommended.yaml | grep image
          image: kubernetesui/dashboard:v2.0.0-beta8
          imagePullPolicy: Always
          image: kubernetesui/metrics-scraper:v1.0.1


# a 查看您下载的一个或多个清单文件，并记下映像名称。使用以下命令在本地下载映像。
docker pull image:<TAG>
# b 使用以下命令标记要推送到中国区域内的 Amazon Elastic Container Registry 存储库的映像。
docker tag image:<TAG> <AWS_ACCOUNT_ID>.<repository_url>/image:<TAG>
docker push ....

kubectl apply -f recommended.yaml
```

```bash
# 3 创建 eks-admin 服务账户和集群角色绑定

# eks-admin-service-account.yaml

kubectl apply -f eks-admin-service-account.yaml
```

```bash
# 4 连接到控制面板

# a 检索 eks-admin 服务账户的身份验证令牌。从输出中复制 token 值。您可以使用此令牌连接到控制面板。
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')

# b 开始 kubectl proxy.
kubectl proxy
```

[本地dashboard](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login)

> 填入 token


<h2 id="64e08a2de07bf4869794d3b8c5666add"></h2>


## 部署 ALB 入口控制器

[官方文档](https://docs.aws.amazon.com/zh_cn/eks/latest/userguide/alb-ingress.html)

1 标记 VPC 中要用于负载均衡器的子网，以便 ALB 入口控制器知道它可以使用这些子网

tag key | value | for ...
--- | --- | --- 
`kubernetes.io/cluster/<cluster-name>` | shared |  标记 VPC 中的所有子网，以便 Kubernetes 能够发现它们
kubernetes.io/role/elb | 1 | 标记 VPC 中的公有子网，以便 Kubernetes 知道仅将这些子网用于外部负载均衡器


2 创建 IAM OIDC 提供程序，并将该提供程序与您的集群关联。

```bash
eksctl utils associate-iam-oidc-provider \
    --region cn-northwest-1 \
    --cluster test \
    --approve
```

3 下载 ALB 入口控制器 pod 的 IAM 策略，该策略允许此 pod 代表您调用 AWS API

```bash
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.8/docs/examples/iam-policy.json
```

4 使用上一步中下载的策略创建一个名为 ALBIngressControllerIAMPolicy 的 IAM 策略。

```bash
aws iam create-policy \
    --policy-name ALBIngressControllerIAMPolicy \
    --policy-document file://iam-policy.json
```

记下返回的策略 ARN。

5 在 kube-system 命名空间中创建一个名为 alb-ingress-controller 的 Kubernetes 服务账户，并创建集群角色和针对 ALB 入口控制器的集群角色绑定

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.8/docs/examples/rbac-role.yaml
```

6 为 ALB 入口控制器创建一个 IAM 角色，并将该角色附加到在上一步中创建的服务账户

```bash
eksctl create iamserviceaccount \
    --region cn-northwest-1 \
    --name alb-ingress-controller \
    --namespace kube-system \
    --cluster test \
    --attach-policy-arn arn:aws-cn:iam::2249932229B6:policy/ALBIngressControllerIAMPolicy \
    --override-existing-serviceaccounts \
    --approve
```

7 部署 ALB 入口控制器

```bash
# download yaml
wget https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.8/docs/examples/alb-ingress-controller.yaml
# edit , add cluster name
    spec:
      containers:
      - args:
        - --ingress-class=alb
        - --cluster-name=prod
        # for WAFv2 is not available in AWS China regions
        - --feature-gates=waf=false,wafv2=false


# deploy
kubectl apply -f alb-ingress-controller.yaml 
```

8 确认 ALB 入口控制器是否正在运行

```
kubectl get pods -n kube-system
```

9 部署 ingress

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
  labels:
    k8s-app: test-ingress
spec:
  rules:
    - http:
        paths:
          - path: /*
            backend:
              serviceName: ipa-server
              servicePort: 7001
```

10 如果在几分钟后尚未创建入口，请运行以下命令以查看入口控制器日志。

```bash
kubectl logs -n kube-system   deployment.apps/alb-ingress-controller
```

For TLS loader balancer 

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: umc-test-ingress-443
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}]'
  labels:
    k8s-app: umc-test-ingress-443
spec:
  rules:
  - host: server1-test.domain.com
    http:
      paths:
        - path: /*
          backend:
            serviceName: my-game-server
            servicePort: 9000
  - host: server2-test.domain.com
    http:
      paths:
        - path: /*
          backend:
            serviceName: my-ipa-server
            servicePort: 7001
```

- alb.ingress.kubernetes.io/security-groups: sg-xxxx, nameOfSg1
    - When this annotation is not present, the controller will automatically create 2 security groups
- [more ALB annotation](https://kubernetes-sigs.github.io/aws-alb-ingress-controller/guide/ingress/annotation/)

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


## Misc

```go
# find cluster security group
aws eks describe-cluster --name cluster_name --query cluster.resourcesVpcConfig.clusterSecurityGroupId
```






