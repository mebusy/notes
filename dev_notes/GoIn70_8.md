# 8 Working with web services

This chapter covers

 - Making REST requests
 - Detecting timeouts and resuming downloads
 - Passing errors over HTTP
 - Parsing JSON, including arbitrary JSON structures 
 - Versioning REST APIs

## 8.1 Using REST APIs

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


### 8.1.2 When faults happen

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

## 8.2 Passing and handling errors over HTTP


