import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
dic = {}

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    msg = msg.decode()
    
    if msg[:4] == 'send':
        mboxId = msg[5]
        dic[mboxId] = msg[7:]
        sock.sendto("OK".encode(), addr)
        
    elif msg[:7]  == 'receive':
        try:
            mboxId = msg[8]
            print(dic[mboxId])
            rep = dic[mboxId]
            sock.sendto(rep.encode(), addr)
            dic.pop(mboxId)
        except:
            sock.sendto("No messages".encode(), addr)
        
    elif msg == 'quit':
        break
    
    
  
    
    