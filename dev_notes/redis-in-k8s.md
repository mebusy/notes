...menustart

- [Deploy a Redis cache to k8s](#ec3e4afb789f2148ebf5986909183d13)

...menuend


# Deploy a stateful set

PV

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redisdb-pv
spec:
  storageClassName: redisdb-storageclass
  persistentVolumeReclaimPolicy: "Recycle"
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/opt/data/redis"
```


STATEFUL SET

```yaml
# PVC

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: redisdb-pvc
spec:
  storageClassName: redisdb-storageclass
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
  name: redisdb-test
spec:
  serviceName: redisdb-test
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
        selector: redisdb-test
    spec:
      containers:
      - name: redisdb-test
        args:
          - --appendonly yes
        image: redis:6.2.6
        volumeMounts:
        - mountPath: /data
          name: redisdb-data
      volumes:
      - name: redisdb-data
        persistentVolumeClaim:
          claimName: redisdb-pvc

---

# Service

apiVersion: v1
kind: Service
metadata:
  name: redisdb-test
  labels:
    app: database
spec:
  ports:
  - name: 6379-6379-tcp
    port: 6379
    protocol: TCP
    targetPort: 6379
  selector:
    app: database
  type: ClusterIP



```




<h2 id="ec3e4afb789f2148ebf5986909183d13"></h2>


# If you just want redis as memory cache...


```yaml
apiVersion: v1
items:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      k8s-app: redis-cache
    name: redis-cache
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: redis-cache
    strategy:
      type: RollingUpdate
    template:
      metadata:
        labels:
          k8s-app: redis-cache
      spec:
        containers:
        - args:
          - --maxmemory 370m
          - --maxmemory-policy allkeys-lru
          - --protected-mode no
          - --save ''
          - --appendonly no
          image: redis:4.0.14
          imagePullPolicy: IfNotPresent
          name: redis-cache
          resources:
            limits:
              cpu: "1"
            requests:
              cpu: 100m
              memory: 128Mi
        dnsPolicy: ClusterFirst
        restartPolicy: Always

- apiVersion: v1
  kind: Service
  metadata:
    name: redis-cache
  spec:
    ports:
    - name: 6379-6379-tcp
      port: 6379
      protocol: TCP
      targetPort: 6379
    selector:
      k8s-app: redis-cache
    sessionAffinity: None
    type: ClusterIP

kind: List
```


