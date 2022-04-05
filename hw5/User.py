import time
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s2 = socket(AF_INET, SOCK_STREAM) 
s.connect(('localhost', 802))
s2.connect(('localhost', 801))

while True:
    msg = input('Number?:')
    if msg == '1':
        s.send(b'Request')
        Temp = s.recv(1024).decode()
        Humid = s.recv(1024).decode()
        lilium = s.recv(1024).decode()
        f = open("data.txt", "w")
        f.writelines(time.asctime() + ": Device1: Temp=" + str(Temp) + ", Humid=" + str(Humid) + ", lilum=" + str(lilium))
        f.close()
    if msg == '2':
        s2.send(b'Request')
        Heartbeat = s.recv(1024)
        Heartbeat = int.from_bytes(Heartbeat, 'big')
        Steps = s.recv(1024)
        Steps = int.from_bytes(Steps, 'big')
        Cal = s.recv(1024)
        Cal = int.from_bytes(Cal, 'big')
        f = open("data.txt", "w")
        f.writelines(time.asctime() + ": Device2: Temp=" + str(Heartbeat) + ", Humid=" + str(Steps) + ", lilum=" + str(Cal))
        f.close()
    if msg == 'quit':
        f.close()
        s.send('quit'.encode())
        s2.send('quit'.encode())
        break

s.close()