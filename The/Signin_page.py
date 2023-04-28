from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv





    root = Tk()
    root.title('Sign in')
    root.geometry('925x500+300+100')
    root.resizable(False, False)
    root.configure(bg="#fff")


    def signup_page(self):
      global root
      root.destroy()
      import signup









img = Image.open(r"C:\Users\Admin\Downloads\login.png")
photo = ImageTk.PhotoImage(img)
Label(root, image=photo, bg='white').place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=510, y=70)
heading = Label(frame, text="Sign in", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=120, y=3)

user = Entry(frame, width=25, border=0, fg="black", bg="white", font=('Microsoft YaHei UI Light', 12))
user.place(x=50, y=75)
user.insert(0, 'username')
Frame(frame, width=280, height=1, bg='black').place(x=40, y=100)


def on_enter1(e):
    a = user.get()
    if a == 'username':
        user.delete(0, 'end')


def on_leave1(e):
    a = user.get()
    if a == '':
        user.insert(0, "username")


user.bind('<FocusIn>', on_enter1)
user.bind('<FocusOut>', on_leave1)
# Tao ra cho nhap password
password = Entry(frame, width=25, border=0, fg="black", bg="white", font=('Microsoft YaHei UI Light', 12))
password.place(x=50, y=175)
password.insert(0, 'password')
Frame(frame, width=280, height=1, bg='black').place(x=40, y=200)
######
button_MODE = True
def hide():
    global button_MODE
    if button_MODE:
        hide_Button.config(text='Show')
        password.config(show="*")
        button_MODE= False
    else:
        hide_Button.config(text='Hide')
        password.config(show="")
        button_MODE = True

hide_Button = Button(frame,text="Hide",bd=0, bg="white",fg='#57a1f8',activeforeground="black",cursor="hand2"
                      ,font=('Microsoft YaHei UI Light',9),command=hide)
hide_Button.place(x=230,y=205)

def on_enter2(e):
    a = password.get()
    if a == 'password':
        password.delete(0, 'end')


def on_leave2(e):
    a = password.get()
    if a == '':
        password.insert(0, "password")


password.bind('<FocusIn>', on_enter2)
password.bind('<FocusOut>', on_leave2)
# Quản lý thông tin đăng nhập
class Dangnhap:
    thongtindangnhap = []

    def __init__(self):
        self.tendangnhap = user.get()
        self.matkhau = password.get()

    @classmethod
    def tim_taikhoan(cls, taikhoan):
        tendangnhap = user.get()
        matkhau = password.get()
        for i in range(len(cls.thongtindangnhap)):
            if tendangnhap == cls.thongtindangnhap[i].tendangnhap and matkhau == cls.thongtindangnhap[i].matkhau:
                return {"idx": i, 'inf': cls.thongtindangnhap[i]}
            elif tendangnhap == cls.thongtindangnhap[i].tendangnhap and matkhau != cls.thongtindangnhap[i].matkhau:
                return 0
            else:
                return -1


# tao dong hoi "Do you have an account?" va sign in

Button(frame, text="Sign in", border=0, width=30, pady=7, bg='#57a1f8', fg='white', justify=CENTER,
       font=('Microsoft YaHei UI Light', 10),command=docFileCSV).place(x=60, y=250)

########
label = Label(frame, text='Do you have an account ?', fg='black', font=('Microsoft YaHei UI Light', 10), bg='white',border=0)
label.place(x=60, y=300)
button = Button(frame, text='Creat an account', border=0, fg='#57a1f8', bg='white', activeforeground='black',command=signup_page).place(x=215, y=300)


root.mainloop()
