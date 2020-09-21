
# github.com/gorilla/websocket

[package websocket](https://pkg.go.dev/github.com/gorilla/websocket)

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

## Concurrency

- **Connections support one concurrent reader and one concurrent writer**.

## Origin Considerations

- The Upgrader calls the function specified in the CheckOrigin field to check the origin.
- If the CheckOrigin field is nil, then the Upgrader uses a safe default: fail the handshake if the Origin request header is present and the Origin host is not equal to the Host request header.

## Buffers

- Some guidelines for setting buffer parameters are:
    - Limit the buffer sizes to the maximum expected message size. Buffers larger than the largest message do not provide any benefit.
    - 注意：是期望值，不是最大值

- Buffers are held for the lifetime of the connection by default.
    - If the Dialer or Upgrader WriteBufferPool field is set, then a connection holds the write buffer only when writing a message.
    - *sync.Pool
- A write buffer pool is useful when the application has a modest number writes over a large number of connections. 
    - when buffers are pooled, a larger buffer size has a reduced impact on total memory use and has the benefit of reducing system calls and frame overhead.



## API

- func (*Conn) SetReadDeadline
    - After a read has timed out, the websocket connection state is corrupt and all future reads will return an error. 
- func (*Conn) SetWriteDeadline ¶
    - After a write has timed out, the websocket state is corrupt and all future writes will return an error. 

- func (*Conn) WriteControl
    - WriteControl writes a control message with the given deadline. The allowed message types are CloseMessage, PingMessage and PongMessage.

