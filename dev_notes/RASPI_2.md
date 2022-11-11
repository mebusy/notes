[](...menustart)

- [Raspberry Pi II](#e03b130e1f3b2c56de9bb84e75301d14)
    - [Network](#eec89088ee408b80387155272b113256)
        - [Connecting to a network](#6163d0d5344363e3ed9c8c35cba6aa8f)
        - [Using a Web Browse](#01f4c6bc4bda78ced8f1cd4555d8afb1)
        - [SSH](#765553e6c7ac8592c389acb9878a050a)
        - [Internet Protocal Family](#71a93e1fa9812a362d4c96147fc4b9d9)
        - [Domain Names](#12cb487a02c71008e53bd64a004d0860)
            - [nslookup](#5d46e505618626b201a5aca4fe2e6b29)
        - [Internect Connections](#2ab4aec4cb63c31debb0851551876d1b)
        - [Sockets on the Client](#719aa84114261906ae42b32d3b2cc7ab)
            - [Creating a Socket](#c62666960662903ff488cbddd3791625)
            - [Connect Socket to Server](#fbc296173c66a5f84aff3a2bf69304a1)
            - [Sending Data on a Socket](#ba86050b8bd9d3cae071425f71deaeff)
            - [Receiving Data on a Socket](#82c00833b57823a4f596c6d0ba003f8d)
            - [Closing a Socket](#18c78f12845c54db7dba0ccd0ed01290)
        - [Exceptions](#d5f1381c5f97f928df4ef8d18c2a27c0)
            - [Socket Exceptions](#4eec4beeae261bf08c1ad4afbdc2b9c5)
        - [Sockets on the Server](#404181167afb206bd622e39eb1c6cebe)
            - [Creating and Binding a Socket](#2919cf8e2b08084c5c14534d8380797c)
            - [Listening and Accepting a Connect](#b85c73f27fd0d1b3769572044aa4cfd5)
            - [Sending and  Receiving](#c7dbc4fd55364e7eb7d9f6f8b04c3174)
    - [Camera](#967d35e40f3f95b1f538bd248640bf3b)
        - [Enabling the Camera](#a01b7f8cc255f7cab060ae9f1f19caf5)
        - [python-picamera Library](#9e62a134a017a3ddea4fe303a1c83ae4)
        - [Capturing Image](#0b8bb194abe8d7202369a512619484e8)
        - [Timelapse Photography](#7a1314d2fcc369c3eb926f232d841e62)

[](...menuend)


<h2 id="e03b130e1f3b2c56de9bb84e75301d14"></h2>

# Raspberry Pi II

<h2 id="eec89088ee408b80387155272b113256"></h2>

## Network

<h2 id="6163d0d5344363e3ed9c8c35cba6aa8f"></h2>

### Connecting to a network

- wired connection using the built-in RJ45 connector
- Wi-Fi connection using a USB Wi-Fi adapter
    - start **Wifi Config** from the desktop


<h2 id="01f4c6bc4bda78ced8f1cd4555d8afb1"></h2>

### Using a Web Browse

- **Epiphany** browse is builti-in


<h2 id="765553e6c7ac8592c389acb9878a050a"></h2>

### SSH

- Should change the private host ID keys
    - Otherwise , they have the same default values.

One you install raspbian on your Pi, you get these default keys ,which are the same as everybody else's default keys.

```bash
sudo rm /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server
```
    
<h2 id="71a93e1fa9812a362d4c96147fc4b9d9"></h2>

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


<h2 id="12cb487a02c71008e53bd64a004d0860"></h2>

### Domain Names

IP addresses are not easy for humans to memorize, so we use domain names. eg. `cc.com`

Each domain name must be resolved to an IP address to send packets.

So ,for that we use what's called **domain naming system, DNS**.

- DNS is a hierarchical naming system used to determine IP addresses from domain names
- Gigantic, distributed tables are accessed by performing a DNS Lookup

When you visit cnn.com, your web browser sends a message to a DNS server and says and look, what is the address of cnn.com?  And if DNS server knows that address, it sends the IP address back to you. If it doesn't , then it goes and asks another DNS server higher up.  The ip address will store in a local cache to save time.

<h2 id="5d46e505618626b201a5aca4fe2e6b29"></h2>

#### nslookup

```
nslookup baidu.com
Server:        192.168.1.1
Address:    192.168.1.1#53

Non-authoritative answer:
Name:    baidu.com
Address: 180.149.132.47
Name:    baidu.com
Address: 220.181.57.217
Name:    baidu.com
Address: 111.13.101.208
Name:    baidu.com
Address: 123.125.114.144
```

- #53 is the port
 

<h2 id="2ab4aec4cb63c31debb0851551876d1b"></h2>

### Internect Connections

 1. A socket is an endpoint of a connection
 2. client and server both have sockets
 3. A port is a 16-bit integer that identifies a process



<h2 id="719aa84114261906ae42b32d3b2cc7ab"></h2>

### Sockets on the Client

Creating a generic network client:

 1. Create a socket
 2. Connect socket to server
 3. Send some data ( a request )
 4. Receive some data ( a response )
 5. Close the socket


<h2 id="c62666960662903ff488cbddd3791625"></h2>

#### Creating a Socket

```python
import socket
mysock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
```
 

- AF_INET declares Address Family Internet
- SOCK_STREAM idicates TCP (connection-based)

<h2 id="fbc296173c66a5f84aff3a2bf69304a1"></h2>

#### Connect Socket to Server

```
>>> host = socket.gethostbyname( 'www.baidu.com' ) #不解析也可以
>>> PORT = 80
>>> mysock.connect( host, PORT )  # mysock.connect( (host, PORT) ) for 2.7 
```

<h2 id="ba86050b8bd9d3cae071425f71deaeff"></h2>

#### Sending Data on a Socket

```python
message = "GET / HTTP/1.1\r\n\r\n"
mysock.sendall(message)
```

- sendall() send the data , and tries until it succeeds.

<h2 id="82c00833b57823a4f596c6d0ba003f8d"></h2>

#### Receiving Data on a Socket

```
data = mysock.recv(1024) 
```

- recv() returns the data on the socket
    - Blocking wait, by default , you can change that
- python will resize the data buffer for you1


<h2 id="18c78f12845c54db7dba0ccd0ed01290"></h2>

#### Closing a Socket

```python
mysock.close()  # free up port
```

<h2 id="d5f1381c5f97f928df4ef8d18c2a27c0"></h2>

### Exceptions 

- Errors may happen when working with sockets
    - Socket cannot be opened
    - Data cannot be sent

<h2 id="4eec4beeae261bf08c1ad4afbdc2b9c5"></h2>

#### Socket Exceptions

- socket.error
    - All socket errors
- gaierror
    - getaddressinfo() - no host found


<h2 id="404181167afb206bd622e39eb1c6cebe"></h2>

### Sockets on the Server

 1. Create a socket
 2. Bind the socket to an IP address and port
 3. Listen for a connection
 4. Accept the connection
 5. Receive the request
 6. Send the response

<h2 id="2919cf8e2b08084c5c14534d8380797c"></h2>

#### Creating and Binding a Socket

```python
mysock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
mysock.bind( "",1234 ) # mysock.bind( ("",1234) ) 2.7
```

- **bind()** : the 1st argument it the host that you want to sssociate it with
    - "" like a wildcard , it allows it to receive from any host


<h2 id="b85c73f27fd0d1b3769572044aa4cfd5"></h2>

#### Listening and Accepting a Connect

```python
mysock.listen(5)
conn , addr = mysock.accept()
```

- **listen()** starts listening for a connect()
    - argument is called **backlog** , it's the number of requests allowed to wait for service.
- **accept()** accepts a connection request
    - return a connection (for sending/receiving) and an address (IP, port)

<h2 id="c7dbc4fd55364e7eb7d9f6f8b04c3174"></h2>

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

<h2 id="967d35e40f3f95b1f538bd248640bf3b"></h2>

## Camera

<h2 id="a01b7f8cc255f7cab060ae9f1f19caf5"></h2>

### Enabling the Camera

- Use **raspi-config** to enable the CSI interface
    - sudo raspi-config 
- Select *Enable Camera* , done

<h2 id="9e62a134a017a3ddea4fe303a1c83ae4"></h2>

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
    
<h2 id="0b8bb194abe8d7202369a512619484e8"></h2>

### Capturing Image

Capture an image, send it on a connection.

```python
mysocket = socket.socket()
mysocket.connect( ( 'aserver' , 8000 ) )
conn = mysocket.makefile( 'wb' )
camera.capture( conn, 'jpeg' )
```

- Need a file-like object to capture to 
 
<h2 id="7a1314d2fcc369c3eb926f232d841e62"></h2>

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

