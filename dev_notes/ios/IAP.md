...menustart

- [IAP](#0390e809a5857323f39ee1814afca57d)
    - [IAP Process](#f05fa4d8ea2700881fb6150bac6cdf69)
        - [Load In-App identifiers](#0581a394c7c5b9dbd1f282ec2281c044)
        - [Fetch Product Info](#0cd9982c3996eda6c09deadde434e851)
        - [Show In-App UI](#a6f26c670dcdf3da2ef9a710e89d9912)
        - [Request Payment](#3f89d0fc745c3be993b761e585311976)
        - [Process Transaction](#9e9b93d51ddf2aa1ede1858c33f1ecd6)
        - [Unlock Content](#dee5f9cf944eaaab05258db5154b9ac0)
        - [Finish Transaction](#de6faa534d9385782a88506d048e58f9)
- [Advanced StoreKit](#2d8b2b36933cde770a9250f72b4dff90)
    - [Receipt validation](#45f6fa235894e559bbfed4c294aaa42c)
        - [On-device validation](#e0f2a22d127bdcb42f3437e829be742c)
            - [Locate the receipt using Bundle API](#008f1851f21efaf5b56749dfa20c5dc6)
            - [Tips for using OpenSSL](#81587df5490a6a5ed548790720db2256)
            - [Downloading pre-built solutions](#621e5d2c86f816065245a62f6c68a898)
            - [Certificate verification](#3a5f295a20d45ac638e2eed855dd6804)
            - [Receipt payload](#a57740e6c71bea91d87abc940ac67f42)
            - [Verify application](#f76f324bde9b4e65f1251223a787db65)
            - [Verify device](#6f40f01ca4e4a270e460a398370f25f2)
        - [In-App Purchase Process](#11fd4b761490e26bfc03282dad341fd5)
            - [Processing transactions](#803016c6af90651418c47284500b5357)
        - [On-Device In-App Purchase State](#4f3f99d97127265360c73642828cdbda)
            - [In-app purchase attributes](#5db82a216102ce1d17d687b83ab34c87)
            - [Unlocking content on-device](#95605d378317855617cfe23110dd6a66)
            - [Subscription: Does the user have an active subscription?](#6b95b2f7cbcb9954a1d2bb2ede0b9c94)
            - [Subscription:  Caveat](#a11873e55117e863f3fa9bf9111797ad)
            - [Receipt Refresh on iOS](#08cb56eeb715e8a6c37332633774221b)
            - [Receipt Refresh on macOS](#f325ffdc194c967be1041f47a4303582)
        - [Receipt Tips](#45db248d4b941523cfe553958f42497b)
            - [Restoring transactions vs. refreshing receipt](#fddcd7391aeb092c0a61b433f627eb93)
            - [Switching to subscriptions](#68a460ec9852ff81d8f5bfd73b9502ea)
        - [Finish the transaction](#03f5910152461e582cf8cd03b4490af1)
        - [Server-Side Receipt Validation](#331b5abc7e7efd004823b27dec6b5fe7)
            - [Verifying a purchase on your server](#bd2a595308cde34bbfce510a813a5c3b)
            - [Unlocking content on your server](#d893bbd350ae9e58d3ca5bbdd31f667d)
            - [Does the user have an active subscription?](#21a7bf8de8a8188401033b1714247992)
    - [Maintaining subscription state](#87bf076f38bc5a9288b536cbc7593a83)
    - [Developing with the Sandbox](#74c9628ca548f9f12d6104c8f2524c90)
        - [The Sandbox](#d8d54e1efcbc1ea594cbb4167576afb3)
            - [Setting up the test environment](#46e951d214c2ed98e37d9b65f91f0734)
            - [App review considerations](#8109b0c0205566f624c6df98ca2c431c)
            - [Server notifications](#601c6fb1a4ee18105f8a5159346c6dfa)

...menuend


<h2 id="0390e809a5857323f39ee1814afca57d"></h2>


# IAP

<h2 id="f05fa4d8ea2700881fb6150bac6cdf69"></h2>


## IAP Process

- Load In-App identifiers
- Fetch Product Info
    - using those identifiers , you can fetch localized product information from App store
- Show In-App UI
    - once you have that localized information for the products, you can display in-app UI to the user
- Request Payment
    - the UI gives user an opportunity to tap that Buy button and agree to purchase it
    - at which point it's up to you to go ahead and request a payment
    - the user then , elects to buy your IAP and authenticate the payment
- Process Transaction
    - And it's up to you, to then process the transaction that comes back from Storekit
- Unlock Content
    - Once the transaction's been processed, it's up to you to unlock the content. 
- Finish Transaction
    - And finally, the last step is to finish the transaction.

<h2 id="0581a394c7c5b9dbd1f282ec2281c044"></h2>


### Load In-App identifiers 

- when it comes to loading these identifiers  in your applications, you can do it a couple of ways.
    - Firstly, you can just bake them directly into your application
    - Or the other way, of course, is to maybe fetch them from your own server.
- anyways you will have this set of strings

<h2 id="0cd9982c3996eda6c09deadde434e851"></h2>


### Fetch Product Info  

```swift
let request = SKProductsRequest( productIndentifiers : identifierSet )
request.delegate = self
request.start()
```

Now, you've set a delegate method on this so you'll get a response in the `didReceive` response callback

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_fetch_product_info.png)

- one more important point, here, just to highlight, is that you shouldn't cache the SKProduct that comes back in this point.
- It's really important that you get up to date product information, by performing these requests regularly.
- Because things like currency can fluctuate. You know, a user might log out, log into a different store front.


<h2 id="a6f26c670dcdf3da2ef9a710e89d9912"></h2>


### Show In-App UI 

- https://developer.apple.com/in-app-purchase/
- There has useful tips about how to format this particular page in a way that can, you know, improve your sales.
- One tip, though, just on formatting the product price.
    - So, when it comes to the product price, this is the technique you can use to actually display that in your UI. 
    - Create a number formatter object. Set the number style to be the currency style.

```swift
let formatter = NumberFormatter()
formatter.numberStyle = .currency
formatter.locale = product.priceLocale // Not the device locale!
let formattedString = formatter.string( from: product.price )
```

- Another point, here, don't perform any currency conversion yourself.  
- You can let StoreKit handle all this for you.

<h2 id="3f89d0fc745c3be993b761e585311976"></h2>


### Request Payment

- You take that SKProduct that the user's agreed to buy, pass it into an SKPayment initializer to create a payment object.
- Then, you add that payment to the SKPaymentQueue's default queue.

```swift
let payment = SKPayment(product: product)
SKPaymentQueue.default().add(payment)
```

- Now, as soon as you add the payment to the default queue, the user sees this great new looking in-app purchase payment sheet. So, this is new in iOS 11.
- And the user, of course, can just authenticate the purchase using Touch ID, and then, continue using your app. 

Now, at this point, I'll just take a quick sidestep to talk a bit about detecting irregular activity.

- For applications with their own account management 
- Provide an `opaque identifier` for `your user's account`


```swift
let payment = SKPayment(product: product)
payment.applicationUsername = hash( yourCustomerAccountName )
SKPaymentQueue.default().add(payment)
```

<h2 id="9e9b93d51ddf2aa1ede1858c33f1ecd6"></h2>


### Process Transaction

- Right at the beginning of your application lifecycle. 
    - And here, I'm doing it at the `didFinishLaunchingWithOptions` app delegate method.
    - It's important to set a transaction observer onto the SKPayment queue.

```swift
SKPaymentQueue.default().add(self)
return true 
```

- here I'm adding the actual AppDelegate, itself, as my SKPayment transaction observer. 
- But you could use another object if you want to actually monitor these transactions. 
- The really important thing here, is that it's happening as early on in the application lifecycle, as possible. 
    - See, transactions can come into this transaction observer any point during your application lifecycle.
- So, make sure that you're registering it right at the start.
- But once that's registered, you're ready to start receiving transactions in the callbacks.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_process_transaction_1.png)

- There's this one callback updated transactions, which is kind of the center of where this all happens.
- You receive an array of transactions that come in, and you can check the transaction state on each of these transactions.
- And you'll look for a transaction in the purchased state.
    - This is a transaction that's StoreKit deems appropriate for you to go ahead and **check for validity** and unlock content for, accordingly. 
- There are some other states here, that we won't go into in this talk. 
    - But one of the ones that I will call out, is the deferred state.
    - A transaction can come through in a deferred state if the user has asked to buy turned on. 
    - So, a child might ask to buy an in-app purchase and a request goes to their parent for approval to actually approve the purchase.
- So, it's important if something comes through in this deferred state, while they're waiting for an approval, that you allow access to the application.
- Allow them to keep using your app, and don't let them get stuck on any kind of modal loading spinners or things like that. 
- In order to test out deferred transactions, we provide a way for you to do this.
    - You can create a mutable payment object.
    - And you can set the simulatesAskToBuy flag on this object. 
    - Now, this is effective when you're using the Sandbox environment.  

```swift
let payment = SKPayment(product: product)
payment.simulatesAskToBuyInSandbox = true 
SKPaymentQueue.default().add(payment)
```

When it comes to handling errors, couple of points to remember. 

- Now, not all errors that come through this process are equal.
- And that means you really need to pay attention to the error code that comes through with a transaction.
- Now, once a transaction comes through in the purchased state, I mentioned that it's important for you to verify that transaction. 
    - Well, we use the application receipt to do this
    - it's a trusted record of the app and any in-app purchases that have occurred for a particular application. 
        - Trusted record of app and IAPs
        - Stored on device
        - Issued by the App Store
        - Singed and verifiable
        - For you app, on that device only
            - So, this receipt document can't be shared across devices.
- To be sure that the document that you're using to check these transactions is indeed a valid one, you do what we call receipt validation.
- Receipt validation can be done a couple of ways.
    - You can do it directly on the user's device using on device validation.
    - The other way is to use server to server validation. 
- Once you've confirmed that this receipt is an authentic document, you can go ahead and read in transactions and ensure that this transaction that's come through in this process is present in the receipt.

<h2 id="dee5f9cf944eaaab05258db5154b9ac0"></h2>


### Unlock Content

- If you are downloading content for in-app purchases, there's a couple of ways you can do this.
- Apple actually offers two techniques for you to use, as well.
    - on-demand resources
    - hosted in-app purchase downloadable content
        - you can associate downloadable content through iTunes Connect that's accessed through the SKProduct object, directly. 

<h2 id="de6faa534d9385782a88506d048e58f9"></h2>


### Finish Transaction

- it's important to finish all transactions that come through this process.
    - if downloading hosted content, wait until after the download completes
- Even if they're in like an error state, you got to finish all transactions that come through in this flow.
    - And that includes when you're dealing with auto-renewable subscriptions. Any renewal transactions that come in this flow, as well.
- Otherwise , the payment will stay in the queue.

```swift
SKPaymentQueue.default().finishTransaction(transaction)
```

- When you're in app review, you must have a Restore button if you've got non-consumable or auto-renewable subscription products in your application. 
    - And this Restore button has to be a separate button from the actual purchase button. 
- So, if you're selling consumable products or non-renewing subscriptions, you've got to persist the state of those things, yourself. 
- In order to actually restore them, this is the API for it. It's `restoreCompletedTransactions` as the method, and it's on the default payment queue.
    - If you call that, that's going to cause all the completed transactions in those categories to reappear on the updated transactions callback. So, you can just do the same process that we just saw, check for them being in the purchase state, do receipt validation, unlock all the features accordingly. 
    

```swift
SKPaymentQueue.default().restoreCompletedTransaction()
```

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_restore_completed_transactions.png)

---


<h2 id="2d8b2b36933cde770a9250f72b4dff90"></h2>


# Advanced StoreKit

<h2 id="45f6fa235894e559bbfed4c294aaa42c"></h2>


## Receipt validation

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_validate_receipt_2ways.png)

- 订阅 需要用到服务器， 以维护在不同设备上的订阅状态


```swift
func application(application: UIApplication, didFinishLaunchingWithOptions
    launchOptions: [NSObject: AnyObject]?) -> Bool {
    SKPaymentQueue.default().add(self)
    return true
}
```

```swift
func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions:
    [SKPaymentTransaction]) {
    for transaction in transactions {
        switch transaction.transactionState {
        case .purchased:
            // Validate the purchase
        }
    }
}
```

- On-device validation
    - Unlock features and content within the app
- Server-to-server validation
    - Online validation through a request to the App Store
    - Unlock features/subscription state on your server

**Do not use online validation directly from the device**

<h2 id="e0f2a22d127bdcb42f3437e829be742c"></h2>


### On-device validation 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_receipt_0.png)

- The basics
    - Stored in the app bundle
        - API to get the path
    - Single file
        - Purchase data
            - 包含有程序的所有购买数据，和已经发生的IAP购买
        - Signature to check authenticity
- Standards 工业标准
    - Signing
        - PKCS#7 Cryptographic Container
    - Data Encoding
        - ASN.1
    - Options for verifying and reading
        - OpenSSL, asn1c, and more
            - OpenSSL is a framework that not only provides the functionality for secure web traffic tunneling, it also includes functions to be able to read in the data encoding from an ASN.1 payload and also check the signing on a cryptographic container like this. 
        - Create your own

<h2 id="008f1851f21efaf5b56749dfa20c5dc6"></h2>


#### Locate the receipt using Bundle API

- 读取 receipt对象的 加密二进制数据

```swift
// Locate the file
guard let url = Bundle.main.appStoreReceiptURL else { // Handle failure
    return
}
// Read the contents
let receipt = Data(contentsOf: url)

```



<h2 id="81587df5490a6a5ed548790720db2256"></h2>


#### Tips for using OpenSSL

- OpenSSL doesn't actually ship with iOS. You have to build it and include it in your app yourself.
- Build your own static library (.a file)
    - Not a dynamic library
- Include Apple Root CA Certificate
    - Available online
        - When it comes to the actual certificate check, you can download the Apple Root certificate authority's certificate from the Apple site.
        - And you can use that certificate to actually perform that check using OpenSSL to see that it is a verified document from Apple. 
    - If bundled in app, watch out for expiry
- Documentation online

<h2 id="621e5d2c86f816065245a62f6c68a898"></h2>


#### Downloading pre-built solutions

- maybe download a pre-build solution from github 
- Convenience comes at a price
    - Reusing code brings with it bugs and vulnerabilities
    - Single exploit affects many
- It’s **your** revenue stream
    - Make decisions that suit your product
    - Know and own the risks

<h2 id="3a5f295a20d45ac638e2eed855dd6804"></h2>


#### Certificate verification

- When you're verifying the receipt -- the actual certificate used to sign the receipt, a couple of tips here.
- **Do not check the expiry date of the certificate relative to current date**
    - Compare expiry date to purchase date of the transaction
    - 在生成收条时，证书是否有效




<h2 id="a57740e6c71bea91d87abc940ac67f42"></h2>


#### Receipt payload




![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_receipt_payload.png)

- Series of attributes
    - Type
    - Value
    - (Version)


<h2 id="f76f324bde9b4e65f1251223a787db65"></h2>


#### Verify application

- 现在你已经检查实际文件是否已经使用正确的Apple证书进行签名, 你需要确定进行签名的程序就是用户运行的程序。
    - 使用 type2 / type3
- Check the bundle identifier
- Check the bundle version
- Use **hardcoded values**
    - Not Info.plist values, plist 很容易被伪造修改

<h2 id="6f40f01ca4e4a270e460a398370f25f2"></h2>


#### Verify device

- 接下来的步骤时 检查用户适用的设备 是否与文件匹配
    - use type4 / type5 
    - only type5 need to check

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_receipt_payload2.png)

- Attribute 5 is a SHA-1 hash of three key values
    - Bundle identifier
    - Device identifier
        - 提供API 读取?
    - Opaque value (Attribute 4)
        - it's a little bit of cryptographic entropy.
        - A bit of secret salt that allows that SHA-1 hash to change over time, even the bundle ID and the device ID aren't changing. 
- Unique to your app on this device
    - this SHA-1 hash is unique to this app on the device. ?
- Create hash using **hardcoded** values, compare it to the one in type number 5.

So now you've done those three checks. That's the process of validating the receipt on the device.



<h2 id="11fd4b761490e26bfc03282dad341fd5"></h2>


### In-App Purchase Process


<h2 id="803016c6af90651418c47284500b5357"></h2>


#### Processing transactions

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_process_transactions.png)

- 现在你知道这是一个可信文件，可以从它读取更多信息。
- So let's take a look at the next step which is to actually update state and inspect the contents of these in-app purchases inside the receipt.

<h2 id="4f3f99d97127265360c73642828cdbda"></h2>


### On-Device In-App Purchase State

<h2 id="5db82a216102ce1d17d687b83ab34c87"></h2>


#### In-app purchase attributes

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_iap_attributes.png)

- The receipt contains a specific type, type 17 for every transaction that occurs for this user on this device.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_attributes_17.png)

- Now in each type 17, the actual payload is another ASN.1 encoded container.
- So we have things like a quantity, a product identifier, a transaction ID. 
    - these are values that you can use to verify that a transaction exists in the real world. 
- One more to call out while I'm here is type 1708. 
    - This is particularly important if you're dealing with auto renewable subscriptions.
    - This contains the expiry date for a particular transaction for a particular billing period. 
- For more types:  see *Receipt Validation Programming Guide*



<h2 id="95605d378317855617cfe23110dd6a66"></h2>


#### Unlocking content on-device

- 现在你可以读出这些交易信息，你可以适用这些信息来核实它们是否与 StoreKit 告诉你的用户购买内容一致

- Transaction will appear in updatedTransactions callback
    - Transaction observer must be registered early in lifecycle
- Receipt payload contains in-app purchase transactions
    - Verify transaction in updatedTransactions callback is present in a receipt transaction
    - So you can use things like the transaction ID, the purchase date, the product identifier that it's saying the user bought, and if you can verify that there's a transaction that matches then great. You can trust the transaction that StoreKit's telling you.



<h2 id="6b95b2f7cbcb9954a1d2bb2ede0b9c94"></h2>


#### Subscription: Does the user have an active subscription?

- Valid receipt ≠ subscribed
- Filter transactions by originalTransactionId
    - 进行分组
    - Matches the first in-app purchase for that subscription
- Check matching transactions for latest expiry date
    - Type 1708
- If there’s no valid transaction, can refresh receipt
    - Repeat above steps


<h2 id="a11873e55117e863f3fa9bf9111797ad"></h2>


#### Subscription:  Caveat

- For determining if subscription is valid, inspect
    - Purchase date
    - Expiry date
    - System date
- if you're doing this purely on the device, the only data you actually have to compare these to is the user system data.
- Caveat for on-device subscription state
    - Device clock could be wound back!
        - So what's stopping the user from just winding their clock back and putting themselves into an active subscription period? 
        - Not a lot, unfortunately.
    - So if this is a problem for you, it's probably likely that you're going to need to look at some kind of server side solution.

---

<h2 id="08cb56eeb715e8a6c37332633774221b"></h2>


#### Receipt Refresh on iOS

- If the receipt doesn’t exist or is invalid, refresh the receipt using StoreKit
- Receipt refresh will require network
- Store sign-in will be required
- Avoid continuous loop of validate-and-refresh
    - 因为这会反复提示用户登录， 只应该发送一次请求

```swift
let request = SKReceiptRefreshRequest() 
request.delegate = self 
request.start()
```

<h2 id="f325ffdc194c967be1041f47a4303582"></h2>


#### Receipt Refresh on macOS

- If the receipt is invalid
- Receipt refresh will require network
- Store sign-in will be required
- Exit app with code 173 to refresh receipt
    - `exit(173)`

<h2 id="45db248d4b941523cfe553958f42497b"></h2>


### Receipt Tips

<h2 id="fddcd7391aeb092c0a61b433f627eb93"></h2>


#### Restoring transactions vs. refreshing receipt

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_restore_vs_refresh.png)

- you'll notice that consumable products are absent from both of these types of requests.
- If you're dealing with consumable product  purchases, they're just going to appear both in the updated transactions and on the receipt at the time of purchase.
- So you kind of have that one chance to actually verify the consumable product and it won't be restored for either of these calls.

<h2 id="68a460ec9852ff81d8f5bfd73b9502ea"></h2>


#### Switching to subscriptions

- Now one other tip for dealing with receipts is if you're looking to switch to subscriptions, maybe you've got a paid application and you want to switch it to being a subscription model, you can use this type 19 value in the application receipt.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_type19.png)

- This contains the original application version.
    - you can use this application version that a user originally downloaded as kind of a gate to know as to whether you need to provide a content based on a paid app or based on a subscription.
    - You know it's not a great experience if you've paid for an application and then suddenly you lose access to that functionality you paid for if it's now a subscription model.
    - So use type 19 as a bit of a gate to be able to supply that.
- Know whether the app was purchased as paid version, or is a subscription version


<h2 id="03f5910152461e582cf8cd03b4490af1"></h2>


### Finish the transaction

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_finish_transaction.png)

- Finish all transactions once content is unlocked
    - If downloading hosted content, wait until after the download completes
- Includes all auto-renewable subscription transactions
- Otherwise, the payment will stay in the queue
- Subscription billing retry depends on up-to-date information about transaction
    - 关于订阅结算重试，我们有一个特定的逻辑： 如果你使用自动续约订阅，很重要的一点，你必须finish these transactions.
    - 这样，如果出现任何类型的结算错误，我们的订阅结算重试逻辑可以继续尝试，并且向用户的信用卡收费。


<h2 id="331b5abc7e7efd004823b27dec6b5fe7"></h2>


### Server-Side Receipt Validation

<h2 id="bd2a595308cde34bbfce510a813a5c3b"></h2>


#### Verifying a purchase on your server

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_server_validate.png)

- Allows your servers to validate the receipt
    - Your server sends the receipt to the App Store
    - Endpoint is `verifyReceipt`
- Response is in JSON
    - Returns status on whether receipt is valid or not
- AGAIN: **Never send the receipt directly from your app to the App Store server**
    - 只有在你的服务器 与 App Store 之间的通道上 进行这些处理才是安全的
- these are whole steps to validate receipt by server, it is very simple.
    - 下一步就是，你如何 解锁内容，并检查交易

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_server_validate2.png)

<h2 id="d893bbd350ae9e58d3ca5bbdd31f667d"></h2>


#### Unlocking content on your server

- In addition to receipt validity, `verifyReceipt` returns  
    - Latest decoded application receipt
- Contains array of in-app purchase transactions
    - Verify product in the `updatedTransactions` callback on device is present in a transaction
- Tell the device to finishTransaction()

<h2 id="21a7bf8de8a8188401033b1714247992"></h2>


#### Does the user have an active subscription?

- Filter transactions by `originalTransactionId`
    - Matches the first IAP for taht subscription
- Check matching transactions for latest expiry date
    - 从app服务器返回的是最新的receipt副本，你不能再进行刷新操作


<h2 id="87bf076f38bc5a9288b536cbc7593a83"></h2>


## Maintaining subscription state

- particularly on the server


<h2 id="74c9628ca548f9f12d6104c8f2524c90"></h2>


## Developing with the Sandbox

<h2 id="d8d54e1efcbc1ea594cbb4167576afb3"></h2>


### The Sandbox

- Environment for testing purchases during development
- Based on certificate used to sign your application

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_sandbox_certificate.png)

- Can request expired and/or revoked receipts
    - 以进行不同的方式处理
- Time contraction for subscriptions
- There's a different endpoint as well when it comes to server-to-server validation. We provide a different url for that verify receipt endpoint. 

<h2 id="46e951d214c2ed98e37d9b65f91f0734"></h2>


#### Setting up the test environment

- Setup in iTunes Connect
    - Create test user
    - Enter products for sale
- Build and sign your app
- Buy products
    - Sign in with test user when prompted
- macOS only: Launch app from Finder once to fetch receipt

<h2 id="8109b0c0205566f624c6df98ca2c431c"></h2>


#### App review considerations

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/IAP_server_side_app_review.png)

- Try the production environment
- If receipt is from Sandbox
    - Receive error 21007
- Then try against Sandbox

<h2 id="601c6fb1a4ee18105f8a5159346c6dfa"></h2>


#### Server notifications

- Not separate production and Sandbox servers
- Sandboxing is handled by a parameter in the payload
- Use the `environment` key in payload

