## Experiment 7

#  Client Server TCP Communication using Virtual Machine

### AIM

Install a java compiler in the virtual machine and implement client-server communcation using Java with TCP protocol.

### ALGORITHM

#### TCP Server
1. Start
2. Import necessary modules
3. Create a Server socket object with a specific port number
4. Wait for the client to connect
5. Create Input and Output Streams from the socket
    1. InputStream to recieve data from the client
    2. OutputStream to send data to the client
6. Read the client message and process the message
7. Send responce back to the client
8. Close the socket and stream after communication is done
9. Stop


#### TCP Client

1. Start
2. Import necessary modules
3. Create a socket object to connect to the server specific port number
4. Create Input and Output Streams from the socket
    1. InputStream to recieve message from the server
    2. OutputStream to send message to the server
5. Send message to server
6. Recieve the message from the Server
7. Display the server response to user
8. Close the socket and stream after communication is done
9. Stop


### RESULT

The output was obtained successfully