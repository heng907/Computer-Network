from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# get path of pcap file
# INPUTPATH = sys.argv[4] 
size1=0
size2=0
size3=0
for k in range (2):
    INPUTPATH= sys.argv[k+1]
    # print(INPUTPATH)


# read pcap
    packets = rdpcap(INPUTPATH) 


    # print ("***Count number of TCP packets***")
    count = 0
    for packet in packets[TCP]:
        count += 1
    # print ("number of TCP packets: ", count)

    #tcp
    if INPUTPATH=="../out/TCP_h3.pcap":
        for i in range(count):
            if packets[TCP][i][2].dport==7778:
                size1=len(packets[TCP][i])+size1
            elif packets[TCP][i][2].dport==7779:
                size2=len(packets[TCP][i])+size2 
    if INPUTPATH=="../out/TCP_h4.pcap":
        for i in range(count):
            if packets[TCP][i][2].dport==7780:
                size3=len(packets[TCP][i])+size3
        
tp1=size1*8/(5*1000000)
tp2=size2*8/(5*1000000)
tp3=size3*8/(5*1000000)
print("---TCP---")    
print(f"Flow1(h1->h3):{tp1} Mbps")
print(f"Flow2(h1->h3):{tp2} Mbps")
print(f"Flow3(h2->h4):{tp3} Mbps")


#udp
size1=0
size2=0
size3=0
for k in range (2):
    INPUTPATH= sys.argv[k+3]
    # print(INPUTPATH)

# read pcap
    packets = rdpcap(INPUTPATH) 


    # print ("***Count number of UDP packets***")
    count = 0
    for packet in packets[UDP]:
        count += 1
    #print ("number of UDP packets: ", count)

    #udp
    if INPUTPATH=="../out/UDP_h3.pcap":
        for i in range(count):
            if packets[UDP][i][2].dport==7778:
                size1=len(packets[UDP][i])+size1
            elif packets[UDP][i][2].dport==7779:
                size2=len(packets[UDP][i])+size2 
    if INPUTPATH=="../out/UDP_h4.pcap":
        for i in range(count):
            if packets[UDP][i][2].dport==7780:
                size3=len(packets[UDP][i])+size3
        
tp1=size1*8/(5*1000000)
tp2=size2*8/(5*1000000)
tp3=size3*8/(5*1000000)
print("\n---UDP---")    
print(f"Flow4(h1->h3):{tp1} Mbps")
print(f"Flow5(h1->h3):{tp2} Mbps")
print(f"Flow6(h2->h4):{tp3} Mbps")

