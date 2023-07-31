[](...menustart)

- [Deploy a stateful set](#7dca21fd06e067f3857514c73c69c33d)

[](...menuend)


<h2 id="7dca21fd06e067f3857514c73c69c33d"></h2>

# Deploy stateful set mongoDB in local redis and expose service

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

