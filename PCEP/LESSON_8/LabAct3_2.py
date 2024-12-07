my_dict = {'Name': 'Tara', 'RollNo': 130046, 'Mark': 458, 'Age': 16}

#Print dictionary before renaming keys
print("Before Rename Key of a Dictionary =", my_dict)

# Rename keys in the dictionary
my_dict['S_RNo'] = my_dict.pop('RollNo')  # Rename 'RollNo' to 'S_RNo'
my_dict['S_Marks'] = my_dict.pop('Mark')   # Rename 'Mark' to 'S_Marks'

#Dictionary after renaming keys
print("After Rename Key of a Dictionary =", my_dict)
