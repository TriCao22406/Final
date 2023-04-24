"""
module chính, có tác dụng điều hướng tới các cửa sổ khác nhau
"""
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Maxwell Co. Ltd")
        self.state("zoomed")


#Frame chính chứa tất cả widget của thẻ (để xóa một lần cho dễ)
class MainFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        self.pack(fill="both", expand=1)
