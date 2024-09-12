Python Backdoor and Listener
This repository contains two Python scripts designed for creating a remote shell backdoor and a corresponding listener. These scripts demonstrate how to establish a reverse shell connection and interact with a remote system.

Important: These tools are intended for educational purposes only. Ensure you have explicit permission to use them in your testing environments. Unauthorized use is illegal and unethical.

Overview
1. Backdoor (reverse_backdoor.py)
The backdoor.py script sets up a reverse shell on the target machine, allowing it to connect back to a listener and execute commands remotely. It supports basic file operations and command execution.

Dependencies: socket, subprocess, json, os, base64
Functionality:
Execute Commands: Executes system commands on the target machine.
Change Directory: Changes the working directory on the target machine.
Download Files: Reads and base64-encodes files from the target machine.
Upload Files: Decodes and writes files to the target machine.

2. Listener (listener.py)
The listener.py script runs on the attacker's machine and listens for incoming connections from the backdoor script. It allows for command execution and file operations on the connected client.

Dependencies: socket, json, base64

Functionality:

Receive Commands: Receives and executes commands sent from the attacker.
Upload Files: Accepts files uploaded from the client.
Download Files: Sends files from the attacker's machine to the client.


Important Notes
Legal and Ethical Use: These scripts are for educational purposes only. Use them in environments where you have explicit permission. Unauthorized use can lead to legal consequences.
Security Considerations: Be cautious when running these scripts, as they can expose your systems to security risks. Use them responsibly and in controlled environments.
