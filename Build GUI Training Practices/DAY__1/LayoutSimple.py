from tkinter import *

win = Tk()
win.config(background = "black")
win.geometry("670x400")

label1 = Label(win, text = "Label1" , bg="olive", fg="white", height = 5, width=30)
label1.grid(row = 0, column = 0, ipadx = 5)

label2 = Label(win, text = "Label2" , bg="dark goldenrod", fg="white", height = 5, width=30)
label2.grid(row = 0, column = 1, ipadx = 5)

label3 = Label(win, text = "Label3" , bg="teal", fg="white", height = 5, width=30)
label3.grid(row = 0, column = 2, ipadx = 5)

label4 = Label(win, text = "Label4" , bg="steel blue", fg="white", bd = 2, height = 5, width=60)
label4.grid(row = 1, column = 0, columnspan = 2, ipadx = 13)

label5 = Label(win, text = "Label5" , bg="purple", fg="white", bd = 2, height = 5, width=30)
label5.grid(row = 1, column = 2, ipadx = 5)

win.mainloop()