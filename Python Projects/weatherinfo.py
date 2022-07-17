'''
Sign up in https://home.openweathermap.org/ and enter your API key in the API_Key = 'here'. 
Instead of urllib library, you can use requests (import requests) after pip install requests is done. 
'''

import urllib.request, urllib.parse
import json
from pprint import pprint


API_key = ''

city = input('Enter a City: ')

try: 
    # &q means query
    base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_key+"&q="+city

    # getting the info form the url and decoding it (because .json() needs a string)
    weather_url = urllib.request.urlopen(base_url)
    for line in weather_url:
        line.decode()   # a list of strings

    # turing the info we got and decoded to a json file
    weather_data = json.loads(line)

    pprint(weather_data)

except:
    print('City Not Found!')