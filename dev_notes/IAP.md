
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

### Unlock Content

 - If you are downloading content for in-app purchases, there's a couple of ways you can do this.
 - Apple actually offers two techniques for you to use, as well.
    - on-demand resources
    - hosted in-app purchase downloadable content
        - you can associate downloadable content through iTunes Connect that's accessed through the SKProduct object, directly. 

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


# Advanced StoreKit

## Receipt validation




## Maintaining subscription state

## Developing with the Sandbox





