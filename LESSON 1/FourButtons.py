from tkinter import *

templ = Tk()
templ.config(background = "Black")
templ.geometry("500x400")

top_button = Button(templ, text= "Top").place(x=10, y=10)
bottom_button = Button(templ, text= "Bottom").place(x=430, y=370)
right_button = Button(templ, text= "Right").place(x=460, y=10)
left_button = Button(templ, text= "Left").place(x=10, y=370)

templ.mainloop()