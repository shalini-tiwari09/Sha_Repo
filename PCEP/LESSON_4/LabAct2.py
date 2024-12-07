distance = float(input("Enter the distance of your travel in miles: "))
age = int(input("Enter your age: "))

# Determine the ticket price based on distance and age
if distance < 1000:
    if age < 12:
        price = 200
    elif 12 <= age <= 64:
        price = 300
    else:  # age >= 65
        price = 250
else:  
    if age < 12:
        price = 400
    elif 12 <= age <= 64:
        price = 500
    else:  # age >= 65
        price = 450

# calculated price
print(f"The price of your airline ticket is: ${price}")
