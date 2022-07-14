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


# K8s Key Ideas

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
 


## Scale Your App 

```bash
$ kubectl scale deployments/kubernetes-bootcamp --replicas=4
deployment.extensions/kubernetes-bootcamp scaled
$ kubectl get deployments
NAME                  DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   4         4         4            4           1m
```


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

