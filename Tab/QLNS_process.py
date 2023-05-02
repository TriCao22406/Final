from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk,Image
import  csv

class Nhanvien():
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,chucvu,hocvan):
      self.manv = manv
      self.tennv = tennv
      self.ngaysinh = ngaysinh
      self.gt = gt
      self.sdt = sdt
      self.email = email
      self.diachi = diachi
      self.chucvu = chucvu
      self.hocvan = hocvan

class  thongtinluong(Nhanvien):
   def __init__(self,manv,tennv,ngaysinh,gt,sdt,email,diachi,chucvu,hocvan,bophan,Bacluong,luongcoban,BHYT,BHXH,luongthang13):
      super().__init__(manv,tennv,ngaysinh,gt,sdt,email,diachi,chucvu,hocvan)
      self.bophan= bophan
      self.bacluong= Bacluong
      self.luongcoban = luongcoban
      self.BHYT = BHYT
      self.BHXH = BHXH
      self.luongthang13 = luongthang13

class Window():
    def __init__(self, master, **kwargs):
        self.master = master
        master.title("THÊM NHÂN VIÊN")
        master.geometry('1000x780+500+300')
        master.resizable(False, False)

        self.nhanvien = []

        self.label1 = tk.Label(master, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20,"bold",),justify=CENTER,fg="#DD0000",anchor="center").place(x=360, y=25)

        tk.Label(master,text="1. Thông tin nhân viên",font=("Times",15),fg="blue").place(x=30,y=70)

        tk.Label(master, text="Mã NV",bg="#66CCFF",fg="black",width =10,anchor="w").place(x=55,y=120)
        self.manv_entry = tk.Entry(master,width=15)
        self.manv_entry.place(x=160,y=120)

        tk.Label(master, text="Họ tên NV", bg="#66CCFF", fg="black", width=10,anchor="w").place(x=330,y=120)
        self.tennv_entry = tk.Entry(width=35)
        self.tennv_entry.place(x=430,y=120)

        tk.Label(master, text="Ngày sinh", bg="#66CCFF", fg="black", width=10,anchor="w").place(x=55, y=160)
        self.ngaysinh_entry = tk.Entry(master,width=15)
        self.ngaysinh_entry.place(x=160, y=160)
        self.ngaysinh_entry.insert(0, "dd/mm/yyyy")
        self.ngaysinh_entry.bind("<1>",self.pick_date)

        tk.Label(master, text="Giới tính",bg="#66CCFF",fg="black",width =10,anchor="w").place(x=330,y=160)
        self.gioitinh_check = tk.StringVar()
        self.gt_options = ["Nam", "Nữ"]
        self.gt_combobox = ttk.Combobox(master, values=self.gt_options,textvariable=self.gioitinh_check,width=17)
        self.gt_combobox.set("Chọn giới tính")
        self.gt_combobox.place(x=430,y=160)

        tk.Label(master, text="Học vấn",bg="#66CCFF",fg="black",width =10,anchor="w").place(x=55, y=200)
        self.hocvan_entry = tk.Entry(master,width=35)
        self.hocvan_entry.place(x=160, y=200)

        tk.Label(master, text="Địa chỉ", bg="#66CCFF", fg="black", width=10,anchor="w").place(x=55, y=240)
        self.diachi_entry = tk.Entry(master,width=35)
        self.diachi_entry.place(x=160, y=240)

        tk.Label(master, text="Email",bg="#66CCFF",fg="black",width =10,anchor="w").place(x=55, y=280)
        self.email_entry = tk.Entry(master,width=35)
        self.email_entry.place(x=160, y=280)

        tk.Label(master, text="SĐT",bg="#66CCFF",fg="black",width =10).place(x=400, y=280)
        self.sdt_entry = tk.Entry(master,width=25)
        self.sdt_entry.place(x=490, y=280)

        tk.Label(master, text="2.Thông tin công việc", font=("Times", 15), fg="blue").place(x=30, y=320)

        tk.Label(master, text="Ngày vào", bg="#66CCFF", fg="black", width=10, anchor="w").place(x=55, y=360)
        self.ngayvao_entry = tk.Entry(master, width=15)
        self.ngayvao_entry.place(x=160, y=360)
        self.ngayvao_entry.insert(0, "dd/mm/yyyy")
        self.ngayvao_entry.bind("<1>",self.pick_date)

        tk.Label(master, text="Bộ phận", bg="#66CCFF", fg="black", width=10,anchor="w").place(x=55, y=400)
        self.bophan_entry = tk.Entry(master, width=35)
        self.bophan_entry.place(x=160, y=400)

        tk.Label(master, text="Chức vụ", bg="#66CCFF", fg="black", width=10, anchor="w").place(x=400, y=400)
        self.chucvu_entry = tk.Entry(master, width=25)
        self.chucvu_entry.place(x=490, y=400)

        tk.Label(master, text="Lương", bg="#66CCFF", fg="black", width=10,anchor="w").place(x=55, y=440)

        self.luonggop_check = IntVar()
        tk.Radiobutton(master,text="Lương gộp",width =10,variable=self.luonggop_check, value=1,anchor="w").place(x=160, y=438)

        self.luongrong_check = IntVar()
        tk.Radiobutton(master, text="Lương ròng", width=10, variable=self.luongrong_check, value=1,anchor="w").place(x=160, y=468)

        tk.Label(master, text="Lương cơ bản", width=12,anchor="w").place(x=260, y=440)
        self.luongcoban_check = tk.BooleanVar()
        self.luongcoban = tk.Checkbutton(master,variable=self.luongcoban_check)
        self.luongcoban.place(x=360, y=440)

        tk.Label(master, text="Lương tháng 13", width=12,anchor="w").place(x=260, y=470)
        self.luong13_check = tk.BooleanVar()
        self.luong13 = tk.Checkbutton(master,variable=self.luong13_check)
        self.luong13.place(x=360, y=470)

        tk.Label(master, text="Trả theo tháng", width=12,anchor="w").place(x=397, y=440)
        self.tratheothang_check = tk.BooleanVar()
        self.tratheothang = tk.Checkbutton(master,variable=self.tratheothang_check)
        self.tratheothang.place(x=496, y=440)

        tk.Label(master, text="Trả theo ca", width=12,anchor="w").place(x=397, y=470)
        self.tratheoca_check = tk.BooleanVar()
        self.tratheoca = tk.Checkbutton(master,variable=self.tratheoca_check)
        self.tratheoca.place(x=496, y=470)

        tk.Label(master, text="Bậc lương", width=10,anchor="w").place(x=540, y=440)
        self.bacluong = tk.Checkbutton(master, variable=self.tratheoca_check)
        self.bacluong_spinbox = tk.Spinbox(master,from_=0,to=12,width=5)
        self.bacluong_spinbox.place(x=610, y=440)

        tk.Label(master, text="Ngày hưởng",width=12, anchor="w").place(x=540, y=470)
        self.ngayhuong_entry = tk.Entry(master, width=15)
        self.ngayhuong_entry.place(x=625, y=470)
        self.ngayhuong_entry.insert(0, "dd/mm/yyyy")
        self.ngayhuong_entry.bind("<1>",self.pick_date )

        tk.Label(master, text="Trả bằng tiền mặt", width=13,anchor="w").place(x=160, y=500)
        self.tratienmat_check = tk.BooleanVar()
        self.tratienmat = tk.Checkbutton(master, variable=self.tratienmat_check)
        self.tratienmat.place(x=265, y=500)

        tk.Label(master, text="Trả qua ngân hàng", width=14,anchor="w").place(x=160, y=530)
        self.tranganhang_check = tk.BooleanVar()
        self.tranganhang = tk.Checkbutton(master, variable=self.tranganhang_check)
        self.tranganhang.place(x=265, y=530)

        tk.Label(master,text="Tên ngân hàng:",width=12,anchor="w").place(x=310, y=530)
        self.nganhang_options = ['BIDV', 'SCB', 'VCB', 'AGRIBANK', 'VIETTINBANK', 'TECHCOMBANK', 'MBBANK']
        self.nganhang_combobox = ttk.Combobox(master,values=self.nganhang_options,width=15)
        self.nganhang_combobox.set("Chọn ngân hàng")
        self.nganhang_combobox.place(x=400, y=530)

        tk.Label(master, text="STK:", width=10, anchor="w").place(x=540, y=530)
        self.stk_entry = tk.Entry(master,width=23)
        self.stk_entry.place(x=580, y=530)

        tk.Label(master, text="BHYT",bg="#66CCFF", fg="black",width=10,anchor="w").place(x=55, y=560)
        self.BHYT_check = tk.BooleanVar()
        self.BHYT = tk.Checkbutton(master,variable=self.BHYT_check)
        self.BHYT.place(x=160, y=560)

        tk.Label(master,text="Mã BHYT:",fg="black",anchor="w",width=10).place(x=240, y=560)
        self.BHYT_entry = tk.Entry(master,width=25)
        self.BHYT_entry.place(x=310, y=560)

        tk.Label(master, text="Từ ngày:",width=10).place(x=540, y=560)
        self.ngay_entry = tk.Entry(master,width=15)
        self.ngay_entry.place(x=610, y=560)
        self.ngay_entry.insert(0, "dd/mm/yyyy")
        self.ngay_entry.bind("<1>",self.pick_date )

        tk.Label(master, text="Đến ngày:", width=10).place(x=540, y=590)
        self.ngay_entry = tk.Entry(master, width=15)
        self.ngay_entry.place(x=610, y=590)
        self.ngay_entry.insert(0, "dd/mm/yyyy")
        self.ngay_entry.bind("<1>",self.pick_date )

        tk.Label(master, text="Bệnh viện:", width=10, anchor="w").place(x=160, y=590)
        self.benhvien_options = ["Bệnh viện Thủ Đức", "Bệnh viện Chợ Rẫy", "Bệnh viên Quân y 175", "Bệnh viện Bệnh nhiệt đới" "Khác"]
        self.benhvien_combobox = ttk.Combobox(master, values=self.benhvien_options, width=35)
        self.benhvien_combobox.set("Chọn bệnh viện")
        self.benhvien_combobox.place(x=230, y=590)

        tk.Label(master, text="BHXH", bg="#66CCFF", fg="black", width=10, anchor="w").place(x=55, y=630)
        self.BHXH_check = tk.BooleanVar()
        self.BHXH = tk.Checkbutton(master, variable=self.BHXH_check)
        self.BHXH.place(x=160, y=630)

        tk.Label(master, text="Mã BHXH:", fg="black", anchor="w", width=10).place(x=240, y=630)
        self.BHXH_entry = tk.Entry(master, width=25)
        self.BHXH_entry.place(x=310, y=630)

        tk.Label(master, text="Từ ngày:", width=10).place(x=540, y=630)
        self.ngay_entry = tk.Entry(master, width=15)
        self.ngay_entry.place(x=610, y=630)
        self.ngay_entry.insert(0, "dd/mm/yyyy")
        self.ngay_entry.bind("<1>",self.pick_date )

        tk.Label(master, text="Đến ngày:", width=10).place(x=540, y=660)
        self.ngay_entry = tk.Entry(master, width=15)
        self.ngay_entry.place(x=610, y=660)
        self.ngay_entry.insert(0, "dd/mm/yyyy")
        self.ngay_entry.bind("<1>",self.pick_date )

        tk.Label(master, text="Nơi cấp:", width=10, anchor="w").place(x=160, y=660)
        self.noicap_entry = tk.Entry(master,width=38)
        self.noicap_entry.place(x=230, y=660)

        #mấy cái này cần thêm hàm thực hiện, chưa def hàm
        self.luu_button = tk.Button(master, text="Lưu thông tin",bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=290,y=710)

        self.luu_button = tk.Button(master, text="Hiển thị thông tin",bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=400,y=710)

        self.luu_button = tk.Button(master, text="Xóa nhân viên", bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=530, y=710)

        self.luu_button = tk.Button(master, text="Cập nhật nhân viên", bg="#FF6A6A", command=self.themnv)
        self.luu_button.place(x=640, y=710)


        #đoạn nàydđnag làm lại chưa xong nữa, cần làm hàm cho nó chạy xong là thoát luôn
        self.thoat_button = tk.Button(master, text="Thoát",bg="#EEDC82", command=master)
        self.thoat_button.place(x=850, y=710)

        #tạo frame chứa ảnh
        width = 200
        height = 280
        self.img = Image.open(rb"E:\Download\avt.png")
        self.photoImg = ImageTk.PhotoImage(self.img)
        self.anh = tk.Label(master,image=self.photoImg, width=300)
        self.anh.place(x=670, y=110)


