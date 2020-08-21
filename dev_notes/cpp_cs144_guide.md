
We want to avoid “paired” operations (e.g. malloc/free, or
new/delete), where it might be possible for the second half of the pair not to happen.

Instead, operations happen in the constructor
to an object, and the opposite operation happens in the destructor. This style is called
“Resource acquisition is initialization,” or RAII.


In particular, we would like you to:

- Use the language documentation at https://en.cppreference.com as a resource.
- Never use malloc() or free().
- Never use new or delete.
- Essentially never use raw pointers (*), and use “smart” pointers (unique ptr or shared ptr) only when necessary. (You will not need to use these in CS144.)
    - smart point is a wrap of a raw pointer
    - make sure the object is deleted when  is not reference any more so as to avoid memory leak.
    - unique ptr means allows only one owner
    - shared ptr maintains a reference count

- Avoid templates, threads, locks, and virtual functions. (You will not need to use these in CS144.)
- Avoid C-style strings (char *str) or string functions (strlen(), strcpy()). These are pretty error-prone. Use a std::string instead.
- Never use C-style casts (e.g., (FILE *)x). Use a C++ static cast if you have to (you generally will not need this in CS144).
    - *static* means compile-time. static cast is more safe.
- Prefer passing function arguments by const reference (e.g.: const Address & address).
- Make every variable const unless it needs to be mutated.
- Make every method const unless it needs to mutate the object.
- Avoid global variables, and give every variable the smallest scope possible.
- Before handing in an assignment, please run make format to normalize the coding style.



