...menustart

 - [TKE](#12510f8273f9a47f538779a3afd71f53)
 - [kubectl](#0f12ee5c9f1dd90158580f1c292b0d37)
     - [install](#19ad89bc3e3c9d7ef68b89523eff1987)
     - [use kubectl](#773c2c719c95cc40967b0e945ada8898)
 - [腾讯云 用户管理](#7616e9353ba2c3c55eb7063e51fc65fb)
     - [策略](#66914536facf5b30973b236fb814d23f)
 - [cntlm 设置代理 (Centos7)](#c36aef5f4c92632a2362a83ed0523565)
 - [cntlm (Macosx)](#48cd1b6a59fb119e19d9f83e6cf43668)

...menuend


<h2 id="12510f8273f9a47f538779a3afd71f53"></h2>

# TKE

<h2 id="0f12ee5c9f1dd90158580f1c292b0d37"></h2>

# kubectl

 - 客户端小版本最多比服务器大1， 比如服务器版本是1.7.8 , 客户端版本可以用 1.8.x 

<h2 id="19ad89bc3e3c9d7ef68b89523eff1987"></h2>

## install

 - linux
    - https://storage.googleapis.com/kubernetes-release/release/v1.8.4/bin/linux/amd64/kubectl
 - macos:
    - replace `linux` with `darwin` 

```
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl
```



<h2 id="773c2c719c95cc40967b0e945ada8898"></h2>

## use kubectl

```
1. list pods
kubectl -n umc-dunkshot-prod2 get po

  only name:
kubectl get po --no-headers -o custom-columns=:.metadata.name

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
  create serviceaccount <name>  , it will also create an secret
  create role  by create -f
  create rolebinding  by create -f 
  ...

7. ImagePullSecret ( 如果需要从外部pull 镜像的话需要设置)
    - qcloudregistrykey , 
    - or tencenthubkey 
```


 - doc: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/
 - [轻松了解Kubernetes部署功能](http://qinghua.github.io/kubernetes-deployment/)


<h2 id="7616e9353ba2c3c55eb7063e51fc65fb"></h2>

# 腾讯云 用户管理

<h2 id="66914536facf5b30973b236fb814d23f"></h2>

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


<h2 id="c36aef5f4c92632a2362a83ed0523565"></h2>

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
    - or `cntlm -H -u <Your ubisoft username> -d cop-domain` ?

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

<h2 id="48cd1b6a59fb119e19d9f83e6cf43668"></h2>

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
