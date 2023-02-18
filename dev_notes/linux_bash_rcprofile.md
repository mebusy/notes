
# Zsh/Bash startup files loading order (.bashrc, .zshrc etc.)

![flowchart](https://miro.medium.com/v2/resize:fit:640/0*ayRnVGxxm8l9MgFT.)

```bash
/bin/bash
       The bash executable
/etc/profile
       The systemwide initialization file, executed for login shells
~/.bash_profile
       The personal initialization file, executed for login shells
~/.bashrc
       The individual per-interactive-shell startup file
~/.bash_logout
       The individual login shell cleanup file, executed when a login shell exits
~/.inputrc
       Individual readline initialization file
```

Generally,

- For bash, put stuff in ~/.bashrc, and make ~/.bash_profile source it.
- For zsh, put stuff in ~/.zshrc, which is always executed.

------


- `~/.bash_profile` is only sourced by bash when started in login mode. 
    - That is typically when you log in at the console (`Ctrl+Alt+F1..F6`), 
    - connect via ssh, 
    - or use `sudo -i or su -` to run commands as another user.
- When you log in graphically(under X), `~/.profile` will be specifically sourced by the script that launches gnome-session (or whichever desktop environment you're using)
    - So `~/.bash_profile` is not sourced at all when you log in graphically.
    - When you open a terminal, the terminal starts bash in ( **non-login** ) interactive mode, 
        - which means it will source `~/.bashrc`.
- The right place for you to put these environment variables is in `~/.profile`, and the effect should be apparent next time you log in.
    - bash is not involved when logging in graphically, so it goes straight for `.profile` instead of `.bash_profile`


---

So what should you put where?

- A good .bash_profile loads `.profile`, and loads `.bashrc` if the shell is interactive.
    ```bash
    . ~/.profile
    if [[ $- == *i* ]]; then . ~/.bashrc; fi
    ```
- In `.profile`, put environment variable definitions, and other session settings such as ulimit.
- In `.bashrc`, put bash interactive settings such as aliases, functions, completion, key bindings (that aren't in .inputrc), …



