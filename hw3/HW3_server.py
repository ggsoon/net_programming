from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        result = client.recv(1024).decode()
        result = eval(result)
        print(result)
        result = result.to_bytes(4, 'big')
        client.send(result)
