from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

class Nhanvien():
   def __init__(self, manv, tennv, ngaysinh, email, sdt, gt, bophan, chucvu, namkinhnghiem, luong):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.email = email
      self.sdt = sdt
      self.gt = gt
      self.bophan = bophan
      self.chucvu = chucvu
      self.namkinhnghiem = namkinhnghiem
      self.luong = luong

class Window():
    def __init__(self, master):
        self.master = master
        self.nhanvien = self.load_data()
        master.title("THÊM NHÂN VIÊN")
        master.geometry('900x600+500+300')
        master.resizable(False, False)

        self.label1 = tk.Label(master, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold",), justify=CENTER, fg="#DD0000", anchor="center").place(x=280, y=35)

        tk.Label(master, text="Mã nhân viên", bg="#66CCFF", fg="black", width =12, anchor="w").place(x=55,y=120)
        self.manv_entry = tk.Entry(master, width=18)
        self.manv_entry.place(x=160, y=120)

        tk.Label(master, text="Tên nhân viên", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=160)
        self.tennv_entry = tk.Entry(master, width=35)
        self.tennv_entry.place(x=160, y=160)

        tk.Label(master, text="Ngày sinh", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=200)
        self.ngaysinh_entry = tk.Entry(master, width=18)
        self.ngaysinh_entry.place(x=160, y=200)

        tk.Label(master, text="Giới tính", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=315, y=200)
        self.gioitinh_check = tk.StringVar()
        self.gt_options = ["Nam", "Nữ", "Khác"]
        self.gt_combobox = ttk.Combobox(master, values=self.gt_options, textvariable=self.gioitinh_check, width=13)
        self.gt_combobox.set("Chọn giới tính")
        self.gt_combobox.place(x=420, y=200)

        tk.Label(master, text="Số điện thoại", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=240)
        self.sdt_entry = tk.Entry(master, width=20)
        self.sdt_entry.place(x=160, y=240)

        tk.Label(master, text="Email", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=315, y=240)
        self.email_entry = tk.Entry(master, width=35)
        self.email_entry.place(x=420, y=240)

        tk.Label(master, text="Bộ phận", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=280)
        self.bophan_entry = tk.Entry(master, width=20)
        self.bophan_entry.place(x=160, y=280)

        tk.Label(master, text="Chức vụ", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=315, y=280)
        self.chucvu_entry = tk.Entry(master, width=35)
        self.chucvu_entry.place(x=420, y=280)

        tk.Label(master, text="Lương", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=320)
        self.luong_entry = tk.Entry(master, width=18)
        self.luong_entry.place(x=160, y=320)

        tk.Label(master, text="Kinh nghiệm", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=315, y=320)
        tk.Label(master, text="năm", fg="black").place(x=460, y=320)
        self.namkinhnghiem = Spinbox(master,from_=1, to=20, width=3)
        self.namkinhnghiem.place(x=420, y=320)

        self.luu_button = tk.Button(master, text="Lưu thông tin", bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=360, y=500)

        self.lammoi_button = tk.Button(master, text="Làm mới", bg="#FF6A6A", command=self.clear)
        self.lammoi_button.place(x=460, y=500)

        self.thoat_button = tk.Button(master, text="Thoát", bg="#EEDC82", command=self.thoat)
        self.thoat_button.place(x=560, y=500)

        #tạo frame chứa ảnh
        self.img = Image.open(r"..\Final\images\avt.png")
        self.photoImg = ImageTk.PhotoImage(self.img)
        self.anh = tk.Label(master, image=self.photoImg, width=300)
        self.anh.place(x=590, y=100)

    def load_data(sefl):
        nhanvien = []
        #sử dụng một khối try-except để xử lý trường hợp tệp chưa tồn tại
        try:  #Nếu tệp tồn tại, tệp csv được mở bằng hàm open()
            with open(r"..\Final\database\employees.csv", newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Dòng next(reader) được sử dụng để bỏ qua hàng tiêu đề chứa tên cột.
                for row in reader:   #hàm lặp qua các hàng trong tệp csv
                    manv, tennv, ngaysinh, email, sdt, gt, bophan, chucvu, namkinhnghiem, luong = row

                    nvm = Nhanvien(manv, tennv, ngaysinh, email, sdt, gt, bophan, chucvu, namkinhnghiem, luong)
                    nhanvien.append(nvm)
        except :   #Nếu tệp không tồn tại, mã trong khối ngoại trừ được thực thi, chỉ trả về danh sách trống
            pass
        return nhanvien     #khi tất cả các hàng đã được thêm vào danh sách, hàm sẽ trả về danh sách.

    def themnv(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        ngaysinh = self.ngaysinh_entry.get()
        email = self.email_entry.get()
        sdt = self.sdt_entry.get()
        gt = self.gioitinh_check.get()
        bophan = self.bophan_entry.get()
        chucvu = self.chucvu_entry.get()
        namkinhnghiem = self.namkinhnghiem.get()
        luong = self.luong_entry.get()


        #kiểm tra tất cả các mục đều được điền,  k bo trong
        if manv == "" or tennv == '' or gt == "---Giới tính---" or bophan == '' or chucvu == '' or ngaysinh == '' or sdt == '' or email == '' or luong == '' or namkinhnghiem =='' :
            messagebox.showerror("Lỗi", "Phải điền đầy đủ thông tin!")
            return

        #kiểm tra sự trùng lặp trong danh sách
        for nv in self.nhanvien:
            if nv.manv == manv:
                messagebox.showerror("Lỗi", "Nhân viên với mã {} đã tồn tại!".format(manv))
                return

        #tạo ra nhân viên mới
        nvm = Nhanvien(manv, tennv, ngaysinh, email, sdt, gt, bophan, chucvu, namkinhnghiem, luong)
        self.nhanvien.append(nvm)

        #thên nhân viên vào trong file csv
        with open(r"..\Final\database\employees.csv", "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                nvm.manv,
                nvm.tennv,
                nvm.ngaysinh,
                nvm.email,
                nvm.sdt,
                nvm.gt,
                nvm.bophan,
                nvm.chucvu,
                nvm.namkinhnghiem,
                nvm.luong
            ])
        self.show = messagebox.showinfo("Thành công", "Thông tin nhân viên đã được lưu.")
        #self.clear()

    def clear(sefl):
        sefl.manv_entry.delete(0, END)
        sefl.tennv_entry.delete(0, END)
        sefl.chucvu_entry.delete(0, END)
        sefl.ngaysinh_entry.delete(0, END)
        sefl.sdt_entry.delete(0, END)
        sefl.email_entry.delete(0, END)
        sefl.namkinhnghiem.delete(0, END)
        sefl.bophan_entry.delete(0, END)
        sefl.luong_entry.delete(0, END)
        sefl.gt_combobox.set("---Giới tính---")
    def thoat(self):
        self.master.destroy()


# root = tk.Tk()
# app = Window(root)
# root.mainloop()





