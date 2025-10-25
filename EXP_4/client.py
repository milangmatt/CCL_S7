import sys  
import socket  
import threading  
import tkinter as tk  
from tkinter import simpledialog, messagebox, scrolledtext  

HOST = "127.0.0.1"  # localhost address
PORT = 65433  # server port number

class ChatClient:  # main chat client class
    def __init__(self, root, nickname):  # initialize with root window and nickname
        self.root = root  # store root window
        self.nickname = nickname  # store user's nickname
        self.root.title(f"Chat - {nickname}")  # set window title

        self.txt = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)  # chat display area
        self.txt.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)  # pack chat display

        bottom = tk.Frame(root)  # frame for input controls
        bottom.pack(fill=tk.X, padx=6, pady=(0,6))  # pack input frame

        self.entry_var = tk.StringVar()  # variable for entry text
        self.entry = tk.Entry(bottom, textvariable=self.entry_var)  # input entry field
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,6))  # pack entry field
        self.entry.bind("<Return>", lambda e: self.send_message())  # bind enter key to send message

        tk.Button(bottom, text="Send", command=self.send_message).pack(side=tk.RIGHT)  # send button

        try:
            self.sock = socket.create_connection((HOST, PORT))  # create socket connection
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect: {e}")  # show error if connection fails
            root.destroy()  # close window
            return

        self.running = True  # flag to keep receiving messages
        threading.Thread(target=self._receive_loop, daemon=True).start()  # start receiving thread
        self.root.protocol("WM_DELETE_WINDOW", self.close)  # handle window close
        self.entry.focus()  # focus on entry field

    def _append(self, text):  # add text to chat display
        def _do():
            self.txt.configure(state=tk.NORMAL)  # enable text area
            self.txt.insert(tk.END, text + "\n")  # insert new message
            self.txt.see(tk.END)  # scroll to the end
            self.txt.configure(state=tk.DISABLED)  # disable text area
        self.root.after(0, _do)  # schedule the update

    def _format_and_show(self, raw, local=False):  # format and display messages
        if local:
            self._append(f"You: {raw}")  # show local message
            return
        if raw.startswith("<") and ">" in raw:  # check for formatted message
            end = raw.find(">")  # find end of nickname
            name = raw[1:end]  # extract nickname
            msg = raw[end+2:] if len(raw) > end+2 else ""  # extract message
            self._append(f"{name}: {msg}")  # display formatted message
        else:
            self._append(raw)  # display raw message

    def send_message(self):  # handle message sending
        text = self.entry_var.get().strip()  # get and strip entry text
        if not text:  # if empty, do nothing
            return
        payload = f"<{self.nickname}> {text}".encode()  # format message for sending
        try:
            self.sock.sendall(payload)  # send message
        except Exception:
            self._append("System: Failed to send message (connection issue).")  # error message
            return
        self._format_and_show(text, local=True)  # show sent message
        self.entry_var.set("")  # clear entry field

    def _receive_loop(self):  # receive messages in background
        try:
            while self.running:  # loop while running
                try:
                    data = self.sock.recv(4096)  # receive data
                except OSError:
                    break  # exit on error
                if not data:  # if no data, exit
                    break
                try:
                    msg = data.decode()  # decode message
                except Exception:
                    continue  # skip on error
                self._format_and_show(msg)  # format and show received message
        finally:
            self._append("System: Disconnected from server.")  # notify disconnection

    def close(self):  # cleanup and close client
        self.running = False  # stop receiving messages
        try:
            self.sock.shutdown(socket.SHUT_RDWR)  # shutdown socket
        except Exception:
            pass  # ignore errors
        try:
            self.sock.close()  # close socket
        except Exception:
            pass  # ignore errors
        self.root.destroy()  # close window

if __name__ == "__main__":  # main execution
    root = tk.Tk()  # create main window
    root.withdraw()  # hide window initially
    nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=root)  # ask for nickname
    if not nickname or not nickname.strip():  # check for valid nickname
        root.destroy()  # close window
        sys.exit()  # exit program
    nickname = nickname.strip()  # strip nickname
    root.deiconify()  # show window
    ChatClient(root, nickname)  # create chat client
    root.mainloop()  # start main loop
