import mimetypes
from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    filename = req[0].split(" ")
    filename = filename[1]
    filename = filename[1:]
    
    if filename == "index.html":
        f = open(filename, 'r', encoding='utf-8')
        mimetypes = 'text/html'
    elif filename == "iot.png":
        f = open(filename, 'rb')
        mimetypes = 'image/png'
    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        mimetypes = 'image/x-icon'
    else:
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())
        c.close()
        

    mimeType = mimetypes
    c.send('HTTP/1.1 200 OK\r\n'.encode())
    c.send('Content-Type: '.encode() + mimeType.encode() + '\r\n'.encode())
    c.send('\r\n'.encode())
    
    data = f.read()
    if filename == "index.html":
        c.send(data.encode('euc-kr'))
    else:
        c.send(data)
    
    c.close()
