import re

numlist = list ()
fhand = open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    stuff = re.findall('^New Revision: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
avg= int(sum(numlist)/len(numlist))
print (avg)
