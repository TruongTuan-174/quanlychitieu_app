import tkinter as tk
from tkinter import ttk, messagebox
from database.database import Database

class IncomeExpenseWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Nhập thu nhập & chi tiêu")
        self.geometry("400x350")

        self.db = Database()

        # Danh mục
        tk.Label(self, text="Danh mục:").pack(pady=5)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self, textvariable=self.category_var)
        self.category_dropdown.pack(pady=5)
        self.load_categories()

        # Số tiền
        tk.Label(self, text="Số tiền (VNĐ):").pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)

        # Loại giao dịch (Thu nhập / Chi tiêu)
        tk.Label(self, text="Loại:").pack(pady=5)
        self.type_var = tk.StringVar(value="expense")
        ttk.Radiobutton(self, text="Chi tiêu", variable=self.type_var, value="expense").pack()
        ttk.Radiobutton(self, text="Thu nhập", variable=self.type_var, value="income").pack()

        # Ngày tháng
        tk.Label(self, text="Ngày tháng (YYYY-MM-DD):").pack(pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)

        # Nút lưu
        tk.Button(self, text="Lưu", command=self.save_transaction).pack(pady=10)

        # Danh sách giao dịch
        self.tree = ttk.Treeview(self, columns=("Danh mục", "Số tiền", "Loại", "Ngày"), show="headings")
        self.tree.heading("Danh mục", text="Danh mục")
        self.tree.heading("Số tiền", text="Số tiền")
        self.tree.heading("Loại", text="Loại")
        self.tree.heading("Ngày", text="Ngày")
        self.tree.pack(pady=10)
        self.load_transactions()

    def load_categories(self):
        """Lấy danh sách danh mục từ database"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM categories")
        categories = [row[0] for row in cursor.fetchall()]
        self.category_dropdown["values"] = categories

    def save_transaction(self):
        """Lưu giao dịch vào database"""
        category = self.category_var.get()
        amount = self.amount_entry.get()
        trans_type = self.type_var.get()
        date = self.date_entry.get()

        if not category or not amount or not date:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền phải là một số!")
            return

        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (category, amount, type, date) VALUES (?, ?, ?, ?)",
                       (category, amount, trans_type, date))
        conn.commit()
        messagebox.showinfo("Thành công", "Đã lưu giao dịch!")
        self.load_transactions()

    def load_transactions(self):
        """Hiển thị danh sách giao dịch"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT category, amount, type, date FROM transactions ORDER BY date DESC")
        transactions = cursor.fetchall()

        # Xóa dữ liệu cũ
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Thêm dữ liệu mới
        for trans in transactions:
            self.tree.insert("", "end", values=trans)