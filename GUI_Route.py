"""
module chính, có tác dụng điều hướng tới các cửa sổ khác nhau
"""
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Maxwell Co. Ltd")
        self.state("zoomed")

        import Login

class MainFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.pack(fill="both", expand=1)