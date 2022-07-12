''' 
Install pip install qrcode 
If you get "ImportError: No module named 'Image'" error, you need to:  pip install pillow
'''

import qrcode

data = str(input('What\'s your message?'))
color = str(input('What color?')).lower()
background_color = str(input('What background color?')).lower()

qr = qrcode.QRCode(version= 1, box_size=10, border=5)
qr.add_data(data)
qr.make (fit=True)
img = qr.make_image(fill_color = color, back_color= background_color)

loc = str('E:\Computer stuff - BUp\Python Projects\pyprojects\QRcode').replace('\\', '/') 
location = loc + str('/myqrcode.png')
img.save(location)