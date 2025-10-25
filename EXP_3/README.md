# Client Server chat using UDP

This is a simple UDP-based chat application implemented in Python using the socket module. The application consists of two programs: a server and a client that can communicate with each other.

### How to run

1. Open two terminals.
2. In each terminal change directory to the EXP_3 folder:
3. In terminal 1 start the server:
    ```bash
    python3 server.py
    ```
4. In terminal 2 start the client:
    ```bash
    python3 client.py
    ```

Notes:
- If `python3` is not available on Windows, use `python` or `py -3`.
- Keep both terminals open; type `exit` in either side to terminate the chat.

### Socket Creation and Configuration

Both programs use the socket module for network communication:

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
```
- `AF_INET`: Specifies IPv4 for network protocol
- `SOCK_DGRAM`: Indicates UDP protocol for connectionless communication

### Server Program

#### Connection Setup
```python
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port number
s.bind((HOST, PORT))
```
- Binds to localhost (127.0.0.1)
- Uses port 65432 for communication

#### Message Handling
```python
data, addr = s.recvfrom(1024)
s.sendto(reply.encode(), addr)
```
- Receives messages and client address (1024 bytes max)
- Sends responses back to client's address

### Client Program

#### Message Handling
```python
s.sendto(message.encode(), (HOST, PORT))
data, server = s.recvfrom(1024)
```
- Sends messages to server's address
- Receives server's responses

### Exit Mechanism
Both programs implement an exit mechanism using the keyword "exit":
```python
if message.lower() == "exit":
    print("Chat ended.")
    break
```

## Complete Source Code


### client.py
```python
import socket  

HOST = '127.0.0.1'  
PORT = 65432       


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("Connected to UDP server. Type 'exit' to quit.")

    while True:
        message = input("Client: ")
        s.sendto(message.encode(), (HOST, PORT))
        if message.lower() == 'exit':
            print("Client ended the chat.")
            break
        data, server = s.recvfrom(1024)
        reply = data.decode()
        print(f"Server: {reply}")
        if reply.lower() == 'exit':
            print("Server ended the chat.")
            break
```

### server.py
```python
import socket

HOST = '127.0.0.1'
PORT = 65432      

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}...")

    while True:
        data, addr = s.recvfrom(1024)
        message = data.decode()
        print(f"Client ({addr}): {message}")

        if message.lower() == 'exit':
            print("Client ended the chat.")
            break

        reply = input("Server: ")

        s.sendto(reply.encode(), addr)

        if reply.lower() == 'exit':
            print("Server ended the chat.")
            break
```