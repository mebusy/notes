
# swift tips 

## swift4 gcd

```swift
DispatchQueue.global().async {
            print("async do something\(Thread.current)")
            DispatchQueue.main.async {
                print("come back to main thread\(Thread.current)")
            }
        }
```
