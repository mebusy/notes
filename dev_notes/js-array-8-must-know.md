
# 8 Must Know JavaScript Array Methods

```javascript
const items = [
    { name: 'Bike', price: 100 },
    { name: 'TV', price: 200 },
    { name: 'Album', price: 10 },
    { name: 'Book', price: 5 },
    { name: 'Phone', price: 500 },
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25 }
]
```

## 1. filter

```javascript
const filteredItems = items.filter((item) => {
    return item.price <= 100
})

console.log(filteredItems)
```

```bash
[
  { name: 'Bike', price: 100 },
  { name: 'Album', price: 10 },
  { name: 'Book', price: 5 },
  { name: 'Keyboard', price: 25 }
]
```

## 2. map

```javascript

```


```bash
[
  'Bike',     'TV',
  'Album',    'Book',
  'Phone',    'Computer',
  'Keyboard'
]
```

## 3. find

find a single object in an array

```javascript
const foundItem = items.find((item) => {
    return item.name === 'Book'
})
```

```bash
{ name: 'Book', price: 5 }
```


## 4. forEach

```javascript
items.forEach((item) => {
    console.log(item.price)
})
```

```bash
100
200
10
5
500
1000
25
```


## 5. some

return true if any items in array satisfy some condition.

```javascript
const hasInexpensiveItems = items.some((item) => {
    return item.price <= 100
})
```

```bash
true
```

## 6. every

return true if all items in array satisfy some condition

```javascript
const allInexpensiveItems = items.every((item) => {
    return item.price <= 100
})
```

```bash
false
```

## 7. reduce



```javascript
const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal
}, 0)
```

```bash
1840
```


## 8. include

```javascript
const numbers = [1,2,3,4,5]
const includesTwo = numbers.includes(2)
console.log(includesTwo)
```

```bash
true
```



