import tkinter as tk
import Tab.QLNS_process as ns

class home(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("trang chủ")
        self.geometry("300x300")
        self.resizable(False,False)

        button1 = tk.Button(self,border=2,text="Thêm nhân viên",bg='lavender',font=('arial',11,'bold'), command = self.themnv_page)
        button1.grid(column=0,row=0)

        def themnv(root):
            root.title("THÊM NHÂN VIÊN")
            root.geometry('900x500+200+100')
            root.resizable(False, False)



        button2= tk.Button(self,border=2,text="Thông tin nhân viên",bg='lavender',font=('arial',11,'bold'))
        entry1= tk.Entry(self,width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
        entry1.grid(column=0,row=1)
        button2.grid(column=0,row=2)
        self.mainloop()

    def themnv_page(self):
        self.destroy()

        root = tk.Tk()
        root.title("THÊM NHÂN VIÊN")
        root.geometry('900x500+200+100')
        root.resizable(False, False)

        ns.Window(master=root)


