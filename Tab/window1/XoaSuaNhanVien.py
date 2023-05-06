import csv
import tkinter as tk
from tkinter import ttk, messagebox
from Tab.window1.QLNS_process import Nhanvien

class DanhSach(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
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
            for i, row in enumerate(rows[1:]):
                if int(row[0]) == int(nv_in4[0]) and str(row[1]) == str(nv_in4[1]):
                    del rows[i+1]
                    break
            a = r"..\Final\database\employees.csv"
            with open(a, mode='w', newline='', encoding='utf-8') as file_csv:
                csv_writer = csv.writer(file_csv)
                csv_writer.writerows(rows)

    def capnhatnv(self):
        nv_capnhat = self.view.selection()
        print(nv_capnhat)
        if nv_capnhat:
            popup = tk.Toplevel()
            popup.title("Cập nhật thông tin nhân viên")
            popup.geometry('500x500+100+100')
            nv_in4 = self.view.item(nv_capnhat)['values']
            # Hiển thị giao diện để người dùng cập nhật thông tin
            tk.Label(popup, text="").grid(row=0, column=0, pady=5)
            ten = tk.Label(popup, text="Cập nhật thông tin", font=("Times", 16, "bold"), fg="#DD0000")
            ten.grid(row=1, column=0, columnspan=2)
            tk.Label(popup, text="").grid(row=2, column=0, pady=5)

            tk.Label(popup, text="Mã nhân viên").grid(row=3, column=0, padx=30, pady=5)
            first_name_entry = tk.Entry(popup, width=45)
            first_name_entry.insert(0, nv_in4[0])
            first_name_entry.grid(row=3, column=1)

            tk.Label(popup, text="Tên nhân viên").grid(row=4, column=0, padx=30, pady=5)
            last_name_entry = tk.Entry(popup, width=45)
            last_name_entry.insert(0, nv_in4[1])
            last_name_entry.grid(row=4, column=1)

            tk.Label(popup, text="Ngày sinh").grid(row=5, column=0, padx=30, pady=5)
            ns_entry = tk.Entry(popup, width=45)
            ns_entry.insert(0, nv_in4[2])
            ns_entry.grid(row=5, column=1)

            tk.Label(popup, text="Email").grid(row=6, column=0, padx=30, pady=5)
            g_entry = tk.Entry(popup, width=45)
            g_entry.insert(0, nv_in4[3])
            g_entry.grid(row=6, column=1)

            tk.Label(popup, text="Số điện thoại").grid(row=7, column=0, padx=30, pady=5)
            phone_entry = tk.Entry(popup, width=45)
            phone_entry.insert(0, nv_in4[4])
            phone_entry.grid(row=7, column=1)

            tk.Label(popup, text="Giới tính").grid(row=8, column=0, padx=30, pady=5)
            e_entry = tk.Entry(popup, width=45)
            e_entry.insert(0, nv_in4[5])
            e_entry.grid(row=8, column=1)

            tk.Label(popup, text="Bộ phận").grid(row=9, column=0, padx=30, pady=5)
            b_entry = tk.Entry(popup, width=45)
            b_entry.insert(0, nv_in4[6])
            b_entry.grid(row=9, column=1)

            tk.Label(popup, text="Chức vụ").grid(row=10, column=0, padx=30, pady=5)
            y_entry = tk.Entry(popup, width=45)
            y_entry.insert(0, nv_in4[7])
            y_entry.grid(row=10, column=1)

            tk.Label(popup, text="Kinh nghiệm").grid(row=11, column=0, padx=30, pady=5)
            s_entry = tk.Entry(popup, width=45)
            s_entry.insert(0, nv_in4[8])
            s_entry.grid(row=11, column=1)

            tk.Label(popup, text="Lương").grid(row=12, column=0, padx=30, pady=5)
            k_entry = tk.Entry(popup, width=45)
            k_entry.insert(0, nv_in4[9])
            k_entry.grid(row=12, column=1)

            popup.grid_columnconfigure(0, minsize=30)

            def capnhat_thongtin():
                # Lưu thông tin đã được cập nhật vào file CSV
                a = r"..\Final\database\employees.csv"
                with open(a, mode='r', newline='', encoding='utf-8') as file_csv:
                    reader = csv.reader(file_csv)
                    rows = list(reader)
                for i, row in enumerate(rows[1:]):
                    if int(row[0]) == int(nv_in4[0]) and str(row[1]) == str(nv_in4[1]):
                        i = i +1
                        rows[i][0] = first_name_entry.get()
                        rows[i][1] = last_name_entry.get()
                        rows[i][2] = ns_entry.get()
                        rows[i][3] = g_entry.get()
                        rows[i][4] = phone_entry.get()
                        rows[i][5] = e_entry.get()
                        rows[i][6] = b_entry.get()
                        rows[i][7] = y_entry.get()
                        rows[i][8] = s_entry.get()
                        rows[i][9] = k_entry.get()
                        break
                with open(a, mode='w', newline='', encoding='utf-8') as file_csv:
                    csv_writer = csv.writer(file_csv)
                    csv_writer.writerows(rows)
                self.view.item(nv_capnhat, values=(
                rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7], rows[i][8], rows[i][9]))
                messagebox.showinfo("Cập nhật", "Hoàn tất cập nhật!")

            tk.Button(popup, text="Lưu thông tin", bg="yellow", fg="red", command=capnhat_thongtin).grid(row=13, column=1, pady=5)

    def tailaitrang(self):
        # Xóa tất cả các dòng cũ trong Treeview
        for i in self.view.get_children():
            self.view.delete(i)

        # Đọc lại file CSV và hiển thị danh sách mới
        a = r"..\Final\database\employees.csv"
        with open(a, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                self.view.insert('', 'end', values=row)

    def hienthidanhsach(self):
        view = ttk.Treeview(self)
        self.view=view
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(side="bottom", pady=5)
        self.xoa_button = tk.Button(self.button_frame, text="Xóa", command=self.xoanv)
        self.xoa_button.pack(side="left", pady=5, padx=5)
        self.capnhat_button = tk.Button(self.button_frame, text="Cập nhật", command=self.capnhatnv)
        self.capnhat_button.pack(side="right", pady=5, padx=5)
        self.tai_button = tk.Button(self.button_frame, text="Tải lại trang", command=self.tailaitrang)
        self.tai_button.pack(side="right", pady=5, padx=5)
        view["columns"] = ("Mã nhân viên","Tên nhân viên", "Ngày sinh", "Email", "Số điện thoại", "Giới tính", "Bộ phận", "Chức vụ", "Kinh nghiệm", "Lương")
        view.column("#0", stretch=tk.NO, width=0)
        view.heading("#0", text="", anchor=tk.W)
        view.heading("Mã nhân viên", text="Mã nhân viên")
        view.heading("Tên nhân viên", text="Tên nhân viên")
        view.heading("Ngày sinh", text="Ngày sinh")
        view.heading("Email", text="Email")
        view.heading("Số điện thoại", text="Số điện thoại")
        view.heading("Giới tính", text="Giới tính")
        view.heading("Bộ phận", text="Bộ phận")
        view.heading("Chức vụ", text="Chức vụ")
        view.heading("Kinh nghiệm", text="Kinh nghiệm")
        view.heading("Lương", text="Lương")


        with open(r'..\Final\database\employees.csv', newline="", mode='r', encoding='utf-8') as nv_csv:
            csv_reader = csv.reader(nv_csv)
            csv_reader = list(csv_reader)
            view["height"] = 50
            for row in csv_reader[1:]:
                view.insert(parent='', index='end',values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        scrollbar_doc = ttk.Scrollbar(self, orient="vertical", command=view.yview)
        scrollbar_ngang = ttk.Scrollbar(self, orient="horizontal", command=view.xview)
        view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
        scrollbar_doc.pack(fill="y", side="right")
        view.configure()
        scrollbar_ngang.pack(fill="x", side="bottom")
        view.pack(fill="both", expand=True)
        view.pack()