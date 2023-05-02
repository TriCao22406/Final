from tkinter import *
from tkinter import ttk
from Tab.window1.Home_page import *
from Tab.window1.CoCauToChuc import *
from Tab.window1.XoaSuaNhanVien import *

class window1:
    def __init__(self):
        root = Tk()
        root.title("Maxwell Co. Ltd")
        root.state('zoomed')

        self.tab = ttk.Notebook()

        tab1 = home(self.tab)
        self.tab2= CoCau(self.tab)
        tab3 = DanhSach(self.tab)

        self.tab.add(tab1, text = "Trang chủ")
        self.tab.add(self.tab2, text = "Cơ cấu tổ chức")
        self.tab.add(tab3, text = "Danh sách nhân viên")

        self.tab.pack(expand=1, fill="both")

        self.tab.bind("<<NotebookTabChanged>>", self.tab_changed)

        root.mainloop()

    def tab_changed(self,event):
        if self.tab.index(self.tab.select()) == 1:
            self.tab2.after(200, self.tab2.draw_line_cond)


window1()