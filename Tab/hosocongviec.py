import tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image

##hellloo
window = Tk()
window.title('Hồ sơ công việc')
window.geometry('1000x700+500+300')


dateLabel = Label(text = 'Ngày vào', fg='white', bg='#569DAA', width = 15, anchor='w')
dateLabel.place(x=30, y=50)
dateText = Text(width=50, height=1)
dateText.place(x=186, y=50)

bophan_Label = Label(text = 'Bộ phận', fg='white', bg='#569DAA', width = 15, anchor='w')
bophan_Label.place(x=30, y=85)
bophan_Text = Text(width=50, height=1)
bophan_Text.place(x=186, y=85)

placeLabel = Label(text = 'Nơi làm', fg='white', bg='#569DAA', width = 15, anchor='w')
placeLabel.place(x=30, y=120)
placeText = Text(width=50, height=1)
placeText.place(x=186, y=120)

positionLabel = Label(text = 'Chức vụ', fg='white', bg='#569DAA', width = 15, anchor='w')
positionLabel.place(x=30, y=155)
positionText = Text(width=50, height=1)
positionText.place(x=186, y=155)

wageLabel = Label(text = 'Lương', fg='white', bg='#569DAA', width = 15, anchor='w')
wageLabel.place(x=30, y=190)

var =IntVar()
cb = IntVar()
Radiobutton(window, text='Lương gộp', variable=var, value=1).place(x=186, y=190)
Radiobutton(window, text='Lương ròng', variable=var, value=2).place(x=186, y=220)
luongLabel = Label(text='Lương tháng', fg='black')
luongLabel.place(x=300, y=192)
checkbutton = Checkbutton(window)
checkbutton.place(x=380, y=192)

luong13=Label(text="Lương tháng 13", fg="black")
luong13.place(x=430, y=192)
checkbutton13=Checkbutton(window)
checkbutton13.place(x=520, y=192)

theothang=Label(text="Trả theo tháng", fg="black")
theothang.place(x=300, y=222)
theothangcheckbtn=Checkbutton(window)
theothangcheckbtn.place(x=380, y=222)

theoca=Label(text="Trả theo ca", fg="black")
theoca.place(x=430, y=222)
theocacheckbtn=Checkbutton(window)
theocacheckbtn.place(x=520, y=222)

bacluong=Label(text="Bậc lương:", fg="black")
bacluong.place(x=186, y=255)
bac=[]
cbb=ttk.Combobox(window, values=bac, width=50)

def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Chọn ngày")
    date_window.geometry('250x220+590+370')
    cal=Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
    cal.place(x=0, y=0)
    submit_btn=Button(date_window, text="Submit", command=ngayhuong)
    submit_btn.place(x=80, y=190)
def ngayhuong():
    dobout_entry.delete(0, END)
    dobout_entry.insert(0, cal.get_date())
    date_window.destroy()

ngayhuongLabel = Label(window, text="Ngày hưởng:", fg="black")
ngayhuongLabel.place(x=350, y=255)

ngayhuong_entry = Entry(window, width=12)
ngayhuong_entry.place(x=430, y=255)
ngayhuong_entry.insert(0, "dd/mm/yyyy")
ngayhuong_entry.bind("<1>", pick_date)

cash=Label(text="Trả bằng tiền mặt", fg="black")
cash.place(x=186, y=285)
cashcheckbtn=Checkbutton(window)
cashcheckbtn.place(x=285, y=285)

bank=Label(text="Trả qua ngân hàng", fg="black")
bank.place(x=350, y=285)
bankcheckbtn=Checkbutton(window)
bankcheckbtn.place(x=455, y=285)


width = 200
height = 280
img = Image.open(r"C:\Users\LAPTOP\Downloads\z3718417799627_7046ee92d3b87fb5986ddba484aee57f.jpg")
img = img.resize((width, height), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)
b = Label(window, image=photoImg, width=300)
b.place(x=700, y=50)

bhytLabel = Label(text = 'BHYT', fg='white', bg='#569DAA', width = 15, anchor='w')
bhytLabel.place(x=30, y=320)
checkbutton = Checkbutton(window)
checkbutton.place(x=186, y=320)

#Mã BHYT
ma = Label(window, text="Mã BHYT: ", fg="black")
ma.place(x=186, y=350)
ma_text=Text(width=25, height=1)
ma_text.place(x=250, y=350)

# Từ ngày
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
def grab_datein():
    dobin_entry.delete(0, END)
    dobin_entry.insert(0, cal.get_date())
    date_window.destroy()

dobin_label = Label(window, text="Từ ngày: ", fg="black")
dobin_label.place(x=186, y=380)

dobin_entry = Entry(window, width=12)
dobin_entry.place(x=242, y=380)
dobin_entry.insert(0, "dd/mm/yyyy")
dobin_entry.bind("<1>", pick_date)

#Đến ngày
def pick_date(event):
    global cal, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Chọn ngày")
    date_window.geometry('250x220+590+370')
    cal=Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
    cal.place(x=0, y=0)
    submit_btn=Button(date_window, text="Submit", command=grab_dateout)
    submit_btn.place(x=80, y=190)
def grab_dateout():
    dobout_entry.delete(0, END)
    dobout_entry.insert(0, cal.get_date())
    date_window.destroy()

dobout_label = Label(window, text="Đến ngày: ", fg="black")
dobout_label.place(x=340, y=380)

dobout_entry = Entry(window, width=12)
dobout_entry.place(x=407, y=380)
dobout_entry.insert(0, "dd/mm/yyyy")
dobout_entry.bind("<1>", pick_date)

#Chọn bệnh viện
bv_label = Label(window, text="Bệnh viện: ", fg="black")
bv_label.place(x=186, y=410)
bv = ["Bệnh viện Thủ Đức", "Bệnh viện Chợ Rẫy", "Bệnh viên Quân y 175", "Bệnh viện Bệnh nhiệt đới"]
combobox=ttk.Combobox(window, values=bv, width=50)
combobox.place(x=250, y=410)
combobox.set("Chọn bệnh viện")



bhxhLabel = Label(text = 'BHXH', fg='white', bg='#569DAA', width = 15, anchor='w')
bhxhLabel.place(x=30, y=440)
checkbutton = Checkbutton(window)
checkbutton.place(x=186, y=440)

#Mã BHXH
mabhxh = Label(window, text="Mã BHXH: ", fg="black")
mabhxh.place(x=186, y=470)
mabhxh_text=Text(width=25, height=1)
mabhxh_text.place(x=250, y=470)



dobin_label = Label(window, text="Từ ngày: ", fg="black")
dobin_label.place(x=186, y=500)

dobin_entry = Entry(window, width=12)
dobin_entry.place(x=242, y=500)
dobin_entry.insert(0, "dd/mm/yyyy")
dobin_entry.bind("<1>", pick_date)


dobout_label = Label(window, text="Đến ngày: ", fg="black")
dobout_label.place(x=340, y=500)

dobout_entry = Entry(window, width=12)
dobout_entry.place(x=407, y=500)
dobout_entry.insert(0, "dd/mm/yyyy")
dobout_entry.bind("<1>", pick_date)

#Chọn nơi cấp
noicap_label = Label(window, text="Nơi cấp: ", fg="black")
noicap_label.place(x=186, y=530)
noicap = ['Hà Nội', 'Hồ Chí Minh']
combobox1=ttk.Combobox(window, values=noicap, width=50)
combobox1.place(x=250, y=530)
combobox1.set("Chọn nơi cấp")




window.mainloop()

