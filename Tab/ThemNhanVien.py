from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x700")
label1 = tk.Label(root, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20, "bold",), justify=CENTER, fg="#DD0000")
label1.grid(row=0, column=0, columnspan=4)


class nhanvien:
    dsnv = []

    def __init__(self):
        self.manv = manv_entry.get()
        self.tennv = tennv_entry.get()
        self.gioitinh = gt_combobox.get()
        self.hocvan = hocvan_entry.get()
        self.ngaysinh = ngaysinh_entry.get()
        self.dienthoai = sdt_entry.get()
        self.email = email_entry.get()
        self.diachi = diachi_entry.get()
        self.bophan = bophan_entry.get()
        self.phucap = phu_cap.get()
        self.BHXH = bhxh.get()
        self.noilamviec = noilamviec_entry.get()
        self.trocap = tro_cap.get()
        self.luongthang13 = luong_thang13.get()
        self.bacluong = spinbox.get()
        self.BHYT = bhyt.get()
        self.luongcoban = luong_entry.get()
        self.loaitiente = combobox.get()
        nhanvien.themnv(self)

    @classmethod
    def timnv(cls, manv):
        for i in range(len(cls.dsnv)):
            if manv == cls.dsnv[i].manv:  # tìm thấy
                return {"idx": i, "inf": cls.dsnv[i]}
        return -1

    @classmethod
    def themnv(cls, nv):
        if cls.timnv(nv.manv) == -1:
            cls.dsnv.append(nv)
            messagebox.showinfo("tk", "Thêm thành công")
            return True
        else:
            messagebox.showerror("Lỗi", "Nhân viên bị trùng id")
        return False


    @classmethod
    def hienthinv(cls):
        root2 = tk.Tk()
        root2.title("Hiển thị nhân viên")
        root2.state("zoomed")

        def create_tree_widget():
            columns = ('Mã nhân viên','Tên nhân viên','Giới tính ', 'Học vấn' , 'Ngày sinh:' , 'Điện thoại:', 'email:', 'địa chỉ:' ,'bộ phận: ','phụ cấp: ','BHXH:','Nơi làm việc ','Trợ cấp: ','Lương tháng 13: ','Bậc lương: ','BHYT', "Lương cơ bản",'loại tiền tệ')
            tree = ttk.Treeview(root2, columns=columns, show='headings')

            tree.heading('Mã nhân viên', text='Mã nhân viên')
            tree.heading('Tên nhân viên', text='Tên nhân viên')
            tree.heading('Giới tính ', text='Giới tính ')
            tree.heading('Học vấn', text='Học vấn')
            tree.heading('Ngày sinh:', text='Ngày sinh:')
            tree.heading('Điện thoại:', text='Điện thoại:')
            tree.heading('email:', text='email:')
            tree.heading('bộ phận: ', text='bộ phận: ')
            tree.heading('phụ cấp: ', text='phụ cấp: ')
            tree.heading('BHXH:', text='BHXH:')
            tree.heading('Nơi làm việc ', text='Nơi làm việc ')
            tree.heading('Trợ cấp: ', text='Trợ cấp: ')
            tree.heading('Lương tháng 13: ', text='Lương tháng 13: ')
            tree.heading('Bậc lương: ', text='Bậc lương: ')
            tree.heading('BHYT', text='BHYT')
            tree.heading("Lương cơ bản", text="Lương cơ bản")
            tree.heading('loại tiền tệ', text='loại tiền tệ')


            scrollbar_doc = Scrollbar(root2)
            scrollbar_doc.pack(side=RIGHT, fill=Y)

            tree.configure(yscrollcommand=scrollbar_doc.set)
            scrollbar_ngang = Scrollbar(root2)
            scrollbar_ngang.pack(side=BOTTOM, fill=X)

            tree.configure(xscrollcommand=scrollbar_ngang.set)
            contact = []
            for nv in cls.dsnv:
                contact.append(
                    [nv.manv, nv.tennv, nv.gioitinh, nv.hocvan, nv.ngaysinh, nv.dienthoai, nv.email, nv.bophan,
                     nv.phucap, nv.BHXH, nv.noilamviec, nv.trocap, nv.luongthang13, nv.bacluong, nv.BHYT, nv.luongcoban,
                     nv.loaitiente])
            for nv1 in contact:
                tree.insert('', tk.END, values=nv1)
            tree.pack(side=LEFT, fill=BOTH)
            scrollbar_doc.config(command=tree.yview)
            scrollbar_ngang.config(command=tree.xview)

        create_tree_widget()

        root2.mainloop()


tk.Label(root, text="MSNV:", bg="#66CCFF", fg="black", width=12).grid(row=1, column=0, pady=5, padx=5)
manv_entry = tk.Entry(root)
manv_entry.grid(row=1, column=1)

tk.Label(root, text="Giới tính:", bg="#66CCFF", fg="black", width=12).grid(row=1, column=2, pady=5, padx=5)
gt_combobox = ttk.Combobox(root, values=["Nam", "Nữ"], )
gt_combobox.set("Nam")
gt_combobox.grid(row=1, column=3)

