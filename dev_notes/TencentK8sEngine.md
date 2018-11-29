
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
```


 - doc: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/
 - [轻松了解Kubernetes部署功能](http://qinghua.github.io/kubernetes-deployment/)


# cntlm 设置代理 (Centos7)

 - 1 `yum install cntlm`
 - 2 Get password hash 
    - (type your password, press enter and copy the output)

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
