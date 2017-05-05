

# Python uWSGI

# Install 

```
pip install uwsgi
```

# Simple WSGI Application

```
vi wsgi.py
```

```python
def application(environ, start_response):                     
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h1 style='color:blue'>Hello There!</h1>"]
```

 - The above code constitutes a complete WSGI application
    - By default, uWSGI will look for a callable called application, which is why we called our function application
    - it takes two parameters.
        - environ 
            - it will be an environmental variable-like key-value dictionary. 
        - start_response
            - refer to the web server (uWSGI) callable that is sent in
    - Our application must take this information and do two things
        1. must call the callable it received with an HTTP status code and any headers it wants to send back. 
            -  In this case, we are sending a "200 OK" response and setting the Content-Type header to text/html.
        2. it needs to return with an iterable to use as the response body. 
            - Here, we've just used a list containing a single string of HTML. 
            - Strings are iterable as well, but inside of a list, uWSGI will be able to process the entire string with one iteration.
 - In a real world scenario, this file would likely be used as a link to the rest of your application code.
    - For instance, Django projects include a wsgi.py file by default that translates requests from the web server (uWSGI) to the application (Django). 

in the folder of wsgi.py, run 

```
uwsgi --socket 0.0.0.0:8080 --protocol=http -w wsgi
```

visit  `localhost:8080`

ok, now you can stop your uwsgi server .


# Configure a uWSGI Config File

In the above example, we manually started the uWSGI server and passed it some parameters on the command line. 

We can avoid this by creating a configuration file. 

The uWSGI server can read configurations in a variety of formats, but we will use the .ini format for simplicity.

```
vi myapp.ini
```

```
[uwsgi]
module = wsgi:application

master = true
processes = 5

socket = myapp.sock
chmod-socket = 664
vacuum = true

die-on-term = true
```

 - 1 The uWSGI server needs to know where the application's callable is. We can give the file and the function within:
    - `wsgi:application`
 - 2 We want to mark the initial uwsgi process as a master and then spawn a number of worker processes. We will start with five workers:
    - `master = true  processes = 5`
 - We are actually going to change the protocol that uWSGI uses to speak with the outside world. 
    - When we were testing our application, we specified `--protocol=http` so that we could see it from a web browser. 
    - Since we will be configuring Nginx as a reverse proxy in front of uWSGI, we can change this. 
        - Nginx implements a uwsgi proxying mechanism, can use to talk with other servers. 
        - The uwsgi protocol is actually uWSGI's default protocol, so simply by omitting a protocol specification, it will fall back to uwsgi.
 - 3 Since we are designing this config for use with Nginx, we're also going to change from using a network port and use a Unix socket instead. 
    - The socket will be created in the current directory if we use a relative path. We'll call it myapp.sock
    - We will change the permissions to "664" so that Nginx can write to it (we will be starting uWSGI with the www-data group that Nginx uses. ) 
    - We'll also add the vacuum option, which will remove the socket when the process stops
 - We need one final option since we will be creating an Upstart file to start our application at boot. 
    - Upstart and uWSGI have different ideas about what the SIGTERM signal should do to an application
    - 4 die-on-term so that uWSGI will kill the process instead of reloading it


# Create an Upstart File to Manage the App

We can launch a uWSGI instance at boot so that our application is always available. 

We will place this in the /etc/init directory that Upstart checks. We'll be calling this myapp.conf

```
sudo vi /etc/init/myapp.conf
```

```
description "uWSGI instance to serve myapp"

start on runlevel [2345]
stop on runlevel [!2345]

setuid qibinyi
setgid www-data

script
    cd /home/demo/myapp
    . myappenv/bin/activate
    uwsgi --ini myapp.ini
end script
```

 - 1 First, we can start out with a description of the service and pick out the system runlevels where it should automatically run. 
    - The standard user runlevels are 2 through 5. 
    - We will tell Upstart to stop the service when it's on any runlevel outside of this group (such as when the system is rebooting or in single user mode):
 - 2 Next, will tell Upstart about which user and group to run the process as.
    - We want to run the application under our own account (we're using qibinyi in this guide, but you should substitute your own user).
    - We want to set the group to the www-data user that Nginx uses however.
 - Next, we'll run the actual commands to start uWSGI. Since we installed uWSGI into a virtual environment, we have some extra work to do. 
    - we'll use a script block. Inside, we'll change to our application directory, activate the virtual environment (we must use . in scripts instead of source), and start the uWSGI instance pointing at our .ini file


With that, our Upstart script is complete. Now, we can start the service by typing:


```
sudo start myapp
```

# Configure Nginx to Proxy to uWSGI

https://www.digitalocean.com/community/tutorials/how-to-set-up-uwsgi-and-nginx-to-serve-python-apps-on-ubuntu-14-04

http://developer.51cto.com/art/201010/229615_all.htm

http://www.bjhee.com/nginx-uwsgi.html

TODO







