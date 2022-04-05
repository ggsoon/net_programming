import numpy as np
from socket import *

s2 = socket()
s2.bind(('', 801))
s2.listen(10)

while True:
    c, addr = s2.accept()
    data = c.recv(1024)
    msg = data.decode()
    
    if msg == "Request":
       Heartbeat = np.random.randint(40, 141)
       Steps = np.random.randint(2000, 6001)
       Cal = np.random.randint(1000, 4001)
       Heartbeat = Heartbeat.to_bytes(4, 'big')
       Steps = Steps.to_bytes(4, 'big')
       Cal = Cal.to_bytes(4, 'big')
       c.send(Heartbeat)
       c.send(Steps)
       c.send(Cal)
    if msg == "quit":
       c.close()
