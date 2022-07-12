
#  Mysql in k8s, PhpMyAdmin


## Expose Mysql service in k8s

use [portforward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward) ,   say you have mysql service  under namespace mysql-57,  you listen on port 33057 on all address, and forward to 3306 in a pod select by the deployment.


```bash
kubectl -n mysql-57  --address 0.0.0.0   port-forward deployment/mysql-57 33057:3306
```


## PhpMyAdmin


```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: phpmyadmin-deployment
  labels:
    app: phpmyadmin
spec:
  replicas: 1
  selector:
    matchLabels:
      app: phpmyadmin
  template:
    metadata:
      labels:
        app: phpmyadmin
    spec:
      containers:
        - name: phpmyadmin
          image: phpmyadmin/phpmyadmin
          ports:
            - containerPort: 80
          env:
            - name: PMA_HOST
              # <service-name>.<namespace-name>.svc.cluster.local
              value: "mysql-57.mysql-57.svc.cluster.local" # TODO
            - name: PMA_PORT
              value: "3306"

---
apiVersion: v1
kind: Service
metadata:
  name: phpmyadmin-service
spec:
  type: NodePort
  selector:
    app: phpmyadmin
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: phpmyadmin-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
    - host: phpmyadmin57 # TODO
      http:
        paths:
          # phpadmin must use root path: /
          - path: /
            pathType: Prefix
            backend:
              service:
                name: phpmyadmin-service
                port:
                  number: 80

```



