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
