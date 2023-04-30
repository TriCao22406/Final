import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widget Notebook")

# Tạo widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tạo thẻ trong widget Notebook
the = tk.Frame(notebook)

# Thêm thẻ vào widget Notebook
notebook.add(the, text="Danh sách nhân viên")

tk.Label(the, text="Nội dung của thẻ").pack(pady=10)

root.mainloop()
