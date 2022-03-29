from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <= 3:
        msg = str(reTx) + ' ' + msg
        sock.sendto(msg.encode(), ('localhost', port))
        sock.settimeout(2) # 소켓의 timeout 설정. 해당 timeout 내 메시지
        # 수신을 못하면 timeout 예외 발생
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    sock.settimeout(None) 
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
        
    