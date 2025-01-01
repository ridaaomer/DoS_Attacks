# Ping of Death - Mitigation

### Rate Limiting Using iptables
To limit the rate of ICMP packets:

#### Commands:
```bash
sudo iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/second --limit-burst 5 -j ACCEPT
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
Verify Rules:
sudo iptables -L -v -n
