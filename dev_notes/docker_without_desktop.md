
# Run Docker Without Docker-Desktop

1. `brew install docker-credential-helper docker`
2. edit `~/.docker/config.json`
    ```json
    {
        "auths": {},
        "credsStore": "osxkeychain",
        "currentContext": "colima"
    }
    ```
3. `brew install colima`
4. `colima start --network-address --mount /Volumes/WORK:w`
    - this is very important
    - mechanism for OSX , it asks for an admin pwd to be able to work.
    - and you must make some Volumn writable which you want to mount 

After the initial run above, you can use `colima start` or use `colima start -e` to edit the configuration file. Run `colima status` at any time to check Colima’s status.

https://ddev.readthedocs.io/en/latest/users/install/docker-installation/#macos

to start Colima automatically on reboot

```bash
brew services start colima
```

By default, Colima only mounts your home directory, so it’s easiest to use it in a subdirectory there. See the `~/.colima/default/colima.yaml`.


sometimes you need restart colima for some problem-defect ... 
