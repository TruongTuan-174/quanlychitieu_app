import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database.database import Database

class ChartsWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Biểu đồ tài chính")
        self.geometry("600x400")

        self.db = Database()

        # Lấy dữ liệu thu nhập & chi tiêu
        self.data = self.get_data()

        # Hiển thị biểu đồ
        self.create_chart()

    def get_data(self):
        """Lấy dữ liệu tổng thu nhập & chi tiêu theo tháng"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT strftime('%Y-%m', date) AS month, 
                   SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) AS total_income,
                   SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS total_expense
            FROM transactions
            GROUP BY month
            ORDER BY month;
        """)
        return cursor.fetchall()

    def create_chart(self):
        """Vẽ biểu đồ thu nhập & chi tiêu"""
        if not self.data:
            tk.Label(self, text="Không có dữ liệu để hiển thị!").pack(pady=20)
            return

        months = [row[0] for row in self.data]
        incomes = [row[1] for row in self.data]
        expenses = [row[2] for row in self.data]

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(months, incomes, marker='o', linestyle='-', color='green', label="Thu nhập")
        ax.plot(months, expenses, marker='o', linestyle='-', color='red', label="Chi tiêu")

        ax.set_title("Biểu đồ tài chính theo tháng")
        ax.set_xlabel("Tháng")
        ax.set_ylabel("Số tiền (VNĐ)")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()
        canvas.draw()