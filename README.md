# DoS_Attacks_demo
This repository contains a project demonstrating three types of Denial-of-Service (DoS) attacks: 
- TCP SYN Flood
- UDP Flood
- Ping of Death
The repository includes the attack mechanisms, Python scripts, mitigation strategies, and results observed during the experiments.
## Project Overview
This project demonstrates:
1. Execution of DoS attacks using **hping3** and **custom Python scripts**.
2. Mitigation techniques like **SYN cookies**, **rate-limiting**, and **firewalls**.
3. Results when firewalls are enabled or disabled.

## Repository Structure
- README.md`             | Main project overview, including details of attacks and structure.|
| `attacks/`              | Directory containing attack-specific content.                     |
| `attacks/syn_flood/`    | Folder for TCP SYN Flood attack files.                            |
| ├── `syn_flood_command.md` | Command to execute the TCP SYN Flood attack.                    |
| ├── `syn_flood_script.py`  | Python script for the TCP SYN Flood attack.                     |
| └── `mitigation.md`        | Mitigation steps for the TCP SYN Flood attack.                  |
| `attacks/udp_flood/`    | Folder for UDP Flood attack files.                                |
| ├── `udp_flood_command.md` | Command to execute the UDP Flood attack.                       |
| ├── `udp_flood_script.py`  | Python script for the UDP Flood attack.                        |
| └── `mitigation.md`        | Mitigation steps for the UDP Flood attack.                     |
| `attacks/ping_of_death/`| Folder for Ping of Death attack files.                            |
| ├── `ping_of_death_command.md` | Command to execute the Ping of Death attack.               |
| ├── `ping_of_death_script.py`  | Python script for the Ping of Death attack.                |
| └── `mitigation.md`          | Mitigation steps for the Ping of Death attack.               |
| `results/`              | Directory containing results of the experiments.                 |
- `bibliography.md`: References used in this project.

## Requirements
- Two virtual machines: **Kali Linux** (attacker) and **Ubuntu** (target).
- Tools: `hping3`, Python, Scapy.

## How to Use
1. Navigate to the `attacks/` directory to find specific DoS attack implementations.
2. Follow the instructions in each subdirectory to execute and mitigate attacks.
3. Review the results in the `results/` directory.

## Disclaimer
**This project is for educational purposes only. Do not use the provided scripts or techniques for malicious activities**.
