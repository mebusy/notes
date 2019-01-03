...menustart

 - [GO Tips](#8b1b84c36166bd2b2098cdf1fe2f18e4)
 - [multiple characters replacement](#092987d14c5ea50ca1043604d333f7f7)
 - [三元表达式](#6ada22780ed552c34465864a2648f7e9)

...menuend


<h2 id="8b1b84c36166bd2b2098cdf1fe2f18e4"></h2>

# GO Tips

<h2 id="092987d14c5ea50ca1043604d333f7f7"></h2>

# multiple characters replacement

```go
r := strings.NewReplacer("(", "", ")", "")                                                                                                     
mt.Println( r.Replace( "a(b)c)d" )  )

// abcd
```

<h2 id="6ada22780ed552c34465864a2648f7e9"></h2>

# 三元表达式

```go
func If(condition bool, trueVal, falseVal interface{}) interface{} {  
    if condition {
        return trueVal
    }
    return falseVal
}

...
If(i==0,"A","B").(string)
```

# How to find out which types implement `ByteReader` interface  in golang pkg ?

```
https://golang.org/search?q=ReadByte
```


