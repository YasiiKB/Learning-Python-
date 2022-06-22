#Write a program to read through the mail box data and when you find
#line that starts with “From”, you will split the line into words using the
#split function. We are interested in who sent the message, which is the
#second word on the From line.
    #From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#You will parse the From line and print out the second word for each
#From line, then you will also count the number of From (not From:)
#lines and print out a count at the end.
count =0
#name=list()
while True:
    fname = input('Enter file name:')
    try:
        fhand=open(fname)
    except:
        print ('Invalid input!')
        continue
    for line in fhand:
        line=line.rstrip()
        if line.startswith ('From'):
            words=line.split()
            # name.append(words[1]) --> Makes name a list! --> more space in the memory!
            name=words[1]
            print(name)
            count+=1
    print('There were',count,'lines in the file with From as the first word!')
    break
