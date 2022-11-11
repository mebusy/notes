[](...menustart)

- [Nodejs Note](#d18aea94aa0f4438e2caa8b2f97d600e)
    - [npm scripts](#77fcf03f0aa3a848efe253c0c5a3c24b)

[](...menuend)


<h2 id="d18aea94aa0f4438e2caa8b2f97d600e"></h2>

# Nodejs Note

<h2 id="77fcf03f0aa3a848efe253c0c5a3c24b"></h2>

## npm scripts

- pm 允许在package.json文件里面，使用scripts字段定义脚本命令。
    ```json
    {
        // ...
        "scripts": {
            "build": "node build.js"
        }
    }
    ```

- 命令行下使用npm run命令，就可以执行这段脚本。
    ```bash
    $ npm run build  # 等同于执行 node build.js
    ```
- npm run 会新开一个Shell，并将当前目录的`node_modules/.bin/` 目录加入PATH 变量

