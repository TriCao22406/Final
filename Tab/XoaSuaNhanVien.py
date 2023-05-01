import csv
import tkinter as tk
from tkinter import ttk
from DanhSachNhanVien import view

def xoanv():
    nv_xoa = view.selection
    if nv_xoa:
        nv_in4 = view.item(nv_xoa)['values']
        view.delete(nv_xoa)
        a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
        with open(a, mode='r', newline='') as file_csv:
            csv_reader =  csv.reader(file_csv)
            rows = list(csv_reader)
        for i, row in enumerate(rows):
            if row[0] == nv_in4[0] and row[1] == str(nv_in4[1]):
                del row[i]
                break
        a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
        with open(a, mode='r', newline='') as file_csv:
            csv_writer = csv.writer(file_csv)
            csv_writer.writerows(rows)

root =tk.Tk()
a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
with open(a, mode='r', newline='') as file_csv:
    csv_reader =  csv.reader(file_csv)
    next(csv_reader)
    for row in csv_reader:
        view.insert("", tk.END, values=row)

view.pack()
delete_button = tk.Button(root, text="Xóa", command=xoanv)
delete_button.pack()

root.mainloop()