
# Client Server TCP Communication using Virtual Machine

## Overview

This project implements a **TCP-based Client–Server communication system** in Java.
It demonstrates the fundamentals of socket programming, where the server waits for client connections and both exchange messages in real time.

### Key Features

* Simple one-to-one chat communication between client and server
* Real-time message exchange using sockets
* Graceful connection termination when “exit” is entered
* Clean, readable, and well-structured Java implementation

---

## System Components

The system consists of **two main programs**:

1. **Server.java** – Creates a server socket and handles client connections
2. **Client.java** – Connects to the server and facilitates two-way communication

---

## How to Run

### 1. Open a terminal or command prompt.

### 2. Move to the directory containing both files:

```bash
cd EXP_7
```

### 3. Compile both Java programs:

```bash
javac Server.java Client.java
```

### 4. Run the server first:

```bash
java Server
```

### 5. In another terminal window, run the client:

```bash
java Client
```

### 6. Chat between client and server!

* Type messages in the client terminal.
* The server receives and responds to them.
* To end the session, type `exit` on the client side.

---

## Code Explanation

### 🖥 Server Implementation (Server.java)

1. **Server Socket Creation**

   ```java
   ServerSocket serverSocket = new ServerSocket(5000);
   ```

   * Initializes a server socket on port `5000`.
   * Waits for an incoming client connection.

2. **Accepting Client Connection**

   ```java
   Socket socket = serverSocket.accept();
   ```

   * Accepts the client request and establishes a socket connection.

3. **Input and Output Streams**

   ```java
   BufferedReader inputFromClient = new BufferedReader(new InputStreamReader(socket.getInputStream()));
   PrintWriter outputToClient = new PrintWriter(socket.getOutputStream(), true);
   ```

   * `inputFromClient` reads messages sent by the client.
   * `outputToClient` sends responses back to the client.

4. **Server Loop**

   ```java
   while ((clientMessage = inputFromClient.readLine()) != null) {
       System.out.println("Client: " + clientMessage);
       outputToClient.println("Server received: " + clientMessage);
   }
   ```

   * Continuously reads client messages and responds.
   * Ends chat if the client sends `"exit"`.

5. **Connection Closure**

   ```java
   inputFromClient.close();
   outputToClient.close();
   socket.close();
   serverSocket.close();
   ```

   * Closes all open connections and stops the server.

---

###  Client Implementation (Client.java)

1. **Socket Connection**

   ```java
   Socket socket = new Socket("localhost", 5000);
   ```

   * Connects to the server running on the same machine (localhost) at port `5000`.

2. **Stream Setup**

   ```java
   BufferedReader inputFromServer = new BufferedReader(new InputStreamReader(socket.getInputStream()));
   PrintWriter outputToServer = new PrintWriter(socket.getOutputStream(), true);
   ```

   * `inputFromServer` receives data from the server.
   * `outputToServer` sends data to the server.

3. **Client Chat Loop**

   ```java
   while (true) {
       clientMessage = userInput.readLine();
       if (clientMessage.equalsIgnoreCase("exit")) break;
       outputToServer.println(clientMessage);
       System.out.println("Server: " + inputFromServer.readLine());
   }
   ```

   * Reads user input, sends it to the server, and displays the server’s reply.
   * Ends when the user types `"exit"`.

4. **Cleanup**

   ```java
   inputFromServer.close();
   outputToServer.close();
   socket.close();
   ```

   * Closes all streams and sockets gracefully.

---

## Complete Source Code

### Client.java
```java
package EXP_7;

import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String hostName = "localhost";
        int port = 5000;

        try {
            // Connect to the server
            Socket socket = new Socket(hostName, port);
            System.out.println("Connected to server at " + hostName + ":" + port);

            // Create input and output streams
            BufferedReader inputFromServer = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter outputToServer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));

            String clientMessage;
            String serverMessage;

            System.out.println("Type your message (type 'exit' to quit):");

            // Chat loop
            while (true) {
                // Read input from client (keyboard)
                System.out.print("You: ");
                clientMessage = userInput.readLine();

                if (clientMessage == null || clientMessage.equalsIgnoreCase("exit")) {
                    System.out.println("Client quitting...");
                    break;
                }

                // Send message to server
                outputToServer.println(clientMessage);

                // Read server response
                serverMessage = inputFromServer.readLine();

                if (serverMessage == null) {
                    System.out.println("Server disconnected.");
                    break;
                }

                // Display server message
                System.out.println("Server: " + serverMessage);
            }

            // Close all connections
            inputFromServer.close();
            outputToServer.close();
            userInput.close();
            socket.close();
            System.out.println("Connection closed.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

```

### Server.java
```java
package EXP_7;

import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 5000;

        try {
            // Step 3: Create a server socket
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server started on port " + port);
            System.out.println("Waiting for client connection...");

            // Step 4: Wait for the client to connect
            Socket socket = serverSocket.accept();
            System.out.println("Client connected: " + socket.getInetAddress());

            // Step 5: Create Input and Output Streams
            BufferedReader inputFromClient = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter outputToClient = new PrintWriter(socket.getOutputStream(), true);

            String clientMessage;
            String serverResponse;

            // Step 6 & 7: Read from client and send response
            while ((clientMessage = inputFromClient.readLine()) != null) {
                System.out.println("Client: " + clientMessage);

                // Simple response logic
                serverResponse = "Server received: " + clientMessage;
                outputToClient.println(serverResponse);

                // End chat if client says exit
                if (clientMessage.equalsIgnoreCase("exit")) {
                    System.out.println("Client requested to quit. Closing connection...");
                    break;
                }
            }

            // Step 8: Close streams and sockets
            inputFromClient.close();
            outputToClient.close();
            socket.close();
            serverSocket.close();

            System.out.println("Server stopped.");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

```


