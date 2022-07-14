...menustart

- [K8s Key Ideas](#9f28f0f9d5bb54ce31695aa4c3a8afbf)
    - [Learn Kubernetes Basics](#d6241ba7176a22c6f5508a221d1716b7)
    - [Using a Service to Expose Your App](#6b755767754f0bdf07e6cc0138438cbf)
    - [Scale Your App](#9ed959ed9324ef3c3af26b8fd76e65c6)
    - [Update Your App](#77246ae2f33852920cb5d43806f8027f)

...menuend


<h2 id="9f28f0f9d5bb54ce31695aa4c3a8afbf"></h2>


# K8s Key Ideas

<h2 id="d6241ba7176a22c6f5508a221d1716b7"></h2>


## Learn Kubernetes Basics

- Cluster Diagram
    - ![](https://d33wubrfki0l68.cloudfront.net/152c845f25df8e69dd24dd7b0836a289747e258a/4a1d2/docs/tutorials/kubernetes-basics/public/images/module_02_first_app.svg)

- access API server through kubectl proxy.
    ```bash
    $ curl http://localhost:8001/api/v1/namespaces/$NAMESPACE/pods/$POD_NAME/proxy/
    Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-5c69669756-jwzln | v=1
    ```
- Nodes
    - ![](https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg)

<h2 id="6b755767754f0bdf07e6cc0138438cbf"></h2>


## Using a Service to Expose Your App

- Services allow your applications to receive traffic. 
- Services can be exposed in different ways by specifying a **type** in the ServiceSpec:
    - ClusterIP (default) 
    - NodePort 
    - LoadBalancer
    - ExternalName
    - ![](https://d33wubrfki0l68.cloudfront.net/cc38b0f3c0fd94e66495e3a4198f2096cdecd3d5/ace10/docs/tutorials/kubernetes-basics/public/images/module_04_services.svg)
- A Service routes traffic across a set of Pods.
    - Services match a set of Pods using labels and selectors
    - ![](https://d33wubrfki0l68.cloudfront.net/b964c59cdc1979dd4e1904c25f43745564ef6bee/f3351/docs/tutorials/kubernetes-basics/public/images/module_04_labels.svg)
 


<h2 id="9ed959ed9324ef3c3af26b8fd76e65c6"></h2>


## Scale Your App 

```bash
$ kubectl scale deployments/kubernetes-bootcamp --replicas=4
deployment.extensions/kubernetes-bootcamp scaled
$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   4         4         4            4           1m
```


<h2 id="77246ae2f33852920cb5d43806f8027f"></h2>


## Update Your App

```bash
$ kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2
deployment.extensions/kubernetes-bootcamp image updated

$ kubectl rollout status deployments/kubernetes-bootcamp
deployment "kubernetes-bootcamp" successfully rolled out
```

- Rollback an update

```bash
$ kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
deployment.extensions/kubernetes-bootcamp image updated
$ kubectl rollout undo deployments/kubernetes-bootcamp
deployment.extensions/kubernetes-bootcamp
```

