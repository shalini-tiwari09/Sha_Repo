from tkinter import *

repl = Tk()
repl.config(bg="Black")
repl.geometry("600x400")

template_label1= Label(repl, text = "Pick a template",background='grey',
            foreground='white',bd=8).place(x= 30, y = 50)

template_user1 = Entry(repl, width = 30,bd=3).place(x = 30, y = 100)


template_label2= Label(repl, text = "Name your project",background='grey',
            foreground='white', bd=8).place(x= 350, y = 50)

template_user2 = Entry(repl, width = 30,bd=3).place(x = 350, y = 100)

create_btn = Button(repl, text = "+ Create repl",background="royal blue", foreground='white', bd=8).place(x = "350", y = "280")

repl.mainloop()


