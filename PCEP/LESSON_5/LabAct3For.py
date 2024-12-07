email = input("Enter your email address: ")

for char in email:
    if char == "@":
        break
    print(char, end="")  # Print characters without adding a newline
