import re

count = 0
fhand = open('mbox-short.txt')
wd = input ('Enter a regular expression: ') 
for line in fhand:
    line=line.rstrip()
    line=line.lower()
    # if the word (wd) is found, count it.
    if re.findall(wd, line) != []: # Just type the wd (no . or * needed) #don't forget the :.
        count+=1
print ('mbox.txt had', count, 'lines that matched', wd)
