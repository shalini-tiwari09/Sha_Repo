#Using different properties to specify where a widget and texts to be positioned
#fonts, dimensions, colors- backgrounds and font colors 

from tkinter import *

win = Tk()
win.config(background = "black")
win.geometry("745x450")

label1 = Label(win, text = "Label1", 
               bg="olive", fg="white", 
               height = 4, width=20,
               anchor= "ne",
               font=("comic sans ms", 15, "bold"))
label1.grid(row = 0, column = 0)

label2 = Label(win, text = "Label2", 
               bg="dark goldenrod", fg="white", 
               height = 4, width=20,   
               anchor= "s",            
               font=("comic sans ms", 15, "bold"))
label2.grid(row = 0, column = 1)

label3 = Label(win, text = "Label3", 
               bg="teal", fg="white", 
               height = 4, width=20,
               anchor= "nw",
               font=("comic sans ms", 15, "bold"))
label3.grid(row = 0, column = 2)

label4 = Label(win, text = "Label4", 
               bg="steel blue", fg="white", 
               height = 4, width=40,
               anchor= "sw",
               font=("comic sans ms", 15, "bold"))
label4.grid(row = 1, column = 0, columnspan = 2, ipadx= 3)

label5 = Label(win, text = "Label5", 
               bg="purple", fg="white", 
               height = 4, width=20,
               anchor= "se",
               font=("comic sans ms", 15, "bold"))
label5.grid(row = 1, column = 2)

win.mainloop()