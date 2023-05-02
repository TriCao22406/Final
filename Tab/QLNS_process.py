from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import  csv


class Nhanvien():
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,chucvu):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.gt = gt
      self.sdt = sdt
      self.email = email
      self.diachi = diachi
      self.hocvan = hocvan
      self.chucvu = chucvu

class  thongtinluong(Nhanvien):
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,chucvu,bophan,noilamviec,Bacluong,luongcoban,Donvitiente,Phucap,BHYT,BHXH,Trocap,luongthang13):
      super().__init__(manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,chucvu)
      self.bophan= bophan
      self.noilamviec= noilamviec
      self.bacluong= Bacluong
      self.luongcoban = luongcoban
      self.phucap= Phucap
      self.BHYT = BHYT
      self.BHXH = BHXH
      self.trocap= Trocap
      self.tiente= Donvitiente
      self.luongthang13 = luongthang13

class Window(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.pack()
        self.nhanvien = []

        self.label1 = tk.Label(self, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold",),justify=CENTER,fg="#DD0000")
        self.label1.grid(row=0, column=0, columnspan=4)

        tk.Label(self, text="MSNV:",bg="#66CCFF",fg="black",width =12).grid(row=1, column=0,pady=5,padx=5)
        self.manv_entry = tk.Entry(self)
        self.manv_entry.grid(row=1, column=1)

        tk.Label(self, text="Giới tính:",bg="#66CCFF",fg="black",width =12).grid(row=1, column=2,pady=5,padx=5)
        self.gioitinh_check = tk.StringVar()
        self.gt_options = ["Nam", "Nữ"]
        self.gt_combobox = ttk.Combobox(self, values=self.gt_options,textvariable=self.gioitinh_check)
        self.gt_combobox.grid(row=1, column=3)


        tk.Label(self, text="Tên nhân viên:",bg="#66CCFF",fg="black",width =12).grid(row=2, column=0,pady=5,padx=5)
        self.tennv_entry = tk.Entry(self)
        self.tennv_entry.grid(row=2, column=1)

        tk.Label(self, text="Học vấn:",bg="#66CCFF",fg="black",width =12).grid(row=2, column=2,pady=5,padx=5)
        self.hocvan_entry = tk.Entry(self)
        self.hocvan_entry.grid(row=2, column=3)

        tk.Label(self, text="Ngày sinh:",bg="#66CCFF",fg="black",width =12).grid(row=3, column=0,pady=5,padx=5)
        self.ngaysinh_entry = tk.Entry(self)
        self.ngaysinh_entry.grid(row=3, column=1)

        tk.Label(self, text="Số điện thoại:",bg="#66CCFF",fg="black",width =12).grid(row=3, column=2,pady=5,padx=5)
        self.sdt_entry = tk.Entry(self)
        self.sdt_entry.grid(row=3, column=3)

        tk.Label(self, text="Chức vụ:",bg="#66CCFF",fg="black",width =12).grid(row=4, column=0,pady=5,padx=5)
        self.chucvu_entry = tk.Entry(self)
        self.chucvu_entry.grid(row=4, column=1)

        tk.Label(self, text="Email:",bg="#66CCFF",fg="black",width =12).grid(row=4, column=2,pady=5,padx=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=3)

        tk.Label(self, text="Địa chỉ:",bg="#66CCFF",fg="black",width =12).grid(row=5, column=0,pady=5,padx=5)
        self.diachi_entry = tk.Entry(self)
        self.diachi_entry.grid(row=5, column=1)

        self.separator = ttk.Separator(self, orient="horizontal")
        self.separator.grid(row=6,column=0,padx=15,pady=10)

        tk.Label(self,text="Mức lương",font=("Times",13,"bold"),fg="#DD0000").grid(row=7,column=0)

        tk.Label(self,text="Bộ phận:",bg='#66CCFF',fg="black",width =12).grid(row=8,column=0,pady=5)
        self.bophan_entry =tk.Entry(self)
        self.bophan_entry.grid(row=8,column=1,pady=5)

        tk.Label(self, text="Phụ cấp:",bg='#66CCFF',fg="black",width =12).grid(row=8, column=2, pady=5)
        self.phucap_check = tk.BooleanVar()
        self.phucap = tk.Checkbutton(self,variable=self.phucap_check)
        self.phucap.place(x=350,y=240)

        tk.Label(self, text="BHXH:", bg='#66CCFF', fg="black", width=12).grid(row=8, column=3, pady=5)
        self.BHXH_check = tk.BooleanVar()
        self.BHXH = tk.Checkbutton(self,variable=self.BHXH_check)
        self.BHXH.place(x=500, y=240)

        tk.Label(self, text="Nơi làm việc:",bg='#66CCFF',fg="black",width =12).grid(row=9, column=0,pady=5)
        self.noilamviec_entry = tk.Entry(self)
        self.noilamviec_entry.grid(row=9, column=1)

        tk.Label(self, text="Trợ cấp:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=2, pady=5)
        self.trocap_check = tk.BooleanVar()
        self.trocap = tk.Checkbutton(self,variable=self.trocap_check)
        self.trocap.place(x=350, y=270)

        tk.Label(self, text="Lương tháng 13:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=3, pady=5)
        self.luong13_check = tk.BooleanVar()
        self.luong13= tk.Checkbutton(self,variable=self.luong13_check)
        self.luong13.place(x=500, y=270)

        tk.Label(self, text="Bậc lương:",bg='#66CCFF',fg="black",width =12).grid(row=10, column=0,pady=5)
        self.spinbox = tk.Spinbox(self,from_=0,to=12)
        self.spinbox.grid(row=10, column=1)

        tk.Label(self, text="BHYT:", bg='#66CCFF', fg="black", width=12).grid(row=10, column=2, pady=5)
        self.BHYT_check = tk.BooleanVar()
        self.BHYT = tk.Checkbutton(self,variable=self.BHYT_check)
        self.BHYT.place(x=350, y=300)

        tk.Label(self, text="Lương cơ bản:",bg='#66CCFF',fg="black",width =12).grid(row=11, column=0, pady=5)
        self.luong_entry = tk.Entry(self)
        self.luong_entry.grid(row=11, column=1)
        self.tiente_check = tk.StringVar()
        self.tiente_options = ["VNĐ","USD"]
        self.combobox = ttk.Combobox(self,values=self.tiente_options,textvariable=self.tiente_check)
        self.combobox.set("VNĐ")
        self.combobox.grid(row=11,column=2)

        #tạo 2 button lưu thông tin và thoát

        self.separator = ttk.Separator(self, orient="horizontal",)
        self.separator.grid(row=12, column=0, padx=30, pady=15)

        self.luu_button = tk.Button(self, text="Lưu thông tin",bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=220,y=390)

        self.thoat_button = tk.Button(self, text="Thoát",bg="#EEDC82", command=self.destroy)
        self.thoat_button.grid(row=13,column=3,columnspan=2,pady=10,padx=10)


    def themnv(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        ngaysinh = self.ngaysinh_entry.get()
        gt = self.gioitinh_check.get()
        sdt = self.sdt_entry.get()
        email = self.email_entry.get()
        diachi = self.diachi_entry.get()
        hocvan = self.hocvan_entry.get()
        chucvu = self.chucvu_entry.get()
        diachi = self.diachi_entry.get()
        bophan = self.bophan_entry.get()
        noilamviec = self.noilamviec_entry.get()
        Bacluong = self.spinbox.get()
        luongcoban = self.luong_entry.get()
        Donvitiente = self.tiente_check.get()
        Phucap = self.phucap_check.get()
        Trocap = self.trocap_check.get()
        BHYT = self.BHYT_check.get()
        BHXH = self.BHXH_check.get()
        luongthang13 = self.luong13_check.get()


        #tạo nhân viên mới
        nvm = thongtinluong(manv, tennv, ngaysinh, gt, sdt, email, diachi, hocvan, chucvu,bophan,noilamviec,Bacluong,luongcoban,Donvitiente,Phucap,Trocap,BHYT,BHXH,luongthang13)

        # kiểm tra sự trùng lặp
        for e in self.nhanvien:
            if e.manv == nvm.manv:
                self.show = messagebox.showerror("Lỗi","Nhân viên với mã {} đã tồn tại!".format(manv), parent = root)

                return

        # thêm nhân viên mới vào trong danh sách và trong file csv
        self.nhanvien.append(nvm)
        with open("../database/employees.csv", "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                nvm.manv,
                nvm.tennv,
                nvm.ngaysinh,
                nvm.gt,
                nvm.sdt,
                nvm.email,
                nvm.diachi,
                nvm.hocvan,
                nvm.chucvu,
                nvm.bophan,
                nvm.noilamviec,
                nvm.bacluong,
                nvm.luongcoban,
                nvm.tiente,
                nvm.phucap,
                nvm.trocap,
                nvm.BHYT,
                nvm.BHXH,
                nvm.luongthang13,

            ])
        self.show1 = messagebox.showinfo("Thành công","Thông tin nhân viên đã được lưu")





