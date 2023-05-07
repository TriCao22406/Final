import tkinter as tk
from tkinter import ttk
from Tab.GUI import App
from Tab.window1.Home_page import home
from Tab.window1.CoCauToChuc import CoCau
from Tab.window1.DanhSachNhanVien import DanhSach

class window1:
    def __init__(self):
        root = App()
        root.change_meta("Maxwell Co. Ltd")
        root.full_hd()
        root.elastic("real")

        self.tab = ttk.Notebook()

        tab1 = home(self.tab)
        self.tab2= CoCau(self.tab)
        tab3 = DanhSach(self.tab)

        self.tab.add(tab1, text = "Trang chủ")
        self.tab.add(self.tab2, text = "Cơ cấu tổ chức")
        self.tab.add(tab3, text = "Danh sách nhân viên")

        self.tab.pack(expand=1, fill="both",side=tk.TOP)

        self.tab.bind("<<NotebookTabChanged>>", self.tab_changed)

        root.mainloop()


    def tab_changed(self,event):
        if self.tab.index(self.tab.select()) == 1:
            self.tab2.after(100, self.tab2.draw_line_cond)