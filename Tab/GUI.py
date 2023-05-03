import tkinter as tk
from tkinter import scrolledtext

class App(tk.Tk):
    def __init__(self):
        super().__init__()

    def change_meta(self,tle,geo=None):
        self.title(tle)
        self.geometry(geo)

    def full_hd(self):
        self.state("zoomed")

    def elastic(self, ye):
        if ye == "real":
            self.resizable(1,1)
        elif ye == "x":
            self.resizable(1,0)
        elif ye == "y":
            self.resizable(0,1)
        elif ye == "no":
            self.resizable(0,0)

    def get_width(self):
        return self.winfo_width()

    def get_height(self):
        return self.winfo_height()

# Frame chính chứa tất cả widget của thẻ (để xóa một lần cho dễ)
class MainFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        self.pack(fill="both", expand=1)




