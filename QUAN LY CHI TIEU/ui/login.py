import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("300x200")
        
        # Nhãn và ô nhập tên đăng nhập
        tk.Label(root, text="Tên đăng nhập:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        # Nhãn và ô nhập mật khẩu
        tk.Label(root, text="Mật khẩu:").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        # Nút đăng nhập và đăng ký
        tk.Button(root, text="Đăng nhập", command=self.login).pack()
        tk.Button(root, text="Đăng ký", command=self.register).pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123":  # Placeholder, sau sẽ kết nối database
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
        
    def register(self):
        messagebox.showinfo("Thông báo", "Chức năng đăng ký chưa triển khai")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
