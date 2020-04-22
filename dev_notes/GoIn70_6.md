...menustart

 - [HTML and email template patterns](#551cb39cf6cd61643026b5c69708ace0)
     - [6.1 Working with HTML templates](#d5210007822d9412f9be8886d1cc15d5)
         - [6.1.1 Standard library HTML package overview](#6313af959752e16cbeae4d485965926c)
         - [6.1.2 Adding functionality inside templates](#d9e159dad96dcd326f096b14169e7be6)
             - [TECHNIQUE 32 Extending templates with functions](#99fa4e3716a3778375f4959fb3f00631)
         - [6.1.3 Limiting template parsing](#1de21ea456194e25d3eb6be7d9093a72)
             - [TECHNIQUE 33 Caching parsed templates](#98fb0d7ee0f06d754fe01fe1b12afcd3)
         - [6.1.4 When template execution breaks](#9163470a01d717d0da1fbab47b9b39ec)
             - [TECHNIQUE 34 Handling template execution failures](#da3141d1f0022f7895b324724f0cdbd7)
         - [6.1.5 Mixing templates](#22f853fa756854fe5fa6308f42bc872d)
             - [TECHNIQUE 35 Nested templates](#e4e2ec9594eedd2ef2ac71c25a313a90)
             - [TECHNIQUE 36 Template inheritance](#9b8782b53f9f5e3d2cedeac1cfc8c662)
             - [TECHNIQUE 37 Mapping data types to templates](#b2914c824c6c6300b0bbf668e252aba9)
     - [6.2 Using templates for email](#fbc0cec7a75759e1aeb8c7fae504cdc3)
         - [TECHNIQUE 38 Generating email from templates](#699d7da5fe23a02c72bb3e698f6d583b)
     - [Misc](#74248c725e00bf9fe04df4e35b249a19)
         - [\[Template Variables\] save data passed to template to a variable](#ed30bbc495303129fb4477e513e551cb)
         - [\[Template Actions\] If/Else Statements](#0812de613c4cb300a833d5814db883e9)
         - [\[Template Actions\] Range Blocks](#90b958d9e4def0f21334970148c2e468)
         - [\[Template Functions\] Indexing structures in Templates](#ab8399154e5022b391c61841fd1cbd13)
         - [\[Template Functions\] The and/or/not Function](#a9f09db2a01293b05017049ce5f00277)
         - [\[Template Comparison Functions\] Comparisons](#a57ee11d00ba4d9aa7ff987a09dfc04f)
         - [\[Templates Calling Functions\] Function Variables (calling struct methods)](#6a9f61e6e9d9d5477d3b3e8909cd64d5)
         - [\[Templates Calling Functions\] Function Variables (call)](#e1a1b477b6952c7a826e61ed78f242b6)
         - [\[Templates Calling Functions\] Custom Functions](#2669d3ad900881a39850a20c145a0da4)
         - [\[Templates Calling Functions\] Custom Functions (Globally)](#0d7594202ff310485a4fc1e0be91ba11)

...menuend


<h2 id="551cb39cf6cd61643026b5c69708ace0"></h2>


# HTML and email template patterns

 - In the standard library, Go provides template han- dling for both text and HTML.
 - The HTML handling is built on top of the text tem- plate engine to add HTML-aware intelligence.

 - It provides a foundation along with the ability to extend and combine templates.
    - For example, you could nest templates or have a template inherit from another one. 
    - This simple and extensible design allows you to use many common template patterns.


<h2 id="d5210007822d9412f9be8886d1cc15d5"></h2>


## 6.1 Working with HTML templates

 - The html and html/template packages in the standard library provide the foundation for working with HTML.
 - This includes the ability to work with variables and functions in the templates. 
 - The advantage of the html/template package over the text/template package for HTML is the context-aware intelligence that saves developers work.


<h2 id="6313af959752e16cbeae4d485965926c"></h2>


### 6.1.1 Standard library HTML package overview

 - Whereas the `html` package provides only a couple of functions to escape and unescape strings for HTML, 
    - the `html/template` package provides a good foundation for working with templates.
 

```
// Listing 6.1 A simple HTML template: simple.html

<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{.Title}}</title>
  </head>
  <body>
     <h1>{{.Title}}</h1>
     <p>{{.Content}}</p>
  </body>
</html>
```

- actions (also called *directives*), which are enclosed in double curly brackets


```
// Listing 6.2 Using a simple HTML template: simple_template.go

package main
import (
    "html/template"
    "net/http"
)

type Page struct {
    Title, Content string
}

func displayPage(w http.ResponseWriter, r *http.Request) {
    p := &Page{
        Title:   "An Example",
        Content: "Have fun stormin’ da castle.",
    }
    t := template.Must(template.ParseFiles("templates/simple.html"))
    // Writes to HTTP output using template and dataset
    t.Execute(w, p)
}

func main() {
    http.HandleFunc("/", displayPage)
    http.ListenAndServe(":8080", nil)
}
```

 - The html/template package is used here instead of the text/template package because it’s context-aware and handles some operations for you.
 - Being context-aware is more than knowing that these are HTML templates. The package understands what’s happening inside the templates.
 - Take the following template snippet: `<a href="/user?id={{.Id}}">{{.Content}}</a>`
 - The html/template package expands this intelligently. 
    - For escaping purposes, it adds context-appropriate functionality. The preceding snippet is automatically expanded to look like this:
    - `<a href="/user?id={{.Id | urlquery}}">{{.Content | html}}</a>` 
    - The variables (in this case, .Id and .Content) are piped through appropriate functions to **escape** their content before turning it into the final output.
    - If you were using the text/template package, you would need to add the escaping yourself.

 - When you want a variable to be rendered as is, without being escaped, you can use the HTML type in the html/template package.
    - Technique 35 provides an example that uses the HTML type to inject data into a template and avoid escaping.


<h2 id="d9e159dad96dcd326f096b14169e7be6"></h2>


### 6.1.2 Adding functionality inside templates

 - Templates in Go have functions that can and will be called from within them. As you just saw, the intelligence in the HTML templates adds escaping functions in the right place for you. 
 - Out of the box, the template packages provide fewer than 20 functions, and several are to support this intelligence.
 - For example, consider one of the built-in functions, whose implementation is provided by `fmt.Sprintf`, is `printf`. 
 - The following code shows its use inside a template: `{{"output" | printf "%q"}}`
    - The snippet takes the string output and passes it into printf by using the format string %q. The output is the *quoted string* output.


<h2 id="99fa4e3716a3778375f4959fb3f00631"></h2>


####  TECHNIQUE 32 Extending templates with functions

 - Although templates provide quite a few features, often you need to extend them with your own functionality. 
 - For example, we’ve often seen the need to display a date and time in an easy-to-read format. 
 - This common request could easily be implemented as part of the template system.
 - PROBLEM
    - The built-in functions in the templates don’t provide all the functionality you need.
 - SOLUTION
    - Just as Go makes functions available in templates (such as fmt.Sprintf being avail- able in templates as printf), make your own functions available.

 - Go actions, the data and commands enclosed in double curly brackets, can have commands that act on the data. 
    - These commands can be chained into pipelines separated by a `|` . 
    - This is the same idea as using pipes from a UNIX-based command- line interface (CLI)
- Go provides an API to add commands to the **set** available to a template. 
    - The following listing takes a template and adds the capability to display formatted dates.

```go
// Listing 6.3 Add template functions: date_command.go

package main
import (
    "html/template"
    "net/http"
    "time" 
)

// template def 
// Pipes Date through the dateFormat command
var tpl = `<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>Date Example</title>
  </head>
  <body>
    <p>{{.Date | dateFormat "Jan 2, 2006"}}</p>
  </body>
</html>`

// Maps Go functions to template functions
var funcMap = template.FuncMap{
     "dateFormat": dateFormat,
}

// Function to convert a time to a formatted string
func dateFormat(layout string, d time.Time) string {
     return d.Format(layout)
}

func serveTemplate(res http.ResponseWriter, req *http.Request) {
    // Creates a new template.Template instance
    t := template.New("date")
    // Passes additional functions in map into template engine
    t.Funcs(funcMap)
    // Parses the template string into the template engine
    t.Parse(tpl)
    // Creates a dataset to pass into template to display
    data := struct{ Date time.Time }{
           Date: time.Now(),
    }
    // Sends template with data to output response
    t.Execute(res, data)
}

func main() {
     http.HandleFunc("/", serveTemplate)
     http.ListenAndServe(":8080", nil)
}
```

- Rather than referencing an external file, this HTML template is stored as a string in a variable. 

 - Because dateFormat isn’t one of the core template functions, it needs to be made available to the template. 
    - Making custom functions available in templates requires two steps.
        1. a map needs to be created, function name : function 
        2. the function map (here, named funcMap) needs to be passed into `t.Funcs` to make the new function mapping available to templates. 
 - If you’re going to apply the same function set to numerous templates, you can use a Go function to create your templates and add your template functions each time:

```
func parseTemplateString(name, tpl string) *template.Template {
    t:= template.New(name)
    t.Funcs(funcMap)
    t = template.Must(t.Parse(tpl))
    return t
}
```

 - This function could be repeatedly used to create a new template object from a template string with your custom template functions included.


<h2 id="1de21ea456194e25d3eb6be7d9093a72"></h2>


### 6.1.3 Limiting template parsing

- Parsing templates that were originally in text into type instances is a bit of work for a Go application. 
    - Parsing a template turns a string of characters into an object model with a variety of nodes and node types that Go knows how to use.
    - The parser in the `text/template/parser` package sits behind functions such as `template.Parse` and `template.ParseFiles`
 - Methods such as the following technique allow you to avoid extra work by using a `text/template/parser` that can speed up your application.

<h2 id="98fb0d7ee0f06d754fe01fe1b12afcd3"></h2>


#### TECHNIQUE 33 Caching parsed templates

 - Go applications, as servers that respond to multiple requests, can generate many responses to requests from many different clients.
 - If for each response the application has to parse a template, a lot of duplicate work is going on.
 - If you can eliminate some of that work at response time, you can speed up your application’s performance.
 - PROBLEM: You want to avoid repeatedly parsing the same template while an application is running.
 - SOLUTION: Parse the template, store the ready-to-use template in a variable, and repeatedly use the same template each time you need to generate the output.

```go
// Listing 6.4 Caching a parsed template: cache_template.go


package main
import (
    "html/template"
    "net/http"
)

// Parses the template when the package is initialized
// Must is a helper that wraps a call to a function returning (*Template, error) and panics if the error is non-nil. 
//     It is intended for use in variable initializations.
var t = template.Must(template.ParseFiles("templates/simple.html"))

type Page struct {
    Title, Content string
}

func displayPage(w http.ResponseWriter, r *http.Request) {
    p := &Page{
        Title:   "An Example",
        Content: "Have fun stormin’ da castle.",
    }
    // Writes to HTTP output using template and dataset
    t.Execute(w, p)
}

func main() {
    http.HandleFunc("/", displayPage)
    http.ListenAndServe(":8080", nil)
}
```


<h2 id="9163470a01d717d0da1fbab47b9b39ec"></h2>


### 6.1.4 When template execution breaks

 - All software has the potential to fail. Template execution is no exception.
 - When template execution fails, an error is returned. But in some cases, template execution can fail and partial output is displayed to the end user. This can provide an experience you want to avoid.

<h2 id="da3141d1f0022f7895b324724f0cdbd7"></h2>


#### TECHNIQUE 34 Handling template execution failures

 - When templates are executed, the output is written as it walks through the template. 
 - If a function is called, causing an error midway through the template, an error will be returned and execution will stop. 
    - But the part of the template before the error would already be displayed to end users.
 - PROBLEM: When an error happens while executing a template, you want to catch the error before anything is displayed to the user. Instead of displaying the partially broken pages, display something more appropriate, such as an error page.
 - SOLUTION: Write the output of the template to a buffer. If no errors occur, write the output of the buffer to end users. Otherwise, handle the error.

```
    var b bytes.Buffer
    err := t.Execute(&b, p)
    if err != nil {
        fmt.Fprint(w, "A error occured.")
        return 
    }
    b.WriteTo(w)
```


<h2 id="22f853fa756854fe5fa6308f42bc872d"></h2>


### 6.1.5 Mixing templates


1. Template nesting
2. Inheritance
3. Mapping a data object to a specific template
    - for example, a user object being mapped to a user template



<h2 id="e4e2ec9594eedd2ef2ac71c25a313a90"></h2>


#### TECHNIQUE 35 Nested templates

 - Sharing and reusing sections of templates, like code reuse, is a common need. 
 - If you have an application with numerous web pages, you’ll typically find that most elements are common across pages, and some elements are custom.
 - PROBLEM: You want to avoid duplicating the common sections of HTML markup in each template and the maintenance burden that goes along with that. Like the software you’re developing, you want to take advantage of reuse.
 - SOLUTION: Use nested templates to share common sections of HTML. The subtemplates enable reuse for sections of markup, cutting down on duplication.

```
// Listing 6.6 Index template including head template: index.html

<!DOCTYPE HTML>
<html>
  {{template "head.html" .}}
  <body>
       <h1>{{.Title}}</h1>
       <p>{{.Content}}</p>
  </body>
</html>
```

 - The directive {{template "head.html" .}} has three parts.
    1. `template` tells the template engine to include another template,
    2. and `head.html` is the name of that template.
    3. The final part is the `.` after head.html.  This is the dataset to pass to the template.
        - In this case, the entire dataset from the parent template is passed to this template.
        - If a property on the dataset contained a dataset for a subtemplate, that could be passed in.
            - For example, if `{{template "head.html" .Foo}}` were used, the properties on `.Foo` would be the ones available inside head.html

```
// Listing 6.7 Head template included in the index: head.html

<head>
<meta charset="utf-8">
<title>{{.Title}}</title>
</head>
```

```go
// Loads the two templates into a template object
func init() {
    t = template.Must(template.ParseFiles("index.html", "head.html"))
}

func diaplayPage(w http.ResponseWriter, r *http.Request) {
    p := &Page{
        Title:   "An Example",
        Content: "Have fun stormin’ da castle.",
    }
    // use t.ExecuteTemplate Instead
    t.ExecuteTemplate(w, "index.html", p)
}
```

 - When the template is executed, *ExecuteTemplate* is used so that the template name to execute can be specified.
 - If *Execute* had been used, as in the previous listings, the first template listed in ParseFiles would be used. 
 - *ExecuteTemplate* provides control over the template file when multiple ones are available.

---

 - If you want nest template not from file but strings...


```go
  {{template "head_html" .}}
  
....

    t:= template.New("head_html")
    t = template.Must(t.Parse(t_head_html))

    t = t.New( "event_html" )
    t = template.Must(t.Parse(t_event_html))
```


<h2 id="9b8782b53f9f5e3d2cedeac1cfc8c662"></h2>


#### TECHNIQUE 36 Template inheritance

```
// Listing 6.9 A base template to inherit from: base.html

{{define "base"}}<!DOCTYPE HTML>    // start a new base template
<html>
  <head>
    <meta charset="utf-8">                  // invokes the title template,
    <title>{{template "title" .}}</title>   // which is defined elsewhere
    {{ block "styles" . }}<style>       // Defines and immediately invokes 
      h1 {
        color: #400080
      }
    </style>{{ end }}
  </head>
  <body>
     <h1>{{template "title" .}}</h1>
     {{template "content" .}}
     {{block "scripts" .}}{{end}}  // Defines and invokes the scripts template,which is currently empty. 
  </body>                          // An extending template can redefine the contents of scripts. 
</html>{{end}}
```

 - Instead of the entire file being a template, the file contains multiple templates.
 - Each template starts with a `define` or `block` directive and closes with an `end` directive.
    - The block directive defines and immediately executes a template.
    - The `base` template, which can be referred to by name, invokes other templates but doesn’t necessarily define them.
 - Templates that extend this one, such as listing 6.10, will need to fill in the missing templates. 
    - In other cases, you may have a section with default content that you want to allow to be overridden by an extending template.
    - Some sections may be optional. For those sections, you can cre- ate empty templates to be used by default.
 - The block directive and ability to redefine template sections that have content was introduced in Go 1.6. Prior to this, you couldn’t redefine templates that had content.

```
// Listing 6.10 Inheriting required sections: user.html

{{define "title"}}User: {{.Username}}{{end}}
{{define "content"}}
<ul>
  <li>Userame: {{.Username}}</li> 
  <li>Name: {{.Name}}</li>
</ul>
{{end}}
```

 - Templates extending the base need to make sure all of the subtemplates without a default are filled out.
    - Here the title and content sections need to be defined because they’re required. 
    - You’ll notice that the optional sections with empty or default content defined from listing 6.9 don’t need to have sections defined.

 - The following listing showcases filling in an optional template in addition to the required sections.

```
// Listing 6.11 Inheriting with optional section: page.html

{{define "title"}}{{.Title}}{{end}}
        {{define "content"}}
        <p>
{{.Content}}
</p>
{{end}}
{{define "styles"}}
<style>
h1 {
     color: #800080
}
</style>
{{end}}
```

 - Here the `styles` template is defined.  This overrides the default supplied in listing 6.9.


<h2 id="b2914c824c6c6300b0bbf668e252aba9"></h2>


#### TECHNIQUE 37 Mapping data types to templates

 - The previous two template techniques rendered all the output together. A dataset consisting of the entire page needs to be passed in, and the template setup needs to handle the variations to the full page.
 - An alternative approach is to render parts of the page, such as a user object instance, on its own and then pass the rendered content to a higher-level template.
 - PROBLEM: You want to render an object to HTML and pass the rendered object to a higher-level template, where it can be part of the output.
 - SOLUTION: Use templates to render objects as HTML. Store the HTML in a variable and pass the HTML to higher-level templates wrapped in `template.HTML`, marking it as safe HTML that doesn’t need to be escaped.

 - There are a couple reasons to have multiple rendering steps.
    - First, if part of the page is expensive to generate a dataset for or render to HTML, it’s worth not repeating when each page is generated.
    - In a second case, say you have applications with complicated logic and have many pages to render. You could have many templates containing a lot of duplicate markup.
        - If each template were instead scoped to render one thing the templates could be easier to manage. 

 - The following listing shows how to render an object from a template, store the HTML, and later inject it into another template.

```
// Listing 6.13 A Quote object template: quote.html

<blockquote>
&ldquo;{{.Quote}}&rdquo;
&mdash; {{.Person}}
</blockquote>
```

 - This template, quote.html, is associated with a Quote object. 
    - The template is used to render the Quote object as HTML and has Quote object fields to render.
    - You’ll notice there are no other elements for a complete page here.
    - Instead those are part of index.html, shown in the following listing.
    - Here, `.Content` will be an template.HTML object

```
// Listing 6.14 A generic page wrapper: index.html

<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{.Title}}</title>
  </head>
  <body>
     <h1>{{.Title}}</h1>
     <p>{{.Content}}</p>
  </body>
</html>
```


```go
// Listing 6.15 Bringing the templates together: object_templates.go

package main
import (
    "bytes"
    "html/template"
    "net/http"
)

var t *template.Template
var qc template.HTML

func init() {
    t = template.Must(template.ParseFiles("index.html", "quote.html"))
}

type Page struct {
     Title   string
     Content template.HTML
}
type Quote struct {
     Quote, Name string
}

func main() {
    q := &Quote{
        Quote: `You keep using that word. I do not think
               it means what you think it means.`,
        Person: "Inigo Montoya",
    }
    var b bytes.Buffer
    // Writes template and data
    t.ExecuteTemplate(&b, "quote.html", q)
    // Stores quote as HTML in global variable
    qc = template.HTML(b.String())
    http.HandleFunc("/", diaplayPage)
    http.ListenAndServe(":8080", nil)
}

func diaplayPage(w http.ResponseWriter, r *http.Request) {
    p := &Page{
         Title:   "A User",
         Content: qc,
    }
    t.ExecuteTemplate(w, "index.html", p)
}
```

 - WARNING User input HTML should never be considered safe. Always escape user input information, such as information gathered from a form field, before presenting.


<h2 id="fbc0cec7a75759e1aeb8c7fae504cdc3"></h2>


## 6.2 Using templates for email

 - The Go standard library doesn’t provide a special template package for email as it does for HTML.
 - Instead, the text and html template packages provide what you need to send text and HTML email.

<h2 id="699d7da5fe23a02c72bb3e698f6d583b"></h2>


####  TECHNIQUE 38 Generating email from templates

 - PROBLEM: When creating and sending email, you want to incorporate templates.
 - SOLUTION: Use the template packages to generate the email text into a buffer. Pass the generated email in the buffer to the code used to send the email, such as the `smtp` package.
 - The following listing creates email messages from a template and sends them using the `net/smtp` package.


```go
// Listing 6.16 Send email from a template: email.go

package main
import (
     "bytes"
     "net/smtp"
     "strconv"
     "text/template"
)
// The data structure for an email
type EmailMessage struct {
     From, Subject, Body string
     To                  []string
}
type EmailCredentials struct { 
    Username, Password, Server string 
    Port int
}

// The email template as a string
const emailTemplate = `From: {{.From}}
To: {{.To}}
Subject {{.Subject}}

{{.Body}} 
`

var t *template.Template
func init() {
     t = template.New("email")
     t.Parse(emailTemplate)
}

func main() {
     message := &EmailMessage{
        From:    "me@example.com",
        To:      []string{"you@example.com"},
        Subject: "A test",
        Body:    "Just saying hi",
    }
    var body bytes.Buffer
    t.Execute(&body, message)

    // Sets up the SMTP mail client
    authCreds := &EmailCredentials{
       Username: "myUsername",
       Password: "myPass",
       Server:   "smtp.example.com",
       Port:     25,
    }
    auth := smtp.PlainAuth("",
       authCreds.Username,
       authCreds.Password,
       authCreds.Server,
    )
    // Sends the email
    smtp.SendMail(authCreds.Server+":"+strconv.Itoa(authCreds.Port),
       auth,
       message.From,
       message.To,
       body.Bytes())  // The bytes from the message buffer 
                      // are passed in when the message is sent.
}
```

 - You’ll notice the listing is using the text/template package instead of the html/template package used in the previous listings in the chapter. 
 - When you execute the template with a dataset, pass in a buffer to store the ren- dered template. The buffer provides the source of the content to send from the mail client.
 - This concept can be expanded to send a variety of email in a variety of ways.
    - For example, you could use the html/template package to send HTML email. 
    - Or you could combine this with the other template techniques to create complex templates.

-----


<h2 id="74248c725e00bf9fe04df4e35b249a19"></h2>


## Misc

[template cheatsheet](https://curtisvermeeren.github.io/2017/09/14/Golang-Templates-Cheatsheet)

<h2 id="ed30bbc495303129fb4477e513e551cb"></h2>


### [Template Variables] save data passed to template to a variable

```
{{$number := .}}
<h1> It is day number {{$number}} of the month </h1>
```

```go
var tpl *template.Template
tpl = template.Must(template.ParseFiles("templateName"))
err := tpl.ExecuteTemplate(os.Stdout, "templateName", 23)
```

<h2 id="0812de613c4cb300a833d5814db883e9"></h2>


### [Template Actions] If/Else Statements

```
<h1>Hello, {{if .Name}} {{.Name}} {{else}} there {{end}}!</h1>
```

Templates also provide `{{else if .Name2 }}` which can be used to evaluate a second option after an if.


<h2 id="90b958d9e4def0f21334970148c2e468"></h2>


### [Template Actions] Range Blocks

```go
type Item struct {
    Name  string
    Price int
}
```



```
{{range .Items}}
  <div class="item">
    <h3 class="name">{{.Name}}</h3>
    <span class="price">${{.Price}}</span>
  </div>
{{end}}
```

Within a range each Item becomes the {{.}} in the template and the item properties become {{.Name}} or {{.Price}} .

---

```
{{ range $index, $event := .Events }}
    <tr>
        <td> {{$event.Event}} </td>
        <td> {{$event.StartTime | utctimestampToBeijingDate}} </td>
        <td> {{$event.Deadline | utctimestampToBeijingDate}} </td>
        <td> {{$event.EndTime | utctimestampToBeijingDate}} </td>
    </tr>
{{ end }}
```

<h2 id="ab8399154e5022b391c61841fd1cbd13"></h2>


### [Template Functions] Indexing structures in Templates

```
<body>
    <h1> {{index .FavNums 2 }}</h1>
</body>
```

<h2 id="a9f09db2a01293b05017049ce5f00277"></h2>


### [Template Functions] The and/or/not Function

```
{{if and .User .User.Admin}}
  You are an admin user!
{{else}}
  Access denied!
{{end}}
```

```
{{ if not .Authenticated}}
  Access Denied!
{{ end }}
```

<h2 id="a57ee11d00ba4d9aa7ff987a09dfc04f"></h2>


### [Template Comparison Functions] Comparisons

- The html/template package provides a variety of functions to do comparisons between operators.
- The operators may only be basic types or named basic types such as `type Temp float32` 
- Remember that template functions take the form `{{ function arg1 arg2 }}`.
    - eq Returns the result of arg1 == arg2
    - ne Returns the result of arg1 != arg2
    - lt Returns the result of arg1 < arg2
    - le Returns the result of arg1 <= arg2
    - gt Returns the result of arg1 > arg2
    - ge Returns the result of arg1 >= arg
- `{{ eq arg1 arg2 }}`
- `{{ eq arg1 arg2 arg3 arg4}}` will result in the following logical expression:
    - `arg1==arg2 || arg1==arg3 || arg1==arg4`


<h2 id="6a9f61e6e9d9d5477d3b3e8909cd64d5"></h2>


### [Templates Calling Functions] Function Variables (calling struct methods)

```go
type User struct {
  ID    int
  Email string
}

func (u User) HasPermission(feature string) bool {
  if feature == "feature-a" {
    return true
  } else {
    return false
  }
}
```

```
{{if .User.HasPermission "feature-a"}}
  <div class="feature">
    <h3>Feature A</h3>
    <p>Some other stuff here...</p>
  </div>
{{else}}
  <div class="feature disabled">
    <h3>Feature A</h3>
    <p>To enable Feature A please upgrade your plan</p>
  </div>
{{end}}
```

<h2 id="e1a1b477b6952c7a826e61ed78f242b6"></h2>


### [Templates Calling Functions] Function Variables (call)

If the Method HasPermission has to change at times, previous implementation may not fit the design.

Instead a HasPermission func(string) bool attribute can be added on the *User* type.

```go
type User struct {  
  ID            int
  Email         string
  HasPermission func(string) bool
}

// Example of creating a ViewData
vd := ViewData{
        User: User{
            ID:    1,
            Email: "curtis.vermeeren@gmail.com",
            // Create the HasPermission function
            HasPermission: func(feature string) bool {
                if feature == "feature-b" {
                    return true
                }
                return false
            },
        },
    }
```

We use the `call` keyword supplied by the go html/template package. 

```
{{if (call .User.HasPermission "feature-b")}}
  <div class="feature">
    <h3>Feature B</h3>
    <p>Some other stuff here...</p>
  </div>
{{else}}
  <div class="feature disabled">
    <h3>Feature B</h3>
    <p>To enable Feature B please upgrade your plan</p>
  </div>
{{end}}
```


<h2 id="2669d3ad900881a39850a20c145a0da4"></h2>


### [Templates Calling Functions] Custom Functions

Create custom function with template.FuncMap .

```go
// Creating a template with function hasPermission
testTemplate, err = template.New("hello.gohtml").Funcs(template.FuncMap{
    "hasPermission": func(user User, feature string) bool {
      if user.ID == 1 && feature == "feature-a" {
        return true
      }
      return false
    },
  }).ParseFiles("hello.gohtml")
```

The function could be executed in the template as follows:

```
{{ if hasPermission .User "feature-a" }}
```

The .User and string "feature-a" are both passed to hasPermission as arguments.


<h2 id="0d7594202ff310485a4fc1e0be91ba11"></h2>


### [Templates Calling Functions] Custom Functions (Globally)

Functions that dost not rely on object ( e.g `user` ).  And this is one that introduced in very beginning of this chapter.

```go
  testTemplate, err = template.New("hello.gohtml").Funcs(template.FuncMap{
    "hasPermission": func(feature string) bool {
      return false
    },
  }).ParseFiles("hello.gohtml")
```



