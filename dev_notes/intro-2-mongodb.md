
# Introduction to MongoDB

## Week1 Getting Started with MongoDB & Basic Data Analysis

### import data
    ```bash
    # import data to your atlas db
    docker run --rm -it -v `pwd`:/work mongo \
        mongoimport --uri mongodb+srv://analytics:analytics-password@<your cluster>.mongodb.net/mflix --collection movies_initial  \
        --type csv --headerline   --collection movies_initial   --file /work/movies_initial.csv 
    ```
    - you may find more useful cmd line in `Your Cluster`/`Cmd Line Tools`



### Aggregation Framework 

- Aggregation Framework: a set of analytics tools within MongoDB that allows you to run various types of reports or analysis on documents in one or more MongoDB collections

- example
    ```python
    #!python3
    from pymongo import MongoClient
    import pprint

    # python feature: string concat
    client = MongoClient( "mongodb+srv://analytics:analytics-password@"
                          "cluster0.bh3z91v.mongodb.net/"
                          "?retryWrites=true&w=majority"  )
    pipeline = [
        {
            '$group': {
                '_id': { "language": "$language" },
                'count': { '$sum': 1 }
            }
        }
    ]

    pprint.pprint( list( client.mflix.movies_initial.aggregate(pipeline) ) )
    ```

    <details>
    <summary>
    Output: 
    </summary>

    ```bash
    [{'_id': {'language': 'English, Mandarin, Vietnamese, Hokkien, Malay'},
      'count': 1},
     {'_id': {'language': 'English, German, French, Russian'}, 'count': 4},
     {'_id': {'language': 'Hindi, Bhojpuri, English'}, 'count': 1},
     {'_id': {'language': 'Polish'}, 'count': 203},
     ...
    ```

    </details>