tk.Label(root, text="Tên nhân viên:", bg="#66CCFF", fg="black", width=12).grid(row=2, column=0, pady=5, padx=5)
tennv_entry = tk.Entry(root)
tennv_entry.grid(row=2, column=1)

tk.Label(root, text="Học vấn:", bg="#66CCFF", fg="black", width=12).grid(row=2, column=2, pady=5, padx=5)
hocvan_entry = tk.Entry(root)
hocvan_entry.grid(row=2, column=3)

tk.Label(root, text="Ngày sinh:", bg="#66CCFF", fg="black", width=12).grid(row=3, column=0, pady=5, padx=5)
ngaysinh_entry = tk.Entry(root)
ngaysinh_entry.grid(row=3, column=1)

tk.Label(root, text="Số điện thoại:", bg="#66CCFF", fg="black", width=12).grid(row=3, column=2, pady=5, padx=5)
sdt_entry = tk.Entry(root)
sdt_entry.grid(row=3, column=3)

tk.Label(root, text="Chức vụ:", bg="#66CCFF", fg="black", width=12).grid(row=4, column=0, pady=5, padx=5)
chucvu_entry = tk.Entry(root)
chucvu_entry.grid(row=4, column=1)

tk.Label(root, text="Email:", bg="#66CCFF", fg="black", width=12).grid(row=4, column=2, pady=5, padx=5)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=3)

tk.Label(root, text="Địa chỉ:", bg="#66CCFF", fg="black", width=12).grid(row=5, column=0, pady=5, padx=5)
diachi_entry = tk.Entry()
diachi_entry.grid(row=5, column=1)

separator = ttk.Separator(root, orient="horizontal")
separator.grid(row=6, column=0, padx=15, pady=10)

tk.Label(root, text="Mức lương", font=("Times", 13, "bold"), fg="#DD0000").grid(row=7, column=0)
tk.Label(root, text="Bộ phận:", bg='#66CCFF', fg="black", width=12).grid(row=8, column=0, pady=5)
bophan_entry = tk.Entry(root)
bophan_entry.grid(row=8, column=1, pady=5)
phu_cap = StringVar()
tk.Label(root, text="Phụ cấp:", bg='#66CCFF', fg="black", width=12).grid(row=8, column=2, pady=5)
phucap = tk.Checkbutton(root, variable=phu_cap, onvalue='có', offvalue='không')
phucap.place(x=350, y=240)
bhxh = StringVar()
tk.Label(root, text="BHXH:", bg='#66CCFF', fg="black", width=12).grid(row=8, column=3, pady=5)
BHXH = tk.Checkbutton(root, variable=bhxh, onvalue='có', offvalue='không')
BHXH.place(x=500, y=240)
tk.Label(root, text="Nơi làm việc:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=0, pady=5)
noilamviec_entry = tk.Entry(root)
noilamviec_entry.grid(row=9, column=1)
tro_cap = StringVar()
tk.Label(root, text="Trợ cấp:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=2, pady=5)
trocap = tk.Checkbutton(root, variable=tro_cap, onvalue='có', offvalue='không')
trocap.place(x=350, y=270)
luong_thang13 = StringVar()
tk.Label(root, text="Lương tháng 13:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=3, pady=5)
luong13 = tk.Checkbutton(root, variable=luong_thang13, onvalue='có', offvalue='không')
luong13.place(x=500, y=270)

tk.Label(root, text="Bậc lương:", bg='#66CCFF', fg="black", width=12).grid(row=10, column=0, pady=5)
spinbox = tk.Spinbox(root, from_=0, to=12)
spinbox.grid(row=10, column=1)
bhyt = StringVar()
tk.Label(root, text="BHYT:", bg='#66CCFF', fg="black", width=12).grid(row=10, column=2, pady=5)
BHYT = tk.Checkbutton(root, variable=bhyt, onvalue='có', offvalue='không')
BHYT.place(x=350, y=300)

tk.Label(root, text="Lương cơ bản:", bg='#66CCFF', fg="black", width=12).grid(row=11, column=0, pady=5)
luong_entry = tk.Entry(root)
luong_entry.grid(row=11, column=1)
combobox = ttk.Combobox(root, values=["VNĐ", "USD"])
combobox.set("VNĐ")
combobox.grid(row=11, column=2)

# tạo 2 button lưu thông tin và thoát

separator = ttk.Separator(root, orient="horizontal", )
separator.grid(row=12, column=0, padx=30, pady=15)

luu_button = tk.Button(root, text="Lưu thông tin", bg="#FF6A6A", command=nhanvien)
luu_button.place(x=20, y=390)
hienthi_button = tk.Button(root, text='Hiển thị thông tin', bg='#FF6A6A', command=nhanvien.hienthinv)
hienthi_button.place(x=100, y=390)

thoat_button = tk.Button(root, text="Thoát", bg="#EEDC82", command=root.destroy)
thoat_button.grid(row=13, column=3, columnspan=2, pady=10, padx=10)
root.mainloop()
