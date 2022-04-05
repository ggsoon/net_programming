import numpy as np
from socket import *

s = socket()
s.bind(('', 802))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    
    if msg == "Request":
       Temp = np.random.randint(41)
       Humid = np.random.randint(101)
       lilium = np.random.randint(70, 151)
       c.send(str(Temp).encode())
       c.send(str(Humid).encode())
       c.send(str(lilium).encode())
    if msg == "quit":
       c.close()
