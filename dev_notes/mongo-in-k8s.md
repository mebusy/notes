...menustart

- [Deploy MongoDB in k8s](#76623500c7c129f55af57521e8f2450f)
    - [Persistent Volume](#dc1691844d1fa3602f797857ca2f638b)
    - [MongoDB](#206e3718af092fd1d12f80cae771ccac)

...menuend


<h2 id="76623500c7c129f55af57521e8f2450f"></h2>


# Deploy MongoDB in k8s

<h2 id="dc1691844d1fa3602f797857ca2f638b"></h2>


## Persistent Volume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mongodb-pv
spec:
  # default reclaim poliy is "Retain", the data persists even if you delete pv.
  #   use Recycle is case you set you local testing environment.
  # persistentVolumeReclaimPolicy: "Recycle"
  storageClassName: mongodb-storageclass
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/opt/data/mongo"
```


<h2 id="206e3718af092fd1d12f80cae771ccac"></h2>


## MongoDB

```yaml
# PVC

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongodb-pvc
spec:
  storageClassName: mongodb-storageclass
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
        image: mongo:4.0.8
        env:
          - name: MONGO_INITDB_ROOT_USERNAME
            value: "mongoadmin"
          - name: MONGO_INITDB_ROOT_PASSWORD
            value: "mongopwd"
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
