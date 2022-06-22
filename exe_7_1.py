#Write a program to read through a file and print the contents
#of the file (line by line) all in upper case.
while True:
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname) #don't forget to fhand it!
    except:
        print('File name is not correct or the file is missing!')
        continue
    if fhand == 'na na boo boo': #doesn't work!
        print ("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        for line in fhand:
            line = line.rstrip()
            print (line.upper()) #use upper() right!
        break
