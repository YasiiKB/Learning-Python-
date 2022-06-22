
email_dictionary=dict()
lst = list()
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
        #make a dictionary
        for word in words:
            email=words [1]
        email_dictionary[email] = email_dictionary.get(email,0) + 1
    #make a list of tuples (count,email) and sort them from high to low
    for email, count in email_dictionary.items():
        new=(count,email)
        lst.append(new)
    lst=sorted(lst,reverse=True)
    #print the first one but flipped agian
    for count,email in lst[:1]:
        print (email,count)
    break
