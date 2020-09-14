...menustart

- [8 Working with web services](#7b7d63cdbd26f14f69e7e90dcf4103c7)
    - [8.1 Using REST APIs](#df0d7e0985c9b27af7dc8078bdd935d9)
        - [8.1.1 Using the HTTP client](#2ac9bab6e0e1503af929373e262bf4dd)
        - [8.1.2 When faults happen](#dcde17007e2905d1c0bf2150aaa80808)
            - [TECHNIQUE 49 Detecting timeouts](#ed8f378a99622e6fa9e881ad40b1ee0a)
            - [TECHNIQUE 50 Timing out and resuming with HTTP](#9828258f9f00dd06f2a1b4105c62f4d6)
    - [8.2 Passing and handling errors over HTTP](#963cdae66bec16a79ef7690052d2047e)
        - [8.2.1 Generating custom errors](#43ed9eb04540fe3034b5b6aa06b1abef)
            - [TECHNIQUE 51 Custom HTTP error passing](#53341acb9a0f40cb60854a46f49a5bf5)
        - [8.2.2 Reading and using custom errors](#85ec98278abcac16ca569a4d95066559)
            - [TECHNIQUE 52 Reading custom errors  TODO](#7fcf93c53d7e837263928d5a87298e27)
    - [8.3 Parsing and mapping JSON](#b9493334b93683d27a08169df7ff3596)
        - [TECHNIQUE 53 Parsing JSON without knowing the schema](#2f8befbec4b0d9643b9d8557bfc3225f)
    - [8.4 Versioning REST APIs](#532f794974813631d51112acb41bd774)
        - [TECHNIQUE 54 API version in the URL  (TODO)](#50b7ca8917f1e5e536411383d910e59c)

...menuend


<h2 id="7b7d63cdbd26f14f69e7e90dcf4103c7"></h2>


# 8 Working with web services

This chapter covers

- Making REST requests
- Detecting timeouts and resuming downloads
- Passing errors over HTTP
- Parsing JSON, including arbitrary JSON structures 
- Versioning REST APIs

<h2 id="df0d7e0985c9b27af7dc8078bdd935d9"></h2>


## 8.1 Using REST APIs

<h2 id="2ac9bab6e0e1503af929373e262bf4dd"></h2>


### 8.1.1 Using the HTTP client

- The HTTP client is found in the `net/http` library within the standard library.
    - It has helper functions to perform GET, HEAD, and POST requests, can perform virtually any HTTP request, and can be heavily customized.
- The helper functions are http.Get, http.Head, http.Post, and http.PostForm.
- With the exception of http.PostForm, each function is for the HTTP verb its name suggests.
    - http.PostForm handles POST requests when the data being posted should be posted as a form.


```go
// Listing 8.1 A simple HTTP get

package main
import (
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
     res, _ := http.Get("http://goinpracticebook.com")
     // Reads the body of the response and
     // closes the Body reader when done reading it
     b, _ := ioutil.ReadAll(res.Body)
     res.Body.Close()
     fmt.Printf("%s", b)
}
```

```go
// Listing 8.2 DELETE request with default HTTP client

package main
import (
    "fmt"
    "net/http"
)

func main() {
    req, _ := http.NewRequest("DELETE", 
        "http://example.com/foo/bar", nil) 
    res, _ := http.DefaultClient.Do(req) 
    fmt.Printf("%s", res.Status)
}
```

- Making a request is broken into two separate parts. 
    - The first part is the request, contained in http.Request instances. 
    - The second part is the client that performs a request.
- The default client has configuration and functionality to handle things like HTTP redirects, cookies, and timeouts.
- It also has a default transport layer that can be customized.

```
// A simple custom HTTP client with timeout
cc := &http.Client{Timeout: time.Second}
res, err := cc.Get("http://goinpracticebook.com")
...
```


<h2 id="dcde17007e2905d1c0bf2150aaa80808"></h2>


### 8.1.2 When faults happen

<h2 id="ed8f378a99622e6fa9e881ad40b1ee0a"></h2>


#### TECHNIQUE 49 Detecting timeouts

- To detect timeouts in the `net` package, the errors returned by it have a Timeout() method that’s set to true in the case of a timeout.
- Yet, in some cases, a timeout occurs and Timeout() doesn’t return true, or the error you’re working with comes from another package, such as url, and doesn’t have the Timeout() method.
- PROBLEM: How can network timeouts be reliably detected?
- SOLUTION: When timeouts occur, a small variety of errors occurs. Check the error for each of these cases to see if it was a timeout.

```
// Listing 8.4 Detect a network timeout from error

// A function whose response is true or false 
// if a network timeout caused the error
func hasTimedOut(err error) bool {
    switch err := err.(type) {
    // A url.Error may be caused by an underlying net
    // error that can checked for a timeout
    case *url.Error:
        if err, ok := err.Err.(net.Error); ok && err.Timeout() {
            return true
        }
    // Looks for timeouts detected 
    // by the net package
    case net.Error:
        if err.Timeout() {
            return true
        }
    case *net.OpError:
        if err.Timeout() {
              return true
        } 
    }
    // Some errors, without a custom type or variable
    // to check against, can indicate a timeout
    errTxt := "use of closed network connection"
    if err != nil && strings.Contains(err.Error(), errTxt) {
        return true
    }
    return false
}
```

- This function provides the capability to detect a variety of timeout situations. The following snippet is an example of using that function to check whether an error was caused by a timeout:

```go
res, err := http.Get("http://example.com/test.zip")
if err != nil && hasTimedOut(err) {
    fmt.Println("A timeout error occured")
    return 
}
```

- Reliably detecting a timeout is useful, and the next technique highlights this in practice.


<h2 id="9828258f9f00dd06f2a1b4105c62f4d6"></h2>


####  TECHNIQUE 50 Timing out and resuming with HTTP

- If a large file is being downloaded and a timeout occurs, starting the download from the beginning isn’t ideal. This is becoming truer with the growth of file sizes.
- It’d be nice to avoid the extra bandwidth use and time to redownload data.
- PROBLEM: You want to resume downloading a file, starting from the end of the data already downloaded, after a timeout occurs.
- SOLUTION: Retry the download again, attempting to use the `Range` HTTP header in which a range of bytes to download is specified.
    - This allows you to request a file, starting partway through the file where it left off.
- DISCUSSION: Servers, such as the one provided in the Go standard library, can support serving parts of a file. 
    - This is a fairly common feature in file servers, and the interface for specifying ranges has been a standard since 1999, when HTTP 1.1 came out:

```go
func main() {
    // Creates a local file to store the download
     file, err := os.Create("file.zip")
     if err != nil {
            fmt.Println(err)
            return
     }
    defer file.Close()
    
    // Downloads the remote file to the local file,
    // retrying up to 100 times
    location := "https://example.com/file.zip"
     err = download(location, file, 100)
     if err != nil {
            fmt.Println(err)
            return
     }
     fi, err := file.Stat()
     if err != nil {
            fmt.Println(err)
            return
     }
     fmt.Printf("Got it with %v bytes downloaded", fi.Size())
}
``` 

```go
// Listing 8.5 Download with retries
func download(location string, file *os.File, retries int64) error {
    // Creates a new GET request for the file being downloaded
    req, err := http.NewRequest("GET", location, nil)
    if err != nil {
        return err
    }
    // Starts the local file to find
    // the current file information
    fi, err := file.Stat()
    if err != nil {
        return err
    }
    // Retrieves the size of the local file
    current := fi.Size()
    if current > 0 {
        start := strconv.FormatInt(current, 10)
        req.Header.Set("Range", "bytes="+start+"-")
    }
    // An HTTP client configured to 
    // explicitly check for timeout
    cc := &http.Client{Timeout: 5 * time.Minute}
    res, err := cc.Do(req)
    // When checking for an error, tries
    // the request again if the error was 
    // caused by a timeout
    if err != nil && hasTimedOut(err) {
        if retries > 0 {
            return download(location, file, retries-1)
        }
        return err
    } else if err != nil {
        return err
    }

    // Handles nonsuccess HTTP status codes
    if res.StatusCode < 200 || res.StatusCode >= 300 {
        errFmt := "Unsuccess HTTP request. Status: %s"
        return fmt.Errorf(errFmt, res.Status)
    }
    // If the server doesn’t support serving 
    // partial files, sets retries to 0
    if res.Header.Get("Accept-Ranges") != "bytes" {
        retries = 0
    }
    // Copies the remote response to the local file
    _, err = io.Copy(file, res.Body)
    if err != nil && hasTimedOut(err) {
        if retries > 0 {
            return download(location, file, retries-1)
        }
        return err
    } else if err != nil {
        return err
    }
    return nil
}
```

- Although the download function can handle timeouts in a fairly straightforward man- ner, it can be customized for your cases:
    - If a hash of a file is easily available, a check could be put in to make sure that the final download matches the hash. This integrity check can improve trust in the final download, even if it takes multiple attempts to download the file.

<h2 id="963cdae66bec16a79ef7690052d2047e"></h2>


## 8.2 Passing and handling errors over HTTP

- The Go standard library provides a rudimentary capability to pass errors. For example, the following listing provides simple HTTP generating an error.

```go
package main
import "net/http"

// Returns an HTTP status 403 with a message
func displayError(w http.ResponseWriter, r *http.Request) {
     http.Error(w, "An Error Occurred", http.StatusForbidden)
}

func main() {
    // Sets up all paths to serve the 
    // HTTP handler displayError
    http.HandleFunc("/", displayError)
    http.ListenAndServe(":8080", nil)
}
```

- This simple server always returns the error message An Error Occurred.
    - Along with the custom message, served with a type of text/plain, the HTTP status message is set to 403, correlating to forbidden access.

```go
// client to check HTTP status
res, _ := http.Get("http://example.com")
fmt.Println(res.Status)
fmt.Println(res.StatusCode)
```

<h2 id="43ed9eb04540fe3034b5b6aa06b1abef"></h2>


### 8.2.1 Generating custom errors

- A plain text error string and an HTTP status code representing an error are often insufficient. 
- For example, if you’re displaying web pages, you’ll likely want your error pages to be styled like your application or site. 
    - Or if you’re building an API server that responds with JSON, you’ll likely want error responses to be in JSON as well.

<h2 id="53341acb9a0f40cb60854a46f49a5bf5"></h2>


#### TECHNIQUE 51 Custom HTTP error passing

- You don’t have much room for customization when using the `Error` function within the `http` package. 
    - The response type is hardcoded as plain text, and the `X-ContentType-Options` header is set to nosniff. 
    - This header tells some tools, such as Microsoft Internet Explorer and Google Chrome, to not attempt to detect a content type other than what was set. 
    - This leaves little opportunity to provide a custom error, aside from the content of the plain text string.
- PROBLEM: How can you provide a custom response body and content type when there’s an error?
- SOLUTION: Instead of using the built-in `Error` function,  use custom functions that send both the correct HTTP status code and the error text as a more appropriate body for your situation.
- To illustrate how this works, let’s look at an error response in JSON. We’ll keep the same response format as the other REST API responses that provide an application- specific error code in addition to the HTTP error. Although this example is targeted at API responses, the same style applies to web pages.

```go
// Listing 8.7 Custom JSON error response

type Error struct {
    HTTPCode int   `json:"-"`
    Code     int    `json:"code,omitempty"`
    Message  string `json:"message"`
}


func JSONError(w http.ResponseWriter, e Error) {
    // Wraps Error struct in anonymous struct 
    // with error property
    data := struct {
        Err Error `json:"error"`
    }{e}
    b, err := json.Marshal(data)
    if err != nil {
       http.Error(w, "Internal Server Error", 500)
       return
    }
    // Sets the response MIME type to application/json
    w.Header().Set("Content-Type", "application/json"
    // Makes sure the HTTP status code
    // is properly set for the error
    w.WriteHeader(e.HTTPCode)
    // Writes the JSON body as output
    fmt.Fprint(w, string(b))
}

func displayError(w http.ResponseWriter, r *http.Request) {

    e := Error{
        HTTPCode: http.StatusForbidden,
        Code:     123,
        Message:  "An Error Occurred",
    }
    // Returns the error message as JSON 
    // when the HTTP handler is called
    JSONError(w, e)
}

func main() {
     http.HandleFunc("/", displayError)
     http.ListenAndServe(":8080", nil)
}
```

- This listing is conceptually similar to listing 8.6. The difference is that listing 8.6 returns a string with the error message, and listing 8.7 returns a JSON response like the following:

```
{
    "error": {
        "code": 123,
        "message": "An Error Occurred"
    }    
}
```


<h2 id="85ec98278abcac16ca569a4d95066559"></h2>


### 8.2.2 Reading and using custom errors

<h2 id="7fcf93c53d7e837263928d5a87298e27"></h2>


#### TECHNIQUE 52 Reading custom errors  TODO
 
- Any client can work with HTTP status codes to detect an error. 
- If an application responds with custom errors, such as those generated by technique 51, this presents an API response with a different structure from the expected response in addition to there being an error.
- PROBLEM: When a custom error with a different structure is returned as an API response, how can you detect that and handle it differently?
- SOLUTION: When a response is returned, check the HTTP status code and MIME type for a possible error.
    - When one of these returns unexpected values or informs of an error, convert it to an error, return the error, and handle the error.


```go
// Listing 8.8 Convert HTTP response to an error

// Structure to hold data from the erro
type Error struct {
     HTTPCode int    `json:"-"`
     Code     int    `json:"code,omitempty"`
     Message  string `json:"message"`
}

// The Error method implements the 
// error interface on the Error struct.
func (e Error) Error() string {
     fs := "HTTP: %d, Code: %d, Message: %s"
     return fmt.Sprintf(fs, e.HTTPCode, e.Code, e.Message)
}

// The get function should be used 
// instead of http.Get to make requests

func get(u string) (*http.Response, error) {
    // Uses http.Get to retrieve the resource
    // and return any http.Get errors
    res, err := http.Get(u)
    if err != nil {
        return res, err
    }
    // Checks if the response code was outside 
    // the 200 range of successful responses
    if res.StatusCode < 200 || res.StatusCode >= 300 {
        // Checks the response content type and
        // returns an error if it’s not correct
        if res.Header.Get("Content-Type") != "application/json" {
            sm := "Unknown error. HTTP status: %s"
            return res, fmt.Errorf(sm, res.Status)
        }
        // Reads the body of the response into a buffer
        b, _ := ioutil.ReadAll(res.Body)
        res.Body.Close()
        // Parses the JSON response and places the data 
        // into a struct and responds to any errors
        var data struct {
            Err Error `json:"error"`
        }
        err = json.Unmarshal(b, &data)
        if err != nil {
            sm := "Unable to parse json: %s. HTTP status: %s"
            return res, fmt.Errorf(sm, err, res.Status)
        }
        // Adds the HTTP status code to the Error instance
        data.Err.HTTPCode = res.StatusCode
        // Returns the custom error and the response
        return res, data.Err
    }
    // When there’s no error, returns the response as expected
    return res , nil
}
```

<h2 id="b9493334b93683d27a08169df7ff3596"></h2>


## 8.3 Parsing and mapping JSON

<h2 id="2f8befbec4b0d9643b9d8557bfc3225f"></h2>


#### TECHNIQUE 53 Parsing JSON without knowing the schema

- PROBLEM: How can you parse a JSON data structure into a Go data structure when you don’t know the structure ahead of time?
- SOLUTION: Parse the JSON into an interface{} instead of a struct. After the JSON is in an inter- face, you can inspect the data and use it.
- A little-known feature of the `encoding/json` package is the capability to parse arbitrary JSON into an `interface{}`. 

```go
// Listing 8.10 Parse JSON into an interface{}

package main
import (
    "encoding/json"
    "fmt"
    "os" 
)

// A JSON document to be parsed 
var ks = []byte(`{
"firstName": "Jean",
"lastName": "Bartik",
"age": 86,
"education": [
    {
        "institution": "Northwest Missouri State Teachers College",
        "degree": "Bachelor of Science in Mathematics"
    } , 
    {
        "institution": "University of Pennsylvania",
        "degree": "Masters in English" 
    } 
],
"spouse": "William Bartik",
"children": [
     "Timothy John Bartik",
     "Jane Helen Bartik",
     "Mary Ruth Bartik"
] 
}`)

func main() {
    // A variable instance of type interface{} 
    // to hold the JSON data
    var f interface{}
    err := json.Unmarshal(ks, &f)
    if err != nil {
       fmt.Println(err)
       os.Exit(1)
    }
    // Accesses the JSON data now 
    // on the interface{}
    fmt.Println(f)
}
```

- Before you can work with the data, you need to access it as a type other than interface{}.
- The following is a way to access firstName:

```go
m := f.(map[string]interface{})
fmt.Println(m["firstName"])
```

- To programmatically walk through the resulting data from the JSON, it’s useful to know how Go treats the data in the conversion. 
- When the JSON is unmarshaled, the values in JSON are converted into the following Go types:
    - bool for JSON Boolean
    - float64 for JSON numbers
    - []interface{} for JSON arrays
    - map[string]interface{} for JSON objects  
    - nil for JSON null
    - string for JSON strings

- Knowing this, you can build functionality to walk the data structure. 
- For example, the following listing shows functions recursively walking the parsed JSON, printing the key names, types, and values.


```go
// Listing 8.11 Walk arbitrary JSON

func printJSON(v interface{}) {
    switch vv := v.(type) {
     case string:
            fmt.Println("is string", vv)
     case float64:
            fmt.Println("is float64", vv)
     case []interface{}:
            fmt.Println("is an array:")
            for i, u := range vv {
                fmt.Print(i, " ")
                printJSON(u)
            }
    case map[string]interface{}:
            fmt.Println("is an object:")
            for i, u := range vv {
                fmt.Print(i, " ")
                printJSON(u)
            }
    default:
        fmt.Println("Unknown type")
    }
}
```


<h2 id="532f794974813631d51112acb41bd774"></h2>


## 8.4 Versioning REST APIs

- Web services evolve and change, which leads to changes in the APIs used to access or manage them. To provide a stable API contract for API consumers, changes to the API need to be versioned. 
- APIs are typically versioned by major number changes such as v1, v2, and v3. 
    - This number scheme signifies breaking changes to the API. 
    - An application designed to work with v2 of an API won’t be able to consume the v3 API version because it’s too different.
- But what about API changes that add functionality to an existing API?
    - For example, say that functionality is added to the v1 API. 
    - In this case, the API can be incremented with a point version; feature additions can increment the API to v1.1. 
    - This tells developers and applications about the additions.


<h2 id="50b7ca8917f1e5e536411383d910e59c"></h2>


####  TECHNIQUE 54 API version in the URL  (TODO)

- PROBLEM: What is an easily accessible method to provide versioned APIs?
- SOLUTION: Provide the API version in the REST API URL. 
    - For example, instead of providing an API of `https://example.com/api/todos`, add a version to the path so it looks like `https://example.com/api/v1/todos`.
- ...




