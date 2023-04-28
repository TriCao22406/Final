from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import csv


def login_page():
    signup_windown.destroy()
    import signin


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def sucess(a, b):
    e = r"C:\Users\Admin\PycharmProjects\pythonProject\data.csv"
    with open(e, newline="", mode='r') as csv_file:
        got_reader = csv.reader(csv_file, delimiter=",",quoting=csv.QUOTE_NONE)
        for r in got_reader:
            if r[0] == usernameEntry.get():
                messagebox.showerror('Error', "Account already exists")
                return False
        with open(e, newline="", mode='a') as csv_new:
            s = [usernameEntry.get(), passwordEntry.get()]
            csv_write = csv.writer(csv_new,delimiter = ",")
            csv_write.writerow(s)
        return True


def connect_database():
    if emailEntry.get() == "" or usernameEntry.get() == "" or passwordEntry.get() == "" or confirmEntry.get() == "":
        messagebox.showerror("Invalid", "All Fields Are Required")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Invalid", "Password non-matching ")
    elif check.get() == 0:
        messagebox.showerror("invalid", "Please accept Terms & Conditions ")
    else:
        if sucess(usernameEntry, passwordEntry) == True:
            messagebox.showinfo("Successful", "Registration is successful")


signup_windown = Tk()
signup_windown.title(" Signup Page")
signup_windown.geometry('925x600+300+100')
signup_windown.resizable(False, False)
signup_windown.configure(bg="#fff")

img = Image.open(r'C:\Users\Admin\Downloads\login.png')
photo = ImageTk.PhotoImage(img)
Label(signup_windown, image=photo, bg='white').place(x=50, y=50)
frame = Frame(signup_windown, width=350, height=350, bg="white")
frame.place(x=510, y=70)
heading = Label(frame, text="Sign in", fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 24, 'bold'))
heading.place(x=120, y=3)

heading = Label(frame, text="CREAT AN ACCOUNT", font=("Microsoft YaHei UI Light", 19, "bold"), bg="white", fg="#57a1f8")
heading.grid(row=0, column=0, padx=10, pady=10)

email = Label(frame, text="Email", font=("Microsoft YaHei UI Light", 10, "bold"), bg="white", fg="#57a1f8")
email.grid(row=1, column=0, sticky="w", padx=25)
emailEntry = Entry(frame, width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
emailEntry.grid(row=2, column=0, sticky="w", padx=25, pady=(10, 0))

username = Label(frame, text="Username", font=("Microsoft YaHei UI Light", 10, "bold"), bg="white", fg="#57a1f8")
username.grid(row=3, column=0, sticky="w", padx=25)
usernameEntry = Entry(frame, width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
usernameEntry.grid(row=4, column=0, sticky="w", padx=25, pady=(10, 0))

password = Label(frame, text="Password", font=("Microsoft YaHei UI Light", 10, "bold"), bg="white", fg="#57a1f8")
password.grid(row=5, column=0, sticky="w", padx=25)
passwordEntry = Entry(frame, width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
passwordEntry.grid(row=6, column=0, sticky="w", padx=25, pady=(10, 0))

confirm = Label(frame, text="Confirm Password", font=("Microsoft YaHei UI Light", 10, "bold"), bg="white", fg="#57a1f8")
confirm.grid(row=7, column=0, sticky="w", padx=25)
confirmEntry = Entry(frame, width=30, font=("Microsoft YaHei UI Light", 10, "bold"), fg="black", bg="white")
confirmEntry.grid(row=8, column=0, sticky="w", padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame, text=" I agree with the Term & Conditions",
                                 font=("Microsoft YaHei UI Light", 10, "bold"), bg="white", fg="#57a1f8",
                                 activebackground="white", activeforeground="blue", cursor="hand2", variable=check,onvalue=1,offvalue=0)
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

signup_Button = Button(frame, text="Sign Up", font=("Microsoft YaHei UI Light", 12, "bold"), bg='#57a1f8', fg='white',
                       width=17, justify=CENTER, command=connect_database)
signup_Button.grid(row=10, column=0, pady=10)

alreadyaccont = Label(frame, text="Have an account?", font=("Open Sans", "9", "bold"), bg="white", fg="black")
alreadyaccont.grid(row=11, column=0, sticky="w", padx=60, pady=10)

login_Button = Button(frame, text="Sign in", font=("Open Sans", 9, "bold underline"), bg="white", fg="blue",
                      cursor="hand2", activebackground="white", activeforeground="blue", command=login_page)
login_Button.place(x=175, y=395)

signup_windown.mainloop()
