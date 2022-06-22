'''
    Use a GeoLocation lookup API modelled after the Google API to look up some
    universities and parse the returned data. The program will prompt for a location,
    contact a web service and retrieve JSON for the web service and parse that data,
    and retrieve the first place_id from the JSON. A place ID is a textual identifier
    that uniquely identifies a place as within Google Maps.

    Use this API endpoint that has a static subset of the Google Data:
    http://py4e-data.dr-chuck.net/geojson?
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break #Exits the program if you press Enter.

#Make a dictionary, put the input address in it and add it to the url.
    parms = dict()
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms)
#open the url
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode() # a list of all the universities.
    print('Retrieved', len(data), 'characters')

    try:   #"json.loads" takes a string, bytes, or byte array instance which contains the JSON document as a parameter (s) and returns a Python object.
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Location Not Found! ====')
        print(data) #Prints a list of all the universities.
        continue
    #convert a Python object into a json string and pretty print the whole thing!
    print(json.dumps(js, indent=4))

    placeid = js['results'][0]['place_id']
    print('Place ID:', placeid)
