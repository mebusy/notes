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


## Generate Key Pair

```bash
# RSA algorihtm introduced since openssl v1.0
$ openssl genrsa -out serv1.key 2048
Generating RSA private key, 2048 bit long modulus
...+++
..........................................................+++
e is 65537 (0x10001)
```

This key is in PKCS1 ( Public Key Cryptography Standards ) format.

## Extract Public Key from Private Key

- use same algorithm RSA
- we want to output public certificate
    - `-pubout`

```bash
$ openssl rsa -in serv1.key -pubout -out serv1_pub.key
writing RSA key
```

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

## Misc

random

```bash
$ openssl rand -base64 16
0qY8lqxWI/SQ1qGllLW+WA==
qibinyi@Qis-Mac-mini mitmproxy_test $ openssl rand -base64 8
IzOi8Mqq8tU=
```

