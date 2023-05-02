import tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image

window = Tk()
window.title('Hồ sơ công việc')
window.geometry('1000x700+500+300')

def pick_date(event):
    global cal, date_window

    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Chọn ngày")
    date_window.geometry('250x220+590+370')
    cal=Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
    cal.place(x=0, y=0)

    submit_btn=Button(date_window, text="Submit", command=grab_datein)
    submit_btn.place(x=80, y=190)
def grab_date():
    dob_entry.delete(0, END)
    dob_entry.insert(0, cal.get_date())
    date_window.destroy()

title = Label(text="THÔNG TIN NHÂN VIÊN", fg="black", font=("bold", 20))
title.place(x=360, y=30)

heading1 = Label(text="1. Thông tin cá nhân", fg="blue", font=(16))
heading1.place(x=30, y=70)


idLabel = Label(text = 'Mã NV', fg='white', bg='#569DAA', width = 10, anchor='w')
idLabel.place(x=60, y=120)
idText = Text(width=10, height=1)
idText.place(x=160, y=120)


hoten_Label = Label(text = 'Họ tên NV', fg='white', bg='#569DAA', width = 10, anchor='w')
hoten_Label.place(x=300, y=120)
hoten_Text = Text(width=37, height=1)
hoten_Text.place(x=400, y=120)


dob_label = Label(text="Ngày sinh", fg='white', bg='#569DAA', width = 10, anchor='w')
dob_label.place(x=60, y=160)

dob_entry = Entry(window, width=13)
dob_entry.place(x=160, y=160)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

gender = Label(text="Giới tính", fg='white', bg='#569DAA', width=10, anchor='w')
gender.place(x=300, y=160)
gioitinh=['Nam', 'Nữ', 'Khác']
gender_Text=ttk.Combobox(window, values=gioitinh, width=15)
gender_Text.place(x=400, y=160)
gender_Text.set("Chọn giới tính")


hocvan = Label(text="Học vấn", fg='white', bg='#569DAA', width=10, anchor='w')
hocvan.place(x=60, y=200)
hocvanText = Text(width=25, height=1)
hocvanText.place(x=160, y=200)

diachi = Label(text="Địa chỉ", fg='white', bg='#569DAA', width=10, anchor='w')
diachi.place(x=60, y=240)
diachiText = Text(width=25, height=1)
diachiText.place(x=160, y=240)

email = Label(text="Email", fg='white', bg='#569DAA', width=10, anchor='w')
email.place(x=60, y=280)
emailText = Text(width=25, height=1)
emailText.place(x=160, y=280)


sdt = Label(text="SĐT", fg='white', bg='#569DAA', width=10, anchor='w')
sdt.place(x=400, y=280)
sdtText = Text(width=25, height=1)
sdtText.place(x=500, y=280)

heading2 = Label(text="2. Thông tin công việc", fg="blue", font=(16))
heading2.place(x=30, y=320)

dob_label = Label(text="Ngày vào", fg='white', bg='#569DAA', width = 10, anchor='w')
dob_label.place(x=60, y=360)

dob_entry = Entry(window, width=13)
dob_entry.place(x=160, y=360)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

placeLabel = Label(text = 'Bộ phận', fg='white', bg='#569DAA', width = 10, anchor='w')
placeLabel.place(x=60, y=400)
placeText = Text(width=25, height=1)
placeText.place(x=160, y=400)

positionLabel = Label(text = 'Chức vụ', fg='white', bg='#569DAA', width = 10, anchor='w')
positionLabel.place(x=400, y=400)
positionText = Text(width=25, height=1)
positionText.place(x=500, y=400)

wageLabel = Label(text = 'Lương', fg='white', bg='#569DAA', width = 10, anchor='w')
wageLabel.place(x=60, y=440)

var =IntVar()
cb = IntVar()
Radiobutton(window, text='Lương gộp', variable=var, value=1).place(x=160, y=438)
Radiobutton(window, text='Lương ròng', variable=var, value=2).place(x=160, y=468)

luongLabel = Label(text='Lương cơ bản', fg='black')
luongLabel.place(x=260, y=440)
checkbutton = Checkbutton(window)
checkbutton.place(x=360, y=440)

luong13=Label(text="Lương tháng 13", fg="black")
luong13.place(x=260, y=470)
checkbutton13=Checkbutton(window)
checkbutton13.place(x=360, y=470)

theothang=Label(text="Trả theo tháng", fg="black")
theothang.place(x=397, y=440)
theothangcheckbtn=Checkbutton(window)
theothangcheckbtn.place(x=496, y=440)

theoca=Label(text="Trả theo ca", fg="black")
theoca.place(x=397, y=470)
theocacheckbtn=Checkbutton(window)
theocacheckbtn.place(x=496, y=470)

