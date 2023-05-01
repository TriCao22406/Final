import csv
import tkinter as tk
from tkinter import ttk

def xoanv():
    nv_xoa = view.selection()
    if nv_xoa:
        nv_in4 = view.item(nv_xoa)['values']
        view.delete(nv_xoa)
        a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
        with open(a, mode='r', newline='') as file_csv:
            reader = csv.reader(file_csv)
            rows = list(reader)
        for i, row in enumerate(rows):
            if row[0] == nv_in4[0] and row[1] == str(nv_in4[1]):
                del rows[i]
                break
        a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
        with open(a, mode='w', newline='') as file_csv:
            csv_writer = csv.writer(file_csv)
            csv_writer.writerows(rows)
        file_csv.close()

root = tk.Tk()
root.state("zoomed")
delete_button = tk.Button(root, text="Xóa", command=xoanv)
delete_button.pack(side="bottom", pady=5)
view = ttk.Treeview(root)

view["columns"] = ("First Name","Last Name","Email","Phone","Gender","Department","Job Title","Years Of Experience","Salary")
view.column("#0", stretch= tk.NO, width=0)
view.heading("#0", text="", anchor=tk.W)
view.heading("First Name", text="First Name")
view.heading("Last Name", text="Last Name")
view.heading("Email", text="Email")
view.heading("Phone", text="Phone")
view.heading("Gender", text="Gender")
view.heading("Department", text="Department")
view.heading("Job Title", text="Job Title")
view.heading("Years Of Experience", text="Years Of Experience")
view.heading("Salary", text="Salary")

with open('../database/employees.csv', newline="", mode='r') as nv_csv:
    csv_reader = csv.reader(nv_csv)
    view["height"] = 70
    for row in csv_reader:
        view.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],))
scrollbar_doc = ttk.Scrollbar(root, orient="vertical", command=view.yview)
scrollbar_ngang = ttk.Scrollbar(root, orient="horizontal", command=view.xview)
view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
scrollbar_doc.pack(fill="y", side="right")
view.configure()
scrollbar_ngang.pack(fill="x", side="bottom")
view.pack(fill="both", expand=True)


a = r"C:\Users\HP\Documents\GitHub\Final\database\employees.csv"
with open(a, mode='r', newline='') as file_csv:
    reader = csv.reader(file_csv)
    next(reader)
    for row in reader:
        view.insert("", tk.END, values=row)

view.pack()


root.mainloop()