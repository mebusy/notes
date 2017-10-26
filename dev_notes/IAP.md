
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


 
