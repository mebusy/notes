...menustart

 - [Deploy a Redis cache to k8s](#ec3e4afb789f2148ebf5986909183d13)

...menuend


<h2 id="ec3e4afb789f2148ebf5986909183d13"></h2>


# Deploy a Redis cache to k8s

```bash
vi redis-cache.yaml

kubectl -n <name-space> replace -f redis-cache.yaml --force
```

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

