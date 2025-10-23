# TCP/IP Security Attack Scripts

This repository contains a collection of Python scripts demonstrating various TCP/IP network attacks, designed for attack against TELNET services, for educational and research purposes. 


## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)
- Netcat (nc) for some scripts

## Scripts Overview

### 1. SYN Flood Attack (`syn_flood.py`)
A script that demonstrates TCP SYN flooding attack by sending multiple SYN packets with randomized source information.

**Usage:**
```bash
python syn_flood.py
```
- When prompted, enter target IP (default: 10.0.2.6)
- Enter target port (default: 23 for TELNET)

**Features:**
- Randomizes source IP address
- Randomizes source port
- Randomizes sequence numbers
- Continuous packet sending

### 2. RST Attack (`rst_attack.py`)
A script that performs a TCP RST (Reset) attack to forcibly terminate an existing TELNET connection between two hosts.

**Usage:**
```bash
python rst_attack.py
```
Required inputs:
- Server IP address
- Client IP address
- Server port
- Client port
- Next sequence number

**Features:**
- Spoofs packets to appear as coming from the server
- Uses RST flag to force connection termination
- Requires accurate sequence number for successful attack

### 3. Session Hijacking Attack (`session_hijacking_attack.py`)
Demonstrates TCP session hijacking by intercepting an existing TELNET connection and executing commands.

**Usage:**
```bash
python session_hijacking_attack.py
```
Required inputs:
- Server IP address
- Client IP address
- Server port
- Client port
- Next sequence number
- ACK number

**Note**: Requires netcat listener on port 9090 (`nc -lvn 9090`) to receive directory listing.

### 4. Remote Shell Attack (`remote_shell.py`)
Similar to the session hijacking attack but attempts to establish a reverse shell connection.

**Usage:**
```bash
python remote_shell.py
```
Required inputs:
- Server IP address
- Client IP address
- Server port
- Client port
- Next sequence number
- ACK number

**Note**: Requires netcat listener on port 9090 (`nc -lvn 9090`) to receive the reverse shell connection.


## Development Information

- Author: Ira Garrett
- Created: October 2025
- README file created with Copilot AI

## Network Configuration

The scripts are configured for a specific lab environment with the following default settings:
- Default target IP: 10.0.2.6
- Default attack listener IP: 10.0.2.15
- Default TELNET port: 23
- Default reverse shell/command output port: 9090