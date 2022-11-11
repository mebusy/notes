[](...menustart)

- [XPath](#b6454d498635710a189184ea13beed1c)
- [List of XPaths](#81f2b3a9d3694a74b785c9d556f5b180)

[](...menuend)


<h2 id="b6454d498635710a189184ea13beed1c"></h2>

# XPath

http://zvon.org/comp/r/tut-XPath_1.html

<h2 id="81f2b3a9d3694a74b785c9d556f5b180"></h2>

# List of XPaths

- Start with / 
    - filesystem addressing
    - /AAA  : mean AAA in root path
- Start with //
    - `//BBB` : file or folder named BBB in any path
    - `//DDD/BBB` : all elements BBB which are children of DDD 
- All elements: \*
    - all elements located by preceeding path
    - `/AAA/CCC/DDD/*` # all elements under /AAA/CCC/DDD
    - `/*/*/*/BBB`   # all BBBs have 3 ancestor
    - `//*`   # Select all elements
- Further conditions inside []
    - `/AAA/BBB[1]`     # choose first BBB under /AAA
    - `/AAA/BBB[last()]`  # choose last BBB under /AAA
- Attributes @
    - `//@id`  
        - all with attributes id  :  `/AAA/CCC id="b1"/>`
    - `//BBB[@id]`
        - BBB have attributes id :  `/AAA/<BBB id="b1"/>`
    - `//BBB[@name]`
        - BBB have attributes name: `/AAA/<BBB name="bbb"/>`
    - `//BBB[@*]`
        - BBB have any attribute
    - `//BBB[not(@*)]`
        - BBB without an attribute
    - to compare with mulitple attributes ,use `and`
        - `//BBB[@id and @id2]`  , or 
        - `//BBB[@id][@id2]`
- Attribute values
    - `//BBB[@id='b1']`
        - BBB elements which have attribute id with value b1 :  `/AAA/<BBB id = "b1"/> `
    - `//BBB[@name='bbb']`
    - `//BBB[normalize-space(@name)='bbb']`
        - BBB elements which have attribute name with value bbb ,leading and trailing spaces are removed before comparison
        - `/AAA/<BBB name = " bbb "/>`
        - `/AAA/<BBB name = "bbb"/>`
- Nodes counting  
    - Function count() counts the number of selected elements
    - `//*[count(BBB)=2]` : elements which have two children BBB
    - `//*[count(*)=2]` : elements which have 2 children
    - `//*[count(*)=3]`  : elements which have 3 children
- Playing with names of selected elements
    - Function name() returns name of the element
    - starts-with function returns true if the first argument string starts with the second argument string
    - contains function returns true if the first argument string contains the second argument string
    - `//*[name()='BBB']`  :  all elements with name BBB, equivalent with //BBB
    - `//*[starts-with(name(),'B')]`  :  all elements name of which starts with letter B
    - `//*[contains(name(),'C')]`  : all elements name of which contain letter C
- Length of string
    - The string-length function returns the number of characters in the string
    - You must use `&lt;` as a substitute for `<` and `&gt;` as a substitute for `>` .
    - `//*[string-length(name()) = 3]`   : elements with three-letter name
    - `//*[string-length(name()) < 3]`
    - `//*[string-length(name()) > 3]`
- Combining XPaths with `|`
    - `//CCC | //BBB`
    - `/AAA/EEE | //BBB`
    - `/AAA/EEE | //DDD/CCC | /AAA | //BBB`
- Descendant axis
    - The descendant axis contains the descendants of the context node
    - a descendant is a child or a child of a child and so on
    - thus the descendant axis never contains attribute or namespace nodes
    - `/descendant::*`  : all descendants of document root and therefore all elements
    - `/AAA/BBB/descendant::*`   : all descendants of /AAA/BBB
    - `//CCC/descendant::*`      : all elements which have ancestor CCC along the path from root
    - `//CCC/descendant::DDD`    : all DDD which have ancestor CCC   along the path from root 
- Parent axis
    - The parent axis contains the parent of the context node, if there is one.
    - `//DDD/parent::*`   : all parents of DDD
        - `BBB/DDD`
- Ancestor axis
    - The ancestor axis contains the ancestors of the context node
    - the ancestors of the context node consist of the parent of context node and the parent's parent and so on; 
    - thus, the ancestor axis will always include the root node, unless the context node is the root node
    - `/AAA/BBB/DDD/CCC/EEE/ancestor::*`  : AAA BBB DDD CCC
    - `//FFF/ancestor::*`   : Select ancestors of FFF element
- Following-sibling axis
    - contains all the following siblings of the context node.
    - `/AAA/BBB/following-sibling::*`    : `/AAA/XXX` , `/AAA/CCC`
    - `//CCC/following-sibling::*`   
- Preceding-sibling axis
    - contains all the preceding siblings of the context node
    - `/AAA/XXX/preceding-sibling::*`
    - `//CCC/preceding-sibling::*`
- Following axis
    - contains all nodes in the same document as the context node that are after the context node in document order
    - excluding any descendants and excluding attribute nodes and namespace nodes.
    - search in entire docutment
    - `/AAA/XXX/following::*`
    - `//ZZZ/following::*`
- Preceding axis
    - contains all nodes in the same document as the context node that are before the context node in document order
    - excluding any ancestors and excluding attribute nodes and namespace nodes
    - `/AAA/XXX/preceding::*`
    - `//GGG/preceding::*`
- Descendant-or-self axis 
    - `/AAA/XXX/descendant-or-self::*`
    - `//CCC/descendant-or-self::*`
- Ancestor-or-self axis
    - `/AAA/XXX/DDD/EEE/ancestor-or-self::*`
    - `//GGG/ancestor-or-self::*`
- Orthogonal axes
    - The ancestor, descendant, following, preceding and self axes partition a document (ignoring attribute and namespace nodes): 
    - they do not overlap and together they contain all the nodes in the document.
    - `//GGG/ancestor::* | //GGG/descendant::* | //GGG/following::* | //GGG/preceding::* | //GGG/self::*`
- Numeric operations
    - div, mod , floor, ceiling ,
    - `//BBB[position() mod 2 = 0 ]`
    - `//BBB[ position() = floor(last() div 2 + 0.5) or position() = ceiling(last() div 2 + 0.5) ]`
    - `//CCC[ position() = floor(last() div 2 + 0.5) or position() = ceiling(last() div 2 + 0.5) ]`
    - position() start with 1

