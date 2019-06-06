
# Module 6: Operating System

## 6.1 Operating System 

### Typical OS Services 

 - Language extensions / standard library
    - mathematical operations (abs,sqrt,...)
    - abstract data types (String, Array, ...)
    - input function  (readChar, readLine, ...)
    - textual output (printChar, printString, ...)
    - graphics output (drawLine, drawCircle, ...)
 - System oriented services 
    - memory management (objects, arrays, ...)
    - file system
    - I/O device drivers
    - UI management (shell, windows)
    - multi-tasking 
    - Networking 
    - security 

### The Jack OS

 1. Math
 2. Memory
 3. Screen
 4. Output
 5. Keyboard
 6. String
 7. Array
 8. Sys




## 6.3 Mathematical Operations

### multiplcation 

- naive implement
    - repeative additon  , O(N)
- optimized solutino
    - binary shift , and then sum up , O(w)


 - Issues:
    - how to handle negative numbers ?
        - it works fine
    - how to handle overflow ?
        - this algorithm always return the correct answer modulu 2ʷ
    - how to implement i'th bit of y quickly ?
        - Jack doesn't have bit test function 
        - Instead, we can use an array that holds the 16 values 2ⁱ, i=0,...,15
            - a fixed array, say , twoToThe[i]
            - implement the bit test function



### Division

```
// return the integer part of x/y
// where x >=0 , and y >0
def divide(x,y):
    if y > x :
        return 0
    q = divide(x, 2*y)
    if x - 2*y*q < y :
        return 2*q
    else:
        return 2*q + 1
```

 - O(logN)
 - Issues:
    - handling negative numbers
        - divide |x| / |y|
        - then set the result's sign
    - handling overflow (of y)
        - solution: the overflow can be detected when y becomes negative 
        - we can change the functions first statement to:
            - `if (y>x or y<0) return 0`
 
### Square root

 - The square root function √x has 2 appealing properties:
    - its inverse function x² can be easily computed
    - it is a monotonically increasing function
 - Therefore:
    - squre roots can be computed using *binary search*
 - Issus:
    - the calculation of   `(y+2ʲ)²` can overflwo
    - solution: change the condition  `(y+2ʲ)²<=x`  to `(y+2ʲ)² <=x and (y+2ʲ)² >0`


## 6.4 Memory Access

 - class Memory 
    - int peek(int addr)
    - void poke(int addr, int value)
    - Array alloc(int size)
    - void deAlloc(Array o)

 - The challenge 
    - THe OS is written in Jack: how can we access the RAM ?
    -
    ```
    class Memory {
        static array ram;
        ...
        function void init() {
            let ram = 0 ;  // Jack is weak typed
        }
    }
    ```

## 6.5 Heap Management 

 - The need
    - During run-time , programs typically create objects and arrays
    - Objects and arrays are implemented using 
        - reference variables
        - pointing at actual data blocks (in the heap)
 - The challenge
    - Allocating memory for new objects / arrays 
    - Recycling memory of disposed objects / arrays 

### Object construction and destruction 

 - The challenge 
    - Implementing *alloc* and *dealloc*
 - The solution 
    - Heap management 

### Heap management (simple)

```
init:
    free = heapBase
    
alloc(size):
    block = free
    free = free + size
    return block

deAlloc(object):
    do nothing (simple, never recycle)
```

### Heap management 

 - Use a **linked list** to keep track of available heap segments , which are presently available to us
    - ![](../imgs/n2t_heap_manage_linkedlist.png)
 - alloc(size):
    - find a block of size *size* in one of the segments ,remove it from the segment , and give it the client 
 - deAlloc(object):
    - append the object/block to the freeList ( i.e. simply append it to the end of the freeList.  )


### Heap management (detailed)

 - alloc(size):
    - for an example,  *size* = 3
    - Terminology: if segment size >= *size* + 2 , we say that the segment is *possible*
        - The *2*  is for the overhead fields which are absolutely necessary. 
    - search the freeList for:
        - the first possible segment (first fit) , or 
        - the smallest possible segment (best fit) 
    - ![](../imgs/n2t_heap_manage_freelist_search.png)
    - if no such segment is found, return failure (or attempt defragmentataion)
    - carve a block of size ( *size* + 2 ) from this segment 
        - update the freeList and the fields of *block* to account for the allocation
    - return the base address of the block's data part 
    - ![](../imgs/n2t_heap_manage_alloc.png)
 - deAlloc (object):
    - append *object* to the end of the freeList. 
    - ![](../imgs/n2t_heap_manage_dealloc.png)
    - problem:  The more we recycle (deAlloc), the more the freeList becomes fragmented.
    - defrag: every once defrag kicks in, it go through the entire freeList, and tries to merge as more small segments into continuous segments in the memory.
        - not required for this course project.


### Implementation notes

 - Implementing the heap / freeList (on Hack platform)

```
class Memory {
    ...
    static Array heap;
    ...

    // In Memory.init 
    ...
    let heap = 2048; // heapBase

    let freeList = 2048;
    let heap[0] = 0 // next, 0 means its tail of freelist
    let heap[1] = 14335; // length
    ...
}
```

 - The *freeList* can be realized using the *heap* array
 - The *next* and *size* properties of the memory segment beginning in address *adrr* can be realized by `heap[addr-2]` and `heap[addr-1]`.
 - alloc, deAlloc, and deFrag can be realized as operations on the *heap* array.


## 6.6 Graphics


