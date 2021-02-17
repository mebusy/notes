# Web Development

- cool sites
    - [codepen](https://codepen.io/)
    - [css tricks](https://css-tricks.com/)
- [course repo](https://github.com/jhu-ep-coursera/fullstack-course4)


## 1 Introduction to HTML5

- [check wheter a tag can use](https://caniuse.com/)
- [W3C validator for your page](https://validator.w3.org/)

### 1.1 Basic HTML Document Structure

- self-closing tag: `<p/>`
    - a tag that happens to not to contain any content
    - for example, a placeholder for some other content that we'll dynamically perhaps insert at some later point.
        - but in practice, it'd better use opening/closing pair to signify the lack of content.

<details>
<summary>
<b>Anatomy of an HTML structure</b>
</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
</body>
</html>
```
- Attributes
    - `charset` : attribute name
    - `"UTF-8"`: attribute value
- doctype declaration
    - `<!DOCTYPE html>`
    - to distinguish between noncompliant and compliant pages
        - noncompliant pages were rendered in what's called the quirks mode
        - compliant pages were rendered in what's called the standards mode
    - if your pages miss doctype declaration, that will signal to the browser that if should treat your pages as one not following HTML standard. Things would be a bit messed up.
    - So to make a long story short always use the simple HTML5 declaration.
- Head
    - contains items that describe the main content of the page.
    - things like 
        - what character coding should the browser use for the main content.
        - authors description
        - page title
        - whatever other external resources are needed to render the page properly.

</details>



### 1.2 HTML Content Models

- The term *content model* refers to which elements are allowed to be nested inside which other elements
- Prior to html5 specification, HTML elements were either block level or inline elements.
    - By default, a block-level element tries to take up as much horizontal space as its containing element will allow

Block-Level Elements | Inline Elements
--- | ---
Render to begin on a new line (by default) |Render on the same line (by default)
May contain inline or other block-level elements |May only contain other inline elements
Roughly Flow Content (HTML5 category) |Roughly Phrasing Content (HTML5 category)


- HTML5 split these 2 content models into **7 models**.
    - [html5 content model](https://www.w3.org/TR/2011/WD-html5-author-20110809/content-models.html#kinds-of-content)
- However, this triditional distinction remains practical because it aligns well with existing CSS rules.

<details>
<summary>
<b>example with dev and span</b>
</summary>

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>div and span elements</title>
</head>
<body>
  <div>*** DIV 1: Some content here ***</div>
  <div>*** DIV 2: Following right after div 1 ***</div>
  <span>*** SPAN 1: Following right after div 2 ***</span>
  <div>
    *** DIV 3: Following right after span 1 
    <span>*** SPAN 2: INSIDE div 3 ***</span>
    Continue content of div 3 ***
  </div>
</body>
</html>
```

- even though span1 is an inline element, since div2 requires that it be on its own line, it pushes the next inline element to it's own line as well.
- this is exactly what happens with div3. even though span is an inline element, technically speaking the tags shouldn't go anywhere but right behind span1. But since div3 is a block level element, it requires it's own line so it's get pushed to the next line to be by itself.

</details>



### 1.6 Essential HTML5 Tags

#### Heading Elements (and some new HTML5 semantic comments)

<details>
<summary>
Heading Elements h1, h2, ...
</summary>

```html
<body>
  <h1>This is the Main Heading</h1>
  <h2>Subheading 2</h2>
  <h3>Subheading 3</h3>
  <h4>Subheading 4</h4>
  <h5>Subheading 5</h5>
  <h6>Subheading 6</h6>
</body>
```

- Couple of important points to understand about these elements
    - first, even though their default rendering in the browser appears to give them visual distinction, these should not be used for styling.
        - these elements are only meant to convey structure of your HTML page, nothing more.
        - With CSS,  any regular development can be styled to look like any one of these heading tags.  So, why not just use a `div` ?  Because if we did, we would lose the meaning of what a heading is.
    - second, something that's marked `h1` is obviously the most important and generalized description of the content of this page.

</details>



<details>
<summary>
Some new HTML5 semantic
</summary>

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Heading Elements</title>
</head>
<body>
  <header>
    header element - Some header information goes here. Usually consists of company logo, some tag line, etc. Sometimes, navigation is contained in the header as well.
    <nav>nav (short for navigation) element - Usually contains links to different parts of the web site.</nav>
  </header>
  <h1>Main Heading of the Page (hard not to have it)</h1>
  <section>
    Section 1
    <article>Article 1</article>
    <article>Article 2</article>
    <article>Article 3</article>
  </section>
  <section>
    Section 2
    <article>Article 4</article>
    <article>Article 5</article>
    <article>Article 6</article>
    <div>Regular DIV element</div>
  </section>
  <aside>
    ASIDE - Some information that relates to the main topic, i.e., related posts.
  </aside>

  <footer>
    JHU Copyright 2015
  </footer>
</body>
</html>
```

- header tag
    - header information about the page
    - usually consists of company logo, some tagline, navigation.
- nav tag
    - navigation
- section / article
    - no hard rule about them
- aside tag
    - something related to the main content of the page.
- footer tag

</details>

### 1.7 Lists

<details>
<summary>
Unordered List
</summary>

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Unordered Lists</title>
</head>
<body>
  <h1>Unordered list</h1>
  <div>
    
    My typical dinner shopping list:
    <ul>
      <li>Milk</li>
      <li>Donuts</li>
      <li>Cookies
        <ul>
          <li>Chocolate</li>
          <li>Sugar</li>
          <li>Peanut Butter</li>
        </ul>
      </li>
      <li>Pepto Bismol</li>
    </ul>
  </div>
</body>
</html>
```

</details>


<details>
<summary>
Ordered List
</summary>

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Ordered Lists</title>
</head>
<body>
  <h1>Ordered list</h1>
  <div>
    Oreo cookie eating procedure:
    <ol>
      <li>Open box</li>
      <li>Take out cookie</li>
      <li>Make a Double Oreo
        <ol>
          <li>Peel off the top part</li>
          <li>Place another cookie in the middle</li>
          <li>Put back the top part</li>
        </ol>
      </li>
      <li>Enjoy!</li>
    </ol>
  </div>
</body>
</html>
```

</details>


### 1.8 HTML Character

- 3 Characters You Should Always Escape: 
    - `<, >, &`
    - use: `&lt; &gt; &amp;`
- non-breaking space: `&nbsp;`
    - very commonly used
    - used to make serveral words never to wrap ( always keep in same line )
    - someone use `&nbsp;` to make more extra spaces. That's a total misuse.
        - If you ever wanted to have spaces, or extra spaces, between some words, what you would do is warpping around those text in a *span* tag, and then apply some left margin.
- `"` may be rendered incorrectly when viewing under some limited encoding.
    - can use `&quot;` instead.


### 1.9 Creating Links

<details>
<summary>
Internal Links

> link to a file in the same directory as this HTML file

</summary>

```html
<body>
  <h1>Internal Links</h1>
  <section>
    We can link to a file in the same directory as this HTML file like this:
    <a href="same-directory.html" title="same dir link">Linking to a file in the same directory</a>

    <a href="same-directory.html" title="same dir link">
      <div> DIV Linking to a file in the same directory</div>
    </a>
  </section>
</body>
```

- Notice: the *a* tag is both a Flow content and a Phrasing content.
    - Allow us to take the *a* tag and surround a *div* tag inside it. 
    - The authors of the HTML5 specificatior realized that there are a lot of times where you would like to be able to click on a whole region, e.g. a logo or some sort of a company name in the top left corner for example.
        - Prior to HTML5, people had to use all kinds of tricks in order to achieve that effect because *a* tag was only an inline tag.

</details>


<details>
<summary>
External Links

> can use `target="_blank"` to force open it in a new tab
</summary>

```html
<body>
  <h1 id="top">External Links</h1>
  <section>
    <p>
      Let's link to a Facebook Fan page I created for this course!
      <!-- link to Facebook page WITH TARGET-->
      <a href="http://www.facebook.com/CourseraWebDev" 
      target="_blank" title="Like Our Page!">Course Facebook Page</a>
    </p>
  </section>
</body>
```

</details>


<details>
<summary>
Same Page Links

> href="#id-name"
</summary>

```html
<body>
  <h1 id="top">Links to Sections of The Same Page</h1>
  <section>
    <ul>
      <!-- Link to every section in the page -->
      <li><a href="#section1">#section1</a></li>
      <li><a href="#section2">#section2</a></li>
      <li><a href="#section3">#section3</a></li>
      <li><a href="#section4">#section4</a></li>
      <li><a href="#section5">#section5</a></li>
      <li><a href="#section6">#section6</a></li>
    </ul>

  </section>

  <section id="section1">
    <h3>(#section1) Section 1</h3>
    <p>Section 1 Content</p>
  </section>

  <section id="section2">
    <h3>(#section2) Section 2</h3>
    <p> Section 2 content</p>
  </section>
  <section id="section3">
    <h3>(#section3) Section 3</h3>
    <p>Section 3 content</p>
  </section>
  <section id="section4">
    <h2>(#section4) Section 4</h2>
    <p>Section 4 content</p>
  </section>
  <section id="section5">
    <h2>(#section5) Section 5</h2>
    <p>Section 5 content</p>
  </section>
  <div>
    <h2><a name="section6">(#section6) Section 6</a></h2>
    <p>
      Back to top: <a href="#top">Back to Top</a>
    </p>
  </div>
</body>
```

- You can identify a section a couple of different ways.
    - you can have in any tag that has an *id* with that section name
    - another way is to create a anchor tag with a *name* attribute 
        - similar to *id*

</details>

### 1.10 Displaying Images

```html
<p>
  <img src="picture-with-quote.jpg" width="400" height="235" alt="Picture with a quote"> 
  Some content
</p>
<p>
<img src="http://lorempixel.com/output/nature-q-c-640-480-1.jpg" width="640" height="480">
</p>
```

- alt attribute
    - is used by screen readers that help people with visual impairment.
- it is always a good idea to provide the *width* and *height* attributes.
    - because if the image take time to load, the page might appear jumpy.
    - this is actually the promary reason why you would want to use the width and height of the image. You want to tell the browser to reserver this space.

### Tag List

tag | stands for | desc
--- | --- | ---
p | paragraph | 
div | division | most generic block-level element
span | span |  super generic inline element
ul | unordered list | only `li` element is allowed inside it
ol | ordered list 
li | list item


---

## 2 Introduction to CSS3

- CSS: Cascading style sheets

### 2.12 Anatomy of a CSS Rule

```css
<style>
p {
    color: blue;
    font-size: 20px;
}

h1 {
    color: green;
    width: 200px;
    text-align: center;
}
</style>
```

- *p* is a **Selector**
    - which is basically saying that whatever rules I'm about to give should apply to the content of **every single** paragraph tag in the entire HTML page.
- Inside the braces, we have CSS declaration.
    - it consists of 2 parts: property and value.
    - **Property** name is something predefined by CSS specification.
    - technically speaking, a semicolon is not a requirement, but it's a best practice to always use it.
    - 0 or more declarations are allowed.
- style sheet
    - the collection of CSS rules.


### 2.13 Element, Class, and ID Selectors

- Selectors
    - CSS selectors are used to determine which HTML element, or set of elements, to apply the CSS declarations to. 
    - The browser uses its selector API to traverse the DOM or Document Object Model, and pick out the elements matching the selector. 
    - Now crafting a selector is a great skill to have and not only for styling using CSS. That's because a lot of JavaScript libraries out there use the browser selector API to attach behavior and data to HTML elements. Much in the same way that CSS applies style to those elements.
- There are 3 different types of selectors: element, class, and id selector.
    - Element Selector: just you specifying the element name
        ```css
        p {
            color: blue;
        }
        ```
        ```html
        <p> ... </p>
        ```
    - Class Selector: is specifyied with a dot and the name of the class
        ```css
        .blue {
            color: blue;
        }
        ```
        ```html
        <p class="blue"> ... </p>
        <div class="blue"> ... </div>
        ```
    - id Selector: specify the value of an id of an element, preceded by a pound sign
        - **least reusable** one, because one id can only appear once in a document.
        ```css
        #name {
            color: blue;
        }
        ```
        ```html
        <div id="name"> ... </div>
        ```
- Grouping Selectors
    ```css
    div, .blue {
        color: blue;
    }
    ```
    - separate selectors with commas


### 2.14 Combining Selectors

- Combining Selectors is a very powerful technique that allows you to more precisely target dumb elements.
- most common ways of combining CSS selectors
    - Element With Class Selector
        ```css
        p.big {
            font-size: 20px; 
        }
        ```
        ```html
        <p class="big"> ... </p>
        ```
    - Child Selector
        - affect on the **direct** child
        ```css
        article > p {
            color: blue;
        }
        ```
        ```html
        <article>
            <p> affected </p>
        </article>
        <article>
            <div> <p> Unaffected </p> </div>
        </article>
        ```
    - Descendant Selector
        - affect on child at any level, even if it's not a direct child
        ```css
        article p {
            color: blue;
        }
        ```
        ```html
        <article>
            <p> affected </p>
        </article>
        <article>
            <div> <p> affected </p> </div>
        </article>
        ```
    - Another 2 Selector (less common)
        - Adjacent sibling selector ( selector + selector )
        - General sibling selector ( selector ~ selector )
- Those combinations are  **Not Limited** To Element Selectors
    ```css
    .colored p {
        color: green;
    }
    article > .colored {
        color: red;
    }
    div.makeMeBlue p {
      color: blue;
    }
    ```
    ```html
    <div>
      <div>
        <div class="makeMeBlue">
          <p> Show in blue</p>
        </div>
      </div>
      <section class="makeMeBlue">
        <p> Unaffect </p>
      </section>
    </div>    
    ```

### 2.15 Pseudo-Class Selectors

- Pseudo-class selectors address targeting only the structures that can be targeted by simple combinations of regular selectors, or targeting the ability to style based on user interaction with the page. 
    - For example, we would want the styling of an element to change if the user hovers or moves their mouse over that element
-  The way you specify pseudo-class selector, is by specifying some selector, with a colon, and a predefined pseudo-class
    ```css
    selector:pseudo-class {
        ...
    }
    ```
- Many pseudo-class selectors exist
    - :link     // unvisited 
    - :visited  // visited 
    - :hover    // mouse curor over it
    - :active   // clicked, but not release yet
    - :nth-child(...)
    - ...

- example: remove the prefix dot from an unorderd list 
    ```css
    li {
        list-style: none;
    }
    ```
- example: links has status, after be clicking, another style will be applied to the visited link
    - to make no difference between those 2 status, and create a menu style
    ```css
    a:link, a:visited {
        text-decoration: none;
        background-color: green;
        border: 1px solid blue;
        display: block ;  // now the bg will fill whole line
        width: 200px ; // fix the menu item width
        text-align: center;
        margin-bottom: 1px;
    }
    ```
- change line style when mouse cursor is on it ,or click on it but not yet releasing.
    ```css
    a:hover, a:active {
        background-color: red;
        color: purple;
    }
    ```
- In a simple form, the nth child pseudo-selector allows you to target a particular element within a list. 
    - change the font-size of 3rd list item to 24px ( start from 1 )
    ```css
    ul li:nth-child(3) {
        font-size: 24px;
    }
    ```
- The nth child pseudo-selector can do much more.
    - ex: change the bg color of all odd line div element
    ```css
    section div:nth-child(odd) {
        background-color: gray;
    }
    ```
    ```html
    <section>
      <div>DIV 1</div>
      <div>DIV 2</div>
      <div>DIV 3</div>
      ...
    </section>
    ```
    - ex: change bg color of 2nd div element when mouse over it
    ```css
    section div:nth-child(2):hover {
        background-color: green;
    }
    ```
- Pseudo-class selectors are very powerful.
    - **Make sure your select is still readable**.
    - Simple/Readable > Complicated/Tricky.


### 2.16 Style Placement

- Where to place ?
    1. style tag inside the head tag
        - only works for this page, can not be reused for other pages
    2. specify a CSS style directly on the element by providing the style attribute.
        - `<p style="text-align: center;">I am centered!</p>`
        - The only thing that's missing from these styles is the target, and it's for a good reason, since we're inside the element, so we don't really need a target any more. 
        - least reusable
    3. external style sheets
        ```css
        <link rel="stylesheet" href="style.css">
        ```
        - a tag called *link*, `rel` tells the browser that it's a style sheet
        - and its location using the `href` attribute.


### 2.17




