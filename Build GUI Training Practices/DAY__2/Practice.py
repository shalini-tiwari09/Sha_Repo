from tkinter import *

# Create the main window
root = Tk()
root.geometry("950x700")
root.title("Scrollable Listbox and Expandable Frames")
root.config(background="Black")

# Configure the root grid to allow dynamic resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# Frame 1: Listbox with Scrollbar and Buttons
frame1 = LabelFrame(root, text="Listbox Operations", bg="olive", 
                    font=("Monotype Corsiva", 15, "bold"), fg = "mint cream",
                    padx=10, pady=10, bd=4, relief = "groove")
frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Configure frame1 to expand
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

# Scrollbar for Listbox
scrollbar = Scrollbar(frame1, orient=VERTICAL)

# Preloaded idioms
idioms = [
    "A blessing in disguise.",
    "A dime a dozen.",
    "Beat around the bush.",
    "Better late than never.",
    "Bite the bullet.",
    "Break the ice.",
    "Call it a day.",
    "Cut corners.",
    "Get out of hand.",
    "Hit the sack.",
    "Let the cat out of the bag.",
    "Miss the boat.",   
    "Hit the nail on the head.",
    "In the same boat.",
    "Out of the blue.",
    "On the ball.",
    "Pull someone's leg.",
    "Speak of the devil.",
    "Under the weather.", 
    "Burning the midnight oil.",
    "Barking up the wrong tree.",
    "Cost an arm and a leg.",
    "Throw in the towel.",
    "By the skin of your teeth.",
    "Back to the drawing board.",
    "Cry over spilled milk.",
    "A picture is worth a thousand words.",
]

# Listbox with scrollbar
listbox = Listbox(
    frame1, width =40, height= 150,
    bg="pale goldenrod", fg="olive",
    font=("Comic sans ms", 14), 
    yscrollcommand=scrollbar.set
)
listbox.grid(row=0, column=0, sticky="nsew", pady=10)

# Configure scrollbar to work with Listbox
scrollbar.config(command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Add preloaded idioms to Listbox
for idiom in idioms:
    listbox.insert(END, idiom)

# Add Item Function
def add_item():
    new_item = item_entry.get()
    if new_item:
        listbox.insert(END, new_item)
        item_entry.delete(0, END)

# Delete Selected Item Function
def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

# Show Selected Item Function
def show_selected():
    selected = listbox.curselection()
    if selected:
        selected_item = listbox.get(selected)
        label_selected.config(text=f"Selected Item: \n\n{selected_item}", 
                              fg="saddle brown", font=("Comic sans ms", 14, "bold underline"))
        
# Entry Widget for Adding New Items
item_entry = Entry(frame1, font=("Arial", 15), bd=3, relief="sunken")
item_entry.grid(row=1, column=0, pady=10, sticky="ew", columnspan=2)

btn_add = Button(frame1, text="Add", command=add_item,
                 bg="pale goldenrod", fg="olive drab",
                font=("Comic sans ms", 14))
btn_add.grid(row=2, column=0, pady=15, sticky="ew")

btn_delete = Button(frame1, text="Delete", command=delete_item, 
                    bg="pale goldenrod", fg="maroon",
                    font=("Comic sans ms", 14))
btn_delete.grid(row=3, column=0, pady=15, sticky="ew")

btn_show = Button(frame1, text="Show Selected", command=show_selected, 
                bg="pale goldenrod", fg="black",
                font=("Comic sans ms", 14))
btn_show.grid(row=4, column=0, pady=15, sticky="ew")

# Label to display selected item
label_selected = Label(frame1, text="Selected Item: None", 
                       bg="pale goldenrod", fg="olive",height=3, width=60,
                       font=("Comic sans ms", 12))
label_selected.grid(row=5, column=0, columnspan=2, pady=10)

# Frame 2: Teen Adventure Planner
frame2 = LabelFrame(root, text="Teen Adventure Planner", bg= "purple",
                    font=("Monotype Corsiva", 15, "bold"), fg = "mint cream",
                    bd=4, relief = "groove", padx=20, pady=20)
frame2.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

# Configure frame2 to expand
frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(0, weight=1)

# Data for Spinboxes
activities = ["Movie Marathon", "Gaming Night", "Shopping Spree", "Sports Practice", "Beach Hangout"]

# Function to display the plan
def display_plan():
    activity = activity_spinbox.get()
    excitement = excitement_spinbox.get()
    time = time_spinbox.get()
    plan_label.config(
        text=f"Amazing Choice :\n\n   'Activity: {activity}\nExcitement: {excitement} stars\nTime Spent: {time} hours'",
        font=("Comic Sans MS", 17)
    )

# Spinbox for Activity
l1 = Label(frame2, text="Choose an Activity:", bg="purple", fg="misty rose",
      font=("Comic Sans MS", 14))
l1.grid(row=0, column=0, padx=10, pady=5, sticky="nw")
activity_spinbox = Spinbox(frame2, values=activities, bg="misty rose", fg="medium violet red", 
                           font=("Comic Sans MS", 12), width=25)
activity_spinbox.grid(row=0, column=1, padx=10, pady=5, sticky="n")

# Spinbox for Excitement Rating
l2 = Label(frame2, text="Rate Your Excitement\n (1.0 - 10.0):", bg="purple", 
       fg="misty rose", font=("Comic Sans MS", 14))
l2.grid(row=1, column=0, padx=10, pady=10, sticky="n")
excitement_spinbox = Spinbox(frame2, from_=1.0, to=10.0, increment=0.5, 
                            bg="misty rose", fg="medium violet red", 
                            font=("Comic Sans MS", 12), width=25)
excitement_spinbox.grid(row=1, column=1, padx=10, pady=10, sticky="n") 

# Spinbox for Time
l3 = Label(frame2, text="Time Spent (hours):", bg="purple", 
       fg="misty rose", font=("Comic Sans MS", 14))
l3.grid(row=2, column=0, rowspan=2, padx=10, pady=5, sticky="n")
time_spinbox = Spinbox(frame2, from_=1, to=5, bg="misty rose", fg="medium violet red", 
                            font=("Comic Sans MS", 12), width=25)
time_spinbox.grid(row=2, column=1, padx=10, pady=5, sticky="n")

# Button to display the plan
b1 = Button(frame2, text="Show My Plan", bg="misty rose", fg="purple", 
                            font=("Lucida Calligraphy", 12), width=25, command=display_plan)
b1.grid(row=3, column=0, columnspan=2, pady=20)

# Label to show the final plan
plan_label = Label(frame2, text="", bg="rosy brown", font=("Viner Hand ITC", 14), 
                   height=10, width=50, fg="medium violet red", justify="left")
plan_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

# Main loop
root.mainloop()
