import tkinter as tk
import csv
from DanhSachNhanVien import *
# chưa có xong bị lỗi rùi mai sửa tiếp
root =tk.Tk()
root.geometry('700x500')
def xoa_nv():
    manv_xoa = view.selection()[0]
    values = view.item(manv_xoa)['values']
    a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
    with open(a, mode='r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        for i, row in enumerate(rows):
            if row == values:
                rows.pop(i)
                break
    a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
    with open(a, mode='r', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    view.delete(manv_xoa)

delete_button = tk.Button(root, text="Xóa", command=xoa_nv)
delete_button.pack()

root.mainloop()