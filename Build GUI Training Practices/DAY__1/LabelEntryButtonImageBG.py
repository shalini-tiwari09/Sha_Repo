#Label, Entry and Button with Image Background

from tkinter import *

win = Tk()
win.geometry("700x730")
bg_image = PhotoImage(file="11.png")
background = Label(win, image=bg_image)
background.place(x=0, y=0, relwidth=1, relheight=1)
win.title("Feedback Form")

heading1 = Label(win, text="CONTACT US" , bg = "black", fg="IndianRed",
                 padx=20, pady=15,
                 bd=5, relief="ridge", highlightthickness=1,
                 font=("Lucida Handwriting", 25, "bold underline"))
heading1.grid(row=0 , column= 0,columnspan=2, padx= 10, pady = 20)


heading2 = Label(win, text="We will get back to you asap!!!" , bg = "Black", 
                 fg="DarkGoldenrod", font=("Lucida Handwriting", 20, "bold"))
heading2.grid(row=1 , column= 0, columnspan=2, padx= 20, pady = 25)


f_name = Label(win, text="First Name" , bg = "Black", fg="IndianRed", 
               font=("Tw Cen MT Condensed", 15, "bold"))
f_name.grid(row=2 , column= 0, padx= 30, sticky="w")


l_name = Label(win, text="Last Name" , bg = "Black", fg="IndianRed", 
               font=("Tw Cen MT Condensed", 15, "bold"))
l_name.grid(row=2 , column= 1, padx= 10, sticky="w")


fname = Entry(win, bg = "pale goldenrod", fg="Black", 
              font=("Comic Sans MS", 18, "italic"))
fname.grid(row=3 , column= 0, padx= 20, pady = 10)


lname = Entry(win, bg = "peach puff", fg="Black", 
              font=("Comic Sans MS", 18, "italic"))
lname.grid(row=3 , column= 1, padx= 20, pady = 10)


lemail = Label(win, text="Email" , bg = "Black", fg="IndianRed", 
               font=("Tw Cen MT Condensed", 15, "bold"))
lemail.grid(row=4 , column= 0, padx= 25, pady = 10, sticky="w")


email = Entry(win , bg = "Wheat", fg="Black", 
              font=("Comic Sans MS", 18, "italic"), width = 42)
email.grid(row= 5, column= 0, columnspan=2, padx=30, pady = 10, sticky="w")


lphone = Label(win, text="Contact No." , bg = "Black", fg="IndianRed", 
               font=("Tw Cen MT Condensed", 15, "bold"))
lphone.grid(row= 6, column= 0, padx= 25, pady = 25, sticky="w")


lphnno = Entry(win , bg = "LightGoldenrodYellow", fg="Black", 
               font=("Comic Sans MS", 18, "italic"))
lphnno.grid(row= 6, column= 1, padx= 20, pady = 25, sticky="w")


bsend = Button(win, text="SEND" , bg = "DarkGoldenrod", fg="Black",width= 20, 
               font=("Lucida Handwriting", 15, "bold"),pady=8)
bsend.grid(row= 7, column= 0,columnspan=2, padx= 10, pady = 20)


callus = Label(win, text="You may also call us at 999-999-9999" , bg = "Black",
               fg="DarkGoldenrod",  font=("Pristina", 20, "bold"))
callus.grid(row= 8,column= 0,columnspan=2, padx= 10, pady = 10)


ldet = Label(win, text="@KeepSmiling" , bg = "Black", fg="Indianred", 
             font=("Lucida Handwriting", 12, "bold"))
ldet.grid(row= 9, column= 1, padx= 30, pady = 26, sticky="e")


win.mainloop()