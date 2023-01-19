[](...menustart)

- [Swagger](#336ff1e9aa6177ea7a71984fa8c241b9)
    - [run swagger editor](#7a8a1e62c3e177c335813e2cda4f44f0)
    - [swagger UI](#d965025d55377342fd1e4ff3e57ad750)
    - [inheritance](#5fed3411faf832174ef1f040028b2c21)
    - [Code Gen](#fe08e791970673313c63001a59ae8f88)
- [OpenAPI 3.0](#a2374b8c1492381dc2135504e8e6800b)
    - [Basic Structure](#fe1861d778ca03acdf4244a3bc9ccdce)
        - [Parameters](#3225a10b07f1580f10dee4abc3779e6c)
        - [Request Body](#ef1845aa2c5377425ac03316124d29ba)
        - [Responses](#b9ee5f76a4d9b6b73e94eb7a131aa91e)
        - [Input and Output Models](#5d7926045275ac45a1d8b88502c7cb2c)
        - [Authentication](#c75f7811d70d17dbcd88e9d03752cbed)
    - [API Server and Base URL](#476211f22abad8f3c96fa55e1420ef86)
        - [Server Templating](#eb1d270333e89c399407d5b9eaeaa8cf)
    - [operationId](#19d240916bb31fd4ebc1206122b0674e)
    - [Describing Parameters](#88b585c002272739ab16a87f55c498be)
        - [Parameter Types](#65b5e8dd96a80097dac383f62d6ce3ab)
        - [schema vs content](#8fadb7c789daca1c989a42570ba8d28f)
        - [Default Parameter Values](#416bdc86ee051d6e63d132f620c4738a)
        - [Empty-Valued and Nullable Parameters](#4c189dbc8627681cdbb965c0b395704e)
    - [Describing Request Body](#b21886458425b4470312da390fff6716)
        - [anyOf, oneOf](#a373aa0f8db6e70b1468984d1b3ecde5)
        - [Reusable Bodies](#2ed6ddc94445341edd97fe099a4fda54)
    - [Describing Responses](#ac408aa995b055ac422646306e29973b)
        - [Response Media Types](#6d37acf452144b401a97ad9bdc7f20b0)
        - [anyOf, oneOf](#a373aa0f8db6e70b1468984d1b3ecde5)
        - [Empty Response Body](#c8dbed315f8603e42eed0e0d8dd7b149)
        - [Response Headers](#90198f1c07c67e3a44ccc6853651ca2c)
        - [Reusing Responses](#20296598c63ade4f7b8ba4753d88c8d2)
    - [Data Models (Schemas)](#704eae6481c8d4f82c54b644ebca03b7)
        - [Data Types](#637881603c973c4967d77ec4ba147e0c)
        - [Enums](#1b22e7dc709b52f1767fe1eb5dc56625)
        - [Dictionaries(aka. HashMaps, or Associative Arrays )](#c8bfb014028c3a06cf9b3852c44fb935)
        - [oneOf, anyOf, allOf, not](#64f5f3bbd10e6ab7c82ed0cbfa6e519a)
        - [Inheritance and Polymorphism Model Composition](#6f90d7bbdfd5a9ffeda0d201a4164e88)
            - [Model Composition](#3382c814ef389ff660adac74524d6555)
            - [Polymorphism](#371fedf6ee6747b1de368aafb08094e8)
            - [Discriminator](#3d07d09db1423c8da8e60b5f36d2d903)
    - [Grouping Operations With Tags](#fb70c8533ca8c289d5b1979656ea9efe)
    - [Authentication and Authorization](#8654aba8cb48ea7d16c3a3e62163d6ef)
        - [Changes from OpenAPI 2.0](#9679874577b1f897fee85f92a3f05749)
        - [Describing Security](#274df024afe245d7c8eec5c9d549dd9c)
        - [Example: global apiKey auth](#dff9a265a966b13fec331324fac51b4e)

[](...menuend)


<h2 id="336ff1e9aa6177ea7a71984fa8c241b9"></h2>

# Swagger 


https://swagger.io/docs/specification/about/


<h2 id="7a8a1e62c3e177c335813e2cda4f44f0"></h2>

## run swagger editor


```bash
docker pull swaggerapi/swagger-ui
docker run --rm -p 8088:8080 swaggerapi/swagger-ui

# ruuning in background
docker run --name swagger-ui --restart=unless-stopped -d -p 8088:8080 swaggerapi/swagger-ui
```

<h2 id="d965025d55377342fd1e4ff3e57ad750"></h2>

## swagger UI 

you can integrate swagger UI in you web server

 1. download from [github repository](https://github.com/swagger-api/swagger-ui) 
 2. put dist folder inside your webserver 
 3. through your webserver , lanuch dist/index.html

you can change the  default URL of swagger config file in  webTools/swaggerUI/index.html



<h2 id="5fed3411faf832174ef1f040028b2c21"></h2>

## inheritance

```yaml
definitions:
  Pet:
    discriminator: petType
    required:
      - name
      - petType # required for inheritance to work
    properties:
      name: 
        type: string
      petType:
        type: string
  Cat:
    allOf:
      - $ref: '#/definitions/Pet' # Cat has all properties of a Pet
      - properties: # extra properties only for cats
          huntingSkill:
            type: string
            default: lazy
            enum:
              - lazy
              - aggressive
  Dog:
    allOf:
      - $ref: '#/definitions/Pet' # Dog has all properties of a Pet
      - properties: # extra properties only for dogs
          packSize:
            description: The size of the pack the dog is from
            type: integer
```


```yaml
Cat:
  allOf:
  - $ref: "#/definitions/Animal"
  - type: "object"
    properties:
      declawed:
        type: "boolean"
Animal:
  type: "object"
  discriminator: "Animal" # ?
  properties:
    className:
      type: "string"
    color:
      type: "string"
      default: "red"
```


<h2 id="fe08e791970673313c63001a59ae8f88"></h2>

## Code Gen

Note: `-v3` for openapi 3.0



- server
    ```bash
    docker run --rm -v `pwd`:/local swaggerapi/swagger-codegen-cli-v3 generate \
        -i /local/swagger.yaml \
        -l go-server \
        -o /local/server/go
    ```
- client
    ```bash
    docker run --rm -v `pwd`:/local swaggerapi/swagger-codegen-cli-v3 generate \
        -i /local/swagger.yaml \
        -l go \
        -o /local/client/go
    ```


<h2 id="a2374b8c1492381dc2135504e8e6800b"></h2>

# OpenAPI 3.0

<h2 id="fe1861d778ca03acdf4244a3bc9ccdce"></h2>

## Basic Structure

```yaml
openapi: 3.0.0
info:
  title: my-server       # Note. title is your API name
  description: Optional multiline or single-line description
               in [CommonMark](http://commonmark.org/help/) or HTML.
  version: 0.1.9  # Note. an arbitrary string that specifies the version of your own API

servers:  # Note. API server and base URL
  - url: http://api.example.com/v1  
    description: Optional server description,
                  e.g. Main (production) server
    # Note. If the server URL is relative, (e.g. `/v1/reports`, `/` , it is resolved 
    #       against the server where the given OpenAPI definition file is hosted 
  - url: http://staging-api.example.com
    description: Optional server description,
                  e.g. Internal staging server for testing

paths: # Note. defines individual endpoints (paths)
  /users:
    ...
```


<h2 id="3225a10b07f1580f10dee4abc3779e6c"></h2>

### Parameters

Operations can have parameters passed via URL path (`/users/{userId}`), query string (`/users?role=admin`), headers (`X-CustomHeader: Value`) or cookies (`Cookie: debug=0`). 

You can define the parameter data types, format, whether they are required or optional, and other details:

```yaml
paths:
  /users/{userId}:  # Note. Parameter in path
    get:
      summary: Returns a user by ID.
      parameters:
        - name: userId
          in: path
          required: true
          description: Parameter description in CommonMark or HTML.
          schema:
            type : integer
            format: int64
            minimum: 1
      responses: 
        '200':
          description: OK
```


<h2 id="ef1845aa2c5377425ac03316124d29ba"></h2>

### Request Body

If an operation sends a request body, use the `requestBody` keyword to describe the body content and media type.

```yaml
paths:
  /users:
    post:
      summary: Creates a user.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
      responses: 
        '201':
          description: Created
```

<h2 id="b9ee5f76a4d9b6b73e94eb7a131aa91e"></h2>

### Responses

For each operation, you can define possible status codes, such as 200 OK or 404 Not Found, 

and the response body schema. Schemas can be defined inline or referenced via `$ref`. 

You can also provide example responses for different content types:

```yaml
  /users/{userId}:
    get:
      summary: Returns a user by ID.
      parameters:
        - name: userId
          in: path
          required: true
          description: The ID of the user to return.
          schema:
            type: integer
            format: int64
            minimum: 1
      responses:
        '200':
          description: A user object.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    example: 4
                  name:
                    type: string
                    example: Jessica Smith
        '400':
          description: The specified user ID is invalid (not a number).
        '404':
          description: A user with the specified ID was not found.
        default:
          description: Unexpected error
```

```bash
# response data
{
  "id": 4,
  "name": "Jessica Smith"
}
```


<h2 id="5d7926045275ac45a1d8b88502c7cb2c"></h2>

### Input and Output Models

The global `components/schemas` section lets you define common data structures used in your API. 

They can be referenced via `$ref` whenever a schema is required, – in parameters, request bodies, and response bodies. 

For example, this JSON object:

```bash
{
  "id": 4,
  "name": "Arthur Dent"
}
```

can be represented as:

```yaml
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          example: 4
        name:
          type: string
          example: Arthur Dent
      # Both properties are required
      required:  
        - id
        - name
```

and then referenced in the request body schema and response body schema as follows:

```yaml
  /users:
    post:
      summary: Creates a new user.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'      # <-------
      responses:
        '201':
          description: Created
```


<h2 id="c75f7811d70d17dbcd88e9d03752cbed"></h2>

### Authentication

The `securitySchemes` and `security` keywords are used to describe the authentication methods used in your API.

```yaml
components:
  securitySchemes:
    BasicAuth:
      type: http
      scheme: basic
security:
  - BasicAuth: []
```

Supported authentication methods are:

- HTTP authentication: [Basic](https://swagger.io/docs/specification/authentication/basic-authentication/), [Bearer](https://swagger.io/docs/specification/authentication/bearer-authentication/), and so on.
- [API key](https://swagger.io/docs/specification/authentication/api-keys/) as a header or query parameter or in cookies
- [OAuth 2](https://swagger.io/docs/specification/authentication/oauth2/)
- [OpenID Connect Discovery](https://swagger.io/docs/specification/authentication/openid-connect-discovery/)


<h2 id="476211f22abad8f3c96fa55e1420ef86"></h2>

## API Server and Base URL

valid server URLs:

```url
https://api.example.com
https://api.example.com:8443/v1/reports
http://localhost:3025/v1
http://10.0.81.36/v1
ws://api.example.com/v1
wss://api.example.com/v1
/v1/reports
/
//api.example.com
```

If the server URL is relative, it is resolved against the server where the given OpenAPI definition file is hosted (more on that below).

<h2 id="eb1d270333e89c399407d5b9eaeaa8cf"></h2>

### Server Templating

Any part of the server URL – scheme, host name or its parts, port, subpath – can be parameterized using variables. Variables are indicated by {curly braces} in the server url, like so:


```yaml
servers:
  - url: https://{customerId}.saas-app.com:{port}/v2
    variables:
      customerId:
        default: demo
        description: Customer ID assigned by the service provider
      port:
        enum:
          - '443'
          - '8443'
        default: '443'
```

Common use cases for server templating:

- Specifying multiple protocols (such as HTTP vs HTTPS).
- SaaS (hosted) applications where each customer has their own subdomain.
- Regional servers in different geographical regions (example: Amazon Web Services).
- Single API definition for SaaS and on-premise APIs.

Examples: HTTPS and HTTP

```yaml
servers:
  - url: '{protocol}://api.example.com'
    variables:
      protocol:
        enum:
          - http
          - https
        default: https
```

<h2 id="19d240916bb31fd4ebc1206122b0674e"></h2>

## operationId

`operationId` is an optional unique string used to identify an operation. If provided, these IDs must be unique among all operations described in your API.

Some common use cases for operationId are:

- Some code generators use this value to name the corresponding methods in code.
- Links can refer to the linked operations by operationId.


<h2 id="88b585c002272739ab16a87f55c498be"></h2>

## Describing Parameters

- parameters are defined in the `parameters` section of an operation or path
- To describe a parameter, you specify
    - its `name`,
    - location (`in`),
    - data type (defined by either `schema` or `content`)
    - and other attributes, such as `description` or `required`. 
- `parameters` is an array, so, in YAML, each parameter definition must be listed with a dash (`-`) in front of it.


<h2 id="65b5e8dd96a80097dac383f62d6ce3ab"></h2>

### Parameter Types

- parameter types based on the parameter location , location is determined by the parameter’s `in` key
    - `path` parameters, such as `/users/{id}`
        - remember to add `required: true`, **because path parameters are always required**. 
    - `query` parameters, such as `/users?role=admin`
    - `header` parameters, such as `X-MyHeader: Value`
    - `cookie` parameters, which are passed in the Cookie header, such as `Cookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCU`

<h2 id="8fadb7c789daca1c989a42570ba8d28f"></h2>

### schema vs content

In most cases, you would use `schema`.

`content` is used in complex serialization scenarios.

```yaml
parameters:
  - in: query
    name: filter
    # Wrap 'schema' into 'content.<media-type>'
    content:
      application/json:  # <---- media type indicates how to serialize / deserialize the parameter content
        schema:
          type: object
          properties:
            type:
              type: string
            color:
              type: string
```

<h2 id="416bdc86ee051d6e63d132f620c4738a"></h2>

### Default Parameter Values

Use the `default` keyword in the parameter schema to specify the default value for an **optional!!** parameter. 

```yaml
  name: offset
  schema:
    type: integer
    minimum: 0
    default: 0
```

- There are two common mistakes when using the `default` keyword:
    1. Using `default` with `required` parameters or properties, for example, with path parameters. 
        - This does not make sense – if a value is required, the client must always send it, and the default value is never used.
    2. Using `default` to specify a sample value. This is not intended use of default and can lead to unexpected behavior in some Swagger tools. 
        - Use the `example` or `examples` keyword for this purpose instead. 

<h2 id="4c189dbc8627681cdbb965c0b395704e"></h2>

### Empty-Valued and Nullable Parameters

Query string parameters may only have a name and no value, like so:

```http
GET /foo?metadata
```

Use `allowEmptyValue` to describe such parameters:

```yaml
      parameters:
        - in: query
          name: metadata
          schema:
            type: boolean
          allowEmptyValue: true  # <-----
```


OpenAPI 3.0 also supports nullable in schemas, allowing operation parameters to have the null value.

```yaml
      schema:
        type: integer
        format: int32
        nullable: true
```

<h2 id="b21886458425b4470312da390fff6716"></h2>

## Describing Request Body

- `requestBody` keyword
    - Schemas can vary by media type.
    - `requestBody.content` maps the media types to their schemas.
    - `anyOf` and `oneOf` can be used to specify alternate schemas.

```yaml
paths:
  /pets:
    post:
      summary: Add a new pet
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Pet'
          application/xml:
            schema:
              $ref: '#/components/schemas/Pet'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PetForm'
          text/plain:
            schema:
              type: string
      responses:
        '201':
          description: Created
```

<h2 id="a373aa0f8db6e70b1468984d1b3ecde5"></h2>

### anyOf, oneOf

- OpenAPI 3.0 supports `anyOf` and `oneOf`.

```yaml
      requestBody:
        description: A JSON object containing pet information
        content:
          application/json:
            schema:
              oneOf:
                - $ref: '#/components/schemas/Cat'
                - $ref: '#/components/schemas/Dog'
                - $ref: '#/components/schemas/Hamster'
```


<h2 id="2ed6ddc94445341edd97fe099a4fda54"></h2>

### Reusable Bodies

- You can put the request body definitions in the global `components.requestBodies` section and `$ref` them elsewhere. - This is handy if multiple operations have the same request body – this way you can reuse the same definition easily.

```yaml
paths:
  /pets:
    post:
      summary: Add a new pet
      requestBody:
        $ref: '#/components/requestBodies/PetBody'
  /pets/{petId}
    put:
      summary: Update a pet
      parameters: [ ... ]
      requestBody:
        $ref: '#/components/requestBodies/PetBody'
components:
  requestBodies:
    PetBody:
        ...
```


<h2 id="ac408aa995b055ac422646306e29973b"></h2>

## Describing Responses

- `responses`
- Each operation must have at least one response defined, usually a successful response.
- A response is defined by its HTTP status code and the data returned in the response body and/or headers. 
- a minimal example:
    ```yaml
    paths:
      /ping:
        get:
          responses:
            '200':
              description: OK
              content:
                text/plain:
                  schema:
                    type: string
                    example: pong
    ```

<h2 id="6d37acf452144b401a97ad9bdc7f20b0"></h2>

### Response Media Types

- To specify the response media types, use the `content` keyword at the operation level.
- `schema` keyword is used to describe the response body. A `schema` can define:
    - an `object` or an `array` — typically used with JSON and XML APIs,
    - a primitive data type such as a number or string – used for plain text responses,
    - a file 
- or defined in the global `components.schemas` section and referenced via `$ref`. 

```yaml
paths:
  /users:
    get:
      summary: Get all users
      responses:
        '200':
          description: A list of users
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ArrayOfUsers'
            application/xml:
              schema:
                $ref: '#/components/schemas/ArrayOfUsers'
            text/plain:
              schema:
                type: string
  # This operation returns image
  /logo:
    get:
      summary: Get the logo image
      responses:
        '200':
          description: Logo image in PNG format
          content:
            image/png:
              schema:
                type: string
                format: binary
```


<h2 id="a373aa0f8db6e70b1468984d1b3ecde5"></h2>

### anyOf, oneOf

OpenAPI 3.0 also supports oneOf and anyOf, so you can specify alternate schemas for the response body.


<h2 id="c8dbed315f8603e42eed0e0d8dd7b149"></h2>

### Empty Response Body

Some responses, such as 204 No Content, have no body. To indicate the response body is empty, do not specify a content for the response:

<h2 id="90198f1c07c67e3a44ccc6853651ca2c"></h2>

### Response Headers

Responses from an API can include custom headers to provide additional information on the result of an API call.

For example, a rate-limited API may provide the rate limit status via response headers as follows:

```http
HTTP 1/1 200 OK
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 2016-10-12T11:00:00Z
{ ... }
```

You can define custom `headers` for each response as follows:

```yaml
paths:
  /ping:
    get:
      summary: Checks if the server is alive.
      responses:
        '200':
          description: OK
          headers:
            X-RateLimit-Limit:
              schema:
                type: integer
              description: Request limit per hour.
            ...
```


<h2 id="20296598c63ade4f7b8ba4753d88c8d2"></h2>

### Reusing Responses

```yaml
# Descriptions of common components
components:
  responses:
    NotFound:
      description: The specified resource was not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error' # Note. $ref again to schemas
```


<h2 id="704eae6481c8d4f82c54b644ebca03b7"></h2>

## Data Models (Schemas)

<h2 id="637881603c973c4967d77ec4ba147e0c"></h2>

### Data Types

- `type` keyword
    - `string` (this includes dates and files)
        - String length can be restricted using `minLength` and `maxLength`
        - An optional `format` modifier serves as a hint at the contents and format of the string. 
        - The pattern `keyword` lets you define a regular expression template for the string value.
    - `number`
        - includes both integer and floating-point numbers
        - An optional `format` keyword to specifiy numeric type
        - Use the `minimum` and `maximum` keywords to specify the range of possible values
            - To exclude the boundary values, specify `exclusiveMinimum: true` and `exclusiveMaximum: true`
        - Use the `multipleOf` keyword to specify that a number must be the multiple of another number
    - `integer`
        - similar to number
    - `boolean`
        - true, false
    - `array`
        ```yaml
        type: array
        items:
          type: ...
        ```
        ```yaml
        type: array
        items:
          $ref: '#/components/schemas/Pet'
        ```
        - Mixed-Type Arrays
            ```yaml
            # ["foo", 5, -2, "bar"]
            type: array
            items:
              oneOf:
                - type: string
                - type: integer
            ```
        - Array of arbitrary types
            ```yaml
            type: array
            items: {}
            # [ "hello", -2, true, [5.7], {"id": 5} ]
            ```
        - use `minItems`, `maxItems` to limit array length
        - use `uniqueItems: true` to specify that all items in the array must be unique:
    - `object`
        - **objects are usually defined in the global** `components/schemas` section
        - Required Properties. Note that `required` is an object-level attribute, not a property attribute:
            ```yaml
            type: object
            properties:
              id:
                type: integer
                ...
            required:
              - id
              - username
            ```
        - `readOnly` and `writeOnly`
            - This is useful, for example, when GET returns more properties than used in POST – you can use the same schema in both GET and POST and mark the extra properties as readOnly.
            ```yaml
            type: object
            properties:
              id:
                # Returned by GET, not used in POST/PUT/PATCH
                type: integer
                readOnly: true
              username:
                type: string
              password:
                # Used in POST/PUT/PATCH, not returned by GET
                type: string
                writeOnly: true
            ```
        - Free-Form Object:  (arbitrary property/value pairs) 
            ```yaml
            type: object
            ```
        - `minProperties` and `maxProperties` to restrict the number of properties.
- Mixed Types
    - mixed types can be described using `oneOf` and `anyOf`, which specify a list of alternate types:
    ```yaml
    oneOf:
      - type: string
      - type: integer
    ```
- String Formats
    - An optional `format` modifier serves as a hint at the contents and format of the string. OpenAPI defines the following built-in string formats:
        - `date` , for example, 2017-07-21
        - `date-time` , for example, 2017-07-21T17:32:28Z
        - `password` – a hint to UIs to mask the input
        - `byte` – base64-encoded characters, for example, U3dhZ2dlciByb2Nrcw==
        - `binary` – binary data, used to describe files
    - However, format is an open value, so you can use any formats, even not those defined by the OpenAPI Specification, such as:
        - email, uuid, uri, hostname, ipv4, ipv6, and others ...
- pattern
    - The pattern keyword lets you define a regular expression template for the string value.
    ```yaml
    ssn:
      type: string
      pattern: '^\d{3}-\d{2}-\d{4}$'
    ```
- Any Type
    - `{}` is shorthand syntax for an arbitrary-type schema:
    ```yaml
    components:
      schemas:
        AnyValue: {}
          nullable: true  # optional
          description: Can be any value, including `null`.
    ```

<h2 id="1b22e7dc709b52f1767fe1eb5dc56625"></h2>

### Enums

- example
    ```yaml
              schema:
                type: string
                enum: [asc, desc]
    ```
- Nullable enums
    ```yaml
    type: string
    nullable: true  # <--- Using `nullable: true` alone is not enough here
    enum:
      - asc
      - desc
      - null        # <--- without quotes, i.e. null not "null"
    ```
- Reusable enums
    ```yaml
    components:
      schemas:
        Color:
          ...
    ```

<h2 id="c8bfb014028c3a06cf9b3852c44fb935"></h2>

### Dictionaries(aka. HashMaps, or Associative Arrays )

- To define a dictionary, use `type: object` and use the `additionalProperties` keyword to specify the type of values in key/value pairs
    - For example, a string-to-string dictionary like this:
        ```json
        {
          "en": "English",
          "fr": "French"
        }
        ```
    - is defined using the following schema:
        ```yaml
        type: object
        additionalProperties:
          type: string
        ```

- Value Type
    - The `additionalProperties` keyword specifies the type of values in the dictionary. 
    - Values can be primitives (strings, numbers or boolean values), arrays or objects.
    - For example, a string-to-object dictionary can be defined as follows:
        ```yaml
        type: object
        additionalProperties:
          type: object
          properties:
            code:
              type: integer
            text:
              type: string
        ```
    - can also `$ref` another schema
- Free-Form Objects
    - If the dictionary values can be of any type (aka free-form object), use `additionalProperties: true`:
        ```yaml
        type: object
        additionalProperties: true
        ```
    - This is equivalent to:
        ```yaml
        type: object
        additionalProperties: {}
        ```
- Fixed Keys
    - If a dictionary has some fixed keys, you can define them explicitly as object properties and mark them as required:
        ```yaml
        type: object
        properties:
          default:
            type: string
        required:
          - default
        additionalProperties:
          type: string
        ```
- Examples of Dictionary Contents
    ```yaml
    type: object
    additionalProperties:
      type: string
    example:
      en: Hello!
      fr: Bonjour!
    ```

<h2 id="64f5f3bbd10e6ab7c82ed0cbfa6e519a"></h2>

### oneOf, anyOf, allOf, not

- oneOf – validates the value against exactly one of the subschemas
- allOf – validates the value against all the subschemas
- anyOf – validates the value against any (one or more) of the subschemas
- not - use to make sure the value is not valid against the specified schema.

- oneOf
    ```yaml
    schema:
      oneOf:
        - $ref: '#/components/schemas/Cat'
        - $ref: '#/components/schemas/Dog'
    ```
- allOf
    - allOf takes an array of object definitions that are used for independent validation but together compose a single object. 
    - it does not imply a hierarchy between the models. For that purpose, you should include the `discriminator`. 
- not
    ```yaml
    PetByType:
      type: object
      properties:
        pet_type:
          not:
            type: integer
      required:
        - pet_type
    ```


<h2 id="6f90d7bbdfd5a9ffeda0d201a4164e88"></h2>

### Inheritance and Polymorphism Model Composition

<h2 id="3382c814ef389ff660adac74524d6555"></h2>

#### Model Composition

you can describe the schemas as a composition of the common property set and schema-specific properties.

In OpenAPI version 3, you do this with the `allOf` keyword:

```yaml
components:
  schemas:
    BasicErrorModel:
      type: object
      required:
        - message
        - code
      properties:
        message:
          type: string
        code:
          type: integer
          minimum: 100
          maximum: 600
    ExtendedErrorModel:
      allOf:     # Combines the BasicErrorModel and the inline model
        - $ref: '#/components/schemas/BasicErrorModel'
        - type: object
          required:
            - rootCause
          properties:
            rootCause:
              type: string
```


<h2 id="371fedf6ee6747b1de368aafb08094e8"></h2>

#### Polymorphism

In your API, you can have request and responses that can be described by several alternative schemas.

In OpenAPI 3.0, to describe such a model, you can use the `oneOf` or `anyOf` keywords:

```yaml
components:
  responses:
    sampleObjectResponse:
      content:
        application/json:
          schema:
            oneOf:
              - $ref: '#/components/schemas/simpleObject'
              - $ref: '#/components/schemas/complexObject'
```

<h2 id="3d07d09db1423c8da8e60b5f36d2d903"></h2>

#### Discriminator

To help API consumers detect the object type, you can add the `discriminator/propertyName` keyword to model definitions.

This keyword points to the property that specifies the data type name:

```yaml
components:
  responses:
    sampleObjectResponse:
      content:
        application/json:
          schema:
            oneOf:
              - $ref: '#/components/schemas/simpleObject'
              - $ref: '#/components/schemas/complexObject'
            discriminator:
              propertyName: objectType
  …
  schemas:
    simpleObject:
      type: object
      required:
        - objectType
      properties:
        objectType:
          type: string
      …
    complexObject:
      type: object
      required:
        - objectType
      properties:
        objectType:
          type: string
      …
```


<h2 id="fb70c8533ca8c289d5b1979656ea9efe"></h2>

## Grouping Operations With Tags

You can assign a list of `tags` to each API operation. Tagged operations may be handled differently by tools and libraries.

```yaml
paths:
  /pet/findByStatus:
    get:
      summary: Finds pets by Status
      tags:
        - pets
      ...
  /pet:
    post:
      summary: Adds a new pet to the store
      tags:
        - pets
      ...
  /store/inventory:
    get:
      summary: Returns pet inventories
      tags:
        - store
      ...
```

<h2 id="8654aba8cb48ea7d16c3a3e62163d6ef"></h2>

## Authentication and Authorization

https://swagger.io/docs/specification/authentication/

<h2 id="9679874577b1f897fee85f92a3f05749"></h2>

### Changes from OpenAPI 2.0

- `securityDefinitions` were renamed to `securitySchemes` and moved inside `components`.
- API keys can now be sent `in: cookie`.
- Added support for OpenID Connect Discovery (`type: openIdConnect`).


<h2 id="274df024afe245d7c8eec5c9d549dd9c"></h2>

### Describing Security

Security is described using the `securitySchemes` and `security` keywords.

You use `securitySchemes` to define all security schemes your API supports, then use `security` to apply specific schemes to the whole API or individual operations.

1. Step 1. Defining securitySchemes
    - All security schemes must be defined in the global `components/securitySchemes` section.
        ```yaml
        components:
          securitySchemes:
            BasicAuth:
              type: http
              scheme: basic
            BearerAuth:
              type: http
              scheme: bearer
            ApiKeyAuth:
              type: apiKey
              in: header
              name: X-API-Key
            OpenID:
              ...
        ```
2. Step 2. Applying security
    - apply them to the whole API or individual operations by adding the `security` section on the root level or operation level, respectively. 
    - In the following example, the API calls can be authenticated using either an API key or OAuth 2. 
        ```yaml
        security:
          - ApiKeyAuth: []
          - OAuth2:
              - read
              - write
        ```
    - For each scheme, you specify a list of security scopes required for API calls. Scopes are used only for OAuth 2 and OpenID Connect Discovery; other security schemes use an empty array `[]` instead. Global `security` can be overridden in individual operations.
        ```yaml
        paths:
          /billing_info:
            get:
              summary: Gets the account billing info
              security:
                - OAuth2: [admin]   # Use OAuth with a different scope
              responses:
                '200':
                  description: OK
                '401':
                  description: Not authenticated
                '403':
                  description: Access token does not have the required scope
          /ping:
            get:
              summary: Checks if the server is running
              security: []   # No security
              responses:
                '200':
                  description: Server is up and running
                default:
                  description: Something is wrong
        ```


<h2 id="dff9a265a966b13fec331324fac51b4e"></h2>

### Example: global apiKey auth

```yaml
security: # apply 1 only aothorization globally
  - ApiKeyAuth: [] # apiKey has no scope, so just provide `[]`

components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: token  # use `token` filed in HTTP headers
```







