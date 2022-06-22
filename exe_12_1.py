import socket

url = input('Enter the URL: ')
try: #if the url is valid, the whole code will run.
    word = url.split('/')
    host = word[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host,80))
    mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(),end='')
    mysock.close()
except: #if the url is valid, nothing will run.
    print ('Invalid URL')
