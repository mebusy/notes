[](...menustart)

- [OpenSSL Cookbook](#754a27afe1ec843b95ea30061717249a)
    - [Getting Started](#bf647454e36069fd16f1a7a35cf6a865)
    - [Examine Available Commands](#0e6210a592ebbd65be8adb49de112534)
    - [Building a Trust Store](#67a3da980fb4978648c92453ec2416ef)
    - [Key and Certificate Management](#8f3d30d41d3b1d2c58d54a0d45d6b57f)
        - [Key Pair Generation](#e1998f23a3dea8331d5d8e51fa1c92dd)
            - [Extract Public Key from Private Key](#2f0b9301923419f5fddf5f25a7762602)
            - [Generate DSA/EDDSA Key](#da56800f6139b1a4e7b0d5fb42ef0e02)
        - [Creating Certificate Signing Requests](#65229e6867fee7f382d257166ac2bb70)
            - [CSR Verification](#31157b4a29c8c0b0a5bafc768e689ba1)
            - [Self Signed Certificate](#5268c2edcf0f7ae7ce41e905564de177)

[](...menuend)


<h2 id="754a27afe1ec843b95ea30061717249a"></h2>

# OpenSSL Cookbook

<h2 id="bf647454e36069fd16f1a7a35cf6a865"></h2>

## Getting Started

```bash
$ openssl version -a
LibreSSL 3.3.6
built on: date not available
platform: information not available
options:  bn(64,64) rc4(16x,int) des(idx,cisc,16,int) blowfish(idx)
compiler: information not available
OPENSSLDIR: "/private/etc/ssl"
```

The last line in the output (`/private/etc/ssl`) tell you where OpenSSL will look for its configuration and certificates.

```bash
$ls /private/etc/ssl
cert.pem    certs       openssl.cnf x509v3.cnf
```

<h2 id="0e6210a592ebbd65be8adb49de112534"></h2>

## Examine Available Commands

```bash
$ openssl -h
```

The **first part** of the help output lists all available utilities.

```bash
Standard commands
asn1parse         ca                certhash          ciphers
...
gendh             gendsa            genpkey           genrsa
pkcs7             pkcs8             pkey              pkeyparam
...
x509
```


To get more information about a particular utility, say `ciphers`, 

```bash
$ openssl ciphers -h
usage: ciphers [-hVv] [-tls1] [cipherlist]
 -tls1              This option is deprecated since it is the default
 -v                 Provide cipher listing
 -V                 Provide cipher listing with cipher suite values
```


In the **second part**, you get the list of message digest commands:

```bash
Message Digest commands (see the `dgst' command for more details)
gost-mac          md4               md5               md_gost94
ripemd160         sha1              sha224            sha256
sha384            sha512            sm3               sm3WithRSAEncryption
streebog256       streebog512       whirlpool
```

In the third part, you’ll see the list of all cipher commands:

```bash
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
aes-256-cbc       aes-256-ecb       base64            bf                
...
```

<h2 id="67a3da980fb4978648c92453ec2416ef"></h2>

## Building a Trust Store

OpenSSL does not come with any trusted root certificates (also known as a trust store).

One possibility is to use the trust store built into your operating system.

Or use the one Mozilla maintains, but you need extra work to convert it to proprietary format.

```bash
https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins...
/certdata.txt
```

```bash
# download convert tool
$ wget https://raw.github.com/agl/extract-nss-root-certs/master/convert_mozilla_certdata.go
# download Mozilla’s certificate data:
$ wget https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt
# convert the file
$ go run convert_mozilla_certdata.go > ca-certificates
```

<h2 id="8f3d30d41d3b1d2c58d54a0d45d6b57f"></h2>

## Key and Certificate Management

Most users turn to OpenSSL because they wish to configure and run a web server that supports SSL.

That process consists of three steps: 

1. generate a strong private key
2. create a Certificate Signing Request (CSR) and send it to a CA
3. install the CA-provided certificate in your web server. 

Before you begin, you must make several decisions:

- Key algorithm
    - OpenSSL supports `RSA`, `DSA`, and `ECDSA` keys.
    - For web server keys everyone uses RSA, because DSA keys are effectively limited to 1,024 bits, and ECDSA keys are yet to be widely supported by CAs.
    - For SSH, DSA and RSA are widely used, whereas ECDSA might not be supported by all clients.
- Key size
    - The default key sizes might not be secure. 
        - For example, the default for RSA keys is only 512 bits, which is simply insecure. An intruder could take your certificate and use brute force to recover your private key
    - Today, 2,048-bit RSA keys are considered secure, and that’s what you should use. 
    - Aim also to use 2,048 bits for DSA keys and at least 256 bits for ECDSA.
- Passphrase
    - Using a passphrase with a key is optional, but strongly recommended.
    - But using protected keys are inconvenient, and in production does not actually increase the security much, if at all (once activated, private keys are kept unprotected in program memory).
    - Thus, passphrases should be viewed only as a mechanism for protecting private keys when they are not installed on production systems. 

<h2 id="e1998f23a3dea8331d5d8e51fa1c92dd"></h2>

### Key Pair Generation

> Note: If you’re using OpenSSL 1.0.2, you can save yourself time by always generating your keys using the `genpke`y command

To generate an RSA key

```bash
$ openssl genrsa -out fd.key 2048
Generating RSA private key, 2048 bit long modulus
...................+++++
.......................+++++
e is 65537 (0x10001)
```

This key is in **PKCS1** ( Public Key Cryptography Standards ) format.

If you want to use passphrase, add `-aes128` (or `-aes192`, `-aes256`), and it's best to stay away from the other algorithms (DES, 3DES, and SEED).

```bash
$ openssl genrsa -aes128 -out fd.key 2048
```

Private keys are stored in the so-called **PEM** format, which is just text:

```bash
$ cat fd.key 
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,30666299C618C15D7C38ACAB4DE673BE

sDNj92sqonfL9zDryoH04bLdvgGdKh/gk3+DixhROUCSDM8Ii2LohJsi/7rYCXJC
...
vRbvP2NH7cQyZP8HwFMrD9dQ6jYnODQsd2YKAM12hU22vBNu1qBob1ds1jLhQGtP
-----END RSA PRIVATE KEY-----
```

<h2 id="2f0b9301923419f5fddf5f25a7762602"></h2>

#### Extract Public Key from Private Key

```bash
$ openssl rsa -in fd.key -pubout -out fd-public.key

$ cat fd-public.key
# x.509 public key
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuQgy4mnd07n137wNVcHE
...
+QIDAQAB
-----END PUBLIC KEY-----
```

If you want to generate the **obsoluted** `RSA PUBLIC KEY`, add `-RSAPublicKey_out`

<details>

```bash
$ openssl rsa -in fd.key -pubout -out fd-rsa-pub.key -RSAPublicKey_out
$cat fd-rsa-pub.key                
-----BEGIN RSA PUBLIC KEY-----
...
```

</details>



<h2 id="da56800f6139b1a4e7b0d5fb42ef0e02"></h2>

#### Generate DSA/EDDSA Key

```bash
# DSA
$ openssl dsaparam -genkey 2048 | openssl dsa -out dsa.key [-aes128]
# ECDSA
$ openssl ecparam -genkey -name secp256r1 | openssl ec -out ec.key [-aes128]
```


<h2 id="65229e6867fee7f382d257166ac2bb70"></h2>

### Creating Certificate Signing Requests

Once you have a private key, you can proceed to create a `Certificate Signing Request (CSR)`.

This is a formal request asking a CA to sign a certificate, and it contains the public key, and some information about the entity. 

```bash
$ openssl req -new -key fd.key -out fd.csr
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

For test purpose, only the `Common Name` is important.

<h2 id="31157b4a29c8c0b0a5bafc768e689ba1"></h2>

#### CSR Verification

After a CSR is generated, use it to sign your own certificate and/or send it to a public CA and ask them to sign the certificate.

But before you do that, it’s a good idea to double-check that the CSR is correct. 

```bash
$ openssl req -text -in fd.csr -noout -verify
verify OK
Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: C=PK, ST=ISB, L=ISB, O=fakecom, OU=fakecom, CN=*.example.com/emailAddress=abc@fake.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
```

Everything that you provided is showing here. If you find that anything is wrong, you can still regenerate your CSR.


<h2 id="5268c2edcf0f7ae7ce41e905564de177"></h2>

#### Self Signed Certificate

```bash
$ openssl x509 -in fd.csr -out fd.crt -req -signkey fd.key -days 3650
Signature ok
subject=/C=PK/ST=ISB/L=ISB/O=fakecom/OU=fakecom/CN=*.example.com/emailAddress=abc@fake.com
Getting Private key
```

`fd.crt` is our signed x509 certificate.


> X.509是密码学里公钥证书的格式标准。
> X.509证书已应用在包括TLS/SSL在内的众多网络协议里，同时它也用在很多非在线应用场景里，比如电子签名服务。
> X.509证书里含有公钥、身份信息（比如网络主机名，组织的名称或个体名称等）和签名信息（可以是证书签发机构CA的签名，也可以是自签名）


You don’t actually have to create a CSR in a separate step. User `openssl req` to create both CSR and CRT.

```bash
$ openssl req -new -x509 -days 3650 -key fd.key -out fd.crt
```

If you don’t wish to be asked any questions, use the `-subj` to provide the informations.

**One line command to self-assign**:

```bash
$ openssl req -new -x509 -days 3650 -key fd.key -out fd.crt \
    -subj "/C=PK/ST=ISB/L=ISB/O=fakecom/OU=fakecom/CN=*.example.com/emailAddress=abc@fake.com"
```

We can take a look inside the certificate.

```bash
$ openssl x509 -text -in fd.crt -noout
```


