[](...menustart)

- [Create A Persistent Volume](#5f8275d909a1c3cade324a55d89e0337)
- [Create a mysql in k8s with root/rootpwd](#e6c4fa270e7ad3daf363af62c5a08163)
- [Expose Mysql service in k8s](#73daabeddc65e8243ffa9143bbc6d239)

[](...menuend)


<h2 id="5f8275d909a1c3cade324a55d89e0337"></h2>

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
  # default reclaim poliy is "Retain", the data persists even if you delete pv.
  #   use Recycle is case you set you local testing environment.
  # persistentVolumeReclaimPolicy: "Recycle"
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/opt/data/mysql"
```

<h2 id="e6c4fa270e7ad3daf363af62c5a08163"></h2>

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


<h2 id="73daabeddc65e8243ffa9143bbc6d239"></h2>

## Expose Mysql service in k8s

so far you can not access mysql exterannly because its type is `ClusterIP`.

use [portforward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward) ,   say you have mysql service  under namespace mysql-57,  you listen on port 33057 on all address, and forward to 3306 in a pod select by the deployment.


```bash
kubectl -n mysql-57  --address 0.0.0.0   port-forward deployment/mysql-57 33057:3306
```

Now you can connect to mysql  from outside

```bash
mysql -h <host-name> -P 33057 -u<user> -p<passwd>
```

NOTE: port-forward will fail after service restarting.




