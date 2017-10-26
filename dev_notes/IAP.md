
# IAP

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

### Load In-App identifiers 

 - when it comes to loading these identifiers  in your applications, you can do it a couple of ways.
    - Firstly, you can just bake them directly into your application
    - Or the other way, of course, is to maybe fetch them from your own server.
 - anyways you will have this set of strings

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



