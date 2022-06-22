
domain_dictionary=dict()
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
        #Get the domains:
        for word in words:
            email=words [1]
        pieces=email.split('@')
        domains=pieces[1]
        #Make the dictionary:
        domain_dictionary[domains] = domain_dictionary.get(domains,0) + 1 #out of the loop!
    print('Domains', domain_dictionary)
    break
