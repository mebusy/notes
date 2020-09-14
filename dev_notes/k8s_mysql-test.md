...menustart

- [create a test mysql in k8s with root/root](#595140279525e99ad195e33954e2f6cf)

...menuend


<h2 id="595140279525e99ad195e33954e2f6cf"></h2>


# create a test mysql in k8s with root/root


```yaml
apiVersion: v1
items:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      k8s-app: mysql-test
    name: mysql-test
  spec:
    replicas: 1
    selector:
      matchLabels:
        k8s-app: mysql-test
    strategy:
      type: RollingUpdate
    template:
      metadata:
        labels:
          k8s-app: mysql-test
      spec:
        containers:
        - env:
          - name: MYSQL_USER
            value: root
          - name: MYSQL_ROOT_PASSWORD
            value: root
          image: mysql:5.6
          imagePullPolicy: IfNotPresent
          name: mysql-test
          resources:
            limits:
              cpu: "1"
              memory: 1Gi
            requests:
              cpu: 100m
              memory: 128Mi
        dnsPolicy: ClusterFirst
        restartPolicy: Always

- apiVersion: v1
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
    sessionAffinity: None
    type: ClusterIP

kind: List
```

