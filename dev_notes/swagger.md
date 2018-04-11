
# Swagger 

## run swagger editor

docker pull swaggerapi/swagger-ui
docker run -p 8080:8080 swaggerapi/swagger-ui

## swagger UI 

you can integrate swagger UI in you web server

 1. download from [github repository](https://github.com/swagger-api/swagger-ui) 
 2. put dist folder inside your webserver 
 3. through your webserver , lanuch dist/index.html

you can change the  default URL of swagger config file in  webTools/swaggerUI/index.html



