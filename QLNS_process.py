from tkinter import *
import tkinter as tk
from tkinter import ttk

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

        self.label1 = tk.Label(self, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold"),justify=CENTER)
        self.label1.grid(row=0, column=0, columnspan=4)

        tk.Label(self, text="MSNV:").grid(row=1, column=0,pady=5,padx=5)
        self.manv_entry = tk.Entry(self)
        self.manv_entry.grid(row=1, column=1)

        tk.Label(self, text="Giới tính:").grid(row=1, column=2,pady=5,padx=5)
        self.gt_entry = tk.Entry(self)
        self.gt_entry.grid(row=1, column=3)

        tk.Label(self, text="Tên nhân viên:").grid(row=2, column=0,pady=5,padx=5)
        self.tennv_entry = tk.Entry(self)
        self.tennv_entry.grid(row=2, column=1)

        tk.Label(self, text="Học vấn:").grid(row=2, column=2,pady=5,padx=5)
        self.hocvan_entry = tk.Entry(self)
        self.hocvan_entry.grid(row=2, column=3)

        tk.Label(self, text="Ngày sinh:").grid(row=3, column=0,pady=5,padx=5)
        self.ngaysinh_entry = tk.Entry(self)
        self.ngaysinh_entry.grid(row=3, column=1)

        tk.Label(self, text="Số điện thoại:").grid(row=3, column=2,pady=5,padx=5)
        self.sdt_entry = tk.Entry(self)
        self.sdt_entry.grid(row=3, column=3)

        tk.Label(self, text="Chức vụ:").grid(row=4, column=0,pady=5,padx=5)
        self.chucvu_entry = tk.Entry(self)
        self.chucvu_entry.grid(row=4, column=1)

        tk.Label(self, text="Email:").grid(row=4, column=2,pady=5,padx=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=3)

        tk.Label(self, text="Địa chỉ:").grid(row=5, column=0,pady=5,padx=5)
        self.diachi_entry = tk.Entry(self)
        self.diachi_entry.grid(row=5, column=1)

        self.separator = ttk.Separator(self, orient="horizontal")
        self.separator.grid(row=6,column=0,padx=15,pady=10)

        tk.Label(self,text="Mức lương",font=("Times",13,"bold")).grid(row=7,column=0)

        tk.Label(self,text="Bộ phận:").grid(row=8,column=0,pady=5)
        self.bophan_entry =tk.Entry(self)
        self.bophan_entry.grid(row=8,column=1,pady=5)

        tk.Label(self, text="Nơi làm việc:").grid(row=9, column=0,pady=5)
        self.bophan_entry = tk.Entry(self)
        self.bophan_entry.grid(row=9, column=1)

        tk.Label(self, text="Bậc lương:").grid(row=10, column=0,pady=5)
        self.spinbox = tk.Spinbox(self,from_=0,to=12)
        self.spinbox.grid(row=10, column=1)

        tk.Label(self, text="Lương cơ bản:").grid(row=11, column=0, pady=5)
        self.luong_entry = tk.Entry(self)
        self.luong_entry.grid(row=11, column=1)

        #làm sao để nó cùng hàng đc đây ?????
        self.combobox = ttk.Combobox(master,values=["VNĐ","USD"],)
        self.combobox.set("VNĐ")
        self.combobox.pack()

    def themnv(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        ngaysinh = self.ngaysinh_entry.get()
        gt = self.gt_entry.get()
        sdt = self.sdt_entry.get()
        email = self.email_entry.get()
        diachi = self.diachi_entry.get()
        hocvan = self.hocvan_entry.get()
        chucvu = self.chucvu_entry.get()




#cửa sổ
root = tk.Tk()
root.title("THÊM NHÂN VIÊN")
root.geometry('900x500+200+100')
root.resizable(False, False)

app = Window(master=root)

app.mainloop()




