[](...menustart)

- [git-secret crash](#2e4987eb00acb019d112359ef4ea14fa)
    - [Install](#349838fb1d851d3e2014b9fe39203275)
    - [0. create a gpg RSA key-pair](#d1d805fbec2198f87dd365a9cd4f6b95)
    - [1. Basic](#7d5cbb16e6b7b4abd4e6cb6346e08140)
    - [2. cooperate with others](#185b0dc72df04605f60858af960736c9)

[](...menuend)


<h2 id="2e4987eb00acb019d112359ef4ea14fa"></h2>

# git-secret crash

https://git-secret.io/

<h2 id="349838fb1d851d3e2014b9fe39203275"></h2>

## Install

```bash
brew install git-secret
```

<h2 id="d1d805fbec2198f87dd365a9cd4f6b95"></h2>

## 0. create a gpg RSA key-pair

```bash
gpg --gen-key
```

<h2 id="7d5cbb16e6b7b4abd4e6cb6346e08140"></h2>

## 1. Basic

init

```bash
$ git secret init
git-secret: init created: '/test-secret/.gitsecret/'

./.gitsecret
./.gitsecret/paths
./.gitsecret/paths/mapping.cfg
./.gitsecret/keys
```

add yourself

```bash
$ git secret tell <gpg email>

./.gitsecret/keys/S.gpg-agent.extra
./.gitsecret/keys/S.gpg-agent.ssh
./.gitsecret/keys/private-keys-v1.d
./.gitsecret/keys/S.gpg-agent
./.gitsecret/keys/pubring.kbx~
./.gitsecret/keys/pubring.kbx
./.gitsecret/keys/S.scdaemon
./.gitsecret/keys/trustdb.gpg
./.gitsecret/keys/S.gpg-agent.browser
```

encrypt file

```bash
$ echo "content" > hideme.txt

$ git secret add hideme.txt
git-secret: file not in .gitignore, adding: hideme.txt
git-secret: 1 item(s) added.

$ cat .gitsecret/paths/mapping.cfg
hideme.txt

$ git secret hide
git-secret: done. 1 of 1 files are hidden.

$ ls
hideme.txt        hideme.txt.secret

$ cat hideme.txt.secret
'?^?(?5K|@t?r???*?*?E???N???N?Ku?4?B??o?Y0?ڕ??)??⸜?;\b?U?k??1?Ċ?6??M??z/(?#?i????W'

$ rm hideme.txt
```

decrypt file


```bash
$ git secret reveal
git-secret: done. 1 of 1 files are revealed.

$ ls
hideme.txt        hideme.txt.secret
```


<h2 id="185b0dc72df04605f60858af960736c9"></h2>

## 2. cooperate with others

to add other users so they can decrypt and work with the files in your repository,

1. first you must import there gpg public key.
    ```bash
    $ gpg --import other_gpy_public_key.txt
    ```
2. then add them to the secrets repo
    ```bash
    $ git secret tell <their email of imported gpg key>
    ```

To export your public key, run:

```bash
$ gpg --armor --export your.email@address.com > public-key.gpg
```





