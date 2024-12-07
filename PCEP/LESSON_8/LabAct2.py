# Define the dictionaries
A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Science': 97, 'Social': 89}
B = {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56}


for key, value in A.items():
    if key in B and B[key] == value:
        print(f"{key} : {value} is present in both A and B")
