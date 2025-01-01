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

## Repo Structure
main: The main branch contains the project overview and documentation (README, etc.).

syn_flood: Contains the files for the TCP SYN Flood attack.

udp_flood: Contains the files for the UDP Flood attack.

ping_of_death: Contains the files for the Ping of Death attack.

## Requirements
- Two virtual machines: **Kali Linux** (attacker) and **Ubuntu** (target).
- Tools: `hping3`, Python, Scapy.

## How to Use
1. Navigate to the `attacks/` directory to find specific DoS attack implementations.
2. Follow the instructions in each subdirectory to execute and mitigate attacks.
3. Review the results in the `results/` directory.

## Disclaimer
**This project is for educational purposes only. Do not use the provided scripts or techniques for malicious activities**.
