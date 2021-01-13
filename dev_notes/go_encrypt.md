...menustart

- [Go Encrype/Decrytp](#a11036bc4335f8906456a2d883026810)
    - [HMAC SHA1](#37974fcc45ff56bd96019b499affde1b)
    - [Java's SHA256withRSA in GO way](#2aab9f8f7b040df1b0b94142b2d0a157)
        - ["crypto/md5"](#e825ff9cfb339d337f0bd935d0df0a14)
    - [SHA1WithRSA 公钥验签](#445d8588e7c1da8fc65aa336369ad632)
    - [SHA256WithRSA 公钥验证](#0ba4261ccbb4f819fba76d40a078bc26)

...menuend


<h2 id="a11036bc4335f8906456a2d883026810"></h2>


# Go Encrype/Decrytp

<h2 id="37974fcc45ff56bd96019b499affde1b"></h2>


## HMAC SHA1

```go
"crypto/hmac"
"crypto/sha1"
"fmt"

key := []byte( SECRET_KEY  )
mac := hmac.New(sha1.New, key)
mac.Write([]byte(signString))
return fmt.Sprintf( "%x" , mac.Sum(nil)  )
```


<h2 id="2aab9f8f7b040df1b0b94142b2d0a157"></h2>


## Java's SHA256withRSA in GO way

```go
    "encoding/pem"
    "crypto/sha256"
    "crypto/rsa"
    "crypto"
    "crypto/x509"
    "crypto/rand"
    "fmt"
    "server/conf"
    "log"
    "errors"
    "encoding/base64"





    fullPrivateKey := fmt.Sprintf( `
-----BEGIN RSA PRIVATE KEY-----
%s
-----END RSA PRIVATE KEY-----
` , conf.CHANNELS[channel].APP_IAP_PRIVATE)

    // log.Println( fullPrivateKey )

    block, _ := pem.Decode(  []byte( fullPrivateKey  )   )
    if block == nil {
        return "", errors.New("private key error")
    }

    // Public/Private, PKCS8/PKCS1
    privateInterface, err  := x509.ParsePKCS8PrivateKey( block.Bytes )
    if err != nil {
        log.Println(err)
        return "", err
    }
    pri := privateInterface.(*rsa.PrivateKey)

    h := sha256.New()
    h.Write([]byte( signString  ))
    d := h.Sum(nil)

    signature, err := rsa.SignPKCS1v15(rand.Reader, pri, crypto.SHA256, d)
    if err != nil {
        log.Println(err)
        return "",err
    }
    return base64.StdEncoding.EncodeToString(signature), nil
```

[RSA 加密/解密 source](https://github.com/polaris1119/myblog_article_code/blob/master/rsa/rsa.go)


<h2 id="e825ff9cfb339d337f0bd935d0df0a14"></h2>


### "crypto/md5"

```go
"crypto/md5"

m5 := fmt.Sprintf("%x", md5.Sum(data))
```

<h2 id="445d8588e7c1da8fc65aa336369ad632"></h2>


## SHA1WithRSA 公钥验签

```go
import (
	"crypto"
	"crypto/rsa"
	"crypto/sha1"
	"crypto/x509"
	"encoding/base64"
	"log"
)

/*
* 发送方: signString -> private key 签名 -> sig
* 接收方: signString -> sha1rsa + publickey 
*/
func oppoVerifySignature( public_key, signString string, sig string ) error {
    // public key
    k := public_key

    key, _ := base64.StdEncoding.DecodeString(k)
    re, err := x509.ParsePKIXPublicKey(key)
    pub := re.(*rsa.PublicKey)
    if err != nil {
        log.Println(err)
        return err
    }

    h := sha1.New()
    h.Write(  []byte(signString) )
    digest := h.Sum(nil)

    ds, _ := base64.StdEncoding.DecodeString(sig)
    err = rsa.VerifyPKCS1v15(pub, crypto.SHA1, digest, ds)
    // fmt.Println("verify:", err)
    if err != nil {
        log.Println(err)
        return err
    }
    return nil
}
```

<h2 id="0ba4261ccbb4f819fba76d40a078bc26"></h2>


## SHA256WithRSA 公钥验证

```go
/*
* 发送方: signString -> private key 签名 -> sig
* 接收方: signString -> sha1rsa + publickey 
*/
func VerifySignatureSHA256withRSA( public_key, signString string, sig string ) error {
    // public key
    k := public_key

    key, _ := base64.StdEncoding.DecodeString(k)
    re, err := x509.ParsePKIXPublicKey(key)
    pub := re.(*rsa.PublicKey)
    if err != nil {
        log.Println(err)
        return err
    }

    h := sha256.New()
    h.Write(  []byte(signString) )
    digest := h.Sum(nil)

    ds, _ := base64.StdEncoding.DecodeString(sig)
    err = rsa.VerifyPKCS1v15(pub, crypto.SHA256, digest, ds)
    // fmt.Println("verify:", err)
    if err != nil {
        log.Println(err)
        return err
    }
    return nil
}
```

