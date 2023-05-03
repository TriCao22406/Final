import tkinter as tk
import Tab.window1.QLNS_process as ns
import Tab.window1.ThongTinNhanVien as tt
class home(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__()

        fr1 = tk.Frame(self, height=30).pack(side=tk.TOP)

        button1 = tk.Button(self,border=2,text="Thêm nhân viên",bg='lavender',font=('arial',11,'bold'), command = self.themnv_page)
        button1.pack(side=tk.TOP,pady=10)


        button2= tk.Button(self,border=2,text="Thông tin nhân viên",bg='lavender',font=('arial',11,'bold'), command= self.tnnv_page)
        entry1= tk.Entry(self,width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
        entry1.pack(side=tk.TOP,pady=10)
        button2.pack(side=tk.TOP,pady=10)

    @staticmethod
    def themnv_page():
        ha = tk.Toplevel()
        ha.title("THÊM NHÂN VIÊN")
        ha.geometry('1000x750')
        ha.resizable(1, 1)


        ns.Window(ha)
        # canva = tk.Canvas(ha)
        # scrollbar_doc = ttk.Scrollbar(ha, orient="vertical", command=canva.yview)
        #
        # frame = tk.Frame(canva)
        # ns.Window(frame)
        # canva.create_window(0, 0, anchor='nw', window=frame)
        # canva.update_idletasks()
        #
        # canva.configure(scrollregion=canva.bbox('all'), yscrollcommand=scrollbar_doc.set)
        #
        # canva.pack(fill='both', expand=True, side='left')
        # scrollbar_doc.pack(fill='y', side='right')

        ha.mainloop()

    @staticmethod
    def tnnv_page():
        tuyen = tk.Toplevel()
        tuyen.geometry('1530x790+0+0')
        tuyen.title("Employee Management System")

        tt.TrangThongTinCaNhan(tuyen)

        tuyen.mainloop()
