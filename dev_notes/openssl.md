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

如果要求 去掉 换行符

```bash
tr -d '\n' < public.txt
```

## Misc

random

```bash
$ openssl rand -base64 16
0qY8lqxWI/SQ1qGllLW+WA==
qibinyi@Qis-Mac-mini mitmproxy_test $ openssl rand -base64 8
IzOi8Mqq8tU=
```

### Self Signed Keys

when we taking about Public Key Infrastructure, or PKI, we only a private key and public key pair for each of the servers.  The public key of the server will be signed by a trust certificate authroity.

Using a self signed key much in same way when we looking at ssh.  Every client would have to trust a server.

```bash
$ openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -subj '/CN=www.example.com' -keyout server.key -out server.crt
Generating a 2048 bit RSA private key
...................................................................................................................................................+++
.............................................+++
writing new private key to 'server.key'
```

The server.key is the private key of server.

> .crt is our signed x509 certificate.

The public key then need to be trusted on the devices.

We can take a look inside the certificate.

```bash
$ openssl x509 -text -in server.crt -noout   
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 10410539609545464661 (0x9079aa9e13175b55)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=www.example.com
        Validity
            Not Before: Mar 22 16:00:21 2022 GMT
            Not After : Mar 22 16:00:21 2023 GMT
        Subject: CN=www.example.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    ...
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
        ...
```

Now we're gonna see how to create our TRUE certificate authority so that our clients only need to trust one system not every single server.


### Private Keys -- Encrypted and Unencrypted

We want to generate a RSA key  -- `genrsa`

we need a strong encryption `-aes256`

we can specify the number of bits, we use  `4096` for our root certificate

```bash
$ openssl genrsa -aes256 -out ca.key 4096
Generating RSA private key, 4096 bit long modulus
.................++
..........................................................................................................................................................++
e is 65537 (0x10001)
Enter pass phrase for ca.key:   # enter password
Verifying - Enter pass phrase for ca.key:
```

We dont want the password phase for our server certificate , `remove -aes256`

```bash
$ openssl genrsa -out server.key 2048
Generating RSA private key, 2048 bit long modulus
...................................................................................................+++
......+++
e is 65537 (0x10001)
```

### Public Certificates  -- Creating the Server CA

The public is gonna be generated from out private key.

Let's way we want to use sha256 , 

```bash
$ openssl req -key server.key -new -sha256 -out server.csr
```

So we have got our request , but of course the request need to be signed.
