import tkinter as tk
from tkinter import messagebox

VALID_USER = "user"
VALID_PASS = "pass123"

def attempt_login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == VALID_USER and password == VALID_PASS:
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid username or password")

root = tk.Tk()
root.title("Login Example")

tk.Label(root, text="Username").grid(row=0, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1)

login_btn = tk.Button(root, text="Login", command=attempt_login)
login_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
