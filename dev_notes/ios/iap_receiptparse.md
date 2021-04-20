
# Use Openssl To Parse IAP Receipt file

[How to Validate iOS In-App Purchase Receipts Locally](https://betterprogramming.pub/how-to-validate-ios-in-app-purchase-receipts-locally-ce57ba752cae)

## Get IAP Receipt Data from StoreKiet Receipt file

```swift
// get receipt data from StoreKit,  encode it by base64
        // Get the receipt if it's available
        if let appStoreReceiptURL = Bundle.main.appStoreReceiptURL,
            FileManager.default.fileExists(atPath: appStoreReceiptURL.path) {

            do {
                let receiptData = try Data(contentsOf: appStoreReceiptURL, options: .alwaysMapped)
                print(receiptData)
                let receiptString = receiptData.base64EncodedString(options: [])
                print( receiptString )
                // Read receiptData
            }
            catch { print("Couldn't read receipt data with error: " + error.localizedDescription) }
        }
```

<details>
<summary>
Save the receiptString (base64 encoded) to file , say `receipt.b64`
</summary>

```bash
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
```

</details>

And then we decode it in order to use openssl to parse it.

```bash
$ base64 -d receipt.b64 > receipt
```

receipt is pkcs7 DER stream. Now we can use openssl to analyze it.

```bash
$ openssl asn1parse -inform DER -in receipt -i
```

<details>
<summary>
Results:
</summary>

```bash
    0:d=0  hl=2 l=inf  cons: SEQUENCE          
    2:d=1  hl=2 l=   9 prim:  OBJECT            :pkcs7-signedData
   13:d=1  hl=2 l=inf  cons:  cont [ 0 ]        
   15:d=2  hl=2 l=inf  cons:   SEQUENCE          
   17:d=3  hl=2 l=   1 prim:    INTEGER           :01
   20:d=3  hl=2 l=  15 cons:    SET               
   22:d=4  hl=2 l=  13 cons:     SEQUENCE          
   24:d=5  hl=2 l=   9 prim:      OBJECT            :sha256
   35:d=5  hl=2 l=   0 prim:      NULL              
   37:d=3  hl=2 l=inf  cons:    SEQUENCE          
   39:d=4  hl=2 l=   9 prim:     OBJECT            :pkcs7-data
   50:d=4  hl=2 l=inf  cons:     cont [ 0 ]        
   52:d=5  hl=2 l=inf  cons:      OCTET STRING   
```

</details>

The raw receipt data is in indefinite length format(BER, not DER), to make it easier to understand, we will convert it to definite length.

```bash
# convert DER to PEM
# !!! PEM is just a base64 encoding of a DER-encoded stream surrounded with `-----BEGIN PKCS7-----`  `-----END PKCS7-----`
$ openssl pkcs7 -inform DER -in receipt > receipt.pkcs7
```
<details>
<summary>
$ cat receipt.pkcs7
</summary>

```PEM
-----BEGIN PKCS7-----
MIIGigYJKoZIhvcNAQcCoIIGezCCBncCAQExDzANBglghkgBZQMEAgEFADCCAVAG
CSqGSIb3DQEHAaCCAUEEggE9MYIBOTAPAgEAAgEBBAcMBVhjb2RlMAsCAQECAQEE
AwIBADAiAgECAgEBBBoMGGNvbS50ZW1wb3JhcnkuaXBhdGVzdGFwcDALAgEDAgEB
BAMMATEwEAIBBAIBAQQIV/+u/wQAAAAwHAIBBQIBAQQUl3/OWjErG+m3VSdOF/rE
IzdcUIkwCgIBCAIBAQQCFgAwIgIBDAIBAQQaFhgyMDIxLTA0LTE2VDEwOjU5OjMz
KzA4MDAwZAIBEQIBAQRcMVowDAICBqUCAQEEAwIBATAaAgIGpgIBAQQRDA9jb20u
dGVtcG9yYXJ5LmMwDQICBqcCAQEEBAwCODYwHwICBqgCAQEEFhYUMjAyMS0wNC0x
NlQxMDo1OTozM1owIgIBFQIBAQQaFhg0MDAxLTAxLTAxVDA4OjAwOjAwKzA4MDCg
ggN4MIIDdDCCAlygAwIBAgIBATANBgkqhkiG9w0BAQsFADBfMREwDwYDVQQDDAhT
dG9yZUtpdDERMA8GA1UECgwIU3RvcmVLaXQxETAPBgNVBAsMCFN0b3JlS2l0MQsw
CQYDVQQGEwJVUzEXMBUGCSqGSIb3DQEJARYIU3RvcmVLaXQwHhcNMjAwNDAxMTc1
MjM1WhcNNDAwMzI3MTc1MjM1WjBfMREwDwYDVQQDDAhTdG9yZUtpdDERMA8GA1UE
CgwIU3RvcmVLaXQxETAPBgNVBAsMCFN0b3JlS2l0MQswCQYDVQQGEwJVUzEXMBUG
CSqGSIb3DQEJARYIU3RvcmVLaXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQDbf5A8LHMP25cmS5O7CvihIT7IYdkkyF4fdT7ak9sxGpGAub/lDMs8uw5E
Yib6BCm2Sedv4BvmDWjNJW7Ddgj1SguuenQ8xKkLs89iD/u0vPfbhF4o60cN8e2L
rPWfsAk4o257yyZQChrhidFydgs5TMtPbsCzX7eVurmoXUp0q+9vQaV+CY26PT3N
cFfY7e/V2nfIkwQc7wmIeGXOgfKNcucHGm4mEvcysQ27OJBrBsT8DeWVUM2RyLol
9FjJjOFx20pF8y0ZlgNWgaZE7nV3W1PPeKxduj5fUCtcKYzdwtcqF98itNfkeKiv
qG2nwdpoLWbMzykLUCzjwvvmXxLBAgMBAAGjOzA5MA8GA1UdEwEB/wQFMAMBAf8w
DgYDVR0PAQH/BAQDAgKEMBYGA1UdJQEB/wQMMAoGCCsGAQUFBwMDMA0GCSqGSIb3
DQEBCwUAA4IBAQCyAOA88ejpYr3A1h1Anle5OJB3dlLSqEtwbrhnmfuzilWf7x0o
uF8q0XOfNUc3u0bTdhDy8GnszWKZcflgioRIOMS9i2cluatsM2Wt2MKaeEgP6czB
Jw3Gz2Q8bYBZM4zKNgYqERuNSc4I/2bARyhL61rBKwlWLKWqCQN7MjHc6IV4SM7A
xRIRag8Mri8Fym96ZH8gLHXmTLES0/3jH14NfbhY16B85H9jq5eaK8Mq2NCy4dVa
DTkbb2coqRKD1od4bZm9XrMK4JjO9urDjm1p67dAgT2HPXBR0cRdjaXcf2pYGt5g
djdS7P+sGV0MFS+KD/WJyNcrHR7sK5EFpz1PMYIBjzCCAYsCAQEwZDBfMREwDwYD
VQQDDAhTdG9yZUtpdDERMA8GA1UECgwIU3RvcmVLaXQxETAPBgNVBAsMCFN0b3Jl
S2l0MQswCQYDVQQGEwJVUzEXMBUGCSqGSIb3DQEJARYIU3RvcmVLaXQCAQEwDQYJ
YIZIAWUDBAIBBQAwDQYJKoZIhvcNAQELBQAEggEANCWPwVh5OV9tYnPG3hJTegxS
TS2pV0KWCuLOJkANX6Wsm902FFSAGqMf/MpaHFrNAptEPpnidSrI0pukwakYGZur
B85E2uTHUDZ4mWYc2u3f/bJTrKiHl/oDUhgt9MepCyGcW3oRJfFZyvFKqM+TccHo
jeL5YisNnDV3qFUrGKmeyel79gRR4e1xvedQ8Oaq3xEKVi6fNUaIrGKVBG8+ZeaY
ymtalHkqrWRWVfTkd60LTVTfLp1Mv3Ga9e25MDeIar5MG0TdOVhtZuBDWFASXp3o
lc+68bkm34qHSTVjwAjMuJs57MuzjEV89i5a2Jxr69rTbxI7slFFLWiVAHCLdA==
-----END PKCS7-----
```

</details>


Export the certs information:

```bash
openssl pkcs7 -print_certs -in receipt.pkcs7 > receipt.pkcs7.certs
```

## Verify The Receipt is Issued By Apple

Get the Google Apple root certificate:  https://www.apple.com/certificateauthority/

```bash
$ wget https://www.apple.com/appleca/AppleIncRootCertificate.cer
```

Now, use this OpenSSL command to convert it to a *.pem file.

```bash
$ openssl x509 -inform der -in  AppleIncRootCertificate.cer -out AppleIncRootCertificate.pem
```

Note, here the example receipt is issued by xcode, so we actually need use the testing certificate. You can get the StoreKitTestCertificate.cer from xcode.

```bash
# for this test receipt data only
$ openssl x509 -inform der -in  StoreKitTestCertificate.cer -out AppleIncRootCertificate.pem
```

Now we have the AppleIncRootCertificate as a *.pem, and we have the chain of certificates in the receipt in receipt.pkcs7.certs. We can now verify that the two match with this command:

```bash
$ openssl verify -CAfile receipt.pkcs7.certs AppleIncRootCertificate.pem
AppleIncRootCertificate.pem: OK
```


## Parse the ASN.1 Payload

```bash
$ openssl asn1parse -in receipt.pkcs7 -i
```

<details>
<summary>
Results:
</summary>

```bash
    0:d=0  hl=4 l=1674 cons: SEQUENCE
    4:d=1  hl=2 l=   9 prim:  OBJECT            :pkcs7-signedData
   15:d=1  hl=4 l=1659 cons:  cont [ 0 ]
   19:d=2  hl=4 l=1655 cons:   SEQUENCE
   23:d=3  hl=2 l=   1 prim:    INTEGER           :01
   26:d=3  hl=2 l=  15 cons:    SET
   28:d=4  hl=2 l=  13 cons:     SEQUENCE
   30:d=5  hl=2 l=   9 prim:      OBJECT            :sha256
   41:d=5  hl=2 l=   0 prim:      NULL
   43:d=3  hl=4 l= 336 cons:    SEQUENCE
   47:d=4  hl=2 l=   9 prim:     OBJECT            :pkcs7-data
   58:d=4  hl=4 l= 321 cons:     cont [ 0 ]
   62:d=5  hl=4 l= 317 prim:      OCTET STRING      [HEX DUMP]:31820139300F02010002010104070C0558636F6465300B02010102010104030201003022020102020101041A0C18636F6D2E74656D706F726172792E69706174657374617070300B02010302010104030C01313010020104020101040857FFAEFF04000000301C0201050201010414977FCE5A312B1BE9B755274E17FAC423375C5089300A02010802010104021600302202010C020101041A1618323032312D30342D31365431303A35393A33332B303830303064020111020101045C315A300C020206A50201010403020101301A020206A602010104110C0F636F6D2E74656D706F726172792E63300D020206A702010104040C023836301F020206A802010104161614323032312D30342D31365431303A35393A33335A3022020115020101041A1618343030312D30312D30315430383A30303A30302B30383030
  383:d=3  hl=4 l= 888 cons:    cont [ 0 ]
  387:d=4  hl=4 l= 884 cons:     SEQUENCE
  391:d=5  hl=4 l= 604 cons:      SEQUENCE
  395:d=6  hl=2 l=   3 cons:       cont [ 0 ]
  397:d=7  hl=2 l=   1 prim:        INTEGER           :02
  400:d=6  hl=2 l=   1 prim:       INTEGER           :01
  403:d=6  hl=2 l=  13 cons:       SEQUENCE
  405:d=7  hl=2 l=   9 prim:        OBJECT            :sha256WithRSAEncryption
```

</details>

Now, luckily, we only need to focus on the gibberish at the top of the file. We’re interested in the section entitled `pkcs7-signedData` !

The hex dump, as it’s so named, is the payload of the signed receipt that has the goods we’re after and is stored in a format known as ASN.1. We use this OpenSSL command to extract the section we want. Look back at the dump to understand the figures. I want to start at 62 + 4 and length of 317

```bash
$ openssl asn1parse -length 317 -offset 66 -in receipt.pkcs7 -i
```

<details>
<summary>
We get the receipt data, which is made up of a number of fields.
</summary>

```bash
    0:d=0  hl=4 l= 313 cons: SET
    4:d=1  hl=2 l=  15 cons:  SEQUENCE
    6:d=2  hl=2 l=   1 prim:   INTEGER           :00
    9:d=2  hl=2 l=   1 prim:   INTEGER           :01
   12:d=2  hl=2 l=   7 prim:   OCTET STRING      [HEX DUMP]:0C0558636F6465
   21:d=1  hl=2 l=  11 cons:  SEQUENCE
   23:d=2  hl=2 l=   1 prim:   INTEGER           :01
   26:d=2  hl=2 l=   1 prim:   INTEGER           :01
   29:d=2  hl=2 l=   3 prim:   OCTET STRING      [HEX DUMP]:020100
   34:d=1  hl=2 l=  34 cons:  SEQUENCE
   36:d=2  hl=2 l=   1 prim:   INTEGER           :02
   39:d=2  hl=2 l=   1 prim:   INTEGER           :01
   42:d=2  hl=2 l=  26 prim:   OCTET STRING      [HEX DUMP]:0C18636F6D2E74656D706F726172792E69706174657374617070
   70:d=1  hl=2 l=  11 cons:  SEQUENCE
   72:d=2  hl=2 l=   1 prim:   INTEGER           :03
   75:d=2  hl=2 l=   1 prim:   INTEGER           :01
   78:d=2  hl=2 l=   3 prim:   OCTET STRING      [HEX DUMP]:0C0131
   83:d=1  hl=2 l=  16 cons:  SEQUENCE
   85:d=2  hl=2 l=   1 prim:   INTEGER           :04
   88:d=2  hl=2 l=   1 prim:   INTEGER           :01
   91:d=2  hl=2 l=   8 prim:   OCTET STRING      [HEX DUMP]:57FFAEFF04000000
  101:d=1  hl=2 l=  28 cons:  SEQUENCE
  103:d=2  hl=2 l=   1 prim:   INTEGER           :05
  106:d=2  hl=2 l=   1 prim:   INTEGER           :01
  109:d=2  hl=2 l=  20 prim:   OCTET STRING      [HEX DUMP]:977FCE5A312B1BE9B755274E17FAC423375C5089
  131:d=1  hl=2 l=  10 cons:  SEQUENCE
  133:d=2  hl=2 l=   1 prim:   INTEGER           :08
  136:d=2  hl=2 l=   1 prim:   INTEGER           :01
  139:d=2  hl=2 l=   2 prim:   OCTET STRING      [HEX DUMP]:1600
  143:d=1  hl=2 l=  34 cons:  SEQUENCE
  145:d=2  hl=2 l=   1 prim:   INTEGER           :0C
  148:d=2  hl=2 l=   1 prim:   INTEGER           :01
  151:d=2  hl=2 l=  26 prim:   OCTET STRING      [HEX DUMP]:1618323032312D30342D31365431303A35393A33332B30383030
  179:d=1  hl=2 l= 100 cons:  SEQUENCE
  181:d=2  hl=2 l=   1 prim:   INTEGER           :11
  184:d=2  hl=2 l=   1 prim:   INTEGER           :01
  187:d=2  hl=2 l=  92 prim:   OCTET STRING      [HEX DUMP]:315A300C020206A50201010403020101301A020206A602010104110C0F636F6D2E74656D706F726172792E63300D020206A702010104040C023836301F020206A802010104161614323032312D30342D31365431303A35393A33335A
  281:d=1  hl=2 l=  34 cons:  SEQUENCE
  283:d=2  hl=2 l=   1 prim:   INTEGER           :15
  286:d=2  hl=2 l=   1 prim:   INTEGER           :01
  289:d=2  hl=2 l=  26 prim:   OCTET STRING      [HEX DUMP]:1618343030312D30312D30315430383A30303A30302B30383030
```

</details>


## Receipt Fields

```bash
   34:d=1  hl=2 l=  34 cons:  SEQUENCE
   36:d=2  hl=2 l=   1 prim:   INTEGER           :02
   39:d=2  hl=2 l=   1 prim:   INTEGER           :01
   42:d=2  hl=2 l=  26 prim:   OCTET STRING      [HEX DUMP]:0C18636F6D2E74656D706F726172792E69706174657374617070
   70:d=1  hl=2 l=  11 cons:  SEQUENCE
   72:d=2  hl=2 l=   1 prim:   INTEGER           :03
   75:d=2  hl=2 l=   1 prim:   INTEGER           :01
   78:d=2  hl=2 l=   3 prim:   OCTET STRING      [HEX DUMP]:0C0131
   83:d=1  hl=2 l=  16 cons:  SEQUENCE
```

- Each [Receipt Field](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html) has 3 parts:
    - ASN.1 object type
    - ASN.1 tag
    - ASN1 value

We known type 2 is bundle  identifier, let print it :

```bash
$ echo '0C18636F6D2E74656D706F726172792E69706174657374617070' | xxd -r -p

com.temporary.ipatestapp
```

```swift
// some fields
switch attributeType {
  case 0x2: // The bundle identifier
  case 0x3: // Bundle version
  case 0x4: // Opaque value
  case 0x5: // Computed GUID (SHA-1 Hash)
  case 0x0C: // Receipt Creation Date
  case 0x11: // IAP Receipt, important, more receipt detail
  case 0x13: // Original App Version
  case 0x15: // Expiration Date
  default: // Ignore other attributes in receipt
}
```


## Verify Device

- Attribute 5 (`977FCE5A312B1BE9B755274E17FAC423375C5089`) is a SHA-1 hash of 3 key values
    - Device identifier
    - Opaque value (Attribute 4)
        - for may example, `57FFAEFF04000000`
    - Bundle identifier
        - for my example, `0C18636F6D2E74656D706F726172792E69706174657374617070`
- The device identifier on which the receipt was created, which I know in my case is `c68bce287e27494aa082acecb9328171` 
    ```swift
    extension Data {
        // Data, byte array to hex string
        var hexDescription: String {
            return reduce("") {$0 + String(format: "%02x", $1)}
        }
    } 

    // ...

    func getDeviceIdentifier() -> Data {
          let device = UIDevice.current
          var uuid = device.identifierForVendor!.uuid
          let addr = withUnsafePointer(to: &uuid) { (p) -> UnsafeRawPointer in
            UnsafeRawPointer(p)
          }
          let data = Data(bytes: addr, count: 16)
          return data
    }
    ```
- Now I have the entire data to calculate the hash

```bash
$ echo "c68bce287e27494aa082acecb932817157FFAEFF040000000C18636F6D2E74656D706F726172792E69706174657374617070" |  xxd -r -p | openssl dgst -sha1 -hex
977fce5a312b1be9b755274e17fac423375c5089
# exactly same as attribute 5 !
```

## Attribute 17

Moving ahead, within the receipt, you have more ASN.1 packets.  They are in Attribute 17.







