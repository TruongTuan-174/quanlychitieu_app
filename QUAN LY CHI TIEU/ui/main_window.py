import tkinter as tk
from tkinter import messagebox
from ui.income_expense import IncomeExpenseWindow
from ui.statistics import StatisticsWindow
from ui.charts import ChartsWindow

class MainWindow(tk.Tk):
    def __init__(self, username):
        super().__init__()

        self.title("Quản lý chi tiêu")
        self.geometry("400x300")

        # Tiêu đề chào mừng
        tk.Label(self, text=f"Chào {username}!", font=("Arial", 14)).pack(pady=10)

        # Nút nhập thu/chi
        tk.Button(self, text="Nhập thu nhập & chi tiêu", command=self.open_income_expense).pack(pady=5)
        
        # Nút thống kê chi tiêu
        tk.Button(self, text="Thống kê chi tiêu", command=self.open_statistics).pack(pady=5)
        
        # Nút vẽ biểu đồ tài chính
        tk.Button(self, text="Vẽ biểu đồ tài chính", command=self.open_charts).pack(pady=5)

        # Nút đăng xuất
        tk.Button(self, text="Đăng xuất", command=self.logout, fg="red").pack(pady=20)

    def open_income_expense(self):
        self.withdraw()  # Ẩn cửa sổ chính
        IncomeExpenseWindow(self)

    def open_statistics(self):
        self.withdraw()
        StatisticsWindow(self)

    def open_charts(self):
        self.withdraw()
        ChartsWindow(self)

    def logout(self):
        self.destroy()
        messagebox.showinfo("Đăng xuất", "Bạn đã đăng xuất thành công!")

# Kiểm tra chạy độc lập
if __name__ == "__main__":
    app = MainWindow("TestUser")
    app.mainloop()