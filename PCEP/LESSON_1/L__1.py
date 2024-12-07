age = 30
height = 5.4
name = "Shalini"
is_student = False

print("Age", age, "Data Type", type(age))
print("name", name, "Data Type", type(name))
print("height", height, "Data Type", type(height))
print("Is a Student", is_student, "Data Type", type(is_student))


#Condition Check
surname = input("enter title")

if surname:
    print(surname)
else:
    print("Invalid what is this")
    
if age:
    print("Valid age")
else :
    print("Invalid")        
    
if is_student:
    print("Valid")
else:
    print("Invalid")        
    
is_teacher = True

if is_teacher:
    print("Valid")
else:
    print("Invalid")            