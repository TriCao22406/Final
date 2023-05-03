import csv
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Danh sách nhân viên")
root.state("zoomed")
view = ttk.Treeview()

view["columns"] = ("Họ và tên","Email","Số điện thoại","Giới tính","Bộ phận","Vị trí","Số năm kinh nghiệm","Lương")
view.column("#0", stretch= tk.NO, width=0)
view.heading("#0", text="", anchor=tk.W)
view.heading("Họ và tên", text="Họ và tên")
view.heading("Email", text="Email")
view.heading("Số điện thoại", text="Số điện thoại")
view.heading("Giới tính", text="Giới tính")
view.heading("Bộ phận", text="Bộ phận")
view.heading("Vị trí", text="Vị trí")
view.heading("Số năm kinh nghiệm", text="Số năm kinh nghiệm")
view.heading("Lương", text="Lương")

with open('../database/employees.csv', newline="", mode='r', encoding='utf-8') as nv_csv:
    csv_reader = csv.reader(nv_csv)
    view["height"] = 50
    for row in csv_reader:
        view.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],))
scrollbar_doc = ttk.Scrollbar(root, orient="vertical", command=view.yview)
scrollbar_ngang = ttk.Scrollbar(root, orient="horizontal", command=view.xview)
view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
scrollbar_doc.pack(fill="y", side="right")
view.configure()
scrollbar_ngang.pack(fill="x", side="bottom")
view.pack(fill="both", expand=True)


view.pack()
root.mainloop()
