#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def valid_input(number):
    while True :
        try:
            n = int(input(number))
            return n
        except ValueError:
            print("This is Invalid. Please enter an Integer!!! ")
  
num = valid_input("\nPlease enter a number of your Choice : ")        
print("You have entered a Valid Integer.!!!! \nInteger you entered is :", num)
