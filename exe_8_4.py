#Write a program to open the file romeo.txt and read it
#line by line. For each line, split the line into a list
#of words using the split function. For each word, check
#to see if the word is already in the list of unique words.
#If the word is not in the list of unique words, add it to
#the list. When the program completes, sort and print the
#list of unique words in alphabetical order.
fhand = open('romeo.txt')
allwords =list() #A list to put all the words in to.
resultlist = list()
for line in fhand:
    line = line.rstrip()
    words= line.split()
    #uwords.append(word) --> would just add 3 lists (3lines) as separate lists to one big list,separately
    #uniquewords+=words --> makes uniquewords a string, rather than a list!
    allwords.extend (words) #add the words, one by one!
    for words in allwords: #Go through all the words
        if words not in resultlist: #If the word is not there, add it.
            resultlist.append (words)
resultlist.sort()
print(resultlist)
