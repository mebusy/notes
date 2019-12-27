...menustart

 - [K8s Tutorial](#2282b019d5749f94b3ff99dadd4d9293)
 - [Learn Kubernetes Basics](#d6241ba7176a22c6f5508a221d1716b7)
     - [Create a Cluster](#f4b3bba7f2a3c2742429d4af98964158)
         - [Using Minikube to Create a Cluster](#f47adff278a05ec02bc76b4d7d802a42)
     - [Deploy an App](#13279284e535f428ddd0037d4839f217)
         - [Using kubectl to Create a Deployment](#6770f897a032a9c25dea6adbd0cb237a)
     - [Explore Your App](#d98050e1771fa15a6ada9626483804bf)
         - [Viewing Pods and Nodes](#17dbb8a1e22daa6afbafb5065b15096c)
     - [Expose Your App Publicly](#82df24365fe3fd9599b3424f53d10145)
         - [Using a Service to Expose Your App](#6b755767754f0bdf07e6cc0138438cbf)
             - [Using labels](#a0147bf58c57372feeab86fd35f3c75c)
             - [Deleting a service](#3eaae17da90da6db3f5a359aff990fac)
     - [Scale Your App](#9ed959ed9324ef3c3af26b8fd76e65c6)
         - [Running Multiple Instances of Your App](#97368dc0d5ea684b04a059061d75f892)
             - [Scaling a deployment](#1cc09de5a7dc45ea6ce22e48ab7741e4)
             - [Load Balancing](#88788d3d6b03d421c6cf518ace672e36)
             - [Scale Down](#321a4150256dc52ed121fe7088de69ee)
     - [Update Your App](#77246ae2f33852920cb5d43806f8027f)
         - [Performing a Rolling Update](#a1f50c0414138a0b33c3f5841fd1f686)
 - [Configuring Redis using a ConfigMap](#27338a7f81ebe603ac23ab9e401ba99a)
 - [install Kubernetes](#fde4a6a869ea132a44d1703b574f94c2)
     - [Step 1 - Kubernetes Installation](#d960b90c6bd83a0c38ebb3243a43ac65)
         - [Disable SELinux and filewall](#70ed350d94ea2ee4beeb7d951dcc3f76)
         - [Enable br_netfilter Kernel Module](#f03737e43278c4e0e94939f9eec9b4f0)
         - [Disable SWAP](#f20da027e3ec9141171d13ff93807f52)
         - [Install Kubernetes](#5ed0c66dfa2ac395ad8e9830aa5964aa)
         - [Change the cgroup-driver](#2e1d298d7606fec45de7985efbfd555c)
     - [Step 2 - Kubernetes Cluster Initialization](#451e4690c07ec59f02a5d699d9e63196)
         - [Allow scheduling of pods on Kubernetes master](#3c77e740edb7196f00f94f28733a7bcb)
         - [Testing Create First Pod](#9010772af260a642bed9bb232163577c)

...menuend


<h2 id="2282b019d5749f94b3ff99dadd4d9293"></h2>


# K8s Tutorial

<h2 id="d6241ba7176a22c6f5508a221d1716b7"></h2>


# Learn Kubernetes Basics

<h2 id="f4b3bba7f2a3c2742429d4af98964158"></h2>


## Create a Cluster

<h2 id="f47adff278a05ec02bc76b4d7d802a42"></h2>


### Using Minikube to Create a Cluster
 
 - Kubernetes Clusters
    - Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. 
    - Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way
    - A Kubernetes cluster consists of two types of resources:
        - The Master coordinates the cluster
        - Nodes are the workers that run applications
 - Cluster Diagram
    - ![](https://d33wubrfki0l68.cloudfront.net/99d9808dcbf2880a996ed50d308a186b5900cec9/40b94/docs/tutorials/kubernetes-basics/public/images/module_01_cluster.svg)
    - The Master is responsible for managing the cluster. 
        - The master coordinates all activities in your cluster, such as 
            - scheduling applications, 
            - maintaining applications' desired state, 
            - scaling applications, 
            - and rolling out new updates.
    - A node is a VM or a physical computer that serves as a worker machine in a Kubernetes cluster.
        - Each node has a Kubelet , which is an agent for managing the node and communicating with the Kubernetes master.
        - The node should also have tools for handling container operations, such as Docker or rkt. 
        - A Kubernetes cluster that handles production traffic should have a minimum of three nodes.
        - The nodes communicate with the master using the Kubernetes API, which the master exposes. 
        - End users can also use the Kubernetes API directly to interact with the cluster.
 - Minikube
    - Minikube is a lightweight Kubernetes implementation that creates a VM on your local machine and deploys a simple cluster containing only one node. 
 - kubectl
    - To interact with Kubernetes we’ll use the command line interface, kubectl. 

```
$ kubectl cluster-info
Kubernetes master is running at https://172.17.0.6:8443

$ kubectl get nodes
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     <none>    51s       v1.10.0
```


<h2 id="13279284e535f428ddd0037d4839f217"></h2>


## Deploy an App

<h2 id="6770f897a032a9c25dea6adbd0cb237a"></h2>


### Using kubectl to Create a Deployment

 - Kubernetes Deployments
    - create a Kubernetes Deployment configuration. 
    - The Deployment instructs Kubernetes how to create and update instances of your application.
    - Once you've created a Deployment, the Kubernetes master schedules mentioned application instances onto individual Nodes in the cluster.
    - Once the application instances are created, a Kubernetes Deployment Controller continuously monitors those instances.
        - If the Node hosting an instance goes down or is deleted, the Deployment controller replaces it.
        - **This provides a self-healing mechanism to address machine failure or maintenance.**
 - ![](https://d33wubrfki0l68.cloudfront.net/152c845f25df8e69dd24dd7b0836a289747e258a/4a1d2/docs/tutorials/kubernetes-basics/public/images/module_02_first_app.svg)
 - Deploying your first app on Kubernetes
    - When you create a Deployment, you'll need to specify the container image for your application and the number of replicas that you want to run. 
    - You can change that information later by updating your Deployment

 - Let’s run our first app on Kubernetes with the `kubctl run` command
    - The `run` command creates a new deployment.

```
$ kubectl run kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 --port=8080
deployment.apps/kubernetes-bootcamp created

$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   1         1         1            1           1m
```

 - View our app
    - Pods that are running inside Kubernetes are running on a private, isolated network.
    - By default they are visible from other pods and services within the same kubernetes cluster, but not outside that network. 
    - When we use kubectl, we're interacting through an API endpoint to communicate with our application.
    - The kubectl command can create a proxy that will forward communications into the cluster-wide, private network. 

```
$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```

 - We now have a connection between our host and the Kubernetes cluster. 
    - The proxy enables direct access to the API from these terminals.
 - You can see all those APIs hosted through the proxy endpoint, now available at through http://localhost:8001. 
 - For example, we can query the version directly through the API using the curl command:

```
$ curl http://localhost:8001/version
{
  "major": "1",
  "minor": "10",
  "gitVersion": "v1.10.0",
  "gitCommit": "fc32d2f3698e36b93322a3465f63a14e9f0eaead",
  "gitTreeState": "clean",
  "buildDate": "2018-04-10T12:46:31Z",
  "goVersion": "go1.9.4",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

 - The API server will automatically create an endpoint for each pod, based on the pod name, that is also accessible through the proxy.
 - First we need to get the Pod name, and we'll store in the environment variable POD_NAME:

```
$ export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
$ echo Name of the Pod: $POD_NAME
Name of the Pod: kubernetes-bootcamp-5c69669756-jwzln
```

 - Now we can make an HTTP request to the application running in that pod:
    - The url is the route to the API of the Pod.

```
$ curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME/proxy/
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-jwzln | v=1
```

<h2 id="d98050e1771fa15a6ada9626483804bf"></h2>


## Explore Your App

<h2 id="17dbb8a1e22daa6afbafb5065b15096c"></h2>


### Viewing Pods and Nodes

 - Kubernetes Pods
    - When you created a Deployment, Kubernetes created a Pod to host your application instance. 
    - A Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker or rkt), and some shared resources for those containers.
    - Those resources include:
        - Shared storage, as Volumes
        - Networking, as a unique cluster IP address
        - Information about how to run each container, such as the container image version or specific ports to use
    - A Pod models an application-specific "logical host", and can contain different application containers which are relatively tightly coupled. 
    - The containers in a Pod share an IP Address and port space, are always co-located and co-scheduled, and run in a shared context on the same Node.
    - Pods are the atomic unit on the Kubernetes platform. 
        - When we create a Deployment on Kubernetes, that Deployment creates Pods with containers inside them
        - Each Pod is tied to the Node where it is scheduled, and remains there until termination (according to restart policy) or deletion. In case of a Node failure, identical Pods are scheduled on other available Nodes in the cluster.
    - ![](https://d33wubrfki0l68.cloudfront.net/fe03f68d8ede9815184852ca2a4fd30325e5d15a/98064/docs/tutorials/kubernetes-basics/public/images/module_03_pods.svg)
 - Nodes
    - Every Kubernetes Node runs at least:
        - Kubelet, a process responsible for communication between the Kubernetes Master and the Node; it manages the Pods and the containers running on a machine.
        - A container runtime (like Docker, rkt) responsible for pulling the container image from a registry, unpacking the container, and running the application.
Containers should only be scheduled together in a single Pod if they are tightly coupled and need to share resources such as disk.
    - ![](https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg)
 - Troubleshooting with kubectl
    - kubectl get - list resources
    - kubectl describe - show detailed information about a resource
    - kubectl logs - print the logs from a container in a pod
    - kubectl exec - execute a command on a container in a pod

<h2 id="82df24365fe3fd9599b3424f53d10145"></h2>


## Expose Your App Publicly 

<h2 id="6b755767754f0bdf07e6cc0138438cbf"></h2>


### Using a Service to Expose Your App

 - Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. 
 - Services allow your applications to receive traffic. 
 - Services can be exposed in different ways by specifying a **type** in the ServiceSpec:
    - ClusterIP (default) 
        - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
    - NodePort 
        - Exposes the Service on the same port of each selected Node in the cluster using NAT
        - Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`. Superset of ClusterIP.
    - LoadBalancer
        - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service.
        - Superset of NodePort.
    - ExternalName
        - Exposes the Service using an arbitrary name (specified by externalName in the spec) by returning a CNAME record with the name.
        - No proxy is used. This type requires v1.7 or higher of kube-dns.
 - ![](https://d33wubrfki0l68.cloudfront.net/cc38b0f3c0fd94e66495e3a4198f2096cdecd3d5/ace10/docs/tutorials/kubernetes-basics/public/images/module_04_services.svg)
 - A Service routes traffic across a set of Pods.
    - Services match a set of Pods using labels and selectors, a grouping primitive that allows logical operation on objects in Kubernetes. 
 - ![](https://d33wubrfki0l68.cloudfront.net/b964c59cdc1979dd4e1904c25f43745564ef6bee/f3351/docs/tutorials/kubernetes-basics/public/images/module_04_labels.svg)
 - We have a Service called kubernetes that is created by default when minikube starts the cluster. 
 - To create a new service and expose it to external traffic we’ll use the **expose** command with NodePort as parameter 

```
$ kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
service/kubernetes-bootcamp exposed
$ kubectl get services
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          39s
kubernetes-bootcamp   NodePort    10.111.213.124   <none>        8080:31921/TCP   13s
```
 
 - Create an environment variable called NODE_PORT that has the value of the Node port assigned:

```
$ export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
$ echo NODE_PORT=$NODE_PORT
NODE_PORT=31921

$ curl $(minikube ip):$NODE_PORT
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-t9t9k | v=1
```


<h2 id="a0147bf58c57372feeab86fd35f3c75c"></h2>


#### Using labels 

 - The Deployment created automatically a label for our Pod.

```
$ kubectl describe deployment
Name:                   kubernetes-bootcamp
Namespace:              default
CreationTimestamp:      Mon, 17 Dec 2018 08:11:51 +0000
Labels:                 run=kubernetes-bootcamp
Annotations:            deployment.kubernetes.io/revision=1
Selector:               run=kubernetes-bootcamp
...
```

 - Let’s use this label to query our list of Pods. 

```
$ kubectl get pods -l run=kubernetes-bootcamp
NAME                                   READY     STATUS    RESTARTS   AGE
kubernetes-bootcamp-5c69669756-t9t9k   1/1       Running   0          6m

$ kubectl get services -l run=kubernetes-bootcamp
NAME                  TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes-bootcamp   NodePort   10.111.213.124   <none>        8080:31921/TCP   6m
```

 - Get the name of the Pod and store it in the POD_NAME environment variable:

```
$ export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
$ echo Name of the Pod: $POD_NAME
Name of the Pod: kubernetes-bootcamp-5c69669756-t9t9k
```

 - To apply a new label we use the label command followed by the object type, object name and the new label:

```
$ kubectl label pod $POD_NAME app=v1
pod/kubernetes-bootcamp-5c69669756-t9t9k labeled

$ kubectl describe pods $POD_NAME
Name:           kubernetes-bootcamp-5c69669756-t9t9k
Namespace:      default
Node:           minikube/172.17.0.2
Start Time:     Mon, 17 Dec 2018 08:11:58 +0000
Labels:         app=v1
                pod-template-hash=1725225312
                run=kubernetes-bootcamp
```

<h2 id="3eaae17da90da6db3f5a359aff990fac"></h2>


#### Deleting a service

```
$ kubectl delete service -l run=kubernetes-bootcamp
service "kubernetes-bootcamp" deleted
```

 - pod is still running, can not access from outside of the cluseter

```
$ kubectl get po
NAME                                   READY     STATUS    RESTARTS   AGE
kubernetes-bootcamp-5c69669756-t9t9k   1/1       Running   0          10m

$ curl $(minikube ip):$NODE_PORT
curl: (7) Failed to connect to 172.17.0.2 port 31921: Connection refused
$ kubectl exec -ti $POD_NAME curl localhost:8080
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-t9t9k | v=1
```

<h2 id="9ed959ed9324ef3c3af26b8fd76e65c6"></h2>


## Scale Your App 

<h2 id="97368dc0d5ea684b04a059061d75f892"></h2>


### Running Multiple Instances of Your App

<h2 id="1cc09de5a7dc45ea6ce22e48ab7741e4"></h2>


#### Scaling a deployment

 - Running multiple instances of an application will require a way to distribute the traffic to all of them. 
 - Services have an integrated load-balancer that will distribute network traffic to all Pods of an exposed Deployment.
 - Services will monitor continuously the running Pods using endpoints, to ensure the traffic is sent only to available Pods.

```
$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   1         1         1            1           21s
```

 - let’s scale the Deployment to 4 replicas. We’ll use the `kubectl scale` command,

```
$ kubectl scale deployments/kubernetes-bootcamp --replicas=4
deployment.extensions/kubernetes-bootcamp scaled
$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   4         4         4            4           1m
$ kubectl get pods -o wide
NAME                                   READY     STATUS    RESTARTS   AGE       IP NODE
kubernetes-bootcamp-5c69669756-59jc4   1/1       Running   0          27s       172.18.0.7 minikube
kubernetes-bootcamp-5c69669756-9mfsm   1/1       Running   0          27s       172.18.0.6 minikube
kubernetes-bootcamp-5c69669756-klk9v   1/1       Running   0          1m        172.18.0.3 minikube
kubernetes-bootcamp-5c69669756-vg59n   1/1       Running   0          27s       172.18.0.5 minikube
```

<h2 id="88788d3d6b03d421c6cf518ace672e36"></h2>


#### Load Balancing

```
$ export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
$ echo NODE_PORT=$NODE_PORT
NODE_PORT=32638
$ curl $(minikube ip):$NODE_PORT
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-vg59n | v=1
$ curl $(minikube ip):$NODE_PORT
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-klk9v | v=1
```

 - We hit a different Pod with every request. This demonstrates that the load-balancing is working.

<h2 id="321a4150256dc52ed121fe7088de69ee"></h2>


#### Scale Down

```
$ kubectl scale deployments/kubernetes-bootcamp --replicas=2
$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   2         2         2            2           5m
$ kubectl get pods -o wide
NAME                                   READY     STATUS        RESTARTS   AGE       IP     NODE
kubernetes-bootcamp-5c69669756-59jc4   1/1       Running       0          4m        172.18.0.7   minikube
kubernetes-bootcamp-5c69669756-9mfsm   1/1       Terminating   0          4m        172.18.0.6   minikube
kubernetes-bootcamp-5c69669756-klk9v   1/1       Running       0          5m        172.18.0.3   minikube
kubernetes-bootcamp-5c69669756-vg59n   1/1       Terminating   0          4m        172.18.0.5   minikube
```

<h2 id="77246ae2f33852920cb5d43806f8027f"></h2>


## Update Your App

<h2 id="a1f50c0414138a0b33c3f5841fd1f686"></h2>


### Performing a Rolling Update

```
$ kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
deployment.extensions/kubernetes-bootcamp image updated
$ kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
$ kubectl get pods
NAME                                   READY     STATUS        RESTARTS   AGE
kubernetes-bootcamp-5c69669756-8sr8t   1/1       Terminating   0          1m
kubernetes-bootcamp-5c69669756-bb7nm   1/1       Terminating   0          1m
kubernetes-bootcamp-5c69669756-fhhf5   1/1       Terminating   0          1m
kubernetes-bootcamp-5c69669756-gl5js   1/1       Terminating   0          1m
kubernetes-bootcamp-7799cbcb86-25fpv   1/1       Running       0          7s
kubernetes-bootcamp-7799cbcb86-g6vwr   1/1       Running       0          3s
kubernetes-bootcamp-7799cbcb86-knjr6   1/1       Running       0          7s
kubernetes-bootcamp-7799cbcb86-swbq8   1/1       Running       0          5s
$ kubectl rollout status deployments/kubernetes-bootcamp
deployment "kubernetes-bootcamp" successfully rolled out
```

 - Rollback an update

```
$ kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
deployment.extensions/kubernetes-bootcamp image updated
$ kubectl rollout undo deployments/kubernetes-bootcamp
deployment.extensions/kubernetes-bootcamp
```


<h2 id="27338a7f81ebe603ac23ab9e401ba99a"></h2>


# Configuring Redis using a ConfigMap

---

<h2 id="fde4a6a869ea132a44d1703b574f94c2"></h2>


# install Kubernetes

<h2 id="d960b90c6bd83a0c38ebb3243a43ac65"></h2>


## Step 1 - Kubernetes Installation

<h2 id="70ed350d94ea2ee4beeb7d951dcc3f76"></h2>


### Disable SELinux and filewall

- In this tutorial, we will not cover about SELinux configuration for Docker, so we will disable it.


```
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

systemctl disable firewalld
```

PS: [开启iptables情况下Swarm、kubernetes等组件正常工作的配置](https://blog.csdn.net/A632189007/article/details/78909835)

<h2 id="f03737e43278c4e0e94939f9eec9b4f0"></h2>


### Enable br_netfilter Kernel Module

 - The br_netfilter module is required for kubernetes installation.
 - Enable this kernel module so that the packets traversing the bridge are processed by iptables for filtering and for port forwarding, and the kubernetes pods across the cluster can communicate with each other.

```
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
echo '1' > /proc/sys/net/bridge/bridge-nf-call-ip6tables

// 其实就是编辑 /etc/sysctl.conf 
```


<h2 id="f20da027e3ec9141171d13ff93807f52"></h2>


### Disable SWAP

```
swapoff -a
```

 - And then edit the '/etc/fstab' file.  Comment the swap line UUID as below

```
# /dev/mapper/cl-swap     swap                    swap    defaults        0 0  
```

 - why disable swap ?
    - The idea of kubernetes is to tightly pack instances to as close to 100% utilized as possible. All deployments should be pinned with CPU/memory limits. So if the scheduler sends a pod to a machine it should never use swap at all. You don't want to swap since it'll slow things down.
    - Its mainly for performance.
    - the idea is if a node only has 3G free to use.. and your new pod wants 4.. its going to go on another node.


<h2 id="5ed0c66dfa2ac395ad8e9830aa5964aa"></h2>


### Install Kubernetes

```
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
        https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
```

```
yum install -y kubelet kubeadm kubectl

reboot

systemctl start docker && systemctl enable docker
systemctl start kubelet && systemctl enable kubelet
```


<h2 id="2e1d298d7606fec45de7985efbfd555c"></h2>


### Change the cgroup-driver

 - We need to make sure the docker-ce and kubernetes are using same 'cgroup'.

```
docker info | grep -i cgroup
Cgroup Driver: cgroupfs
```

 - And you see the docker is using 'cgroupfs' as a cgroup-driver.

 - Now run the command below to change the kuberetes cgroup-driver to 'cgroupfs'.

```
sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

systemctl daemon-reload
systemctl restart kubelet
```

 - 注意，可能  10-kubeadm.conf 文件中没有 cgroup-driver . 
    - 手动添加 `Environment="KUBELET_CGROUP_ARGS=--cgroup-driver=cgroupfs"`

<h2 id="451e4690c07ec59f02a5d699d9e63196"></h2>


## Step 2 - Kubernetes Cluster Initialization

```
kubeadm init --apiserver-advertise-address=10.192.83.78 --pod-network-cidr=10.244.0.0/16
```

 - apiserver-advertise-address = determines which IP address Kubernetes should advertise its API server on.
 - pod-network-cidr = specify the range of IP addresses for the pod network. We're using the 'flannel' virtual network. If you want to use another pod network such as weave-net or calico, change the range IP address.


 - when the initialization done, do the things listed 
    1. Create new '.kube' configuration directory and copy the configuration 'admin.conf'.
    2. deploy the flannel network to the kubernetes cluster using the kubectl command.
        - `kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`

 - for worker node, use `kubeadm join` to join into the cluster
    - use `journalctl -u kubelet` to debug worker if it still in status `NotReady`


<h2 id="3c77e740edb7196f00f94f28733a7bcb"></h2>


###  Allow scheduling of pods on Kubernetes master

```
kubectl taint node <mymasternode> node-role.kubernetes.io/master:NoSchedule-
node/<mymasternode>  untainted
```


<h2 id="9010772af260a642bed9bb232163577c"></h2>


### Testing Create First Pod

```
kubectl create deployment nginx --image=nginx
kubectl create service nodeport nginx --tcp=80:80

[root@localhost ~]# kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        69m
nginx        NodePort    10.97.24.123   <none>        80:31116/TCP   16m
```

 - Now you will get the nginx pod is now running under cluster IP address '10.97.24.123' port 80, and the node main IP address  on port '31116'.
