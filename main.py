"""
module run app
"""
from tkinter import *
from tkinter import ttk
import Tab.Signin_page
from Tab.XoaSuaNhanVien import DanhSach

if __name__ == "__main__":
    root = Tk()
    DanhSach().pack()
    # Tab.Signin_page.login_page(root)

    root.mainloop()


