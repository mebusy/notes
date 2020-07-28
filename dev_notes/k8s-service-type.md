
# k8s service type

## cluster only

通过集群的内部 IP 暴露服务。当您的服务只需要在集群内部被访问时，请使用该类型。该类型为默认的 ServiceType。

```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: ipa-server
  spec:
    ports:
    - name: 7001-7001-tcp
      port: 7001
      protocol: TCP
      targetPort: 7001
    selector:
      k8s-app: ipa-server
    sessionAffinity: None
    type: ClusterIP
```


## NodePort 

通过每个集群节点上的 IP 和静态端口（NodePort）暴露服务。

NodePort 服务会路由到 ClusterIP 服务，该 ClusterIP 服务会自动创建。通过请求 <NodeIP>:<NodePort>，可从集群的外部访问该 NodePort 服务。

除了测试以及非生产环境以外，不推荐在生产环境中直接通过集群节点 **对外** 甚至公网提供服务。从安全上考虑，使用该类型会直接暴露集群节点，容易受到攻击。使用该类型使得对外提供服务的地址和集群节点有了耦合。



```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: ipa-server
  spec:
    ports:
    - name: 7001-7001-tcp
      port: 7001
      protocol: TCP
      targetPort: 7001
    selector:
      k8s-app: ipa-server
    sessionAffinity: None
    type: NodePort
```

## LoadBalancer

负载均衡器可以路由到 NodePort 服务，或直接转发到处于 VPC-CNI 网络条件下的容器中。

1. type: LoadBalancer
2. depends on service provider


