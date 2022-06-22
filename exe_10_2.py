hours_dictionary=dict()
lst=list()
while True:
    fname= input('Enter File Name:')
    try:
        fhand =open(fname)
    except:
        print("Invalid File Name!")
        continue
    for line in fhand:
        line=line.rstrip()
        words=line.split()
        #Guardian line for empty lines:
        if len(words)<3 or words[0] != 'From':
            continue
        #Get the time & Hours
        for word in words:
            time=words [5]
            pieces=time.split(':')
            hours=pieces[0]
        #Make the dictionary:
        hours_dictionary[hours] = hours_dictionary.get(hours,0) + 1
    #make the list of tuples to order
    lst=list(hours_dictionary.items())
    lst=sorted(lst)
    #to print one per line
    for hours,count in lst[:]:
        print (hours,count)
    break
