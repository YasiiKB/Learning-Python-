import string  #need this library to use the functions later

letters_dictionary =dict()
lst = list()
counts= 0
fname=input("Enter File Name:")
try:
    fhand=open(fname)
except:
    print('Invalid File Name!')
    exit()
for line in fhand:
    line=line.rstrip()
    #deleting the punctuation and the numbers & truing them all to lowercase letters
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.translate(str.maketrans('','',string.digits)) # = line=line.translate(str.maketrans('','','1234567890'))
    line=line.lower()
    words=line.split()
    for word in words: #Two for loops to go through words, then letters
        for letter in word:
            counts+=1 #count all the letters
            if letter not in letters_dictionary:
                letters_dictionary[letter]=1
            else:
                letters_dictionary[letter]+=1
    #print(letters_dictionary)
    for letter, val in letters_dictionary.items():
        pval= round(val/counts*100) # calculating the %
        new=(pval,letter) #making the tuples
        lst.append(new)  #making the list of the tuples
    lst=sorted(lst,reverse=True) #sort from high frequency to low
    for pval,letter in lst[:]:  #print one tuple on each line, the letter first.
        print(letter,pval,'%')
    break
