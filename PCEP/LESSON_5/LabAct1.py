even_count = 0
odd_count = 0

print("Enter a sequence of numbers (OR Enter 0 to stop):")


while True:
    num = int(input("Enter No. of your Choice and press Enter"))
    if num == 0:
        break
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
