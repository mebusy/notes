# Raspberry Pi II

## Network

### Connecting to a network

 - wired connection using the built-in RJ45 connector
 - Wi-Fi connection using a USB Wi-Fi adapter
    - start **Wifi Config** from the desktop


### Using a Web Browse

 - **Epiphany** browse is builti-in


### SSH

 - Should change the private host ID keys
    - Otherwise , they have the same default values.

One you install raspbian on your Pi, you get these default keys ,which are the same as everybody else's default keys.

```bash
sudo rm /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server
```
    
### Internet Protocal Family

 - **IP** (Internet protocal)
    - Host naming scheme , define IP address
    - Host-to-host connection, unreliable
 - **UDP** (Unreliable Datagram Protocal)
    - Process-to-process communication
    - Process naming
    - Also unreliable
 - **TCP** (Transmission Control Protocal)
    - Process-to-process communication and naming
    - Process naming
    - Reliable communication


### Domain Names

IP addresses are not easy for humans to memorize, so we use domain names. eg. `cc.com`

Each domain name must be resolved to an IP address to send packets.

So ,for that we use what's called **domain naming system, DNS**.

 - DNS is a hierarchical naming system used to determine IP addresses from domain names
 - Gigantic, distributed tables are accessed by performing a DNS Lookup

When you visit cnn.com, your web browser sends a message to a DNS server and says and look, what is the address of cnn.com?  And if DNS server knows that address, it sends the IP address back to you. If it doesn't , then it goes and asks another DNS server higher up.  The ip address will store in a local cache to save time.

#### nslookup

```
nslookup baidu.com
Server:		192.168.1.1
Address:	192.168.1.1#53

Non-authoritative answer:
Name:	baidu.com
Address: 180.149.132.47
Name:	baidu.com
Address: 220.181.57.217
Name:	baidu.com
Address: 111.13.101.208
Name:	baidu.com
Address: 123.125.114.144
```

 - #53 is the port
 

### Internect Connections

 1. A socket is an endpoint of a connection
 2. client and server both have sockets
 3. A port is a 16-bit integer that identifies a process



### Sockets on the Client

Creating a generic network client:

 1. Create a socket
 2. Connect socket to server
 3. Send some data ( a request )
 4. Receive some data ( a response )
 5. Close the socket


#### Creating a Socket

```python
import socket
mysock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
```
 

 - AF_INET declares Address Family Internet
 - SOCK_STREAM idicates TCP (connection-based)

#### Connect Socket to Server

```
>>> host = socket.gethostbyname( 'www.baidu.com' ) #不解析也可以
>>> PORT = 80
>>> mysock.connect( host, PORT )  # mysock.connect( (host, PORT) ) for 2.7 
```

#### Sending Data on a Socket

```python
message = "GET / HTTP/1.1\r\n\r\n"
mysock.sendall(message)
```

 - sendall() send the data , and tries until it succeeds.

#### Receiving Data on a Socket

```
data = mysock.recv(1024) 
```

 - recv() returns the data on the socket
    - Blocking wait, by default , you can change that
 - python will resize the data buffer for you1


#### Closing a Socket

```python
mysock.close()  # free up port
```

### Exceptions 

 - Errors may happen when working with sockets
    - Socket cannot be opened
    - Data cannot be sent

#### Socket Exceptions

 - socket.error
    - All socket errors
 - gaierror
    - getaddressinfo() - no host found


### Sockets on the Server

 1. Create a socket
 2. Bind the socket to an IP address and port
 3. Listen for a connection
 4. Accept the connection
 5. Receive the request
 6. Send the response

#### Creating and Binding a Socket

```python
mysock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
mysock.bind( "",1234 ) # mysock.bind( ("",1234) ) 2.7
```

 - **bind()** : the 1st argument it the host that you want to sssociate it with
    - "" like a wildcard , it allows it to receive from any host


#### Listening and Accepting a Connect

```python
mysock.listen(5)
conn , addr = mysock.accept()
```

 - **listen()** starts listening for a connect()
    - argument is called **backlog** , it's the number of requests allowed to wait for service.
 - **accept()** accepts a connection request
    - return a connection (for sending/receiving) and an address (IP, port)

#### Sending and  Receiving

```python
data = conn.recv(1000)
conn.sendall(data)

conn.close()
mysock.close()
```

**A Live Server**

```python
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    conn.sendall(data)
    
conn.close()
mysock.close()
```

## Camera

### Enabling the Camera

 - Use **raspi-config** to enable the CSI interface
    - sudo raspi-config 
 - Select *Enable Camera* , done

### python-picamera Library

 - install the library
    - 
    ```
    sudo apt-get update
    sudo apt-get install python3-picamera
    ```
    
 - Using the library
    -
    ```
    import picamera
    camera = picamera.PiCamera()
    ```
   
 
 #### Camera Functions
 
 
 - Take a picture
    - camera.capture("pict.jpg")
 - Changing camera settings
    - There are many
    - `camera.hflip = True`
    - `camera.vflip = True`
    - `camera.brightness = 50`
    - `camera.sharpness = 0`
 - View video on RPi screen
    - `camera.start_preview()`
    - `camera.stop_preview()`
 - Video Recording
    - 
    ```
    camera.start_recording( "vid.h264" )
    time.sleep(10)
    camera.stop_recording()
    ```
    
### Capturing Image

Capture an image, send it on a connection.

```python
mysocket = socket.socket()
mysocket.connect( ( 'aserver' , 8000 ) )
conn = mysocket.makefile( 'wb' )
camera.capture( conn, 'jpeg' )
```

 - Need a file-like object to capture to 
 
### Timelapse Photography

 - `camera.capture_continuous()`
    - takes photos over time
 - Takes one argument , a file name
 - {counter} and {timestamp} can be substituted
 - ex. "picture{counter}.jpg" produces picture1.jpg, picture2.jpg, etc.


```python
camera = picamera.PiCamera()
for filename in
    camera.capture_continuous('img{counter}.jpg'):
    time.sleep(300) # 不知道什么用意
```

 - Iterate through all images, infinite loop
 - 5 minute delya between images

