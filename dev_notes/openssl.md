[](...menustart)

- [PEM Headers](#8767d9b0a0775bd3ce785aba5e9d78ce)
    - [Other convertion](#34590c775b79aa0219feabb60a77c6c8)

[](...menuend)


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



<h2 id="34590c775b79aa0219feabb60a77c6c8"></h2>

## Other convertion

Convert RSA public key between X.509 and PKCS #1 formats

```bash
openssl rsa -pubin -in public.pem -RSAPublicKey_out
openssl rsa -RSAPublicKey_in -in pkcs1-public.pem -pubout
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


---

[SSH协议中的非对称加密](https://blog.csdn.net/m0_46573836/article/details/108900752)

[彻底搞懂HTTPS的加密原理](https://zhuanlan.zhihu.com/p/43789231)

[HTTPS用的是对称加密还是非对称加密](https://zhuanlan.zhihu.com/p/96494976)

[HTTPS用的是对称加密还是非对称加密](https://www.cnblogs.com/lfri/p/12593232.html)

**利用私钥加密的过程，其实就是在对数据进行签名，所以也叫数字签名**



