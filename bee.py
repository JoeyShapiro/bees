from scapy.all import *

f = open('log.pcap', 'ab')
stickyIPs = [] # list is easy

def print_pkt(pkt):
    try:
        source = pkt['IP'].src
        # check if questionable
        if((pkt['IP'].dst == '192.168.192.131') and (source not in stickyIPs)):
            #add to list (make sticky)
            stickyIPs.append(source)
            print(source + " is now sticky")
        if souce in stickyIPs:
            #monitor any traffic sticky IPs do on network
            wrpcap(f, pkt, append=True)
            print("doing something")
    except:
        pass

print("scanny network")
sniff(filter="", prn=print_pkt)
