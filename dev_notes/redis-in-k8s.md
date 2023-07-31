[](...menustart)

- [Deploy Redis in local k8s and expose service](#867c17202bd1062ba34bf99faf434d6b)
    - [PersistentVolume](#858e55ea2e6429120a862313c50a9f5f)
    - [STATEFUL SET Redis](#305457477e783f4354ecabe28cd3081c)
    - [Deploy](#507a3a88cebc46603ce2be8eaa924eee)
- [If you just want redis as memory cache...](#15b6834685dfbd80ef67e02007df091d)

[](...menuend)


<h2 id="867c17202bd1062ba34bf99faf434d6b"></h2>

# Deploy Redis in local k8s and expose service

<h2 id="858e55ea2e6429120a862313c50a9f5f"></h2>

## PersistentVolume

PV

```yaml
# redis-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redisdb-626-pv
spec:
  storageClassName: redisdb-626-storageclass
  persistentVolumeReclaimPolicy: "Recycle"
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/Volumes/WORK/_DockerMnt/redisdb-626"
```

- Persistent volumes are cluster-global objects and do not live in specific namespaces.  
    - So you'd better to name it with a unique name, e.g. `redisdb-626-storageclass`
- On MacOs Docker Desktop, `/Volumes` is mounted by default, you can specify the `hostPath` of PV to maintain pod data, 
    - e.g., `/Volumes/WORK/_DockerMnt/redisdb-626`.


<h2 id="305457477e783f4354ecabe28cd3081c"></h2>

## STATEFUL SET Redis

- You should specify a correct storageClassName
- You normally deploy redis in specific namespace, no need worry about naming.

```yaml
# redis.yaml

# PVC

apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: redisdb-pvc
spec:
  storageClassName: redisdb-626-storageclass
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


<h2 id="507a3a88cebc46603ce2be8eaa924eee"></h2>

## Deploy 

```bash
kubectl create -f redis-pv.yaml
kubectl create ns redis-626
kubectl -n redis-626 create -f redis.yaml
```

To expose redis by port-forward to redis service:

```bash
# access locally
kubectl -n redis-626 --address 127.0.0.1 port-forward   statefulset.apps/redisdb-test 6379:6379
# can access from any host
kubectl -n redis-626 --address 0.0.0.0 port-forward   statefulset.apps/redisdb-test 6379:6379
```


<h2 id="15b6834685dfbd80ef67e02007df091d"></h2>

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


