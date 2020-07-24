
# Deploy Redis Cache to k8s



1. Create a kustomization.yaml file containing:
    - a ConfigMap generator
    - a Pod resource config using the ConfigMap
2. Apply the directory by running `kubectl -n <name-space> apply -k ./`


PS. works with kubectl 1.14 and above.


```bash
# main file must be named as kustomization.yml
kubectl -n test apply -k .
```

