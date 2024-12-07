# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Using ternary operator to find the smaller number
smaller = num1 if num1 < num2 else num2
print("The smaller number is:", smaller)

# Bitwise AND operation
bitwise_and = num1 & num2
print("Bitwise AND of num1 and num2:", bitwise_and)

# Bitwise OR operation
bitwise_or = num1 | num2
print("Bitwise OR of num1 and num2:", bitwise_or)

# Bitwise NOT operation for the first number
bitwise_not = ~num1
print("Bitwise NOT of num1:", bitwise_not)

# 1-bit left shift of the second number
left_shift = num2 << 1
print("1-bit left shift of num2:", left_shift)

# 2-bit right shift of the second number
right_shift = num2 >> 2
print("2-bit right shift of num2:", right_shift)

