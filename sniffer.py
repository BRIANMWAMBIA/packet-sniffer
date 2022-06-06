import socket
import struct
import binascii
#Create a socket, with three parameters
#socket.AF_INET-packet interface foer windows, socket.PF_PACKET-->LINUX
#The second parameters tells us that it a raw socket
#The third parameter tells us about the protocol weare intersted in  -0x800 used for IP

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket. htons(0x0800)
# We need to receive the packet using recvfrom()
t = True
while t:
   packet = s.recvfrom(2048)
#Rip off the  ethernet header
ethernet_header = packet[0][0:14]
#parse and unpack the header with the struct method
eth_header = struct.unpack("!6s6s2s", ethernet_header)
print "Destination MAC:" + binascii.hexlify(eth_header[0]) + " Source MAC:" + binascii.hexlify(eth_header[1]) + " Type:" + binascii.hexlify(eth_header[2])
ipheader = pkt[0][14:34]
ip_header = struct.unpack("!12s4s4s", ipheader)
print "Source IP:" + socket.inet_ntoa(ip_header[1]) + " Destination IP:" + socket.inet_ntoa(ip_header[2])
