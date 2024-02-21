
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
4. `colima start --mount /Volumes/WORK:w`
    - this is very important, you must make some Volumn writable which you want to mount 


