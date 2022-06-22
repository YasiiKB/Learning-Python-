allwords= dict()
#words = list()
fhand= open('words.txt')
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        allwords[word] = allwords.get(word,1)
print(allwords)
if 'kinds' in allwords:
    print('Found it!')
else:
    print('NOT THERE!')
