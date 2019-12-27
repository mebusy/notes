...menustart

 - [swift tips](#3acaa7c4a789484d951ddabfacd81ccd)
     - [swift4 gcd](#1199cc9f00bed626fcf3b39d762743a0)

...menuend


<h2 id="3acaa7c4a789484d951ddabfacd81ccd"></h2>


# swift tips 

<h2 id="1199cc9f00bed626fcf3b39d762743a0"></h2>


## swift4 gcd

```swift
DispatchQueue.global().async {
            print("async do something\(Thread.current)")
            DispatchQueue.main.async {
                print("come back to main thread\(Thread.current)")
            }
        }
```
