# TCP SYN Flood - Mitigation
### 1. Add rate limting using iptables
sudo iptables -A INPUT -p tcp --syn -m limit --limit 50/second --limit-burst 100 -j ACCEPT
sudo iptables -A INPUT -p tcp --syn -j DROP

### 2. Enable SYN Cookies
SYN cookies prevent resource allocation for half-open connections.
#### Command:
```bash
sudo sysctl -w net.ipv4.tcp_syncookies=1
Make it Permanent:
Open the file:
bash
Copy code
sudo nano /etc/sysctl.conf
Add:
bash
Copy code
net.ipv4.tcp_syncookies=1
Apply changes:
bash
Copy code
sudo sysctl -p

**Command:**
sudo sysctl -w net.ipv4.tcp_syncookies=1




