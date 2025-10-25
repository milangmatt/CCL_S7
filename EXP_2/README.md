# Client Server chat using TCP

This is a simple TCP-based chat application implemented in Python using the socket module. The application consists of two programs: a server and a client that can communicate with each other.

### How to run

1. Open two terminals.
2. In each terminal change directory to the EXP_2 folder:
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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
```
- `AF_INET`: Specifies IPv4 for network protocol. For IPv6 use `AF_INET6`.
- `SOCK_STREAM`: Indicates TCP protocol for reliable communication

### Server Program

#### Connection Setup
```python
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port number
s.bind((HOST, PORT))
s.listen()
```
- Binds to localhost (127.0.0.1)
- Uses port 65432 for communication
- Starts listening for incoming connections

#### Message Handling
```python
conn, addr = s.accept()
data = conn.recv(1024).decode()
conn.sendall(reply.encode())
```
- Accepts client connections
- Receives messages (1024 bytes max)
- Sends responses back to client

### Client Program

#### Connection Setup
```python
HOST = '127.0.0.1'  # Server's IP
PORT = 65432        # Server's port
s.connect((HOST, PORT))
```
- Connects to server using same HOST and PORT

#### Message Handling
```python
s.sendall(message.encode())
data = s.recv(1024).decode()
```
- Sends messages to server
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

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server. Type 'exit' to quit.")

    while True:
        message = input("Client: ")
        s.sendall(message.encode())

        if message.lower() == "exit":
            print("Client ended the chat.")
            break

        data = s.recv(1024).decode()
        print(f"Server: {data}")

        if data.lower() == "exit":
            print("Server ended the chat.")
            break
```

### server.py
```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()

            if not data:
                break

            print(f"Client: {data}")

            if data.lower() == "exit":
                print("Client ended the chat.")
                break

            reply = input("Server: ")
            conn.sendall(reply.encode())

            if reply.lower() == "exit":
                print("Server ended the chat.")
                break
```