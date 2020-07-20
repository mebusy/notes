
# Go Encrype/Decrytp

## HMAC SHA1

```go
"crypto/hmac"
"crypto/sha1"
"fmt"

key := []byte( conf.CHANNELS[channel].APP_SECRET  )
mac := hmac.New(sha1.New, key)
mac.Write([]byte(signString))
return fmt.Sprintf( "%x" , mac.Sum(nil)  )
```


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


### "crypto/md5"

```go
"crypto/md5"

m5 := fmt.Sprintf("%x", md5.Sum(data))
```



