'''
pip install bs4 
* If you want to use "import requests" instead of urllib, you need to ```pip install requests``` first.
Basic Idea: https://www.youtube.com/watch?v=SqvVm3QiQVk&ab_channel=freeCodeCamp.org
'''


import urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs

### Step 1: getting the html page
github_user = input('Input Github Username: ')
url = 'https://github.com/'+ github_user
# print(github_user_url)

try: 
    html = urllib.request.urlopen(url).read()
    soup = bs (html, 'html.parser')

    ### Step 2: getting the profile picture url 

    # the profile image element on the github page has this code 
    # (which you can see by right-clicking on the profile picture and choosing Inspect):
    # <img style="height:auto;" alt="Avatar" width="260" height="260" class="avatar avatar-user width-full border color-bg-default" src="https://avatars.githubusercontent.com/....">
    # since we don't need just any image, we have to specify: {'alt' : 'Avatar'} 
    # and we need the url of that image, which is in src="https://avatars.githubusercontent.com/....."

    profile_image = soup.find('img', {'alt' : 'Avatar'})['src']

    print (profile_image)

except:
    print('User Not Found!')