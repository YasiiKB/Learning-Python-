dictionary_days = dict()
fhand =open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    words=line.split()
    #Guardian in a compound statement:
    if len(words)<3 or words[0] != 'From':
        continue
    for word in words:
        day = words[2]
    #print(day)
    dictionary_days[day] = dictionary_days.get(day,0) + 1 #needs to be out of the for loop
print('Days',dictionary_days)
    #else:  ---- THIS DOES THE .get JOB ---------
    #    if words[2] not in dictionary_days:
    #        dictionary_days[words[2]] =1  #First Count
    #    else:
    #        dictionary_days[words[2]]+=1    #Additional Counts
