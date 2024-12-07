income = float(input("Enter your income: "))
health_ins = input("Did you pay for health insurance? (yes/no): ").strip().lower()
char_donation = input("Did you make any charitable donations? (yes/no): ").strip().lower()

# Initialize deduction rate
deduction = 0

# Check if health insurance deduction applies
if health_ins == "yes":
    deduction += 0.05

# Check if charitable donations deduction applies
if char_donation == "yes":
    deduction += 0.10 

# Calculate effective income after applying deductions
final_income = income * (1 - deduction)

# Calculate tax based on effective income
if final_income <= 10000:
    tax = 0
elif 10001 <= final_income <= 50000:
    tax = (final_income - 10000) * 0.10
    tax += 0  
else:
    tax = (50000 - 10000) * 0.10 
    tax += (final_income - 50000) * 0.20 
    
# Display the results
print(f"Original income: ${income:.2f}")
print(f"Effective income after deductions: ${final_income:.2f}")
print(f"Total income tax: ${tax:.2f}")
