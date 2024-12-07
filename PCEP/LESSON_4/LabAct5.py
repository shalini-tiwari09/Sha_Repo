# Accept income as input from the user
income = float(input("Enter your income in thalers: "))

# Define the tax calculation based on the given rules
if income <= 85528:
    tax = (0.18 * income) - 556.02
else:
    tax = 14839.02 + (0.32 * (income - 85528))

# Ensure tax is not negative
if tax < 0:
    tax = 0

# Round the tax to the nearest whole number (full thalers)
tax_rounded = round(tax)

# Print the result
print("The calculated tax is:", tax_rounded, "thalers")
