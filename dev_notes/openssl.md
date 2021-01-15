...menustart

- [OpenSSL](#ee302fd5fd2a7a5a3c19fc5be21f979c)
    - [使用OpenSSL工具生成密钥](#e35855d8b0178ee80e1543aad6d1a5ce)

...menuend


<h2 id="ee302fd5fd2a7a5a3c19fc5be21f979c"></h2>


# OpenSSL


<h2 id="e35855d8b0178ee80e1543aad6d1a5ce"></h2>


## 使用OpenSSL工具生成密钥

```bash
首先进入OpenSSL工具，输入以下命令：

OpenSSL> genrsa -out app_private_key.pem   2048  #生成私钥

OpenSSL> pkcs8 -topk8 -inform PEM -in app_private_key.pem -outform PEM -nocrypt -out app_private_key_pkcs8.pem #Java开发者需要将私钥转换成PKCS8格式

OpenSSL> rsa -in app_private_key.pem -pubout -out app_public_key.pem #生成公钥

OpenSSL> exit #退出OpenSSL程序

经过以上步骤，开发者可以在当前文件夹中（OpenSSL运行文件夹），看到 app_private_key.pem（开发者RSA私钥，非 Java 语言适用）、app_private_key_pkcs8.pem（pkcs8格式开发者RSA私钥，Java语言适用）和app_public_key.pem（开发者RSA公钥）3个文件。
```


