d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}

merged_dict = d1.copy()  #copy of d1
merged_dict.update(d2)   # Update with the contents of d2

print("Merged Dictionary:", merged_dict)
