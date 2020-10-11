...menustart

- [github.com/gorilla/websocket](#6fa1b8e5c3878c9c6185055837bd2fde)
    - [Overview](#3b878279a04dc47d60932cb294d96259)
    - [Control Messages](#cfbf5a3d7314f33620de8b7105a40090)
    - [Concurrency](#3e48afddb0c5521684b8d2687b0869d6)
    - [Origin Considerations](#d09a4b59e096374b40568f20866ee2b1)
    - [Buffers](#4c19ddb10d5a902842dda06a62c3d601)
    - [API](#db974238714ca8de634a7ce1d083a14f)

...menuend


<h2 id="6fa1b8e5c3878c9c6185055837bd2fde"></h2>


# github.com/gorilla/websocket

[package websocket](https://pkg.go.dev/github.com/gorilla/websocket)

<h2 id="3b878279a04dc47d60932cb294d96259"></h2>


## Overview

- The *Conn* type represents a WebSocket connection.
- Server application calls the Upgrader.Upgrade method from an HTTP request handler to get a *Conn:
    ```golang
    var upgrader = websocket.Upgrader{
        ReadBufferSize:  1024,
        WriteBufferSize: 1024,
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        conn, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
            log.Println(err)
            return
        }
        ... Use conn to send and receive messages.
    }
    ```

- send and receive messages as a slice of bytes
    ```golang
    for {
        messageType, p, err := conn.ReadMessage()
        if err != nil {
            log.Println(err)
            return
        }
        if err := conn.WriteMessage(messageType, p); err != nil {
            log.Println(err)
            return
        }
    }
    ```
    - p is a []byte and messageType is an int with value websocket.BinaryMessage or websocket.TextMessage.

- Can also send and receive messages using the io.WriteCloser and io.Reader interfaces
    ```golang
    for {
        messageType, r, err := conn.NextReader()
        if err != nil {
            return
        }
        w, err := conn.NextWriter(messageType)
        if err != nil {
            return err
        }
        // write the message to the writer and close the writer when done
        if _, err := io.Copy(w, r); err != nil {
            return err
        }
        if err := w.Close(); err != nil {
            return err
        }
    }
    ```
    - connection NextWriter method to get an io.WriteCloser
    - connection NextReader method to get an io.Reader and read until io.EOF is returned

<h2 id="cfbf5a3d7314f33620de8b7105a40090"></h2>


## Control Messages

- three types of control messages: close, ping and pong
- Call the connection WriteControl, WriteMessage or NextWriter methods to send a control message to the peer.
- If an application sends ping messages, then the application should set a pong handler to receive the corresponding pong.
- The application must read the connection to process close, ping and pong messages sent from the peer. 
    - If the application is not otherwise interested in messages from the peer, then the application should start a goroutine to read and discard messages from the peer. 
    - A simple example is:
    ```golang
    func readLoop(c *websocket.Conn) {
        for {
            if _, _, err := c.NextReader(); err != nil {
                c.Close()
                break
            }
        }
    }
    ```

<h2 id="3e48afddb0c5521684b8d2687b0869d6"></h2>


## Concurrency

- **Connections support one concurrent reader and one concurrent writer**.

<h2 id="d09a4b59e096374b40568f20866ee2b1"></h2>


## Origin Considerations

- The Upgrader calls the function specified in the CheckOrigin field to check the origin.
- If the CheckOrigin field is nil, then the Upgrader uses a safe default: fail the handshake if the Origin request header is present and the Origin host is not equal to the Host request header.

<h2 id="4c19ddb10d5a902842dda06a62c3d601"></h2>


## Buffers

- Some guidelines for setting buffer parameters are:
    - Limit the buffer sizes to the maximum expected message size. Buffers larger than the largest message do not provide any benefit.
    - 注意：是期望值，不是最大值

- Buffers are held for the lifetime of the connection by default.
    - If the Dialer or Upgrader WriteBufferPool field is set, then a connection holds the write buffer only when writing a message.
    - *sync.Pool
    ```go
    var upgrader = websocket.Upgrader{
    ReadBufferSize:  512, // comments these 2 lines if you want use default upgrader
    // WriteBufferSize: 1024,
    WriteBufferPool: &sync.Pool{},
    }
    ```
- A write buffer pool is useful when the application has a modest number writes over a large number of connections. 
    - when buffers are pooled, a larger buffer size has a reduced impact on total memory use and has the benefit of reducing system calls and frame overhead.


<h2 id="db974238714ca8de634a7ce1d083a14f"></h2>


## API

- func (*Conn) SetReadDeadline
    - After a read has timed out, the websocket connection state is corrupt and all future reads will return an error. 
- func (*Conn) SetWriteDeadline ¶
    - After a write has timed out, the websocket state is corrupt and all future writes will return an error. 

- func (*Conn) WriteControl
    - WriteControl writes a control message with the given deadline. The allowed message types are CloseMessage, PingMessage and PongMessage.


## Optimization

- Each connection in the **naive** solution comsumes ~20K.
    - Mem = conns · ( goroutine + buf<sub>net/http</sub> + buf<sub>gorilla/ws</sub> ) 
    - That is, 1M CCU would consume over 20G of RAM
- Optimization
    1. goroutine 
        - knowing when data exists on the wire would allow us to reuse goroutines and reduce memory footprint
        - epoll
    2. buffers allocations
        - gorilla/websocket keeps a reference to the underlying buffers given by Hijack()
        - use `https://github.com/gobwas/ws` instead

- Recap
    - Ulimit: Increase the cap of NOFILE resource
    - Epoll(Async I/O): Reduce the high load of goroutines
        - epoll is available only on linux, solution [epoller](https://github.com/smallnest/epoller)
    - Gobwas: More performant ws library to reduce buffer allocations
    - Conntrack table: Increase the cap of total concurrent connections in the OS
        - `echo 2621440 > /proc/sys/net/netfilter/nf_conntrack_max `  ?
    - other reading
        - [A Million WebSockets and Go](https://www.freecodecamp.org/news/million-websockets-and-go-cc58418460bb/)
        - [github 1M websockets](https://github.com/eranyanay/1m-go-websockets)



