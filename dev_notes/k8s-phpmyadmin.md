
# Expose k8s mysql with PhpMyAdmin

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



