# tmux

## Layer 1: session

### detach & attach a session

```bash

Ctl+B D  # Detach from session

```bash
[detached (from session 0)]
```

ssh from any other computer, resume that session

```bash
$ tmux a[ttach]
```


### start a named session

```bash
$ tmux new -s bob
```

when detaching it

```bash
[detached (from session bob)]
```


### list sessions

```bash
$ tmux ls
0: 1 windows (created Fri Oct 25 19:09:12 2024)
bob: 1 windows (created Fri Oct 25 19:22:36 2024)
```

### attach to a named session

```bash
$ tmux a -t 0
```

### delete a session

```bash
$ tmux kill-session -t bob
$ tmux ls
bob: 1 windows (created Fri Oct 25 19:22:36 2024)
```

### delete all sessions

```bash
$ tmux kill-server
```



## =========== Layer 2: window ===========

### create a new window

- Ctl + B  c
    - notice the bottom left corner, it shows the window infos
    - `[0] 0:zsh- 1:zsh* `

### move between windows

- Ctl + B  n
    - `[0] 0:zsh* 1:zsh-` 

### list all windows and move around

- Ctl + B  w

### delete a window

- Ctl + B  &
    - then type `y` to confirm


## =========== Layer 3: Panel ===========

### split window

- Split window horizontally
    - Ctl + B  %
- Split window vertically
    - Ctl + B  "


### move between panels

- Ctl + B  arrow

### show panel number

- Ctl + B  q

to move to specific panel with panel number, e.g. panel 2

- Ctl + B  q  2

### delete a panel

- Ctl + B  x
    - then type `y` to confirm




