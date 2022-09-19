
# Deploy MongoDB in k8s

## Persistent Volume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mongodb-pv
spec:
  storageClassName: mongodb-storageclass
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/opt/data/mongo"
```


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
