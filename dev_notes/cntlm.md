

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
    - or `cntlm -H -u <Your username> -d cop-domain` ?

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
- To have launchd start cntlm now and restart at startup:
    - `sudo brew services start cntlm`


- set proxy env

```
export http_proxy=http://localhost:3128
export https_proxy=https://localhost:3128
```

- restart 
    - `brew services restart cntlm`