#đang lỗi phần chọn ngày, đang kiếm cách sửa
    def pick_date(sefl):
        global cal, date_window
        sefl.date_window = Toplevel()
        sefl.date_window.grab_set()
        sefl.date_window.title("Chọn ngày")
        sefl.date_window.geometry('250x220+590+370')
        sefl.cal=Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
        sefl.cal.place(x=0, y=0)
        sefl.pickdate = cal.get_date()
        submit_btn=Button(date_window, text="Submit", command=sefl.grap_date)
        submit_btn.place(x=80, y=190)
    def grap_date(self):
        self.ngayhuong_entry.delete(0, END)
        self.ngayvao_entry.delete(0, END)
        self.ngay_entry.delete(0,END)

        self.ngayhuong_entry.insert(0, cal.get_date())
        self.ngayvao_entry.insert(0, cal.get_date())
        self.ngay_entry.insert(0, cal.get_date())
        date_window.destroy()


    def themnv(self):
        manv = self.manv_entry.get()
        tennv = self.tennv_entry.get()
        ngaysinh = self.ngaysinh_entry.get()
        gt = self.gioitinh_check.get()
        hocvan = self.hocvan_entry.get()
        diachi = self.diachi_entry.get()
        email = self.email_entry.get()
        sdt = self.sdt_entry.get()
        bophan = self.bophan_entry.get()
        chucvu = self.chucvu_entry.get()
        Bacluong = self.bacluong_spinbox.get()
        luongcoban = self.luongcoban_check.get()
        BHYT = self.BHYT_check.get()
        BHXH = self.BHXH_check.get()
        luongthang13 = self.luong13_check.get()

        #tạo nhân viên mới
        nvm = thongtinluong(manv, tennv, ngaysinh,hocvan,gt,diachi,email,sdt,bophan,chucvu,Bacluong,luongcoban,BHYT,BHXH,luongthang13)

        # kiểm tra sự trùng lặp
        for e in self.nhanvien:
            if e.manv == nvm.manv:
                self.show = messagebox.showerror("Lỗi","Nhân viên với mã {} đã tồn tại!".format(manv), parent = root)
                return

        # thêm nhân viên mới vào trong danh sách và trong file csv
        self.nhanvien.append(nvm)
        with open("test.csv", "a", newline='',encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                nvm.manv,
                nvm.tennv,
                nvm.ngaysinh,
                nvm.hocvan,
                nvm.gt,
                nvm.diachi,
                nvm.email,
                nvm.sdt,
                nvm.bophan,
                nvm.chucvu,
                nvm.bacluong,
                nvm.luongcoban,
                nvm.BHYT,
                nvm.BHXH,
                nvm.luongthang13,
            ])
        self.show1 = messagebox.showinfo("Thành công","Thông tin nhân viên đã được lưu")





root = tk.Tk()
app = Window(root)


root.mainloop()




