#Create a list
color1 = []         #empty list

colors = ["purple", "navy", "pink", "black", "magenta", "gold", "yellow", "goldenrod"]
print(colors)

#Finding the length of list
print(len(colors))

#Slicing  Syntax- list_name[start:end:step]
print(colors[1:6:2])       #elements from 1st index to index 5 skipping every 2nd element 
print(colors[2::])      #all element from 2nd to last
print(colors[::3])      #every 3rd element
print(colors[-3:-1])    #last third and second element
print(colors[::-1])    #last to first element

#adding element to a list - appending
color1.append("teal")
print(color1[-1])
color1.append("orange")
print(color1)
print(color1[-1])

#adding element to a list - inserting at any existing index 
color1.insert(0, "cyan")
color1.insert(4, "red")     #if index is not present, element is added at the end of the list
print(color1)

#delete any element 
del color1[-1]
print(color1)
'''
del color1              #delete entire list
print(color1)
'''

#Check present or not using "in" keyword
if "navy" in colors :
    print("Present") 
    
if "brown"  not in colors :
    print("Not Present")     

#Traverse through the LIST Iterate and print individual element from the List
print("\nList of all colors We have : ")
for colorr in colors:
    print(colorr)

#Using end parameter
print("\nList of all colors We have : ")
for colorr in colors:
    print(colorr, end = " !*! ")    #changes the default of print function ie, newline