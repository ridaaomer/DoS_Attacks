# UDP Flood - Mitigation

### Rate Limiting Using iptables
To limit the rate of incoming UDP packets:

#### Commands:
```bash
sudo iptables -A INPUT -p udp -m limit --limit 10/second --limit-burst 20 -j ACCEPT
sudo iptables -A INPUT -p udp -j DROP
