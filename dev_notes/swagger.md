...menustart

- [Swagger](#336ff1e9aa6177ea7a71984fa8c241b9)
    - [run swagger editor](#7a8a1e62c3e177c335813e2cda4f44f0)
    - [swagger UI](#d965025d55377342fd1e4ff3e57ad750)

...menuend


<h2 id="336ff1e9aa6177ea7a71984fa8c241b9"></h2>


# Swagger 

<h2 id="7a8a1e62c3e177c335813e2cda4f44f0"></h2>


## run swagger editor

docker pull swaggerapi/swagger-ui
docker run -p 8080:8080 swaggerapi/swagger-ui

<h2 id="d965025d55377342fd1e4ff3e57ad750"></h2>


## swagger UI 

you can integrate swagger UI in you web server

 1. download from [github repository](https://github.com/swagger-api/swagger-ui) 
 2. put dist folder inside your webserver 
 3. through your webserver , lanuch dist/index.html

you can change the  default URL of swagger config file in  webTools/swaggerUI/index.html



