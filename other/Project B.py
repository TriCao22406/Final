from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas as pd




class TrangThongTinCaNhan:
       def __init__(self, root):
              self.root = root
              self.root.geometry('1530x790+0+0')
              self.root.title("Employees Information System")


              # variables
              self.var_dep = StringVar()
              self.var_ID = StringVar()
              self.var_email = StringVar()
              self.var_Name = StringVar()
              self.var_born = StringVar()
              self.var_gender = StringVar()
              self.var_sal = StringVar()
              self.var_addr = StringVar()
              self.var_phone = StringVar()
              self.var_year = StringVar()

              lbl_title = Label(self.root, text='Employ Management System', font=('times new roman', 37, 'bold'),
                                fg="white",
                                bg='#f6a88c')
              lbl_title.place(x=0, y=0, width=1530, height=50)

              # logo
              img_logo = Image.open('../images/I1.jpg')
              img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
              self.photo_logo = ImageTk.PhotoImage(img_logo)

              self.logo = Label(self.root, image=self.photo_logo)
              self.logo.place(x=270, y=0, width=50, height=50)
              # image frame
              img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
              img_frame.place(x=0, y=50, width=1530, height=160)

              # 1st
              img1 = Image.open('../images/i3.jpg')
              img1 = img1.resize((540, 160), Image.ANTIALIAS)
              self.photo1 = ImageTk.PhotoImage(img1)

              self.imag_1 = Label(self.root, image=self.photo1)
              self.imag_1.place(x=0, y=0, width=540, height=160)

              # 2nd
              img2 = Image.open('../images/i5.jpg')
              img2 = img2.resize((540, 160), Image.ANTIALIAS)
              self.photo2 = ImageTk.PhotoImage(img2)

              self.imag_2 = Label(self.root, image=self.photo2)
              self.imag_2.place(x=540, y=0, width=540, height=160)

              # 3rd
              img3 = Image.open('../images/I1.jpg')
              img3 = img3.resize((540, 160), Image.ANTIALIAS)
              self.photo3 = ImageTk.PhotoImage(img3)

              self.imag_3 = Label(self.root, image=self.photo3)
              self.imag_3.place(x=1000, y=0, width=540, height=160)

              # main frame

              main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
              main_frame.place(x=1, y=220, width=1500, height=560)

              # upper frame
              upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text=' Employee Information',
                                       font=('times new roman', 17, 'bold'), fg="darkblue", bg='white')
              upper_frame.place(x=10, y=10, width=1480, height=270)

              # label and Entry fields
              lbl_dep = Label(upper_frame, text='Department', font=('arial', 11, 'bold'), fg="black", bg='white')
              lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

              combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('arial', 12, 'bold'),
                                       width=17,
                                       state='readonly')
              combo_dep['value'] = ('Select Department', 'HR', 'SE', 'IT')
              combo_dep.current(0)
              combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

              # name
              lbl_name = Label(upper_frame, text='Name', font=('arial', 11, 'bold'), fg='black', bg='white')
              lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)
              txt_name = ttk.Entry(upper_frame, textvariable=self.var_Name, font=('arial', 12, 'bold'))
              txt_name.grid(row=0, column=3, padx=2, pady=7)

              # ID
              lbl_ID = Label(upper_frame, text='ID', font=('arial', 11, 'bold'), bg='white')
              lbl_ID.grid(row=1, column=0, sticky=W, padx=2, pady=7)
              txt_ID = ttk.Entry(upper_frame, textvariable=self.var_ID, font=('arial', 12, 'bold'))
              txt_ID.grid(row=1, column=1, padx=2, pady=7, sticky=W)

              # Email
              lbl_email = Label(upper_frame, text='Email', font=('arial', 11, 'bold'), bg='white')
              lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)
              txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, font=('arial', 12, 'bold'))
              txt_email.grid(row=1, column=3, padx=2, pady=7)

               # Years of Experience
              lbl_ye = Label(upper_frame, text='Y.O.E', font=('arial', 11, 'bold'), bg='white')
              lbl_ye.grid(row=2, column=0, sticky=W, padx=2, pady=7)
              txt_ye = ttk.Entry(upper_frame, textvariable=self.var_year, font=('arial', 12, 'bold'))
              txt_ye.grid(row=2, column=1, padx=2, pady=7,sticky=W)


              # Address
              lbl_addr = Label(upper_frame, text='Address', font=('arial', 11, 'bold'), bg='white')
              lbl_addr.grid(row=3, column=2, sticky=W, padx=2, pady=7)
              txt_addr = ttk.Entry(upper_frame, textvariable=self.var_addr, font=('arial', 12, 'bold'))
              txt_addr.grid(row=3, column=3, padx=2, pady=7)

              # gender
              lbl_gen = Label(upper_frame, text='Gender', font=('arial', 11, 'bold'), fg="black", bg='white')
              lbl_gen.grid(row=2, column=2, padx=2, sticky=W)
              combo_gen = ttk.Combobox(upper_frame, textvariable=self.var_gender, font=('arial', 12, 'bold'),
                                       width=17, \
                                       state='readonly')
              combo_gen['value'] = ('Male', 'Female', 'Other')
              combo_gen.current(0)
              combo_gen.grid(row=2, column=3, padx=2, pady=10)

              # D.O.B
              lbl_born = Label(upper_frame, text='D.O.B', font=('arial', 11, 'bold'), bg='white')
              lbl_born.grid(row=3, column=0, sticky=W, padx=2, pady=7)
              txt_born = ttk.Entry(upper_frame, textvariable=self.var_born, width=22, font=('arial', 12, 'bold'))
              txt_born.grid(row=3, column=1, padx=2, pady=7, sticky=W)

              # salary
              lbl_sal = Label(upper_frame, text='Salary', font=('arial', 11, 'bold'), bg='white')
              lbl_sal.grid(row=4, column=0, sticky=W, padx=2, pady=7)
              txt_sal = ttk.Entry(upper_frame, textvariable=self.var_sal, width=22, font=('arial', 12, 'bold'))
              txt_sal.grid(row=4, column=1, padx=2, pady=7, sticky=W)

              # Phone
              lbl_phone = Label(upper_frame, text='Phone Number', font=('arial', 11, 'bold'), bg='white')
              lbl_phone.grid(row=4, column=2, sticky=W, padx=2, pady=7)
              txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22,
                                    font=('arial', 12, 'bold'))
              txt_phone.grid(row=4, column=3, padx=2, pady=7)

              # face
              img = Image.open('../images/i4.jpg')
              img = img.resize((500, 220), Image.ANTIALIAS)
              self.photo = ImageTk.PhotoImage(img)

              self.imag = Label(upper_frame, image=self.photo)
              self.imag.place(x=700, y=0, width=500, height=220)



              # Button frame
              button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
              button_frame.place(x=1290, y=20, width=170, height=210)

              btn_add = Button(button_frame, text='Save',command=self.add_data(), font=('arial', 15, 'bold'), width=13, bg='white',
                               fg='black')
              btn_add.grid(row=0, column=0, padx=1, pady=5)

              btn_update = Button(button_frame, text='Update', font=('arial', 15, 'bold'), width=13, bg='white',
                                  fg='black')
              btn_update.grid(row=1, column=0, padx=1, pady=5)

              btn_delete = Button(button_frame, text='Delete', font=('arial', 15, 'bold'), width=13, bg='white',
                                  fg='black')
              btn_delete.grid(row=2, column=0, padx=1, pady=5)

              btn_clear = Button(button_frame, text='Clear', font=('arial', 15, 'bold'), width=13, bg='white',
                                 fg='black')
              btn_clear.grid(row=3, column=0, padx=1, pady=5)

              # down frame
              down_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text=' Employee Information Table',
                                      font=('times new roman', 17, 'bold'), fg="darkblue", bg='white')
              down_frame.place(x=10, y=280, width=1480, height=270)

              # Search frame
              search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white',
                                        text='Search Employee Information',
                                        font=('times new roman', 11, 'bold'), fg='darkblue')
              search_frame.place(x=0, y=0, width=1470, height=60)

              search_by = Label(search_frame, text='Search by',
                                font=('times new roman', 13, 'bold'), fg='black', bg='white')
              search_by.grid(row=0, column=0, sticky=W, padx=5)

              # searching
              combo_txt_search = ttk.Combobox(search_frame, font=('arial', 12, 'bold'), width=18,
                                              state='readonly')
              combo_txt_search['value'] = ('Select Option', 'ID', 'Email')
              combo_txt_search.current(0)
              combo_txt_search.grid(row=0, column=1, padx=5, sticky=W)

              txt_search = ttk.Entry(search_frame, width=22, font=('arial', 12, 'bold'))
              txt_search.grid(row=0, column=2, padx=5)
              btn_search = Button(search_frame, text='Search', font=('arial', 12, 'bold'), width=14, fg='black',
                                  bg='white')
              btn_search.grid(row=0, column=3, padx=5)

              btn_ShowAll = Button(search_frame, text='Show All', font=('arial', 12, 'bold'), width=14,
                                   fg='black',
                                   bg='white')
              btn_ShowAll.grid(row=0, column=4, padx=5)

              # Employee table

              # Table Frame
              table_frame = Frame(down_frame, bd=3, relief=RIDGE)
              table_frame.place(x=0, y=60, width=1470, height=170)

              scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
              scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

              self.employees_table = ttk.Treeview(table_frame,column=('Name', 'ID', 'Dep', 'Email', 'D.O.B', 'Gender','Salary', 'Phone', 'Address','Y.O.E'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

              scroll_x.pack(side=BOTTOM, fill=X)
              scroll_y.pack(side=RIGHT, fill=Y)

              scroll_x.config(command=self.employees_table.xview)
              scroll_y.config(command=self.employees_table.yview)

              self.employees_table.heading('ID', text='ID')
              self.employees_table.heading('Name', text='Name')
              self.employees_table.heading('Email', text='Email')
              self.employees_table.heading('Dep', text='Department')
              self.employees_table.heading('D.O.B', text='D.O.B')
              self.employees_table.heading('Gender', text='Gender')
              self.employees_table.heading('Phone', text='Phone Number')
              self.employees_table.heading('Address', text='Address')
              self.employees_table.heading('Salary', text='Salary')
              self.employees_table.heading('Y.O.E', text='Years of Experience')

              self.employees_table['show'] = 'headings'

              self.employees_table.column('ID', width=100)
              self.employees_table.column('Name', width=100)
              self.employees_table.column('Email', width=100)
              self.employees_table.column('Dep', width=100)
              self.employees_table.column('D.O.B', width=100)
              self.employees_table.column('Salary', width=100)
              self.employees_table.column('Gender', width=100)
              self.employees_table.column('Phone', width=100)
              self.employees_table.column('Address', width=100)
              self.employees_table.column('Y.O.E', width=100)

              self.employees_table.pack(fill=BOTH, expand=1)

       # Function declaration
       def add_data(self):
              if self.var_ID.get() == "" or self.var_email.get() == "":
                     messagebox.showerror('Error', 'All fields are required')
              else:
                     try:
                            conn=pd.read_csv("../database/dataemployees.csv")

                            new_employee=[self.var_ID.get(),self.var_Name.get(),self.var_email.get(),self.var_dep.get(),self.var_born.get(),self.var_phone.get(),self.var_gender.get(),self.var_year.get(),self.var_addr.get(),self.var_sal.get()]
                            conn.loc[conn.shape[0]] = new_employee
                            conn.to_csv("database/dataemployees.csv", index=False)

                            """def hienthinv(cls):
                                   root2 = tk.Tk()
                                   root2.title("Hiển thị nhân viên")
                                   root2.state("zoomed")"""
                            conn.close()
                            messagebox.showinfo('Success','Employee has been added', parent=self.root)
                     except Exception as es:
                            messagebox.showerror('Error', f'Due To:{str(es)}',parent=self.root)







if __name__ == "__main__":
           root = Tk()
           obj=TrangThongTinCaNhan(root)
           root.mainloop()