
#***Extracting Data from XML****

#In this assignment you will write a Python program somewhat similar
#to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL,
#read the XML data from that URL using urllib and then parse and extract
#the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we
#give you the sum for your testing and the other is the actual data you need to
#process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_97410.xml (Sum ends with 59)
#You do not need to save these files to your folder since your program will read
#the data directly from the URL.
#Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis."""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sum = 0
total = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data) #Take the string, puts it through ET and  give us a XML Tree.
    counts = tree.findall('.//count') #Retrieve 'count' which is the sub-tree of comment, so we need //.
    for count in counts:
        sum += int(count.text)
        total +=1

    print ('Sum of the Numbers in the File:',sum)
    print ('Comment Counts:',total)
    break
