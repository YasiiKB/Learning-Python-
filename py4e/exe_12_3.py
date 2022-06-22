import urllib.request, urllib.parse, urllib.error

count = 0
#get the url and open it like a file.
url = input('Enter - ')
fhand = urllib.request.urlopen(url)
#read line by line
for line in fhand:
    #new lines need to be deleted because otherwise they'll count as characters.
    line = line.decode().rstrip('\n')
    ncount = count + len(line)
    if ncount <= 3000:
        print(line)
    elif count < 3000: #if there's been less than 3000, print the rest.
        rest = 3000 - ncount
        #print from 0 to 2999 (3000 characters)
        print (line[:rest-1])
    count = ncount
print ('Count:', count)
