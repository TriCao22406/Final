import csv
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Danh sách nhân viên")
root.state("zoomed")
view = ttk.Treeview()

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

with open('../database/employees.csv', newline="", mode='r', encoding='utf-8') as nv_csv:
    csv_reader = csv.reader(nv_csv)
    view["height"] = 50
    for row in csv_reader:
        view.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],))
scrollbar_doc = ttk.Scrollbar(root, orient="vertical", command=view.yview)
scrollbar_ngang = ttk.Scrollbar(root, orient="horizontal", command=view.xview)
view.configure(yscrollcommand=scrollbar_doc.set, xscrollcommand=scrollbar_ngang.set)
scrollbar_doc.pack(fill="y", side="right")
view.configure()
scrollbar_ngang.pack(fill="x", side="bottom")
view.pack(fill="both", expand=True)


view.pack()
root.mainloop()
