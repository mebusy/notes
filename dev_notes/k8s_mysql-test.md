...menustart

- [create a test mysql in k8s with root/root](#595140279525e99ad195e33954e2f6cf)

...menuend


## Create A Persistent Volume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-mysql-data
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/opt/data/mysql"
```

<h2 id="595140279525e99ad195e33954e2f6cf"></h2>


## Create a mysql in k8s with root/rootpwd


```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-mysql-57
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi

---
apiVersion: v1
items:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      k8s-app: mysql-57
    name: mysql-57
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: mysql-57
    strategy:
      type: RollingUpdate
    template:
      metadata:
        labels:
          k8s-app: mysql-57
      spec:
        containers:
        - env:
          - name: MYSQL_ROOT_PASSWORD
            value: rootpwd
          image: mysql:5.7
          imagePullPolicy: IfNotPresent
          name: mysql-57
          resources:
            limits:
              cpu: "1"
              memory: 1Gi
            requests:
              cpu: 100m
              memory: 128Mi
          volumeMounts: # sub level under containers [optional]
            - mountPath: "/var/lib/mysql"
              name: pvc-mysql-57-storage
        dnsPolicy: ClusterFirst
        restartPolicy: Always
        volumes: # same level as containers [optional]
          - name: pvc-mysql-57-storage
            persistentVolumeClaim:
              claimName: pvc-mysql-57

- apiVersion: v1
  kind: Service
  metadata:
    name: mysql-57
  spec:
    ports:
    - name: 3306-3306-tcp
      port: 3306
      protocol: TCP
      targetPort: 3306
    selector:
      k8s-app: mysql-57
    sessionAffinity: None
    type: ClusterIP

kind: List

```

