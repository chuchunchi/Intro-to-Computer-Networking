from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# get path of pcap file
I1 = "../out/TCP_h4.pcap"
I2 = "../out/TCP_h3.pcap"
U1 = "../out/UDP_h4.pcap"
U2 = "../out/UDP_h3.pcap"

# read pcap
# packets = rdpcap(INPUTPATH)
packets1 = rdpcap(I1)
packets2 = rdpcap(I2)
packetsUDP1= rdpcap(U1)
packetsUDP2 = rdpcap(U2)

#I1
lens1 =0
for packet in packets1[TCP]:
    lens1 += len(packet)
rate=0
rate = lens1*8 / 1000000 / 5

print("--- TCP ---")
print("Flow1(h1->h4):" + str(rate) + "Mbps")

#I2
lens2 =0
for packet in packets2[TCP]:
    lens2 += len(packet)
rate=0
rate = lens2*8 / 1000000 / 5

print("Flow1(h2->h3):" + str(rate) + "Mbps")

#U1
lens_u1 =0
for packet in packetsUDP1[UDP]:
    lens_u1 += len(packet)
rate=0
rate = lens_u1*8 / 1000000 / 5

print("--- UDP ---")
print("Flow1(h1->h4):" + str(rate) + "Mbps")

#U2
lens_u2 =0
for packet in packetsUDP2[UDP]:
    lens_u2 += len(packet)
rate=0
rate = lens_u2*8 / 1000000 / 5

print("Flow1(h2->h3):" + str(rate) + "Mbps")







