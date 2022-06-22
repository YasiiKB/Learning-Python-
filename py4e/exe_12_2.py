import socket

count = 0
while True:
    url = input('Enter URL: ')
    try:
        words = url.split('/')
        host = words[2]
        #Socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())
        #Reading the data
        while True:
            data = mysock.recv(512)
            count += len(data)
            if (len(data) < 1) or count > 3000:
                break
            print(data.decode(), end='')
        mysock.close()
        print ('Count:', count)
        break
    except:
        print('Invalid URL')
        break
