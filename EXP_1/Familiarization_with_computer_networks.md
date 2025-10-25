## Experiment 1

# Familiarization with Computer Networks

### AIM

To familiarize with computer networks

### THEORY

Python provides two levels of acces to network programming

1. **Low Level Access** : At the low level you ca*n access the base socket support or the operating system.

2. **High Level Access** : At the high level it allows to implement protocol like  HTTP, FTP, etc..

Socket acts as an end point in a bidirectional communication channel. Socket use different protocol for determining the connection type for port to port communication type betweeen client and server.

Socket programming is a way of communication of two nodes of a network through connection with each other. One socket listen on a particular port which the other socket reaches out to form a communication. 

To create a socket we use the `socket.socket()` method.

```python
socket.socket(socket_family,socket_type,protocol)
```
---
#### `socket.server()` methods:

- `s.bind()`: Bind address to the socket. The address contains the pair of hostname and the port number
- `s.listen()` : Start the listener
- `s.accept()` : Accept the client connection socket client methods
- `s.connect()` : Actively start the connection with the server
---
Socket general methods :
- `s.send()` : sends the TCP message
- `s.sendto()` : sends the UDP message
- `s.recv()` : recieves the TCP message
- `s.recvfrom()` : recieves the UDP message
- `s.close()` : close the socket

---

**TCP** : Transmission Control Protocol is a connection oriented protocol for communication that helps in the exchange of messages between different devices over a network.

**UDP** : User Datagram Protocol is a connection less protocol which does not establish a conenction before data transfer.

### RESULT

The concepts in computer network was familiarized




