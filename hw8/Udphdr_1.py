import socket
import struct
import binascii

class Udphdr:
    def __init__(self, saddr, daddr, tot_len, check):
        self.saddr = saddr
        self.daddr = daddr
        self.tot_len = tot_len
        self.check = check
                  
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.saddr, self.daddr)
        packed += struct.pack('!HH', self.tot_len, self.check)
        return packed

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))
