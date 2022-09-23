
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

- filter a specific value
    ```sql
    SELECT ...
    FROM ...
    WHERE <field> = xxxx
    ```
    - couchbase neither enforces nor validates a particular schema
    - so fiters with misspelled fields succeed... with 0 results

- Create a full index
    ```sql
    CREATE INDEX indexName
    ON bucket( field, field(s)) ;
    ```
- Index less than all documents ?
    ```sql
    CREATE INDEX indexName
    ON bucket( field, field(s))
    WHERE field = value
        AND field = value ;
    ```
    - example
        ```sql
        CREATE INDEX idx_state_where_active
        ON couchmusic2 (address.state)
        WHERE status = "active"

        -- Fails to include filter, so index is not used
        SELECT * FROM couchmusic2
        WHERE address.state = "oregon";

        -- includes filter, so index is used
        SELECT * FROM couchmusic2 
        WHERE address.state = "oregon"
            AND status = "active";

        SELECT * FROM couchmusic2 
        WHERE status = "active"
            AND address.state = "oregon";
        ```
- Optimize very large index 
    ```sql
    CREATE INDEX indexName ON bucket( field, field(s)) 
    PARTITION BY HASH(field)
    WHERE type = value
    ```
    - example
        ```sql
        CREATE INDEX idx_partitioned
        ON couchmusic2(postalCode)
        PARTITION BY HASH(countryCode);

        -- only index part including "US" is used
        SELECT favoriteGenres
        FROM couchmusic2
        WHERE postalCode = 97203
            AND countryCode = "US"
        -- full index used
        SELECT favoriteGenres
        FROM couchmusic2
        WHERE postalCode = 97203
        ```


## Lesson 5 - Querying ranges, ordering results, getting system and document metadata


