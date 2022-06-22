while True:
    count = 0
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname) #don't forget to fhand it!
    except:
        print('File name is not correct or the file is missing!')
        continue
    for line in fhand:
        if line.startswith ('X-DSPAM-Confidence:'):
        #    str = 'X-DSPAM-Confidence:0.8475'
            colpos = line.find(':')
            num = line[colpos+1 : ]
            num = float(num)
            count+=1
            print (count,')' , num)
    print ('Average spam confidence:' , num/count)
    break #otherwise it will go back to input forever!!!
