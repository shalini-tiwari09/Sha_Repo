from tkinter import *

win = Tk()
win.config(background = "black")
win.geometry("760x400")

label1 = Label(win, text = "Label1", 
               bg="olive", fg="white", 
               height = 4, width=20,
               justify = "left",
               anchor= "ne",
               bd = 5, relief=RAISED,
               font=("comic sans ms", 15, "bold"))
label1.grid(row = 0, column = 0)

label2 = Label(win, text = "Label2", 
               bg="dark goldenrod", fg="white", 
               height = 4, width=20, 
               justify = "left",  
               anchor= "s",
               bd = 5, relief=GROOVE,       
               font=("comic sans ms", 15, "bold"))
label2.grid(row = 0, column = 1)

label3 = Label(win, text = "Label3", 
               bg="teal", fg="white", 
               height = 4, width=20,
               justify = "right",
               anchor= "nw",
               bd = 5, relief=SUNKEN,
               font=("comic sans ms", 15, "bold"))
label3.grid(row = 0, column = 2)

label4 = Label(win, text = "Label4", 
               bg="steel blue", fg="white", 
               height = 4, width=40,
               anchor= "sw",
               bd = 5, relief=RIDGE,
               font=("comic sans ms", 15, "bold"))
label4.grid(row = 1, column = 0, columnspan = 2, ipadx= 3)

label5 = Label(win, text = "Label5", 
               bg="purple", fg="white", 
               height = 4, width=20,
               anchor= "se",
               bd = 5, relief=FLAT,
               font=("comic sans ms", 15, "bold"))
label5.grid(row = 1, column = 2)

win.mainloop()