...menustart

 - [Locust](#ee9c4c52006ab904c02898addbd22f91)
     - [Installation](#7cd8fb6e31cc946c078d2740c76a9899)
     - [Quich start](#e1c7074e1c4d023402ee6164766e6fde)
         - [Example locustfile.py](#07a0fcb9aeae9150db1994f575768fc1)
         - [Start Locust](#5818c3f44e2dc782824809dface48782)
         - [Open up Locust’s web interface](#0b83bfe6ef2a315017a7a511a659738d)
     - [Writing a locustfile](#a68f707e65b8641b73c329764e983414)
         - [The Locust class](#17909d322ee85b757b0a2da94f5a6c65)
         - [TaskSet class](#9c07c110dc52aed577d7d571811f6d80)
             - [Declaring tasks:](#856e1ed6703f100ddb34260e858157ff)
             - [tasks attribute](#69b67acae5e44a6d396ebf8b48e0f7ba)
             - [Referencing the Locust instance, or the parent TaskSet instance](#80b785988c0e04f1f45801f4f6b70c3d)
         - [TaskSequence class](#68364ef1a4284141a6ee8f52d2b212c9)
         - [Setups, Teardowns, on_start, and on_stop](#bb8557529751c16ab2fdf9bda9d837d0)
             - [Setups and Teardowns](#09288898f790687018c0a6e33f1fe57d)
             - [The on_start and on_stop methods](#c185ebe8be7bef6661e45bf00e6e3291)
             - [Order of events](#9466aa1dc479ae1c7da40c3d273d25ae)
         - [Making HTTP requests](#9e1edb42e7f308a64ccee832eb1ab5bf)
             - [Using the HTTP client](#ea493d7b6bf94bafb89e84a3637c0a14)
             - [Safe mode](#8f515507f68651c99f27a6790119d54b)
             - [Manually controlling if a request should be considered successful or a failure](#b5431017aad3c9e5df25938d8cee350e)
             - [Grouping requests to URLs with dynamic parameters](#ef2e4c961c56e33d44553e9363e54ebb)
     - [Running Locust distributed](#3e38fcc9f82e983c75263725bd426b37)
     - [Running Locust without the web UI](#b5ef92324c2f19871c6c35b8303f2132)
         - [Setting a time limit for the test](#b7485a0fc6cd00ba97c74332b56d1b0d)
         - [Running Locust distributed without the web UI](#a6192bcf475fe53f0db6cc7f137a5924)
     - [Retrieve test statistics in CSV format](#3c26f7b316cf2486f480c9c90f5dbd9e)

...menuend


<h2 id="ee9c4c52006ab904c02898addbd22f91"></h2>

# Locust

<h2 id="7cd8fb6e31cc946c078d2740c76a9899"></h2>

## Installation

```
# for macosx
brew install libev

pip install locustio --user
```


<h2 id="e1c7074e1c4d023402ee6164766e6fde"></h2>

## Quich start

<h2 id="07a0fcb9aeae9150db1994f575768fc1"></h2>

### Example locustfile.py

```python
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
```

 - HttpLocust represents a user
    - you can define how long a simulated user should wait between executing tasks (min_wait and max_wait) , in milliseconds
    - HttpLocust class inherits from the `Locust` class, and it adds a client attribute which is an instance of `HttpSession` that can be used to make HTTP requests
 - TaskSet is to define task behavior , it can be nested


<h2 id="5818c3f44e2dc782824809dface48782"></h2>

### Start Locust

```
# To run Locust with the above Locust file, if it was named locustfile.py 
# and located in the current working directory, we could run:
$ locust --host=http://example.com
```

```
# or to specific a locust file
$ locust -f locust_files/my_locust_file.py --host=http://example.com
```

```
# To run Locust distributed across multiple processes 
#  we would start a master process by specifying --master
$ locust -f locust_files/my_locust_file.py --master --host=http://example.com

# and then we would start an arbitrary number of slave processes:
locust -f locust_files/my_locust_file.py --slave --host=http://example.com

# If we want to run Locust distributed on multiple machines 
# we would also have to specify the master host when starting the slaves 
$ locust -f locust_files/my_locust_file.py --slave --master-host=192.168.0.100 --host=http://example.com
```

<h2 id="0b83bfe6ef2a315017a7a511a659738d"></h2>

### Open up Locust’s web interface

http://127.0.0.1:8089

---

<h2 id="a68f707e65b8641b73c329764e983414"></h2>

## Writing a locustfile

<h2 id="17909d322ee85b757b0a2da94f5a6c65"></h2>

### The Locust class

 - A locust class represents one user 
 - Locust will spawn (hatch) one instance of the locust class for each user that is being simulated
 - There are a few attributes that a locust class should typically define.
    - The *task_set* attribute
        - should point to a TaskSet class which defines the behaviour of the user 
    - The *min_wait* and *max_wait* attributes
        - in milliseconds ,  minimum and maximum time that a simulated user will wait between executing **each task**.
        - min_wait and max_wait default to 1000
    - The min_wait and max_wait attributes can also be overridden in a TaskSet class.
 - The host attribute
    - Usually, this is specified on the command line, using the --host option
    - If one declares a host attribute in the locust class, it will be used in the case when no --host is specified on the command line.
 - The weight attribute
    - You can run two locusts from the same file like so:
    - `$ locust -f locust_file.py WebUserLocust MobileUserLocust`
    - If you wish to make one of these locusts execute more often you can set a weight attribute on those classes 
        - Say for example, web users are three times more likely than mobile users:

```python
class WebUserLocust(Locust):
    weight = 3
    ...

class MobileUserLocust(Locust):
    weight = 1
    ...
```


<h2 id="9c07c110dc52aed577d7d571811f6d80"></h2>

### TaskSet class

 - a collection of tasks
 - These tasks are normal python callables 
 - When a load test is started, each instance of the spawned Locust classes will start executing their TaskSet. 
    - pick one of its tasks and call it
    - then wait a number of milliseconds, chosen at random between the Locust class’ min_wait and max_wait attributes
    - again pick a new task to be called
    - wait again, and so on

<h2 id="856e1ed6703f100ddb34260e858157ff"></h2>

####  Declaring tasks:

```
    @task
    def my_task(self):
        print("Locust instance (%r) executing my_task" % (self.locust))
```

 - @task takes an optional weight argument that can be used to specify the task’s execution ratio
    - the following example task2 will be executed twice as much as task1:

```
    @task(3)
    def task1(self):
        pass

    @task(6)
    def task2(self):
        pass
```

<h2 id="69b67acae5e44a6d396ebf8b48e0f7ba"></h2>

#### tasks attribute

 - Using the @task decorator to declare tasks is a convenience, and usually the best way to do it. 
 - However, it’s also possible to define the tasks of a TaskSet by setting the tasks attribute
 - The tasks attribute is either a list of python callables, or a <callable : int> dict

```python
from locust import Locust, TaskSet

def my_task(l):
    pass

class MyTaskSet(TaskSet):
    tasks = [my_task]

class MyLocust(Locust):
    task_set = MyTaskSet
```

 - TaskSets can be nested

```python
class ForumPage(TaskSet):
    @task(20)
    def read_thread(self):
        pass

    @task(1)
    def new_thread(self):
        pass

    @task(5)
    def stop(self):
        self.interrupt()

class UserBehaviour(TaskSet):
    tasks = {ForumPage:10}

    @task
    def index(self):
        pass
```

 - There is one important thing to note about the above example, and that is the call to `self.interrupt()` 
 - What this does is essentially to stop executing the ForumPage task set and the execution will continue in the UserBehaviour instance.
 - If we didn’t have a call to the interrupt() method somewhere in ForumPage, the Locust would never stop running the ForumPage task once it has started. 
 - It’s also possible to declare a nested TaskSet, inline in a class, using the @task decorator, just like when declaring normal tasks:

```python
class MyTaskSet(TaskSet):
    @task
    class SubTaskSet(TaskSet):
        @task
        def my_task(self):
            pass
```

<h2 id="80b785988c0e04f1f45801f4f6b70c3d"></h2>

#### Referencing the Locust instance, or the parent TaskSet instance

 - A TaskSet instance will have the attribute locust point to its Locust instance,
 - and the attribute parent point to its parent TaskSet (it will point to the Locust instance, in the base TaskSet).

---

<h2 id="68364ef1a4284141a6ee8f52d2b212c9"></h2>

### TaskSequence class

 - TaskSequence class is a TaskSet but its tasks will be executed in order.

```
class MyTaskSequence(TaskSequence):
    @seq_task(1)
    def first_task(self):
        pass

    @seq_task(2)
    def second_task(self):
        pass

    @seq_task(3)
    @task(10)
    def third_task(self):
        pass
```

 - In the above example
    - the order is defined to execute first_task, then second_task and lastly the third_task for 10 times.

<h2 id="bb8557529751c16ab2fdf9bda9d837d0"></h2>

### Setups, Teardowns, on_start, and on_stop

 - Locust optionally supports
    - Locust level setup and teardown
    - TaskSet level setup and teardown, and TaskSet on_start and on_stop

<h2 id="09288898f790687018c0a6e33f1fe57d"></h2>

#### Setups and Teardowns

 - methods that are run only once.
    - setup is run before tasks start running, 
    - while teardown is run after all tasks have finished and Locust is exiting. 
 - This enables you to perform some preparation before tasks start running (like creating a database) and to clean up before the Locust quits (like deleting the database).
 - simply declare a setup and/or teardown on the Locust or TaskSet class

<h2 id="c185ebe8be7bef6661e45bf00e6e3291"></h2>

#### The on_start and on_stop methods

 - The on_start method is called when a simulated user starts executing that TaskSet class, 
 - while the on_stop method is called when the TaskSet is stopped.
 

<h2 id="9466aa1dc479ae1c7da40c3d273d25ae"></h2>

#### Order of events

 1. Locust setup
 2. TaskSet setup
 3. TaskSet on_start
 4. TaskSet tasks…
 5. TaskSet on_stop
 6. TaskSet teardown
 7. Locust teardown


<h2 id="9e1edb42e7f308a64ccee832eb1ab5bf"></h2>

### Making HTTP requests

 - HttpLocust class provide a *client* attribute which will be an instance of HttpSession which can be used to make HTTP requests.
 - `client` support cookies, and therefore keeps the session between HTTP requests.

```python
class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")
```

 - PS:  TaskSet has a convenience property called *client*  that simply returns `self.locust.client`.

<h2 id="ea493d7b6bf94bafb89e84a3637c0a14"></h2>

#### Using the HTTP client

 - Each instance of HttpLocust has an instance of HttpSession in the client attribute
 - The HttpSession class is actually a subclass of requests.Session ,  and can be used to make HTTP requests, that will be reported to Locust’s statistics
    - using the get, post, put, delete, head, patch and options methods. 
 - The HttpSession instance will preserve cookies between requests so that it can be used to log in to websites and keep a session between requests.

```python
response = self.client.get("/about")
print("Response status code:", response.status_code)
print("Response content:", response.text)
```

```python
response = self.client.post("/login", {"username":"testuser", "password":"secret"})
```

```python
# add header 
headers = {'content-type': 'application/json'}
response = self.client.post("/login", {"username":"testuser", "password":"secret" } , headers=headers )
```

<h2 id="8f515507f68651c99f27a6790119d54b"></h2>

#### Safe mode

 - The HTTP client is configured to run in safe_mode
 - What this does is that any request that fails due to a connection error, timeout, or similar will not raise an exception, but rather return an empty dummy Response object. 
 - The request will be reported as a failure in Locust’s statistics. 
 - The returned dummy Response’s content attribute will be set to None, and its status_code will be 0.

<h2 id="b5431017aad3c9e5df25938d8cee350e"></h2>

#### Manually controlling if a request should be considered successful or a failure

 - By default, requests are marked as failed requests unless the HTTP response code is OK (2xx). 
 - Most of the time, this default is what you want. Sometimes however there’s a need for manually controlling if locust should consider a request as a success or a failure.
    - for example when testing a URL endpoint that you expect to return 404
    - or testing a badly designed system that might return 200 OK even though an error occurred 
 - One can mark requests as failed, even when the response code is OK ,
    - by using the `catch_response` argument and a with statement:

```python
with client.get("/", catch_response=True) as response:
    if response.content != b"Success":
        response.failure("Got wrong response")
```

 - can one can also make requests that resulted in an HTTP error code still be reported as a success in the statistics:

```python
with client.get("/does_not_exist/", catch_response=True) as response:
    if response.status_code == 404:
        response.success()
```

<h2 id="ef2e4c961c56e33d44553e9363e54ebb"></h2>

#### Grouping requests to URLs with dynamic parameters

 - It’s very common for websites to have pages whose URLs contain some kind of dynamic parameter(s).
 - Often it makes sense to group these URLs together in Locust’s statistics.
 - This can be done by passing a name argument to the HttpSession's different request methods.

```python
# Statistics for these requests will be grouped under: /blog/?id=[id]
for i in range(10):
    client.get("/blog?id=%i" % i, name="/blog?id=[id]")
```

---

<h2 id="3e38fcc9f82e983c75263725bd426b37"></h2>

## Running Locust distributed

https://docs.locust.io/en/latest/running-locust-distributed.html

<h2 id="b5ef92324c2f19871c6c35b8303f2132"></h2>

## Running Locust without the web UI

 - You can run locust without the web UI 
    - by using the `--no-web` flag together with `-c` and `-r`:

```
$ locust -f locust_files/my_locust_file.py --no-web -c 1000 -r 100
```

 - `-c` specifies the number of Locust users to spawn, 
 - and `-r` specifies the hatch rate (number of users to spawn per second).

<h2 id="b7485a0fc6cd00ba97c74332b56d1b0d"></h2>

### Setting a time limit for the test

 - PS: This is a new feature in v0.9. For 0.8 use `-n` to specify the number of requests

 - If you want to specify the run time for a test, you can do that with `--run-time` or `-t`:

```
$ locust -f --no-web -c 1000 -r 100 --run-time 1h30m
```

 - Locust will shutdown once the time is up.

<h2 id="a6192bcf475fe53f0db6cc7f137a5924"></h2>

### Running Locust distributed without the web UI

 - If you want to run Locust distributed without the web UI, you should specify the `--expect-slaves` option when starting the master node, to specify the number of slave nodes that are expected to connect. 
 - It will then wait until that many slave nodes have connected before starting the test.


<h2 id="3c26f7b316cf2486f480c9c90f5dbd9e"></h2>

## Retrieve test statistics in CSV format

 - when running Locust with the web UI, you can retrieve CSV files under the Download Data tab.
 - when running with `--no-web` flag:

```
$ locust -f examples/basic.py --csv=example --no-web -t10m
```

 - The files will be named example_distribution.csv and example_requests.csv (when using --csv=example) and mirror Locust’s built in stat pages.
 - You can also customize how frequently this is written if you desire faster (or slower) writing:

```
import locust.stats
locust.stats.CSV_STATS_INTERVAL_SEC = 5 # default is 2 seconds
```





 


