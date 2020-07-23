
# EKS

![](../imgs/eks_cname.png)

- when you create an EKS cluster, you'll be given a cname like
    - `mycluster.eks.amazonaws.com`, the cname represents the ID of your cluster 
    - and when you deploy your worker nodes , they'll connect into this cluster by connecting directly to that cname.
- when you want to actually connect into it, you'll configure a kuberneters config file, used by `kubectl` tool.
    - this cname represents the managed control plane for your EKS cluster, and allows you to send operations to k8s.


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


## Create Cluster

### aws

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: region-code
Default output format [None]: json
```

- those information are stored in `~/.aws/`

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
--name prod \
--version 1.17 \
--region cn-northwest-1 \
--nodegroup-name standard-workers \
--node-type t3.medium \
--nodes 1 \
--nodes-min 1 \
--nodes-max 4 \
--ssh-access \
--ssh-public-key hda.pub \
--managed
```


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

[本地dash](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login)

> 填入 token

## Misc

[容器服务](https://cn-northwest-1.console.amazonaws.cn/eks/home?region=cn-northwest-1#/clusters)

```go
# find cluster security group
aws eks describe-cluster --name cluster_name --query cluster.resourcesVpcConfig.clusterSecurityGroupId
```






