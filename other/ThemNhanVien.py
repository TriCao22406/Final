from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x700")
label1 = tk.Label(root, text="THÔNG TIN NHÂN VIÊN", font=("Times", 20, "bold",), justify=CENTER, fg="#DD0000")
label1.grid(row=0, column=0, columnspan=4)

def clear():
    manv_entry.delete(0,END)
    tennv_entry.delete(0,END)
    hocvan_entry.delete(0,END)
    chucvu_entry.delete(0,END)
    ngaysinh_entry.delete(0,END)
    sdt_entry.delete(0,END)
    email_entry.delete(0,END)
    diachi_entry.delete(0,END)
    gt_combobox.set("---Giới tính---")
class nhanvien:
    dsnv = []

    def __init__(self):
        self.manv = manv_entry.get()
        self.tennv = tennv_entry.get()
        self.gioitinh = gt_combobox.get()
        self.hocvan = hocvan_entry.get()
        self.chucvu=chucvu_entry.get()
        self.ngaysinh = ngaysinh_entry.get()
        self.dienthoai = sdt_entry.get()
        self.email = email_entry.get()
        self.diachi = diachi_entry.get()
        nhanvien.themnv(self)

    @classmethod
    def timnv(cls, manv):
        for i in range(len(cls.dsnv)):
            if manv == cls.dsnv[i].manv:  # tìm thấy
                return {"idx": i, "inf": cls.dsnv[i]}
        return -1

    @classmethod
    def themnv(cls, nv):
        if nv.manv == "" or nv.tennv=='' or nv.gioitinh== "---Giới tính---" or nv.hocvan=='' or nv.chucvu == '' or nv.ngaysinh=='' or nv.dienthoai =='' or nv.email =='' or nv.diachi=='':
            messagebox.showerror("Lỗi", "Phải điền đầy đủ thông tin!")
            return False
        else:
          if cls.timnv(nv.manv) == -1:
            cls.dsnv.append(nv)
            messagebox.showinfo("tk", "Thêm thành công")
            clear()
            return True
          else:
            messagebox.showerror("Lỗi", "Nhân viên bị trùng id")
            clear()
            return False


    @classmethod
    def hienthinv(cls):
        root2 = tk.Tk()
        root2.title("Hiển thị nhân viên")
        root2.state("zoomed")

        def create_tree_widget():
            columns = ('Mã nhân viên','Tên nhân viên','Giới tính ', 'Học vấn' ,'Chức vụ', 'Ngày sinh:' , 'Điện thoại:', 'email:', 'địa chỉ:' ,'bộ phận: ','phụ cấp: ','BHXH:','Nơi làm việc ','Trợ cấp: ','Lương tháng 13: ','Bậc lương: ','BHYT', "Lương cơ bản",'loại tiền tệ')
            tree = ttk.Treeview(root2, columns=columns, show='headings')

            tree.heading('Mã nhân viên', text='Mã nhân viên')
            tree.heading('Tên nhân viên', text='Tên nhân viên')
            tree.heading('Giới tính ', text='Giới tính ')
            tree.heading('Học vấn', text='Học vấn')
            tree.heading('Chức vụ', text='Chức vụ')
            tree.heading('Ngày sinh:', text='Ngày sinh:')
            tree.heading('Điện thoại:', text='Điện thoại:')
            tree.heading('email:', text='email:')


            scrollbar_doc = Scrollbar(root2)
            scrollbar_doc.pack(side=RIGHT, fill=Y)

            tree.configure(yscrollcommand=scrollbar_doc.set)
            scrollbar_ngang = Scrollbar(root2)
            scrollbar_ngang.pack(side=BOTTOM, fill=X)

            tree.configure(xscrollcommand=scrollbar_ngang.set)
            contact = []
            for nv in cls.dsnv:
                contact.append(
                    [nv.manv, nv.tennv, nv.gioitinh, nv.hocvan,nv.chucvu, nv.ngaysinh, nv.dienthoai, nv.email])

            for nv1 in contact:
                tree.insert('', tk.END, values=(nv1[0],nv1[1],nv1[2],nv1[3],nv1[4],nv1[5],nv1[6],nv1[7]))
            tree.pack(side=LEFT, fill=BOTH)
            scrollbar_doc.config(command=tree.yview)
            scrollbar_ngang.config(command=tree.xview)

        create_tree_widget()

        root2.mainloop()
        clear()
    @staticmethod
    def xoanv():
        manv= manv_entry.get()
        t = nhanvien.timnv(manv)
        if t == -1:
            messagebox.showerror("Lỗi", 'Không tìm thấy nhân viên để xóa')
            clear()
            return False
        else:
            nhanvien.dsnv.pop(t["idx"])
            messagebox.showinfo("tk",'xóa thành công')
            clear()
            return True
    @classmethod
    def capnhatlaithongtin(cls):
        manv= manv_entry.get()
        t = nhanvien.timnv(manv)
        if t ==-1:
            messagebox.showerror("Lỗi", 'Không tìm thấy nhân viên để cập nhật lại thông tin')
            clear()
            return False
        else:
            cls.dsnv[t['idx']].manv = manv_entry.get()
            cls.dsnv[t['idx']].tennv = tennv_entry.get()
            cls.dsnv[t['idx']].gioitinh = gt_combobox.get()
            cls.dsnv[t['idx']].hocvan = hocvan_entry.get()
            cls.dsnv[t['idx']].chucvu = chucvu_entry.get()
            cls.dsnv[t['idx']].ngaysinh = ngaysinh_entry.get()
            cls.dsnv[t['idx']].dienthoai = sdt_entry.get()
            cls.dsnv[t['idx']].email = email_entry.get()
            cls.dsnv[t['idx']].diachi = diachi_entry.get()
            if cls.dsnv[t['idx']].manv == "" or cls.dsnv[t['idx']].tennv == '' or cls.dsnv[t['idx']].gioitinh == "---Giới tính---" or cls.dsnv[t['idx']].hocvan == '' or cls.dsnv[t['idx']].chucvu == '' or cls.dsnv[t['idx']].ngaysinh == '' or cls.dsnv[t['idx']].dienthoai == '' or cls.dsnv[t['idx']].email == '' or cls.dsnv[t['idx']].diachi == '':
                messagebox.showerror("Lỗi", "Phải điền đầy đủ thông tin!")
            else:
                messagebox.showinfo("tk", 'Hoàn thành quá trình cập nhật')
                clear()
            return True





