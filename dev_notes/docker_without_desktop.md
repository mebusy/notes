
# [MacOS] Run Docker Without Docker-Desktop

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
4. `colima start --network-address --vm-type=vz --mount-type=virtiofs  --disk 128  --mount /Volumes/WORK:w`
    - `--mount /Volumes/WORK:w` this is very important, you must make some Volumn writable which you want to mount 
    - `--network-address` mechanism for OSX , it asks for an admin pwd to be able to work.
    - `colima start --network-address --vm-type=vz --mount-type=virtiofs`  virtiofs is limited to macOS and vmType `vz`. It is the fastest of the options.

After the initial run above, you can use `colima start` or use `colima start -e` to edit the configuration file. Run `colima status` at any time to check Colima’s status.

https://ddev.readthedocs.io/en/latest/users/install/docker-installation/#macos

to start Colima automatically on reboot

```bash
brew services start colima
```

By default, Colima only mounts your home directory, so it’s easiest to use it in a subdirectory there. See the `~/.colima/default/colima.yaml`.


