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
        packed += struct.pack('!H', self.saddr)
        packed += struct.pack('!H', self.daddr)
        packed += struct.pack('!H', self.tot_len)
        packed += struct.pack('!H', self.check)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:12])
    return unpacked
def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]
def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]
def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]
def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print('Sourece Port:{} Destination port:{} Length:{} Checksum:{}'\
.format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))
