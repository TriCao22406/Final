import tkinter as tk
from tkinter import ttk

#tạo cửa sổ chính
root = tk.Tk()
root.title("QUẢN LÝ NHÂN VIÊN")
root.geometry('925x650+250+100')
root.resizable(False, False)
root.configure(bg="#fff")

class Widget:
   def __init__(self, master):
      self.master = master
      master.title("Quản lý nhân viên")
      self.notebook = ttk.Notebook(master)

      # tạo các tab
      self.tab1 = tk.Frame(self.notebook, bg="#E9E7F2")
      self.tab2 = tk.Frame(self.notebook, bg="#E9E7F2")
      self.tab3 = tk.Frame(self.notebook, bg="#E9E7F2")

      # thêm tab vào trong Notebook
      self.notebook.add(self.tab1, text="Thông tin cá nhân", )
      self.notebook.add(self.tab2, text="Hồ sơ công việc")
      self.notebook.add(self.tab3, text="Tính lương")
      # đóng gói các notebook object
      self.notebook.pack(expand=1, fill=tk.BOTH)


      # Thêm các widget khác vào các tab
      # tab1
      self.label1 = tk.Label(self.tab1, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20))
      self.label1.pack(pady=10, padx=10)



class Nhanvien_TTca_nhan():
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,hocvan):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.gt = gt
      self.sdt = sdt
      self.email = email
      self.diachi = diachi
      self.hocvan = hocvan

class QuanlyNV():
   pass





widget = Widget(root)
root.mainloop()