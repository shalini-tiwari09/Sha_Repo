'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

Write a Python program that prompts the user to input two numbers and raises a ValueError exception if the inputs are not numerical.

Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.
'''

def valid_input(number):
    while True :
        try:
            n = int(input(number))
            return n
        except ValueError:
            print("This is Invalid. Please enter an Integer!!! ")
  
num = valid_input("\nPlease enter a number of your Choice : ")        
print("You have entered a Valid Integer.!!!! \nInteger you entered is :", num)