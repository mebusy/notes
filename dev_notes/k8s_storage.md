[](...menustart)

- [K8s Storage](#4a33fe904326d6f56ec74b22f13145a1)
    - [Volumns](#4ce59818ee682136129b1f122cee6573)
        - [emptyDir](#77ea5ef86c2c650eb37fa7374f084bbc)
        - [configMap](#5eeadeea1e2bd82727f9a220408a5f2a)
        - [hostPath](#f1e81401ee0afe2275193298ef588120)
    - [Persistent Volume](#dc1691844d1fa3602f797857ca2f638b)
        - [Create a PersistentVolume](#7a25b4411e122cd14b3d7150ddd960da)
        - [Create a PersistentVolumeClaim](#f720852f4291583f90ac6c9ca381d279)
        - [Create a Pod](#0adc8bf342f1769161c24a88adfe4ff3)

[](...menuend)


<h2 id="4a33fe904326d6f56ec74b22f13145a1"></h2>

# K8s Storage

<h2 id="4ce59818ee682136129b1f122cee6573"></h2>

## Volumns

- A Container's file system lives only as long as the Container does. 
    - So when a Container terminates and restarts, filesystem changes are lost. 
    - For more consistent storage that is independent of the Container, you can use a [Volume](https://kubernetes.io/docs/concepts/storage/volumes/).


<h2 id="77ea5ef86c2c650eb37fa7374f084bbc"></h2>

### emptyDir

- An [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume is first created when a Pod is assigned to a node, and exists as long as that Pod is running on that node. 
    - As the name says, the emptyDir volume is initially empty. 
    - All containers in the Pod can read and write the same files in the emptyDir volume, though that volume can be mounted at the same or different paths in each container. 
    - When a Pod is removed from a node for any reason, the data in the emptyDir is deleted permanently.


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: redis
spec:
  containers:
  - name: redis
    image: redis
    volumeMounts:
    - name: redis-storage
      mountPath: /data/redis
  volumes:
  - name: redis-storage
    emptyDir: {}
```

<h2 id="5eeadeea1e2bd82727f9a220408a5f2a"></h2>

### configMap

- A [ConfigMap](https://kubernetes.io/docs/concepts/storage/volumes/#configmap) provides a way to inject configuration data into pods. 
    - The data stored in a ConfigMap can be referenced in a volume of type configMap and then consumed by containerized applications running in a pod.
- The following configuration shows how to mount the log-config ConfigMap onto a Pod called configmap-pod:


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod
spec:
  containers:
    - name: test
      image: busybox:1.28
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
  volumes:
    - name: config-vol
      configMap:
        name: log-config
        items:
          - key: log_level
            path: log_level
```


<h2 id="f1e81401ee0afe2275193298ef588120"></h2>

### hostPath

Warning: [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) volumes present many security risks,  and it is a best practice to avoid the use of HostPaths when possible.


<h2 id="dc1691844d1fa3602f797857ca2f638b"></h2>

## Persistent Volume

- summary of the process to use [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
    1. You, as cluster administrator, create a PersistentVolume backed by physical storage.
    2. You, now taking the role of a developer / cluster user, create a PersistentVolumeClaim that is automatically bound to a suitable PersistentVolume.
    3. You create a Pod that uses the above PersistentVolumeClaim for storage.


- **PV should be in cluster scope**,  PVC could be in namespace scope , along with Pods

<h2 id="7a25b4411e122cd14b3d7150ddd960da"></h2>

### Create a PersistentVolume

- In this exercise, you create a hostPath PersistentVolume.  Kubernetes supports hostPath for development and testing on a *single-node* cluster. 

> In a production cluster, you would not use hostPath. Instead a cluster administrator would provision a network resource like a Google Compute Engine persistent disk, an NFS share, or an Amazon Elastic Block Store volume.

> Cluster administrators can also use StorageClasses to set up dynamic provisioning.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
```

- The configuration file specifies that the volume is at `/mnt/data` on the cluster's Node. 
    - a size of 10 gibibytes and an access mode of ReadWriteOnce, which means the volume can be mounted as read-write by a single Node.
    - It defines the StorageClass name manual for the PersistentVolume, which will be used to bind PersistentVolumeClaim requests to this PersistentVolume.


View information about the PersistentVolume:


```bash
kubectl get pv task-pv-volume
```


<h2 id="f720852f4291583f90ac6c9ca381d279"></h2>

### Create a PersistentVolumeClaim

- Pods use PersistentVolumeClaims to request physical storage.
- In this exercise, you create a PersistentVolumeClaim that requests a volume of at least 3 gibibytes that can provide read-write access for at least one Node.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 3Gi
```

```bash
kubectl get pvc task-pv-claim
```


<h2 id="0adc8bf342f1769161c24a88adfe4ff3"></h2>

### Create a Pod

- The next step is to create a Pod that uses your PersistentVolumeClaim as a volume.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes: # same level as containers
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts: # sub level under containers
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```


- Mounting the same persistentVolume in two places


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  containers:
    - name: test
      image: nginx
      volumeMounts: # sub level under containers
        # a mount for site-data
        - name: config
          mountPath: /usr/share/nginx/html
          subPath: html
        # another mount for nginx config
        - name: config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
  volumes: # same level as containers
    - name: config
      persistentVolumeClaim:
        claimName: test-nfs-claim
```










