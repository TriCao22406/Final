"""
module run app
"""
from tkinter import *
import Tab.Signin_page

if __name__ == "__main__":
    root = Tk()

    Tab.Signin_page.login_page(root)

    root.mainloop()