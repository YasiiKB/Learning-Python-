'''
The program will prompt for a URL, read the JSON data from that URL using urllib,
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_113035.json (Sum ends with 41)
'''
import urllib.request
import json

url= input('Enter URL:')
connection = urllib.request.urlopen(url)
data = connection.read().decode()
#deserialize 'data' (dictionary in json) to a Python object
js = json.loads(data)
print ('Retrieving url', url)
print ('Retrieving', len(data), 'characters')

counts = 0
sum = 0
                    #Don't forget the '' for the keys.
for comment in js['comments']:
    counts += comment ['count']
    sum+=1
print('Comment Counts:', counts)
print ('Sum of the number in file:', sum )
