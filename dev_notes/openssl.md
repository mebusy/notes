[](...menustart)

- [OpenSSL](#ee302fd5fd2a7a5a3c19fc5be21f979c)
    - [使用OpenSSL工具生成密钥](#e35855d8b0178ee80e1543aad6d1a5ce)
    - [Generate Key Pair](#b849b180cf9c062b2ba3154b86a027fc)
    - [Extract Public Key from Private Key](#2f0b9301923419f5fddf5f25a7762602)
    - [CSR: Certificate Signing Request](#5001afbd80b25e4b6c597fb68880c032)
    - [Self Signed Certificate](#5268c2edcf0f7ae7ce41e905564de177)
    - [Misc](#74248c725e00bf9fe04df4e35b249a19)
- [RSA Public Key format](#967cf47a9ccbc9f0477ffe8ac2df05dd)
    - [Convert between different formats...](#b877b734093e9001b4572816c5ed60bd)
- [PEM Headers](#8767d9b0a0775bd3ce785aba5e9d78ce)
    - [Other convertion](#34590c775b79aa0219feabb60a77c6c8)

[](...menuend)


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


<h2 id="b849b180cf9c062b2ba3154b86a027fc"></h2>

## Generate Key Pair

```bash
# RSA algorihtm introduced since openssl v1.0
$ openssl genrsa -out serv1.key 2048
Generating RSA private key, 2048 bit long modulus
...+++
..........................................................+++
e is 65537 (0x10001)

$ cat serv1.key
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAx9smn4lu+xTyjoi8O
...
```

This key is in PKCS1 ( Public Key Cryptography Standards ) format.

<h2 id="2f0b9301923419f5fddf5f25a7762602"></h2>

## Extract Public Key from Private Key

- use same algorithm RSA
- we want to output public certificate
    - `-pubout`

```bash
$ openssl rsa -in serv1.key -pubout -out serv1_pub.key
writing RSA key

# x.509 public key
$ cat serv1_pub.key
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAO
...
```

if you want to generate the obsoluted RSA PUBLIC KEY, add `-RSAPublicKey_out`

```bash
$ openssl rsa -in serv1.key -pubout -out serv1_pub_rsa.key -RSAPublicKey_out
writing RSA key

$ cat serv1_pub_rsa.key
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAx9smn4lu+xTyjoi8Ob
...
```


<h2 id="5001afbd80b25e4b6c597fb68880c032"></h2>

## CSR: Certificate Signing Request

Normally the procedure is that first you create a key pair, and after creating a key pair, you create a Certificate Signing Request (CSR). 

If it's in a real scenario in the real productions after creating the certificate signing request this CSR is handed over to CA (Certification  Authority). And they sign it on your behalf and then you get the certificate which CA signed.

But here what we will do we will create a CSR and then we will do self-signed.

```bash
# create a CSR
$ openssl req -new -key serv1.key -out serv1.csr
-----
Country Name (2 letter code) []:PK
State or Province Name (full name) []:ISB
Locality Name (eg, city) []:ISB
Organization Name (eg, company) []:fakecom
Organizational Unit Name (eg, section) []:fakecom
Common Name (eg, fully qualified host name) []:*.example.com
Email Address []:abc@fake.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
```

For test purpose, only the Common Name is important.

Once you create a CSR it's very important that CSR contains the information info. If in real scenairos you arg going to get it signed by the CA then you should first verify and make sure that whatever information you want it for your CSR is correctly entered. In order to do that you can do the verification.

```bash
$ openssl req -text -in serv1.csr -noout -verify
verify OK
Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: C=PK, ST=ISB, L=ISB, O=fakecom, OU=fakecom, CN=*.example.com/emailAddress=abc@fake.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
```

Everything that you provided is showing here. If you find that anything is wrong, you can still regenerate your CSR.

<h2 id="5268c2edcf0f7ae7ce41e905564de177"></h2>

## Self Signed Certificate

> X.509是密码学里公钥证书的格式标准。X.509证书已应用在包括TLS/SSL在内的众多网络协议里，同时它也用在很多非在线应用场景里，比如电子签名服务。X.509证书里含有公钥、身份信息（比如网络主机名，组织的名称或个体名称等）和签名信息（可以是证书签发机构CA的签名，也可以是自签名）

```bash
$ openssl x509 -in serv1.csr -out serv1.crt -req -signkey serv1.key -days 3650
Signature ok
subject=/C=PK/ST=ISB/L=ISB/O=fakecom/OU=fakecom/CN=*.example.com/emailAddress=abc@fake.com
Getting Private key
```

serv1.crt is our signed x509 certificate.

<details>
<summary>
one line command to self-assigned ?
</summary>

```bash
$ openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -subj '/CN=www.example.com' -keyout server.key -out server.crt
Generating a 2048 bit RSA private key
...................................................................................................................................................+++
.............................................+++
writing new private key to 'server.key'
```

We can take a look inside the certificate.

```bash
$ openssl x509 -text -in serv1.crt -noout
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 13243143775929165193 (0xb7c9191959aee589)
    Signature Algorithm: sha1WithRSAEncryption
        Issuer: C=PK, ST=ISB, L=ISB, O=fakecom, OU=fakecom, CN=*.example.com/emailAddress=abc@fake.com
        Validity
            Not Before: Mar 23 06:10:33 2022 GMT
            Not After : Mar 20 06:10:33 2032 GMT
    ...
```

</details>

<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>

## Misc

random

```bash
$ openssl rand -base64 16
0qY8lqxWI/SQ1qGllLW+WA==
$ openssl rand -base64 8
IzOi8Mqq8tU=
```


<h2 id="967cf47a9ccbc9f0477ffe8ac2df05dd"></h2>

# RSA Public Key format

An RSA public key formatted by OpenSSH , can be generated by  `ssh-keygen`

> SSH keys are used for secure connections across a network. 

```bash
$ ssh-keygen -b 2048 -t rsa
```

```text
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQB/nAmOjTmezNUDKYvEeIRf2YnwM9/uUG1d0BYsc8/tRtx+RGi7N2lUbp728MXGwdnL9od4cItzky/zVdLZE2cycOa18xBK9cOWmcKS0A8FYBxEQWJ/q9YVUgZbFKfYGaGQxsER+A0w/fX8ALuk78ktP31K69LcQgxIsl7rNzxsoOQKJ/CIxOGMMxczYTiEoLvQhapFQMs3FL96didKr/QbrfB1WT6s3838SEaXfgZvLef1YB2xmfhbT9OXFE3FXvh2UPBfN+ffE7iiayQf/2XR+8j4N4bW30DiPtOQLGUrH1y5X/rpNZNlWW2+jGIxqZtgWg7lTy3mXy5x836Sj/6L
```

> usually they are all in one line

The standard ssh2 file format for use in Secure Shell

`-e` : The default export format is “RFC4716”

```bash
$ ssh-keygen -b 2048 -t rsa -e

---- BEGIN SSH2 PUBLIC KEY ----
Comment: "2048-bit RSA, ..."
AAAAB3NzaC1yc2EAAAABJQAAAQB/nAmOjTmezNUDKYvEeIRf2YnwM9/uUG1d0BYs
c8/tRtx+RGi7N2lUbp728MXGwdnL9od4cItzky/zVdLZE2cycOa18xBK9cOWmcKS
0A8FYBxEQWJ/q9YVUgZbFKfYGaGQxsER+A0w/fX8ALuk78ktP31K69LcQgxIsl7r
NzxsoOQKJ/CIxOGMMxczYTiEoLvQhapFQMs3FL96didKr/QbrfB1WT6s3838SEaX
fgZvLef1YB2xmfhbT9OXFE3FXvh2UPBfN+ffE7iiayQf/2XR+8j4N4bW30DiPtOQ
LGUrH1y5X/rpNZNlWW2+jGIxqZtgWg7lTy3mXy5x836Sj/6L
---- END SSH2 PUBLIC KEY ----
```

The same public key formatted as an RSA public key (note the five -, and no space):

```text
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEA+xGZ/wcz9ugFpP07Nspo6U17l0YhFiFpxxU4pTk3Lifz9R3zsIsu
ERwta7+fWIfxOo208ett/jhskiVodSEt3QBGh4XBipyWopKwZ93HHaDVZAALi/2A
+xTBtWdEo7XGUujKDvC2/aZKukfjpOiUI8AhLAfjmlcD/UZ1QPh0mHsglRNCmpCw
mwSXA9VNmhz+PiB+Dml4WWnKW/VHo2ujTXxq7+efMU4H2fny3Se3KYOsFPFGZ1TN
QSYlFuShWrHPtiLmUdPoP6CV2mML1tk+l7DIIqXrQhLUKDACeM5roMx0kLhUWB8P
+0uj1CNlNN4JRZlC7xFfqiMbFRU9Z4N6YwIDAQAB
-----END RSA PUBLIC KEY-----
```

> The "RSA PUBLIC KEY" format was used in very early SSLeay, which evolved into OpenSSL, but obsoleted before 2000

> Although this format is long obsolete, **OpenSSL still supports** it.

openssl  x.509 public key, which looks like this:

```text
-----BEGIN PUBLIC KEY-----
...
-----END PUBLIC KEY-----
```

---

`RSA PUBLIC KEY` is closer to the content of a `PUBLIC KEY`.

"RSA PUBLIC KEY" format is the RSA-specific format from PKCS#1, whereas "PUBLIC KEY" is the X.509 generic structure that handles numerous (and extensible) algorithm. 



<h2 id="b877b734093e9001b4572816c5ed60bd"></h2>

## Convert between different formats...

**The ssh-keygen utility is used to covert SSH keys between the different formats.**

- convert to OpenSSH format.
    - `-i` : this option will read an unencrypted private (or public) key file in the format specified by the -m option and print an OpenSSH compatible private (or public) key to stdout.
        - The default **import** format is “RFC4716”(SSH2).
    ```bash
    # -mPKCS8  to specify the input format
    ssh-keygen -f pub1key.pub -i -mPKCS8
    ```

> -m key_format Specify a key format for the -i (import) or -e (export) conversion options. The supported key formats are: “RFC4716” (RFC 4716/SSH2 public or private key), “PKCS8” (PEM PKCS8 public key) or “PEM” (PEM public key). The default conversion format is “RFC4716”.

- to convert OpenSSH format(ssh-rsa) to SSH2 format
    - `-e`: read a private or public OpenSSH key file and print to stdout a public key in one of the formats specified by the -m option
        - The default **export** format is “RFC4716”(SSH2).
    ```bash
    ssh-keygen -e -f ./openssh.pub
    ```

<h2 id="8767d9b0a0775bd3ce785aba5e9d78ce"></h2>

# PEM Headers 

PEM Header | Pub/Priv | Format 
--- | --- | ---
BEGIN RSA PUBLIC KEY | Public | PKCS#1 RSA 
BEGIN RSA PRIVATE KEY | Private | PKCS#1 RSA
BEGIN PUBLIC KEY | Public | X.509 
BEGIN PRIVATE KEY | Private | PKCS#8 
BEGIN ENCRYPTED PRIVATE KEY | Private | PKCS#8 Encrypted


format | for 
--- | ---
PKCS#1  | traditional format for RSA keys
PKCS#8  | foramt any private key
X.509 | format for any public key


- convert between PKCS#1 and PKCS#2
    ```basn
    # #1 -> #8
    openssl pkcs8 -in private-pkcs1.pem -topk8 -out private-pkcs8.pem -nocrypt
    openssl pkcs8 -in private-pkcs1.pem -topk8 -out private-pkcs8-enc.pem
    ```
    ```bash
    # #8 -> #1
    openssl rsa -in private-pkcs8.pem -out private-pkcs1.pem
    ```

<h2 id="34590c775b79aa0219feabb60a77c6c8"></h2>

## Other convertion

Convert RSA public key between X.509 and PKCS #1 formats

```bash
openssl rsa -pubin -in public.pem -RSAPublicKey_out
openssl rsa -RSAPublicKey_in -in pkcs1-public.pem -pubout
```

Extract public key from RSA private key

```bash
openssl rsa -in private.pem -out public.pem -pubout
```

Extract public key from X.509 CSR

```bash
openssl req -in cert.csr -pubkey -noout
```

Extract public key from X.509 certificate

```bash
openssl x509 -in cert.crt -inform pem -pubkey -noout
openssl x509 -in cert.cer -inform der -pubkey -noout
```

Convert X.509 certificate between DER and PEM formats

```bash
openssl x509 -in cert.cer -inform der -out cert.crt -outform pem
openssl x509 -in cert.crt -inform pem -out cert.cer -outform der
```

---

[SSH协议中的非对称加密](https://blog.csdn.net/m0_46573836/article/details/108900752)

[彻底搞懂HTTPS的加密原理](https://zhuanlan.zhihu.com/p/43789231)

[HTTPS用的是对称加密还是非对称加密](https://zhuanlan.zhihu.com/p/96494976)

[HTTPS用的是对称加密还是非对称加密](https://www.cnblogs.com/lfri/p/12593232.html)

**利用私钥加密的过程，其实就是在对数据进行签名，所以也叫数字签名**



