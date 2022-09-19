
# MongoDB Cheatsheet

[db.collection.find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/?_ga=2.77243475.790102026.1663232700-1298892323.1663232700)

[Query and Projection Operators](https://www.mongodb.com/docs/manual/reference/operator/query/?_ga=2.77243475.790102026.1663232700-1298892323.1663232700)

[BSON types](https://www.mongodb.com/docs/manual/reference/operator/query/type/?&_ga=2.77243475.790102026.1663232700-1298892323.1663232700#available-types)

[Read Concern](https://www.mongodb.com/docs/manual/reference/read-concern/?_ga=2.6016245.790102026.1663232700-1298892323.1663232700)

## Helpers 

### Show Databases

```
> show dbs
admin   100.00 KiB
config  108.00 KiB
local    72.00 KiB
```

### Switch Database

```mongo
// even not exists
use <database_name>
```

```
> use db-name
'switched to db db-name'
db-name>
```

### Show Collections

```
> show collections
system.users
system.version
```

### Run JavaScript File

```
// mongo, not implemented in mongosh
load("myScript.js")
```


## CRUD

### Create

```
db.coll.insertOne({name: "Max"})  // coll not necessarily need to be existed
// _id 6323029eb06cf9f6dfcac219
// name "Max"
show collections
coll
```

```
db.coll.insertMany([{name: "Max"}, {name:"Alex"}]) // ordered bulk insert
// _id 63230545b06cf9f6dfcac220
// name "Max"
// _id 63230545b06cf9f6dfcac221
// name "Alex"
```

```
db.coll.insertMany([{name: "Max"}, {name:"Alex"}], {ordered: false}) // unordered bulk insert
db.coll.insert({date: ISODate()})
db.coll.insert({name: "only this obj will be inserted"}, 
               {"wontBeInserted": {"w": "majority", "wtimeout": 5000}})
```


### Read


```
db.coll.findOne() // returns a single document
db.coll.find()    // returns a cursor - show 20 results - "it" to display more
db.coll.find({name: "Max", age: 32}) // implicit logical "AND".
db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})  // find date
```

```
// or "queryPlanner" or "allPlansExecution"
db.coll.find({name: "Max", age: 32}).explain("executionStats") 
```

```
> db.coll.distinct("name")
[ 'Alex', 'Max', 'dddd', 'only this obj will be inserted' ]
```

count

```
// estimation based on collection metadata
db.coll.count({age: 32}) 
db.coll.estimatedDocumentCount() 
db.coll.countDocuments({age: 32}) // alias for an aggregation pipeline - accurate count
```

Comparison

```
db.coll.find({"year": {$gt: 1970}})
db.coll.find({"year": {$ne: 1970}})
db.coll.find({"year": {$nin: [1958, 1959]}})
```


Logical

```
> db.coll.find({name:{$not: {$eq: "Max"}}})
{ _id: ObjectId("63230545b06cf9f6dfcac221"), name: 'Alex' }
{ _id: ObjectId("63230579b06cf9f6dfcac223"), name: 'Alex' }
...
```

```
db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
db.coll.find({
  $and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
    {$or: [{sale: true}, {price: {$lt: 5 }}]}
  ]
})
```

Element

```
db.coll.find({name: {$exists: true}})
db.coll.find({"zipCode": {$type: 2 }})
db.coll.find({"zipCode": {$type: "string"}})
```

Aggregation Pipeline

```
db.coll.aggregate([
  {$match: {status: "A"}},
  {$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
  {$sort: {total: -1}}
])
```


Text search with a "text" index

- MongoDB provides text indexes to support text search queries on string content.
- A collection can only have one text search index, but that index can cover multiple fields.
- text search queries will compute a relevance score for each document
    - To sort the results in order of relevance score, you must explicitly project the $meta textScore field and sort on it:

```
db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}})
       .sort({score: {$meta: "textScore"}})
```

Regex  `Perl compatible`

```
db.coll.find({name: /^Max/})   // regex: starts by letter "M"
db.coll.find({name: /^Max$/i}) // regex case insensitive
```








## Databases and Collections
## Indexes
## Handy commands
## Change Streams
## Replica Set
## Sharded Cluster
## Wrap-up




