[](...menustart)

- [Swagger](#336ff1e9aa6177ea7a71984fa8c241b9)
    - [run swagger editor](#7a8a1e62c3e177c335813e2cda4f44f0)
    - [swagger UI](#d965025d55377342fd1e4ff3e57ad750)

[](...menuend)


<h2 id="336ff1e9aa6177ea7a71984fa8c241b9"></h2>

# Swagger 


https://swagger.io/docs/specification/about/


<h2 id="7a8a1e62c3e177c335813e2cda4f44f0"></h2>

## run swagger editor


```bash
docker pull swaggerapi/swagger-ui
docker run -p 8080:8080 swaggerapi/swagger-ui
```

<h2 id="d965025d55377342fd1e4ff3e57ad750"></h2>

## swagger UI 

you can integrate swagger UI in you web server

 1. download from [github repository](https://github.com/swagger-api/swagger-ui) 
 2. put dist folder inside your webserver 
 3. through your webserver , lanuch dist/index.html

you can change the  default URL of swagger config file in  webTools/swaggerUI/index.html



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


# OpenAPI 3.0

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

## operationId

`operationId` is an optional unique string used to identify an operation. If provided, these IDs must be unique among all operations described in your API.

Some common use cases for operationId are:

- Some code generators use this value to name the corresponding methods in code.
- Links can refer to the linked operations by operationId.


## Describing Parameters

- parameters are defined in the `parameters` section of an operation or path
- To describe a parameter, you specify
    - its `name`,
    - location (`in`),
    - data type (defined by either `schema` or `content`)
    - and other attributes, such as `description` or `required`. 
- `parameters` is an array, so, in YAML, each parameter definition must be listed with a dash (`-`) in front of it.


### Parameter Types

- parameter types based on the parameter location , location is determined by the parameter’s `in` key
    - `path` parameters, such as `/users/{id}`
        - remember to add `required: true`, **because path parameters are always required**. 
    - `query` parameters, such as `/users?role=admin`
    - `header` parameters, such as `X-MyHeader: Value`
    - `cookie` parameters, which are passed in the Cookie header, such as `Cookie: debug=0; csrftoken=BUSe35dohU3O1MZvDCU`

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




