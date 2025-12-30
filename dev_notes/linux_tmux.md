[](...menustart)

- [tmux](#96714c9d36de9b638d9efd4e60f38bfe)
    - [Layer 1: session](#17a9d9a1e9cb47f6b81b0d10325cad7a)
        - [detach & attach a session](#ec4d527642385d3a8558e82713288179)
        - [start a named session](#e2e8ccc1eb66e4d47797d61cfd1295f7)
        - [list sessions](#d20287ac07e632d030b1182e36905cdf)
        - [attach to a named session](#306a34ae6065dbc4f8e193c44b7afd76)
        - [delete a session](#2574ae0262959dde6ab6216e8ed27ce4)
        - [delete all sessions](#b6e696a8e44ab5efecfe2622d4554b5d)
    - [=========== Layer 2: window ===========](#474fa89f2aea1b02e8baf9e5d4f27dca)
        - [create a new window](#f9f6431495e9c094ca785c97168039ab)
        - [move between windows](#c035e69a865b873cc7cbeb6e26629d72)
        - [list all windows and move around](#a61dcda050adc2783a4e03d5e19531b0)
        - [delete a window](#19f28441c605b9f9dd0ce430185ef494)
    - [=========== Layer 3: Panel ===========](#b081d60fa4826f0eb57fd766c83c07cf)
        - [split window](#821adc4050df9d11c6b042d441aed621)
        - [move between panels](#5ae57863ca99d6a3bc9e5d7b8a1f5b44)
        - [show panel number](#5522cf8642d141657c4919711c645e58)
        - [delete a panel](#7bd4c19590c81309063e3bd25573500e)

[](...menuend)


<h2 id="96714c9d36de9b638d9efd4e60f38bfe"></h2>

# tmux

<h2 id="17a9d9a1e9cb47f6b81b0d10325cad7a"></h2>

## Layer 1: session

<h2 id="ec4d527642385d3a8558e82713288179"></h2>

### detach & attach a session

```bash
Ctl+B D  # Detach from session
```

```bash
[detached (from session 0)]
```

ssh from any other computer, resume that session

```bash
$ tmux a[ttach]
```


<h2 id="e2e8ccc1eb66e4d47797d61cfd1295f7"></h2>

### start a named session

```bash
$ tmux new -s bob
```

when detaching it

```bash
[detached (from session bob)]
```


<h2 id="d20287ac07e632d030b1182e36905cdf"></h2>

### list sessions

```bash
$ tmux ls
0: 1 windows (created Fri Oct 25 19:09:12 2024)
bob: 1 windows (created Fri Oct 25 19:22:36 2024)
```

<h2 id="306a34ae6065dbc4f8e193c44b7afd76"></h2>

### attach to a named session

```bash
$ tmux a -t 0
```

<h2 id="2574ae0262959dde6ab6216e8ed27ce4"></h2>

### delete a session

```bash
$ tmux kill-session -t bob
$ tmux ls
bob: 1 windows (created Fri Oct 25 19:22:36 2024)
```

<h2 id="b6e696a8e44ab5efecfe2622d4554b5d"></h2>

### delete all sessions

```bash
$ tmux kill-server
```



<h2 id="474fa89f2aea1b02e8baf9e5d4f27dca"></h2>

## =========== Layer 2: window ===========

<h2 id="f9f6431495e9c094ca785c97168039ab"></h2>

### create a new window

- Ctl + B  c
    - notice the bottom left corner, it shows the window infos
    - `[0] 0:zsh- 1:zsh* `

<h2 id="c035e69a865b873cc7cbeb6e26629d72"></h2>

### move between windows

- Ctl + B  n
    - `[0] 0:zsh* 1:zsh-` 

<h2 id="a61dcda050adc2783a4e03d5e19531b0"></h2>

### list all windows and move around

- Ctl + B  w

<h2 id="19f28441c605b9f9dd0ce430185ef494"></h2>

### delete a window

- Ctl + B  &
    - then type `y` to confirm


<h2 id="b081d60fa4826f0eb57fd766c83c07cf"></h2>

## =========== Layer 3: Panel ===========

<h2 id="821adc4050df9d11c6b042d441aed621"></h2>

### split window

- Split window horizontally
    - Ctl + B  %
- Split window vertically
    - Ctl + B  "


<h2 id="5ae57863ca99d6a3bc9e5d7b8a1f5b44"></h2>

### move between panels

- Ctl + B  arrow

<h2 id="5522cf8642d141657c4919711c645e58"></h2>

### show panel number

- Ctl + B  q

to move to specific panel with panel number, e.g. panel 2

- Ctl + B  q  2

<h2 id="7bd4c19590c81309063e3bd25573500e"></h2>

### delete a panel

- Ctl + B  x
    - then type `y` to confirm


## FAQ

### tmux 下， netty 网络请求报错，route 找不到

原因是, 原因是本机 env no_proxy 中 带了 本机的 域名, 导致 tmux session 中的 proxy / no_proxy 设置出现问题。 删掉后解决。

```bash
# tmux 环境下
tmux new-session -d "env | sort > /tmp/env-tmux.log"
# 正常 zsh 环境下
env | sort > /tmp/env-zsh.log

# diff 两者的区别，看看是否 proxy / no_proxy 有区别
diff -u /tmp/env-zsh.log /tmp/env-tmux.log
```

