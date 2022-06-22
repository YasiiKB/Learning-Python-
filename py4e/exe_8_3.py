#Guardian!
fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    words=line.split()
    #Guardian line:
    #if len(words)<3:
        #continue
    #Guardian in a compound statement:
    if len(words)<3 or words[0] != 'From':
        continue
    print (words[2])
