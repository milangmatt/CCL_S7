## Experiment 2

# Client Server chat using TCP

### AIM

Write a python program to implement client-server communcation using software programming with TCP as transport layer protocol

### ALGORITHM

#### Client
1. Start
2. Import necessary modules
3. Define Server IP address and port number
4. Create TCP Socket using socket methods
5. Connect the client socket to server
6. Print instructions and information
7. Start a loop
    1. Read the client input
    2. Send message from client
    3. If 'exit', end the loop and exit chat
    4. Else recieve reply from the server
    5. Print server reply
    6. If server sends 'exit', break loop and exit chat
8. Close socket
9. Stop

#### Server
1. Start
2. Import necessary modules
3. Set IP Address and Port
4. Create and bind the TCP socket
5. Lister and accept connection
6. Initialize a Loop
    1. Recieve message
    2. If 'exit' or empty, break the loop and exit chat
    3. Else display message
    4. Take reply input
    5. Send reply
    6. if 'exit', break loop and exit chat
7. Close the connection
8. Stop

### RESULT

The output was obtained successfully