- explanation
    1. '$group'
        - Stage, always begins with the dollar sign.
        - A `$group` stage groups its input documents by a specified expression, and applies any accumulator expressions supplied to each group.
    2. "$language" is a field path identifier. It identifies a particular field in input documents.
    3. '$sum' is one such an [accumulator](https://www.mongodb.com/docs/manual/reference/operator/aggregation/). 


### Incremental Improvements with $sort and $sortByCount

- You can sort your output
    ```python
    pipeline = [
        {
            '$group': {
                '_id': { "language": "$language" },
                'count': { '$sum': 1 }
            }
        }, 
        {
            # sort on `count` filed
            '$sort': { 'count': -1 }   # 1 for ascending; -1 for descending
        }
    ]
    ```

    <details>
    <summary>
    Output: 
    </summary>

    ```bash
    [{'_id': {'language': 'English'}, 'count': 25325},
     {'_id': {'language': 'French'}, 'count': 1784},
     {'_id': {'language': 'Italian'}, 'count': 1480},
     {'_id': {'language': 'Japanese'}, 'count': 1290},
    ...
    ```

    </details>



 - this is a very common sequence of operations. So common that the aggregation framework actually inclues a single stage that supports this idiom. It's called `sortByCount`.
    ```python
    pipeline = [
        {
            '$sortByCount': "$language"
        }
    ]
    ```

### Wowza! You can do that? ($facet)

- The problem with this output is that it doesn't provide a very good summary of what values the language fields holds. 
    - Using this movies data might require a deeper understanding of say, how the languages are distributed. 
- I want two different types of summary information. 
    - One has details on specific language combinations, 
    - the other just provides some raw counts. 
- The challenge doing these two types of analysis simultaneously presents to the aggregation framework, is that with the pipeline I can really only process, the documents to **one outcome**. 
    - Again, this type of situation frequently arises, so the aggregation framework actually does support running multiple pipelines in parallel, with the use of the `$facet` stage.
- '$facet': 
    - Processes **multiple** aggregation pipelines **within a single stage** on the **same** set of **input** documents. 
    - Each sub-pipeline has its own field in the output document where its results are stored as an array of documents.
    ```python
    pipeline = [
        {
            '$sortByCount': "$language"
        }, 
        {
            '$facet': {
                'top language combinations': [{'$limit': 100}], # first 100 input documents
                'unusual combinations shared by': [
                    {
                        '$skip': 100  # skip first 100 
                    },
                    {
                        '$bucketAuto': {   # kind of auto group ...
                            'groupBy': "$count" ,  # define bucket
                            'buckets': 5,  # bucket count
                            'output': {
                                'language combinations': {'$sum': 1 }
                            }
                        }
                    }
                ]  # unusual
            } # $facet
        } # 2nd stage
    ]
    ```

    <details>
    <summary>
    Output:
    </summary>

    ```bash
    [{'top language combinations': [{'_id': 'English', 'count': 25325},
                                    {'_id': 'French', 'count': 1784},
                                    {'_id': 'Italian', 'count': 1480},
                                    {'_id': 'Japanese', 'count': 1290},
        ...

      'unusual combinations shared by': [{'_id': {'max': 2, 'min': 1},
                                          'language combinations': 1868},
                                         {'_id': {'max': 6, 'min': 2},
                                          'language combinations': 519},
                                         {'_id': {'max': 16, 'min': 6},
                                          'language combinations': 124}]}]
    ```

    </details>

- explanation
    - I defines 2 fields `top language combinations` and `unusual combinations shared by`, each has its value, an array.
    - each one of there arrays defines a separate pipeline, that will be processed in parallel.
    - and the result of running each pipeline will be stored as the value of there field keys.
    - '$bucketAuto' stage is very similar to the group stage except it automatically defines a list of buckets into which it will group input documents.
        - the buckets are defined by the value you specify for the groupBy key.
        - However, rather than create groups based on the single value, `$bucketAuto` will automatically define ranges of values, and group all documents that fall within that range into the bucket.


### Filtering on Scalar Fields ($match, find(), and Compass)

- $match
    ```python
    pipeline = [
        {
            '$match': { "language": 'Korean, English'}  # match by key `language`
        }
    ]
    ```

    <details>
    <summary>
    Output:
    </summary>

    ```bash
    [{'_id': ObjectId('63284fa0e2b6d723b2021a69'),
      'awards': '1 win.',
      'cast': 'Jock Mahoney, Pat Yi, Youngson Chon, Dong-hwi Jang',
      'country': 'South Korea, USA',
      'director': 'Man-hui Lee',
      'fullplot': 'A division of marines survive a battle with the Chinese army '
                  'but find themselves stranded without contact on the wrong side '
                  'of the front.',
      'genre': 'Drama, War',
      'imdbID': 239594,
      'imdbRating': 6.9,
      'imdbVotes': 60,
      'language': 'Korean, English',    
    ...
    ```

    </details>

- For filtering you will most commonly use the find collection method ( returns a cursor)
    ```python
    filter = { 'language': 'Korean, English' }

    pprint.pprint( list( client.mflix.movies_initial.find(filter) ) )  # find is a method
    ```
    ```python
    # add more condition
    filter = { 'language': 'Korean, English', 'rating': "UNRATED" } # AND
    pprint.pprint( list( client.mflix.movies_initial.find(filter) ) )
    ```


## Week2 Cleaning Data with MongoDB & Query Essentials


### Projecting Query

[Aggregation Stages](https://www.mongodb.com/docs/manual/meta/aggregation-quick-reference/)

- projections: 
    - `$project` allows to specify a projection on all documents that pass through this stage. 
    - we may went to do some processing ont the data,  e.g. an integer 'runtime' field, an array of 'languages', and so on...
    ```python
    pipeline = [
        {
            '$limit': 100
        },
        {
            '$project': {
                'title': 1,  # include this field by 1, or explicitly exclude by 0
                'year': 1,
                'directors': {'$split': ["$director", ", "]},
                'actors': {'$split': ["$cast", ", "]},
                'writers': {'$split': ["$writer", ", "]},
                'genres': {'$split': ["$genre", ", "]},
                'languages': {'$split': ["$language", ", "]}, # reshape into array & rename
                'countries': {'$split': ["$country", ", "]},
                'plot': 1,
                'fullPlot': "$fullplot",  # rename
                'rated': "$rating",
                'released': 1,
                'runtime': 1,  
                'poster': 1,
                'imdb': {  # create an ebedded document 
                    'id': "$imdbID",
                    'rating': "$imdbRating",
                    'votes': "$imdbVotes"
                    },
                'metacritic': 1,
                'awards': 1,
                'type': 1,
                'lastUpdated': "$lastupdated"
            }
        },
        {
            # dump the results to another collection `movies_scratch`
            '$out': "movies_scratch"
        }
    ]

    pprint.pprint( list( client.mflix.movies_initial.aggregate(pipeline) ) )
    ```

    <details>
    <summary>
    Document after projecting
    </summary>

    ```bash
    {
      "_id": {
        "$oid": "63284f8ce2b6d723b201c2d1"
      },
      "title": "Carmencita",
      "year": 1894,
      "runtime": "1 min",
      "released": "1894-01-09",
      "metacritic": "",
      "poster": "https://m.media-amazon.com/images/M/MV5BMjAzNDEwMzk3OV5BMl5BanBnXkFtZTcwOTk4OTM5Ng@@._V1_SX300.jpg",
      "plot": "Performing on what looks like a small wooden stage, wearing a dress with a hoop skirt and white high-heeled pumps, Carmencita does a dance with kicks and twirls, a smile always on her face.",
      "awards": "",
      "type": "movie",
      "directors": [
        "William K.L. Dickson"
      ],
      "actors": [
        "Carmencita"
      ],
      "writers": [
        ""
      ],
      "genres": [
        "Documentary",
        "Short"
      ],
      "languages": [
        ""
      ],
      "countries": [
        "USA"
      ],
      "fullPlot": "Performing on what looks like a small wooden stage, wearing a dress with a hoop skirt and white high-heeled pumps, Carmencita does a dance with kicks and twirls, a smile always on her face.",
      "rated": "NOT RATED",
      "imdb": {
        "id": 1,
        "rating": 5.9,
        "votes": 1032
      },
      "lastUpdated": "2015-08-26 00:03:45.040000000"
    }
    ```

    </details>



#### Convert String To Date

- now we want to convert `release` field from string to Date.
    ```python
    "released": "1994-01-09",
    ```
- do some modifications
    ```python
    'released': {
        '$cond': {  # conditional expression
            'if': {'$ne': ["$released", ""]},
            'then': {
                '$dateFromString': {
                    'dateString': "$released"
                }
            },
            'else': ""}},
    ```
- after converting:
    ```python
    'released': 1994-01-09T00:00:00.000+00:00
    ```
- PS. The MongoDB JSON parser currently does not support loading ISO-8601 strings representing dates **prior** to theUnix epoch. When formatting pre-epoch dates and dates past what your system’stime_ttype can hold, the following format is used:
    ```python
    "released": {
        "$date": {
          "$numberLong": "-2335564800000"
        }
      }
    ```


#### Pre-Processing Data

- `'lastupdated': "2015-08-26 00:03:45.040000000"`
- now we want to change lastupdated filed to a specific timezone: 
    - we're going to use `$dataFromString` to do it. But `$dataFromString` can not parse it because the million seconds part: `.040000000`
    - so we need to do a little bit pre-processing on this data
    ```python
    {
        '$limit': 100
    },
    {
        '$addFields': {
            'lastupdated': {  # if the field exists, it will simply replace it
                '$arrayElemAt': [  # select the element in the array
                    {'$split': ['$lastupdated', "."]},
                    0   # pick the index 0 element
                ]
            }
        }
    },
    ```
    - now we can use `$dataFromString` to convert the data
    ```python
            'lastUpdated': {
                '$cond': {  # conditional expression
                    'if': {'$ne': ["$lastupdated", ""]},
                    'then': {
                        '$dateFromString': {
                            'dateString': "$lastupdated",
                            'timezone': "America/New_York"
                        }
                    },
                    'else': ""}},
    ```

- after converting:
    ```python
    'lastUpdated': 2015-08-26T04:03:45.000+00:00
    ```


### Update Documents

[Update Operators](https://www.mongodb.com/docs/manual/reference/operator/update/)


- let's start with `update_one`
    ```python
    # limit is a cursor method
    # use find() to return a cursor
    for movie in client.mflix.movies.find({}).limit(100):
        ...
        # update one 
        db.movies.update_one( {'_id': movie[ '_id' ] } , update_doc )
    ```
    - the frist argument `{'_id': movie[ '_id' ] }` is a filter that selects the document we wish to update.
        - here this filter says, I'm interested in updating the document with the `_id` value equals `movie['_id']`
    - the 2nd argument `update_doc` is the change that I make
        - some examples
        ```python
        {"year": 2016}  # WARNING! Replaces the entire document
        {$set: {"year": 2016, name: "Max"}}  # insert / update  `year` and `name` fields
        {$unset: {"year": 1}}  # remore `year` field
        ```


### Bulk Updates

```python
...
from pymongo import MongoClient, UpdateOne

updates = []

updates.append( UpdateOne( {'_id': movie[ '_id' ] } , update_doc ) )

...
client.mflix.movies.bulk_write( updates )
```