bacluong=Label(text="Bậc lương:", fg="black")
bacluong.place(x=540, y=440)
bacluong_Spinbox = Spinbox(from_=0, to=12, width=5)
bacluong_Spinbox.place(x=610, y=440)

#ngày hưởng
dob_label = Label(window, text="Ngày hưởng:", fg="black")
dob_label.place(x=540, y=470)

dob_entry = Entry(window, width=12)
dob_entry.place(x=625, y=470)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

cash=Label(text="Trả bằng tiền mặt", fg="black")
cash.place(x=160, y=500)
cashcheckbtn=Checkbutton(window)
cashcheckbtn.place(x=265, y=500)

bank=Label(text="Trả qua ngân hàng", fg="black")
bank.place(x=160, y=530)
bankcheckbtn=Checkbutton(window)
bankcheckbtn.place(x=265, y=530)

namebank = Label(text="Tên ngân hàng:", fg="black")
namebank.place(x=310, y=530)
name=['BIDV', 'SCB', 'VCB', 'AGRIBANK', 'VIETTINBANK', 'TECHCOMBANK', 'MBBANK']
namebank_cbb=ttk.Combobox(window, values=name, width=15)
namebank_cbb.set("Chọn ngân hàng")
namebank_cbb.place(x=400, y=530)

stk = Label(text="STK:", fg="black")
stk.place(x=540, y=530)
stk_Text=Text(width=15, height=1)
stk_Text.place(x=580, y=530)

bhytLabel = Label(text = 'BHYT', fg='white', bg='#569DAA', width = 10, anchor='w')
bhytLabel.place(x=60, y=570)
checkbutton = Checkbutton(window)
checkbutton.place(x=160, y=570)

#Mã BHYT
ma = Label(window, text="Mã BHYT: ", fg="black")
ma.place(x=240, y=570)
ma_text=Text(width=20, height=1)
ma_text.place(x=310, y=570)

# Từ ngày

dob_label = Label(window, text="Từ ngày: ", fg="black")
dob_label.place(x=540, y=570)

dob_entry = Entry(window, width=12)
dob_entry.place(x=600, y=570)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)


dob_label = Label(window, text="Đến ngày: ", fg="black")
dob_label.place(x=540, y=600)

dob_entry = Entry(window, width=12)
dob_entry.place(x=600, y=600)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

#Chọn bệnh viện
bv_label = Label(window, text="Bệnh viện: ", fg="black")
bv_label.place(x=160, y=600)
bv = ["Bệnh viện Thủ Đức", "Bệnh viện Chợ Rẫy", "Bệnh viên Quân y 175", "Bệnh viện Bệnh nhiệt đới"]
combobox=ttk.Combobox(window, values=bv, width=37)
combobox.place(x=230, y=600)
combobox.set("Chọn bệnh viện")


#bhxh
bhxhLabel = Label(text = 'BHXH', fg='white', bg='#569DAA', width = 10, anchor='w')
bhxhLabel.place(x=60, y=630)
checkbutton = Checkbutton(window)
checkbutton.place(x=160, y=630)

#Mã BHXH
mabhxh = Label(window, text="Mã BHXH: ", fg="black")
mabhxh.place(x=240, y=630)
mabhxh_text=Text(width=20, height=1)
mabhxh_text.place(x=310, y=630)

#từ ngày
dob_label = Label(window, text="Từ ngày: ", fg="black")
dob_label.place(x=540, y=630)

dob_entry = Entry(window, width=12)
dob_entry.place(x=600, y=630)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

#đến ngày
dob_label = Label(window, text="Đến ngày: ", fg="black")
dob_label.place(x=540, y=660)

dob_entry = Entry(window, width=12)
dob_entry.place(x=600, y=660)
dob_entry.insert(0, "dd/mm/yyyy")
dob_entry.bind("<1>", pick_date)

#Chọn nơi cấp
noicap_label = Label(window, text="Nơi cấp: ", fg="black")
noicap_label.place(x=160, y=660)
noicap = ['Hà Nội', 'Hồ Chí Minh']
combobox1=ttk.Combobox(window, values=noicap, width=37)
combobox1.place(x=230, y=660)
combobox1.set("Chọn nơi cấp")

width = 200
height = 280
img = Image.open(r"C:\Users\LAPTOP\Downloads\z3718417799627_7046ee92d3b87fb5986ddba484aee57f.jpg")
img = img.resize((width, height), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
b = Label(window, image=photoImg, width=300)
b.place(x=700, y=120)


save = Button(text="Lưu thông tin", bg="blue", fg="white", width=12, height=2)
save.place(x=815, y=450)

quit = Button(text="Thoát", bg="red", fg="white", width=12, height=2)
quit.place(x=815, y=510)


window.mainloop()

