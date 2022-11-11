[](...menustart)

- [7 Serving and receiving assets and forms](#4c4f94964de9b380c09ef02655cd111c)
    - [7.1 Serving static content](#3a682f610038c898479871d57c7b1805)
        - [TECHNIQUE 39 Serving subdirectories](#3c5523c5e1abe28dfc6de26a395bb6bf)
    - [7.2 Handling form posts](#35df994f14b36fba0672e7b4cff94f9f)
        - [7.2.1 Introduction to form requests](#cc10622fdbb0431fa2f773bfd734aaed)
            - [TECHNIQUE 44 Accessing multiple values for a form field](#d899152b3a89a982e960535b41d046e8)
        - [7.2.2 Working with files and multipart submissions](#8ce582ef69928a1ebfc5d6ba03a524b0)
            - [TECHNIQUE 45 Uploading a single file](#8c979490bd1b37dcea666c8f9b4467a9)
            - [TECHNIQUE 46 Uploading multiple files](#a0208958d6a483dda58216795b0b4afe)
            - [TECHNIQUE 47 Verify uploaded file is allowed type](#d2fb3ec944fda34debbc612113660bd6)
        - [7.2.3 Working with raw multipart data](#226c031cb6a7636b20c3491377c5d1eb)
            - [TECHNIQUE 48 Incrementally saving a file](#2aa8a6363809849fc0475ef29b6405c4)

[](...menuend)


<h2 id="4c4f94964de9b380c09ef02655cd111c"></h2>

# 7 Serving and receiving assets and forms

<h2 id="3a682f610038c898479871d57c7b1805"></h2>

## 7.1 Serving static content

- To handle static files, the http package in the standard library has a series of functions that deal with file serving. 

```
// Listing 7.1 http package file serving: file_serving.go

package main
import (
     "net/http"
)
func main() {
    // Uses a directory on the filesystem
    dir := http.Dir("./files")
    // Serves the filesystem directory
    http.ListenAndServe(":8080", http.FileServer(dir))
}
```

- From a directory on the local filesystem, FileServer will serve files following proper permissions.
- It’s capable of looking at the `If-Modified-Since` HTTP header and responding with a 304 Not Modified response if the version of the file a user already has matches the one currently being served.

- When you want to write your own handler to serve files, the ServeFile function in the http package is useful, as shown in the next listing.

```
// Listing 7.2 Serve file with custom handler: servefile.go

// Registers a handler for all paths
func main() {
     http.HandleFunc("/", readme)
     http.ListenAndServe(":8080", nil)
}

// Serves the contents of a readme file
func readme(res http.ResponseWriter, req *http.Request) {
     http.ServeFile(res, req, "./files/readme.txt")
}
```

- This readme handler serves the content of a file located at ./files/readme.txt by using the ServeFile function. 
- And like FileServer, ServeFile looks at the If-Modified-Since HTTP header and responds with a 304 Not Modified response if possible.
- This functionality, along with some of its underpinnings, enables you to serve con- tent by using a variety of techniques.


<h2 id="3c5523c5e1abe28dfc6de26a395bb6bf"></h2>

####  TECHNIQUE 39 Serving subdirectories

```
// Listing 7.3 Serving a subdirectory
func main() {
    // A directory and its subdirectories 
    // on the filesystem are chosen to serve.
    dir := http.Dir("./files/")
    // The /static/ path serves the directory and 
    // needs to be removed before looking up file path.
    handler := http.StripPrefix("/static/", http.FileServer(dir))
    http.Handle("/static/", handler)

    // Serves a home page that may include
    // files from the static directory
    http.HandleFunc("/", homePage)
    http.ListenAndServe(":8080", nil)
```

- Here, the built-in web server is serving the ./files/ directory at the path /static/ by using the file server from the http package. 


<h2 id="35df994f14b36fba0672e7b4cff94f9f"></h2>

## 7.2 Handling form posts

<h2 id="cc10622fdbb0431fa2f773bfd734aaed"></h2>

### 7.2.1 Introduction to form requests

- When a request is made to a server and it contains form data, that request isn’t processed into a usable structure by default. 
- The following example shows the simplest way to parse form data and get access to it:

```go
func exampleHandler(w http.ResponseWriter, r *http.Request) {
     name := r.FormValue("name")
}
```

- Behind this call to `FormValue`, a lot is going on.
    - FormValue starts by parsing the form data into a Go data structure. It’s looking to parse text form data and multipart form data, such as files.
    - After the data is parsed, it looks up the key (form field name) and returns the first value for the key, if one exists.
    - If there’s nothing with this key, an empty string is returned.
- Although this case makes it look easy, a lot is going on that you may not want, and there are features that you can’t access here.
    - For example, what if you want to skip looking for multipart form data and trying to parse it because you know it won’t be present?
    - Or what if a form field has multiple values, and you want to get at all of them?
- The first step to work with form data is to parse it .
    - Inside a request handler are two methods on the Request object that can parse form data into a Go data structure. 
        - The ParseForm method parses fields that contain text. 
        - If you need to work with binary data or files from the form, you need to use ParseMultipartForm.
            - As its name suggests, this method works on multipart form data (a form containing con- tent with different MIME content types).
            - ParseMultipartForm is called by FormValue in the preceding example if parsing hasn’t happened yet.
- The form data is parsed into two locations:
    - The Form property on the Request object will contain the values from the URL query along with the values submitted as a POST or PUT body. 
        - Each key on Form is an array of values. 
        - The FormValue method on Request can be used to get the first value for a key. 
    - When you want the values from the POST or PUT body without those from the URL query, you can use the `PostForm` property on the Request object. 
        - Like FormValue, the `PostFormValue` method can retrieve the first value from PostForm for a key.


```
// Listing 7.10 Parsing a simple form response

func exampleHandler(w http.ResponseWriter, r *http.Request) {
    err := r.ParseForm()
    if err != nil {
        fmt.Println(err)
    }
    // Gets the first value for the name field from the form
    name := r.FormValue("name")
}
```

- This listing contains the handling for a simple form. 
    - This simple example works for forms with only text fields. 
    - If a file field were present, it wouldn’t be parsed or accessible.
    - And it works only for form values that have a single response. HTML forms allow for multiple responding values. 

<h2 id="d899152b3a89a982e960535b41d046e8"></h2>

#### TECHNIQUE 44 Accessing multiple values for a form field

- PROBLEM: FormValue and PostFormValue each return the first value for a form field. 
    - When you have multiple values, how can you access all of them?
- SOLUTION: Instead of using FormValue and PostFormValue to retrieve a field value, look up the field on the `Form or PostForm properties` on the Request object. Then iterate over all the values.

```
// Listing 7.11 Parsing a form with multiple values for a field

func exampleHandler(w http.ResponseWriter, r *http.Request) {
    // The maximum memory to store file parts, where rest is stored to disk
    maxMemory := 16 << 20
    err := r.ParseMultipartForm(maxMemory)
    if err != nil {
        fmt.Println(err)
    }
    for k, v := range r.PostForm["names"] {
        fmt.Println(v)
    }
}
```

- The default number used when FormValue or PostFormValue needs to call ParseMultipartForm is 32 megabytes.
- The names field on the PostForm property is used, limiting the values to just those submitted in the POST or PUT body.

<h2 id="8ce582ef69928a1ebfc5d6ba03a524b0"></h2>

### 7.2.2 Working with files and multipart submissions

<h2 id="8c979490bd1b37dcea666c8f9b4467a9"></h2>

#### TECHNIQUE 45 Uploading a single file

- PROBLEM: When a file is uploaded with a form, how to you process and save it?
- SOLUTION: When a file is uploaded, process the form as a multipart form by using `ProcessMultipartForm` on the Request object.
    - This picks up the file parts. 
    - Then use the FormFile method on the Request object to access and file fields, uploading a single file.
    - For each file, you can access the metadata and a file object that’s similar to File objects from the os package.
- Handling a file is nearly as straightforward as handling text form data.
    - The difference lies in the binary file and the metadata surrounding it, such as the filename.
    - The following listing presents a simple file-upload form.


```
// Listing 7.12 A form with a single-value file-upload field

<!doctype html>
<html>
  <head>
    <title>File Upload</title>
  </head>
  <body>
      <form action="/" method="POST" enctype="multipart/form-data">
        <label for="file">File:</label>
        <input type="file" name="file" id="file">
        <br>
        <button type="submit" name="submit">Submit</button>
      </form>
  </body>
</html>
```

- This form has some important parts. The form method is POST, and its encoding is in multipart.
    - Being multipart allows the text part of the form to be uploaded and processed as text, while the file is handled using its own file type.
    - The input field is typed for a file, which tells browsers to use a file picker and upload the contents of the file. 
- This form is served and processed by the handler function for the http package in the following listing.


```
// Listing 7.13 Handle a single file upload

// http handler to display and process the form in file.html
func fileForm(w http.ResponseWriter, r *http.Request) {
    // When the path is accessed with a GET
    // request, displays the HTML page and form
    if r.Method == "GET" {
        t, _ := template.ParseFiles("file.html")
        t.Execute(w, nil)
    } else {
        // Gets the file handler, header information, and
        // error for the form field keyed by its name
        f, h, err := r.FormFile("file")
        if err != nil {
            panic(err)
        }
        defer f.Close()
        filename := "/tmp/" + h.Filename
        out, err := os.Create(filename)
        if err != nil {
            panic(err)
        }
        defer out.Close()
        // Copies the uploaded file to 
        // the local location
        io.Copy(out, f)
        fmt.Fprint(w, "Upload complete")
    } 
}
```

- The first step used to process the file field is to retrieve it by using the FormFile method on the Request.
    - If the form hasn’t been parsed, FormFile will call Parse- MultipartForm. 
    - FormFile then returns a `multipart.File` object, a `*multipart .FileHeader` object, and an error if there is one.
    - The `*multipart.FileHeader` object has a Filename property that it uses here as part of the location on the local filesystem to store the upload.
- This solution works well for a field with a single file.
    - HTML forms allow for multi- value fields, and this solution will pick up only the first of the files. 
    - For multivalue file uploads, see the next technique.


<h2 id="a0208958d6a483dda58216795b0b4afe"></h2>

#### TECHNIQUE 46 Uploading multiple files

- PROBLEM: How do you process the files when multiple files are uploaded to a single file-input field on a form?
- SOLUTION: Instead of using FormFile,   parse the form and retrieve a slice with the files from the `MultipartForm` property on the Request.  Then iterate over the slice, individually handling each file.

```
// Listing 7.14 A form with a multiple value file-upload field

<!doctype html>
<html>
  <head>
    <title>File Upload</title>
  </head>
  <body>
    <form action="/" method="POST" enctype="multipart/form-data">
      <label for="files">File:</label>
      <input type="file" name="files" id="files" multiple>
      <br>
      <button type="submit" name="submit">Submit</button>
    </form>
</body>
</html>
```

- The `multiple` attribute turns a single file-input field into one accepting multiple files. 

```go
// Listing 7.15 Process file form field with multiple files

func fileForm(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        t, _ := template.ParseFiles("file_multiple.html")
        t.Execute(w, nil)
    } else {
        err := r.ParseMultipartForm(16 << 20)
        if err != nil {
            fmt.Fprint(w, err)
            return
        }
        data := r.MultipartForm
        files := data.File["files"]
        for _, fh := range files {
            f, err := fh.Open()
            defer f.Close()
            if err != nil {
                fmt.Fprint(w, err)
                return
            }
            out, err := os.Create("/tmp/" + fh.Filename)
            defer out.Close()
            if err != nil {
                fmt.Fprint(w, err)
                return
            }
            _, err = io.Copy(out, f)
            if err != nil {
                fmt.Fprintln(w, err)
                return
            }
        }
        fmt.Fprint(w, "Upload complete")
    }
}
```

<h2 id="d2fb3ec944fda34debbc612113660bd6"></h2>

#### TECHNIQUE 47 Verify uploaded file is allowed type

- When a file is uploaded, it could be any type of file. 
     - The upload field could be expecting an image, a document, or something else altogether.
     - But is that what was uploaded? How would you handle an improper file being uploaded?
- PROBLEM: How can you detect the type of file uploaded to a file field inside your application?
- SOLUTION: To get the MIME type for a file, you can use one of a few ways, with varying degrees of trust in the value:
    - When a file is uploaded, the request headers will have a Content-Type field with either a specific content type, such as image/png, or a general value of application/octet-stream.
    - A file extension is associated with a MIME type and can provide insight into the type of file being uploaded.
    - You can parse the file and detect the content type based on the contents of the file.
- These first two methods rely on outside parties for accuracy and trust. 
    - The third solution requires parsing the file and knowing what to look for to map to a content type. This is the most difficult method and uses the most system resources, but is also the most trusted one


```
// he content type here will either be a specific MIME type, 
// such as image/png, or a generic value of 
// application/octet-stream when the type was unknown.
file, header, err := r.FormFile("file")
contentType := header.Header["Content-Type"][0]
```

```
file, header, err := r.FormFile("file")
extension := filepath.Ext(header.Filename)
type := mime.TypeByExtension(extension)
```
 
- The http package contains the function DetectContentType, capable of detecting the type for a limited number of file types. 
    -  These include HTML, text, XML, PDF, PostScript, common image formats, com- pressed files such as RAR, Zip, and GZip, wave audio files, and WebM video files.

```go
file, header, err := r.FormFile("file")
buffer := make([]byte, 512)
_ , err = file.Read(buffer)
filetype := http.DetectContentType(buffer)
```

- The buffer is only 512 bytes because DetectContentType looks at only up to the first 512 bytes when determining the type. When it isn’t able to detect a specific type, application/octet-stream is returned.


<h2 id="226c031cb6a7636b20c3491377c5d1eb"></h2>

### 7.2.3 Working with raw multipart data

- The previous file-handling techniques work well when you’re dealing with small files or files as a whole, but limit your ability to work with files while they’re being uploaded.
    - For example, if you’re writing a proxy and want to immediately transfer the file to another location, the previous techniques will cache large files on the proxy.
- The Go standard library provides both high-level helper functions for common file-handling situations, and lower-level access that can be used for the less common ones or when you want to define your own handling.
- Instead of using the ParseMultipartForm method on the Request object inside an http handler function, you can access the raw stream of the request by accessing the underlying `*multipart.Reader` object. 
    - This object is accessible by using the MultipartReader method on the Request.
 

<h2 id="2aa8a6363809849fc0475ef29b6405c4"></h2>

#### TECHNIQUE 48 Incrementally saving a file

- Imagine that you’re building a system meant to handle a lot of large file uploads. The files aren’t stored on your API server but are instead stored in a back-end service designed for files
- Using ParseMultipartForm is going to put those files into the tem- porary files directory on your API server while the uploads are in progress.
- To support large file uploads with ParseMultipartForm handling, your server would need a large disk cache for the files and careful handling to make sure it doesn’t get full while parallel uploads are happening.

- PROBLEM: You want to save the file, as it’s being uploaded, to a location of your choice. That location could be on the server, on a shared drive, or on another location altogether.
- SOLUTION: Instead of using `ParseMultipartForm`, read the multipart data from the request as it’s being uploaded. This can be accessed with the `MultipartReader` method on the `Request`.  
    -  As files and other information are coming in, chunk by chunk, save and process the parts rather than wait for uploads to complete.


```
// Listing 7.16 HTML form containing a file and text field

<!doctype html>
<html>
  <head>
    <title>File Upload</title>
  </head>
  <body>
    <form action="/" method="POST" enctype="multipart/form-data">
      <label for="name">Name:</label>
      <input type="text" name="name" id="name">
      <br>
      <label for="file">File:</label>
      <input type="file" name="file" id="file">
      <br>
      <button type="submit" name="submit">Submit</button>
    </form>
  </body>
</html>      
```

- 这里，你还是上传一个文件，但是你会额外的设置一个名字

```go
// Listing 7.17 Incrementally save uploaded files

// http handler to display and 
// process the form in file_plus.html
func fileForm(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        t, _ := template.ParseFiles("file_plus.html")
        t.Execute(w, nil)
    } else {
        mr, err := r.MultipartReader()
        if err != nil {
            panic("Failed to read multipart message")
        }
        // A map to store form field values not relating to files
        values := make(map[string][]string)
        maxValueBytes := int64(10 << 20)
        for {
            // Attempts to read the next part,
            // breaking the loop if the end of 
            // the request is reached
            part, err := mr.NextPart()
            if err == io.EOF {
                break
            }

            // Retrieves the name of the form field,
            // continuing the loop if there’s no name
            name := part.FormName()
            if name == "" {
                continue
            }
            // Retrieves the name of the file if one exists
            filename := part.FileName()
            // A buffer to read the value of a text field into
            var b bytes.Buffer
            // If there’s no filename, treats it as a text field
            if filename == ""{
                n, err := io.CopyN(&b, part, maxValueBytes)
                if err != nil && err != io.EOF {
                    fmt.Fprint(w, "Error processing form")
                    return
                }
                maxValueBytes -= n
                if maxValueBytes == 0 {
                    msg := "multipart message too large"
                    fmt.Fprint(w, msg)
                    return
                }
                values[name] = append(values[name],b.String())
                continue
            }

            dst, err := os.Create("/tmp/" + filename)
            defer dst.Close()
            if err != nil {
                return
            }
            // As the file content of a part is uploaded, 
            // writes it to the file
            for {
                buffer := make([]byte, 100000)
                cBytes, err := part.Read(buffer)
                if err == io.EOF {
                    break
                }
                dst.Write(buffer[0:cBytes])
            }
        } 
        fmt.Fprint(w, "Upload complete")
    } // end else
}
```

- Because the handler function parses the form, instead of relying on ParseMultipartForm, you have a few elements to set up before working with the form itself.
    - For access to the data on the form as it comes in, you’ll need access to a reader. 
    - The MultipartReader method on the Request object returns `*mime.Reader`, which you can use to iterate over the multipart body of the request.
    - This reader consumes input as needed.
    - For the form fields not being handled as files, you need a place to store the values. Here a map is created to store the values.
- After the setup is complete, the handler iterates over the parts of the multipart message. 
- The parsing loop can now start handling the parts of the message. 
    - It first checks for the name of the form field by using the FormName method and continues the loop if there’s no name. 
    - Files will have a filename in addition to the name of the field.This can be retrieved by using the FileName method.
    - The existence of a filename is a way to distinguish between file and text-field handling.
- When there’s no filename, the handler copies the value of the content of the field into a buffer and decrements a size counter that starts at 10 megabytes.
    - If the size counter runs down to 0, the parser returns and provides an error.
    - This is put in place as a protection against text-field content being too large and consuming too much memory. 
    - 10 MB is quite large and is the default value inside ParseMultipartForm as well. 
    - If no errors occur, the content of the text form field is stored in the values map previously created and the parsing loop continues on the next part.
- If the parsing loop has reached this point, the form field is a file. A file on the operating system is created to store the contents of the file.
- After the loop completes, the files are all available on disk and the text fields are available on the values map.


