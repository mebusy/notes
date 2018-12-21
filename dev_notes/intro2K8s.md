...menustart

 - [edX  Introduction to Kuberneters](#e017284a962c40a7dc29fd29bea64bb4)
 - [Access Kuberneters](#10ebfd4c6ede5e99a80eb32105dc4419)
     - [HTTP API Space of Kubernetes](#c9157975d6f67292424e86421d6ca49c)
     - [kubectl Configuration File](#70becb84ec118d75e27f125448562a2b)
     - [Kubernetes dashboard](#6bbde18895b093a1a0fc79b5c02e4462)
         - [Deploying the Dashboard UI](#ae1fd03692378014b99c5c70b6c121af)
         - [Accessing the Dashboard UI](#f32d0f539f9fbaff4c670cd2e5d7b14d)
         - [APIs - with 'kubectl proxy'](#d7dba71d2e1aa5aea658e819489eab4d)
         - [APIs - without 'kubectl proxy'](#c4a8eba76a7943e2e98a2e8b0f014db3)

...menuend


<h2 id="e017284a962c40a7dc29fd29bea64bb4"></h2>

# edX  Introduction to Kuberneters


<h2 id="10ebfd4c6ede5e99a80eb32105dc4419"></h2>

# Access Kuberneters

<h2 id="c9157975d6f67292424e86421d6ca49c"></h2>

## HTTP API Space of Kubernetes

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s-api-server-space.jpg)

HTTP API space of Kubernetes can be divided into three independent groups:

 - Core Group (/api/v1)
    - This group includes objects such as Pods, Services, nodes, etc.
 - Named Group
    - This group includes objects in **/apis/$NAME/$VERSION** format
    - These different API versions imply different levels of stability and support:
        - Alpha level - it may be dropped at any point in time, without notice. For example, /apis/batch/v2alpha1.
        - Beta level - it is well-tested, but the semantics of objects may change in incompatible ways in a subsequent beta or stable release. 
            - example, /apis/certificates.k8s.io/v1beta1
        - Stable level - appears in released software for many subsequent versions.
            - For example, /apis/networking.k8s.io/v1
 - System-wide
    - This group consists of system-wide API endpoints, like /healthz, /logs, /metrics, /ui, etc.

<h2 id="70becb84ec118d75e27f125448562a2b"></h2>

## kubectl Configuration File

 - To connect to the Kubernetes cluster, kubectl needs the master node endpoint and the credentials to connect to it.
 - On the master node machine, by default, a configuration file, config, inside the.kube directory, which resides in the user's home directory.
 - That configuration file has all the connection details.  
 - To look at the connection details, we can either see the content of the ~/.kube/config(Linux) file, or run the following command:


```
# kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://10.192.83.78:6443
  name: kubernetes
...
```

 - Once kubectl is installed, we can get information about the Minikube cluster with the `kubectl cluster-info` command

```
# kubectl cluster-info
```


<h2 id="6bbde18895b093a1a0fc79b5c02e4462"></h2>

## Kubernetes dashboard 

<h2 id="ae1fd03692378014b99c5c70b6c121af"></h2>

### Deploying the Dashboard UI

```
kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
```

<h2 id="f32d0f539f9fbaff4c670cd2e5d7b14d"></h2>

### Accessing the Dashboard UI

```
kubectl proxy
```

 - Kubectl will make Dashboard available at
    - `http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/`

 - to access the proxy from external browse , try 

```
# kubectl proxy --port=8001 --address='<master.ip.addr>' --accept-hosts="^*$"
Starting to serve on 10.192.83.78:8001
```

 - now access `http://10.192.83.78:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/`
    - PS. it will lead to authoriation problem.

 - for test purpose only , you can Granting admin privileges to Dashboard's Service Account 
    - Afterwards you can use Skip option on login page to access Dashboard.

```
$ cat <<EOF | kubectl create -f -
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard
  labels:
    k8s-app: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubernetes-dashboard
  namespace: kube-system
EOF
```


[more solutions on stackoverflow](https://stackoverflow.com/questions/46664104/how-to-sign-in-kubernetes-dashboard)




<h2 id="d7dba71d2e1aa5aea658e819489eab4d"></h2>

### APIs - with 'kubectl proxy'

 - When kubectl proxy is configured, we can send requests to localhost on the proxy port:
    - With the above curl request, we requested all the API endpoints from the API server.

```
$ curl http://localhost:8001/
{
 "paths": [
   "/api",
   "/api/v1",
   "/apis",
   "/apis/apps",
   ......
   ......
   "/logs",
   "/metrics",
   "/swaggerapi/",
   "/ui/",
   "/version"
 ]
}
```

<h2 id="c4a8eba76a7943e2e98a2e8b0f014db3"></h2>

### APIs - without 'kubectl proxy'

 - Without **kubectl proxy** configured, we can get the **Bearer Token** using kubectl,and then send it with the API request.
 - A **Bearer Token** is an **access token** which is generated by the authentication server(the API server on the master node) and given back to the client. 
 - Using that token, the client can connect back to the Kubernetes API server without providing further authentication details, and then, access resources. 

 - **Get the token**

```
TOKEN=$(kubectl describe secret -n kube-system $(kubectl get secrets -n kube-system | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t' | tr -d " ")
```

 - **Get the API server endpoint**


```
APISERVER=$(kubectl config view | grep https | cut -f 2- -d ":" | tr -d " ")
# echo $APISERVER
https://10.192.83.78:6443
```

 - Access the API Server using the curl command, as shown below

```
curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.192.83.78:6443"
    }
  ]
}
```

# Kubernetes Building Blocks

## Kubernetes Object Model

 - With each object, we declare our intent or desired state using the **spec** field
 - The Kubernetes system manages the **status** field for objects, in which it records the actual state of the object. 
 - To create an object, we need to provide the **spec** field to the Kubernetes API server. 
    - The spec field describes the desired state, along with some basic information, like the name. 
 - Below is an example of a Deployment object:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

 - kind
    - mention the object type
 - metadata
    - attach the basic information to objects, like the name.
 - spec
    - define the desired state of the deployment.
    - You may have noticed that in our example we have two spec fields (spec and spec.template.spec).
    - In our example, we want to make sure that, at any point in time, at least 3 Pods are running, which are created using the Pods Template defined in spec.template.
    - In spec.template.spec, we define the desired state of the Pod.
        - Here, our Pod would be created using nginx:1.7.9.
 - Once the object is created, the Kubernetes system attaches the **status** field to the object; we will explore it later.

## Pods

 - A Pod is the smallest and simplest Kubernetes object.
    - It is the unit of deployment in Kubernetes, which represents a single instance of the application. 
 - A Pod is a logical collection of one or more containers, which:
    - Are scheduled together on the same host
    - Share the same network namespace
    - Mount the same external storage (volumes).

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s_pod.png)

 - Pods do not have the capability to self-heal by themselves. 
    - That is why we use them with controllers, which can handle a Pod's replication, fault tolerance, self-heal, etc. 
    - Examples of controllers are Deployments, ReplicaSets, ReplicationControllers, etc.
 - We attach the Pod's specification to other objects using Pods Templates, as we have seen in the previous section.


## Labels

 - Labels are key-value pairs that can be attached to any Kubernetes objects (e.g. Pods).
 - Labels are used to organize and select a subset of objects, based on the requirements in place.
 - Many objects can have the same Label(s). Labels do not provide uniqueness to objects.  

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s_label.png)

 - In the image above, we have used two Labels: app and env.
    - Based on our requirements, we have given different values to our four Pods.

## Label Selectors

 - With Label Selectors, we can select a subset of objects. 
 - Kubernetes supports two types of Selectors:
    - Equality-Based Selectors
        - allow filtering of objects based on Label keys and values. 
        - With this type of selectors, we can use the =, ==, or != operators. 
        - For example, with env==dev we are selecting the objects where the env Label is set to dev. 
    - Set-Based Selectors
        - allow filtering of objects based on a set of values
        - With this type of Selectors, we can use the in, notin, and exist operators. 
        - For example, with **env in (dev,qa)**, we are selecting objects where the env Label is set to dev or qa. 

## ReplicationControllers

 - A ReplicationController (rc) is a controller that is part of the master node's controller manager. 
 - It makes sure the specified number of replicas for a Pod is running at any given point in time.
 - Generally, we don't deploy a Pod independently, as it would not be able to re-start itself, if something goes wrong. 
 - We always use controllers like ReplicationController to create and manage Pods. 

## ReplicaSets

 - A ReplicaSet (rs) is the next-generation ReplicationController.
 - ReplicaSets support both equality- and set-based selectors, whereas ReplicationControllers only support equality-based Selectors.
    - Currently, this is the only difference.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s_rs.png)

 - ReplicaSets can be used independently, but they are mostly used by Deployments to orchestrate the Pod creation, deletion, and updates. 
 - A Deployment automatically creates the ReplicaSets, and we do not have to worry about managing them. 


## Deployments

 - Deployment objects provide declarative updates to Pods and ReplicaSets.
 - The DeploymentController is part of the master node's controller manager, and it makes sure that the current state always matches the desired state.
 - let's say we have a **Deployment** which creates a **ReplicaSet A**.  **ReplicaSet A** then create **3 Pods**. 
    - In each Pod, one of the containers user the nginx:1.7.9 image.
 - Now, in the Deployment, we change the Pods Template and we update the image for the nginx container from nginx:1.7.9 to nginx:1.9.1.
    - As have modified the Pods Template, a new **ReplicaSet B** gets created. 
    - This process is referred to as a **Deployment rollout**.
 - A rollout is only triggered when we update the Pods Template for a deployment.
    - Operations like scaling the deployment do not trigger the deployment.
 - Once **ReplicaSet B** is ready, the Deployment starts pointing to it.
 - Once ReplicaSet B is ready, the Deployment starts pointing to it,
    - with which, if something goes wrong, we can rollback to a previously known state.

## Namespaces

 - we can partition the Kubernetes cluster into sub-clusters using Namespaces.
 - The names of the resources/objects created inside a Namespace are unique, but not across Namespaces.

```
# kubectl get namespaces
NAME          STATUS   AGE
default       Active   22h
kube-public   Active   22h
kube-system   Active   22h
```

 - Generally, Kubernetes creates two default Namespaces: kube-system and default. 
    - The kube-system Namespace contains the objects created by the Kubernetes system.
    - By default, we connect to the default Namespace.
 - kube-public is a special Namespace, which is readable by all users and used for special purposes, like bootstrapping a cluster. 
 - Using **Resource Quotas**, we can divide the cluster resources within Namespaces. 

# Authentication, Authorization, and Admission Control

## Overview

 - To access and manage any resources/objects in the Kubernetes cluster, we need to access a specific API endpoint on the API server. 
 - Each access request goes through the following three stages:
    - Authentication
        - Logs in a user.
    - Authorization
        - Authorizes the API requests added by the logged-in user.
    - Admission Control
        - Software modules that can modify or reject the requests based on some additional checks, like **Quota**.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s_access_the_API.png)


## Authentication

 - Kubernetes does not have an object called user, nor does it store usernames or other related details in its object store.
 - However, even without that, Kubernetes can use usernames for access control and request logging.
 - Kubernetes has two kinds of users:
    - Normal Users
        - They are managed outside of the Kubernetes cluster via independent services like User/Client Certificates, a file listing usernames/passwords, etc.
    - Service Accounts
        - With Service Account users, in-cluster processes communicate with the API server to perform different operations.
        - Most of the Service Account users are created automatically via the API server, but they can also be created manually. 
        - The Service Account users are tied to a given Namespace and mount the respective credentials to communicate with the API server as Secrets.
 - If properly configured, Kubernetes can also support **anonymous requests**, along with requests from Normal Users and Service Accounts.
 - For authentication, Kubernetes uses different authenticator modules:
    - Client Certificates
        - need to reference a file containing one or more certificate authorities by passing the **--client-ca-file=SOMEFILE** option to the API server. 
    - Static Token File
        - pass a file containing pre-defined bearer tokens with the **--token-auth-file=SOMEFILE** option to the API server. 
        - Currently, these tokens would last indefinitely, and they cannot be changed without restarting the API server.
    - Bootstrap Tokens
        - currently in an alpha statu
    - Static Password File
        - It is similar to Static Token File
        - pass a file containing basic authentication details with the **--basic-auth-file=SOMEFILE** option.
    - Service Account Tokens
        - This is an automatically enabled authenticator that uses signed bearer tokens to verify the requests. 
        - These tokens get attached to Pods using the ServiceAccount Admission Controller, which allows in-cluster processes to talk to the API server.
    - OpenID Connect Tokens
        - OpenID Connect helps us connect with OAuth 2 providers, such as Azure Active Directory, Salesforce, Google, etc., to offload the authentication to external services.
    - Webhook Token Authentication
        - With Webhook-based authentication, verification of bearer tokens can be offloaded to a remote service.
    - Keystone Password
        - Keystone authentication can be enabled by passing the **--experimental-keystone-url=<AuthURL> option** to the API server, where AuthURL is the Keystone server endpoint.
    - Authenticating Proxy
        - If we want to program additional authentication logic, we can use an authenticating proxy. 

 - We can enable multiple authenticators,
    - In order to be successful, you should enable at least two methods: the service account tokens authenticator and the user authenticator.

## Authorization

 - After a successful authentication, users can send the API requests to perform different operations.
 - Then, those API requests get authorized by Kubernetes using various authorization modules.
 - Some of the API request attributes that are reviewed by Kubernetes include user, group, extra, Resource or Namespace, to name a few.
    - Next, these attributes are evaluated against policies. 
    - If the evaluation is successful, then the request will be allowed, otherwise it will get denied. 
 - Similar to the Authentication step, Authorization has multiple modules/authorizers.

 - Authorization modules
    - Node Authorizer
        - Node authorization is a special-purpose authorization mode which specifically authorizes API requests made by kubelets.
        - It authorizes the kubelet's read operations for services, endpoints, nodes, etc., and writes operations for nodes, pods, events, etc. 
    - Attribute-Based Access Control (ABAC) Authorizer
        - With the ABAC authorizer, Kubernetes grants access to API requests, which combine policies with  attributes.
        - In the following example, user nkhare can only read Pods in the Namespace lfs158.
        - 
        ```
        {
          "apiVersion": "abac.authorization.kubernetes.io/v1beta1",
          "kind": "Policy",
          "spec": {
            "user": "nkhare",
            "namespace": "lfs158",
            "resource": "pods",
            "readonly": true
          }
        }
        ```

        - To enable the ABAC authorizer, we would need to start the API server with the **--authorization-mode=ABAC** option.
        - We would also need to specify the authorization policy, like **--authorization-policy-file=PolicyFile.json**
    - Webhook Authorizer
        - With the Webhook authorizer, Kubernetes can offer authorization decisions to some third-party services, which would return true for successful authorization, and false for failure. 
        - In order to enable the Webhook authorizer, we need to start the API server with the **--authorization-webhook-config-file=SOME_FILENAME** option, where SOME_FILENAME is the configuration of the remote authorization service. 
    - Role-Based Access Control (RBAC) Authorizer
        - 使用RBAC，我们可以根据各个用户的角色来规范对资源的访问。
        - In Kubernetes, we can have different roles that can be attached to subjects like users, service accounts, etc. 
        - While creating the roles, we restrict resource access by specific operations, such as create, get, update, patch, etc.
        - In RBAC, we can create two kinds of roles:
            - Role  -- With Role, we can grant access to resources within a specific Namespace.
            - ClusterRole  -- The ClusterRole can be used to grant the same permissions as Role does, but its scope is cluster-wide.
        - 
        ```
        kind: Role
        apiVersion: rbac.authorization.k8s.io/v1
        metadata:
          namespace: lfs158
          name: pod-reader
        rules:
        ~ apiGroups: [""] # "" indicates the core API group, ~ should be -
          resources: ["pods"]
          verbs: ["get", "watch", "list"]
        ```

        - Above example creates a pod-reader role, which has access only to the Pods of lfs158 Namespace.
        - Once the role is created, we can bind users with RoleBinding.
        - There are two kinds of RoleBindings:         
            - RoleBinding
                - It allows us to bind users to the same namespace as a Role 
            - ClusterRoleBinding
                - It allows us to grant access to resources at a cluster-level and to all Namespaces.
        - 
        ```
        kind: RoleBinding
        apiVersion: rbac.authorization.k8s.io/v1
        metadata:
          name: pod-read-access
          namespace: lfs158
        subjects:
        ~ kind: User  # ~ should be -
          name: nkhare
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: pod-reader
          apiGroup: rbac.authorization.k8s.io
        ```

        - see above example,  it gives access to nkhare to read the Pods of lfs158 Namespace.
        - To enable the RBAC authorizer, we would need to start the API server with the **--authorization-mode=RBAC** option. 
        - With the RBAC authorizer, we dynamically configure policies. 


## Admission Control

 - Admission control is used to specify granular access control policies, which include allowing privileged containers, checking on resource quota, etc.
 - We force these policies using different admission controllers, like ResourceQuota, AlwaysAdmit, DefaultStorageClass, etc. 
 - To use admission controls, we must start the Kubernetes API server with the admission-control

```
--admission-control=NamespaceLifecycle,ResourceQuota,PodSecurityPolicy,DefaultStorageClass.
```

 - By default, Kubernetes comes with some built-in admission controllers.

# Service

## Connecting Users to Pods

 - To access the application, a user/client needs to connect to the Pods
 - Kubernetes provides a higher-level abstraction called Service, which logically groups Pods and a policy to access them. 
    - This grouping is achieved via Labels and Selectors, which we talked about in the previous chapter. 
 - We can assign a name to the logical grouping, referred to as a **Service name**. 

## Service Object Example

 - The following is an example of a Service object:

```
kind: Service
apiVersion: v1
metadata:
  name: frontend-svc
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
```

 - In this example, we are creating a **frontend-svc** Service by selecting all the Pods that have the Label **app** set to the **frontend**.
 - By default, each Service also gets an IP address, which is routable only inside the cluster. 
    - The IP address attached to each Service is also known as the ClusterIP for that Service.
 - The user/client now connects to a service via the IP address, which forwards the traffic to one of the Pods attached to it.
    - A service does the load balancing while selecting the Pods for forwarding the data/traffic.
 - While forwarding the traffic from the Service, we can select the target port on the Pod.
    - for example, for frontend-svc, we will receive requests on Port 80.  We will then forward these requests to one of the attached Pods on Port 5000. 
    - If the target port is not defined explicitly, then traffic will be forwarded to Pods on the port on which the Service receives traffic.

## kube-proxy

 - All of the worker nodes run a daemon called kube-proxy, which watches the API server on the master node for the addition and removal of Services and endpoints. 
 - For each new Service, on each node, kube-proxy configures the iptables rules to capture the traffic for its ClusterIP and forwards it to one of the endpoints.
 - When the service is removed, kube-proxy removes the iptables rules on all nodes as well.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s-kube-proxy-svc-endpoint.png)


## Service Discovery

As Services are the primary mode of communication in Kubernetes, we need a way to discover them at runtime. 

Kubernetes supports two methods of discovering a Service:

 - Environment Variables
    - As soon as the Pod starts on any worker node, the kubelet daemon running on that node adds a set of environment variables in the Pod for all active Services.
    - For example, if we have an active Service called redis-master, which exposes port 6379, and its ClusterIP is 172.17.0.6, then, on a newly created Pod, we can see the following environment variables:
    - 
    ```
    REDIS_MASTER_SERVICE_HOST=172.17.0.6
    REDIS_MASTER_SERVICE_PORT=6379
    REDIS_MASTER_PORT=tcp://172.17.0.6:6379
    REDIS_MASTER_PORT_6379_TCP=tcp://172.17.0.6:6379
    REDIS_MASTER_PORT_6379_TCP_PROTO=tcp
    REDIS_MASTER_PORT_6379_TCP_PORT=6379
    REDIS_MASTER_PORT_6379_TCP_ADDR=172.17.0.6
    ```

 - DNS
    - Kubernetes has an add-on for DNS, which creates a DNS record for each Service and its format is like my-svc.my-namespace.svc.cluster.local
    - **Services within the same Namespace can reach to other Services with just their name.**
    - For example, if we add a Service redis-master in the **my-ns** Namespace, then all the Pods in the same Namespace can reach to the redis Service just by using its name, **redis-master**. 
    - Pods from other Namespaces can reach the Service by adding the respective Namespace as a `suffix`, like **redis-master.my-ns**. 
    - This is the most common and highly recommended solution. 

        
## ServiceType

 - While defining a Service, we can also choose its access scope.
 - We can decide whether the Service:
    - Is only accessible within the cluster
    - Is accessible from within the cluster and the external world
    - Maps to an external entity which resides outside the cluster.
 - Access scope is decided by `ServiceType`, which can be mentioned when creating the Service.

### ServiceType: ClusterIP and NodePort

 - ClusterIP is the default ServiceType. 
    - A Service gets its Virtual IP address using the ClusterIP. 
    - That IP address is used for communicating with the Service and is accessible only within the cluster. 
 - With the NodePort ServiceType, in addition to creating a ClusterIP, a port from the range 30000-32767 is mapped to the respective Service, from all the worker nodes.
    - For example, if the mapped NodePort is `32233` for the service frontend-svc, then, if we connect to any worker node on port 32233, the node would redirect all the traffic to the assigned ClusterIP - 172.17.0.4.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s-NodePort.png)

 - The NodePort ServiceType is useful when we want to make our Services accessible from the external world.
 - The end-user connects to the worker nodes on the specified port, which forwards the traffic to the applications running inside the cluster.
 - To access the application from the external world, administrators can configure a reverse proxy outside the Kubernetes cluster and map the specific endpoint to the respective port on the worker nodes. 


### ServiceType: LoadBalancer

 - With the LoadBalancer ServiceType:
    - NodePort and ClusterIP Services are automatically created, and the external load balancer will route to them
    - The Services are exposed at a static port on each worker node
    - The Service is exposed externally using the underlying cloud provider's load balancer feature.
 - The LoadBalancer ServiceType will only work if the underlying infrastructure supports the automatic creation of Load Balancers and have the respective support in Kubernetes, as is the case with the Google Cloud Platform and AWS. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s-svc-lb.png)


# Deploying an Application

## Deploy vi kubectl

### List the Pods, along with their attached Labels

```
$ kubectl get pods -L k8s-app,label2
NAME                         READY   STATUS    RESTARTS   AGE   K8S-APP     LABEL2
webserver-74d8bd488f-dwbzz   1/1     Running   0          14m   webserver   <none>
webserver-74d8bd488f-npkzv   1/1     Running   0          14m   webserver   <none>
webserver-74d8bd488f-wvmpq   1/1     Running   0          14m   webserver   <none>
```

### Select the Pods with a given Label

```
$ kubectl get pods -l k8s-app=webserver
NAME                         READY     STATUS    RESTARTS   AGE
webserver-74d8bd488f-dwbzz   1/1       Running   0          17m
webserver-74d8bd488f-npkzv   1/1       Running   0          19m
webserver-74d8bd488f-wvmpq   1/1       Running   0          17m

$ kubectl get pods -l k8s-app=webserver1
No resources found.
```

### Delete the Deployment 

```
$ kubectl delete deployments webserver
deployment "webserver" deleted
```

 - Deleting a Deployment also deletes the ReplicaSets and the Pods we created:

```
$ kubectl get replicasets
No resources found.

$ kubectl get pods
No resources found.
```

### Create a YAML file with Deployment details

 - Let us now create the webserver.yaml file with the following content:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webserver
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
```


```
$ kubectl create -f webserver.yaml
deployment "webserver" created
```

 - we can also name a port  , it can be be using the referenced web-port name while creating the Service 

```
        ports:
        - containerPort: 5000
          name: web-port
```

### Creating a Service and Exposing It to the External World with NodePort I

 - with the **NodePort**  ServiceType, Kubernetes opens up a static port on all the worker nodes. I
 - If we connect to that port from any node, we are forwarded to the respective Service.
 - Create a webserver-svc.yaml file with the following content:

```
apiVersion: v1
kind: Service
metadata:
  name: web-service
  labels:
    run: web-service
spec:
  type: NodePort
  ports:
  - port: 80
    protocol: TCP
  selector:
    app: nginx
```

```
$ kubectl create -f webserver-svc.yaml
service/web-service created

$ kubectl get svc
NAME          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes    ClusterIP   10.96.0.1      <none>        443/TCP        1d
web-service   NodePort    10.110.47.84   <none>        80:31074/TCP   12s
```

 - Our web-service is now created and its ClusterIP is 10.110.47.84.
 - In the PORT(S)section, we can see a mapping of 80:31074,
    - which means that we have reserved a static port 31074 on the node
    - If we connect to the node on that port, our requests will be forwarded to the ClusterIP on port 80.
 - It is not necessary to create the Deployment first, and the Service after. They can be created in any order. 
 - A Service will connect Pods based on the Selector.


```
$ kubectl describe svc web-service
Name:                     web-service
Namespace:                default
Labels:                   run=web-service
Annotations:              <none>
Selector:                 app=nginx
Type:                     NodePort
IP:                       10.110.47.84
Port:                     <unset>  80/TCP
TargetPort:               80/TCP
NodePort:                 <unset>  31074/TCP
Endpoints:                172.17.0.4:80,172.17.0.5:80,172.17.0.6:80
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

## Liveness and Readiness Probes

 - These probes are very important, because they allow the kubelet to control the health of the application running inside a Pod's container.

### Liveness

 - If a container in the Pod is running, but the application running inside this container is not responding to our requests, then that container is of no use to us. 
    - This kind of situation can occur, for example, due to application deadlock or memory pressure.
    - In such a case, it is recommended to restart the container to make the application available.
 - Rather than doing it manually, we can use **Liveness Probe**.
    - Liveness probe checks on an application's health, and, if for some reason, the health check fails, it restarts the affected container automatically.
 - Liveness Probes can be set by defining:
    - Liveness command
    - Liveness HTTP request
    - TCP Liveness Probe.

#### Liveness Command

 - In the following example, we are checking the existence of a file /tmp/healthy:

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: liveness
  name: liveness-exec
spec:
  containers:
  - name: liveness
    image: k8s.gcr.io/busybox
    args:
    - /bin/sh
    - -c
    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 3
      periodSeconds: 5
```
 
 - The existence of the **/tmp/healthy** file is configured to be checked every 5 seconds using the **periodSeconds** parameter. 
 - The **initialDelaySeconds** parameter requests the kubelet to wait for 3 seconds before doing the first probe. 
 - When running the container, we will first create the /tmp/healthy file, and then we will remove it after 30 seconds. 
    -  The deletion of the file would trigger a health failure, and our Pod would get restarted.


### Liveness HTTP Request

 - In the following example, the kubelet sends the HTTP GET request to the /healthz endpoint of the application, on port 8080. 
 - If that returns a failure, then the kubelet will restart the affected container; otherwise, it would consider the application to be alive.

```
livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
        httpHeaders:
        - name: X-Custom-Header
          value: Awesome
      initialDelaySeconds: 3
      periodSeconds: 3
```

### TCP Liveness Probe

 - With TCP Liveness Probe, the kubelet attempts to open the TCP Socket to the container which is running the application. 
 - If it succeeds, the application is considered healthy, otherwise the kubelet would mark it as unhealthy and restart the affected container.

```
livenessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
```


## Readiness Probes

 - Sometimes, applications have to meet certain conditions before they can serve traffic. 
 - These conditions include 
    - ensuring that the depending service is ready,
    - or acknowledging that a large dataset needs to be loaded, etc.
 - In such cases, we use Readiness Probes and wait for a certain condition to occur. Only then, the application can serve traffic.
 - A Pod with containers that do not report ready status will not receive traffic from Kubernetes Services.

```
readinessProbe:
  exec:
    command:
    - cat
    - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```

 - Readiness Probes are configured similarly to Liveness Probes. Their configuration also remains the same.


# Kubernetes Volume Management  

 - To back a Pod with a persistent storage, Kubernetes uses **Volumes**. 

## Volumes

 - containers, which create the Pods, are ephemeral in nature.
    - All data stored inside a container is deleted if the container crashes.
    - However, the kubelet will restart it with a clean state, which means that it will not have any of the old data.
 - To overcome this problem, Kubernetes uses Volumes. 
    - A Volume is essentially a directory backed by a storage medium. 
    - The storage medium and its content are determined by the Volume Type.
 - In Kubernetes, a Volume is attached to a Pod and shared among the containers of **that Pod**.
    - The Volume has the same life span as the **Pod**,  and it outlives the containers of the Pod 
        - this allows data to be preserved across container restarts.

## Volume Types

 - A directory which is mounted inside a Pod is backed by the underlying Volume Type.
 - A Volume Type decides the properties of the directory, like size, content, etc. Some examples of Volume Types are:
    - emptyDir
        - An empty Volume is created for the Pod as soon as it is scheduled on the worker node. The Volume's life is tightly coupled with the Pod. If the Pod dies, the content of emptyDir is deleted forever.  
    - hostPath
        - With the hostPath Volume Type, we can share a directory from the host to the Pod. 
        - If the Pod dies, the content of the Volume is still available on the host.
    - gcePersistentDisk
        - we can mount a Google Compute Engine (GCE) persistent disk into a Pod.
    - awsElasticBlockStore
        - we can mount an AWS EBS Volume into a Pod. 
    - nfs
        - we can mount an NFS share into a Pod.
    - iscsi
        - we can mount an iSCSI share into a Pod.
    - secret
        - With the secret Volume Type, we can pass sensitive information, such as passwords, to Pods.
    - persistentVolumeClaim
        - We can attach a PersistentVolume to a Pod.


## PersistentVolumes

 - A Persistent Volume is a network-attached storage in the cluster, which is provisioned by the administrator.
 - PersistentVolumes can be dynamically provisioned based on the StorageClass resource. 
    - A StorageClass contains pre-defined provisioners and parameters to create a PersistentVolume
    - Using PersistentVolumeClaims, a user sends the request for dynamic PV creation, which gets wired to the StorageClass resource.
 - Some of the Volume Types that support managing storage using PersistentVolumes are:
    - GCEPersistentDisk
    - AWSElasticBlockStore
    - AzureFile
    - NFS
    - iSCSI

## PersistentVolumeClaims

 - A PersistentVolumeClaim (PVC) is a request for storage by a user. 
    - Users request for PersistentVolume resources based on size, access modes, etc. 
    - Once a suitable PersistentVolume is found, it is bound to a PersistentVolumeClaim.
 - After a successful bound, the PersistentVolumeClaim resource can be used in a Pod.
 - Once a user finishes its work, the attached PersistentVolumes can be released. The underlying PersistentVolumes can then be reclaimed and recycled for future usage. 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/k8s-pvc.png)



# ConfigMaps and Secrets

 - While deploying an application, we may need to pass such runtime parameters like configuration details, passwords, etc. 
 - In such cases, we can use the ConfigMap API resource.
 - Similarly, when we want to pass sensitive information, we can use the Secret API resource.

## ConfigMaps

 - ConfigMaps allow us to decouple the configuration details from the container image.
 - Using ConfigMaps, we can pass configuration details as key-value pairs, which can be later consumed by Pods, or any other system components, such as controllers. 
 - We can create ConfigMaps in two ways:
    - From literal values
    - From files.

### Create a ConfigMap from Literal Values and Get Its Details

```
$ kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
configmap "my-config" created
```

```
$ kubectl get configmaps my-config -o yaml
apiVersion: v1
data:
  key1: value1
  key2: value2
kind: ConfigMap
metadata:
  creationTimestamp: 2017-05-31T07:21:55Z
  name: my-config
  namespace: default
  resourceVersion: "241345"
  selfLink: /api/v1/namespaces/default/configmaps/my-config
  uid: d35f0a3d-45d1-11e7-9e62-080027a46057
```

### Create a ConfigMap from a Configuration File

 - First, we need to create a configuration file.

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: customer1
data:
  TEXT1: Customer1_Company
  TEXT2: Welcomes You
  COMPANY: Customer1 Company Technology Pct. Ltd.
```

```
$ kubectl create -f customer1-configmap.yaml
configmap "customer1" created
```


### Use ConfigMap Inside Pods




