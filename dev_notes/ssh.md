
# SSH

## SSH login through multiple jump servers

```bash
$ ssh -J user1@jump1:port1[,user2@jump2:port2],... user@target-server [-p port]
```

## SSH proxy tunnel

TODO


## Configure SSH Key-Based Authentication on a Linux Server

1. creating SSH Keys on you local machine
    - we can use ssh-keygen to generate a key pair, by default, this will create a 3072 bit RSA key pair.
        ```bash
        $ ssh-keygen
        Generating public/private rsa key pair.
        Enter file in which to save the key (/Users/mebusy/.ssh/id_rsa): 
        ```
    - It is best to stick with the default location at this stage. 
        - Doing so will allow your SSH client to automatically find your SSH keys when attempting to authenticate.
        ```bash
        $ ls ~/.ssh
        config          id_rsa          id_rsa.pub      known_hosts     known_hosts.old
        ```
2. Copying an SSH Public Key to Your Server
    - method1
        ```bash
        cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
        ```
    - method2
        - manually copy content of your public key, and append it to server's `~/.ssh/authorized_keys`


Now you should be able to log into the remote host without the remote account’s password.



