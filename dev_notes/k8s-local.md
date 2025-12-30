[](...menustart)

- [Work With Local k8s](#b12bf4d31f18ea1cf240df43682ed0b5)
    - [install kind k8s](#e629a5281ed6903f92a461cc54e08857)
    - [Install ingress controller](#588da1e7cecfc3f40fa3e015ff722499)
    - [Install Dashboard](#5633d2848d737c44ec1d89bc54ccdfa9)
    - [metrics server](#5be52954321051abb86007a11a9a0b17)

[](...menuend)


<h2 id="b12bf4d31f18ea1cf240df43682ed0b5"></h2>

# Work With Local k8s


<h2 id="e629a5281ed6903f92a461cc54e08857"></h2>

## install kind k8s

- install kubectl...
    - https://github.com/kubernetes-sigs/kind/releases
    ```bash
    $ curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.24.0/kind-$(uname)-amd64
    $ chmod +x ./kind
    $ sudo mv ./kind /usr/local/bin/


    ```

<details>
<summary>
<b>QuickStart: Create a simple kind cluster with extraPortMappings and node-labels.</b>
</summary>

- create cluster
    - extraPortMappings allow the local host to make requests to the Ingress controller over ports 80/443
    - node-labels only allow the ingress controller to run on a specific node(s) matching the label selector
    - before creating a cluster, please check your proxy setting
    ```bash
    cat <<EOF | kind create cluster --name wslk8s  --config=-
    kind: Cluster
    apiVersion: kind.x-k8s.io/v1alpha4
    nodes:
    - role: control-plane
      kubeadmConfigPatches:
      - |
        kind: InitConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            node-labels: "ingress-ready=true"
      extraPortMappings:
      - containerPort: 80
        hostPort: 80
        protocol: TCP
      - containerPort: 443
        hostPort: 443
        protocol: TCP
      extraMounts:
      - hostPath: /home/<user-name>/www
        containerPath: /www
    EOF
    ```
    - extraMounts may be used to mount a host directory into the container
    - **NOTE**: you can NOT use a loopback proxy, e.g. '127.0.0.1:3128' for kind, it will result `ErrImagePull` when creating pod containers. You must use a dedicated proxy for kind, e.g. '
        ```bash
        export HTTP_PROXY=http://xxx-proxy:3128 && export HTTPS_PROXY=$HTTP_PROXY && export NO_PROXY="localhost, 127.0.0.*, 172.17.*" && export http_proxy=$HTTP_PROXY && export https_proxy=$HTTPS_PROXY && export no_proxy=$NO_PROXY && cat <<EOF | kind create cluster ...
        ```
        - check proxy setting
            ```bash
            # wslk8s-control-plane is the name of kind node container
            $ docker inspect wslk8s-control-plane | grep -i proxy
            ```
- test whether it works...
    ```bash
    $ kubectl cluster-info
    Kubernetes control plane is running at https://127.0.0.1:35537
    CoreDNS is running at https://127.0.0.1:35537/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    ```

或者使用 配置 kind-proxy-mirror.yaml

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4

nodes:
  - role: control-plane
    kubeadmConfigPatches:
      - |
        kind: InitConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            node-ip: "127.0.0.1"

    extraMounts:
      - hostPath: /etc/hosts
        containerPath: /etc/hosts

containerdConfigPatches:
  - |
    [plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
      endpoint = [
        "https://docker.m.daocloud.io",
        "https://dockerproxy.com",
        "https://docker.nju.edu.cn",
        "https://docker.mirrors.ustc.edu.cn"
      ]

```

kind create cluster --config kind-proxy-mirror.yaml

</details>


<details>
<summary>
<b>Advanced: create a kind cluster with ingress & local registry enabled</b>
</summary>

```bash

#!/bin/sh
set -o errexit

# with cluster name:
#   --name wslk8s
# with register name:
#   kind-registry
# with register port:
#   5050
# with ingress enable


# create registry container unless it already exists
reg_name='kind-registry'
reg_host="<TODO: your reg host>"
reg_port='5050'
if [ "$(docker inspect -f '{{.State.Running}}' "${reg_name}" 2>/dev/null || true)" != 'true' ]; then
  docker run \
    -d --restart=always -p "${reg_port}:5000" --name "${reg_name}" \
    registry:2
fi

# create a cluster with the local registry enabled in containerd
cat <<EOF | kind create cluster --name wslk8s  --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
containerdConfigPatches:
- |-
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."${reg_host}:${reg_port}"]
    endpoint = ["http://${reg_host}:${reg_port}"]

nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP

EOF

# connect the registry to the cluster network if not already connected
if [ "$(docker inspect -f='{{json .NetworkSettings.Networks.kind}}' "${reg_name}")" = 'null' ]; then
  docker network connect "kind" "${reg_name}"
fi

# Document the local registry
# https://github.com/kubernetes/enhancements/tree/master/keps/sig-cluster-lifecycle/generic/1755-communicating-a-local-registry
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: local-registry-hosting
  namespace: kube-public
data:
  localRegistryHosting.v1: |
    host: "${reg_host}:${reg_port}"
    help: "https://kind.sigs.k8s.io/docs/user/local-registry/"
EOF
```

</details>




<h2 id="588da1e7cecfc3f40fa3e015ff722499"></h2>

## Install ingress controller 

Ingress controller is a service which type is `LoadBalancer`. It is also another set of pods that run on your nodes in your k8s cluster, and thus evaluation and processing of ingress routes.

- evaluates all the rules
- manages redirections
- entrypoint to cluster
- many third-party implementations
    - there is one from kubernetes itself which is `K8s nginx ingress controller`
    - if you are using a cloud service, you would have a cloud load balancer that is specifically implemented by that cloud provider.


```bash
# specific version
# kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.2/deploy/static/provider/cloud/deploy.yaml

# latest version
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

```

You will notice that ingress-nginx-controller listening port has been changed

```bash
$ kubectl get svc -A
NAMESPACE       NAME                                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                           AGE
ingress-nginx   ingress-nginx-controller             LoadBalancer   10.108.84.93    localhost     80:31402/TCP,443:32053/TCP   20s
```

wait ingress-nginx-controller to be running.

```bash
$ kubectl get po -n ingress-nginx
NAME                                       READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-sxwsg       0/1     Completed   0          51s
ingress-nginx-admission-patch-b85nx        0/1     Completed   1          50s
ingress-nginx-controller-b6cb664bc-tnzbm   1/1     Running     0          51s
```


Here is a [simple sample](http://threelambda.com/2020/07/06/run-ingress-example-on-mac/) to test ingress on Mac OSX docker desktop.


<details>
<summary>
apple.yaml
</summary>

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: apple-app
  labels:
    app: apple
spec:
  containers:
    - name: apple-app
      image: hashicorp/http-echo
      args:
        - "-text=apple"

---

kind: Service
apiVersion: v1
metadata:
  name: apple-service
spec:
  selector:
    app: apple
  ports:
    - port: 5678 # Default port for image
```

</details>


<details>
<summary>
banana.yaml
</summary>

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: banana-app
  labels:
    app: banana
spec:
  containers:
    - name: banana-app
      image: hashicorp/http-echo
      args:
        - "-text=banana"

---

kind: Service
apiVersion: v1
metadata:
  name: banana-service
spec:
  selector:
    app: banana
  ports:
    - port: 5678 # Default port for image
```

</details>


<details>
<summary>
ingress.yaml
</summary>


```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    # kubernetes.io/ingress.class: "nginx"
spec:
  rules:
    - host: 
      http:
        paths:
          - path: /apple
            pathType: Prefix
            backend:
              service:
                name: apple-service
                port:
                  number: 5678
          - path: /banana
            pathType: Prefix
            backend:
              service:
                name: banana-service
                port:
                  number: 5678
```

</details>

To check whether your ingress have got address.

```bash
$ kubectl get ingress -A
NAMESPACE     NAME                  CLASS    HOSTS              ADDRESS     PORTS   AGE
default       example-ingress       <none>   *                  localhost   80      4m17s

$ curl localhost/apple  
apple
```

if your ingress's ADDRESS column is empty, you can use following command to debug

```bash
$ kubectl describe ingress example-ingress
Name:             example-ingress
Namespace:        default
Address:          localhost
Default backend:  default-http-backend:80 (<error: endpoints "default-http-backend" not found>)
Rules:
  Host        Path  Backends
  ----        ----  --------
  *
              /apple    apple-service:5678 (10.1.0.17:5678)
              /banana   banana-service:5678 (10.1.0.18:5678)
Annotations:  ingress.kubernetes.io/rewrite-target: /
              kubernetes.io/ingress.class: nginx
Events:
  Type    Reason  Age               From                      Message
  ----    ------  ----              ----                      -------
  Normal  Sync    91s (x2 over 2m)  nginx-ingress-controller  Scheduled for sync
```

```bash
$ kubectl -n ingress-nginx logs ingress-nginx-controller-xxxxx
...
I0325 07:01:02.452984       8 status.go:299] "updating Ingress status" namespace="default" ingress="example-ingress" currentValue=[] newValue=[{IP: Hostname:localhost Ports:[]}]
I0325 07:01:02.461367       8 event.go:282] Event(v1.ObjectReference{Kind:"Ingress", Namespace:"default", Name:"example-ingress", UID:"e1b49b5e-c5a0-49a0-8e2a-64dd36820261", APIVersion:"networking.k8s.io/v1", ResourceVersion:"296455", FieldPath:""}): type: 'Normal' reason: 'Sync' Scheduled for sync
```


**PS. Do NOT add ANNOTATIONS that are not recognized by ingress nginx !! e.g. aws alb annotations**


---

route with specific host sample:


<details>
<summary>
ingress with specified host
</summary>

```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: {name}-ingress-443
  spec:
    rules:
    - host: dot-iap-dev.imac
      http:
        paths:
          - pathType: Prefix
            path: /
            backend:
              service:
                name: {name}
                port:
                  number: {port}             

```

</details>

```bash
$ kubectl get ingress -A
NAMESPACE     NAME                  CLASS    HOSTS              ADDRESS     PORTS   AGE
umc-dot-dev   dot-iap-ingress-443   <none>   dot-iap-dev.imac   localhost   80      28m

$ curl localhost
$ curl dot-iap-dev.imac
ok
$ curl localhost
404 Not Found
# because ingress host is `dot-iap-dev.imac`
#     so we need specify that host in request headers
$ curl -H "host: dot-iap-dev.imac" localhost
ok
```

<h2 id="5633d2848d737c44ec1d89bc54ccdfa9"></h2>

## Install Dashboard

NOTE: **As of version 7.0.0, we have dropped support for Manifest-based installation. Only Helm-based installation is supported now.**

- install dash board
    ```bash
    # check https://github.com/kubernetes/dashboard
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.0/aio/deploy/recommended.yaml
    ```
- helm install
    - `helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/`
    - `helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard`
    - `kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443`
- create a simple user
    - Creating a Service Account
        ```yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: admin-user
          namespace: kubernetes-dashboard
        ```
    - Creating a ClusterRoleBinding
        ```yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          name: admin-user
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: cluster-admin
        subjects:
        - kind: ServiceAccount
          name: admin-user
          namespace: kubernetes-dashboard
        ```
    - Getting a Bearer Token
        ```bash
        $ kubectl -n kubernetes-dashboard create token admin-user --duration=10000h
        eyJhbGciOiJSUzI1NiIsImtpZCI...
        ```


- [dashboard url](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login)


- to allow access from remote machine
    1. if you can successfully access cluster via kubectl
        - `kubectl proxy`
    2. otherwise, you can use ssh tunnel
        - on your workstation, create a tunnel to k8s server
            ```bash
            ssh -L 9999:127.0.0.1:8001 -N -f -l <ssh user name> <k8s master host name or ip>
            ```
        - repalce 8001 to 9999
            - http://localhost:9999/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login

- remote tunnels you maybe use...
    ```bash
    # tunnel 1, access k8s dashboard , 9999 -> 8001, dashboard port
    loc_port=9999
    ret=`lsof -i:$loc_port`
    if [ -z "$ret" ]
    then
        # run in background is not necessary
        nohup ssh -p 2222 -L $loc_port:127.0.0.1:8001 -N -f -l <ssh user> <ssh host> &> /dev/null
    fi

    sleep 1

    # tunnel 2, access kubectl,  9998 -> api server port
    loc_port=9998
    ret=`lsof -i:$loc_port`
    if [ -z "$ret" ]
    then
        # run in background is not necessary
        nohup ssh -p 2222 -L $loc_port:127.0.0.1:45933 -N -f -l <ssh user> <ssh host> &> /dev/null
    fi
    ```

<h2 id="5be52954321051abb86007a11a9a0b17"></h2>

## metrics server 

https://github.com/kubernetes-sigs/metrics-server

```bash
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
# high available version if you have a cluster with at least 2 nodes 
# wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability-1.21+.yaml
```

add `- --kubelet-insecure-tls` to container args

```bash
kubectl apply -f components.yaml
```
