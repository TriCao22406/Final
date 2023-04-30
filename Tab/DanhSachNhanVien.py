import tkinter as tk
from tkinter import ttk
import csv

class DanhSachNhanVien:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x700')
        self.root.title("Employee Management System")

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        # Tạo thẻ trong widget Notebook
        the = tk.Frame(notebook)

        # Thêm thẻ vào widget Notebook
        notebook.add(the, text="Danh sách nhân viên")

        dsnv = tk.Listbox(root, height=100)
        dsnv.pack(padx=100, pady=100)

        with open("../database/ThongTinNhanVien.csv", "w", newline="") as nv_csv:
            write_csv = csv.writer(nv_csv)
            write_csv.writerow(["Mã NV", "Tên NV", "Đơn vị", "Phòng ban", "Chức danh", "Chức vụ", "Giới tính", "Ngày sinh", "Email", "SĐT"])


if __name__=="__main__":
       root = tk.Tk()
       obj= DanhSachNhanVien(root)
       root.mainloop()
