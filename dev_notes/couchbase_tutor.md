
# Couchbase Tutorial

```bash
docker run -d --restart unless-stopped -p 8091:8091 --name couchbase-test couchbase
```

web UI: `localhost:8091/ui`


## Lesson 2 - Selecting documents and limiting results

- N1QL supports SELECT, FROM(WHERE, HAVING, etc) syntax
- Select fields in documents from a bucket
    - Not columns from tables

- Compare SQL

    SQL database | CouchBase
    --- | ---
    Database | Bucket
    table |  assign an explicit `type` field to docoment


- Select JSON document field 
    ```sql
    SELECT * | field, field, object.fiedl, ...
    FROM bucket
    LIMIT number ;
    ```

- cbp -- command line tool for N1QL query execution
    - cbp [options]
    - -e  database engine (default localhost:8091)
    - -u / -p  user/password
    - How do you lanch and use cbq ?
        ```bash
        cbq -e localhost:8091 -u admin -p adminpwd
        ```
    ```bash
    cbq> SELECT *
       > FROM couchmusic2
       > LIMIT 1
    ```


## Lesson 3 - Aliasing, concatenating, and selecting by keys

- Document ID ("keys") is metadata, created on insert
    - retained in memory to speed access if bucket set to value only ejection
- you can get documents directly by key in N1QL, not just query for them.
    ```sql
    SELECT * | field, field(s) ...
    FROM bucket
    USE KEYS key | [key, key, ...];
    ```
    - example
        ```sql
        SELECT * 
        FROM couchmusic2
        USE KEYS "country::ES";
        ```
        ```sql
        SELECT * 
        FROM couchmusic2
        USE KEYS [ "country::ES", "country::FR" ];
        ```

- alias: works just like SQL
    ```sql
    SELECT field.field AS alias
    FROM bucket;
    ```
    - example
        ```sql
        SELECT lastName, address.postalCode AS zipcode
        FROM couchmusic2
        USE KEYS "userprofile::aahingeffeteness42037"
        ```
    - results
        ```python
        [{
            "lastName": "Riley",
            "zipcode": 63450
        }]
        ```
- Concatenate values
    ```sql
    SELECT field.field ... || ["literal"] || field
    FROM bucket;
    ```
    - example
        ```sql
        SELECT firstName || " " || lastName as fullName
        FROM couchmusic2
        USE kEYS "userprofile::aahingeffeteness42037"
        ```
    - results
        ```python
        [{
            "fullName": "Delores Riley"
        }]
        ```


## Lesson 4 - Creating indexes and filtering queries


