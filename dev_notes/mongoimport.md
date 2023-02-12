[](...menustart)

- [Import Data into MongoDB with mongoimport](#5a09cfae926cb81d3334da915f1640c9)
    - [Connect](#49ab28040dfa07f53544970c6d147e1e)
    - [Import One JSON Document](#f5a48ed9a17549f933886dd99c5b4db0)
    - [Import One Big JSON Array](#4af68c1e3a65f0b45f6ee4f50556707f)
    - [Update Existing Records](#f4242f2593ccd9f62d965058358f4339)
    - [Merge Data into Existing Records](#d3b1dce1ff7e27026b92455d7b3d34d4)
    - [Other Options](#fb155326387b981974c6fe737e86d00f)

[](...menuend)


<h2 id="5a09cfae926cb81d3334da915f1640c9"></h2>

# Import Data into MongoDB with mongoimport

https://www.mongodb.com/developer/products/mongodb/mongoimport-guide/


```bash
docker run --rm -it mongo:5  mongoimport
```


<h2 id="49ab28040dfa07f53544970c6d147e1e"></h2>

## Connect

- uri protocal
    ```bash
    mongodb://[user:password@]host:port/[dbname]?authSource=admin
    ```
- e.g.
    ```bash
    mongoimport --uri 'mongodb://root:root@10.192.0.4:27017/db_test?authSource=admin'
    ```


<h2 id="f5a48ed9a17549f933886dd99c5b4db0"></h2>

## Import One JSON Document

the json data should be dict/object like.

```bash
mongoimport --collection='mycollectionname' --file=path_json_file
```

<h2 id="4af68c1e3a65f0b45f6ee4f50556707f"></h2>

## Import One Big JSON Array

```bash
mongoimport --collection='mycollectionname' --file=path_json_array_file --jsonArray
```


<h2 id="f4242f2593ccd9f62d965058358f4339"></h2>

## Update Existing Records

- if your data has `_id` field, then just simply supply the option `--mode=upsert`
- If you're upserting records that don't have `_id`, you can specify some fields to use to match against documents in the collection, with the `--upsertFields` option
    ```bash
    --upsertFields=name,address,height
    ```


<h2 id="d3b1dce1ff7e27026b92455d7b3d34d4"></h2>

## Merge Data into Existing Records

- If you are supplied with data files which extend your existing documents by adding new fields, or update certain fields, you can use mongoimport with "merge mode". 
    ```bash
    --mode=merge
    ```
- You can also use the `--upsertFields` option here as well as when you're doing upserts, to match the documents you want to update.


<h2 id="fb155326387b981974c6fe737e86d00f"></h2>

## Other Options

Option | Description
--- | ---
`--ignoreBlanks` | Ignore fields or columns with empty values.
`--drop`    | Drop the collection before importing the new documents. This is particularly useful during development, but will lose data if you use it accidentally.
`--stopOnError` | Another option that is useful during development, this causes mongoimport to stop immediately when an error occurs.

