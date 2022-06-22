import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://virastudy.com/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
dedata = data.decode()
#find header
headerpos = dedata.find ('\r\n\r\n')
#Skip 4 lines (r\n\r\n) of header and print the rest
print(dedata[headerpos+4:], end='')

#print the (rest) page (as always)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()
