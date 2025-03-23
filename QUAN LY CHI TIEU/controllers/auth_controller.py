import sqlite3
from database.database import Database

class AuthController:
    def __init__(self):
        self.db = Database()
    
    def register_user(self, username, password):
        """Đăng ký tài khoản mới"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        # Kiểm tra xem username đã tồn tại chưa
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return "Tên đăng nhập đã tồn tại!"
        
        # Chèn tài khoản mới vào database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return "Đăng ký thành công!"
    
    def login_user(self, username, password):
        """Kiểm tra đăng nhập"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            return True  # Đăng nhập thành công
        return False  # Sai tài khoản hoặc mật khẩu