from tkinter import *
from tkinter.ttk import *

# Main window setup
win = Tk()
win.geometry("1000x500")
win.configure(bg="SteelBlue", relief="solid", bd=10, highlightbackground="black")
win.title("Pizza App")

title = Label(win, text="Welcome to Pizza Hut", font=("Comic sans ms", 25, "bold"), background="SteelBlue", foreground = "Goldenrod")
title.grid(row=0, column=1, columnspan=2, padx = 60, pady=20)

# Labels for Pizza Type and Quantity
choice_lbl = Label(win, text="Select Your Fav Pizza:", font=("Comic sans ms", 15, "bold"), background="SteelBlue", foreground = "white")
choice_lbl.grid(row=1, column=0, padx=15, pady=10)

quantity_lbl = Label(win, text="Enter Quantity:", font=("Comic sans ms", 15, "bold"), background="SteelBlue", foreground = "white")
quantity_lbl.grid(row=2, column=0, padx=15, pady=10)

# Combobox for Pizza Type
pizza_type = StringVar()
p_type = Combobox(win, textvariable=pizza_type, width=25, font=("Comic sans ms", 12), foreground = "maroon")
p_type['values'] = ("Veg Extravaganza", "Garden Delight", "Plain Cheese", "Margarita", "Pepperoni")
p_type.grid(row=1, column=1, columnspan=3)
p_type.set("Veg Extravaganza")  # Default value

# Combobox for Quantity
num = IntVar()
numbers = Combobox(win, textvariable=num, width=25, foreground="maroon", font=("Comic sans ms", 12, "bold"))
numbers['values'] = tuple(range(1, 21))
numbers.grid(row=2, column=1, columnspan=3, padx=10)
numbers.set(1)  # Default value

# Radiobuttons for Size (Vertical Alignment) using `ttk` Style
size_lbl = Label(win, text="Select Size :", font=("Comic sans ms", 15, "bold"), background="SteelBlue", foreground = "white")
size_lbl.grid(row=2, column=3, columnspan=3, padx=10, pady=10)

# Define a style for Radiobuttons
style = Style()
style.configure("TRadiobutton", background="SteelBlue", foreground="white", font=("Comic sans ms", 16, "bold"))
style.configure("TButton", background="white", foreground="SteelBlue", font=("Comic sans ms", 16, "bold"))

size = StringVar()
size.set("Small")  # Default value

S = Radiobutton(win, text="S", variable=size, value="Small", style="TRadiobutton")
M = Radiobutton(win, text="M", variable=size, value="Medium", style="TRadiobutton")
L = Radiobutton(win, text="L", variable=size, value="Large", style="TRadiobutton")

# Place the Radiobuttons Vertically
S.grid(row=3, column=3, columnspan=2, padx=10, pady=1)
M.grid(row=4, column=3, columnspan=2, padx=10, pady=2)
L.grid(row=5, column=3, columnspan=2, padx=10, pady=2)

# Order Button and Display
def generateOrder():
    order = (
        f"You ordered {num.get()} {p_type.get()} {size.get()} Size pizza(s).")
    orders.config(text=order, justify="center", foreground = "goldenrod")

btn = Button(win, text="Order.....", width=15, command=generateOrder, style="TButton")
btn.grid(row=6, column=1, columnspan=3, pady=15)

orders = Label(win, text="Waiting for Your Order...\n", wraplength=500, font=("Comic sans ms", 14, "bold"), background="SteelBlue", foreground = "white")
orders.grid(row=7, column=0, columnspan=5, padx= 50, pady=5)

win.mainloop()
