
from QLNS_process import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk





class TrangThongTinCaNhan:

        def __init__(self, root):
               self.root = root
               self.root.geometry('1530x790+0+0')
               self.root.title("Employee Management System")

               lbl_title=Label(self.root,text='Employ Management System', font=('times new roman', 37, 'bold'),fg="white",
                                bg='#f6a88c')
               lbl_title.place(x=0, y=0, width=1530, height=50)

               #logo
               img_logo= Image.open('nguyen-tac-tuyen-dung-nhan-su-4.jpg')
               img_logo= img_logo.resize((50,50),Image.ANTIALIAS)
               self.photo_logo=ImageTk.PhotoImage(img_logo)

               self.logo=Label(self.root,image=self.photo_logo)
               self.logo.place(x=270, y=0, width=50, height=50)
                # image frame
               img_frame=Frame(self.root,bd=2, relief=RIDGE,bg='white')
               img_frame.place(x=0,y=50,width=1530,height=160)

               #1st
               img1= Image.open('2.jpg')
               img1= img1.resize((540,160), Image.ANTIALIAS)
               self.photo1=ImageTk.PhotoImage(img1)

               self.imag_1=Label(self.root,image=self.photo1)
               self.imag_1.place(x=0, y=0, width=540, height=160)

               #2nd
               img2= Image.open('nguyen-tac-tuyen-dung-nhan-su-4.jpg')
               img2= img2.resize((540,160), Image.ANTIALIAS)
               self.photo2=ImageTk.PhotoImage(img2)

               self.imag_2=Label(self.root,image=self.photo2)
               self.imag_2.place(x=540, y=0, width=540, height=160)

               #3rd
               img3= Image.open('3.jpg')
               img3= img3.resize((540,160), Image.ANTIALIAS)
               self.photo3=ImageTk.PhotoImage(img3)

               self.imag_3=Label(self.root,image=self.photo3)
               self.imag_3.place(x=1000, y=0, width=540, height=160)


               #main frame

               main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
               main_frame.place(x=1, y=220, width=1500, height=560)

               # upper frame
               upper_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text= ' Employee Information',
                                      font=('times new roman', 17, 'bold'),fg="darkblue",bg='white')
               upper_frame.place(x=10, y=10, width=1480,height=270)

               # label and Entry fields
               lbl_dep=Label(upper_frame,text='Department',font=('arial', 11, 'bold'),fg="black",bg='white')
               lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
               combo_dep=ttk.Combobox(upper_frame,font=('arial', 12, 'bold'),width=17, state='readonly')
               combo_dep['value'] = ('Select Department', 'HR', 'SE', 'Manager')
               combo_dep.current(0)
               combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W )

               #name
               lbl_name = Label(upper_frame, text='Name', font=('arial', 11, 'bold'),bg='white')
               lbl_name.grid(row=0, column=2,  sticky=W,padx=2,pady=7)
               txt_name=ttk.Entry(upper_frame,width=22,font=('arial', 12, 'bold'))
               txt_name.grid(row=0,column=3,padx=2,pady=7,sticky=W )

               #Email
               lbl_email = Label(upper_frame, text='Email', font=('arial', 11, 'bold'),bg='white')
               lbl_email.grid(row=0, column=2,  sticky=W,padx=2,pady=7)
               txt_email=ttk.Entry(upper_frame,width=22,font=('arial', 12, 'bold'))
               txt_email.grid(row=0,column=3,padx=2,pady=7,sticky=W )




               # down frame
               down_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text= ' Employee Information Table',
                                      font=('times new roman', 17, 'bold'),fg="darkblue",bg='white')
               down_frame.place(x=10, y=280, width=1480,height=270)






if __name__=="__main__":
       root=Tk()
       obj= TrangThongTinCaNhan(root)
       root.mainloop()