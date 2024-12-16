#Create a Tuple
color1 = ()         #empty Tuple

colors = ("purple", "navy", "pink", "black", "magenta", "gold", "yellow", "goldenrod")
print(colors)

#Finding the length of Tuple
print(len(colors))

#Slicing  Syntax- tuple_name[start:end:step]
print(colors[1:6:2])       #elements from 1st index to index 5 skipping every 2nd element 
print(colors[2::])      #all element from 2nd to last
print(colors[::3])      #every 3rd element
print(colors[-3:-1])    #last third and second element
print(colors[::-1])    #last to first element

#adding element to a list - appending
color1 += ("teal",)
print(color1[-1])
color1 = color1 + ("orange",)
print(color1)
print(color1[-1])


#delete  entire tuple 
'''
del color1          
print(color1)
'''

#Check present or not using "in" keyword
if "navy" in colors :
    print("Present") 
    
if "brown"  not in colors :
    print("Not Present")     

#Traverse through the TUPLE
print("\nAll colors We have : ")
for colorr in colors:
    print(colorr)

#Using end parameter
print("\nAll colors We have : ")
for colorr in colors:
    print(colorr, end = " !*! ")    #changes the default of print function ie, newline