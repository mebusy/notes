[](...menustart)

- [Deploy stateful set mongoDB in local redis and expose service](#e17ec5d192fb3858c49e4993eaad4d94)
    - [PersistentVolume](#858e55ea2e6429120a862313c50a9f5f)
    - [STATEFUL SET MongoDb](#6485e1c68187975fdbfc44e4325775b3)
    - [Deploy](#507a3a88cebc46603ce2be8eaa924eee)

[](...menuend)


<h2 id="e17ec5d192fb3858c49e4993eaad4d94"></h2>

# Deploy stateful set mongoDB in local redis and expose service

<h2 id="858e55ea2e6429120a862313c50a9f5f"></h2>

## PersistentVolume


```yaml
# mongo-pv.yaml

apiVersion: v1
kind: PersistentVolume
metadata:
  name: mongodb-503-pv
spec:
  storageClassName: mongodb-503-storageclass
  persistentVolumeReclaimPolicy: "Recycle"
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/Volumes/WORK/_DockerMnt/mongodb-503"

```

- Persistent volumes are cluster-global objects and do not live in specific namespaces.  
    - So you'd better to name it with a unique name, e.g. `mongodb-503-storageclass`
- On MacOs Docker Desktop, `/Volumes` is mounted by default, you can specify the `hostPath` of PV to maintain pod data, 
    - e.g., `/Volumes/WORK/_DockerMnt/mongodb-503`.


<h2 id="6485e1c68187975fdbfc44e4325775b3"></h2>

## STATEFUL SET MongoDb

- You should specify a correct storageClassName
- You normally deploy mongo in specific namespace, no need worry about naming.

```yaml
# mongo.yaml

# PVC

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongodb-pvc
spec:
  storageClassName: mongodb-503-storageclass
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
  name: mongodb-test
spec:
  serviceName: mongodb-test
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
        selector: mongodb-test
    spec:
      containers:
        - name: mongodb-test
          image: mongo:5.0.3
          env:
            - name: MONGO_INITDB_DATABASE
              value: "admin"
            - name: MONGO_INITDB_ROOT_USERNAME
              value: "root"
            - name: MONGO_INITDB_ROOT_PASSWORD
              value: "root"
          volumeMounts:
            - mountPath: /data/db
              name: mongodb-data
      volumes:
        - name: mongodb-data
          persistentVolumeClaim:
            claimName: mongodb-pvc

---
# Service

apiVersion: v1
kind: Service
metadata:
  name: mongodb-test
  labels:
    app: database
spec:
  ports:
    - name: 27017-27017-tcp
      port: 27017
      protocol: TCP
      targetPort: 27017
  selector:
    app: database
  type: ClusterIP


```


<h2 id="507a3a88cebc46603ce2be8eaa924eee"></h2>

## Deploy 

```bash
kubectl create -f mongo-pv.yaml
kubectl create ns mongo-503
kubectl -n  mongo-503 create -f mongo.yaml
```

Exposing mongodb by port-forward to mongodb service:

```bash
# access locally
kubectl -n mongo-503  --address 127.0.0.1 port-forward   statefulset.apps/mongodb-test 27017:27017
# can access from any host
kubectl -n mongo-503  --address 0.0.0.0 port-forward   statefulset.apps/mongodb-test 27017:27017
```


# Deploy a shard cluster

```bash
helm install shard-mongo bitnami/mongodb-sharded --namespace helm-mongo-606  \
  --set image.tag=6.0.6 --version 6.0 \
  --set auth.rootUser=root \
  --set auth.rootPassword=root
```


