# TCP SYN Flood - Mitigation

### 1. Enable SYN Cookies
SYN Cookies block half-open TCP connections.

**Command:**
sudo sysctl -w net.ipv4.tcp_syncookies=1
