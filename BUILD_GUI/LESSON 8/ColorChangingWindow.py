from tkinter import *
from tkinter import messagebox

# Function to update background color
def change_bg_color():
    selected_color = color_listbox.get(ANCHOR)
    if selected_color:
        win.config(bg=selected_color)
        color_label.config(bg=selected_color) 
    else:
        messagebox.showwarning("No Selection", "Please select a color from the list.")

# Function to add a new color to the listbox
def add_color():
    new_color = new_color_entry.get().strip()
    if new_color and new_color not in colors:
        colors.append(new_color)
        color_listbox.insert(END, new_color)
        new_color_entry.delete(0, END)
    else:
        messagebox.showwarning("Invalid Color", "Please enter a valid, non-duplicate color.")

# Function to remove selected color from the listbox
def remove_color():
    selected_color = color_listbox.get(ANCHOR)
    if selected_color:
        color_listbox.delete(ANCHOR)
        colors.remove(selected_color)
    else:
        messagebox.showwarning("No Selection", "Please select a color to remove.")

# Main window setup
win = Tk()
win.geometry("450x550")
win.title("Color Selector")

color_label = Label(win, text = "COLOR CHANGING WINDOW!!!", font=("Comic sans ms", 15, "bold"), foreground = "dark slate gray")
color_label.grid(row=0, column=0, columnspan=2, padx=45, pady=10)

# List of colors to populate the listbox
colors = ["Indian Red", "dark cyan", "Blue", "Teal", "Gold", "Dark Salmon", "Goldenrod", "Navy", "rosy brown", "Maroon", 
          "Olive", "Khaki", "Purple", "Pink", "White", "Black"]

# Listbox for color selection
color_listbox = Listbox(win, selectmode=SINGLE, height=15, width=30, font=("Comic sans ms", 8))
color_listbox.grid(row=1, column=0, columnspan=2, padx=50, pady=10)

# Populate listbox with initial colors
for color in colors:
    color_listbox.insert(END,color)

# Button to remove selected color from list
change_color_btn = Button(win, text="Change Background", command=change_bg_color, padx=20,font=("Comic sans ms", 10, "bold"))
change_color_btn.grid(row=2, column=0, pady=5, padx=40)

# Add button to change background color

remove_color_btn = Button(win, text="Remove Color", command=remove_color, font=("Comic sans ms", 10, "bold"))
remove_color_btn.grid(row=2, column=1,padx=40, pady=5)

# Entry box for adding new colors
new_color_entry = Entry(win, width=15, font=("Comic sans ms", 15), justify= "center")
new_color_entry.grid(row=4, column=0, columnspan=2, pady=10, padx=60)

# Button to add new color to list
add_color_btn = Button(win, text="Add Color", command=add_color, font=("Comic sans ms", 10, "bold"))
add_color_btn.grid(row=5, column=0, columnspan=2, padx=50, pady=10)

win.mainloop()
