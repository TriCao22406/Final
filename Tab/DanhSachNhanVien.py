import csv
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
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

with open('../database/employees.csv', newline="", mode='r') as nv_csv:
    csv_reader = csv.reader(nv_csv)
    view["height"] = 50
    for row in csv_reader:
        view.insert(parent='', index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8],))

view.pack()
root.mainloop()
