
# C++ 2 WASM


## 1 Setting Up Your Toolchain

https://emscripten.org/


```bash
brew install emscripten

emcc -v
```


## 2 Hello World

```bash
$ emcc hello.cpp
$ ls
a.out.js   a.out.wasm hello.cpp
```

```bash
node a.out.js
Hello, World!
```

**Generating HTML**

```bash
$ emcc hello.cpp -o hello.html
$ ls
hello.cpp  hello.html hello.js   hello.wasm

# run
emrun hello.html
```


## 3 Interacting with the Browser

- WebAssembly cannot natively interact with the web browser
    - it doesn't understand the DOM or the browser
- WASM can call Javascript Functions.
- JavaScript functions can do whatever they want like interact with DOM, setup callbacks, and so on


- How
    1. in .cpp, you can use `EM_JS` macro to define javascript function
        - pic_1
    2. in .cpp, call this defined JS function
        - pic_2


## 4 Interacting with System Libraries

- Most native executable link against a standard library (libc, libc++, etc..) 
    - this libraries provide you access to functions to interact hardward, file system, or operating systems.
    - but we can not use those in the web browser.
- Emscripten provides an implementation of libc and libc++ to replace sytem libraries
- Provides a POSIX-like API that users can depend on
- Some parts of the implementation are done in WebAssembly, others in JavaScript.
    - e.g. https://github.com/emscripten-core/emscripten/blob/main/system/lib/libcxx/src/future.cpp


## 5 SDL

- Simple DirectMedia Layer
    - A library provides hardware interactions in a program
    - keyboard, mouse, graphics, audio, networking
- Emscripten will build with SDL 1 automatically
    - if you want to use SDL2, there exists an SDL emscripten-port for SDL2 that you can pass a command-line option to include that.
        - SDL2 is pretty easy to use
    - Additional ports exist for SDL_Mixer, SDL_Image, SDL_Net, and SDL_TTF






