#Leap Year or Not 

year = int(input("Enter the year you want to check: "))

# Check if the year is divisible by 4
if year % 4 == 0:
    # Check if the year is a century year
    if year % 100 == 0:
        # Check if the century year is divisible by 400
        if year % 400 == 0:
            print("The Year is a LEAP YEAR")
        else:
            print("The Year is NOT a LEAP YEAR")
    else:
        print("The Year is a LEAP YEAR")
else:
    print("The Year is NOT a LEAP YEAR")
