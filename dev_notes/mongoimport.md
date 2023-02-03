
# Import Data into MongoDB with mongoimport

https://www.mongodb.com/developer/products/mongodb/mongoimport-guide/


```bash
docker run --rm -it mongo:5  mongoimport
```


## Connect

- uri protocal
    ```bash
    mongodb://[user:password@]host:port/[dbname]?authSource=admin
    ```
- e.g.
    ```bash
    mongoimport --uri 'mongodb://root:root@10.192.0.4:27017/db_test?authSource=admin'
    ```


## Import One JSON Document

the json data should be dict/object like.

```bash
mongoimport --collection='mycollectionname' --file=path_json_file
```

## Import One Big JSON Array

```bash
mongoimport --collection='mycollectionname' --file=path_json_array_file --jsonArray
```


## Update Existing Records

- if your data has `_id` field, then just simply supply the option `--mode=upsert`
- If you're upserting records that don't have `_id`, you can specify some fields to use to match against documents in the collection, with the `--upsertFields` option
    ```bash
    --upsertFields=name,address,height
    ```


## Merge Data into Existing Records

- If you are supplied with data files which extend your existing documents by adding new fields, or update certain fields, you can use mongoimport with "merge mode". 
    ```bash
    --mode=merge
    ```
- You can also use the `--upsertFields` option here as well as when you're doing upserts, to match the documents you want to update.


## Other Options

Option | Description
--- | ---
`--ignoreBlanks` | Ignore fields or columns with empty values.
`--drop`    | Drop the collection before importing the new documents. This is particularly useful during development, but will lose data if you use it accidentally.
`--stopOnError` | Another option that is useful during development, this causes mongoimport to stop immediately when an error occurs.

