from tkinter import *

# Main Window
win = Tk()
win.geometry("700x600")
win.config(background="Black")
win.title("Feedback Form")

# Heading 1
heading1 = Label(win, text="CONTACT US", bg="Black", fg="IndianRed",
                 font=("Lucida Handwriting", 28, "italic", "bold"), relief="solid", padx=10, pady=5)
heading1.pack(pady=20)

# Subheading
heading2 = Label(win, text="We will get back to you asap!!!", bg="Black", fg="DarkGoldenrod",
                 font=("Pristina", 22, "italic", "bold"))
heading2.pack(pady=10)

# First Name Label
fname_label = Label(win, text="First Name", bg="Black", fg="IndianRed",
                    font=("Arial", 14, "bold"), anchor="w")
fname_label.pack(padx=10, pady=(10, 0), anchor="w")

# First Name Entry
fname_entry = Entry(win, bg="LightYellow", fg="Black",
                    font=("Arial", 15), width=30)
fname_entry.pack(padx=10, pady=5, anchor="w")

# Last Name Label
lname_label = Label(win, text="Last Name", bg="Black", fg="IndianRed",
                    font=("Arial", 14, "bold"), anchor="w")
lname_label.pack(padx=10, pady=(10, 0), anchor="w")

# Last Name Entry
lname_entry = Entry(win, bg="MistyRose", fg="Black",
                    font=("Arial", 15), width=30)
lname_entry.pack(padx=10, pady=5, anchor="w")

# Email Label
email_label = Label(win, text="Email", bg="Black", fg="IndianRed",
                    font=("Arial", 14, "bold"), anchor="w")
email_label.pack(padx=10, pady=(10, 0), anchor="w")

# Email Entry
email_entry = Entry(win, bg="Bisque", fg="Black",
                    font=("Arial", 15), width=60)
email_entry.pack(padx=10, pady=5, anchor="w")

# Contact Number Label
phone_label = Label(win, text="Contact No.", bg="Black", fg="IndianRed",
                    font=("Arial", 14, "bold"), anchor="w")
phone_label.pack(padx=10, pady=(10, 0), anchor="w")

# Contact Number Entry
phone_entry = Entry(win, bg="LightYellow", fg="Black",
                    font=("Arial", 15), width=30)
phone_entry.pack(padx=10, pady=5, anchor="w")

# Send Button
send_button = Button(win, text="SEND", bg="Goldenrod", fg="Black",
                     font=("Pristina", 20, "bold"), relief="raised")
send_button.pack(pady=20)

# Footer Text (Call Label)
call_label = Label(win, text="You may also call us at 999-999-9999", bg="Black", fg="DarkGoldenrod",
                   font=("Pristina", 18, "italic"))
call_label.pack(pady=10)

# Footer Text (Social Handle)
footer_label = Label(win, text="@KeepSmiling", bg="Black", fg="IndianRed",
                     font=("Comic Sans MS", 14, "italic"))
footer_label.pack(pady=5)

# Run the application
win.mainloop()
