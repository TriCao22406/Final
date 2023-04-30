import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Quản lý nhân sự")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tạo thẻ trong widget Notebook
the = tk.Frame(notebook)

# Thêm thẻ vào widget Notebook
notebook.add(the, text="Danh sách nhân viên")

dsnv = tk.Listbox(root, height=10)
dsnv.pack(padx=10, pady=10)


tk.Label(the, text="Nội dung của thẻ").pack(pady=10)

root.mainloop()
