from tkinter import *
import tkinter as tk
from tkinter import ttk
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
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan,chucvu,bophan,noilamviec,Bacluong,luongcoban,Donvitiente,Phucap,BHYT,BHXH,Trocap,Luongthang13):
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
      self.luongthang13 = Luongthang13

class Window(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.pack()

        self.label1 = tk.Label(self, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold",),justify=CENTER,fg="#DD0000")
        self.label1.grid(row=0, column=0, columnspan=4)

        tk.Label(self, text="MSNV:",bg="#66CCFF",fg="black",width =12).grid(row=1, column=0,pady=5,padx=5)
        self.manv_entry = tk.Entry(self)
        self.manv_entry.grid(row=1, column=1)

        tk.Label(self, text="Giới tính:",bg="#66CCFF",fg="black",width =12).grid(row=1, column=2,pady=5,padx=5)
        self.gt_combobox = ttk.Combobox(self, values=["Nam", "Nữ"], )
        self.gt_combobox.set("Nam")
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
        self.phucap = tk.Checkbutton(self)
        self.phucap.place(x=350,y=240)

        tk.Label(self, text="BHXH:", bg='#66CCFF', fg="black", width=12).grid(row=8, column=3, pady=5)
        self.BHXH = tk.Checkbutton(self)
        self.BHXH.place(x=500, y=240)

        tk.Label(self, text="Nơi làm việc:",bg='#66CCFF',fg="black",width =12).grid(row=9, column=0,pady=5)
        self.noilamviec_entry = tk.Entry(self)
        self.noilamviec_entry.grid(row=9, column=1)

        tk.Label(self, text="Trợ cấp:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=2, pady=5)
        self.trocap = tk.Checkbutton(self)
        self.trocap.place(x=350, y=270)

        tk.Label(self, text="Lương tháng 13:", bg='#66CCFF', fg="black", width=12).grid(row=9, column=3, pady=5)
        self.luong13= tk.Checkbutton(self)
        self.luong13.place(x=500, y=270)

        tk.Label(self, text="Bậc lương:",bg='#66CCFF',fg="black",width =12).grid(row=10, column=0,pady=5)
        self.spinbox = tk.Spinbox(self,from_=0,to=12)
        self.spinbox.grid(row=10, column=1)

        tk.Label(self, text="BHYT:", bg='#66CCFF', fg="black", width=12).grid(row=10, column=2, pady=5)
        self.BHYT = tk.Checkbutton(self)
        self.BHYT.place(x=350, y=300)

        tk.Label(self, text="Lương cơ bản:",bg='#66CCFF',fg="black",width =12).grid(row=11, column=0, pady=5)
        self.luong_entry = tk.Entry(self)
        self.luong_entry.grid(row=11, column=1)
        self.combobox = ttk.Combobox(self,values=["VNĐ","USD"])
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
        gt = self.gt_combobox
        sdt = self.sdt_entry.get()
        email = self.email_entry.get()
        diachi = self.diachi_entry.get()
        hocvan = self.hocvan_entry.get()
        chucvu = self.chucvu_entry.get()
        diachi = self.diachi_entry.get()
        bophan = self.bophan_entry.get()
        noilamviec = self.noilamviec_entry.get()
        Bacluong = self.spinbox
        luongcoban = self.luong_entry.get()
        Donvitiente = self.combobox
        Phucap = self.phucap
        Trocap = self.trocap
        BHYT = self.BHYT
        BHXH = self.BHXH
        Luongthang13 = self.luong13


#đoạn này đang làm lại

        nhanvienmoi = thongtinluong(tennv,ngaysinh,gt,sdt,email,diachi,hocvan,chucvu,bophan,noilamviec,Bacluong,luongcoban,Donvitiente,Phucap,Trocap,BHYT,BHXH,Luongthang13)

       # thêm nhân viên mới vào trong file csv
        with open(r"C:\Users\Dell\OneDrive\Tài liệu\GitHub\Final\database\thongtinluong.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([nhanvienmoi.manv,nhanvienmoi.tennv,nhanvienmoi.ngaysinh,nhanvienmoi.gt,nhanvienmoi.sdt,nhanvienmoi.email,nhanvienmoi.diachi,nhanvienmoi.hocvan,nhanvienmoi.chucvu,nhanvienmoi.bophan,nhanvienmoi.noilamviec,nhanvienmoi.luongcoban,nhanvienmoi.phucap,nhanvienmoi.trocap,nhanvienmoi.BHYT,nhanvienmoi.BHXH,nhanvienmoi.BHYT])



#cửa sổ
root = tk.Tk()
root.title("THÊM NHÂN VIÊN")
root.geometry('900x500+200+100')
root.resizable(False, False)

app = Window(master=root)

app.mainloop()




