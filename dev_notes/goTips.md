
# GO Tips

# multiple characters replacement

```go
r := strings.NewReplacer("(", "", ")", "")                                                                                                     
mt.Println( r.Replace( "a(b)c)d" )  )

// abcd
```

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
