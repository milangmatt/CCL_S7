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
