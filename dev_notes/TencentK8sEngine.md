
# TKE

# kubectl

 - 客户端小版本最多比服务器大1， 比如服务器版本是1.7.8 , 客户端版本可以用 1.8.x 

## install

 - linux
    - https://storage.googleapis.com/kubernetes-release/release/v1.8.4/bin/linux/amd64/kubectl
 - macos:
    - replace `linux` with `darwin` 

```
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```



## use kubectl

```
1. list pods
kubectl -n umc-dunkshot-prod2 get po

2. exec
kubectl exec -ti -n <namespace> <name of workernode> <command>
i.e. kubectl exec -ti -n <namespace> <name of workernode>

3.
kubectl -n umc-dunkshot-dev2 get svc

4. find pod by ip
kubectl get po --all-namespaces -o wide | grep 10.0.0.39

5. get yaml 
kubectl ... get ...  -o yaml --export 

6. service accont 
  create serviceaccount
  create role
  create rolebinding
  ...

7. 使用 ccr.ccs.tencentyun.com 仓库上的镜像，需要 secret: 
    - qcloudregistrykey , 
    - tencenthubkey (自动创建？)
```


 - doc: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/
 - [轻松了解Kubernetes部署功能](http://qinghua.github.io/kubernetes-deployment/)


# 腾讯云 用户管理

## 策略

 - 访问 COS 某个bucket的策略

```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cos:*"
            ],
            "resource": "qcs::cos:::BUCKET-NAME/*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": [
                "monitor:*",
                "cam:ListUsersForGroup",
                "cam:ListGroups",
                "cam:GetGroup"
            ],
            "resource": "*"
        }
    ]
}
```


# cntlm 设置代理 (Centos7)

 - 1 install cntlm

```
1) download from 
    https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/c/
2) rpm -Uvh xxx.rpm
```


 - 2 Get password hash 
    - (type your password, press enter and copy the output)
    - modify your username/domain first in `/etc/cntlm.conf`

```
$ cntlm -H
Password:
PassLM          14BE8CB0282308185246B269C29C0A88
PassNT          DD8F12AC2482B5BC43A6972E7DFD0F78
PassNTLMv2      934498581AFCBE80CA0457E0FD30B0F9    # Only for user '', domain ''
```

 - 3 Edit cntlm configuration file(Example for testuser)

```
#vi /etc/cntlm.conf

Username YOURUSERNAME
Domain YOURCOMPANYDOMAIN
########Paste result of cntlm -H here###########
PassLM          14BE8CB0282308185246B269C29C0A88
PassNT          DD8F12AC2482B5BC43A6972E7DFD0F78
PassNTLMv2      934498581AFCBE80CA0457E0FD30B0F9    # Only for user '', domain ''

Proxy YOUR_COMPANY_PROXY_HOST:PORT
NoProxy ...
Auth NTLM
```

 - 4 Enable cntlm service at boot , and start it now
    - `#systemctl enable cntlm`
    - `#systemctl start cntlm`

 - 5 Set environment variables (HTTP_PROXY and HTTPS_PROXY)
    - use:  `127.0.0.1:3128`

---

# cntlm (Macosx)

 - /usr/local/etc/cntlm.conf 
    - otherwise it might be in /etc/cntlm.conf

 - You can run cntlm in debug mode for testing purpose and see what’s happening:
    - `cntlm -f` # Run in foreground, do not fork into daemon mode.
 - If everything is fine you can launch it as a daemon just by typing:
    - `cntlm`
 - Using LaunchAgent for automatic service launch at start
    - `~/Library/LaunchAgents/com.oho.cntlm.daemon.plist`

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.oho.cntlm.daemon</string>
  <key>ProgramArguments</key>
  <array>
      <string>/usr/local/bin/cntlm</string>
  </array>
  <key>KeepAlive</key>
  <false/>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardErrorPath</key>
  <string>/dev/null</string>
  <key>StandardOutPath</key>
  <string>/dev/null</string>
</dict>
</plist>
```

 - set proxy env

```
export http_proxy=http://localhost:3128
export https_proxy=https://localhost:3128
```

 - restart 
    - `brew services restart cntlm`
