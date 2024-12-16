#Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def valid_input(number1, number2):
        try:
            result = int(number1 / number2)
            print(f"\nYour inputs are {number1} and {number2}.\n The Result of Division is : {result}")

        except ZeroDivisionError:
            print("Division by Zero Error!!! \n")
        
  
num1 = int(input("\nPlease enter a number of your Choice : "))
num2 = int(input("Please enter a number of your Choice : "))        

valid_input(num1, num2)
