#Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.
Fruit= 'Banana'
index = len(Fruit)
while index >= 1:
    letter = Fruit [index-1]
    print (letter)
    index=index-1
