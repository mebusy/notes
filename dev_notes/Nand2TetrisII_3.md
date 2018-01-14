
# 3 Hight Level Language 

## 3.1 The Jack Language in a nutshell

 - A simple, Java-like language 
 - Object-based , no inheritance
 - Multi-purpose
 - Lends itself to interactive apps
 - Can be learned in about an hour


### Example 

 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_example_1.png)
 - ![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_example_2.png)
    - entry:  Main.main
    - flow of control:
        - if / if ... else
        - while
        - do
    - Array :
        - Array is implemented as part of the stardard class library
        - Jack arrays are not typed, they can contain any value of any type
    - OS services:
        - Keyboard.readInt
        - Output.printString
        - Output.printInt
        - More...
    - Jack data types:
        - Primitive:
            - int
            - char
            - boolean
        - Class types:
            - OS: Array, String, ...
            - Program extensions : as needed

## 3.2 Object-Based Programming

 - Jack 的基本数据类型，数值方面的，只有int ，所有有必要扩充一下数值类型，比如 rational number.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_factionAPI.png)

### OO programming: building a class

 - filed, aka property, aka member variable
 - In Jack the only way to access field values from outside the class is through *accessor* methods.

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_oop_1.png)

 - functions are equivalent to static methods in JAVA. 
 - Jack constructor must return  the base address or must return an object of the type( i.e. this)
    - Java construtors do exactly the same but they do it implicity. You don't have to say `return this`  in Java but actually , compiler will do it. 
 - Jack method must call `return`  as well

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_jack_oop_2.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/v2t_jack_dispose.png)

 - dispose method is implemented using a call to the host OS -- `Memory.deAlloc(this)`
    - which takes an address in memory and disposes the memory block 
    - the memory resouces will be freed.
 - GC
    - Jack has no garbage collection
    - Objects must be disposed explicitly
    - every jack class with `at least` one constructor must have a dispose() method.


### OO programming : object representation 

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_1.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_2.png)

![](https://raw.githubusercontent.com/mebusy/notes/master/imgs/n2t_obj_represent_3.png)














