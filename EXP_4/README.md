# Multiuser Chat server with TCP using GUI

This project implements a multiuser chat application using Python's socket programming and tkinter GUI library. Key features include:

- TCP-based client-server architecture for reliable communication
- Graphical user interface built with tkinter
- Support for multiple concurrent client connections
- Real-time message transmission between clients
- Simple and intuitive chat interface

The system consists of two main components:
1. A server program that handles client connections and message routing
2. A client application with a GUI for sending and receiving messages

### How to run

1. Open a terminal.
2. Start the server:
    ```bash
    python3 server.py
    ```
3. In a separate terminal, start the client:
    ```bash
    python3 client.py
    ```

Notes:
- If `python3` is not available on Windows, use `python` or `py -3`.
- Keep both terminals open; type your messages in the client terminal.

## Code Explanation

### Server Implementation (server.py)
The server implementation consists of the following key components:

1. **Socket Setup**
    ```python
    HOST = '127.0.0.1'
    PORT = 65433
    clients = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
    ```
    - Uses TCP/IP with `socket.AF_INET` and `socket.SOCK_STREAM`
    - Binds to localhost (127.0.0.1) on port 65433
    - Maintains a list of connected clients

2. **Client Handling**
    ```python
    def handle_client(conn, addr):
        print(f"[+] {addr} connected.")
        while True:
            try:
                msg = conn.recv(1024)
                if not msg: break
                broadcast(msg, conn)
            except:
                break
    ```
    - `handle_client()` function manages individual client connections
    - Receives messages in a continuous loop
    - Removes clients when they disconnect
    - Thread-based handling for concurrent connections

3. **Broadcasting**
    ```python
    def broadcast(msg, sender):
        for client in clients:
            if client != sender:
                client.sendall(msg)
    ```
    - `broadcast()` function sends messages to all connected clients
    - Excludes the sender from receiving their own message
    - Handles message distribution in real-time

### Client Implementation (client.py)
The client uses tkinter for the GUI and includes these components:

1. **Main Window Elements**
    ```python
    self.txt = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    self.txt.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

    bottom = tk.Frame(root)
    bottom.pack(fill=tk.X, padx=6, pady=(0,6))

    self.entry = tk.Entry(bottom, textvariable=self.entry_var)
    tk.Button(bottom, text="Send", command=self.send_message)
    ```
    - **ScrolledText Widget (`self.txt`)**: 
        - Displays chat messages.
        - `wrap=tk.WORD`: Wraps text at word boundaries.
        - `state=tk.DISABLED`: Prevents user editing.
        - `pack(fill=tk.BOTH, expand=True, padx=6, pady=6)`: Expands to fill available space with padding.
    
    - **Frame (`bottom`)**: 
        - Organizes layout for input elements.
        - `pack(fill=tk.X, padx=6, pady=(0,6))`: Fills horizontally with padding.

    - **Entry Widget (`self.entry`)**: 
        - Input field for user messages.
        - `textvariable=self.entry_var`: Binds to a StringVar for dynamic updates.

    - **Button**: 
        - Triggers message sending.
        - `command=self.send_message`: Calls the send_message method on click.

2. **Welcome Window Elements**
    ```python
    if __name__ == "__main__":
        root = tk.Tk()
        root.withdraw()
        nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=root)
    ```
    - **Tkinter Root Window (`root`)**: 
        - Main application window.
        - `withdraw()`: Hides the window until nickname is set.
    
    - **SimpleDialog**: 
        - Prompts user for a nickname.
        - `askstring("Nickname", "Enter your nickname:", parent=root)`: Displays a dialog with a title and message.

3. **Client Features**
    ```python
    def _format_and_show(self, raw, local=False):
        if local:
            self._append(f"You: {raw}")
            return
        if raw.startswith("<") and ">" in raw:
            end = raw.find(">")
            name = raw[1:end]
            msg = raw[end+2:]
    ```
    - **Message Formatting**: 
        - Identifies sender and formats messages.
        - `local`: Indicates if the message is sent by the user.
        - Uses string manipulation to extract sender name and message content.

4. **Threading**
    ```python
    self.running = True
    threading.Thread(target=self._receive_loop, daemon=True).start()
    ```
    - **Threading for Message Reception**: 
        - Creates a separate thread for receiving messages.
        - `daemon=True`: Ensures the thread exits when the main program does.

5. **Network Operations**
    ```python
    self.sock = socket.create_connection((HOST, PORT))
    ```
    - **Socket Connection**: 
        - Establishes a TCP connection to the server.
        - `create_connection((HOST, PORT))`: Takes a tuple of host and port for connection.
        - Handles message encoding and decoding for communication.

6. **Graceful Connection Closure**
    - Ensures proper shutdown of the socket connection when the client closes.
    - Monitors connection status and handles errors gracefully.

This detailed breakdown provides a comprehensive understanding of the client implementation and its GUI components.


## Complete Source Code

### client.py
```python
import sys
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

HOST = "127.0.0.1"
PORT = 65433

class ChatClient:
    def __init__(self, root, nickname):
        self.root = root
        self.nickname = nickname
        self.root.title(f"Chat - {nickname}")

        self.txt = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
        self.txt.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        bottom = tk.Frame(root)
        bottom.pack(fill=tk.X, padx=6, pady=(0,6))

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(bottom, textvariable=self.entry_var)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,6))
        self.entry.bind("<Return>", lambda e: self.send_message())

        tk.Button(bottom, text="Send", command=self.send_message).pack(side=tk.RIGHT)

        try:
            self.sock = socket.create_connection((HOST, PORT))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect: {e}")
            root.destroy()
            return

        self.running = True
        threading.Thread(target=self._receive_loop, daemon=True).start()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.entry.focus()

    def _append(self, text):
        def _do():
            self.txt.configure(state=tk.NORMAL)
            self.txt.insert(tk.END, text + "\n")
            self.txt.see(tk.END)
            self.txt.configure(state=tk.DISABLED)
        self.root.after(0, _do)

    def _format_and_show(self, raw, local=False):
        if local:
            self._append(f"You: {raw}")
            return
        if raw.startswith("<") and ">" in raw:
            end = raw.find(">")
            name = raw[1:end]
            msg = raw[end+2:] if len(raw) > end+2 else ""
            self._append(f"{name}: {msg}")
        else:
            self._append(raw)

    def send_message(self):
        text = self.entry_var.get().strip()
        if not text:
            return
        payload = f"<{self.nickname}> {text}".encode()
        try:
            self.sock.sendall(payload)
        except Exception:
            self._append("System: Failed to send message (connection issue).")
            return
        self._format_and_show(text, local=True)
        self.entry_var.set("")

    def _receive_loop(self):
        try:
            while self.running:
                try:
                    data = self.sock.recv(4096)
                except OSError:
                    break
                if not data:
                    break
                try:
                    msg = data.decode()
                except Exception:
                    continue
                self._format_and_show(msg)
        finally:
            self._append("System: Disconnected from server.")

    def close(self):
        self.running = False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        try:
            self.sock.close()
        except Exception:
            pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=root)
    if not nickname or not nickname.strip():
        root.destroy()
        sys.exit()
    nickname = nickname.strip()
    root.deiconify()
    ChatClient(root, nickname)
    root.mainloop()

```

### server.py
```python

import socket
import threading

HOST = '127.0.0.1'
PORT = 65433
clients = []

def handle_client(conn, addr):
    print(f"[+] {addr} connected.")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            broadcast(msg, conn)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"[-] {addr} disconnected.")

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.sendall(msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
```


