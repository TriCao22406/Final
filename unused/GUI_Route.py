import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Maxwell Co. Ltd")
        self.state("zoomed")
        self.resizable(True, True)


    def get_width(self):
        return self.winfo_width()

    def get_height(self):
        return self.winfo_height()

# Frame chính chứa tất cả widget của thẻ (để xóa một lần cho dễ)
class MainFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()
        self.pack(fill="both", expand=1)




