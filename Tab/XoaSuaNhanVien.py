import csv
import tkinter as tk
from tkinter import ttk

# def xoanv():
#     nv_xoa = view.selection()
#     if nv_xoa:
#         nv_in4 = view.item(nv_xoa)['values']
#         view.delete(nv_xoa)
#         a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
#         with open(a, mode='r', newline='') as file_csv:
#             reader = csv.reader(file_csv)
#             rows = list(reader)
#         for i, row in enumerate(rows):
#             if row[0] == nv_in4[0] and row[1] == str(nv_in4[1]):
#                 del rows[i]
#                 break
#         a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
#         with open(a, mode='w', newline='', encoding='utf-8') as file_csv:
#             csv_writer = csv.writer(file_csv)
#             csv_writer.writerows(rows)
#         file_csv.close()
#
# def capnhatnv():
#     nv_capnhat = view.selection()
#     if nv_capnhat:
#         nv_in4 = view.item(nv_capnhat)['values']
#         with open('employees.csv', mode='r', newline='', encoding='utf-8') as file_csv:
#             reader = csv.reader(file_csv)
#             for row in reader:
#                 if row[0] == nv_in4[0] and row[1] == str(nv_in4[1]):
#                     # Tạo dialog box
#                     dialog = tk.Toplevel()
#                     dialog.title("Cập nhật thông tin nhân viên")
#                     dialog.geometry("400x300")
#
#                     # Tạo các widget trong dialog box
#                     tk.Label(dialog, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
#                     tk.Label(dialog, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
#                     tk.Label(dialog, text="Email:").grid(row=2, column=0, padx=5, pady=5)
#
#                     fn_entry = tk.Entry(dialog, width=30)
#                     fn_entry.insert(0, row[0])
#                     fn_entry.grid(row=0, column=1, padx=5, pady=5)
#                     ln_entry = tk.Entry(dialog, width=30)
#                     ln_entry.insert(0, row[1])
#                     ln_entry.grid(row=1, column=1, padx=5, pady=5)
#                     email_entry = tk.Entry(dialog, width=30)
#                     email_entry.insert(0, row[2])
#                     email_entry.grid(row=2, column=1, padx=5, pady=5)
#
#                     # Tạo button để lưu thông tin nhân viên
#                     def save_changes():
#                         row[0] = fn_entry.get()
#                         row[1] = ln_entry.get()
#                         row[2] = email_entry.get()
#                         with open('employees.csv', mode='w', newline='') as file_csv:
#                             writer = csv.writer(file_csv)
#                             for r in reader:
#                                 if r[0] == row[0] and r[1] == row[1]:
#                                     writer.writerow(row)
#                                 else:
#                                     writer.writerow(r)
#                         messagebox.showinfo("Thông báo", "Thông tin nhân viên đã được cập nhật thành công!")
#                         dialog.destroy()
#                     tk.Button(dialog, text="Lưu", command=save_changes).grid(row=3, column=1, pady=10)
#                     tk.Button(dialog, text="Hủy", command=dialog.destroy).grid(row=3, column=2, pady=10)
#
# root = tk.Tk()
# root.title("Danh sách nhân viên")
# root.state("zoomed")
#
# xoa_button = tk.Button(root, text="Xóa", command=xoanv)
# xoa_button.pack(side="bottom", pady=5)
# capnhat_button = tk.Button(root, text="Cập nhật", command=capnhatnv)
# capnhat_button.pack(side="bottom", pady=5)
# view = ttk.Treeview(root)
#
#
# view["columns"] = ("First Name","Last Name","Email","Phone","Gender","Department","Job Title","Years Of Experience","Salary")
# view.column("#0", stretch= tk.NO, width=0)
# view.heading("#0", text="", anchor=tk.W)
# view.heading("First Name", text="First Name")
# view.heading("Last Name", text="Last Name")
# view.heading("Email", text="Email")
# view.heading("Phone", text="Phone")
# view.heading("Gender", text="Gender")
# view.heading("Department", text="Department")
# view.heading("Job Title", text="Job Title")
# view.heading("Years Of Experience", text="Years Of Experience")
# view.heading("Salary", text="Salary")
#
# with open('../database/employees.csv', newline="", mode='r', encoding='utf-8') as nv_csv:
#     csv_reader = csv.reader(nv_csv)
#     view["height"] = 70
#     for row in csv_reader:
#         view.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],))
# scrollbar_doc = ttk.Scrollbar(root, orient="vertical", command=view.yview)
# scrollbar_ngang = ttk.Scrollbar(root, orient="horizontal", command=view.xview)
# view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
# scrollbar_doc.pack(fill="y", side="right")
# view.configure()
# scrollbar_ngang.pack(fill="x", side="bottom")
# view.pack(fill="both", expand=True)
#
#
# a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
# with open(a, mode='r', newline='', encoding='utf-8') as file_csv:
#     reader = csv.reader(file_csv)
#     next(reader)
#     for row in reader:
#         view.insert("", tk.END, values=row)
#
# view.pack()
#
#
# root.mainloop()

class DanhSach(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.tree = ttk.Treeview(self)
        self.tree.pack()
        self.hienthidanhsach()
        self.pack()

    def xoanv(self):
        nv_xoa = self.view.selection()
        if nv_xoa:
            nv_in4 = self.view.item(nv_xoa)['values']
            self.view.delete(nv_xoa)
            a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
            with open(a, mode='r', newline='', encoding='utf-8') as file_csv:
                reader = csv.reader(file_csv)
                rows = list(reader)
            for i, row in enumerate(rows):
                if row[0] == nv_in4[0] and row[1] == str(nv_in4[1]):
                    del rows[i]
                    break
            a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
            with open(a, mode='w', newline='', encoding='utf-8') as file_csv:
                csv_writer = csv.writer(file_csv)
                csv_writer.writerows(rows)

    @classmethod
    def hienthidanhsach(cls):
        root = tk.Tk()
        root.title("Danh sách nhân viên")
        root.state("zoomed")
        view = ttk.Treeview(root)
        view["columns"] = (
            "First Name", "Last Name", "Email", "Phone", "Gender", "Department", "Job Title", "Years Of Experience",
            "Salary")
        view.column("#0", stretch=tk.NO, width=0)
        view.heading("#0", text="", anchor=tk.W)
        view.heading("First Name", text="First Name")
        view.heading("Last Name", text="Last Name")
        view.heading("Email", text="Email")
        view.heading("Phone", text="Phone")
        view.heading("Gender", text="Gender")
        view.heading("Department", text="Department")
        view.heading("Job Title", text="Job Title")
        view.heading("Years Of Experience", text="Years Of Experience")
        view.heading("Salary", text="Salary")

        with open('../database/employees.csv', newline="", mode='r', encoding='utf-8') as nv_csv:
            csv_reader = csv.reader(nv_csv)
            view["height"] = 50
            for row in csv_reader:
                view.insert(parent='', index='end',
                            values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],))
        scrollbar_doc = ttk.Scrollbar(root, orient="vertical", command=view.yview)
        scrollbar_ngang = ttk.Scrollbar(root, orient="horizontal", command=view.xview)
        view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
        scrollbar_doc.pack(fill="y", side="right")
        view.configure()
        scrollbar_ngang.pack(fill="x", side="bottom")
        view.pack(fill="both", expand=True)
        view.pack()
        root.mainloop()
