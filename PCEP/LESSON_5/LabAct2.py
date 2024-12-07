word = input("Enter Word of Your Choice").lower()

index = 0 

while index < len(word):
    letter = word[index]
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
        index += 1
        continue
    print(letter, end="")
    index += 1