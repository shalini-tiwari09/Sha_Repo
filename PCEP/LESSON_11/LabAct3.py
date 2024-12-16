#Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
def test_list_operation(nums):
    try:
        # Attempt to access the 'length' attribute of the 'nums' list and assign it to 'r'.
        r = len(nums)  # Trying to access the length attribute
        #r = nums.length #gives Attribute Error.
        # Print the length of the list 'nums'.
        print("Length of the list:", r)
    except AttributeError:
        # Handle the exception if an AttributeError occurs when attempting to access the 'length' attribute.
        print("Error: The list does not have a 'length' attribute.")

# Create a list 'nums' containing integer values.
nums = [1, 2, 3, 4, 5]
# Call the 'test_list_operation' function with the 'nums' list as a parameter to check for the 'length' attribute.
test_list_operation(nums)