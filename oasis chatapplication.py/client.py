import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 55555

class ChatClient:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Chat Application")
        self.window.geometry("500x400")

        # CHAT DISPLAY (READ ONLY, NO FOCUS)
        self.chat_area = scrolledtext.ScrolledText(
            self.window,
            state='disabled',
            takefocus=0
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # MESSAGE ENTRY
        self.msg_entry = tk.Entry(self.window)
        self.msg_entry.pack(fill=tk.X, padx=10, pady=5)
        self.msg_entry.bind("<Return>", self.send_message)

        # SEND BUTTON
        self.send_button = tk.Button(
            self.window,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(pady=5)

        # SOCKET
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))

        self.username = simpledialog.askstring(
            "Username", "Enter your username:"
        )
        if not self.username:
            self.username = "User"

        self.socket.send(self.username.encode())

        threading.Thread(
            target=self.receive_messages,
            daemon=True
        ).start()

        # 🔥 CRITICAL FOCUS FIX
        self.window.after(200, self.force_focus)
        self.window.bind("<Button-1>", lambda e: self.force_focus())

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def force_focus(self):
        self.window.lift()
        self.window.focus_force()
        self.msg_entry.focus_set()
        self.msg_entry.icursor(tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode()
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message)
                self.chat_area.yview(tk.END)
                self.chat_area.config(state='disabled')
            except:
                break

    def send_message(self, event=None):
        msg = self.msg_entry.get()
        if msg.strip():
            self.socket.send(msg.encode())
            self.msg_entry.delete(0, tk.END)
            self.msg_entry.focus_set()

    def close(self):
        try:
            self.socket.close()
        except:
            pass
        self.window.destroy()

ChatClient()