### Draw Pixel

 - recap
    - 8k screen memory map 
    - target screen:   512 pixel * 256 pixel 
    - Jack word:  16 bits

```
function void drawPixel(int x, int y) {
    address = 32*y + x/16 
    value = Memory.peek[ 16384 + address ]
    set (x%16)th bit of value to 1
    do Memory.poke(address, value)
}
```


### Line Drawing

 - Basic idea: image drawing is implemented through a sequence of *drawLine* operations
 - Challenge: draw lines *fast*
 - Naive idea: 

```
// just for an example
// assuming x2 > x1, y2 > y1
drawLine(x1,y1, x2,y2)
let:
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1

a = 0 ; b = 0 ;
while ( (a<=dx) and (b<=dy) )
    drawPixel( x + a, y + b )
    // decide if to go right , or up
    // to avoid going diagonally
    if ( b/a > dy / dx ) , a = a + 1 
    else           , b = b + 1 

```

 - opitmize:
    - ![](../imgs/n2t_os_line_drawing.png)
    - `( b/a > dy / dx )` has the same value as `( a*dy < b*dx )`
    - `let diff = a*dy - b*dx`
        - when a = a + 1 , *diff* goes up by **dy**
        - when b = b + 1 , *diff* goes down by **dx**
    - solution:
        - 
        ```
        if (diff < 0 ) 
            a = a + 1
            diff = diff + dy 
        else
            b = b + 1
            diff = diff - dx 
        ```
    - now , it involves only addition and subtraction operations 
        - and can be implemented either in software or hardware.

 - Issue :
    - modify this algorithm for a screen origin (0,0)  at the screen's top-left corner
    - generalize the algorithm to draw lines that go in any direction
    - drawing horizontal and vertical lines should probably be handled as special cases. 


### Circle drawing 

![](../imgs/n2t_os_cirlcle_draw_0.png)

![](../imgs/n2t_os_circle_draw1.png)

```
drawCircle(x,y,r):
    for each dy = -r tp r do:
        drawLine( x - √(r²-dy²) , y+dy ,  x + √(r²-dy²) , y+dy  ) 
```


 - for *drawCircleOutline* , do twice *drawPixel*  instead of *drawCircle*
 - Issue :
    - can potentially lead to overflow
    - to handle , limit r to no greater that 181

## 6.8: Handling Textual Output

 - Textual output:
    - Screen : 23 rows of 64 characters , b&w
    - Managed by the Jack OS class *Output*
 - Hack Font
    - Each character occupies a fixed 11x8 pixel fream
    - The frame include 2 empty right columns and 1 empty buttom row for character spacing

### Font implementation

```
class Output {
    static Array charMaps; // character map for displaying characters

    function void init() {
        do initMap(); 
    }
    ...
    // Initializes the caracter map array
    function void intiMap() {
        let charMaps = Array.new(127);

        // Assigns the bitma for each character in the character set
        do Output.create(97, 0,0,0,14,24, 30,27,27,54,0, 0); // a 
        do Output.create(98, 3,3,3,15,27, 51,51,51,30,0, 0); // b
        ...

        // black square , used for non printable characters
        do Output.create(0, 63,63,63,63,63, 63,63,63,63,63,0, 0)
        return
    }
    
    // create a character map array of the given char index with the given values 
    function void create( int index, int a, int b, int c, int d, int e,
                                     int f, int g, int h, int i, int j, int k) {
        var Array map;
        let map = Array.new(11)
        let charMaps[index] = map;
        let map[0] = a; let map[1] = b; let map[2] = c;
        let map[3] = d; let map[4] = e; let map[5] = f;
        let map[6] = g; let map[7] = h; let map[8] = i;
        let map[9] = j; let map[10] = k;
        return 
    }
}
```


### Cursor 

 - Indicates where the next character will be written
 - Logical / physical implications
 - But Jack platform does not show a cursor at all

 - Manage cursor
    - if asked to display *newline* : move the cursor to the beginning of the next line
    - if asked to display *backspace* : move the cursor one column left
    - if asked to display any other character:  dislay the character , and move the cursor one columen to the right .

---

## 6.9 Input

 - recap
    - 1 word kb map ,  24576 (0x6000)

 - keyPressed
    - use `Memory.peak` to access the keyboard's memory map
 - readChar
    - 
    ```
    readChar():
        display the cursor
        // waits until a key is pressed
        while (keyPressed() ==0) :
            do nothing 
        c = code of the currently pressed key 
        while (keyPressed() !=0 ):
            do nothing
        display c at the current cursor location 
        advance the cursor 
    ```

 - readLine
    - 
    ```
    readLine():
        str = empty string 
        repeat 
            c = readChar()
            if c == newLine :
                display newLine
                return str 
            else if c == backspace:
                remove the last character from str
                do Output.backspace()
            else:
                str = str.append( c )
    ```

## 6.10 String Processing 

 - int2string
    - 
    ```
    ini2String(val):
        lastDigit = val % 10
        c = character representing lastDigit
        if val < 0 
            return c (as a string)
        else
            return int2String(val/10).append(c)
    ```
 - string2int
    - 
    ```
    string2Int(str):
        val = 0
        for i = 0...str.length do 
            d = integer value of str[i]
            val = val * 10 + d 
        return val
    ```


### Implementation notes

```
class String {
    field Array str;
    field int length ;

    constructor String new (int maxLength) {
        let str = Array.new( maxLength ) ;
        let length = 0
        return this 
    }
    ...
}
```

---


