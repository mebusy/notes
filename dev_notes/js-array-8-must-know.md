[](...menustart)

- [8 Must Know JavaScript Array Methods](#ab7987044420e54c91c08f19820fc741)
    - [1. filter](#b7e9c356372c6190077c0d2644a7886a)
    - [2. map](#1ab5fbd0c4ddc51f5d32c40e05099ebc)
    - [3. find](#a2e947d461b484e60f8d68660ee60687)
    - [4. forEach](#56a6768645be8464bbadc6fb8a682a93)
    - [5. some](#f6a64c8511d26eae9ca74403f1b2caae)
    - [6. every](#99838ef5da412ee9bc8180dd401e7f8c)
    - [7. reduce](#f9242b615d9ac48e610d25c12a1b9cf7)
    - [8. include](#571fd09a922e46e5159bf2049e93890b)

[](...menuend)


<h2 id="ab7987044420e54c91c08f19820fc741"></h2>

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

<h2 id="b7e9c356372c6190077c0d2644a7886a"></h2>

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

<h2 id="1ab5fbd0c4ddc51f5d32c40e05099ebc"></h2>

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

<h2 id="a2e947d461b484e60f8d68660ee60687"></h2>

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


<h2 id="56a6768645be8464bbadc6fb8a682a93"></h2>

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


<h2 id="f6a64c8511d26eae9ca74403f1b2caae"></h2>

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

<h2 id="99838ef5da412ee9bc8180dd401e7f8c"></h2>

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

<h2 id="f9242b615d9ac48e610d25c12a1b9cf7"></h2>

## 7. reduce



```javascript
const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal
}, 0)
```

```bash
1840
```


<h2 id="571fd09a922e46e5159bf2049e93890b"></h2>

## 8. include

```javascript
const numbers = [1,2,3,4,5]
const includesTwo = numbers.includes(2)
console.log(includesTwo)
```

```bash
true
```



