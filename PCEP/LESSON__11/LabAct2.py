#Write a Python program that prompts the user to input two numbers and raises a ValueError exception if the inputs are not numerical.

def valid_input(number):
    while True :
        try:
            n = float(input(number))
            return n
        except ValueError:
            print("This is Invalid. Please enter Numerical Value!!! ")
  
num1 = valid_input("\nPlease enter a number of your Choice : ")
num2 = valid_input("\nPlease enter a number of your Choice : ")        
print(f"You have entered a Valid Input.!!!! \nYour inputs are {num1} and {num2}.")
