import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root).pack()
label = tk.Label(frame, text="Hello, world!")
label.place(relx=0.5, rely=0.5)
root.mainloop()
