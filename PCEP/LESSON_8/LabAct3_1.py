my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}

# Sort in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))


print("Sorted dictionary in ascending order by value:")
print(sorted_dict_asc)

print("\nSorted dictionary in descending order by value:")
print(sorted_dict_desc)