tk.Label(root, text="MSNV:", bg="#66CCFF", fg="black", width=12).grid(row=1, column=0, pady=5, padx=5)
manv_entry = tk.Entry(root)
manv_entry.grid(row=1, column=1)

tk.Label(root, text="Giới tính:", bg="#66CCFF", fg="black", width=12).grid(row=1, column=2, pady=5, padx=5)
gt_combobox = ttk.Combobox(root, values=["Nam", "Nữ","---Giới tính---"], )
gt_combobox.set("---Giới tính---")
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




# tạo 2 button lưu thông tin và thoát

separator = ttk.Separator(root, orient="horizontal", )
separator.grid(row=12, column=0, padx=30, pady=15)

luu_button = tk.Button(root, text="Lưu thông tin", bg="#FF6A6A", command=nhanvien)
luu_button.place(x=20, y=390)
hienthi_button = tk.Button(root, text='Hiển thị thông tin', bg='#FF6A6A', command=nhanvien.hienthinv)
hienthi_button.place(x=100, y=390)
xoa_button = tk.Button(root, text='xóa nhân viên', bg='#FF6A6A', command=nhanvien.xoanv)
xoa_button.place(x=200, y=390)
capnhat_button = tk.Button(root, text='cập nhật nhân viên', bg='#FF6A6A', command=nhanvien.capnhatlaithongtin)
capnhat_button.place(x=285, y=390)

thoat_button = tk.Button(root, text="Thoát", bg="#EEDC82", command=root.destroy)
thoat_button.place(x=460,y=390)
root.mainloop()
