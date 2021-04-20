from scapy.all import *

f = open('log.pcap', 'ab')

def print_pkt(pkt):
    wrpcap(f, pkt, append=True)

sniff(filter="", prn=print_pkt)