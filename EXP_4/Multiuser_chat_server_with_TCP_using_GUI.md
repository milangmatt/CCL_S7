## Experiment 4

#  Multiuser Chat server with TCP using GUI

### AIM

Write a python program to implement multiuser chat service with TCP as transport layer protocol using GUI.

### ALGORITHM

#### Server
1. Start
2. Import necessary modules
3. Create a TCP socket and bind it to the host IP and port number
4. Listen for incoming connections
5. Initialise a list for connected client sockets
6. Start a loop
    1. Accept client connection
    2. Add the client to the list
    3. Start a thread to handle message from the client
7. Inside the thread
    1. Continously recieve messages from the client
    2. Broadcast each message to all other clients
    3. If the client disconnects, remove if from the list
8. Repeat Until the server is stopped
9. Close all connections
10. Stop

#### Client
1. Start
2. Import necessary modules
3. Ask the user for nickname in a welcome dialogue box
4. Create a TCP socket and connect to the server using its port number
5. Launch a thread to
    1. Continously recieve messages from the server
    2. Display the message in the predesigned GUI with textboxes, entry field and send button
6. On user input, prepend the nickname with the message and send the mesage to the server through the socket
7. Display sent messages locally for immediate feedback
8. Keep updating the chat area as messages are recieved
9. Close the connection
10. Stop

### RESULT

The output was obtained successfully