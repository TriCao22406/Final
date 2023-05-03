from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

class Nhanvien():
   def __init__(self, manv, tennv, ngaysinh, gt, sdt, email, chucvu, bophan, luong, namkinhnghiem):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.gt = gt
      self.sdt = sdt
      self.email = email
      self.chucvu = chucvu
      self.bophan = bophan
      self.luong = luong
      self.namkinhnghiem = namkinhnghiem


class Window():
    def __init__(self, master):
        self.master = master
        master.title("THÊM NHÂN VIÊN")
        master.geometry('900x600+500+300')
        master.resizable(False, False)

        self.nhanvien = []

        self.label1 = tk.Label(master, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold",), justify=CENTER, fg="#DD0000", anchor="center").place(x=280, y=20)

        tk.Label(master, text="Mã nhân viên", bg="#66CCFF", fg="black", width =12, anchor="w").place(x=55,y=120)
        self.manv_entry = tk.Entry(master,width=18)
        self.manv_entry.place(x=160, y=120)

        tk.Label(master, text="Giới tính", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=330, y=120)
        self.gioitinh_check = tk.StringVar()
        self.gt_options = ["Nam", "Nữ"]
        self.gt_combobox = ttk.Combobox(master, values=self.gt_options, textvariable=self.gioitinh_check, width=13)
        self.gt_combobox.set("Chọn giới tính")
        self.gt_combobox.place(x=430, y=120)

        tk.Label(master, text="Tên nhân viên", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=160)
        self.tennv_entry = tk.Entry(master, width=22)
        self.tennv_entry.place(x=160, y=160)

        tk.Label(master, text="Ngày sinh", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=330, y=160)
        self.ngaysinh_entry = tk.Entry(width=18)
        self.ngaysinh_entry.place(x=430, y=160)

        tk.Label(master, text="Chức vụ", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=200)
        self.chucvu_entry = tk.Entry(master, width=22)
        self.chucvu_entry.place(x=160, y=200)

        tk.Label(master, text="Năm kinh nghiệm", width=16, anchor="w").place(x=330, y=200)
        self.nkm_entry = tk.Entry(master, width=5)
        self.nkm_entry.place(x=440, y=200)

        tk.Label(master, text="Bộ phận", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=240)
        self.bophan_entry = tk.Entry(master, width=25)
        self.bophan_entry.place(x=160, y=240)

        tk.Label(master, text="Lương", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=280)
        self.luong_entry = tk.Entry(master, width=25)
        self.luong_entry.place(x=160, y=280)

        tk.Label(master, text="Số điện thoại", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=320)
        self.sdt_entry = tk.Entry(master, width=28)
        self.sdt_entry.place(x=160, y=320)

        tk.Label(master, text="Email", bg="#66CCFF", fg="black", width=12, anchor="w").place(x=55, y=360)
        self.email_entry = tk.Entry(master, width=35)
        self.email_entry.place(x=160, y=360)

        self.luu_button = tk.Button(master, text="Lưu thông tin", bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=360, y=500)

        self.thoat_button = tk.Button(master, text="Thoát", bg="#EEDC82", command=self.thoat)
        self.thoat_button.place(x=460, y=500)

        #tạo frame chứa ảnh
        self.img = Image.open(r"C:\Users\Dell\OneDrive\Tài liệu\GitHub\Final\images\avt.png")
        self.photoImg = ImageTk.PhotoImage(self.img)
        self.anh = tk.Label(master, image=self.photoImg, width=300)
        self.anh.place(x=590, y=100)


    def timnv(sefl, manv):
            for i in range(len(sefl.nhanvien)):
                if manv == sefl.nhanvien[i].manv:  # tìm thấy
                    return {"idx": i, "inf": sefl.nhanvien[i]}
            return -1

    def themnv(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        ngaysinh = self.ngaysinh_entry.get()
        gt = self.gioitinh_check.get()
        email = self.email_entry.get()
        sdt = self.sdt_entry.get()
        bophan = self.bophan_entry.get()
        chucvu = self.chucvu_entry.get()
        luong = self.luong_entry.get()
        namkinhnghiem = self.nkm_entry.get()

        #kiểm tra nhân viên đã tn tại trong ds chưa
        #cái này nó k chạy, đang xem lại
        for nvm in self.nhanvien:
            if nvm.manv == manv:
                self.show = messagebox.showerror("Lỗi", "Nhân viên với mã {} đã tồn tại!".format(manv))
                return


        #kiểm tra tất cả các mục đều được điền
        if manv == "" or tennv == '' or gt == "---Giới tính---" or bophan == '' or chucvu == '' or ngaysinh == '' or sdt == '' or email == '' or luong == '' or namkinhnghiem =='' :
            messagebox.showerror("Lỗi", "Phải điền đầy đủ thông tin!")
            return

        #thêm nvm mới vào trong ds và file csv
        nvm = Nhanvien(manv, tennv, ngaysinh, email, sdt, gt, bophan, chucvu, namkinhnghiem, luong)
        self.nhanvien.append(nvm)

        with open("test.csv", "a", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                nvm.manv,
                nvm.tennv,
                nvm.ngaysinh,
                nvm.email,
                nvm.sdt,
                nvm.gt,
                nvm.bophan.
                nvm.chucvu,
                nvm.namkinhnghiem,
                nvm.luong
            ])
        self.show = messagebox.showinfo("Thành công", "Thông tin nhân viên đã được lưu.")

        self.clear()

    def clear(sefl):
        sefl.manv_entry.delete(0, END)
        sefl.tennv_entry.delete(0, END)
        sefl.chucvu_entry.delete(0, END)
        sefl.ngaysinh_entry.delete(0, END)
        sefl.sdt_entry.delete(0, END)
        sefl.email_entry.delete(0, END)
        sefl.nkm_entry.delete(0, END)
        sefl.bophan_entry.delete(0, END)
        sefl.luong_entry.delete(0, END)
        sefl.gt_combobox.set("---Giới tính---")

    def thoat(self):
        self.master.destroy()



root = tk.Tk()

app = Window(root)

root.mainloop()





