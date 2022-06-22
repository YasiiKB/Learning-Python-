
email_dictionary=dict()
while True:
    fname= input('Enter File Name:')
    try:
        fhand =open(fname)
    except:
        print("Invalid File Name!")
        continue #you need a while true loop for this to work
    for line in fhand:
        line=line.rstrip()
        words=line.split()
        #Guardian line for empty lines:
        if len(words)<3 or words[0] != 'From':
            continue
        for word in words:
            email=words [1]
        email_dictionary[email] = email_dictionary.get(email,0) + 1 #out of the loop!
    #print('Emails', email_dictionary)
    # --- Who has sent the most emails? ------
    bigcount= None
    bigsender= None
    for email,email_dictionary in email_dictionary.items(): #email->key , email-dic->value
        if bigcount is None or email_dictionary> bigcount:
            bigsender = email
            bigcount = email_dictionary
    print(bigsender,bigcount)
    break
