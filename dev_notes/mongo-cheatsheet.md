
# MongoDB Cheatsheet

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




```
> db.coll.find({name:{$not: {$eq: "Max"}}})
{ _id: ObjectId("63230545b06cf9f6dfcac221"), name: 'Alex' }
{ _id: ObjectId("63230579b06cf9f6dfcac223"), name: 'Alex' }
...
```




## Databases and Collections
## Indexes
## Handy commands
## Change Streams
## Replica Set
## Sharded Cluster
## Wrap-up




