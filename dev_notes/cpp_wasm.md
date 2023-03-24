[](...menustart)

- [C++ 2 WASM](#04b687d530d939da6556492edd2ce09a)
    - [1 Setting Up Your Toolchain](#3a157ad067712e34eed57ea16b861092)
    - [2 Hello World](#576bf482f0e7634add05ce80a0dc6f3a)
    - [3 Interacting with the Browser](#fbcd61b551dae978f714283936e343cf)
    - [4 Interacting with System Libraries](#d507c7afc9368f32c80bb989442db9ad)
    - [5 SDL](#a5f53dae0134725a778b2f73fd65e94e)

[](...menuend)


<h2 id="04b687d530d939da6556492edd2ce09a"></h2>

# C++ 2 WASM


<h2 id="3a157ad067712e34eed57ea16b861092"></h2>

## 1 Setting Up Your Toolchain

https://emscripten.org/


```bash
brew install emscripten

emcc -v
```


<h2 id="576bf482f0e7634add05ce80a0dc6f3a"></h2>

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


<h2 id="fbcd61b551dae978f714283936e343cf"></h2>

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


<h2 id="d507c7afc9368f32c80bb989442db9ad"></h2>

## 4 Interacting with System Libraries

- Most native executable link against a standard library (libc, libc++, etc..) 
    - this libraries provide you access to functions to interact hardward, file system, or operating systems.
    - but we can not use those in the web browser.
- Emscripten provides an implementation of libc and libc++ to replace sytem libraries
- Provides a POSIX-like API that users can depend on
- Some parts of the implementation are done in WebAssembly, others in JavaScript.
    - e.g. https://github.com/emscripten-core/emscripten/blob/main/system/lib/libcxx/src/future.cpp


<h2 id="a5f53dae0134725a778b2f73fd65e94e"></h2>

## 5 SDL

- Simple DirectMedia Layer
    - A library provides hardware interactions in a program
    - keyboard, mouse, graphics, audio, networking
- Emscripten will build with SDL 1 automatically
    - if you want to use SDL2, there exists an SDL emscripten-port for SDL2 that you can pass a command-line option to include that.
        - SDL2 is pretty easy to use
    - Additional ports exist for SDL_Mixer, SDL_Image, SDL_Net, and SDL_TTF






