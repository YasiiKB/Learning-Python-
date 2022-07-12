''' 
Install pip install pyzbar 
'''
from unittest import result
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open ('E:/Computer stuff - BUp/Python Projects/pyprojects/QRcode/myqrcode.png')


# decode function gives a *list* with only 1 item:

# [Decoded(data=b'Hello from Yasi', type='QRCODE', rect=Rect(left=52, top=52, width=247, height=247), 
# polygon=[Point(x=52, y=52), Point(x=52, y=297), Point(x=299, y=299), Point(x=297, y=52)], quality=1, orientation='UP')]

# print(type(result)) --> list 
# print(len(result)) ---> 1

# turing a list into a string so we can split it at '. 
result = str(decode(img)).split("'")[1]
print(result)