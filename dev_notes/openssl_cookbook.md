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
        - [Key and Certificate Conversion](#c1f061fc07e339060fdee68b6e6fe858)
            - [PEM and DER Conversion](#754014ce9cfa74c39214abce03284f0d)
            - [convert between PKCS#1 and PKCS#8](#e8759212e92e32d3654613a8bb64ccdb)
    - [Testing with OpenSSL](#bd19a0b75e268da9a5fed8ddd347fe26)
        - [Connecting to SSL Services](#0ee6bf1381cea193a44901bd6f6161d9)
        - [Extracting Remote Certificates](#6c59b3e66e386f8bd237466e9502a75e)
        - [Testing Protocol Support](#c0ba517e5697c8eadc30894c02ba239b)
        - [Testing Session Reuse](#f4f526e2ee7828bd47af449aaed0d1d2)
    - [Other Commands](#32fa66f13d05678402f1989484ea0327)
        - [rand](#34d1c35063280164066ecc517050da0b)
        - [dgst](#89a989347373b1b0a211f15dc1cee2af)
- [OpenSSH Key](#4d3e358489bdaf54b3f4a637f7c239c1)
    - [SSH RSA Public Key](#25d10e0e599a839f7973eb01bf1d4b8c)
    - [Convert between different formats...](#b877b734093e9001b4572816c5ed60bd)

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
$ openssl genrsa -out serv.key 2048
Generating RSA private key, 2048 bit long modulus
...................+++++
.......................+++++
e is 65537 (0x10001)
```

This key is in **PKCS1** ( Public Key Cryptography Standards ) format.

If you want to use passphrase, add `-aes128` (or `-aes192`, `-aes256`), and it's best to stay away from the other algorithms (DES, 3DES, and SEED).

```bash
$ openssl genrsa -aes128 -out serv.key 2048
```

Private keys are stored in the so-called **PEM** format, which is just text:

```bash
$ cat serv.key 
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
$ openssl rsa -in serv.key -pubout -out serv-public.key

$ cat serv-public.key
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuQgy4mnd07n137wNVcHE
...
+QIDAQAB
-----END PUBLIC KEY-----
```

If you want to generate the **obsoluted** `RSA PUBLIC KEY`, add `-RSAPublicKey_out`

<details>


```bash
$ openssl rsa -in serv.key -pubout -out serv-rsa-pub.key -RSAPublicKey_out
$cat serv-rsa-pub.key                
-----BEGIN RSA PUBLIC KEY-----
...
```

</details>

> The "RSA PUBLIC KEY" format was used in very early SSLeay, which evolved into OpenSSL, but obsoleted before 2000.
> Although this format is long obsolete, **OpenSSL still supports** it.
> "RSA PUBLIC KEY" format is the RSA-specific format from PKCS#1, 
> whereas "PUBLIC KEY" is the X.509 generic structure that handles numerous (and extensible) algorithm. 


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
$ openssl req -new -key serv.key -out serv.csr
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
$ openssl req -text -in serv.csr -noout -verify
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

If you’re installing a TLS server for your own use, you probably don’t want to go to a CA for a publicly trusted certificate. It’s much easier to just use a self-signed certificate.

```bash
$ openssl x509 -in serv.csr -out serv.crt -req -signkey serv.key -days 3650
Signature ok
subject=/C=PK/ST=ISB/L=ISB/O=fakecom/OU=fakecom/CN=*.example.com/emailAddress=abc@fake.com
Getting Private key
```

`serv.crt` is our signed x509 certificate.


> X.509是密码学里公钥证书的格式标准。
> X.509证书已应用在包括TLS/SSL在内的众多网络协议里，同时它也用在很多非在线应用场景里，比如电子签名服务。
> X.509证书里含有公钥、身份信息（比如网络主机名，组织的名称或个体名称等）和签名信息（可以是证书签发机构CA的签名，也可以是自签名）


You don’t actually have to create a CSR in a separate step. User `openssl req` to create both CSR and CRT.

```bash
$ openssl req -new -x509 -days 3650 -key serv.key -out serv.crt
```

If you don’t wish to be asked any questions, use the `-subj` to provide the informations.

**One line command to self-assign**:

```bash
$ openssl req -new -x509 -days 3650 -key serv.key -out serv.crt \
    -subj "/C=PK/ST=ISB/L=ISB/O=fakecom/OU=fakecom/CN=*.example.com/emailAddress=abc@fake.com"
```

We can take a look inside the certificate.

```bash
$ openssl x509 -text -in serv.crt -noout
```


<h2 id="c1f061fc07e339060fdee68b6e6fe858"></h2>

### Key and Certificate Conversion

Private keys and certificates can be stored in a variety of formats:

- Binary (DER) certificate
    - Contains an X.509 certificate in its raw form, using DER ASN.1 encoding.
- ASCII (PEM) certificate(s)
    - Contains a base64-encoded DER certificate, with `-----BEGIN CERTIFICATE-----` used as the header and `-----END CERTIFICATE-----` as the footer. 
- Binary (DER) key
    - Contains a private key in its raw form, using DER ASN.1 encoding. 
    - OpenSSL creates keys in its own traditional (SSLeay) format
    - There’s also an alternative format called PKCS#8 (defined in RFC 5208), but it’s not widely used.
    - OpenSSL can convert **to and from** PKCS#8 format using the `pkcs8` command.
- ASCII (PEM) key
    - Contains a base64-encoded DER key, sometimes with additional metadata(e.g., the algorithm used for password protection).
- PKCS#7 certificate(s)
    - It’s usually seen with .p7b and .p7c extensions and can include the entire certificate chain as needed. This format is supported by Java’s keytool utility.
- PKCS#12 (PFX) key and certificate(s)
    - A complex format that can store and protect a server key along with an entire certificate chain.
    - It’s commonly seen with .p12 and .pfx extensions. This format is commonly used in Microsoft products, but is also used for client certificates.


<h2 id="754014ce9cfa74c39214abce03284f0d"></h2>

#### PEM and DER Conversion

Convert X.509 certificate:

```bash
openssl x509 -in cert.cer -inform der -out cert.crt -outform pem
openssl x509 -in cert.crt -inform pem -out cert.cer -outform der
```

The syntax is identical if you need to convert private keys between DER and PEM formats, but different commands are used: `rsa` for RSA keys, and `dsa` for DSA keys.


<h2 id="e8759212e92e32d3654613a8bb64ccdb"></h2>

#### convert between PKCS#1 and PKCS#8

```bash
# #1 -> #8
openssl pkcs8 -in private-pkcs1.pem -topk8 -out private-pkcs8.pem -nocrypt
openssl pkcs8 -in private-pkcs1.pem -topk8 -out private-pkcs8-enc.pem
```
```bash
# #8 -> #1
openssl rsa -in private-pkcs8.pem -out private-pkcs1.pem
```


<h2 id="bd19a0b75e268da9a5fed8ddd347fe26"></h2>

## Testing with OpenSSL

<h2 id="0ee6bf1381cea193a44901bd6f6161d9"></h2>

### Connecting to SSL Services

OpenSSL comes with a client tool, this tool is similar to telnet or nc, in the sense that it handles the SSL/TLS layer **but** allows you to fully control the layer that comes next.

```bash
$ openssl s_client -connect openai.com:443
```

Once you type the command, you’re going to see a lot of diagnostic output,

followed by an opportunity to type whatever you want.

Because we’re talking to an HTTP server, the most sensible thing to do is to submit an HTTP request. 

```bash
HEAD / HTTP/1.0
HOST: openai.com

HTTP/1.1 200 OK
...
closed
```

Now, let’s go back to the diagnostic output. 

The first couple of lines show the information about the server certificate:

```bash
CONNECTED(00000006)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root G2
verify return:1
depth=1 C = US, O = Microsoft Corporation, CN = Microsoft Azure TLS Issuing CA 01
verify return:1
depth=0 C = US, ST = WA, L = Redmond, O = Microsoft Corporation, CN = *.azureedge.net
verify return:1
```

The next section in the output lists all the certificates presented by the server in the order in which they were delivered:


```bash
Certificate chain
 0 s:/C=US/ST=WA/L=Redmond/O=Microsoft Corporation/CN=*.azureedge.net
   i:/C=US/O=Microsoft Corporation/CN=Microsoft Azure TLS Issuing CA 01
 1 s:/C=US/O=Microsoft Corporation/CN=Microsoft Azure TLS Issuing CA 01
   i:/C=US/O=DigiCert Inc/OU=www.digicert.com/CN=DigiCert Global Root G2
```

For each certificate, the first line shows the subject and the second line shows the issuer information.

The next item in the output is the server certificate.

```bash
Server certificate
-----BEGIN CERTIFICATE-----
MIIIvDCCBqSgAwIBAgITMwCJVYBSn8/jQ4R/UwAAAIlVgDANBgkqhkiG9w0BAQwF
...
-----END CERTIFICATE-----
subject=/C=US/ST=WA/L=Redmond/O=Microsoft Corporation/CN=*.azureedge.net
issuer=/C=US/O=Microsoft Corporation/CN=Microsoft Azure TLS Issuing CA 01
```

The following is a lot of information about the TLS connection.

```bash
No client certificate CA names sent
Server Temp Key: ECDH, P-384, 384 bits
---
SSL handshake has read 4286 bytes and written 445 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    ...
```

The most important information here is the protocol version (TLS 1.2), and cipher suite used `ECDHE-RSA-AES256-GCM-SHA384`.


<h2 id="6c59b3e66e386f8bd237466e9502a75e"></h2>

### Extracting Remote Certificates

If you need the server certificate for any reason, you can copy it from the scroll-back buffer.

Or use this command line as a shortcut:

```bash
# Following command is for MacOSX. On Linux, you may replace `-n` with `--quiet`
echo | openssl s_client -connect openai.com:443 2>&1 | sed -n '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > openai.crt
```

```bash
$ cat openai.crt
-----BEGIN CERTIFICATE-----
MIIIvDCCBqSgAwIBAgITMwCJVYBSn8/jQ4R/UwAAAIlVgDANBgkqhkiG9w0BAQwF
...
-----END CERTIFICATE-----
```

<h2 id="c0ba517e5697c8eadc30894c02ba239b"></h2>

### Testing Protocol Support

By default, s_client will try to use the best protocol to talk to the remote server and report the negotiated version in output.

```bash
    Protocol  : TLSv1.2
```

If you need to test support for specific protocol versions

```bash
 -no_tls1           Disable the use of TLSv1
 -no_tls1_1         Disable the use of TLSv1.1
 -no_tls1_2         Disable the use of TLSv1.2
 -no_tls1_3         Disable the use of TLSv1.3

 -tls1              Just use TLSv1
 -tls1_1            Just use TLSv1.1
 -tls1_2            Just use TLSv1.2
 -tls1_3            Just use TLSv1.3
```

e.g.

```bash
$ openssl s_client -connect openai.com:443 -tls1_1
```

<h2 id="f4f526e2ee7828bd47af449aaed0d1d2"></h2>

### Testing Session Reuse

When coupled with the `-reconnect` switch, the s_client command can be used to test session reuse.

```bash
$ echo | openssl s_client -connect baidu.com:443 -reconnect 2>/dev/null |  grep 'New\|Reuse'
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Reused, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Reused, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Reused, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Reused, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Reused, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES128-GCM-SHA256
```

<h2 id="32fa66f13d05678402f1989484ea0327"></h2>

## Other Commands

<h2 id="34d1c35063280164066ecc517050da0b"></h2>

### rand

Generate random bytes, can be encoded as `-base64` or `-hex`

To generate a random password in hex format:

```bash
$ openssl rand -hex 20
a23b977ca0fac4ced01de8cb69f0dfb73bdb41ab
```

To generate the random password in base64:

```bash
$ openssl rand -base64 20
ocrioY+RhvmV3OfWl6D7BhyXmjY=
```

<h2 id="89a989347373b1b0a211f15dc1cee2af"></h2>

### dgst

Calculate hash

```bash
$ echo -m hello | openssl dgst -md5
8f5dbe1b32c6881ddc8a74238d52ef2a
$ echo -m hello | md5 # verify
8f5dbe1b32c6881ddc8a74238d52ef2a
```

```bash
$ echo -m hello | openssl dgst -sha1
9fe12ce55bf59bc5d099870e8bcc20a433e78bb8
$ echo -m hello | shasum # verify
9fe12ce55bf59bc5d099870e8bcc20a433e78bb8  -
```


<h2 id="4d3e358489bdaf54b3f4a637f7c239c1"></h2>

# OpenSSH Key

<h2 id="25d10e0e599a839f7973eb01bf1d4b8c"></h2>

## SSH RSA Public Key

An RSA public key formatted by OpenSSH , can be generated by  `ssh-keygen`


```bash
$ ssh-keygen -b 2048 -t rsa
```

SSH keys are used for secure connections across a network, usually they are all in one line.

```bash
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQB/nAmOjTmezNUDKYvEeIRf2YnwM9/uUG1d0BYsc8/tRtx+RGi7N2lUbp728MXGwdnL9od4cItzky/zVdLZE2cycOa18xBK9cOWmcKS0A8FYBxEQWJ/q9YVUgZbFKfYGaGQxsER+A0w/fX8ALuk78ktP31K69LcQgxIsl7rNzxsoOQKJ/CIxOGMMxczYTiEoLvQhapFQMs3FL96didKr/QbrfB1WT6s3838SEaXfgZvLef1YB2xmfhbT9OXFE3FXvh2UPBfN+ffE7iiayQf/2XR+8j4N4bW30DiPtOQLGUrH1y5X/rpNZNlWW2+jGIxqZtgWg7lTy3mXy5x836Sj/6L
```

The standard ssh2 file format for use in Secure Shell.

```bash
$ ssh-keygen -b 2048 -t rsa -e
```

- `-e` 
    - The export format is “RFC4716”

```bash
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




