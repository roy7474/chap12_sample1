'''simple Python program that makes a connection to a web 
server and follows the rules of the HTTP protocol to requests
 a document and display what the server sends back.'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)< 1 ):
        break
    print(data.decode())

mysock.close()
