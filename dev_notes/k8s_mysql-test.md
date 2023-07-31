[](...menustart)

- [Create A Persistent Volume](#5f8275d909a1c3cade324a55d89e0337)
- [Create a mysql in k8s with root/rootpwd](#e6c4fa270e7ad3daf363af62c5a08163)
- [Expose Mysql service in k8s](#73daabeddc65e8243ffa9143bbc6d239)

[](...menuend)


# Create A Stateful Set Mysql in local k8s

<h2 id="5f8275d909a1c3cade324a55d89e0337"></h2>

## Create A Persistent Volume

```yaml
# mysql57-pv.yaml 

apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-57-pv
spec:
  storageClassName: mysql-57-storageclass
  # default reclaim poliy is "Retain", the data persists even if you delete pv.
  #   use Recycle is case you set you local testing environment.
  persistentVolumeReclaimPolicy: "Recycle"
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/Volumes/WORK/_DockerMnt/mysql-57"
```

- Persistent volumes are cluster-global objects and do not live in specific namespaces.  
    - So you'd better to name it with a unique name, e.g. `mysql-57-storageclass`
- On MacOs Docker Desktop, `/Volumes` is mounted by default, you can specify the `hostPath` of PV to maintain pod data, 
    - e.g., `/Volumes/WORK/_DockerMnt/mysql-57`.


<h2 id="e6c4fa270e7ad3daf363af62c5a08163"></h2>

## Create a mysql in k8s with root/rootpwd

- You should specify a correct storageClassName
- You normally deploy it in specific namespace, no need worry about naming.


```yaml
# mysql57.yaml

# PVC

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysqldb-pvc
spec:
  storageClassName: mysql-57-storageclass
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 1Gi

---
# StatefulSet

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql-test
spec:
  serviceName: mysql-test
  replicas: 1
  selector:
    matchLabels:
      k8s-app: mysql-test
  template:
    metadata:
      labels:
        k8s-app: mysql-test
    spec:
      containers:
        - env:
            - name: MYSQL_ROOT_PASSWORD
              value: rootpwd
          image: mysql:5.7
          imagePullPolicy: IfNotPresent
          name: mysql-test
          volumeMounts:
            - mountPath: "/var/lib/mysql"
              name: mysql-data
      volumes:
        - name: mysql-data
          persistentVolumeClaim:
            claimName: mysqldb-pvc
---
# Service

apiVersion: v1
kind: Service
metadata:
  name: mysql-test
spec:
  ports:
    - name: 3306-3306-tcp
      port: 3306
      protocol: TCP
      targetPort: 3306
  selector:
    k8s-app: mysql-test
  type: ClusterIP


```


## Deploy

```bash
kubectl create -f mysql57-pv.yaml
kubectl create ns mysql-57
kubectl -n mysql-57 create -f mysql57.yaml 
```


so far you can not access mysql exterannly because its type is `ClusterIP`.

use [portforward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward) to expose mysql service:


```bash
# access locally
kubectl -n mysql-57 --address 127.0.0.1 port-forward   statefulset.apps/mysql-test 6379:6379
# can access from any host
kubectl -n mysql-57 --address 0.0.0.0 port-forward   statefulset.apps/mysql-test 6379:6379
```




