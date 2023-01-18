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



